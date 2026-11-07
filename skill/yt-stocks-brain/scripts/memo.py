"""Weekly and monthly insight memos — what changed in the library, for direction, not precision.

  python3 memo.py context            # evidence pack + memos/<ISO-week>.json skeleton (signals embedded)
  python3 memo.py month [YYYY-MM]    # evidence pack + memos/<YYYY-MM>.json skeleton (default: last month)
  # ... fill title / summary (/ insights / watch / labels) in that JSON (see ref/weekly-memo.md) ...
  python3 memo.py render memos/<key>.json   # -> memos/<key>.html + reindex

Computed, never written by hand: "what moved" (this snapshot diffed against the previous memo's),
the narrative trajectory (recent share across the last weekly snapshots), and the follow-up on the
previous memo's watch items (briefs naming their `entities` since). New briefs are counted by
brief id: each weekly memo records the `briefs` it covered, so a brief made after a memo, or an old
video briefed late, lands in the next memo instead of falling between two. Run from the repo root.
"""
import datetime as dt
import glob
import json
import os
import re
import sqlite3
import sys

import signals
from build_kb import DB_PATH

MEMO_DIR = "memos"
WEEK_RE, MONTH_RE = re.compile(r"\d{4}-W\d{2}$"), re.compile(r"\d{4}-\d{2}$")


def week_key(d=None):
    y, w, _ = (d or dt.date.today()).isocalendar()
    return f"{y}-W{w:02d}"


def last_month(d=None):
    first = (d or dt.date.today()).replace(day=1)
    return (first - dt.timedelta(days=1)).strftime("%Y-%m")


def _load(p):
    return json.load(open(p, encoding="utf-8"))


def memo_paths():
    """Weekly memo JSON paths, newest week first."""
    return sorted(glob.glob(os.path.join(MEMO_DIR, "*-W*.json")), reverse=True)


def month_paths():
    """Monthly memo JSON paths, newest first."""
    return sorted((p for p in glob.glob(os.path.join(MEMO_DIR, "*.json"))
                   if MONTH_RE.match(os.path.basename(p)[:-5])), reverse=True)


def is_due(today=None):
    """A memo is due when none exists for this ISO week and the last one is >= 6 days old."""
    paths = memo_paths()
    if not paths:
        return True
    last = _load(paths[0])
    if last.get("week") == week_key(today):
        return False
    return (today or dt.date.today()) - dt.date.fromisoformat(last["date"]) >= dt.timedelta(days=6)


def month_due(today=None):
    """Last month's memo is due once it has weekly memos and no monthly memo yet."""
    m = last_month(today)
    return (m if _weeklies(m) and not os.path.exists(os.path.join(MEMO_DIR, f"{m}.json")) else None)


def _weeklies(month):
    """Weekly memos dated in that month, oldest first."""
    return [m for m in map(_load, reversed(memo_paths())) if m["date"].startswith(month)]


def label(n):
    return n.get("label") or " · ".join(n["names"][:3])


def carry_labels(cur, prev):
    """Narrative names written in an earlier memo follow the same cluster into this snapshot."""
    for n in cur.get("narratives", []):
        was = next((p for p in (prev or {}).get("narratives", [])
                    if p.get("label") and signals.same_narrative(n["members"], p["members"])), None)
        if was and not n.get("label"):
            n["label"] = was["label"]
    return cur


def diff(cur, prev):
    """Signals snapshot vs previous one -> {"new_names": {"new", "dropped"}, "narratives": [lines]}."""
    now = {i["key"]: i["name"] for i in cur.get("new_names", [])}
    before = {i["key"]: i["name"] for i in (prev or {}).get("new_names", [])}
    out = {"new_names": {"new": [now[k] for k in now if k not in before],
                         "dropped": [before[k] for k in before if k not in now]}}
    pn = (prev or {}).get("narratives", [])
    out["narratives"] = []
    for n in cur.get("narratives", []):
        was = next((p for p in pn if signals.same_narrative(n["members"], p["members"])), None)
        if not was:
            if n.get("briefs", 1):  # a cluster nobody named in the recent window isn't news
                out["narratives"].append(f'new: {label(n)} ({n["recent_pct"]}%, {n["briefs"]} briefs)')
        elif abs(n["recent_pct"] - was["recent_pct"]) >= 5:
            out["narratives"].append(f'{label(n)} {was["recent_pct"]}% → {n["recent_pct"]}% '
                                     f'({was.get("briefs", "?")} → {n["briefs"]} briefs)')
        elif n.get("emerging") and not was.get("emerging"):
            out["narratives"].append(f'now emerging: {label(n)}')
    out["narratives"] += [f'faded: {label(p)}' for p in pn
                          if not any(signals.same_narrative(p["members"], n["members"]) for n in cur.get("narratives", []))]
    return out


