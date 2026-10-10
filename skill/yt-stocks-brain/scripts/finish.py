#!/usr/bin/env python3
"""
finish.py — after generate.py: archive transcripts, set entity kinds, verify, commit, push.

    python3 finish.py <slug-substring> --src <dir with VID.en.srt/.txt> [--kind key=kind ...] [--no-push]

1. Copies the video's .srt/.txt from --src into research-data/<slug>/.
2. Applies --kind key=kind to kb/entities.json (line edit; key is the registry key, e.g. philips=company).
3. Regenerates from the archived data file, prints the entity list (names-pollution check) and
   runs check_quotes.py (quotes/hot takes must be in the transcript; read each flag).
4. Refuses to commit while any newly added registry entity is still kind "unknown".
5. Commits (no Co-Authored-By trailer: repo rule) and pushes, unless --no-push. --amend for re-runs.

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


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--src", required=True)
    ap.add_argument("--kind", action="append", default=[], metavar="key=kind")
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--amend", action="store_true", help="amend HEAD instead of adding a commit (unpushed re-runs)")
    a = ap.parse_args()

    dirs = [d for d in glob.glob("research-data/*") if a.slug in os.path.basename(d)]
    if len(dirs) != 1:
        sys.exit(f"slug {a.slug!r} matched {len(dirs)} folders: {dirs}")
    d = dirs[0]
    slug = os.path.basename(d)
    meta = json.load(open(os.path.join(d, slug + ".json"), encoding="utf-8"))["meta"]
    vid = re.search(r"([\w-]{11})$", meta["video_url"]).group(1)

    copied = 0
    for f in glob.glob(os.path.join(a.src, vid + ".*")):
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

    data = glob.glob(os.path.join(d, "*_data.py"))[0]
    g = sh([sys.executable, os.path.join(HERE, "generate.py"), data])
    for line in (g.stdout + g.stderr).splitlines():
        if "warning" in line.lower():
            print(line)

    lib = json.load(open("library.json", encoding="utf-8"))
    for b in lib["briefs"]:
        if b["html"].startswith(slug):
            print("entities:", [e["display"] for e in b["entities"]])

    q = sh([sys.executable, os.path.join(HERE, "check_quotes.py"), d])
    print("quotes:", q.stdout.strip() or q.stderr.strip())

    added = sh(["git", "diff", "-U0", "kb/entities.json"]).stdout
    unknown = [l for l in added.splitlines() if l.startswith("+") and '"kind": "unknown"' in l]
    if unknown:
        print("STOP: new entities still kind unknown (pass --kind key=kind):")
        print("\n".join(unknown))
        sys.exit(1)

    msg = f"Add brief: {meta['channel']} — {meta['title']} ({meta['date']})"
    paths = [p for p in ("index.html", "library.json", "kb", "research-data", "memos") if os.path.exists(p)]
    sh(["git", "add", "-A", "--", *paths, *glob.glob(slug + ".html")])
    c = sh(["git", "commit", "-q", *(["--amend"] if a.amend else []), "-m", msg])
    if c.returncode:
        sys.exit(c.stdout + c.stderr)
    print("committed:", msg)
    if not a.no_push:
        p = sh(["git", "push", "-q"])
        print("pushed" if p.returncode == 0 else "PUSH FAILED: " + p.stderr)


if __name__ == "__main__":
    main()
