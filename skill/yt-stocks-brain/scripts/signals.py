"""Signals — direction, not precision. Spot ideas before they go mainstream.

compute() reads kb/brain.db, market briefs only (dev/life content would dilute every share).
Windows are counted in briefs, not days: the latest RECENT_N briefs vs the PRIOR_N before them,
so a slow week isn't a fall and backfilled old videos don't move the "recent" window.

The unit is the narrative: entities that keep getting named together (see clusters()). Each one
gets a vector: convergence (briefs naming >= 2 members), growth (recent share vs prior share) and
direction (net stance of those mentions, recent vs prior). Rows carry the converging information
itself: the theme titles and leads where the members were named. Narratives growing but not yet
mainstream are "emerging"; the rest are "established". "New names" catches single entities first
seen in the recent window and already in >= 2 briefs, before they cluster with anything.

render() turns that into the index.html Signals tab; snapshot() is the compact form embedded in
weekly memos so they can say what changed since last week (see memo.py).
"""
import html
import itertools
import math
import sqlite3
from collections import defaultdict

RECENT_N, PRIOR_N = 30, 90  # briefs, newest first; prior = the PRIOR_N before the recent ones
EMERGE_LIFT, MAINSTREAM_PCT = 1.25, 30  # emerging = recent share >= 1.25x prior and under 30% of briefs
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


def same_narrative(a, b):
    """Membership drifts week to week; >= half overlap counts as the same narrative."""
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) >= 0.5


