"""Weekly insight memo — what changed in the library, written for direction, not precision.

  python3 memo.py context   # rebuilds nothing; reads kb/brain.db, prints the evidence pack and
                            # creates memos/<ISO-week>.json (skeleton + embedded signals snapshot)
  # ... fill summary / insights / watch in that JSON (see SKILL.md "Weekly memo") ...
  python3 memo.py render memos/<ISO-week>.json   # -> memos/<ISO-week>.html + reindex

The "What moved since the last memo" section is computed, never written by hand: this memo's
embedded snapshot is diffed against the previous memo's. Run from the repo root.
"""
import datetime as dt
import glob
import json
import os
import sys

import signals
from build_kb import DB_PATH

MEMO_DIR = "memos"


def week_key(d=None):
    y, w, _ = (d or dt.date.today()).isocalendar()
    return f"{y}-W{w:02d}"


def memo_paths():
    """Memo JSON paths, newest week first."""
    return sorted(glob.glob(os.path.join(MEMO_DIR, "*-W*.json")), reverse=True)


def is_due(today=None):
    """A memo is due when none exists for this ISO week and the last one is >= 6 days old."""
    paths = memo_paths()
    if not paths:
        return True
    last = json.load(open(paths[0], encoding="utf-8"))
    if last.get("week") == week_key(today):
        return False
    return (today or dt.date.today()) - dt.date.fromisoformat(last["date"]) >= dt.timedelta(days=6)


def diff(cur, prev):
    """Signals snapshot vs previous one -> {section: {"new": [names], "dropped": [names]}, ...}."""
    out = {}
    for s in signals.SECTIONS:
        now = {i["key"]: i["name"] for i in cur.get(s, [])}
        before = {i["key"]: i["name"] for i in (prev or {}).get(s, [])}
        out[s] = {"new": [now[k] for k in now if k not in before],
                  "dropped": [before[k] for k in before if k not in now]}
    pt = {t["tag"]: t for t in (prev or {}).get("themes", [])}
    out["themes"] = [f'{t["tag"]} {pt[t["tag"]]["recent_pct"]}% → {t["recent_pct"]}%' for t in cur.get("themes", [])
                     if t["tag"] in pt and abs(t["recent_pct"] - pt[t["tag"]]["recent_pct"]) >= 5]
    pc = {(c["a"], c["b"]) for c in (prev or {}).get("connections", [])}
    out["connections"] = [f'{c["a_name"]} + {c["b_name"]}' for c in cur.get("connections", []) if (c["a"], c["b"]) not in pc]
    pn, label = (prev or {}).get("narratives", []), lambda n: " · ".join(n["names"][:3])
    out["narratives"] = []
    for n in cur.get("narratives", []):
        was = next((p for p in pn if signals.same_narrative(n["members"], p["members"])), None)
        if not was:
            out["narratives"].append(f'new: {label(n)}')
        elif abs(n["recent_pct"] - was["recent_pct"]) >= 5:
            out["narratives"].append(f'{label(n)} {was["recent_pct"]}% → {n["recent_pct"]}%')
    out["narratives"] += [f'faded: {label(p)}' for p in pn
                          if not any(signals.same_narrative(p["members"], n["members"]) for n in cur.get("narratives", []))]
    return out


def _previous(week):
    for p in memo_paths():
        m = json.load(open(p, encoding="utf-8"))
        if m.get("week") < week:
            return m
    return None