def trajectory(snaps, cur, n=4):
    """Each current narrative's recent share across the last n snapshots (oldest first)."""
    snaps = snaps[-(n - 1):] if n > 1 else []
    out = []
    for c in cur.get("narratives", []):
        pts = [next((f'{p["recent_pct"]}%' for p in s.get("narratives", [])
                     if signals.same_narrative(c["members"], p["members"])), "–") for s in snaps]
        pts.append(f'{c["recent_pct"]}%')
        if any(p not in ("–", "0%") for p in pts):
            out.append((label(c), pts, c.get("emerging")))
    return out


def _previous(key):
    for p in memo_paths():
        m = _load(p)
        if m.get("week") < key:
            return m
    return None


def _covered(week):
    """Brief html files already listed by an earlier weekly memo."""
    return {h for m in map(_load, memo_paths()) if m["week"] < week for h in m.get("briefs", [])}


def followup(prev, html_ids, db):
    """Previous memo's watch items with `entities` -> how often they came up in these briefs."""
    out = []
    for w in (prev or {}).get("watch", []):
        keys = w.get("entities") or []
        if not keys or not w.get("title"):
            continue
        q = (f"SELECT b.html, m.stance, m.conviction FROM mentions m JOIN briefs b ON b.id = m.brief_id "
             f"WHERE m.entity_key IN ({','.join('?' * len(keys))}) AND b.html IN ({','.join('?' * len(html_ids)) or 'NULL'})")
        rows = db.execute(q, [*keys, *html_ids]).fetchall()
        net = signals._net([signals.direction(s, c) for _, s, c in rows])
        n = len({r[0] for r in rows})
        out.append(f'{w["title"]}: {n} of {len(html_ids)} new briefs'
                   + (f', sentiment {signals.sent_label(net)}' if n and net is not None else ""))
    return out


def _db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def _print_signals(data):
    print("\n## narratives (entity clusters; share of briefs naming >= 2 members, prior -> recent; E = emerging)")
    for n in data["narratives"]:
        print(f"- {'E ' if n['emerging'] else ''}{', '.join(n['names'])} [{n['tag']}]"
              + (f' (named: {n["label"]})' if n.get("label") else "")
              + f": {n['prior_pct']}% -> {n['recent_pct']}% ({n['briefs']} recent / {n['briefs_all']} total briefs), "
              f"sentiment {n['sent_prior']} -> {n['sent_recent']}")
        for r in n.get("rows", [])[:4]:
            print(f"    · {r['date']} {r['channel']}: " + " | ".join(t for t, _ in r["themes"]) + f" ({r['html']})")
        for c in n.get("claims", [])[:2]:
            print(f"    → {c['who']}: {c['claim']} ({c['by_when'] or 'no date'})")


