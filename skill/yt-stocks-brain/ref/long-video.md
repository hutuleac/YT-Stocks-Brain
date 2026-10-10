# Long or dense videos: written inventory + coverage check

Load when the cleaned `.txt` exceeds ~50k characters, or the video is a multi-speaker panel, covers many distinct stories, or the user asked for exhaustive coverage.

## Inventory (before drafting themes)
Write an explicit flat inventory list before drafting themes — one line per fact, checked off
against the drafted `bullets`/`quote`/`watch`/`names` once themes are written — whenever **any** of
these holds: the cleaned `.txt` exceeds ~50k characters (`wc -c` it after Section 2); the video is a
multi-hour or multi-speaker panel; it covers many distinct stories; or the user asked for
exhaustive/"deep" coverage. Don't agonize over the call — a 59-minute single-guest interview at 63k
chars still surfaced facts that a read-and-place pass had dropped. Put the inventory in the
scratchpad directory, not the project.

## Coverage check (after generating)
**Do this against the inventory file itself, line by line — not against your memory of the
  themes.** Recalling what you wrote and believing it complete is how facts get dropped. When you
  wrote an inventory, run the bundled checker instead of eyeballing it:
  ```bash
  python3 <skill-folder>/scripts/check_coverage.py <inventory.md> <slug-substring> --ignore=SpeakerSurname
  ```
  It pulls distinctive tokens (numbers-with-units, proper nouns) out of every `- [ ]` line and
  reports any fact with no trace in the generated brief JSON; exit code 1 means something is
  unplaced. Point it at the slug, never at `library.json` — that file is only the manifest and
  contains no bullets, so checking against it reports nearly every fact as missing. Each flag is a
  candidate, not a verdict: a paraphrase can land fine and still trip it, and a clean run doesn't
  prove nothing was watered down. Read every flag before editing. **A fact is never
  dropped for being "minor."** If a theme's bullet cap won't hold everything that belongs there,
  the thread is two themes — that is not a licence to cut. Anything that fits no theme goes to
  `OTHER_NEWS` or `GLOSSARY`, or gets appended to the most closely related existing bullet.
