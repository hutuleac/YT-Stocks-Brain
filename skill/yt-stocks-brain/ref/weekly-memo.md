# Weekly memo

When `generate.py` prints `memo due:` (no memo yet this ISO week and the last is 6+ days old),
write it in the same session, after the brief is committed. The user wants **direction, not
precision**: which narratives are emerging, which are fading, and which new names appear. Never score predictions here.

1. `python3 <skill-folder>/scripts/memo.py context > <scratchpad>/memo_ctx.md` and read all of
   it (Read in chunks). This creates `memos/<ISO-week>.json` with the signals snapshot embedded and
   `briefs` = the brief files this memo covers (every brief no earlier memo listed, so briefs made
   after the last memo or old videos briefed late are never skipped). Don't edit `signals` except
   `label` (step 2) and don't edit `briefs`.
2. Fill `title`, `summary` (2-3 sentences, the answer), `insights` (3: each a headline claim,
   3-5 evidence bullets with the numbers from the context, `evidence` = brief `.html` files) and
   `watch` (3-5, prioritized, each with why it's worth a closer look, and `entities` = the
   registry keys it's about, shown in `[key]` in the context — next week's memo follows them up
   automatically). Connect dots across narratives: an insight that explains *why* several of them
   move together beats a list of movers. Name contrarian setups (falling attention vs a still-rising
   thesis), conflicts of interest, and thin evidence (one channel, one brief) plainly. Use the
   context's "Last memo's watch list, followed up" and "Trajectory" lines instead of re-deriving them.
   Narratives are auto-built entity clusters: give each one you cite a human name in prose and set
   the same name as `label` on that narrative in `signals.narratives` ("private credit / alt
   managers"). Labels carry forward to matching clusters in later memos, so names stay stable
   across weeks and in the monthly trajectory.
3. `python3 <skill-folder>/scripts/memo.py render memos/<ISO-week>.json` → `memos/<week>.html`,
   index rebuilt with the link on the Signals tab. "What moved", "Trajectory" and the watch-list
   follow-up are computed, not written.
4. Commit `memos/` with the message `Add weekly memo <ISO-week>: <title>` and a short body, then push.

## Monthly memo

When `generate.py` prints `memo due: monthly memo for <YYYY-MM>` (last month has weekly memos and
no monthly one), write it after the weekly memo, if one is due too.

1. `python3 <skill-folder>/scripts/memo.py month <YYYY-MM> > <scratchpad>/month_ctx.md` and read
   it: every weekly memo of the month (summary, insights, watch), the month's computed diff and
   each narrative's trajectory across the month's weekly memos. Creates `memos/<YYYY-MM>.json`.
2. Fill only `title` and `summary` (3-4 sentences): the month's arc (what it opened on, what it
   closed on), the steadiest narrative, what spiked and vanished (say when it was one or two
   voices), and the open thread into next month. Numbers come from the trajectory lines.
3. `python3 <skill-folder>/scripts/memo.py render memos/<YYYY-MM>.json`, then commit
   `Add monthly memo <YYYY-MM>: <title>` with a short body and push.
