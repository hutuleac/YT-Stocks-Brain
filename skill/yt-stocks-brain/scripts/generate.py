#!/usr/bin/env python3
"""
YouTube Research Brief generator (v3 — data-file driven, theme-grouped, mobile-first).

This script never needs editing per video. Instead, create a per-video data file
(copy TEMPLATE.py, fill in META / SNAPSHOT / THEMES / TAKEAWAYS / HOT_TAKES / CLAIMS /
RELATIONS / OTHER_NEWS / GLOSSARY — see SKILL.md Sections 3-5 for what each field means), then:

    python3 generate.py <data_file.py>

Writes:
  <slug-channel>_<date>_<slug-title>.html       -> current working directory
  <slug-channel>_<date>_<slug-title>.json       -> research-data/<same-slug>/
  <slug-channel>_<date>_<slug-title>_data.py     -> research-data/<same-slug>/ (archived copy
                                                     of the data file, so the brief can be
                                                     regenerated or edited later)
  index.html                                     -> current working directory, rebuilt from
                                                     every research-data/*/*.json found

Rebuild just the index (e.g. after manually deleting/renaming a brief) without generating
a new one:

    python3 generate.py --reindex

---------------------------------------------------------------------------------------------
HTML/CSS DESIGN — "Editorial Refined, Theme-Grouped" (v2). Implemented below; not reasoned
about per-brief. Only read this if you're actually changing the template/CSS, not when writing
a data file for a video.
---------------------------------------------------------------------------------------------
- Single page, full page width (max ~1600px), cream body (--bg:#efece2) with a warm white page
  card (--card:#fffdf8) and warm line color #e4e2d8 — no dark hero banner.
- Serif headlines (Iowan Old Style/Palatino Linotype/Georgia fallback) for titles, section heads,
  and quotes; system sans for body copy — this pairing is the "analyst report" read.
- Amber/brown brand accent (--brand:#8a5a2e) for kickers, italic eyebrows, and section-heading
  underlines. Header has NO separate "Watch on YouTube" button — it's a small inline link folded
  into the one-line stats row under the byline, to save space.
- Themes, not tables. The main content is a stack of theme-card <section>s (one per theme, 3-6
  total), each with: a color-coded status badge (solid fill, white text — not a pale tint — for
  genuinely obvious at-a-glance scanning) + a caps status line; a bold headline with a colored
  left accent bar in the theme's stance color; a bold one-line lead; 3-5 short bullets (never
  paragraphs) with a dot marker in the theme's color, in the main (left) column. Bullets/badge/
  title-bar all sharing one color per theme is what makes the coding "obvious" rather than
  decorative.
- Side column ("theme-side") is a stack of up to three "sidecards," always in this order:
  pull-quote, names-in-play, worth-noting. Every sidecard shares one shape (rounded card, thin
  colored left bar, small caps label) so the reader learns the pattern once — only the accent
  color changes, and that color is the fast-scan signal for what kind of side content it is:
  pull-quote uses the theme's own stance color (it's telling you more about this theme);
  names-in-play uses a fixed neutral slate #65695f (it's reference material, not a stance
  signal); worth-noting uses a fixed amber #93711b regardless of the theme's stance color (it
  always reads as "caution," even inside a green/high-conviction theme). Any of the three is
  omitted if the theme has nothing for it — never an empty card.
- Stance colors (theme accent bar, badge, bullet dots, pull-quote sidecard only): green
  #3f6b2e = positive/confirmed-good, amber #93711b = mixed/contested/one-eye-open, gray
  #65695f = speculative/low-confidence, red #a23f22 = negative/bearish. Names-in-play and
  worth-noting sidecards do NOT use the theme's stance color — they use their own fixed colors
  (above) so they stay visually consistent and scannable across every theme regardless of that
  theme's stance.
- No "Jump to a thread" nav strip — it was removed as low-value chrome that just ate vertical
  space; the reader scrolls straight from the snapshot into the theme cards.
- Takeaways and Other Notable News are icon-only cards (no colored side accent bar — keep those
  reserved for theme cards so the color-coding stays meaningful, not decorative everywhere).
  Claim/relation/hot-take boxes reuse one bordered card with a colored side accent bar. No
  warning-triangle glyph anywhere — a plain colored bar carries the "caution" meaning.
- Glossary renders as a grid-template-columns:repeat(auto-fill,minmax(260px,1fr)) grid — pure
  CSS, no media query needed, it reflows column count on its own as the viewport narrows.
- Mobile-first, no hidden columns. There is no data table anywhere in the main content, so
  there is nothing to hide on small screens. Layout is done entirely with flex-wrap:wrap + CSS
  grid auto-fill/auto-fit + clamp() for type/spacing — this reflows continuously from a phone
  (iPhone-width) to a full desktop window without a single @media breakpoint, and without ever
  cutting a column of information.
- No external deps, no JS frameworks, no CDNs.
"""
import glob
import html
import importlib.util
import json
import os
import re
import shutil
import sys
import unicodedata

from build_kb import DB_PATH as KB_PATH, build as build_kb
from signals import render as render_signals
from entities import Registry, split_list as _split_entity_list

sys.dont_write_bytecode = True  # don't litter the working directory with __pycache__

REQUIRED_FIELDS = ["META", "SNAPSHOT", "THEMES", "TAKEAWAYS", "OTHER_NEWS", "GLOSSARY"]
# HOT_TAKES / CLAIMS / RELATIONS are optional so data files written before they existed still
# regenerate. RISKS (removed) is silently ignored if an old data file still defines it.
OPTIONAL_LISTS = ["HOT_TAKES", "CLAIMS", "RELATIONS"]

# Knowledge-graph vocabularies. Data files must draw from these — unknown values print a
# warning (not a hard fail) so an old brief can never be blocked from regenerating.
TAGS = {
    "ai-infra", "semis", "software", "macro-rates", "crypto", "energy", "space", "biotech",
    "robotics", "geopolitics", "policy", "consumer", "finance", "dev-workflow", "career", "health",
    "family", "parenting", "mindset", "relationships",
}
REL_VERBS = {
    "acquires", "invests_in", "partners_with", "supplies", "customer_of", "competes_with",
    "owns_stake", "endorses", "criticizes",
}
STANCES = {
    "OWNS", "BUYING-ADDING", "WATCHING", "POSITIVE VIEW", "NEGATIVE VIEW", "CASUAL MENTION",
    "UNCERTAIN",
}


