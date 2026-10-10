#!/usr/bin/env python3
"""
check_quotes.py — are the brief's verbatim quotes actually in the transcript?

    python3 check_quotes.py <research-data/slug folder>

Also checks `names`: each entry must be a ticker-index kind (company/fund/crypto/commodity/unknown
in kb/entities.json) and its name, an alias or its ticker must be spoken in the transcript, which
catches countries/products in the index and companies guessed through a garbled caption.

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


TICKER_KINDS = {"company", "fund", "crypto", "commodity", "unknown"}


def check_names(slug_dir, tw):
    """Flag names entries of a non-index kind, or never spoken in the transcript."""
    slug = os.path.basename(os.path.abspath(slug_dir))
    root = os.path.abspath(os.path.join(slug_dir, "..", ".."))
    try:
        reg = json.load(open(os.path.join(root, "kb", "entities.json"), encoding="utf-8"))
        lib = json.load(open(os.path.join(root, "library.json"), encoding="utf-8"))
    except OSError:
        return 0
    text = "".join(tw)  # spaces squeezed out so "Open AI" matches OpenAI
    bad = 0
    seen = set()
    for b in lib["briefs"]:
        if not b["html"].startswith(slug):
            continue
        for e in b["entities"]:
            if e["key"] in seen:
                continue
            seen.add(e["key"])
            r = reg.get(e["key"])
            if not isinstance(r, dict):
                continue
            if r["kind"] not in TICKER_KINDS:
                bad += 1
                print(f"names: {e['display']} is kind {r['kind']}, belongs in bullets")
            forms = [r.get("name", "")] + list(r.get("aliases", [])) + [r.get("ticker") or ""]
            toks = {w for f in forms for w in words(re.sub(r"\(.*?\)", " ", f)) if len(w) >= 4}
            toks |= {t.lower() for t in [r.get("ticker") or ""] if len(t) >= 3}
            if toks and not any(t.replace(" ", "") in text for t in toks):
                bad += 1
                print(f"names: {e['display']} not found as spoken (caption spelling variant, an inference, or a garbled-caption guess: confirm)")
    print(f"{len(seen)} names checked, {bad} flagged")
    return bad


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
    bad += check_names(d, words(open(txts[0], encoding="utf-8", errors="replace").read()))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
