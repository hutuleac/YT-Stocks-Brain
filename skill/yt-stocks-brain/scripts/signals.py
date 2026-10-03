"""Signals tab for index.html — direction, not precision.

Reads kb/brain.db (built just before) and compares the most recent window of briefs with the
window before it. Every measure is a share of briefs in its window, so a busier month doesn't
look like a trend. Six lenses: attention gaining, early signals (new + spreading across
channels), sentiment turning, contested now, themes gaining, new connections. Each entity row
expands to its recent stances and the forward-looking claims attached to it.
"""
import datetime as dt
import html
import math
import sqlite3
from collections import defaultdict

RECENT_DAYS, PRIOR_DAYS, NEW_DAYS = 30, 60, 45
SKIP_KINDS = {"other", "group"}
_POS = ("OWN", "BUY", "ADD", "POSITIVE", "LONG", "BULL")
_NEG = ("NEGATIVE", "BEAR", "SELL", "AVOID", "SHORT")
_CONV = {"high": 1.0, "medium": 0.67, "low": 0.33}


def direction(stance, conviction):
    """Stance label -> signed weight in [-1, 1]; 0 = attention without a direction."""
    s = (stance or "").upper()
    sign = -1 if any(k in s for k in _NEG) else 1 if any(k in s for k in _POS) else 0
    return sign * _CONV.get((conviction or "").strip().lower(), 0.5)


def esc(s):
    return html.escape(str(s or ""), quote=True)


def _lift(n_r, tot_r, n_p, tot_p):
    return ((n_r + 0.5) / max(tot_r, 1)) / ((n_p + 0.5) / max(tot_p, 1))


def _net(ws):
    d = [w for w in ws if w]
    return sum(d) / len(d) if d else None


def _arrow(x):
    return "&uarr;" if x > 0 else "&darr;" if x < 0 else "&rarr;"


def _sent(x):
    if x is None:
        return "no stated view"
    word = "bullish" if x >= 0.25 else "bearish" if x <= -0.25 else "mixed"
    return f"{word} ({x:+.1f})"


