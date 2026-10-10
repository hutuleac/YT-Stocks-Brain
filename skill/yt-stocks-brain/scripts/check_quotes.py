#!/usr/bin/env python3
"""
check_quotes.py — are the brief's verbatim quotes actually in the transcript?

    python3 check_quotes.py <research-data/slug folder>

Checks every theme `quote` and every `HOT_TAKES.take` against the cleaned transcript in the same
folder (*.txt). Matching is by word 3-grams, ignoring case and punctuation, so caption-noise
tightening passes but a paraphrase or invented line does not. Prints quotes under 70% overlap.
Exit 1 if any are flagged. Report-only: read each flag before editing (censored words such as
f***ing and quotes you merged across a speaker turn will trip it legitimately).
"""
import glob
import json
import os
import re
import sys


def words(s):
    return re.findall(r"[a-z0-9']+", s.lower().replace("’", "'"))


def grams(w, n=3):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)} or {tuple(w)}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = sys.argv[1]
    js = [f for f in glob.glob(os.path.join(d, "*.json"))]
    txts = [f for f in glob.glob(os.path.join(d, "*.txt"))]
    if not js or not txts:
        sys.exit("need the brief .json and the cleaned transcript .txt in the folder")
    brief = json.load(open(js[0], encoding="utf-8"))
    corpus = grams(words(open(txts[0], encoding="utf-8", errors="replace").read()))

    items = []
    for t in brief.get("themes", []):
        q = t.get("quote")
        if q:
            items.append(("quote", t.get("title", ""), q["text"] if isinstance(q, dict) else q))
    for h in brief.get("hot_takes", []):
        items.append(("take", "", h.get("take", "")))

    bad = 0
    for kind, ctx, text in items:
        g = grams(words(text))
        score = len(g & corpus) / len(g) if g else 1
        if score < 0.7:
            bad += 1
            print(f"{score:.0%} {kind}: {text[:110]}")
    print(f"{len(items)} quotes/takes checked, {bad} flagged")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