def load_data(path):
    spec = importlib.util.spec_from_file_location("video_data", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    missing = [f for f in REQUIRED_FIELDS if not hasattr(mod, f)]
    if missing:
        sys.exit(f"{path} is missing required field(s): {', '.join(missing)}")
    for f in OPTIONAL_LISTS:
        if not hasattr(mod, f):
            setattr(mod, f, [])
    for t in mod.THEMES:
        for tag in set(t.get("tags") or []) - TAGS:
            print(f"warning: theme '{t.get('id')}' has unknown tag '{tag}' (TAGS in generate.py)")
        for n in t.get("names") or []:
            st = n.get("stance")
            if st and st not in STANCES:
                print(f"warning: '{n.get('name')}' has unknown stance '{st}' (STANCES in generate.py)")
    for r in mod.RELATIONS:
        if r.get("rel") not in REL_VERBS:
            print(f"warning: relation {r.get('from')} -> {r.get('to')} has unknown rel '{r.get('rel')}'")
    return mod


# ---------------------------------------------------------------------------
# GENERATOR — should not need editing per video
# ---------------------------------------------------------------------------

STANCE_COLORS = {
    "green": "#3f6b2e",
    "amber": "#93711b",
    "gray": "#65695f",
    "red": "#a23f22",
}

CSS = """
:root{
  --ink:#20231f; --muted:#6b6f66; --line:#e4e2d8; --card:#fffdf8; --bg:#efece2;
  --brand:#8a5a2e; --serif:'Iowan Old Style','Palatino Linotype',Georgia,serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  font-size:clamp(15px,1.05vw,18px);line-height:1.7;-webkit-font-smoothing:antialiased;}
.page{max-width:1600px;width:100%;margin:0 auto;background:var(--card);box-shadow:0 0 0 1px var(--line);}
.hero{padding:clamp(18px,2.4vw,34px) clamp(18px,4vw,56px) clamp(14px,1.8vw,22px);border-bottom:1px solid var(--line);}
.kicker{font-family:var(--serif);font-style:italic;font-size:clamp(13px,1vw,16px);color:var(--brand);margin-bottom:10px;}
.backlink{margin-bottom:12px;}
.backlink a{font-size:clamp(12.5px,.95vw,14px);color:var(--muted);text-decoration:none;border:1px solid var(--line);
  border-radius:20px;padding:5px 14px;transition:color .15s,border-color .15s;}
.backlink a:hover{color:var(--brand);border-color:var(--brand);}
.hero h1{font-family:var(--serif);margin:0 0 14px;font-size:clamp(24px,3.4vw,42px);line-height:1.15;
  letter-spacing:-.01em;font-weight:600;color:#171916;max-width:42ch;}
.byline{border-top:1px solid var(--line);padding-top:12px;color:var(--muted);font-size:clamp(13px,1vw,15px);line-height:1.6;}
.byline b{color:var(--ink);font-weight:600;}
.stats-line{font-family:var(--serif);font-style:italic;color:var(--brand);font-size:clamp(12.5px,.95vw,14.5px);margin-top:4px;}
.stats-line a{color:var(--brand);}
.inner{padding:10px clamp(18px,4vw,56px) 48px;}
section.sec{padding:34px 0;border-bottom:1px solid var(--line);}
.sec-eye{font-family:var(--serif);font-style:italic;font-size:14px;color:var(--brand);margin-bottom:4px;}
.sec h2{font-family:var(--serif);margin:0;font-size:clamp(20px,2vw,26px);font-weight:600;color:#171916;
  border-bottom:2px solid var(--brand);display:inline-block;padding-bottom:5px;}
.card{background:#fbf7ef;border:1px solid var(--line);border-radius:14px;padding:clamp(18px,3vw,28px);}
.snap{list-style:none;margin:0;padding:0;}
.snap li{padding:12px 0;border-bottom:1px solid var(--line);line-height:1.6;font-size:clamp(14.5px,.95vw,16.5px);}
.snap li:last-child{border-bottom:none}
.theme{padding:36px 0;border-bottom:1px solid var(--line);}
.theme-badgerow{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-bottom:10px;}
.badge{display:inline-block;padding:5px 13px;border-radius:3px;font-size:12px;font-weight:700;
  white-space:nowrap;letter-spacing:.03em;text-transform:uppercase;color:#fffdf8;}
.theme-status{font-family:var(--serif);font-style:italic;font-size:13.5px;color:var(--muted);}
.theme h2{font-family:var(--serif);margin:0 0 20px;font-size:clamp(20px,2.2vw,28px);font-weight:600;
  color:#171916;line-height:1.25;max-width:32ch;padding-left:16px;}
.theme-body{display:flex;flex-wrap:wrap;gap:28px;}
.theme-main{flex:3 1 400px;min-width:0;}
.theme-side{flex:2 1 260px;min-width:0;}
.lead{margin:0 0 18px;font-size:clamp(16px,1.15vw,19px);line-height:1.6;color:#171916;font-weight:600;max-width:70ch;}
.bullets{list-style:none;margin:0 0 22px;padding:0;max-width:76ch;}
.bullets li{position:relative;padding:9px 0 9px 20px;border-bottom:1px solid var(--line);
  font-size:clamp(14px,.95vw,15.5px);line-height:1.65;color:#2c2f28;}
.bullets li .dot{position:absolute;left:0;top:16px;width:7px;height:7px;border-radius:50%;}
.sidecard{position:relative;background:#fffefb;border:1px solid var(--line);border-radius:12px;
  padding:14px 16px 14px 26px;max-width:76ch;margin:0 0 18px;}
.sidecard:last-child{margin-bottom:0;}
.sidecard::before{content:"";position:absolute;left:11px;top:12px;bottom:12px;width:7px;border-radius:5px;
  background:var(--sc-accent);}
.sidecard .lbl{font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  color:var(--sc-accent);margin-bottom:8px;}
.sidecard.quote{font-family:var(--serif);font-style:italic;font-size:clamp(15px,1.1vw,18px);
  line-height:1.5;color:#2c2f28;}
.sidecard.quote .lbl{font-family:-apple-system,sans-serif;font-style:normal;}
.sidecard.quote cite{display:block;font-family:-apple-system,sans-serif;font-style:normal;font-size:13px;
  color:var(--muted);margin-top:9px;}
.sidecard .txt{font-size:14.5px;line-height:1.55;color:#3a3d35;}
.namechip{padding:0 0 10px;margin:0 0 10px;border-bottom:1px solid var(--line);}
.namechip:last-child{padding-bottom:0;margin-bottom:0;border-bottom:none;}
.namechip b{display:block;font-weight:600;font-size:14.5px;color:#171916;}
.namechip span{font-size:13px;color:#4a4d44;line-height:1.5;}
.icardbox{background:#fffefb;border:1px solid var(--line);border-radius:12px;padding:2px 18px;}
.irow{display:flex;gap:14px;align-items:flex-start;padding:13px 0;}
.irow+.irow{border-top:1px solid var(--line);}
.irow .ic{flex:none;width:30px;height:30px;border-radius:6px;display:grid;place-items:center;
  font-size:14px;background:#f4e9db;line-height:1;}
.irow .title{font-weight:600;font-size:clamp(14px,.95vw,15.5px);color:#171916;line-height:1.42;}
.irow .tag{display:inline-block;font-family:var(--serif);font-style:italic;font-size:12.5px;font-weight:600;color:var(--brand);margin-left:6px;}
.irow .detail{font-size:13.5px;color:#4a4d44;line-height:1.55;margin-top:4px;}
.irow .tline{font-size:clamp(14px,.95vw,15.5px);line-height:1.48;}
.irow .tline .cat{font-family:var(--serif);font-style:italic;font-weight:700;color:var(--brand);margin-right:6px;}
.irow .tline .txt{font-weight:600;color:#171916;}
b{font-weight:700;}
i{font-style:italic;}
.riskcard{position:relative;background:#fffefb;border:1px solid var(--line);border-radius:12px;
  padding:14px 18px 14px 28px;margin:11px 0;}
.riskcard::before{content:"";position:absolute;left:11px;top:12px;bottom:12px;width:7px;border-radius:5px;background:#a23f22;}
.riskbox{position:relative;background:#fffefb;border:1px solid var(--line);border-radius:12px;
  padding:2px 18px 2px 28px;}
.riskbox::before{content:"";position:absolute;left:11px;top:14px;bottom:14px;width:7px;border-radius:5px;background:var(--box-accent,#a23f22);}
.riskbox .cmeta{font-weight:600;color:#2d6a4f;white-space:nowrap;}
.riskbox .rel{font-family:var(--serif);font-style:italic;color:#3b5b8c;}
.riskbox .tag{font-size:11px;color:#8a8d81;margin-left:6px;}
.namechip .stance{display:inline-block;margin-left:8px;padding:1px 7px;border-radius:999px;color:#fff;font-size:10.5px;font-weight:600;letter-spacing:.02em;vertical-align:middle;}
.theme-badgerow .ttag{font-size:11px;color:#8a8d81;border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin-left:6px;}
.riskbox .ritem{font-size:clamp(13.5px,.9vw,15px);color:#171916;line-height:1.55;padding:13px 0;}
.riskbox .ritem+.ritem{border-top:1px solid var(--line);}
.riskcard.takecard::before{background:#6d4b9c;}
.riskcard.takecard .txt{font-family:var(--serif);font-style:italic;font-weight:400;font-size:clamp(16px,1.3vw,19px);line-height:1.5;}
.riskcard cite{display:inline;margin-left:6px;font-size:11px;color:#8a8d81;font-style:normal;white-space:nowrap;}
.riskcard .txt{font-weight:500;font-size:clamp(13.5px,.9vw,15px);color:#171916;line-height:1.55;}
.gloss{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:6px 30px;}
.gloss div{padding:9px 0;border-bottom:1px solid var(--line);font-size:13.8px;line-height:1.55;}
.gloss b{font-family:var(--serif);color:#171916;}
.empty{color:var(--muted);font-style:italic;font-size:14.5px;}
html{-webkit-text-size-adjust:100%;}
@media (max-width:640px){.riskbox .cmeta,.badge{white-space:normal;}.theme h2{padding-left:0;}}
html.dark{color-scheme:dark;}
.hero{position:relative;}
.theme-toggle{position:absolute;top:clamp(14px,2vw,26px);right:clamp(14px,3vw,40px);width:40px;height:40px;border-radius:50%;border:1px solid var(--line);background:var(--card);color:var(--muted);display:grid;place-items:center;cursor:pointer;padding:0;}
.theme-toggle:hover{color:var(--brand);border-color:var(--brand);}
.theme-toggle .sun,html.dark .theme-toggle .moon{display:none;}
html.dark .theme-toggle .sun{display:block;}
html.dark{--ink:#e6e2d6;--muted:#9c978a;--line:#34322b;--card:#1b1a17;--bg:#121210;--brand:#d39c63;}
html.dark .hero h1,html.dark .sec h2,html.dark .theme h2,html.dark .lead,html.dark .namechip b,html.dark .irow .title,html.dark .irow .tline .txt,html.dark .riskbox .ritem,html.dark .riskcard .txt,html.dark .gloss b{color:#f2eee3;}
html.dark .bullets li,html.dark .sidecard.quote{color:#d4cfc2;}
html.dark .sidecard .txt,html.dark .namechip span,html.dark .irow .detail{color:#b3ae9f;}
html.dark .card{background:#211f1b;}
html.dark .sidecard,html.dark .icardbox,html.dark .riskcard,html.dark .riskbox{background:#23211d;}
html.dark .irow .ic{background:#342c22;}
html.dark .riskbox .cmeta{color:#74c79b;}
html.dark .riskbox .rel{color:#93b4e6;}
html.dark .namechip .stance{color:#fff;}
"""

INDEX_CSS = CSS + """
.sig-intro{font-size:14px;color:var(--muted);line-height:1.55;margin:4px 0 18px;max-width:760px;}
.sig-h{font-family:var(--serif);font-size:clamp(18px,1.4vw,22px);margin:28px 0 2px;}
.sig-note{font-size:13px;color:var(--muted);font-style:italic;margin:0 0 12px;}
.sig-fwd{margin-top:10px;padding:10px 12px;border-radius:8px;background:var(--line);font-size:13.3px;line-height:1.5;}
.sig-fwd span{display:block;font-weight:600;font-size:12px;color:var(--brand);margin-bottom:4px;}
.sig-fwd ul{margin:0;padding-left:18px;}
.sig-by{color:var(--muted);font-size:12px;white-space:nowrap;}
ul.rows.sig-tags li{display:flex;gap:12px;justify-content:space-between;}
ul.rows.sig-tags span{color:var(--muted);font-variant-numeric:tabular-nums;}
.idx-stats{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:6px;}
.idx-stats span{font-family:var(--serif);font-style:italic;color:var(--brand);font-size:clamp(12.5px,.95vw,14.5px);}
.controls{position:sticky;top:0;z-index:5;background:var(--card);margin:0 calc(-1*clamp(18px,4vw,56px)) 22px;
  padding:12px clamp(18px,4vw,56px);border-bottom:1px solid var(--line);}
.searchwrap{margin:0 0 12px;}
#q{width:100%;box-sizing:border-box;padding:12px 16px;border:1px solid var(--line);border-radius:10px;
  background:#fffefb;font-size:15px;font-family:inherit;color:var(--ink);}
#q:focus{outline:2px solid var(--brand);outline-offset:-1px;}
.tabs{display:flex;flex-wrap:wrap;gap:8px;}
.tab{font-family:inherit;font-size:13.5px;font-weight:600;padding:9px 16px;border-radius:20px;
  border:1px solid var(--line);background:#fbf7ef;color:var(--muted);cursor:pointer;}
.tab.active{background:var(--brand);border-color:var(--brand);color:#fffdf8;}
.view{display:none;}
.view.active{display:block;}
table.idx{width:100%;border-collapse:collapse;}
table.idx th{text-align:left;font-family:var(--serif);font-style:italic;font-weight:600;
  color:var(--brand);font-size:13px;padding:8px 14px 8px 0;border-bottom:2px solid var(--brand);}
table.idx td{padding:12px 14px 12px 0;border-bottom:1px solid var(--line);vertical-align:top;
  font-size:clamp(13.5px,.95vw,15px);}
table.idx tr:hover td{background:#fbf7ef;}
.idx-date{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums;}
.idx-channel{white-space:nowrap;font-weight:600;}
.idx-title a,ul.rows a,ul.mentions a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line);}
.idx-title a:hover,ul.rows a:hover,ul.mentions a:hover{color:var(--brand);border-bottom-color:var(--brand);}
.idx-thread{color:var(--muted);font-size:13px;}
.grp{border:1px solid var(--line);border-radius:12px;background:#fbf7ef;margin:0 0 12px;overflow:hidden;}
.grp[hidden]{display:none;}
.grp summary{list-style:none;cursor:pointer;padding:14px 18px;display:flex;align-items:center;
  gap:12px;font-weight:600;}
.grp summary::-webkit-details-marker{display:none;}
.grp summary::before{content:"\\25B8";color:var(--brand);font-size:12px;transition:transform .15s;}
.grp[open] summary::before{transform:rotate(90deg);}
.grp summary b{font-family:var(--serif);font-size:clamp(15px,1.1vw,18px);font-weight:600;color:#171916;}
.grp summary .cnt{margin-left:auto;font-size:12.5px;color:var(--muted);font-weight:500;white-space:nowrap;}
.tkr{display:inline-block;min-width:44px;text-align:center;padding:3px 8px;border-radius:5px;
  background:#171916;color:#fffdf8;font-size:12px;font-weight:700;letter-spacing:.02em;}
.tkr.none{background:var(--line);color:var(--muted);}
.grp-body{padding:0 18px 14px;}
ul.rows{list-style:none;margin:0;padding:0;}
ul.rows li{padding:9px 0;border-bottom:1px solid var(--line);font-size:13.8px;}
ul.rows li:last-child{border-bottom:none;}
ul.mentions{list-style:none;margin:0;padding:0;}
ul.mentions li{position:relative;padding:10px 0 10px 18px;border-bottom:1px solid var(--line);}
ul.mentions li:last-child{border-bottom:none;}
ul.mentions .dot{position:absolute;left:0;top:16px;width:7px;height:7px;border-radius:50%;}
.m-date{white-space:nowrap;color:var(--muted);font-variant-numeric:tabular-nums;font-size:12.5px;margin-right:8px;}
.m-channel{font-weight:600;font-size:12.5px;margin-right:8px;}
.m-stance{display:block;font-size:12px;color:var(--brand);font-style:italic;margin-top:2px;}
.m-blurb{font-size:13.3px;color:#3a3d35;line-height:1.5;margin-top:4px;}
.noresults{color:var(--muted);font-style:italic;padding:20px 0;display:none;}
.hits{display:flex;flex-direction:column;}
.hitrow{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--line);}
.hitrow:last-child{border-bottom:none;}
.htype{flex:none;margin-top:1px;padding:3px 9px;border-radius:20px;background:#171916;color:#fffdf8;
  font-size:10.5px;font-weight:700;letter-spacing:.03em;text-transform:uppercase;white-space:nowrap;height:fit-content;}
.hit-body{min-width:0;}
.hit-text{font-size:14px;line-height:1.5;color:#232520;}
.hit-cite{color:var(--muted);font-style:italic;font-size:12.5px;}
.hit-meta{margin-top:5px;font-size:12.5px;}
.hit-meta a{color:var(--brand);text-decoration:none;border-bottom:1px solid var(--line);}
.hit-meta a:hover{border-bottom-color:var(--brand);}
.hit-more{color:var(--muted);font-style:italic;padding:14px 0 4px;font-size:13px;}
.tcount{margin-left:7px;font-size:11.5px;font-weight:700;padding:1px 7px;border-radius:10px;background:var(--line);color:var(--ink);font-variant-numeric:tabular-nums;}
.tab.active .tcount{background:rgba(255,255,255,.25);color:inherit;}
.tab.zero{opacity:.55;}
mark{background:#f3dcb0;color:inherit;border-radius:2px;padding:0 1px;}
html.dark mark{background:#5c4422;}
@media (max-width:640px){
  #q{font-size:16px;}
  .tabs{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin-right:calc(-1*clamp(18px,4vw,56px));padding-right:18px;}
  .tabs::-webkit-scrollbar{display:none;}
  .tab{flex:none;padding:11px 16px;}
  table.idx,table.idx tbody{display:block;}
  table.idx thead{display:none;}
  table.idx tr{display:block;padding:12px 0;border-bottom:1px solid var(--line);}
  table.idx td{display:inline;padding:0;border:none;white-space:normal;}
  table.idx .idx-date{margin-right:10px;}
  table.idx .idx-title{display:block;margin:4px 0 2px;font-size:15.5px;line-height:1.45;}
  table.idx .idx-thread{display:block;}
  table.idx tr:hover td{background:none;}
}
html.dark #q{background:#23211d;}
html.dark .tab,html.dark .grp{background:#211f1b;}
html.dark .tab.active{background:var(--brand);color:#121210;}
html.dark table.idx tr:hover td{background:#211f1b;}
html.dark .grp summary b{color:#f2eee3;}
html.dark .tkr,html.dark .htype{background:#e6e2d6;color:#121210;}
html.dark .tkr.none{background:var(--line);color:var(--muted);}
html.dark .m-blurb,html.dark .hit-text{color:#c4bfb2;}
"""


SITE_URL = "https://hutuleac.github.io/YT-Stocks-Brain/"


def social_meta(title, desc):
    t, d = html.escape(title), html.escape(desc)
    return (f'<meta name="description" content="{d}">\n'
            f'<meta property="og:site_name" content="YouTube Research Briefs">\n'
            f'<meta property="og:title" content="{t}">\n<meta property="og:description" content="{d}">\n'
            f'<meta property="og:image" content="{SITE_URL}og.png">\n<meta name="twitter:card" content="summary_large_image">')


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def esc(s):
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


_MD_BOLD = re.compile(r"\*\*(.+?)\*\*")
_MD_ITAL = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
_AUTO_ANCHOR = re.compile(
    r"\$[\d][\d,.]*\s*(?:trillion|billion|million|[TBMK])?\b"
    r"|\b\d[\d,.]*%"
    r"|\([A-Z]{1,6}(?:\.[A-Z]{2,4})?\)"
)


def emph(s, auto=True):
    """Escape, then render **bold**/*italic* markdown, then (if auto and no
    manual markup was used) bold the single first $-amount / percentage /
    ticker in the string — one scannable anchor per line, not a wall of bold."""
    if s is None:
        return ""
    t = esc(s)
    had_markup = "**" in t or _MD_ITAL.search(t)
    t = _MD_BOLD.sub(r"<b>\1</b>", t)
    t = _MD_ITAL.sub(r"<i>\1</i>", t)
    if auto and not had_markup:
        t = _AUTO_ANCHOR.sub(lambda m: f"<b>{m.group(0)}</b>", t, count=1)
    return t


def render_snapshot(items):
    if not items:
        return '<p class="empty">No clear snapshot could be extracted from this transcript.</p>'
    lis = "".join(f"<li>{emph(b)}</li>" for b in items)
    return f'<ol class="snap">{lis}</ol>'


NAMES_ACCENT = "#65695f"  # fixed neutral slate — distinct from stance colors, reads as "reference"
WATCH_ACCENT = "#93711b"  # fixed amber — reads as "caution", regardless of the theme's own stance color


def render_theme(t):
    color = STANCE_COLORS.get(t.get("color", "gray"), STANCE_COLORS["gray"])
    bullets = "".join(
        f'<li><span class="dot" style="background:{color};"></span>{emph(b)}</li>'
        for b in t.get("bullets", [])
    )
    quote_html = ""
    q = t.get("quote")
    if q:
        quote_html = (
            f'<div class="sidecard quote" style="--sc-accent:{color};">'
            f'<div class="lbl">Pull quote</div>'
            f'&#8220;{emph(q["text"], auto=False)}&#8221;<cite>{esc(q.get("cite",""))}</cite></div>'
        )
    names_html = ""
    names = t.get("names")
    if names:
        chips = []
        for n in names:
            bits = [x for x in (n.get("stance"), n.get("conviction"), n.get("horizon")) if x]
            chip = (f'<span class="stance" style="background:{STANCE_COLORS[_stance_color(n.get("stance"))]};">'
                    f'{esc(" · ".join(bits))}</span>') if bits else ""
            chips.append(f'<div class="namechip"><b>{esc(n["name"])}{chip}</b><span>{esc(n["blurb"])}</span></div>')
        chips = "".join(chips)
        names_html = (
            f'<div class="sidecard" style="--sc-accent:{NAMES_ACCENT};">'
            f'<div class="lbl">Names in play</div>{chips}</div>'
        )
    watch_html = ""
    if t.get("watch"):
        watch_html = (
            f'<div class="sidecard" style="--sc-accent:{WATCH_ACCENT};">'
            f'<div class="lbl">Worth noting</div>'
            f'<div class="txt">{esc(t["watch"])}</div></div>'
        )

    tags_html = "".join(f'<span class="ttag">{esc(x)}</span>' for x in t.get("tags") or [])
    return f"""
<section class="theme" id="{t['id']}">
  <div class="theme-badgerow">
    <span class="badge" style="background:{color};">{esc(t.get('badge',''))}</span>
    <span class="theme-status">{esc(t.get('status',''))}</span>{tags_html}
  </div>
  <h2 style="border-left:4px solid {color};">{esc(t['title'])}</h2>
  <div class="theme-body">
    <div class="theme-main">
      <p class="lead">{emph(t.get('lead',''), auto=False)}</p>
      <ul class="bullets">{bullets}</ul>
    </div>
    <div class="theme-side">
      {quote_html}
      {names_html}
      {watch_html}
    </div>
  </div>
</section>
"""


def render_icards(items, icon_default="\U0001F4CC", with_tag_detail=False, inline_tag=False):
    if not items:
        return '<p class="empty">Nothing notable found in this category for this video.</p>'
    rows = []
    for it in items:
        if inline_tag:
            tag = esc(it.get("tag", ""))
            cat = f'<span class="cat">{tag}:</span> ' if tag else ""
            rows.append(
                f'<div class="irow"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div class="tline">{cat}<span class="txt">{emph(it["title"])}</span></div></div>'
            )
        elif with_tag_detail:
            tag = esc(it.get("tag", ""))
            detail = it.get("detail", "")
            rows.append(
                f'<div class="irow"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div><div class="title">{emph(it["title"])}'
                + (f' <span class="tag">{tag}</span>' if tag else "")
                + '</div>'
                + (f'<div class="detail">{emph(detail)}</div>' if detail else "")
                + '</div></div>'
            )
        else:
            rows.append(
                f'<div class="irow"><div class="ic">{it.get("icon", icon_default)}</div>'
                f'<div><div class="title">{emph(it["title"])}</div>'
                f'<div class="tag">{esc(it.get("tag",""))}</div></div></div>'
            )
    return '<div class="icardbox">' + "".join(rows) + '</div>'


def claim_line(c):
    """One-line rendering of a CLAIMS row; also used as its search-hit text."""
    head = " · ".join(esc(x) for x in (c.get("metric"), c.get("target"), c.get("by")) if x)
    tail = f' <i>if {esc(c["condition"])}</i>' if c.get("condition") else ""
    ent = f' <span class="tag">{esc(c["entity"])}</span>' if c.get("entity") else ""
    return (f'<b>{esc(c.get("who",""))}:</b> {emph(c.get("claim",""), auto=False)}'
            + (f' <span class="cmeta">{head}</span>' if head else "") + tail + ent)


def render_claims(items):
    if not items:
        return '<p class="empty">No dated or numeric calls made in this video.</p>'
    rows = "".join(f'<div class="ritem">{claim_line(c)}</div>' for c in items)
    return f'<div class="riskbox" style="--box-accent:#2d6a4f;">{rows}</div>'


def render_relations(items):
    if not items:
        return '<p class="empty">No company-to-company relationships stated in this video.</p>'
    rows = "".join(
        f'<div class="ritem"><b>{esc(r.get("from",""))}</b> '
        f'<span class="rel">{esc(r.get("rel","")).replace("_", " ")}</span> <b>{esc(r.get("to",""))}</b>'
        + (f' &mdash; {emph(r["note"], auto=False)}' if r.get("note") else "") + '</div>'
        for r in items
    )
    return f'<div class="riskbox" style="--box-accent:#3b5b8c;">{rows}</div>'


def render_hot_takes(items):
    if not items:
        return '<p class="empty">No standout hot takes or personal convictions in this video.</p>'
    out = []
    for t in items:
        cite = t.get("cite", "")
        out.append(
            '<div class="riskcard takecard"><div class="txt">&#8220;' + emph(t["take"], auto=False) + '&#8221;'
            + (f' <cite>{esc(cite)}</cite>' if cite else "")
            + '</div></div>'
        )
    return "".join(out)


def render_glossary(items):
    if not items:
        return '<p class="empty">No glossary terms extracted for this video.</p>'
    return '<div class="gloss">' + "".join(
        f'<div><b>{esc(g["term"])}</b> &mdash; {esc(g["def"])}</div>' for g in items
    ) + "</div>"


def build_html(data):
    META = data.META
    thread_count = len(data.THEMES)
    thread_line = META.get("thread_line") or f"{thread_count} threads"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<script>(function(){{var d=document.documentElement,t,m=matchMedia('(prefers-color-scheme: dark)');try{{t=localStorage.getItem('theme')}}catch(e){{}}function a(){{d.classList.toggle('dark',t?t==='dark':m.matches)}}a();m.addEventListener('change',function(){{if(!t)a()}});window.toggleTheme=function(){{t=d.classList.contains('dark')?'light':'dark';try{{localStorage.setItem('theme',t)}}catch(e){{}}a()}}}})();</script>
<title>Research: {esc(META['title'])}</title>
{social_meta(META['title'], f"{META['channel']} · {thread_line}")}
<style>{CSS}</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle light/dark mode"><svg class="moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
    <div class="backlink"><a href="index.html">&#8592; All Research Briefs</a></div>
    <div class="kicker">A YouTube Research Brief</div>
    <h1>{esc(META['title'])}</h1>
    <div class="byline">
      Channel: <b>{esc(META['channel'])}</b> &middot; Speaker: <b>{esc(META['speakers'])}</b> &middot; <b>{esc(META['date'])}</b>
      <div class="stats-line">{esc(thread_line)} &middot; <a href="{esc(META['video_url'])}" target="_blank" rel="noopener">Watch on YouTube &#8599;</a></div>
    </div>
  </header>
  <div class="inner">
    <section class="sec">
      <div class="sec-eye">The one-paragraph takeaway</div>
      <h2>Video Snapshot</h2>
      <div class="card" style="margin-top:16px;">{render_snapshot(data.SNAPSHOT)}</div>
    </section>

    {''.join(render_theme(t) for t in data.THEMES)}

    <section class="sec">
      <div class="sec-eye">What to do with this</div>
      <h2>Best Actionable Takeaways</h2>
      <div style="margin-top:16px;">{render_icards(data.TAKEAWAYS, inline_tag=True)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Where they stuck their neck out</div>
      <h2>Hot Takes &amp; Personal Convictions</h2>
      <div style="margin-top:16px;">{render_hot_takes(data.HOT_TAKES)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Numbers and dates someone can be held to</div>
      <h2>Predictions &amp; Dated Calls</h2>
      <div style="margin-top:16px;">{render_claims(data.CLAIMS)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Who is tied to whom</div>
      <h2>Relationships</h2>
      <div style="margin-top:16px;">{render_relations(data.RELATIONS)}</div>
    </section>

    <section class="sec">
      <div class="sec-eye">Beyond the main threads</div>
      <h2>Other Notable News</h2>
      <div style="margin-top:16px;">{render_icards(data.OTHER_NEWS, with_tag_detail=True)}</div>
    </section>

    <section class="sec" style="border-bottom:none;">
      <div class="sec-eye">Names and terms at a glance</div>
      <h2>Glossary &amp; Entities</h2>
      <div style="margin-top:16px;">{render_glossary(data.GLOSSARY)}</div>
    </section>
  </div>
</div>
</body>
</html>"""
    return html


SCHEMA_VERSION = 2  # 1 = pre-Oct-2026 briefs (no field); 2 = adds schema_version itself


def build_json(data):
    return {
        "schema_version": SCHEMA_VERSION,
        "meta": data.META,
        "snapshot": data.SNAPSHOT,
        "themes": data.THEMES,
        "takeaways": data.TAKEAWAYS,
        "hot_takes": data.HOT_TAKES,
        "claims": data.CLAIMS,
        "relations": data.RELATIONS,
        "other_news": data.OTHER_NEWS,
        "glossary": data.GLOSSARY,
    }


# ---------------------------------------------------------------------------
# CROSS-VIDEO INDEX — scans research-data/*/*.json, rebuilt on every run.
# Builds three facets over the same underlying data: chronological, by-channel,
# and by-company/ticker (the entity cross-reference used to build an investing
# thesis across many videos). See _entities_from_theme / _entities_from_conviction
# for how each JSON schema (current 'meta' vs legacy 'metadata') is parsed.
# ---------------------------------------------------------------------------

TICKER_RE = re.compile(r"\(([A-Z]{1,5})\)\s*$")
BARE_TICKER_RE = re.compile(r"^[A-Z]{1,5}$")
TICKER_BLACKLIST = {
    "ADR", "IPO", "CEO", "CFO", "CTO", "ETF", "AI", "GPU", "SEC", "IRA", "WACC",
    "SOFR", "CPI", "PPI", "FOMC", "OER", "US", "UK", "EU", "GDP", "FED", "Q1",
    "Q2", "Q3", "Q4", "YOY", "MOM", "ATH", "IRL", "CEO", "COO", "R&D",
}
STANCE_KEYWORDS_RED = ("NEGATIVE", "BEARISH", "SELL", "AVOID", "SHORT")
STANCE_KEYWORDS_GREEN = ("OWN", "BUY", "ADD", "POSITIVE", "LONG")
STANCE_KEYWORDS_AMBER = ("WATCH", "UNCERTAIN", "CASUAL", "MIXED", "CONTESTED")
INVESTABLE_CATEGORY_HINTS = (
    "stock", "crypto", "equity", "etf", "sector", "compan", "hardware", "semic",
    "commodity", "big tech", "financ", "infrastructure", "market",
)




def _parse_ticker(piece):
    m = TICKER_RE.search(piece)
    if m and m.group(1) not in TICKER_BLACKLIST:
        return m.group(1), piece[: m.start()].strip()
    if BARE_TICKER_RE.match(piece) and piece not in TICKER_BLACKLIST:
        return piece, piece
    return None, piece


def _stance_color(stance_text):
    s = (stance_text or "").upper()
    if any(k in s for k in STANCE_KEYWORDS_RED):
        return "red"
    if any(k in s for k in STANCE_KEYWORDS_GREEN):
        return "green"
    if any(k in s for k in STANCE_KEYWORDS_AMBER):
        return "amber"
    return "gray"


def _entities_from_theme(theme):
    out = []
    for n in theme.get("names") or []:
        raw = n.get("name", "")
        blurb = n.get("blurb", "")
        for piece in _split_entity_list(raw):
            ticker, display = _parse_ticker(piece)
            stance = n.get("stance")
            out.append({
                "ticker": ticker, "display": display or piece, "raw": piece, "theme_id": theme.get("id"),
                "stance_label": stance or theme.get("badge", ""),
                "conviction": n.get("conviction"), "horizon": n.get("horizon"),
                "color": _stance_color(stance) if stance else theme.get("color", "gray"),
                "blurb": blurb,
            })
    return out


def _entities_from_conviction(conviction_map):
    out = []  # legacy schema: no per-entity horizon
    for c in conviction_map or []:
        raw = c.get("topic", "")
        category = c.get("category", "") or ""
        investable = any(k in category.lower() for k in INVESTABLE_CATEGORY_HINTS)
        for piece in _split_entity_list(raw):
            ticker, display = _parse_ticker(piece)
            if not ticker and not investable:
                continue
            stance = c.get("stance", "")
            out.append({
                "ticker": ticker, "display": display or piece, "raw": piece,
                "stance_label": stance, "conviction": c.get("conviction"),
                "color": _stance_color(stance), "blurb": c.get("core_thesis", ""),
            })
    return out


def _legacy_thread_line(d):
    """Legacy schema has no thread_line field — derive a short one so the chronological
    view isn't blank: first sentence of the executive takeaway, or a company/ticker count."""
    exec_take = (d.get("executive_takeaway") or "").strip()
    if exec_take:
        first = re.split(r"(?<=[.!?])\s+", exec_take)[0]
        return first if len(first) <= 160 else first[:157].rstrip() + "..."
    n = len(d.get("conviction_map") or [])
    if n:
        return f"{n} companies/tickers covered"
    return ""


def _content_hits(d):
    """Flatten a brief's raw JSON into searchable snippets — quotes, hot takes/
    claims, relations, recommendations, glossary terms, company notes — each
    optionally anchored to the theme section it came from (current schema only;
    legacy fixed-table briefs link to the brief page itself). Powers the
    Quotes & Takes search view. Handles both the current ('meta'/'themes') and
    legacy ('metadata'/'conviction_map') JSON schemas."""
    hits = []

    def add(kind, text, cite="", theme_id=None):
        text = (text or "").strip()
        if text:
            hits.append({"type": kind, "text": text, "cite": cite or "", "theme_id": theme_id})

    if "meta" in d:  # current schema
        for t in d.get("themes", []) or []:
            tid = t.get("id")
            for b in t.get("bullets", []) or []:
                add("Bullet", b, theme_id=tid)
            q = t.get("quote")
            if q:
                add("Quote", q.get("text", ""), q.get("cite", ""), theme_id=tid)
            if t.get("watch"):
                add("Watch", t["watch"], theme_id=tid)
            for n in t.get("names") or []:
                add("Company note", f'{n.get("name","")}: {n.get("blurb","")}', theme_id=tid)
        for it in d.get("takeaways", []) or []:
            add("Takeaway", it.get("title", ""), it.get("tag", ""))
        for it in d.get("hot_takes", []) or []:
            add("Hot take", it.get("take", ""), it.get("cite", ""))
        for c in d.get("claims", []) or []:
            add("Claim", " ".join(x for x in (c.get("claim"), c.get("metric"), c.get("target"), c.get("by")) if x), c.get("who", ""))
        for r in d.get("relations", []) or []:
            add("Relation", f'{r.get("from","")} {r.get("rel","").replace("_"," ")} {r.get("to","")}' + (f' — {r["note"]}' if r.get("note") else ""))
        for it in d.get("other_news", []) or []:
            add("News", it.get("title", ""), it.get("tag", ""))
        for g in d.get("glossary", []) or []:
            add("Glossary", f'{g.get("term","")}: {g.get("def","")}')
    elif "metadata" in d:  # legacy fixed-table schema — no theme anchors
        for c in d.get("conviction_map", []) or []:
            add("View", f'{c.get("topic","")}: {c.get("core_thesis","")}', c.get("stance", ""))
        for c in d.get("companies_assets", []) or []:
            add("Company note", f'{c.get("company","")}: {c.get("view","")}', c.get("status", ""))
        for t in d.get("technology_ai_views", []) or []:
            add("View", f'{t.get("theme","")}: {t.get("view","")}')
        for w in d.get("ai_workflows", []) or []:
            add("Workflow", f'{w.get("name","")}: {w.get("goal","")}')
        for p in d.get("predictions", []) or []:
            add("Prediction", p.get("prediction", ""), p.get("horizon", ""))
        for q in d.get("notable_quotes", []) or []:
            add("Quote", q.get("quote", ""), q.get("speaker", ""))
        for it in d.get("actionable_takeaways", []) or []:
            add("Takeaway", it.get("item", ""), it.get("type", ""))
        for it in d.get("other_notable_news", []) or []:
            add("News", it.get("title", ""), it.get("category", ""))
        for g in d.get("glossary", []) or []:
            add("Glossary", f'{g.get("term","")}: {g.get("definition","")}')
    return hits


def _load_brief(json_path):
    try:
        d = json.load(open(json_path, encoding="utf-8"))
    except Exception:
        return None
    base = os.path.splitext(os.path.basename(json_path))[0]
    html_name = f"{base}.html"
    if not os.path.exists(html_name):
        return None
    if "meta" in d:  # current schema
        m = d["meta"]
        date = m.get("date", "")
        speakers = m.get("speakers", "")
        thread_line = m.get("thread_line", "")
        category = m.get("category") or "market"
        entities = [e for t in d.get("themes", []) for e in _entities_from_theme(t)]
        tags = sorted({x for t in d.get("themes", []) for x in (t.get("tags") or [])})
    elif "metadata" in d:  # legacy fixed-table schema
        m = d["metadata"]
        date = m.get("publication_date") or m.get("analysis_date", "")
        speakers = m.get("speaker", "")
        thread_line = _legacy_thread_line(d)
        category = "market"
        entities = _entities_from_conviction(d.get("conviction_map"))
        tags = []
    else:
        return None
    return {
        "html": html_name,
        "title": m.get("title", base),
        "channel": m.get("channel", ""),
        "date": date,
        "speakers": speakers,
        "thread_line": thread_line,
        "category": category,
        "tags": tags,
        "entities": entities,
        "hits": _content_hits(d),
        "_raw": d,
    }


def _date_sort_key(date_str):
    try:
        return -int(date_str.replace("-", ""))
    except (ValueError, AttributeError):
        return 0


def _search_blob(*parts):
    """Word-normalized blob: lowercase, no accents/apostrophes, punctuation -> single spaces,
    space-padded so the index JS can prefix-match words with indexOf(' ' + token).
    Must stay in sync with norm() in INDEX_JS."""
    s = unicodedata.normalize("NFKD", " ".join(p for p in parts if p).lower())
    s = re.sub(r"['’]", "", "".join(c for c in s if not unicodedata.combining(c)))
    return " " + re.sub(r"[^a-z0-9]+", " ", s).strip() + " "


def _entity_words(b):
    return " ".join(f'{e["ticker"] or ""} {e["display"]}' for e in b["entities"])


def _render_chrono_view(briefs):
    rows = "".join(
        f'<tr class="row" data-search="{_search_blob(b["title"], b["channel"], b["speakers"], b["thread_line"], " ".join(b["tags"]), _entity_words(b))}">'
        f'<td class="idx-date">{esc(b["date"])}</td>'
        f'<td class="idx-channel">{esc(b["channel"])}</td>'
        f'<td class="idx-title"><a href="{esc(b["html"])}">{esc(b["title"])}</a></td>'
        f'<td class="idx-thread">{esc(b["thread_line"])}</td></tr>'
        for b in briefs
    ) or '<tr><td colspan="4" class="empty">No briefs found yet.</td></tr>'
    return f"""<table class="idx">
      <thead><tr><th>Date</th><th>Channel</th><th>Title</th><th>Threads</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>"""


def _render_channel_view(briefs):
    by_channel = {}
    for b in briefs:
        by_channel.setdefault(b["channel"], []).append(b)
    groups = sorted(
        by_channel.items(),
        key=lambda kv: min(_date_sort_key(b["date"]) for b in kv[1]),
    )
    out = []
    for channel, items in groups:
        items = sorted(items, key=lambda b: _date_sort_key(b["date"]))
        search = _search_blob(channel, " ".join(b["title"] for b in items))
        rows = "".join(
            f'<li><span class="idx-date">{esc(b["date"])}</span> '
            f'<a href="{esc(b["html"])}">{esc(b["title"])}</a> '
            f'<span class="idx-thread">{esc(b["thread_line"])}</span></li>'
            for b in items
        )
        out.append(
            f'<details class="grp" data-search="{search}">'
            f'<summary><b>{esc(channel)}</b><span class="cnt">{len(items)} brief{"s" if len(items) != 1 else ""}</span></summary>'
            f'<div class="grp-body"><ul class="rows">{rows}</ul></div></details>'
        )
    return "".join(out) or '<p class="empty">No briefs found yet.</p>'


def _render_entity_view(briefs):
    entities = {}  # canonical key (see entities.py) -> {ticker, display, mentions: []}
    for b in briefs:
        for e in b["entities"]:
            slot = entities.setdefault(e["key"], {"ticker": e["ticker"], "display": e["display"], "mentions": []})
            slot["mentions"].append({**e, "brief": b})

    ordered = sorted(
        entities.values(),
        key=lambda s: (-len(s["mentions"]), 0 if s["ticker"] else 1, s["display"].lower()),
    )
    out = []
    for s in ordered:
        mentions = sorted(s["mentions"], key=lambda m: _date_sort_key(m["brief"]["date"]))
        search = _search_blob(
            s["ticker"] or "", s["display"],
            " ".join(m["brief"]["title"] for m in mentions),
            " ".join(m["brief"]["channel"] for m in mentions),
        )
        tkr_badge = f'<span class="tkr">{esc(s["ticker"])}</span>' if s["ticker"] else '<span class="tkr none">—</span>'
        items = []
        for m in mentions:
            color = STANCE_COLORS.get(m["color"], STANCE_COLORS["gray"])
            b = m["brief"]
            stance_bits = " · ".join(x for x in [m["stance_label"], m["conviction"]] if x)
            items.append(
                f'<li><span class="dot" style="background:{color};"></span>'
                f'<span class="m-date">{esc(b["date"])}</span>'
                f'<span class="m-channel">{esc(b["channel"])}</span>'
                f'<a href="{esc(b["html"])}">{esc(b["title"])}</a>'
                + (f'<span class="m-stance">{esc(stance_bits)}</span>' if stance_bits else "")
                + (f'<div class="m-blurb">{esc(m["blurb"])}</div>' if m["blurb"] else "")
                + "</li>"
            )
        out.append(
            f'<details class="grp" data-search="{search}" data-key="{_search_blob(s["ticker"] or "", s["display"])}">'
            f'<summary>{tkr_badge}<b>{esc(s["display"])}</b>'
            f'<span class="cnt">{len(mentions)} mention{"s" if len(mentions) != 1 else ""}</span></summary>'
            f'<div class="grp-body"><ul class="mentions">{"".join(items)}</ul></div></details>'
        )
    return "".join(out) or '<p class="empty">No companies or tickers extracted yet.</p>'


def _content_hits_payload(briefs):
    """Compact JSON payload for the Quotes & Takes view. Brief fields are stored once in "b"
    ([date, channel, title, html, search blob]) and each of the ~8000 hits in "x" points at
    its brief by index: [brief_idx, theme anchor or "", type, text, cite, search blob]."""
    out_b, out_x = [], []
    for i, b in enumerate(briefs):
        out_b.append([b["date"], esc(b["channel"]), esc(b["title"]), esc(b["html"]),
                      _search_blob(b["title"], b["channel"], b["speakers"])])
        for h in b["hits"]:
            out_x.append([i, h["theme_id"] or "", esc(h["type"]), esc(h["text"]), esc(h["cite"]),
                          _search_blob(h["type"], h["text"], h["cite"])])
    return json.dumps({"b": out_b, "x": out_x}, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")


INDEX_JS = """
(function(){
  var q = document.getElementById('q');
  var tabs = document.querySelectorAll('.tab');
  var LIMIT = 300;
  // must stay in sync with _search_blob() in generate.py
  function norm(s){
    return (s || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .replace(/['\\u2019]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
  }
  // word-prefix match; "metas"/"meta's"/"bitcoins" also match the bare word
  function has(blob, t){
    return blob.indexOf(' ' + t) !== -1 ||
      (t.length > 3 && t.charAt(t.length - 1) === 's' && blob.indexOf(' ' + t.slice(0, -1) + ' ') !== -1);
  }
  function hasAll(blob, toks){ for (var i = 0; i < toks.length; i++) if (!has(blob, toks[i])) return false; return true; }
  var data = null;
  function getData(){
    if (!data) data = JSON.parse(document.getElementById('hitdata').textContent || '{"b":[],"x":[]}');
    return data;
  }
  function reEsc(s){ return s.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&'); }
  function highlight(html, toks){
    if (!toks.length) return html;
    var re = new RegExp('(^|[^a-z0-9&#])(' + toks.map(reEsc).join('|') + ')', 'gi');
    return html.split(/(<[^>]*>)/).map(function(part){
      return part.charAt(0) === '<' ? part : part.replace(re, '$1<mark>$2</mark>');
    }).join('');
  }

  // Quotes & Takes: every word must appear in the quote or its brief; quotes that
  // contain all the words themselves rank first, newest first within a tier.
  function findHits(toks){
    var d = getData(), out = [];
    d.x.forEach(function(h, i){
      var b = d.b[h[0]], inText = 0;
      for (var k = 0; k < toks.length; k++){
        if (has(h[5], toks[k])) inText++;
        else if (!has(b[4], toks[k])) return;
      }
      out.push({h: h, b: b, score: inText, i: i});
    });
    out.sort(function(a, z){ return (z.score - a.score) || (a.i - z.i); });
    return out;
  }
  function renderHits(hits, toks){
    var mount = document.getElementById('hits-mount');
    if (!toks.length){
      mount.innerHTML = '<p class="empty">Type to search quotes, recommendations, claims, and opinions across every indexed brief.</p>';
      return;
    }
    if (!hits.length){ mount.innerHTML = '<p class="empty">No matches.</p>'; return; }
    var html = hits.slice(0, LIMIT).map(function(m){
      var h = m.h, b = m.b, href = b[3] + (h[1] ? '#' + h[1] : '');
      return '<div class="hitrow"><span class="htype">' + h[2] + '</span><div class="hit-body">'
        + '<div class="hit-text">' + highlight(h[3].replace(/\\*\\*(.+?)\\*\\*/g, '<b>$1</b>'), toks) + (h[4] ? ' <span class="hit-cite">' + highlight(h[4], toks) + '</span>' : '') + '</div>'
        + '<div class="hit-meta"><span class="m-date">' + b[0] + '</span><span class="m-channel">' + b[1] + '</span>'
        + '<a href="' + href + '">' + b[2] + '</a></div></div></div>';
    }).join('');
    if (hits.length > LIMIT){
      var more = hits.length - LIMIT;
      html += '<p class="hit-more">' + more + ' more match' + (more === 1 ? '' : 'es') + ' \\u2014 add a word to narrow further.</p>';
    }
    mount.innerHTML = html;
  }

  // Row/group views. On By Company / Ticker, groups whose name/ticker matches one of the
  // words win: if any exist, groups that only matched via a brief title or channel are hidden.
  function hasAny(blob, toks){ for (var i = 0; i < toks.length; i++) if (has(blob, toks[i])) return true; return false; }
  function filterView(view, toks){
    var els = view.querySelectorAll('[data-search]'), n = 0;
    var isPrimary = function(el){ return hasAny(el.dataset.key, toks) && hasAll(el.dataset.search + el.dataset.key, toks); };
    var primary = view.id === 'view-entity' && toks.length && Array.prototype.some.call(els, isPrimary);
    els.forEach(function(el){
      var hit = !toks.length || (primary ? isPrimary(el) : hasAll(el.dataset.search, toks));
      el.hidden = !hit;
      if (hit) n++;
      if (el.tagName === 'DETAILS') el.open = hit && toks.length > 0 && n <= 5;
    });
    var empty = view.querySelector('.noresults');
    if (!empty){ empty = document.createElement('p'); empty.className = 'noresults'; empty.textContent = 'No matches in this tab.'; view.appendChild(empty); }
    empty.style.display = toks.length && !n ? 'block' : 'none';
    return n;
  }

  function setCount(tab, n){
    var c = tab.querySelector('.tcount');
    if (!c){ c = document.createElement('span'); c.className = 'tcount'; tab.appendChild(c); }
    c.textContent = n === null ? '' : (n > 999 ? '999+' : n);
    c.hidden = n === null;
    tab.classList.toggle('zero', n === 0);
  }

  function activeView(){ return document.querySelector('.tab.active').dataset.view; }
  function apply(){
    var toks = norm(q.value) ? norm(q.value).split(' ') : [];
    tabs.forEach(function(tab){
      var v = tab.dataset.view, n;
      if (v === 'content'){
        var hits = toks.length ? findHits(toks) : [];
        if (activeView() === 'content') renderHits(hits, toks);
        n = hits.length;
      } else {
        n = filterView(document.getElementById('view-' + v), toks);
      }
      setCount(tab, toks.length ? n : null);
    });
    var url = location.pathname + (q.value.trim() ? '?q=' + encodeURIComponent(q.value.trim()) : '') + '#' + activeView();
    history.replaceState(null, '', url);
  }
  var timer;
  q.addEventListener('input', function(){ clearTimeout(timer); timer = setTimeout(apply, 90); });

  function select(v){
    var tab = document.querySelector('.tab[data-view="' + v + '"]');
    if (!tab) return;
    tabs.forEach(function(t){ t.classList.toggle('active', t === tab); });
    document.querySelectorAll('.view').forEach(function(el){ el.classList.toggle('active', el.id === 'view-' + v); });
    var row = tab.parentElement; row.scrollLeft = tab.offsetLeft - row.offsetLeft - 18;
  }
  tabs.forEach(function(tab){
    tab.addEventListener('click', function(){ select(tab.dataset.view); apply(); });
  });

  document.addEventListener('keydown', function(e){
    if (e.key === '/' && document.activeElement !== q){ e.preventDefault(); q.focus(); q.select(); }
    else if (e.key === 'Escape' && document.activeElement === q){ q.value = ''; apply(); }
  });

  var initial = new URLSearchParams(location.search).get('q');
  if (location.hash) select(location.hash.slice(1));
  if (initial){ q.value = initial; }
  if (initial || location.hash) apply();
})();
"""


def _canonicalize_entities(briefs):
    """Resolve every entity string (names, claim entities/speakers, relation endpoints) through
    the kb/entities.json registry, then rewrite each mention's display/ticker from it and add
    its permanent "key". Claims and relations go first so a ticker written there reaches the
    index in the same run."""
    reg = Registry()
    for b in briefs:
        for c in b["_raw"].get("claims") or []:
            reg.resolve_list(c.get("entity"))
            reg.resolve_who(c.get("who"), b["speakers"], b["channel"])
        for x in b["_raw"].get("relations") or []:
            reg.resolve_list(x.get("from"))
            reg.resolve_list(x.get("to"))
        for e in b["entities"]:
            e["key"] = reg.resolve(e["raw"])
    for b in briefs:
        for e in b["entities"]:
            ent = reg.get(e["key"])
            e["display"], e["ticker"] = ent["name"], ent.get("ticker")
    return reg


def build_index():
    briefs = [b for b in (_load_brief(p) for p in sorted(glob.glob(os.path.join("research-data", "*", "*.json")))) if b]
    briefs.sort(key=lambda b: _date_sort_key(b["date"]))
    reg = _canonicalize_entities(briefs)
    kb_warnings = build_kb(briefs, reg)

    channels = sorted(set(b["channel"] for b in briefs))
    tickers = sorted(set(e["ticker"] for b in briefs for e in b["entities"] if e["ticker"]))
    dev_briefs = [b for b in briefs if b["category"] == "dev"]
    life_briefs = [b for b in briefs if b["category"] == "life"]
    hit_count = sum(len(b["hits"]) for b in briefs)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<script>(function(){{var d=document.documentElement,t,m=matchMedia('(prefers-color-scheme: dark)');try{{t=localStorage.getItem('theme')}}catch(e){{}}function a(){{d.classList.toggle('dark',t?t==='dark':m.matches)}}a();m.addEventListener('change',function(){{if(!t)a()}});window.toggleTheme=function(){{t=d.classList.contains('dark')?'light':'dark';try{{localStorage.setItem('theme',t)}}catch(e){{}}a()}}}})();</script>
<title>YouTube Research Briefs — Index</title>
{social_meta("YouTube Research Briefs", f"{len(briefs)} theme-grouped briefs on markets, AI and the people building them: tickers, quotes and takes.")}
<style>{INDEX_CSS}</style>
</head>
<body>
<div class="page">
  <header class="hero">
    <button class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle light/dark mode" title="Toggle light/dark mode"><svg class="moon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg><svg class="sun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
    <div class="kicker">All Research Briefs</div>
    <h1>YouTube Research Brief Index</h1>
    <div class="byline">{len(briefs)} brief{'s' if len(briefs) != 1 else ''} &middot; {len(channels)} channel{'s' if len(channels) != 1 else ''} &middot; {len(tickers)} ticker{'s' if len(tickers) != 1 else ''} tracked &middot; {hit_count} quotes/takes/notes indexed
      <div class="idx-stats"><span>One search covers everything: tickers, companies, people, quotes and takes. The number on each tab shows where the matches are.</span></div>
    </div>
  </header>
  <div class="inner">
    <div class="controls">
    <div class="searchwrap"><input id="q" type="search" placeholder="Search tickers, companies, people, quotes..." autocomplete="off"></div>
    <div class="tabs">
      <button class="tab active" data-view="chrono">All Briefs</button>
      <button class="tab" data-view="channel">By Channel</button>
      <button class="tab" data-view="signals">Signals</button>
      <button class="tab" data-view="entity">By Company / Ticker</button>
      <button class="tab" data-view="content">Quotes &amp; Takes</button>
      <button class="tab" data-view="dev">Dev &amp; Workflows</button>
      <button class="tab" data-view="life">Life &amp; Perspectives</button>
    </div>
    </div>
    <div id="view-chrono" class="view active">{_render_chrono_view(briefs)}</div>
    <div id="view-channel" class="view">{_render_channel_view(briefs)}</div>
    <div id="view-signals" class="view">{render_signals(KB_PATH)}</div>
    <div id="view-entity" class="view">{_render_entity_view(briefs)}</div>
    <div id="view-content" class="view"><div id="hits-mount"><p class="empty">Type to search quotes, recommendations, claims, and opinions across every indexed brief.</p></div></div>
    <div id="view-dev" class="view">{_render_chrono_view(dev_briefs)}</div>
    <div id="view-life" class="view">{_render_chrono_view(life_briefs)}</div>
  </div>
</div>
<script id="hitdata" type="application/json">{_content_hits_payload(briefs)}</script>
<script>{INDEX_JS}</script>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    manifest = {
        "generated_from": "youtube-research-brief generate.py --reindex",
        "briefs": [{k: v for k, v in b.items() if k not in ("entities", "hits", "_raw")} | {
            "entities": [{"key": e["key"], "ticker": e["ticker"], "display": e["display"], "stance": e["stance_label"],
                          "conviction": e["conviction"], "horizon": e.get("horizon"), "color": e["color"]}
                         for e in b["entities"]]
        } for b in briefs],
    }
    with open("library.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)

    for w in reg.summary_warnings() + kb_warnings:
        print(f"warning: {w}")
    if reg.save():
        print(f"Updated {reg.path} (new entities/aliases — commit it with the brief)")

    return "index.html"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    if sys.argv[1] in ("--reindex", "--index"):
        print(f"Wrote {build_index()}")
        return

    data_path = sys.argv[1]
    data = load_data(data_path)

    channel_slug = slugify(data.META["channel"])
    date_slug = slugify(data.META["date"])
    title_slug = slugify(data.META["title"])
    base = f"{channel_slug}_{date_slug}_{title_slug}"

    html_path = f"{base}.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html(data))

    data_dir = os.path.join("research-data", base)
    os.makedirs(data_dir, exist_ok=True)
    json_path = os.path.join(data_dir, f"{base}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(build_json(data), f, indent=1, ensure_ascii=False)

    data_copy_path = os.path.join(data_dir, f"{base}_data.py")
    if os.path.abspath(data_path) != os.path.abspath(data_copy_path):
        shutil.copyfile(data_path, data_copy_path)

    print(f"Wrote {html_path}")
    print(f"Wrote {json_path}")
    print(f"Archived data file to {data_copy_path}")
    print(f"Wrote {build_index()}")


if __name__ == "__main__":
    main()
