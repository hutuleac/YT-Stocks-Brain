# Weekly memo

When `generate.py` prints `memo due:` (no memo yet this ISO week and the last is 6+ days old),
write it in the same session, after the brief is committed. The user wants **direction, not
precision**: what is emerging, turning, contested, connecting. Never score predictions here.

1. `python3 <skill-folder>/scripts/memo.py context > <scratchpad>/memo_ctx.md` and read all of
   it. This creates `memos/<ISO-week>.json` with the signals snapshot embedded (don't edit
   `signals`).
2. Fill `title`, `summary` (2-3 sentences, the answer), `insights` (3: each a headline claim,
   3-5 evidence bullets with the numbers from the context, `evidence` = brief `.html` files) and
   `watch` (3-5, prioritized, each with why it's worth a closer look). Connect dots across
   lenses: an insight that explains *why* several signals move together beats a list of movers.
   Name contrarian setups (falling attention vs a still-rising thesis), conflicts of interest,
   and thin evidence (one channel, one brief) plainly. The context's `narratives` are auto-built
   entity clusters labeled only by member names: give the ones you cite a human name in prose
   ("private credit / alt managers", "memory + optics supply chain").
3. `python3 <skill-folder>/scripts/memo.py render memos/<ISO-week>.json` → `memos/<week>.html`,
   index rebuilt with the link on the Signals tab. "What moved since the last memo" is computed
   from the previous memo's snapshot, not written.
4. Commit `memos/` with the message `Add weekly memo <ISO-week>: <title>` and push.
