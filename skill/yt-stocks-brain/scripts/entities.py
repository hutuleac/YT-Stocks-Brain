"""Entity + speaker identity registry shared by generate.py (index, library.json) and build_kb.py.

kb/entities.json is the committed source of identity: one line per entity,
    "nvidia": {"name": "Nvidia", "ticker": "NVDA", "kind": "company", "aliases": [...]}
The key ("nvidia") is permanent. Ticker, name and kind are attributes that can change (an IPO
adds a ticker, it doesn't re-key history). Speakers in claims `who` are entities too
(kind "person"), so Elon Musk the speaker and Elon Musk the mention are one node.

Resolution of a raw string ("Nvidia (NVDA)", "NVIDIA", "CoreWeave (comparison)"):
  1. exact alias  2. name with qualifier stripped  3. explicit "(TICKER)"  4. else register a
  new entity (kind "unknown") and warn. Learned variants are appended as aliases, so the
  registry diff lands in the same commit as the brief that introduced it. Never fails a run.
"""
import json
import os
import re

REGISTRY_PATH = os.path.join("kb", "entities.json")
KINDS = {"company", "fund", "crypto", "commodity", "person", "country", "government", "org",
         "product", "group", "other", "unknown"}

_PAREN_TICKER = re.compile(r"\((?=[A-Z0-9.]*[A-Z])([A-Z0-9]{1,6}(?:\.[A-Z]{1,2})?)\)\s*$")
_TRAILING_PAREN = re.compile(r"\s*\([^()]*\)\s*$")
_WHO_SPLIT = re.compile(r"\s*/\s*|\s*&\s*|\s+and\s+|\s+si\s+|\s+with\s+", re.I)
TICKER_BLACKLIST = {
    "ADR", "IPO", "CEO", "CFO", "CTO", "ETF", "AI", "GPU", "SEC", "IRA", "WACC", "SOFR", "CPI",
    "PPI", "FOMC", "OER", "US", "UK", "EU", "GDP", "FED", "Q1", "Q2", "Q3", "Q4", "YOY", "MOM",
    "ATH", "IRL", "COO", "FDIC", "FTC", "FBI",
    # bare exchange suffixes some briefs put in parens ("Henkel (DE)") — not tickers
    "DE", "HK", "SS", "SZ", "TW", "TWO", "KS", "KQ", "TO", "AX", "PA", "AS",
}


def split_list(raw):
    """Split on top-level commas only — commas inside parens (e.g. an aside like
    "Memory semis (Samsung, SK Hynix implied)") don't count as separate entities."""
    parts, depth, buf = [], 0, []
    for ch in raw or "":
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


def split_name(raw):
    """'Nvidia (NVDA)' -> ('Nvidia', 'NVDA'); 'CoreWeave (comparison)' -> ('CoreWeave', None)."""
    s = raw.strip()
    m = _PAREN_TICKER.search(s)
    ticker = m.group(1) if m and m.group(1) not in TICKER_BLACKLIST else None
    if ticker:
        s = s[: m.start()].strip()
    while _TRAILING_PAREN.search(s) and _TRAILING_PAREN.sub("", s):
        s = _TRAILING_PAREN.sub("", s)
    return s, ticker


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "entity"


def _strip_parens(s):
    return re.sub(r"\s*\([^()]*\)", "", s).strip()