def compute(db_path):
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    briefs = db.execute("""SELECT id, date, channel, title, html FROM briefs
                           WHERE date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
                           AND COALESCE(category, 'market') = 'market' ORDER BY date, id""").fetchall()
    if not briefs:
        db.close()
        return None
    info = {b["id"]: dict(b) for b in briefs}
    order = [b["id"] for b in briefs]
    pos = {b: i for i, b in enumerate(order)}
    recent, prior = set(order[-RECENT_N:]), set(order[-RECENT_N - PRIOR_N:-RECENT_N])
    win = lambda b: "r" if b in recent else "p" if b in prior else None
    tot = {"r": len(recent), "p": len(prior)}

    eb, by_ent, name, ticker = defaultdict(set), defaultdict(list), {}, {}
    for m in db.execute("""SELECT m.brief_id bid, m.theme_id tid, m.entity_key k, e.name, e.ticker, e.kind,
                                  m.stance, m.conviction, m.blurb
                           FROM mentions m JOIN entities e ON e.key = m.entity_key"""):
        if m["bid"] in info and m["kind"] in NARR_KINDS:
            eb[m["k"]].add(m["bid"])
            by_ent[m["k"]].append(m)
            name[m["k"]], ticker[m["k"]] = m["name"], m["ticker"]
    themes = {(t["brief_id"], t["theme_id"]): (t["title"], t["lead"])
              for t in db.execute("SELECT brief_id, theme_id, title, lead FROM themes")}
    ttags = defaultdict(set)
    for t in db.execute("SELECT brief_id, theme_id, tag FROM theme_tags"):
        ttags[(t["brief_id"], t["theme_id"])].add(t["tag"])
    claims = defaultdict(list)
    for c in db.execute("""SELECT ce.entity_key k, c.brief_id bid, c.who, c.claim, c.by_when
                           FROM claim_entities ce JOIN claims c ON c.claim_id = ce.claim_id"""):
        if c["bid"] in info:
            claims[c["k"]].append(dict(c))

    def evidence(keys, bids, limit=8):
        """The information itself: per brief (newest first) the themes where these names came up,
        plus each name's own blurb; then forward-looking claims about them."""
        rows = defaultdict(lambda: {"themes": {}, "notes": []})
        for k in keys:
            for m in by_ent[k]:
                if m["bid"] in bids:
                    r = rows[m["bid"]]
                    if (m["bid"], m["tid"]) in themes:
                        r["themes"][m["tid"]] = themes[(m["bid"], m["tid"])]
                    if m["blurb"]:
                        r["notes"].append(f'{name[k]}: {m["blurb"]}')
        out = [{**{x: info[b][x] for x in ("date", "channel", "title", "html")},
                "themes": list(rows[b]["themes"].values()), "notes": rows[b]["notes"]}
               for b in sorted(rows, key=pos.get, reverse=True)[:limit]]
        fwd, seen = [], set()
        for c in sorted((c for k in keys for c in claims[k] if c["bid"] in bids), key=lambda c: -pos[c["bid"]]):
            if c["claim"] not in seen:
                seen.add(c["claim"])
                fwd.append({x: c[x] for x in ("who", "claim", "by_when")})
        return out, fwd[:4]

    def stances(keys, bids):
        w = {"r": [], "p": []}
        for k in keys:
            for m in by_ent[k]:
                if m["bid"] in bids and win(m["bid"]):
                    w[win(m["bid"])].append(direction(m["stance"], m["conviction"]))
        return _net(w["r"]), _net(w["p"])

    narr = []
    for g in clusters(eb, len(order)):
        hits = {b for b in set().union(*(eb[k] for k in g)) if sum(b in eb[k] for k in g) >= 2}
        n_r, n_p = sum(win(b) == "r" for b in hits), sum(win(b) == "p" for b in hits)
        tags = [t for k in g for m in by_ent[k] if m["bid"] in hits for t in ttags[(m["bid"], m["tid"])]]
        rows, fwd = evidence(g, hits)
        sr, sp = stances(g, hits)
        n = {"members": g, "names": [name[k] for k in g], "tag": max(sorted(set(tags)), key=tags.count, default=None),
             "briefs_all": len(hits), "briefs": n_r, "prior": n_p,
             "recent_pct": round(100 * n_r / max(tot["r"], 1)), "prior_pct": round(100 * n_p / max(tot["p"], 1)),
             "lift": round(_lift(n_r, tot["r"], n_p, tot["p"]), 2), "sent_recent": sr, "sent_prior": sp,
             "rows": rows, "claims": fwd}
        n["emerging"] = n_r >= 2 and n["lift"] >= EMERGE_LIFT and n["recent_pct"] < MAINSTREAM_PCT
        narr.append(n)
    narr.sort(key=lambda n: (-n["emerging"], -(n["lift"] * math.log1p(n["briefs"])) if n["emerging"] else -n["briefs_all"]))

    new, clustered = [], {k for n in narr for k in n["members"]}
    for k, bs in eb.items():
        if len(bs) >= 2 and bs <= recent and k not in clustered:
            rows, fwd = evidence([k], bs, 6)
            sr, _ = stances([k], bs)
            new.append({"key": k, "name": name[k], "ticker": ticker[k], "briefs": len(bs),
                        "first_seen": info[min(bs, key=pos.get)]["date"], "sent": sr, "rows": rows, "claims": fwd})
    new.sort(key=lambda i: (-i["briefs"], i["first_seen"]))

    rs = sorted(recent, key=pos.get)
    out = {"window": {"latest": info[order[-1]]["date"], "recent_from": info[rs[0]]["date"],
                      "recent_briefs": tot["r"], "prior_briefs": tot["p"]},
           "narratives": narr, "new_names": new[:15]}
    db.close()
    return out


def snapshot(data):
    """Compact weekly record for memos: everything but the evidence rows."""
    strip = lambda xs: [{k: v for k, v in x.items() if k not in ("rows", "claims")} for x in xs]
    return {"window": data["window"], "narratives": strip(data["narratives"]), "new_names": strip(data["new_names"])}


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


def _plain(s, cap=260):
    s = (s or "").replace("**", "").strip()
    return s if len(s) <= cap else s[:cap].rsplit(" ", 1)[0] + "…"


