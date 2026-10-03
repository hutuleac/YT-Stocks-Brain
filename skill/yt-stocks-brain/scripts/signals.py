"""Signals — direction, not precision.

compute() reads kb/brain.db and compares the most recent window of briefs with the window
before it. Every measure is a share of briefs in its window, so a busier month doesn't look like
a trend. Seven lenses: attention gaining, early signals (new + spreading across channels),
sentiment turning, contested now, themes gaining, new connections, narratives (clusters of
entities that keep being named together, see narratives()).

render() turns that into the index.html Signals tab; snapshot() is the compact form saved weekly
to kb/signals/<ISO-week>.json so memos can say what changed since last week (see memo.py).
"""
import datetime as dt
import html
import itertools
import math
import sqlite3
from collections import defaultdict

RECENT_DAYS, PRIOR_DAYS, NEW_DAYS = 30, 60, 45
SKIP_KINDS = {"other", "group"}
SECTIONS = ("gaining", "early", "turning", "contested")
_POS = ("OWN", "BUY", "ADD", "POSITIVE", "LONG", "BULL")
_NEG = ("NEGATIVE", "BEAR", "SELL", "AVOID", "SHORT")
_CONV = {"high": 1.0, "medium": 0.67, "low": 0.33}
NARR_KINDS = {"company", "fund", "crypto", "commodity", "product", "unknown"}
HUB_SHARE, NARR_COSINE = 0.2, 0.4  # tuned by eye on 124 briefs; revisit as the library grows


def direction(stance, conviction):
    """Stance label -> signed weight in [-1, 1]; 0 = attention without a direction."""
    s = (stance or "").upper()
    sign = -1 if any(k in s for k in _NEG) else 1 if any(k in s for k in _POS) else 0
    return sign * _CONV.get((conviction or "").strip().lower(), 0.5)


def _lift(n_r, tot_r, n_p, tot_p):
    return ((n_r + 0.5) / max(tot_r, 1)) / ((n_p + 0.5) / max(tot_p, 1))


def _net(ws):
    d = [w for w in ws if w]
    return round(sum(d) / len(d), 2) if d else None


def clusters(ent_briefs, n_briefs):
    """{entity: set(brief ids)} -> [member lists], biggest first. Hubs (named in > HUB_SHARE of all
    briefs) co-occur with everything and would glue it into one blob, so they're left out. Edges:
    cosine overlap >= NARR_COSINE with >= 2 shared briefs; groups by weighted label propagation."""
    ents = sorted(k for k, s in ent_briefs.items() if 3 <= len(s) <= HUB_SHARE * n_briefs)
    w = defaultdict(dict)
    for a, b in itertools.combinations(ents, 2):
        n = len(ent_briefs[a] & ent_briefs[b])
        cos = n / math.sqrt(len(ent_briefs[a]) * len(ent_briefs[b]))
        if n >= 2 and cos >= NARR_COSINE:
            w[a][b] = w[b][a] = cos
    order = sorted(w, key=lambda k: (-len(ent_briefs[k]), k))
    lab = {k: k for k in w}
    for _ in range(20):  # ponytail: label propagation, swap for Louvain if groups start bleeding
        changed = False
        for k in order:
            score = defaultdict(float)
            for j, x in w[k].items():
                score[lab[j]] += x
            best = max(score.items(), key=lambda t: (t[1], t[0]))[0]
            changed |= best != lab[k]
            lab[k] = best
        if not changed:
            break
    groups = defaultdict(list)
    for k in order:
        groups[lab[k]].append(k)
    return sorted((g for g in groups.values() if len(g) >= 3), key=len, reverse=True)


def narratives(db, win, tot):
    """Clusters over all time; growth = share of briefs naming >= 2 members, recent vs prior."""
    eb, info, name = defaultdict(set), {}, {}
    for r in db.execute("""SELECT DISTINCT m.brief_id bid, m.entity_key k, e.name, e.kind, b.date, b.channel, b.title, b.html
                           FROM mentions m JOIN entities e ON e.key = m.entity_key JOIN briefs b ON b.id = m.brief_id"""):
        info[r["bid"]] = (r["date"], r["channel"], r["title"], r["html"])
        if r["kind"] in NARR_KINDS:
            eb[r["k"]].add(r["bid"])
            name[r["k"]] = r["name"]
    tags = defaultdict(set)
    for t in db.execute("SELECT DISTINCT brief_id, tag FROM theme_tags"):
        tags[t["brief_id"]].add(t["tag"])
    out = []
    for g in clusters(eb, len(info)):
        hits = [b for b in set().union(*(eb[k] for k in g)) if sum(b in eb[k] for k in g) >= 2]
        n = {"r": [b for b in hits if win(info[b][0]) == "r"], "p": [b for b in hits if win(info[b][0]) == "p"]}
        tag = max(sorted({t for b in hits for t in tags[b]}), key=lambda t: sum(t in tags[b] for b in hits), default=None)
        recent = sorted(n["r"], key=lambda b: info[b][0], reverse=True)[:6]
        out.append({"members": g, "names": [name[k] for k in g], "tag": tag, "briefs_all": len(hits),
                    "briefs": len(n["r"]), "prior": len(n["p"]),
                    "recent_pct": round(100 * len(n["r"]) / max(tot["r"], 1)),
                    "prior_pct": round(100 * len(n["p"]) / max(tot["p"], 1)),
                    "lift": round(_lift(len(n["r"]), tot["r"], len(n["p"]), tot["p"]), 2),
                    "rows": [dict(zip(("date", "channel", "title", "html"), info[b])) for b in recent]})
    return sorted(out, key=lambda x: (-x["briefs"], -x["briefs_all"]))


