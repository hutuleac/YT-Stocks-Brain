---
name: yt-stocks-brain
version: 1.1.0
metadata:
  author: Peter <peter@example.com>
  tags: [youtube, research, transcript, brief, investing, knowledge-graph]
allowed-tools: Read, Write, Bash, Grep, Glob
description: |
  Turn a YouTube video into a clean, standalone HTML + JSON research brief built from the transcript, organized by theme rather than fixed category tables. Handles investment/market videos, tech/AI workflow videos, lifestyle/recommendation videos (supplements, workouts, products), and any mix of these. Use whenever the user gives a YouTube URL and wants a structured research summary. Triggers on: youtube link, "research this video", "analyze this youtube", "summarize the transcript", "make the HTML for this video".
---

# YT Stocks Brain — YouTube Research Brief

Generate a structured, evidence-based, mobile-friendly research brief (HTML + JSON) from any
YouTube video. The content of a video can be investing/market commentary, AI/tech workflows,
lifestyle/product recommendations, quotes-and-culture, or (most often) a mix — the brief adapts
to whichever mix of that is actually in the transcript instead of forcing every video through
the same fixed table set.

## When to use
- User pastes a YouTube URL and asks to "analyze", "research", "summarize", or "do the HTML for" a video.
- User wants a conviction map, stocks/companies breakdown, workflow extraction, product/supplement
  recommendations, or notable quotes from a talk/interview/market update/podcast.

## Workflow (do this in order)

### 1-2. Fetch, check for duplicates, clean (one call)
```bash
python3 <skill-folder>/scripts/start.py "URL_OR_ID" <scratchpad-dir>
```
Exits `EXISTS: <folder>` if the video is already in `research-data/` (stop, tell the user). Otherwise
it prints metadata, fetches captions with yt-dlp (falling back to `youtube-transcript-api` on 429
or failure), cleans to `<id>.en.txt` (timestamps stripped, rolling duplicates collapsed) and
prints `flag:` lines for possible sponsor paragraphs and a cut-off ending. Read the full `.txt`,
never the raw `.srt`. If there are no usable captions, use the **local-whisper** skill
(`~/.claude/skills/local-whisper/SKILL.md`); it writes the same `VID.<lang>.srt`. If captions truly
fail, state the limitation at the top of the brief. **Romanian video:** read `ref/romanian.md`.

### 3. Read for coverage, not just gist — track where every fact will land
Free-form themes have no fixed-table safety net (no guaranteed Conviction Map / Companies / Tech /
Quotes slot), so the real risk isn't missing the gist — it's silently dropping specific numbers,
analogies, and comparisons while compressing a rich transcript into 3-6 cards. Read the whole
cleaned transcript once, and as you read, register every discrete, evidence-carrying fact worth
keeping and roughly which Section 4 theme it belongs to: named numbers/metrics (not just headline
ones), named companies/products (even in passing comparisons), explanatory analogies the speaker
uses (these carry real reasoning, not just color), standalone-quotable lines, opinions the speaker
would be on the hook for (hot takes, contrarian calls, dated predictions — these feed `HOT_TAKES`),
named sources, dates, or forward-looking claims — and the four things the knowledge graph is
built from: **an explicit stance on a named asset** (owns / buying / watching / positive /
negative, plus how strongly and over what horizon — feeds per-entity `stance`), **any call with a
number or a date attached** (feeds `CLAIMS`), **any stated tie between two named entities**
(acquires, partners, supplies, invests in, competes with — feeds `RELATIONS`), and **who said it**
when speakers disagree (attribute the bullet to the speaker; a panel disagreement is signal, not
noise). Also register upcoming catalysts the speaker points at (an earnings date, a launch, a
ruling, a rate decision) — those go in `CLAIMS` with the date as `by`. For a short, single-topic video a direct read-and-place pass is
enough; past the thresholds below, write the list.

