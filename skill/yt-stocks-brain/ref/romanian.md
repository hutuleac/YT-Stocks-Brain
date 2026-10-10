# Romanian-language videos

Load when the video is Romanian.

`start.py` fetches English captions; for Romanian run yt-dlp with `--sub-lang ro` (or `fetch_transcript_api.py ID ro`), then `clean_transcript.py`.

Write the brief in **English** — snapshot, themes, claims, glossary, everything the search, Signals and graph read
(changed Oct 2026: Romanian briefs were invisible to English search and their claims couldn't
group with the rest). Keep the speaker's own words in Romanian: theme `quote` text and `HOT_TAKES`
`take` stay verbatim Romanian, **without diacritics** (ș→s, ț→t, ă→a, î/â→i/a). The video `title`
stays as published. Set `META["region"] = "ro"` so the brief lands on the **Romania** tab, and
add the `romania` tag only to themes about Romania itself (the leu, local airlines, Cernavoda) —
a Romanian show's Micron or Anthropic story is a global theme and gets global tags only.
