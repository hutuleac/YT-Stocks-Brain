"""Entity canonicalization shared by generate.py (index + library.json) and build_kb.py.

Every raw entity string in the library ("Nvidia (NVDA)", "NVIDIA", "Meta Platforms",
"CoreWeave (comparison)") resolves to one stable key, so all mentions of a company join up.

Resolution, in order:
  1. kb/aliases.json lookup (case-insensitive) — the manual layer for semantic merges
     ("Meta Platforms" -> "Meta") and tickers the regex can't parse ("000660.KS").
  2. A trailing "(TICKER)" is parsed; any other trailing "(...)" is a qualifier and dropped.
  3. No explicit ticker -> borrow one seen on the same name elsewhere ("Micron" -> MU).
  4. key = ticker, else lowercased name. Display = most common name variant under that key.
"""
import collections
import json
import os
import re

ALIASES_PATH = os.path.join("kb", "aliases.json")

_PAREN_TICKER = re.compile(r"\((?=[A-Z0-9.]*[A-Z])([A-Z0-9]{1,6}(?:\.[A-Z]{1,2})?)\)\s*$")
_BARE_TICKER = re.compile(r"^[A-Z]{1,5}$")
_TRAILING_PAREN = re.compile(r"\s*\([^()]*\)\s*$")
TICKER_BLACKLIST = {
    "ADR", "IPO", "CEO", "CFO", "CTO", "ETF", "AI", "GPU", "SEC", "IRA", "WACC",
    "SOFR", "CPI", "PPI", "FOMC", "OER", "US", "UK", "EU", "GDP", "FED", "Q1",
    "Q2", "Q3", "Q4", "YOY", "MOM", "ATH", "IRL", "COO", "FDIC", "FTC", "FBI",
}


def load_aliases(path=ALIASES_PATH):
    try:
        raw = json.load(open(path, encoding="utf-8"))
    except FileNotFoundError:
        return {}
    return {k.lower(): v for k, v in raw.items() if not k.startswith("_")}


def _split(raw):
    """-> (name, explicit_ticker or None, bare_ticker or None). Strips qualifiers."""
    s = raw.strip()
    m = _PAREN_TICKER.search(s)
    ticker = m.group(1) if m and m.group(1) not in TICKER_BLACKLIST else None
    if ticker:
        s = s[: m.start()].strip()
    while _TRAILING_PAREN.search(s) and _TRAILING_PAREN.sub("", s):
        s = _TRAILING_PAREN.sub("", s)
    bare = s if not ticker and _BARE_TICKER.match(s) and s not in TICKER_BLACKLIST else None
    return s, ticker, bare


class Resolver:
    """Two-pass: observe() every raw string first, then resolve() any of them."""

    def __init__(self, aliases=None):
        self.aliases = load_aliases() if aliases is None else {k.lower(): v for k, v in aliases.items()}
        self.seen = collections.Counter()
        self._cache = None

    def observe(self, raw):
        if raw and raw.strip():
            self.seen[raw.strip()] += 1
            self._cache = None

    def _parts(self, raw):
        target = self.aliases.get(raw.strip().lower(), raw)
        name, ticker, bare = _split(target)
        if name.lower() in self.aliases:  # "Meta Platforms (META)" -> "Meta Platforms" -> alias
            n2, t2, b2 = _split(self.aliases[name.lower()])
            name, ticker, bare = n2, ticker or t2, bare or b2
        return name, ticker, bare

    def _build(self):
        parts = {raw: self._parts(raw) for raw in self.seen}
        learned = {}  # name -> ticker, only from explicit "(TICKER)" mentions
        for name, ticker, _ in parts.values():
            if ticker:
                learned.setdefault(name.lower(), ticker)
        keyed, names_by_key = {}, collections.defaultdict(collections.Counter)
        for raw, (name, ticker, bare) in parts.items():
            t = ticker or learned.get(name.lower()) or bare
            key = t or name.lower()
            keyed[raw] = (key, t)
            names_by_key[key][name] += self.seen[raw]
        display = {k: sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0][0] for k, c in names_by_key.items()}
        self._cache = {raw: {"key": k, "name": display[k], "ticker": t} for raw, (k, t) in keyed.items()}

    def resolve(self, raw):
        """-> {"key", "name", "ticker"} or None for empty input."""
        if not raw or not raw.strip():
            return None
        raw = raw.strip()
        if raw not in self.seen:
            self.observe(raw)
        if self._cache is None:
            self._build()
        return self._cache[raw]


def _selftest():
    r = Resolver({"Meta Platforms": "Meta", "SK Hynix": "SK Hynix (000660.KS)"})
    raws = ["Nvidia (NVDA)", "NVIDIA", "Nvidia", "Meta Platforms (META)", "Meta", "Meta (META)",
            "CoreWeave (comparison)", "CoreWeave (CRWV)", "TSMC", "TSMC (TSM)", "SK Hynix",
            "Berkshire Hathaway (BRK.B)", "Z.AI", "Z.ai", "Anthropic (via Claude)", "Anthropic",
            "Amazon / Google (hyperscalers)", "FDIC"]
    for x in raws:
        r.observe(x)
    k = lambda x: r.resolve(x)["key"]
    assert k("NVIDIA") == k("Nvidia (NVDA)") == "NVDA" and r.resolve("NVIDIA")["name"] == "Nvidia"
    assert k("Meta Platforms (META)") == k("Meta") == "META" and r.resolve("Meta Platforms (META)")["name"] == "Meta"
    assert k("CoreWeave (comparison)") == "CRWV"
    assert k("TSMC") == "TSM", "learned ticker must beat bare-ticker parse"
    assert r.resolve("SK Hynix")["ticker"] == "000660.KS"
    assert r.resolve("Berkshire Hathaway (BRK.B)")["ticker"] == "BRK.B"
    assert k("Z.AI") == k("Z.ai") == "z.ai"
    assert k("Anthropic (via Claude)") == k("Anthropic") == "anthropic"
    assert r.resolve("Amazon / Google (hyperscalers)")["name"] == "Amazon / Google"
    assert r.resolve("FDIC")["ticker"] is None
    print("entities selftest ok")


if __name__ == "__main__":
    _selftest()