For a transcript over ~50k characters, a multi-speaker panel or many distinct stories,
write the inventory and run the checker: read `ref/long-video.md`. Either way, a fact that doesn't
fit any theme goes to `OTHER_NEWS` or `GLOSSARY`, never dropped for being "minor". If a theme's
bullet cap is too tight, the thread is two themes.

### 4. Identify the video's content mix, then find THEMES (not fixed tables)
First, classify what's actually in the transcript — most videos are a mix of:
- **Market/investing**: positions, conviction, stocks/funds, macro calls
- **Tech/AI**: workflows, tools, prompts, product/model releases
- **Lifestyle/recommendations**: products, supplements, workouts, media, travel, habits
- **Culture/quotes/geopolitics**: opinions, notable quotes, non-investment news

Set `META["category"]` from this classification: `"market"` when investing/market content is
present at all (even mixed with other types — this is the default and covers most videos), or
`"dev"` when the video is dev/systems/knowledge/AI-workflow content with no market angle (e.g. a
career-advice or coding-practice video like "Why Most Devs Stop Improving"), or `"life"` when the
video is knowledge-sharing and perspective content about life, family, parenting, mindset,
relationships, creativity or business/founder wisdom with no primary investing angle (e.g. a
founders-podcast riff on habits, systems and stories). Tie-break: `market` if there's an
investable angle worth indexing; otherwise `dev` for tools/workflows/craft, `life` for
perspectives and personal frameworks. This one field decides
which `index.html` tab the brief appears under (Section 6) and which color/badge vocabulary applies
below.