def _body(rows, claims, notes):
    items = []
    for r in rows:
        th = "".join(f'<div class="sig-theme"><b>{esc(_plain(t, 200))}</b> {esc(_plain(l))}</div>' for t, l in r["themes"])
        nt = "".join(f'<div class="m-blurb">{esc(x)}</div>' for x in r["notes"]) if notes else ""
        items.append(f'<li><span class="m-date">{esc(r["date"])}</span><span class="m-channel">{esc(r["channel"])}</span>'
                     f'<a href="{esc(r["html"])}">{esc(r["title"])}</a>{th}{nt}</li>')
    out = f'<ul class="mentions">{"".join(items)}</ul>' if items else ""
    if claims:
        out += ('<div class="sig-fwd"><span>Where speakers see it heading</span><ul>' + "".join(
            f'<li><b>{esc(c["who"])}:</b> {esc(c["claim"])}'
            + (f' <span class="sig-by">{esc(c["by_when"])}</span>' if c["by_when"] else "") + "</li>" for c in claims)
            + "</ul></div>")
    return out


def narrative_row(n):
    move = _arrow(n["recent_pct"] - n["prior_pct"] if abs(n["recent_pct"] - n["prior_pct"]) >= 3 else 0)
    sent = sent_label(n["sent_recent"])
    if n["sent_recent"] is not None and n["sent_prior"] is not None and abs(n["sent_recent"] - n["sent_prior"]) >= 0.4:
        sent += f' {_arrow(n["sent_recent"] - n["sent_prior"])} was {sent_label(n["sent_prior"])}'
    return (f'<details class="grp" data-search="{esc(" ".join(n["names"]).lower())}">'
            f'<summary><b>{" · ".join(esc(x) for x in n["names"][:3])}</b>'
            f'<span class="cnt">{move} {n["recent_pct"]}% of recent briefs (was {n["prior_pct"]}%) · '
            f'{n["briefs_all"]} briefs · {sent}' + (f' · {esc(n["tag"])}' if n["tag"] else "") + '</span></summary>'
            f'<div class="grp-body"><p class="m-blurb">{esc(", ".join(n["names"]))}</p>'
            f'{_body(n["rows"], n["claims"], notes=False)}</div></details>')


def name_row(i):
    tkr = f'<span class="tkr">{esc(i["ticker"])}</span>' if i["ticker"] else '<span class="tkr none">&mdash;</span>'
    return (f'<details class="grp" data-search="{esc((i["name"] + " " + (i["ticker"] or "")).lower())}">'
            f'<summary>{tkr}<b>{esc(i["name"])}</b><span class="cnt">first seen {esc(i["first_seen"])} · '
            f'{i["briefs"]} briefs · {sent_label(i["sent"])}</span></summary>'
            f'<div class="grp-body">{_body(i["rows"], i["claims"], notes=True)}</div></details>')


def render(data, memos=()):
    """memos: [(label, href)] newest first, linked above the signals."""
    if not data:
        return '<p class="empty">No dated briefs yet.</p>'
    w = data["window"]
    emerging = [n for n in data["narratives"] if n["emerging"]]
    rest = [n for n in data["narratives"] if not n["emerging"]]

    def section(title, note, body):
        return (f'<h3 class="sig-h">{title}</h3><p class="sig-note">{note}</p>'
                + (body or '<p class="empty">Nothing crosses the bar right now.</p>'))

    out = []
    if memos:
        out.append('<div class="sig-memos"><span>Weekly memos</span>'
                   + " ".join(f'<a href="{esc(h)}">{esc(l)}</a>' for l, h in memos) + "</div>")
    out.append(f'<p class="sig-intro">Ideas your sources are converging on, from market briefs only. A narrative is a group '
               f'of companies and assets that keep getting named together; open one to read the information behind it. '
               f'Growth compares the latest {w["recent_briefs"]} briefs ({esc(w["recent_from"])} to {esc(w["latest"])}) '
               f'with the {w["prior_briefs"]} before them. It shows attention and lean, not price action.</p>')
    out.append(section("Emerging narratives", f"Taking a growing share of recent briefs, not yet mainstream "
                       f"(under {MAINSTREAM_PCT}% of them).", "".join(narrative_row(n) for n in emerging)))
    out.append(section("New names", f"First named in the latest {w['recent_briefs']} briefs and already in two or more. "
                       "Too new to cluster with anything yet.", "".join(name_row(i) for i in data["new_names"])))
    if rest:
        out.append(f'<details class="sig-more"><summary><h3 class="sig-h">Established narratives ({len(rest)})</h3></summary>'
                   f'<p class="sig-note">Steady, fading or already mainstream. Sorted by how many briefs back them.</p>'
                   + "".join(narrative_row(n) for n in rest) + "</details>")
    return "".join(out)