def context():
    data = signals.compute(DB_PATH)
    if not data:
        sys.exit("no dated briefs in kb/brain.db — run generate.py --reindex first")
    today = dt.date.today()
    week = week_key(today)
    prev = _previous(week)
    since = prev["date"] if prev else data["window"]["recent_from"]
    path = os.path.join(MEMO_DIR, f"{week}.json")
    os.makedirs(MEMO_DIR, exist_ok=True)
    db = _db()
    covered = _covered(week)
    new = [b for b in db.execute("SELECT date, channel, title, html FROM briefs ORDER BY date")
           if b["html"] not in covered]
    snap = carry_labels(signals.snapshot(data), prev and prev.get("signals"))
    m = _load(path) if os.path.exists(path) else {
        "week": week, "date": today.isoformat(), "since": since, "title": "", "summary": "",
        "insights": [{"title": "", "bullets": [], "evidence": []}],
        "watch": [{"title": "", "why": "", "entities": []}], "signals": snap}
    m["briefs"] = [b["html"] for b in new]
    json.dump(m, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for n, s in zip(data["narratives"], snap["narratives"]):
        n["label"] = s.get("label")
    d = diff(snap, prev and prev.get("signals"))

    print(f"# Memo context {week} — {len(new)} new briefs since the last memo (window "
          f"{data['window']['recent_from']}..{data['window']['latest']})\n")
    print(f"Skeleton: {path}\n\n## New briefs since last memo")
    for b in new:
        print(f"- {b['date']} {b['channel']}: {b['title']} ({b['html']})")
    print("\n## What moved since the last memo" + ("" if prev else " (first memo: everything is new)"))
    for k, v in d.items():
        print(f"- {k}: {v}")
    print("\n## Last memo's watch list, followed up")
    for line in followup(prev, [b["html"] for b in new], db) or ["(no watch item had `entities`)"]:
        print(f"- {line}")
    print("\n## Trajectory (recent share, last 4 memos, oldest first)")
    for lab, pts, em in trajectory([_load(p)["signals"] for p in reversed(memo_paths()) if _load(p)["week"] < week], snap):
        print(f"- {'E ' if em else ''}{lab}: {' → '.join(pts)}")
    _print_signals(data)
    print("\n## new names (first named in the recent window, >= 2 briefs, not in any narrative yet)")
    for i in data["new_names"]:
        print(f"- {i['name']} ({i['ticker'] or '-'}) [{i['key']}]: {i['briefs']} briefs, first {i['first_seen']}, sentiment {i['sent']}")
        for r in i["rows"][:3]:
            print(f"    · {r['date']} {r['channel']}: {' / '.join(r['notes'])} ({r['html']})")
        for c in i["claims"][:2]:
            print(f"    → {c['who']}: {c['claim']} ({c['by_when'] or 'no date'})")
    print("\n## hot takes in the new briefs")
    ids = [b["html"] for b in new]
    for t in db.execute(f"""SELECT t.take, t.cite, b.html FROM takes t JOIN briefs b ON b.id = t.brief_id
                            WHERE b.html IN ({','.join('?' * len(ids)) or 'NULL'}) ORDER BY b.date DESC LIMIT 40""", ids):
        print(f"- {t['take']} {t['cite']} ({t['html']})")


def month_context(month=None):
    month = month or last_month()
    weeks = _weeklies(month)
    if not weeks:
        sys.exit(f"no weekly memos dated in {month}")
    before = [m for m in map(_load, reversed(memo_paths())) if m["date"] < month]
    base = before[-1]["signals"] if before else weeks[0]["signals"]
    cur = weeks[-1]["signals"]
    path = os.path.join(MEMO_DIR, f"{month}.json")
    if not os.path.exists(path):
        json.dump({"month": month, "date": dt.date.today().isoformat(), "title": "", "summary": "",
                   "weeks": [m["week"] for m in weeks], "base": base, "signals": cur},
                  open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"# Month context {month} — {len(weeks)} weekly memos, "
          f"{sum(len(m.get('briefs', [])) for m in weeks)} briefs\n\nSkeleton: {path}\n")
    for m in weeks:
        print(f"## {m['week']}: {m['title']}\n{m['summary']}")
        for i in m.get("insights", []):
            print(f"- insight: {i['title']}")
        for w in m.get("watch", []):
            print(f"- watch: {w['title']}")
        print()
    print(f"## What moved over the month ({'last memo before ' + month if before else 'first memo of the month'} → last memo of the month)")
    for k, v in diff(cur, base).items():
        print(f"- {k}: {v}")
    print("\n## Trajectory across the month's weekly memos")
    for lab, pts, em in trajectory([m["signals"] for m in weeks[:-1]], cur, n=len(weeks)):
        print(f"- {'E ' if em else ''}{lab}: {' → '.join(pts)}")


def _page(kicker, title, byline, sections):
    import generate as g
    esc = g.esc
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<script>(function(){{var d=document.documentElement,t,m=matchMedia('(prefers-color-scheme: dark)');try{{t=localStorage.getItem('theme')}}catch(e){{}}function a(){{d.classList.toggle('dark',t?t==='dark':m.matches)}}a();m.addEventListener('change',function(){{if(!t)a()}});window.toggleTheme=function(){{t=d.classList.contains('dark')?'light':'dark';try{{localStorage.setItem('theme',t)}}catch(e){{}}a()}}}})();</script>
<title>{esc(kicker)}: {esc(title)}</title>
<style>{g.CSS}
.memo-h{{font-family:var(--serif);font-size:clamp(17px,1.3vw,21px);margin:0 0 10px;}}
.memo-ev{{font-size:13px;color:var(--muted);margin:10px 0 0;}}
.memo-list{{margin:16px 0 0;padding-left:20px;line-height:1.6;}}
.memo-list li{{margin-bottom:8px;}}
.traj{{font-variant-numeric:tabular-nums;color:var(--muted);white-space:nowrap;}}
</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle light/dark mode">&#9680;</button>
    <div class="backlink"><a href="../index.html#signals">&#8592; Signals</a></div>
    <div class="kicker">{esc(kicker)}</div>
    <h1>{esc(title)}</h1>
    <div class="byline">{byline}</div>
  </header>
  <div class="inner">
{"".join(f'''    <section class="sec"{' style="border-bottom:none;"' if i == len(sections) - 1 else ''}>
      <div class="sec-eye">{eye}</div>
      <h2>{h}</h2>
      {body}
    </section>
''' for i, (eye, h, body) in enumerate(sections))}  </div>
</div>
</body>
</html>"""


def _moved_html(d):
    import generate as g
    esc = g.esc
    nn = d["new_names"]
    out = (f'<li><b>New names:</b> ' + "; ".join(x for x in (
        f'new: {", ".join(map(esc, nn["new"]))}' if nn["new"] else "",
        f'dropped off: {", ".join(map(esc, nn["dropped"]))}' if nn["dropped"] else "") if x) + "</li>"
        if nn["new"] or nn["dropped"] else "")
    out += "".join(f'<li>{esc(x)}</li>' for x in d["narratives"])
    return out or "<li>First memo, or nothing new crossed a signal threshold.</li>"


def _traj_html(rows):
    import generate as g
    return "".join(f'<li><b>{g.esc(lab)}</b>{" · emerging" if em else ""} <span class="traj">{" → ".join(pts)}</span></li>'
                   for lab, pts, em in rows) or "<li>No narratives yet.</li>"


NOTE = ('<p class="memo-ev">Signals measure what your sources talk about and how they lean, not prices. '
        'Market briefs only; windows are counted in briefs.</p>')


def render(path):
    import generate as g
    m = _load(path)
    key = os.path.basename(path)[:-5]
    esc = g.esc
    titles = {b["html"]: f'{b["channel"]}: {b["title"]}' for b in _load("library.json")["briefs"]}
    summary = ("The answer", "In one read", f'<div class="card" style="margin-top:16px;"><p>{g.emph(m["summary"], auto=False)}</p></div>')

    if MONTH_RE.match(key):
        weeks = [_load(os.path.join(MEMO_DIR, f"{w}.json")) for w in m["weeks"]]
        wl = "".join(f'<li><a href="{esc(w["week"])}.html"><b>{esc(w["week"])}</b> {esc(w["title"])}</a></li>' for w in weeks)
        traj = trajectory([w["signals"] for w in weeks[:-1]], m["signals"], n=len(weeks))
        page = _page(f"Monthly memo · {key}", m["title"],
                     f'{len(weeks)} weekly memos &middot; {sum(len(w.get("briefs", [])) for w in weeks)} briefs',
                     [summary,
                      ("Computed, not written", "Narrative trajectory", f'<ul class="memo-list">{_traj_html(traj)}</ul>'
                       '<p class="memo-ev">Share of recent market briefs naming two or more members, one point per weekly memo.</p>'),
                      ("Computed, not written", "What moved over the month", f'<ul class="memo-list">{_moved_html(diff(m["signals"], m["base"]))}</ul>{NOTE}'),
                      ("The weeks", "Weekly memos", f'<ol class="memo-list">{wl}</ol>')])
    else:
        prev = _previous(m["week"])
        d = diff(m["signals"], prev and prev.get("signals"))

        def link(ev):
            return f'<a href="../{esc(ev)}">{esc(titles.get(ev, ev))}</a>'

        insights = "".join(
            f'<div class="card" style="margin-top:16px;"><h3 class="memo-h">{g.emph(i["title"], auto=False)}</h3>'
            f'{g.render_snapshot(i.get("bullets", []))}'
            + (f'<p class="memo-ev">Evidence: {" · ".join(link(e) for e in i.get("evidence", []))}</p>' if i.get("evidence") else "")
            + "</div>" for i in m["insights"] if i.get("title"))
        watch = "".join(f'<li><b>{g.emph(w["title"], auto=False)}</b> {g.emph(w.get("why", ""), auto=False)}</li>'
                        for w in m["watch"] if w.get("title"))
        fu = followup(prev, m.get("briefs", []), _db()) if m.get("briefs") else []
        snaps = [_load(p)["signals"] for p in reversed(memo_paths()) if _load(p)["week"] < m["week"]]
        w = m["signals"]["window"]
        n_new = f'{len(m["briefs"])} new briefs &middot; ' if m.get("briefs") else ""
        page = _page(f"Weekly memo · {m['week']}", m["title"],
                     f'{n_new}since <b>{esc(m["since"])}</b> &middot; signals window {esc(w["recent_from"])} to {esc(w["latest"])} ({w["recent_briefs"]} briefs)',
                     [summary,
                      ("Direction, not precision", "Insights", insights),
                      ("Where to look next", "Worth a closer look", f'<ol class="memo-list">{watch}</ol>'),
                      *([("Computed, not written", "Last memo's watch list, since then",
                          '<ul class="memo-list">' + "".join(f"<li>{esc(x)}</li>" for x in fu) + "</ul>")] if fu else []),
                      ("Computed, not written", "Trajectory, last 4 memos",
                       f'<ul class="memo-list">{_traj_html(trajectory(snaps, m["signals"]))}</ul>'),
                      ("Computed, not written", "What moved since the last memo", f'<ul class="memo-list">{_moved_html(d)}</ul>{NOTE}')])
    out = path[:-5] + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out}")
    print(f"Wrote {g.build_index()}")


def _selftest():
    a = {"new_names": [{"key": "x", "name": "X"}]}
    b = {"new_names": [{"key": "z", "name": "Z"}]}
    d = diff(a, b)
    assert d["new_names"] == {"new": ["X"], "dropped": ["Z"]} and diff(a, None)["new_names"]["new"] == ["X"]
    n = lambda m, pct, em=False: {"members": m, "names": [x.upper() for x in m], "recent_pct": pct, "briefs": pct // 3, "emerging": em}
    a["narratives"] = [n(["p", "q", "r"], 30), n(["s", "t", "u"], 9), n(["g", "h", "i"], 8, True)]
    b["narratives"] = [n(["p", "q", "r", "v"], 21), n(["w", "x", "y"], 6), n(["g", "h", "i"], 7)]
    assert diff(a, b)["narratives"] == ["P · Q · R 21% → 30% (7 → 10 briefs)", "new: S · T · U (9%, 3 briefs)",
                                        "now emerging: G · H · I", "faded: W · X · Y"], diff(a, b)["narratives"]
    assert diff(a, {})["narratives"][0] == "new: P · Q · R (30%, 10 briefs)"
    b["narratives"][0]["label"] = "pq story"
    carry_labels(a, b)
    assert a["narratives"][0]["label"] == "pq story" and "label" not in a["narratives"][1]
    assert trajectory([b], a)[0] == ("pq story", ["21%", "30%"], False)
    assert trajectory([b], a)[1] == ("S · T · U", ["–", "9%"], False)
    assert week_key(dt.date(2026, 10, 3)) == "2026-W40"
    assert last_month(dt.date(2026, 1, 15)) == "2025-12"
    print("memo selftest ok")


if __name__ == "__main__":
    cmd, args = (sys.argv[1] if len(sys.argv) > 1 else ""), sys.argv[2:]
    if cmd == "context":
        context()
    elif cmd == "month" and len(args) <= 1:
        month_context(*args)
    elif cmd == "render" and len(args) == 1:
        render(args[0])
    elif cmd == "selftest":
        _selftest()
    else:
        sys.exit(__doc__)