class Registry:
    def __init__(self, path=REGISTRY_PATH):
        self.path = path
        try:
            raw = json.load(open(path, encoding="utf-8"))
        except FileNotFoundError:
            raw = {}
        self.doc = raw.pop("_doc", "")
        self.ents = raw
        self.dirty = False
        self.warnings = []
        self.alias, self.ticker = {}, {}
        for key, e in self.ents.items():
            self._index(key, e)

    def _warn(self, msg):
        if msg not in self.warnings:
            self.warnings.append(msg)

    def _index(self, key, e):
        for a in [e["name"].lower(), *e.get("aliases", [])]:
            other = self.alias.setdefault(a, key)
            if other != key:
                self._warn(f"alias '{a}' claimed by both '{other}' and '{key}' in {self.path}")
        if e.get("ticker"):
            other = self.ticker.setdefault(e["ticker"], key)
            if other != key:
                self._warn(f"ticker {e['ticker']} on both '{other}' and '{key}' in {self.path}")

    def _learn(self, key, raw):
        a = raw.lower()
        if a not in self.alias:
            self.alias[a] = key
            self.ents[key].setdefault("aliases", []).append(a)
            self.dirty = True

    def get(self, key):
        return self.ents.get(key)

    def resolve(self, raw, kind="unknown"):
        """raw entity string -> permanent key (registering it if new), or None for empty."""
        if not raw or not raw.strip():
            return None
        raw = raw.strip()
        name, ticker = split_name(raw)
        key = self.alias.get(raw.lower()) or self.alias.get(name.lower()) or self.ticker.get(ticker)
        if key:
            e = self.ents[key]
            if ticker and not e.get("ticker"):
                e["ticker"] = ticker
                self.ticker.setdefault(ticker, key)
                self.dirty = True
                self._warn(f"ticker {ticker} added to '{key}' from '{raw}'")
            elif ticker and ticker != e.get("ticker") and raw.lower() not in self.alias:  # known variant = reviewed
                self._warn(f"'{raw}' says {ticker} but '{key}' has {e['ticker']} — typo, or a new listing?")
            self._learn(key, raw)
            return key
        key, n = slugify(name), 2
        while key in self.ents:
            key, n = f"{slugify(name)}-{n}", n + 1
        self.ents[key] = {"name": name, "ticker": ticker, "kind": kind, "aliases": []}
        self._index(key, self.ents[key])
        self._learn(key, raw)
        self.dirty = True
        self._warn(f"new entity '{key}' from '{raw}' — set its kind in {self.path}")
        return key

    def resolve_list(self, raw):
        """Comma-separated entity field (claims entity, relation endpoints) -> [keys]."""
        return [k for k in (self.resolve(p) for p in split_list(raw or "")) if k]

    def resolve_who(self, who, speakers="", channel=""):
        """Claim `who` -> ([speaker keys], note). 'Sacks / Chamath' -> two keys. A first name
        that matches exactly one person in the brief's speakers line expands to the full name;
        one that doesn't is scoped to the channel ('Andrew @ The Wolf Of All Streets') so two
        shows' Andrews never merge. '(cited by Jason)' / ', citing X' are provenance -> note."""
        if not who or not who.strip():
            return [], None
        notes = re.findall(r"\(([^()]*)\)", who)
        core = _strip_parens(who)
        if core.lower() in self.alias:  # whole string known: "US Securities and Exchange Commission"
            return [self.resolve(core)], "; ".join(notes) or None
        full = [_strip_parens(p) for p in split_list(speakers or "")]
        full = [n for p in full for n in _WHO_SPLIT.split(p) if n]
        parts = []
        for chunk in split_list(core):
            if re.match(r"(citing|citand|via|per)\b", chunk, re.I):
                notes.append(chunk)
            else:
                parts += _WHO_SPLIT.split(chunk)
        keys = []
        for part in (p.strip() for p in parts):
            if not part:
                continue
            if " " not in part and part.lower() not in self.alias:
                hits = [n for n in full if part.lower() in n.lower().split()]
                if len(hits) == 1 and " " in hits[0]:
                    part = hits[0]
                elif channel:
                    part = f"{part} @ {channel}"
            keys.append(self.resolve(part))
        return [k for k in keys if k], "; ".join(notes) or None

    def summary_warnings(self):
        unknown = sorted(k for k, e in self.ents.items() if e.get("kind") not in KINDS - {"unknown"})
        out = list(self.warnings)
        if unknown:
            out.append(f"{len(unknown)} entities need a kind in {self.path}: {', '.join(unknown[:12])}"
                       + (" ..." if len(unknown) > 12 else ""))
        return out

    def save(self):
        if not self.dirty:
            return False
        lines = [f'  "_doc": {json.dumps(self.doc, ensure_ascii=False)}']
        for key in sorted(self.ents):
            e = self.ents[key]
            e["aliases"] = sorted(set(e.get("aliases", [])) - {e["name"].lower()})
            lines.append(f"  {json.dumps(key)}: {json.dumps(e, ensure_ascii=False)}")
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("{\n" + ",\n".join(lines) + "\n}\n")
        self.dirty = False
        return True


def _selftest():
    import tempfile
    p = os.path.join(tempfile.mkdtemp(), "entities.json")
    json.dump({"_doc": "t",
               "nvidia": {"name": "Nvidia", "ticker": "NVDA", "kind": "company", "aliases": ["nvidia (nvda)"]},
               "meta": {"name": "Meta", "ticker": "META", "kind": "company", "aliases": ["meta platforms"]},
               "anthropic": {"name": "Anthropic", "ticker": None, "kind": "company", "aliases": []},
               "david-sacks": {"name": "David Sacks", "ticker": None, "kind": "person", "aliases": ["sacks"]}},
              open(p, "w"))
    r = Registry(p)
    assert r.resolve("NVIDIA") == r.resolve("Nvidia (comparison)") == "nvidia"
    assert r.resolve("Meta Platforms (META)") == "meta"
    assert r.resolve("Anthropic (ANTH)") == "anthropic" and r.get("anthropic")["ticker"] == "ANTH", "IPO adds ticker, key stays"
    assert r.resolve("Nvidia (NVDX)") == "nvidia" and any("NVDX" in w for w in r.warnings)
    r.warnings.clear()
    assert r.resolve("Nvidia (NVDX)") == "nvidia" and not r.warnings, "conflict warns once, then it's a known alias"
    assert r.resolve("Berkshire Hathaway (BRK.B)") == "berkshire-hathaway" and r.get("berkshire-hathaway")["kind"] == "unknown"
    assert r.resolve_list("Nvidia, Meta (META)") == ["nvidia", "meta"]
    keys, note = r.resolve_who("Sacks / Chamath (cited by Jason)", "Jason Calacanis (host), Chamath Palihapitiya, David Sacks")
    assert keys == ["david-sacks", "chamath-palihapitiya"] and note == "cited by Jason"
    keys, note = r.resolve_who("Andrew, citing Glassnode", "Scott Melker, Andrew, Tilman", "Wolf")
    assert keys == ["andrew-wolf"] and note == "citing Glassnode"
    assert r.resolve("Henkel (DE)") == "henkel" and r.get("henkel")["ticker"] is None
    assert r.save() and Registry(p).resolve("nvidia (nvda)") == "nvidia"
    assert not Registry(p).dirty
    print("entities selftest ok")


if __name__ == "__main__":
    _selftest()
