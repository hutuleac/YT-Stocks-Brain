#!/usr/bin/env python3
"""
check_quotes.py — are the brief's verbatim quotes actually in the transcript?

    python3 check_quotes.py <research-data/slug folder>

Also checks `names`: each entry must be a ticker-index kind (company/fund/crypto/commodity/unknown
in kb/entities.json) and its name, an alias, its ticker or a `heard` caption spelling must be
spoken in the transcript, which catches countries/products in the index and companies guessed
through a garbled caption. A caption spelling ("cues" for QQQ) is recorded once with
`finish.py --heard key=variant` and never flags again.

Checks every theme `quote` and every `HOT_TAKES.take` against the cleaned transcript (all *.txt
in the folder; a `region: "ro"` brief uses only its *.ro*.txt, so an English back-translation
can't pass against YouTube's auto-translated .en track). Matching is by word 3-grams, ignoring
case and punctuation, so caption-noise tightening passes but a paraphrase or invented line does
not. Prints quotes under 70% overlap. Quoted spans of 6+ words inside bullets, leads, watch lines,
snapshot, takeaways and other news are checked too, at 50% (tightened lines pass; a paraphrase or
translation in quotation marks does not): drop the quotation marks or use the speaker's words.
Exit 1 if anything is flagged; finish.py refuses to commit on exit 1 unless --accept-flags.
Censored words (f***ing) and quotes merged across a speaker turn trip it legitimately.
"""
import glob
import json
import os
import re
import sys
import unicodedata

INLINE = re.compile(r'[“"]([^“”"]+)[”"]')
SKIP_KEYS = {"icon", "tag", "id", "color", "badge", "status", "tags", "names", "quote"}


def words(s):
    # fold diacritics so Romanian quotes written without them (per ref/romanian.md) still match
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.findall(r"[a-z0-9']+", s.lower())


def grams(w, n=3):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)} or {tuple(w)}


def transcript(d, region):
    txts = sorted(glob.glob(os.path.join(d, "*.txt")))
    ro = [f for f in txts if ".ro" in os.path.basename(f)]
    use = ro if region == "ro" and ro else txts
    return "\n".join(open(f, encoding="utf-8", errors="replace").read() for f in use)


def strings(x):
    """Every rendered prose string under x, minus the fields checked elsewhere or not prose."""
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for k, v in x.items():
            if k not in SKIP_KEYS:
                yield from strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from strings(v)


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
                print(f"names: {e['display']} [{e['key']}] is kind {r['kind']}, belongs in bullets")
            forms = [r.get("name", "")] + list(r.get("aliases", [])) + [r.get("ticker") or ""]
            toks = {w for f in forms for w in words(re.sub(r"\(.*?\)", " ", f)) if len(w) >= 4}
            toks |= {t.lower() for t in [r.get("ticker") or ""] if len(t) >= 3}
            toks |= {"".join(words(h)) for h in r.get("heard", [])}
            if toks and not any(t.replace(" ", "") in text for t in toks):
                bad += 1
                print(f"names: {e['display']} [{e['key']}] not found as spoken — a caption spelling: "
                      f"finish.py --heard {e['key']}=<as captioned>; an inference or guess: move it to bullets")
    print(f"{len(seen)} names checked, {bad} flagged")
    return bad


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = sys.argv[1].rstrip("/")
    js = os.path.join(d, os.path.basename(d) + ".json")
    if not os.path.exists(js) or not glob.glob(os.path.join(d, "*.txt")):
        sys.exit("need the brief .json and the cleaned transcript .txt in the folder")
    brief = json.load(open(js, encoding="utf-8"))
    tw = words(transcript(d, brief.get("meta", {}).get("region")))
    corpus = grams(tw)

    items = []
    for t in brief.get("themes", []):
        q = t.get("quote")
        if q:
            items.append(("quote", 0.7, q["text"] if isinstance(q, dict) else q))
    for h in brief.get("hot_takes", []):
        items.append(("take", 0.7, h.get("take", "")))
    for s in strings([brief.get(k) for k in ("themes", "snapshot", "takeaways", "other_news")]):
        items += [("inline", 0.5, q) for q in INLINE.findall(s) if len(words(q)) >= 6]

    bad = 0
    for kind, floor, text in items:
        g = grams(words(text))
        score = len(g & corpus) / len(g) if g else 1
        if score < floor:
            bad += 1
            print(f"{score:.0%} {kind}: {text[:110]}")
    print(f"{len(items)} quotes/takes checked, {bad} flagged")
    bad += check_names(d, tw)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
