#!/usr/bin/env python3
"""
finish.py — after generate.py: archive transcripts, set entity kinds, verify, commit, push.

    python3 finish.py <slug-or-substring> --src <dir with VID.en.srt/.txt> [--kind key=kind ...]
                      [--heard key=variant ...] [--accept-flags] [--no-push | --amend]

0. Runs the scripts' selftests (stops if the toolchain itself is broken).
1. Copies the video's .srt/.txt from --src into research-data/<slug>/ (an exact folder name wins
   over a substring match).
2. Applies --kind key=kind and --heard key=variant (a caption spelling, "qqq=cues") to
   kb/entities.json.
3. Regenerates from the archived data file (stops if generate.py fails), prints the entity list,
   runs check_quotes.py, and check_coverage.py when --src holds an inventory*.md.
4. Refuses to commit while a new registry entity is kind "unknown", or while a quote/name/coverage
   check is flagged — fix the brief, record caption spellings with --heard, or pass
   --accept-flags once every remaining flag has been read and judged noise.
5. Commits (no Co-Authored-By trailer: repo rule; body = theme titles) and pushes unless
   --no-push. --amend for re-runs. Exits 1 if the push fails.

Run from the repo root. Does not stage .playwright-mcp/ or anything outside brief output.
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
SELFTESTS = [["memo.py", "selftest"], ["build_kb.py"], ["entities.py"], ["signals.py"], ["test_canonicalize.py"]]


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def py(*args):
    return sh([sys.executable, os.path.join(HERE, args[0]), *args[1:]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--src", required=True)
    ap.add_argument("--kind", action="append", default=[], metavar="key=kind")
    ap.add_argument("--heard", action="append", default=[], metavar="key=variant")
    ap.add_argument("--accept-flags", action="store_true", help="commit despite flags you have read and judged noise")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--amend", action="store_true", help="amend HEAD instead of adding a commit (unpushed re-runs)")
    a = ap.parse_args()

    for t in SELFTESTS:
        r = py(*t)
        if r.returncode:
            sys.exit(f"selftest {' '.join(t)} failed — fix the scripts first:\n{r.stdout}{r.stderr}")

    dirs = [d for d in glob.glob("research-data/*") if a.slug in os.path.basename(d)]
    dirs = [d for d in dirs if os.path.basename(d) == a.slug] or dirs
    if len(dirs) != 1:
        sys.exit(f"slug {a.slug!r} matched {len(dirs)} folders (pass the full folder name): {dirs}")
    d = dirs[0]
    slug = os.path.basename(d)
    brief = json.load(open(os.path.join(d, slug + ".json"), encoding="utf-8"))
    meta = brief["meta"]
    m = re.search(r"([\w-]{11})$", meta["video_url"])  # no match for non-YouTube text sources
    vid = m.group(1) if m else None

    copied = 0
    for f in glob.glob(os.path.join(a.src, vid + ".*")) if vid else []:
        if f.endswith((".srt", ".txt")):
            shutil.copy(f, d)
            copied += 1
    print(f"transcripts copied: {copied}")

    if a.kind:
        reg = open("kb/entities.json", encoding="utf-8").read()
        for kv in a.kind:
            key, kind = kv.split("=", 1)
            reg, n = re.subn(rf'("{re.escape(key)}": \{{[^\n]*?"kind": )"[a-z]+"', rf'\1"{kind}"', reg, count=1)
            print(f"kind {key}={kind}" if n else f"WARNING: registry key {key!r} not found")
        open("kb/entities.json", "w", encoding="utf-8").write(reg)
    if a.heard:
        sys.path.insert(0, HERE)
        from entities import Registry
        r = Registry()
        for kv in a.heard:
            key, variant = kv.split("=", 1)
            if r.get(key) is None:
                print(f"WARNING: registry key {key!r} not found")
                continue
            heard = r.get(key).setdefault("heard", [])
            if variant.lower() not in heard:
                heard.append(variant.lower())
                r.dirty = True
            print(f"heard {key}={variant}")
        r.save()

    data = glob.glob(os.path.join(d, "*_data.py"))[0]
    g = py("generate.py", data)
    if g.returncode:
        sys.exit(f"generate.py failed:\n{g.stdout}{g.stderr}")
    for line in (g.stdout + g.stderr).splitlines():
        if "warning" in line.lower():
            print(line)
    brief = json.load(open(os.path.join(d, slug + ".json"), encoding="utf-8"))

    lib = json.load(open("library.json", encoding="utf-8"))
    for b in lib["briefs"]:
        if b["html"].startswith(slug):
            print("entities:", [e["display"] for e in b["entities"]])

    q = py("check_quotes.py", d)
    print("quotes:", q.stdout.strip() or q.stderr.strip())
    flagged = q.returncode != 0
    inv = sorted(glob.glob(os.path.join(a.src, "inventory*.md")))
    if inv:
        # speaker names appear in most inventory lines, so they'd mark every fact as placed
        ignore = ",".join(re.sub(r"\(.*?\)", " ", meta.get("speakers") or "").replace(",", " ").split())
        c = py("check_coverage.py", inv[-1], slug, f"--ignore={ignore}")
        print("coverage:", c.stdout.strip() or c.stderr.strip())
        flagged |= c.returncode != 0
    else:
        print("coverage: no inventory*.md in --src (required past ~50k transcript chars, see ref/long-video.md)")

    added = sh(["git", "diff", "-U0", "kb/entities.json"]).stdout
    unknown = [l for l in added.splitlines() if l.startswith("+") and '"kind": "unknown"' in l]
    if unknown:
        print("STOP: new entities still kind unknown (pass --kind key=kind):")
        print("\n".join(unknown))
        sys.exit(1)
    if flagged and not a.accept_flags:
        sys.exit("STOP: flags above. Fix the brief and re-run; a caption spelling -> --heard key=variant; "
                 "--accept-flags only once every remaining flag is read and judged noise.")

    if a.amend:
        top = sh(["git", "log", "-1", "--format=%s"]).stdout.strip()
        if not top.startswith("Add brief:"):
            sys.exit(f"--amend refused: HEAD is not a brief commit ({top!r})")

    msg = f"Add brief: {meta['channel']} — {meta['title']} ({meta['date']})"
    body = "\n".join(f"- {t['title']}" for t in brief.get("themes", []) if t.get("title"))
    paths = [p for p in ("index.html", "search-hits.json", "library.json", "kb", "research-data", "memos") if os.path.exists(p)]
    sh(["git", "add", "-A", "--", *paths, *glob.glob(slug + ".html")])
    c = sh(["git", "commit", "-q", *(["--amend"] if a.amend else []), "-m", msg, *(["-m", body] if body else [])])
    if c.returncode:
        sys.exit(c.stdout + c.stderr)
    print("committed:", msg)
    if not a.no_push:
        p = sh(["git", "push", "-q"])
        if p.returncode:
            sys.exit("PUSH FAILED: " + p.stderr)
        print("pushed")


if __name__ == "__main__":
    main()