Then read across the WHOLE transcript and group related facts into **3-6 self-contained themes**
— a theme is a real topic thread the speaker returns to (e.g. "a hedge fund unwind," "the
hyperscaler capex debate," "a new harness-design practice," "a supplement stack change"), not a
content-type bucket. A theme pulls together whatever applies to it: a stance/conviction if it's
an investment view, a company/product mini-profile, a pull-quote, a "not settled yet" watch-flag,
a reusable workflow — all in one card. This is the single most important step: it replaces the
old pattern of splitting the same facts across a Conviction Map table, a Companies table, a Tech
table, and a Quotes section. **If a fact would appear in two theme cards, it belongs in whichever
one it's most central to — mention it once, not twice.**

For each theme, capture:
- `id` (short anchor slug), `color`, `badge`, `status` — see the category-conditional rules below;
  these three fields carry different meaning depending on `META["category"]`.
- `tags` — 1-3 sector/topic tags from the fixed list in `generate.py` (`TAGS`: `ai-infra`, `semis`,
  `software`, `macro-rates`, `crypto`, `energy`, `space`, `biotech`, `robotics`, `geopolitics`,
  `policy`, `consumer`, `finance`, `dev-workflow`, `career`, `health`, `family`, `parenting`,
  `mindset`, `relationships`, `romania` — the one regional tag, see Romanian-language videos). These aggregate across
  briefs in the graph, so never coin a new one per video — the generator warns on unknown tags;
  if none fits, pick the nearest and move on.
- `title` — a specific, concrete headline (not a category name)
- `lead` — one bold sentence giving the point before any detail. The whole line already renders
  bold via CSS — don't wrap it in `**...**`, that's redundant (harmless if you do, just pointless).
- `bullets` — 3-5 short, concrete, evidence-carrying bullets as the norm; flex to 6-7 rather than
  cutting a fact when a thread is genuinely dense (e.g. an earnings-call theme with many distinct
  guided figures) — never a dense paragraph either way (see Section 7).
  **Emphasis for scanning:** text fields across the brief (bullets, `SNAPSHOT`, `TAKEAWAYS` titles,
  `OTHER_NEWS`) support `**bold**` and `*italic*` markdown. The renderer also auto-bolds
  the first `$`-amount, `%`, or `(TICKER)` in each bullet/snapshot/news line for you — don't
  hand-bold those, you'll just get a redundant nested tag. Reach for manual `**bold**` only on a
  bullet that has no such figure but still has one keyword worth anchoring the eye on (a named
  company, a dated claim, "non-consensus", etc.) — one bold phrase per line, never more; the point
  is a single scannable anchor, not emphasis for its own sake. `HOT_TAKES` and theme `quote` text
  render markdown too but get no auto-bold — leave those as clean verbatim quotes.
- `quote` (optional) — the single best verbatim quote for this theme, or none
- `watch` (optional) — an explicit "this isn't settled" caveat when the speaker themselves
  hedges, **or** a conflict of interest / undisclosed position that colors this theme's claim
  (e.g. "he sells the compute both sides of this debate run on"). Provenance lives here, next
  to the claim it affects — there is no separate caveats section. Never audit vocabulary
  (`unverified`, `uncorroborated`) and never tell the reader to go verify; label, don't grade.
- `names` (optional) — see the category-conditional rules below; omit entirely (`None`) when a
  theme has no company/product/person worth naming, which is common and fine outside `market`.
  Each entry is `{"name", "blurb", "stance", "conviction", "horizon"}`. `stance` is one of
  `OWNS` / `BUYING-ADDING` / `WATCHING` / `POSITIVE VIEW` / `NEGATIVE VIEW` / `CASUAL MENTION` /
  `UNCERTAIN`, `conviction` is `High` / `Medium` / `Low` / `None`, `horizon` is short text
  (`"12-18 months"`, `"by 2030"`) or `None`. **This per-entity stance is what the ticker index and
  the graph read** — the theme's `color`/`badge` describe the thread, not each name in it, and a
  bullish name can sit inside a red-flag theme. Only label what's explicitly said; a name merely
  mentioned gets `CASUAL MENTION` with `conviction: None`.

**Category vocabulary.** `market` → read `ref/market.md` (stance colors, conviction, `names`
hygiene, ticker format). `dev` / `life` → read `ref/non-market.md`. A market video with a large
health/life/workflow stretch stays `market`; give those themes the non-market badge
vocabulary and no `names`.

  **Never write a name you can only reach by guessing through a garbled caption.** Auto-captions
  mangle proper nouns constantly (ERCOT→"Urkott", FERC→"FK", Cerebras→"Cerrus", Cagney→"Kagny",
  Warsh→"Worsh", KOSPI→"Cosby"). Resolving an obvious one is fine; guessing at a company you can't
  identify is not, because `names` and tickers are durable index data and a wrong entry is
  permanent damage. When you can't identify a company with confidence, describe it by spec in a
  bullet ("a ~10 MW micro-reactor firm building five-unit pods") and leave it out of `names`,
  `CLAIMS` and `RELATIONS` entirely.

MANDATORY — capture non-investment signal too, wherever it fits best (inside a theme if it's
central to one, otherwise in Other Notable News): strong convictions/opinions on any topic,
recommendations (products, tools, supplements, workouts, media, travel, safety), notable
non-stock news (cybersecurity, energy, space, science, health, policy, culture), and any
standout verbatim quotes not already used inside a theme.

MANDATORY — capture references to other sources by name: any other podcast, show, channel,
publication, article, book, or person the speakers cite as where a claim or number came from, or
name as someone they follow/trust/recommend (e.g. "I heard this on the All-In podcast," "Bloomberg
reported," "this is the Joshua Kushner framework"). If the reference is central to a theme (it's
where that theme's key fact or figure came from), fold it into that theme's bullets or `quote` —
don't create a parallel section for something that already has a home. If several small references
don't anchor to any one theme, group them into a single `OTHER_NEWS` entry (e.g. "Sources referenced
this episode: ..."). A show naming zero outside sources is common and fine — say so briefly rather
than leaving the reader to wonder if you missed something; never pad this out with vague "as
reported elsewhere" hand-waving when no specific source was named. Vague attributions ("some
people," "you often hear") are opinions to capture in bullets, not references — only capture a
named source or a named person's stated view.

EXCLUDED — sponsor content never goes in the brief. Skip paid sponsorship segments, "this video
is sponsored by" reads, host-endorsed sponsor products/tools, and sponsor discount codes/links
entirely — do not give them a theme, an OTHER_NEWS entry, a CLAIMS row, a RELATIONS edge, or a GLOSSARY term. If
a sponsor segment interrupts an otherwise substantive discussion mid-transcript, skip only the
sponsor material and continue capturing the surrounding content normally.

### 5. Fill in the remaining sections
- `SNAPSHOT` — 5-8 scannable bullets, the one-paragraph read of the whole video (unchanged from
  before; this is a bulleted list, never one dense paragraph).
- `TAKEAWAYS` — 4-6 short, imperative, DISTINCT actions. If a takeaway just restates a theme's
  bullet verbatim, cut it — takeaways are the "so what do I do" layer, not a recap. `tag` is a
  short topic category (1-3 words: "Markets", "Macro", "AI ethics", "Health", "Energy",
  "Geopolitics", "Crypto", "Robotics", "Space", "Policy", "Careers" — coin another short category
  when none fit, but keep it a topic label, not an action verb like "Watch" or "Track"; the
  imperative verb belongs in `title` itself). It renders inline, leading the takeaway text on the
  same line ("Markets: Track RSP and IGV first...") — never a separate line below.
- `CLAIMS` — the graph's checkable-predictions layer: one row per call that carries a number
  or a date, `{"who", "claim", "metric", "target", "by", "condition", "entity"}`. `who` is the
  speaker; `claim` is one plain sentence; `metric`/`target`/`by` hold the checkable part split out
  ("China native lithography" / "achieved" / "2030"; "Nvidia NeoClouds" / "50-1,000" / None) — at
  least one of the three is filled; `condition` is the speaker's own "if" or `None`; `entity` is
  the `"Company (TICKER)"`, asset, or region the call is about, or `None`. Include upcoming
  catalysts the speaker points at (earnings dates, launches, rulings) with the date as `by`.
  Write `who` as the speaker's full name (`"David Sacks"`, not `"Sacks"`; several speakers
  joined with ` / `; provenance in parens: `"Polymarket (cited by Jason Calacanis)"`) and `by` as
  an ISO date or month (`"2026-10-30"`, `"2026-12"`) whenever the speaker gave one — relative
  spans ("12-18 months") are fine when that's all they said. Both feed per-speaker track
  records with real due dates in `kb/brain.db`.
  A claim that already lives in a bullet or hot take still gets a row here — this section is
  structure over the same material, so the no-duplicate rule does NOT apply. Numbers stated as
  history ("we did $400B last quarter") are bullets, not claims; a claim is something the future
  can prove wrong.
- `RELATIONS` — edges between named entities as stated in the video:
  `{"from", "rel", "to", "note"}` with `rel` from the fixed set `acquires` / `invests_in` /
  `partners_with` / `supplies` / `customer_of` / `competes_with` / `owns_stake` / `endorses` /
  `criticizes`. `from`/`to` use the same canonical `"Company (TICKER)"` string as `names` so the
  graph can join them. Only stated relationships — a comparison in passing is not an edge.
  `note` is one short clause or `None`. Empty is fine when the video names none.
- `HOT_TAKES` — 0-6 opinions the speaker personally owns and would be quoted on: hot takes,
  contrarian/unpopular calls, personal convictions, dismissals ("X is dead", "nobody needs Y"),
  and predictions carrying a number or a date. Shape: `{"take": ..., "cite": "— Speaker",
  "why": short context}`. `take` is verbatim or near-verbatim, tightened only for caption noise —
  never paraphrased into neutral prose, because the value here is the speaker's own phrasing and
  the risk they took saying it. Only `take` and `cite` render on the page — `cite` sits inline
  right after the take, same line, not on its own line below — and `why` is kept in the data file
  purely as your own drafting/vetting aid (the exposure test below), never shown to the reader.
  **The test is exposure, not volume:** would a reasonable listener disagree, or is the speaker
  on the hook if it's wrong? A number, date, or ranking makes it a take; "AI is important"
  does not. Include takes on any subject, not just the investable ones.
  This section is a lens on material that mostly already lives in the themes, so the Section 4
  no-duplicate rule does NOT apply to it — a line can be a theme's `quote` and a hot take. Do not
  invent a separate theme bullet just to host one. If a video is pure reporting with no
  neck-out opinions, leave it empty and let the placeholder say so.
- `OTHER_NEWS` — only items that don't fit inside any theme. If everything folds into a theme,
  it's fine for this section to end up short or empty — never pad it.
- `GLOSSARY` — compact term/definition pairs, tightened to one sentence each.

Any list left empty renders an honest "nothing found" placeholder — never fabricate content to
fill a section.
### 6. Generate and finish
Copy `<skill-folder>/scripts/TEMPLATE.py` to the scratchpad, fill it in, then:

```bash
python3 <skill-folder>/scripts/generate.py <data-file>.py
python3 <skill-folder>/scripts/finish.py <slug-substring> --src <scratchpad-dir> [--kind key=kind ...]
```
`generate.py` writes the `.html`, `research-data/<slug>/` json plus archived data file, and rebuilds
`index.html`, `library.json` and the KB. A new entity prints `warning: new entity '<key>' ... set its
kind`. `finish.py` copies the transcripts into the slug folder, sets kinds from `--kind key=kind`
(company / fund / crypto / commodity / person / country / government / org / product / group /
other), regenerates, prints the entity list, refuses to commit while a new entity is still
`unknown`, then commits and pushes with no Co-Authored-By trailer. Add `--no-push` to hold.
Output layout, index tabs and correction passes: `ref/outputs.md`.

### 7. Quality check before finishing
- Re-scan the full cleaned transcript against the drafted data lists: every named number, company/
  product, analogy, standalone quote, and forward-looking claim you noted in Section 3 is placed in
  a theme, `OTHER_NEWS`, or `GLOSSARY`. If you wrote an explicit inventory list, check every line
  off; anything unchecked (or, without a written list, anything you notice on re-scan that isn't
  represented) gets added, not dropped for length.
  For long videos, run the checker in `ref/long-video.md`.
- Entities (printed by `finish.py`): every row is a company, fund, organization or investable
  asset. A country, product name or concept means that `names` entry moves into `bullets`.
- Graph fields are complete and vocabulary-clean: every `names` entry in a `market` brief has a
  `stance`; every `CLAIMS` row has `who` plus at least one of `metric`/`target`/`by`; every
  `RELATIONS` row uses a verb from the fixed set and canonical entity strings; every theme has
  `tags`. `generate.py` prints a `warning:` line for any unknown tag, stance or verb — a clean
  run has none.
  Ticker conflict warning = a typo in the brief or a real new listing (update `ticker` on the
  entity). A split row is fixed by moving the alias onto the right entity in `kb/entities.json`.
- A correction pass that edits a claim's `who` or `claim` text re-keys it (`claim_id` hashes
  both); if `kb/claim_outcomes.json` already has a verdict for it, the orphan warning names the
  old id — move the verdict to the new id.
- No fact appears in two theme cards (see the dedup rule in Section 4). `HOT_TAKES` is exempt —
  it deliberately re-surfaces lines that also live in a theme.
- `HOT_TAKES` entries are verbatim/near-verbatim and each one would actually make someone
  disagree or hold the speaker to it. A bland consensus statement in there means it should be cut.
- Every major claim has transcript evidence; ownership/buying intent is never inferred.
- Conflicts of interest sit in the relevant theme's `watch`, not in a bullet and not dropped.
- Bullets are short and concrete — no dense multi-sentence paragraphs inside a theme.
- HTML well-formed, closes `</html>`.
- Working folder root only gained the `.html`; transcript/JSON live in `research-data/<slug>/`.

## Weekly memo
When `generate.py` prints `memo due:`, write it after the brief is committed: `ref/weekly-memo.md`.
`generate.py` itself is never edited per video; the page design lives in its HTML/CSS comment block.