def same_narrative(a, b):
    """Membership drifts week to week; >= half overlap counts as the same narrative."""
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) >= 0.5


def compute(db_path):
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    dates = [r[0] for r in db.execute("SELECT date FROM briefs WHERE date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'")]
    if not dates:
        return None
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
            e["rows"].append({x: r[x] for x in ("date", "channel", "title", "html", "stance", "conviction", "blurb")})

    def lift(e):
        return _lift(len(e["r"]["b"]), tot["r"], len(e["p"]["b"]), tot["p"])

    def item(k):
        e = ent[k]
        dirs = e["r"]["w"]
        return {"key": k, "name": e["name"], "ticker": e["ticker"], "first_seen": e["first"],
                "briefs": len(e["r"]["b"]), "channels": len(e["r"]["c"]),
                "briefs_all": len(e["all"]), "channels_all": len(e["r"]["c"] | e["p"]["c"]),
                "lift": round(lift(e), 2), "sent_recent": _net(dirs), "sent_prior": _net(e["p"]["w"]),
                "sent_all": _net(dirs + e["p"]["w"]), "pos": sum(w > 0 for w in dirs), "neg": sum(w < 0 for w in dirs)}

    out = {"window": {"latest": latest.isoformat(), "recent_from": r0, "prior_from": p0,
                      "recent_briefs": tot["r"], "prior_briefs": tot["p"]}}
    out["gaining"] = [item(k) for k in sorted(
        (k for k, e in ent.items() if len(e["r"]["b"]) >= 3 and lift(e) >= 1.5 and e["first"] <= new0),
        key=lambda k: -lift(ent[k]) * math.log1p(len(ent[k]["r"]["b"])))[:15]]
    out["early"] = [item(k) for k in sorted(
        (k for k, e in ent.items() if e["first"] > new0 and len(e["all"]) >= 2 and len(e["r"]["c"] | e["p"]["c"]) >= 2),
        key=lambda k: (-len(ent[k]["r"]["c"] | ent[k]["p"]["c"]), -len(ent[k]["all"])))[:15]]
    turning = [item(k) for k, e in ent.items()
               if sum(map(bool, e["r"]["w"])) >= 2 and sum(map(bool, e["p"]["w"])) >= 2
               and abs(_net(e["r"]["w"]) - _net(e["p"]["w"])) >= 0.4]
    out["turning"] = sorted(turning, key=lambda i: -abs(i["sent_recent"] - i["sent_prior"]))[:15]
    out["contested"] = sorted((item(k) for k, e in ent.items() if sum(w > 0 for w in e["r"]["w"]) >= 1
                               and sum(w < 0 for w in e["r"]["w"]) >= 1 and sum(map(bool, e["r"]["w"])) >= 3),
                              key=lambda i: -i["briefs"])[:12]

    tags = defaultdict(lambda: {"r": set(), "p": set()})
    for t in db.execute("SELECT DISTINCT tt.tag, b.id, b.date FROM theme_tags tt JOIN briefs b ON b.id = tt.brief_id"):
        if win(t["date"]):
            tags[t["tag"]][win(t["date"])].add(t["id"])
    # denominator = tagged briefs only: briefs before Sept 2026 have no tags and would fake a rise
    ttot = {w: len(set().union(*(v[w] for v in tags.values()))) if tags else 0 for w in ("r", "p")}
    out["themes"] = sorted(({"tag": tag, "recent_pct": round(100 * len(v["r"]) / max(ttot["r"], 1)),
                             "prior_pct": round(100 * len(v["p"]) / max(ttot["p"], 1)),
                             "lift": round(_lift(len(v["r"]), ttot["r"], len(v["p"]), ttot["p"]), 2)}
                            for tag, v in tags.items() if len(v["r"]) >= 2), key=lambda x: -x["lift"])

    by_brief, bdate = defaultdict(set), {}
    for r in rows:
        if r["kind"] not in SKIP_KINDS:
            by_brief[r["bid"]].add(r["k"])
            bdate[r["bid"]] = r["date"]
    pairs_r, pairs_before = defaultdict(set), set()
    for bid, ks in by_brief.items():
        for a in ks:
            for b in ks:
                if a < b:
                    (pairs_r[(a, b)].add(bid) if bdate[bid] > r0 else pairs_before.add((a, b)))
    out["connections"] = [{"a": a, "b": b, "a_name": ent[a]["name"], "b_name": ent[b]["name"], "briefs": len(bs)}
                          for (a, b), bs in sorted(pairs_r.items(), key=lambda x: (-len(x[1]), x[0]))
                          if len(bs) >= 2 and (a, b) not in pairs_before][:15]

    out["narratives"] = narratives(db, win, tot)

    keys = {i["key"] for s in SECTIONS for i in out[s]} | {k for c in out["connections"] for k in (c["a"], c["b"])}
    claims = defaultdict(list)
    for c in db.execute("""SELECT ce.entity_key k, c.who, c.claim, c.target, c.by_when, b.date, b.html
                           FROM claim_entities ce JOIN claims c ON c.claim_id = ce.claim_id
                           JOIN briefs b ON b.id = c.brief_id WHERE b.date > ? ORDER BY b.date DESC""", (p0,)):
        if c["k"] in keys:
            claims[c["k"]].append(dict(c))
    out["detail"] = {k: {"rows": ent[k]["rows"][:6], "claims": claims.get(k, [])[:4]} for k in sorted(keys)}
    db.close()
    return out


