# What generate.py writes

Outputs (channel-first naming so same-creator videos group together in Finder/`ls`, with the
upload date giving chronological order within each creator):
- `<slug-channel>_<date>_<slug-title>.html` — standalone, responsive brief, written to the
  **current working directory**.
- `<slug-channel>_<date>_<slug-title>.json` — same structured data, written to
  **`research-data/<slug-channel>_<date>_<slug-title>/`** (created automatically).
- `<slug-channel>_<date>_<slug-title>_data.py` — an archived copy of the data file you passed
  in, written to that same `research-data/<slug>/` folder, so the brief can be regenerated or
  hand-edited later without re-deriving it from the transcript.
- `index.html` — rebuilt at the **working directory root** every run: a single searchable page
  with tabs — **All Briefs** (chronological, every category), **By Channel**, **By Company /
  Ticker**, **Quotes & Takes**, **Dev & Workflows** (`category == "dev"` only), **Life &
  Perspectives** (`category == "life"` only) and **Romania** (`region == "ro"`). The ticker view
  parses every theme's `names` field (current schema) or `conviction_map` topic (legacy schema)
  into a cross-reference: click a ticker's group to see every brief that mentioned it, with date,
  channel, per-entity stance/conviction/horizon, and blurb — this is what turns a growing pile of briefs into an
  investing-thesis tool instead of just a list of pages. Run `python3 <skill-folder>/scripts/generate.py
  --reindex` to rebuild it standalone (e.g. after manually deleting or renaming a brief).
- `library.json` — rebuilt alongside `index.html` at the **working directory root**: a flat
  machine-readable manifest of every brief plus its tags and extracted ticker/company entities
  (with stance/conviction/horizon), meant to be fed directly into an external AI/knowledge-graph
  tool. `CLAIMS` and `RELATIONS` live in each per-brief `.json` under `research-data/`.

Filename convention: lowercase, non-alphanumerics → single hyphen, diacritics stripped, date as
`YYYY-MM-DD` (from `META["date"]`). Example: `jordi-visser_2026-08-09_the-ai-crash-is-over.html`.
After generating, move the raw transcript and cleaned `.txt` into that same `research-data/<slug>/`
folder, and delete the data-file copy from the working directory root (the archived copy in
`research-data/` is the one that persists) — the working folder root should only ever gain the
finished `.html` plus the refreshed `index.html`.

**Fixing a brief after the root data file is gone:** edit the archived
`research-data/<slug>/<slug>_data.py` in place and run `generate.py` against that path. It
regenerates the `.html`, rewrites the `.json`, re-archives the data file over itself, and rebuilds
`index.html` + `library.json` — no need to copy anything back to the root. Use this for every
correction pass rather than re-deriving a fresh data file from the transcript.