def _e2e():
    """40 market briefs + 1 dev: a1-a3 cluster mostly in the recent window -> emerging; b1-b3 spread
    evenly -> established; x first named in 2 recent briefs -> new name; dev brief ignored."""
    import os
    import tempfile
    path = os.path.join(tempfile.mkdtemp(), "t.db")
    db = sqlite3.connect(path)
    db.executescript("""CREATE TABLE briefs (id, date, channel, title, html, category);
        CREATE TABLE entities (key, name, ticker, kind); CREATE TABLE themes (brief_id, theme_id, title, lead);
        CREATE TABLE mentions (brief_id, theme_id, entity_key, stance, conviction, blurb);
        CREATE TABLE theme_tags (brief_id, theme_id, tag); CREATE TABLE claims (claim_id, brief_id, who, claim, by_when);
        CREATE TABLE claim_entities (claim_id, entity_key);""")
    for i in range(40):
        db.execute("INSERT INTO briefs VALUES (?,?,?,?,?,?)", (f"v{i:02d}", f"2026-01-{1 + i % 28:02d}" if i < 28
                   else f"2026-02-{i - 27:02d}", "C", f"T{i}", f"b{i}.html", "market"))
        db.execute("INSERT INTO themes VALUES (?,?,?,?)", (f"v{i:02d}", "t1", f"Theme {i}", "**Lead** text"))
    db.execute("INSERT INTO briefs VALUES ('dev', '2026-02-12', 'C', 'D', 'd.html', 'dev')")
    for k in ("a1", "a2", "a3", "b1", "b2", "b3", "x", "dx"):
        db.execute("INSERT INTO entities VALUES (?,?,?,?)", (k, k.upper(), None, "company"))
    def m(bid, k, stance="BULLISH"):
        db.execute("INSERT INTO mentions VALUES (?,?,?,?,?,?)", (bid, "t1", k, stance, "high", f"{k} note"))
    for b in ("v34", "v35", "v36", "v37"):
        for k in ("a1", "a2", "a3"):
            m(b, k)
    for b in ("v02", "v12", "v22", "v32"):
        for k in ("b1", "b2", "b3"):
            m(b, k, "BEARISH")
    m("v38", "x"), m("v39", "x"), m("dev", "dx"), m("v39", "dx")
    db.execute("INSERT INTO claims VALUES ('c1', 'v39', 'Ann', 'X doubles', '2027')")
    db.execute("INSERT INTO claim_entities VALUES ('c1', 'x')")
    db.commit()
    db.close()
    d = compute(path)
    em = [n["names"] for n in d["narratives"] if n["emerging"]]
    assert em == [["A1", "A2", "A3"]], em
    assert [n["names"] for n in d["narratives"] if not n["emerging"]] == [["B1", "B2", "B3"]]
    assert [i["name"] for i in d["new_names"]] == ["X"], d["new_names"]  # dx: one market brief only
    x = d["new_names"][0]
    assert x["first_seen"] == "2026-02-11" and x["claims"][0]["claim"] == "X doubles" and x["sent"] == 1.0
    assert d["narratives"][0]["rows"][0]["themes"] == [("Theme 37", "**Lead** text")]
    assert d["window"]["recent_briefs"] == 30 and "rows" not in snapshot(d)["narratives"][0]
    assert "Lead text" in render(d)


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
    _e2e()
    print("signals selftest ok")