def snapshot(data):
    """Compact weekly record: everything but the per-entity / per-narrative evidence rows."""
    snap = {k: v for k, v in data.items() if k != "detail"}
    snap["narratives"] = [{k: v for k, v in n.items() if k != "rows"} for n in data.get("narratives", [])]
    return snap


# ---------------------------------------------------------------- rendering (Signals tab)

def esc(s):
    return html.escape(str(s if s is not None else ""), quote=True)


def _arrow(x):
    return "&uarr;" if x > 0 else "&darr;" if x < 0 else "&rarr;"


def sent_label(x):
    if x is None:
        return "no stated view"
    word = "bullish" if x >= 0.25 else "bearish" if x <= -0.25 else "mixed"
    return f"{word} ({x:+.1f})"


def render(data, memos=()):
    """memos: [(label, href)] newest first, linked above the signals."""
    if not data:
        return '<p class="empty">No dated briefs yet.</p>'
    w = data["window"]

    def row(i, chips):
        d = data["detail"].get(i["key"], {"rows": [], "claims": []})
        tkr = f'<span class="tkr">{esc(i["ticker"])}</span>' if i["ticker"] else '<span class="tkr none">&mdash;</span>'
        items = []
        for r in d["rows"]:
            stance = " · ".join(x for x in (r["stance"], r["conviction"]) if x and x != "None")
            items.append(f'<li><span class="m-date">{esc(r["date"])}</span><span class="m-channel">{esc(r["channel"])}</span>'
                         f'<a href="{esc(r["html"])}">{esc(r["title"])}</a>'
                         + (f'<span class="m-stance">{esc(stance)}</span>' if stance else "")
                         + (f'<div class="m-blurb">{esc(r["blurb"])}</div>' if r["blurb"] else "") + "</li>")
        fwd = [f'<li><b>{esc(c["who"])}:</b> {esc(c["claim"])}'
               + (f' <span class="sig-by">{esc(c["by_when"])}</span>' if c["by_when"] else "") + "</li>"
               for c in d["claims"]]
        body = f'<ul class="mentions">{"".join(items)}</ul>' if items else ""
        if fwd:
            body += f'<div class="sig-fwd"><span>Where speakers see it heading</span><ul>{"".join(fwd)}</ul></div>'
        return (f'<details class="grp" data-search="{esc((i["name"] + " " + (i["ticker"] or "")).lower())}">'
                f'<summary>{tkr}<b>{esc(i["name"])}</b><span class="cnt">{chips}</span></summary>'
                f'<div class="grp-body">{body}</div></details>')

    def section(title, note, body):
        return (f'<h3 class="sig-h">{title}</h3><p class="sig-note">{note}</p>'
                + (body or '<p class="empty">Nothing crosses the bar this window.</p>'))

    out = []
    if memos:
        out.append('<div class="sig-memos"><span>Weekly memos</span>'
                   + " ".join(f'<a href="{esc(h)}">{esc(l)}</a>' for l, h in memos) + "</div>")
    out.append(f'<p class="sig-intro">Last {RECENT_DAYS} days ({esc(w["recent_from"])} to {esc(w["latest"])}, '
               f'{w["recent_briefs"]} briefs) vs the {PRIOR_DAYS} days before ({w["prior_briefs"]} briefs), normalized '
               f'per brief. This is what your sources are paying attention to and how they lean, not price action.</p>')
    out.append(section("Gaining attention", "Named in a rising share of briefs compared with the prior window.",
        "".join(row(i, f'{i["briefs"]} briefs · {i["channels"]} channels · &uarr; {i["lift"]:.1f}&times; · '
                       f'{sent_label(i["sent_recent"])}') for i in data["gaining"])))
    out.append(section("Early signals", f"First appeared in the last {NEW_DAYS} days and already named by more than one channel.",
        "".join(row(i, f'first seen {esc(i["first_seen"])} · {i["briefs_all"]} briefs · {i["channels_all"]} channels · '
                       f'{sent_label(i["sent_all"])}') for i in data["early"])))
    out.append(section("Sentiment turning", "Speakers' stated views moved meaningfully between windows.",
        "".join(row(i, f'{_arrow(i["sent_recent"] - i["sent_prior"])} {sent_label(i["sent_prior"])} &rarr; '
                       f'{sent_label(i["sent_recent"])}') for i in data["turning"])))
    out.append(section("Contested now", "Bulls and bears both on record this window. Disagreement is where the edge is.",
        "".join(row(i, f'{i["pos"]} positive · {i["neg"]} negative') for i in data["contested"])))
    out.append(section("Themes gaining", "Share of tagged briefs carrying each topic, this window vs the prior one.",
        '<ul class="rows sig-tags">' + "".join(
            f'<li data-search="{esc(t["tag"])}"><b>{esc(t["tag"])}</b><span>'
            f'{_arrow(t["lift"] - 1 if abs(t["lift"] - 1) >= 0.15 else 0)} {t["recent_pct"]}% of briefs '
            f'(was {t["prior_pct"]}%)</span></li>' for t in data["themes"]) + "</ul>" if data["themes"] else ""))
    out.append(section("New connections", "Pairs named together in several recent briefs that were never linked before.",
        '<ul class="rows">' + "".join(
            f'<li data-search="{esc((c["a_name"] + " " + c["b_name"]).lower())}"><b>{esc(c["a_name"])}</b> + '
            f'<b>{esc(c["b_name"])}</b><span class="m-date"> · {c["briefs"]} briefs</span></li>'
            for c in data["connections"]) + "</ul>" if data["connections"] else ""))
    out.append(section("Narratives", "Companies and assets that keep getting named together, grouped automatically. "
        "Share = briefs naming at least two of them. The biggest names (in over a fifth of all briefs) are left out "
        "because they show up everywhere.", "".join(narrative_row(n) for n in data.get("narratives", []))))
    return "".join(out)


