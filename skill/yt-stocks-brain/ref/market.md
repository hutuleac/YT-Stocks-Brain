# Market briefs (`META["category"] == "market"`)

Load when the video has any investing/market content (the default).

- **`category: "market"`** (investing/AI-news mix, stocks/funds/macro): `color` is a stance signal
  — `green`=positive/bullish/confirmed-good, `amber`=mixed/contested/one-eye-open, `gray`=
  speculative/low-confidence, `red`=negative/bearish/red-flag. `badge`/`status` use conviction
  language: `badge` e.g. "High conviction" / "Contested" / "Speculative" / "Confirmed event";
  `status` e.g. "HOLDING — reduced but not exited", "RELEASED July 27, 2026". Per-entity `stance`
  and `conviction` (fields on each `names` entry, vocabulary above) are never inferred — label only
  what's explicitly said. Conviction `High` = clear thesis + explicit action/holding + repeated
  emphasis; `Medium` = clear view + some reasoning, no confirmed action; `Low` = passing/
  speculative. For any publicly-tradeable entity
  in `names`, write `"Company (TICKER)"` (e.g. `"Nvidia (NVDA)"`, `"RSP"` for a bare-ticker ETF) —
  the index's cross-reference view parses this pattern into a per-ticker mention history across
  every brief. Several tickers sharing one bullet get comma-separated in `name`, e.g. `"Apollo,
  BlackRock, KKR"`, so each gets its own index entry.

  **`names` is the permanent cross-reference index, not a general "notable things" slot.** Every
  entry becomes a row in the By Company/Ticker view spanning every brief in the library, forever.
  Companies, funds and organizations belong there — and so do investable asset classes/commodities
  the speaker takes a position on (crypto — `"Bitcoin (BTC)"`, `"Ethereum (ETH)"` — and metals/ETFs
  — `"Gold"`, `"Silver"`, `"GLD"` — are explicit, confirmed exceptions; this was a standing
  instruction, not a default). Countries, regions, and non-investable product/model names or
  technologies still do NOT belong there — put those in `bullets`. A `names` entry of `"Australia,
  Chile, Mexico"` creates three country rows in the ticker index; `"Natrium, BWRX-300"` creates two
  rows for reactor designs that aren't companies. Use the comma-split deliberately: only when you
  genuinely want each side indexed separately (a bloc like `"JPMorgan (JPM), Goldman Sachs (GS)"`
  is the intended use); otherwise join with `/` or a word, e.g. `"Natrium / BWRX-300 class"`.

  **Use the plain canonical form for a company you've named before, not a decorated variant.**
  The index groups rows by exact string match, so `"Nvidia"` and `"NVIDIA"`, or `"CoreWeave"` and
  `"CoreWeave (comparison)"`, become two separate rows for the same company instead of one combined
  history. Default to the bare `"Company (TICKER)"` form; only append a parenthetical qualifier
  (`"(supply chain)"`, `"(comparison)"`) when the distinction is actually load-bearing for that
  entry, and prefer folding that nuance into the `blurb` instead. When unsure what form a company
  has used before in this library, a quick check keeps it consistent:
  `python3 -c "import json;d=json.load(open('library.json'));print(sorted({e['display'] for b in d['briefs'] for e in b['entities'] if 'nvidia' in e['display'].lower()}))"`
  (swap the search term). This is a forward-looking hygiene habit, not a mandate to go back and
  fix older entries — existing variant rows are left as-is unless the user asks for a cleanup pass.
  Since Oct 2026 every entity string resolves through the repo's identity registry
  `kb/entities.json` (`scripts/entities.py`): case, trailing qualifiers and known tickers merge
  automatically. A split row that still shows up is fixed by moving the stray variant into the
  right entity's `aliases` there — never a per-brief workaround. Keys are permanent; edit
  `name`/`ticker`/`kind`, never the key.