def context():
    import sqlite3
    data = signals.compute(DB_PATH)
    if not data:
        sys.exit("no dated briefs in kb/brain.db — run generate.py --reindex first")
    today = dt.date.today()
    week = week_key(today)
    prev = _previous(week)
    since = prev["date"] if prev else data["window"]["recent_from"]
    path = os.path.join(MEMO_DIR, f"{week}.json")
    os.makedirs(MEMO_DIR, exist_ok=True)
    if not os.path.exists(path):
        json.dump({"week": week, "date": today.isoformat(), "since": since, "title": "", "summary": "",
                   "insights": [{"title": "", "bullets": [], "evidence": []}], "watch": [{"title": "", "why": ""}],
                   "signals": signals.snapshot(data)}, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    d = diff(signals.snapshot(data), prev and prev.get("signals"))

    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    print(f"# Memo context {week} — briefs since {since} (window {data['window']['recent_from']}..{data['window']['latest']})\n")
    print(f"Skeleton: {path}\n\n## New briefs since last memo")
    for b in db.execute("SELECT date, channel, title, html FROM briefs WHERE date > ? ORDER BY date", (since,)):
        print(f"- {b['date']} {b['channel']}: {b['title']} ({b['html']})")
    print("\n## What moved since the last memo" + ("" if prev else " (first memo: everything is new)"))
    for k, v in d.items():
        print(f"- {k}: {v}")
    for s in signals.SECTIONS:
        print(f"\n## {s}")
        for i in data[s]:
            print(f"- {i['name']} ({i['ticker'] or '-'}): briefs {i['briefs']}, channels {i['channels']}, lift {i['lift']}, "
                  f"sentiment {i['sent_prior']} -> {i['sent_recent']}, +{i['pos']}/-{i['neg']}, first {i['first_seen']}")
            det = data["detail"].get(i["key"], {})
            for r in det.get("rows", [])[:3]:
                print(f"    · {r['date']} {r['channel']} [{r['stance']}] {r['blurb']} ({r['html']})")
            for c in det.get("claims", [])[:2]:
                print(f"    → {c['who']}: {c['claim']} ({c['by_when'] or 'no date'})")
    print("\n## themes (share of tagged briefs, recent vs prior)")
    for t in data["themes"]:
        print(f"- {t['tag']}: {t['prior_pct']}% -> {t['recent_pct']}%")
    print("\n## new connections")
    for c in data["connections"]:
        print(f"- {c['a_name']} + {c['b_name']}: {c['briefs']} briefs")
    print("\n## narratives (entity clusters; share of briefs naming >= 2 members, prior -> recent)")
    for n in data["narratives"]:
        print(f"- {', '.join(n['names'])} [{n['tag']}]: {n['prior_pct']}% -> {n['recent_pct']}% ({n['briefs']} recent briefs)")
    print("\n## hot takes since last memo")
    for t in db.execute("""SELECT t.take, t.cite, b.html FROM takes t JOIN briefs b ON b.id = t.brief_id
                           WHERE b.date > ? ORDER BY b.date DESC LIMIT 40""", (since,)):
        print(f"- {t['take']} {t['cite']} ({t['html']})")


def render(path):
    import generate as g
    m = json.load(open(path, encoding="utf-8"))
    prev = _previous(m["week"])
    d = diff(m["signals"], prev and prev.get("signals"))
    esc = g.esc
    titles = {b["html"]: f'{b["channel"]}: {b["title"]}' for b in json.load(open("library.json", encoding="utf-8"))["briefs"]}

    def link(ev):
        return f'<a href="../{esc(ev)}">{esc(titles.get(ev, ev))}</a>'

    insights = "".join(
        f'<div class="card" style="margin-top:16px;"><h3 class="memo-h">{g.emph(i["title"], auto=False)}</h3>'
        f'{g.render_snapshot(i.get("bullets", []))}'
        + (f'<p class="memo-ev">Evidence: {" · ".join(link(e) for e in i.get("evidence", []))}</p>' if i.get("evidence") else "")
        + "</div>" for i in m["insights"] if i.get("title"))
    watch = "".join(f'<li><b>{g.emph(w["title"], auto=False)}</b> {g.emph(w.get("why", ""), auto=False)}</li>'
                    for w in m["watch"] if w.get("title"))
    labels = {"gaining": "Gaining attention", "early": "Early signals", "turning": "Sentiment turning",
              "contested": "Contested"}
    moved = "".join(f'<li><b>{labels[s]}:</b> ' + "; ".join(
        x for x in (f'new: {", ".join(map(esc, d[s]["new"]))}' if d[s]["new"] else "",
                    f'dropped off: {", ".join(map(esc, d[s]["dropped"]))}' if d[s]["dropped"] else "") if x)
        + "</li>" for s in signals.SECTIONS if d[s]["new"] or d[s]["dropped"])
    if d["themes"]:
        moved += f'<li><b>Themes:</b> {esc("; ".join(d["themes"]))}</li>'
    if d["connections"]:
        moved += f'<li><b>New connections:</b> {esc("; ".join(d["connections"]))}</li>'
    if d["narratives"]:
        moved += f'<li><b>Narratives:</b> {esc("; ".join(d["narratives"]))}</li>'
    w = m["signals"]["window"]
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<script>(function(){{var d=document.documentElement,t,m=matchMedia('(prefers-color-scheme: dark)');try{{t=localStorage.getItem('theme')}}catch(e){{}}function a(){{d.classList.toggle('dark',t?t==='dark':m.matches)}}a();m.addEventListener('change',function(){{if(!t)a()}});window.toggleTheme=function(){{t=d.classList.contains('dark')?'light':'dark';try{{localStorage.setItem('theme',t)}}catch(e){{}}a()}}}})();</script>
<title>Weekly memo {esc(m["week"])}: {esc(m["title"])}</title>
<style>{g.CSS}
.memo-h{{font-family:var(--serif);font-size:clamp(17px,1.3vw,21px);margin:0 0 10px;}}
.memo-ev{{font-size:13px;color:var(--muted);margin:10px 0 0;}}
.memo-list{{margin:16px 0 0;padding-left:20px;line-height:1.6;}}
.memo-list li{{margin-bottom:8px;}}
</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle light/dark mode">&#9680;</button>
    <div class="backlink"><a href="../index.html#signals">&#8592; Signals</a></div>
    <div class="kicker">Weekly memo &middot; {esc(m["week"])}</div>
    <h1>{esc(m["title"])}</h1>
    <div class="byline">Covers briefs since <b>{esc(m["since"])}</b> &middot; signals window {esc(w["recent_from"])} to {esc(w["latest"])} ({w["recent_briefs"]} briefs)</div>
  </header>
  <div class="inner">
    <section class="sec">
      <div class="sec-eye">The answer</div>
      <h2>This week in one read</h2>
      <div class="card" style="margin-top:16px;"><p>{g.emph(m["summary"], auto=False)}</p></div>
    </section>
    <section class="sec">
      <div class="sec-eye">Direction, not precision</div>
      <h2>Insights</h2>
      {insights}
    </section>
    <section class="sec">
      <div class="sec-eye">Where to look next</div>
      <h2>Worth a closer look</h2>
      <ol class="memo-list">{watch}</ol>
    </section>
    <section class="sec" style="border-bottom:none;">
      <div class="sec-eye">Computed, not written</div>
      <h2>What moved since the last memo</h2>
      <ul class="memo-list">{moved or "<li>First memo, or nothing new crossed a signal threshold.</li>"}</ul>
      <p class="memo-ev">Signals measure what your sources talk about and how they lean, not prices. Windows are normalized per brief.</p>
    </section>
  </div>
</div>
</body>
</html>"""
    out = path[:-5] + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out}")
    print(f"Wrote {g.build_index()}")


def _selftest():
    a = {"gaining": [{"key": "x", "name": "X"}], "early": [], "turning": [], "contested": [],
         "themes": [{"tag": "energy", "recent_pct": 30}], "connections": [{"a": "x", "b": "y", "a_name": "X", "b_name": "Y"}]}
    b = {"gaining": [{"key": "z", "name": "Z"}], "early": [], "turning": [], "contested": [],
         "themes": [{"tag": "energy", "recent_pct": 20}], "connections": []}
    d = diff(a, b)
    assert d["gaining"] == {"new": ["X"], "dropped": ["Z"]} and d["themes"] == ["energy 20% → 30%"]
    assert d["connections"] == ["X + Y"] and diff(a, None)["gaining"]["new"] == ["X"]
    n = lambda m, pct: {"members": m, "names": [x.upper() for x in m], "recent_pct": pct}
    a["narratives"] = [n(["p", "q", "r"], 30), n(["s", "t", "u"], 10)]
    b["narratives"] = [n(["p", "q", "r", "v"], 20), n(["w", "x", "y"], 5)]
    assert diff(a, b)["narratives"] == ["P · Q · R 20% → 30%", "new: S · T · U", "faded: W · X · Y"]
    assert diff(a, {})["narratives"][0] == "new: P · Q · R"
    assert week_key(dt.date(2026, 10, 3)) == "2026-W40"
    print("memo selftest ok")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "context":
        context()
    elif cmd == "render" and len(sys.argv) == 3:
        render(sys.argv[2])
    elif cmd == "selftest":
        _selftest()
    else:
        sys.exit(__doc__)