def narrative_row(n):
    items = "".join(f'<li><span class="m-date">{esc(r["date"])}</span><span class="m-channel">{esc(r["channel"])}</span>'
                    f'<a href="{esc(r["html"])}">{esc(r["title"])}</a></li>' for r in n["rows"])
    move = _arrow(n["recent_pct"] - n["prior_pct"] if abs(n["recent_pct"] - n["prior_pct"]) >= 3 else 0)
    return (f'<details class="grp" data-search="{esc(" ".join(n["names"]).lower())}">'
            f'<summary><b>{" · ".join(esc(x) for x in n["names"][:3])}</b>'
            f'<span class="cnt">{move} {n["recent_pct"]}% of briefs (was {n["prior_pct"]}%) · {len(n["names"])} names'
            + (f' · {esc(n["tag"])}' if n["tag"] else "") + '</span></summary>'
            f'<div class="grp-body"><p class="m-blurb">{esc(", ".join(n["names"]))}</p>'
            f'<ul class="mentions">{items}</ul></div></details>')


if __name__ == "__main__":
    assert direction("OWNS", "High") == 1.0 and direction("NEGATIVE VIEW", "Low") == -0.33
    assert direction("CASUAL MENTION", "None") == 0 and direction("BUYING-ADDING", None) == 0.5
    assert _lift(4, 40, 2, 80) > 3
    # two tight groups + a hub named in most briefs -> two clusters, hub excluded
    toy = {"a1": {1, 2, 3}, "a2": {1, 2, 3}, "a3": {1, 2, 3, 4}, "b1": {5, 6, 7}, "b2": {5, 6, 7}, "b3": {5, 6, 8},
           "hub": set(range(1, 9))}
    got = sorted(sorted(g) for g in clusters(toy, 20))
    assert got == [["a1", "a2", "a3"], ["b1", "b2", "b3"]], got
    assert same_narrative(["a", "b", "c"], ["a", "b", "c", "d"]) and not same_narrative(["a", "b"], ["c", "d"])
    print("signals selftest ok")