def render(db_path):
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    dates = [r[0] for r in db.execute("SELECT date FROM briefs WHERE date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'")]
    if not dates:
        return '<p class="empty">No dated briefs yet.</p>'
    latest = dt.date.fromisoformat(max(dates))
    r0 = (latest - dt.timedelta(days=RECENT_DAYS)).isoformat()
    p0 = (latest - dt.timedelta(days=RECENT_DAYS + PRIOR_DAYS)).isoformat()
    new0 = (latest - dt.timedelta(days=NEW_DAYS)).isoformat()
    win = lambda d: "r" if d > r0 else "p" if d > p0 else None
    tot = defaultdict(int)
    for d in dates:
        if win(d):
            tot[win(d)] += 1

    rows = db.execute("""
        SELECT m.entity_key k, e.name, e.ticker, e.kind, b.date, b.channel, b.title, b.html,
               m.stance, m.conviction, m.blurb, b.id bid
        FROM mentions m JOIN entities e ON e.key = m.entity_key JOIN briefs b ON b.id = m.brief_id
        ORDER BY b.date DESC""").fetchall()
    ent = {}
    for r in rows:
        if r["kind"] in SKIP_KINDS:
            continue
        e = ent.setdefault(r["k"], {"name": r["name"], "ticker": r["ticker"], "first": r["date"],
                                    "all": set(), "rows": [],
                                    "r": {"b": set(), "c": set(), "w": []}, "p": {"b": set(), "c": set(), "w": []}})
        e["first"] = min(e["first"], r["date"])
        e["all"].add(r["bid"])
        w = win(r["date"])
        if w:
            e[w]["b"].add(r["bid"])
            e[w]["c"].add(r["channel"])
            e[w]["w"].append(direction(r["stance"], r["conviction"]))
        if w == "r":
            e["rows"].append(r)
    claims = defaultdict(list)
    for c in db.execute("""SELECT ce.entity_key k, c.who, c.claim, c.target, c.by_when, b.date
                           FROM claim_entities ce JOIN claims c ON c.claim_id = ce.claim_id
                           JOIN briefs b ON b.id = c.brief_id WHERE b.date > ? ORDER BY b.date DESC""", (p0,)):
        claims[c["k"]].append(c)

    def row(k, chips):
        e = ent[k]
        tkr = f'<span class="tkr">{esc(e["ticker"])}</span>' if e["ticker"] else '<span class="tkr none">&mdash;</span>'
        items = []
        for r in e["rows"][:6]:
            stance = " · ".join(x for x in (r["stance"], r["conviction"]) if x and x != "None")
            items.append(f'<li><span class="m-date">{esc(r["date"])}</span><span class="m-channel">{esc(r["channel"])}</span>'
                         f'<a href="{esc(r["html"])}">{esc(r["title"])}</a>'
                         + (f'<span class="m-stance">{esc(stance)}</span>' if stance else "")
                         + (f'<div class="m-blurb">{esc(r["blurb"])}</div>' if r["blurb"] else "") + "</li>")
        fwd = [f'<li><b>{esc(c["who"])}:</b> {esc(c["claim"])}'
               + (f' <span class="sig-by">{esc(c["by_when"])}</span>' if c["by_when"] else "") + "</li>"
               for c in claims.get(k, [])[:4]]
        body = f'<ul class="mentions">{"".join(items)}</ul>' if items else ""
        if fwd:
            body += f'<div class="sig-fwd"><span>Where speakers see it heading</span><ul>{"".join(fwd)}</ul></div>'
        search = esc(f'{e["name"]} {e["ticker"] or ""}'.lower())
        return (f'<details class="grp" data-search="{search}"><summary>{tkr}<b>{esc(e["name"])}</b>'
                f'<span class="cnt">{chips}</span></summary><div class="grp-body">{body}</div></details>')

    def section(title, note, body):
        return (f'<h3 class="sig-h">{title}</h3><p class="sig-note">{note}</p>'
                + (body or '<p class="empty">Nothing crosses the bar this window.</p>'))

    out = [f'<p class="sig-intro">Last {RECENT_DAYS} days ({esc(r0)} to {esc(latest.isoformat())}, {tot["r"]} briefs) '
           f'vs the {PRIOR_DAYS} days before ({tot["p"]} briefs), normalized per brief. This is what your '
           f'sources are paying attention to and how they lean, not price action.</p>']

    def lift(e):
        return _lift(len(e["r"]["b"]), tot["r"], len(e["p"]["b"]), tot["p"])

    gaining = sorted((k for k, e in ent.items() if len(e["r"]["b"]) >= 3 and lift(e) >= 1.5 and e["first"] <= new0),
                     key=lambda k: (-lift(ent[k]) * math.log1p(len(ent[k]["r"]["b"]))))[:15]
    out.append(section("Gaining attention", "Named in a rising share of briefs compared with the prior window.",
        "".join(row(k, f'{len(ent[k]["r"]["b"])} briefs · {len(ent[k]["r"]["c"])} channels · '
                       f'{_arrow(1)} {lift(ent[k]):.1f}&times; · {_sent(_net(ent[k]["r"]["w"]))}') for k in gaining)))

    early = sorted((k for k, e in ent.items() if e["first"] > new0 and len(e["all"]) >= 2
                    and len(e["r"]["c"] | e["p"]["c"]) >= 2),
                   key=lambda k: (-len(ent[k]["r"]["c"] | ent[k]["p"]["c"]), -len(ent[k]["all"])))[:15]
    out.append(section("Early signals", f"First appeared in the last {NEW_DAYS} days and already named by more than one channel.",
        "".join(row(k, f'first seen {esc(ent[k]["first"])} · {len(ent[k]["all"])} briefs · '
                       f'{len(ent[k]["r"]["c"] | ent[k]["p"]["c"])} channels · {_sent(_net(ent[k]["r"]["w"] + ent[k]["p"]["w"]))}')
                for k in early)))

    turning = []
    for k, e in ent.items():
        nr, np_ = _net(e["r"]["w"]), _net(e["p"]["w"])
        if nr is not None and np_ is not None and sum(map(bool, e["r"]["w"])) >= 2 \
                and sum(map(bool, e["p"]["w"])) >= 2 and abs(nr - np_) >= 0.4:
            turning.append((k, nr, np_))
    turning.sort(key=lambda t: -abs(t[1] - t[2]))
    out.append(section("Sentiment turning", "Speakers' stated views moved meaningfully between windows.",
        "".join(row(k, f'{_arrow(nr - np_)} {_sent(np_)} &rarr; {_sent(nr)}') for k, nr, np_ in turning[:15])))

    contested = sorted((k for k, e in ent.items() if sum(w > 0 for w in e["r"]["w"]) >= 1
                        and sum(w < 0 for w in e["r"]["w"]) >= 1 and sum(map(bool, e["r"]["w"])) >= 3),
                       key=lambda k: -len(ent[k]["r"]["b"]))[:12]
    out.append(section("Contested now", "Bulls and bears both on record this window. Disagreement is where the edge is.",
        "".join(row(k, f'{sum(w > 0 for w in ent[k]["r"]["w"])} positive · {sum(w < 0 for w in ent[k]["r"]["w"])} negative')
                for k in contested)))

    tags = defaultdict(lambda: {"r": set(), "p": set()})
    for t in db.execute("SELECT DISTINCT tt.tag, b.id, b.date FROM theme_tags tt JOIN briefs b ON b.id = tt.brief_id"):
        if win(t["date"]):
            tags[t["tag"]][win(t["date"])].add(t["id"])
    # denominator = tagged briefs only: briefs before Sept 2026 have no tags and would fake a rise
    ttot = {w: len(set().union(*(v[w] for v in tags.values()))) if tags else 0 for w in ("r", "p")}
    tag_rows = sorted(((tag, len(v["r"]), len(v["p"]), _lift(len(v["r"]), ttot["r"], len(v["p"]), ttot["p"]))
                       for tag, v in tags.items() if len(v["r"]) >= 2), key=lambda x: -x[3])
    out.append(section("Themes gaining", "Share of tagged briefs carrying each topic, this window vs the prior one.",
        '<ul class="rows sig-tags">' + "".join(
            f'<li data-search="{esc(tag)}"><b>{esc(tag)}</b><span>{_arrow(lf - 1 if abs(lf - 1) >= 0.15 else 0)} '
            f'{100 * nr / max(ttot["r"], 1):.0f}% of briefs (was {100 * np_ / max(ttot["p"], 1):.0f}%)</span></li>'
            for tag, nr, np_, lf in tag_rows) + "</ul>" if tag_rows else ""))

    pairs_r, pairs_before = defaultdict(set), set()
    by_brief = defaultdict(set)
    bdate = {}
    for r in rows:
        if r["kind"] not in SKIP_KINDS:
            by_brief[r["bid"]].add(r["k"])
            bdate[r["bid"]] = r["date"]
    for bid, ks in by_brief.items():
        for a in ks:
            for b in ks:
                if a < b:
                    if bdate[bid] > r0:
                        pairs_r[(a, b)].add(bid)
                    else:
                        pairs_before.add((a, b))
    new_pairs = sorted(((p, len(bs)) for p, bs in pairs_r.items() if len(bs) >= 2 and p not in pairs_before),
                       key=lambda x: -x[1])[:15]
    out.append(section("New connections", "Pairs named together in several recent briefs that were never linked before.",
        '<ul class="rows">' + "".join(
            f'<li data-search="{esc((ent[a]["name"] + " " + ent[b]["name"]).lower())}"><b>{esc(ent[a]["name"])}</b> + '
            f'<b>{esc(ent[b]["name"])}</b><span class="m-date"> · {n} briefs</span></li>' for (a, b), n in new_pairs)
        + "</ul>" if new_pairs else ""))
    db.close()
    return "".join(out)


if __name__ == "__main__":
    assert direction("OWNS", "High") == 1.0 and direction("NEGATIVE VIEW", "Low") == -0.33
    assert direction("CASUAL MENTION", "None") == 0 and direction("BUYING-ADDING", None) == 0.5
    assert _lift(4, 40, 2, 80) > 3
    print("signals selftest ok")
