"""
Per-video data for youtube-research-brief. Copy this file, fill in every field, then:

    python3 <skill-folder>/generate.py <this-file>

See SKILL.md Section 3 (coverage/inventory) and Section 4 (themes, incl. category-conditional
color/badge/names rules) for what belongs where and the rules for each field (dedup, labeling,
bullet counts, etc.) — this file only has the shape.
"""

META = {
    "title": "",
    "channel": "",
    "speakers": "",
    "date": "",           # YYYY-MM-DD, video upload date — drives filename + index sort order
    "video_url": "",
    "thread_line": "",    # e.g. "5 threads · short summary of each thread"
    "category": "market", # "market" (investing/AI-news, default), "dev" (dev/systems/knowledge/
                           # AI-workflow) or "life" (life/family/mindset/business perspectives) — drives which index.html tab the brief appears in
}

SNAPSHOT = [
    # 5-8 scannable bullets: the one-paragraph read of the whole video
]

THEMES = [
    {
        "id": "",              # short anchor slug, e.g. "elon-thesis"
        "tags": [],            # 1-3 from generate.py TAGS: ai-infra semis software macro-rates crypto
                               # energy space biotech robotics geopolitics policy consumer finance
                               # dev-workflow career health
        "color": "green",      # green | amber | gray | red
        "badge": "",           # e.g. "High conviction" / "Contested" / "Speculative" / "Recommendation"
        "status": "",          # one caps line of context, e.g. "RELEASED JULY 27, 2026"
        "title": "",           # specific, concrete headline (not a category name)
        "lead": "",            # one bold sentence giving the point before any detail — already
                               # renders bold via CSS, don't wrap in **...**
        "bullets": [
            # 3-5 short, concrete, evidence-carrying bullets; flex to 6-7 for dense threads.
            # **bold**/*italic* markdown supported; the renderer auto-bolds the first $/%/
            # (TICKER) in each line for you — only hand-bold a line that has none of those but
            # still has one keyword worth anchoring (max one bold phrase per line).
        ],
        "quote": None,         # {"text": "...", "cite": "— speaker"} or None
        "watch": None,         # str caveat ("this isn't settled") or None
        "names": None,         # [{"name": "Nvidia (NVDA)", "blurb": "...",
                               #   "stance": "POSITIVE VIEW",   # OWNS | BUYING-ADDING | WATCHING |
                               #                                # POSITIVE VIEW | NEGATIVE VIEW |
                               #                                # CASUAL MENTION | UNCERTAIN
                               #   "conviction": "High",        # High | Medium | Low | None
                               #   "horizon": "by 2030"}]       # short text or None
                               # or None. stance/conviction only as explicitly stated — never inferred.
    },
    # 3-6 themes total
]

TAKEAWAYS = [
    # {"icon": "\U0001F3AF", "tag": "...", "title": "..."} × 4-6, imperative and distinct
    # tag = short topic category (1-3 words: "Markets", "Macro", "AI ethics", "Health", "Energy",
    # "Geopolitics", "Crypto", "Robotics", "Space", "Policy", "Careers", ...) — not an action verb.
    # Renders inline, leading the line: "Markets: Track RSP and IGV first..." — title carries the verb.
]

HOT_TAKES = [
    # {"take": "...", "cite": "— Speaker", "why": "short context: what makes it a take"} × 0-6
    # only take + cite render (cite inline, end of the same line) — why is a drafting aid only
    # Verbatim-or-near-verbatim opinions the speaker owns: hot takes, unpopular/contrarian calls,
    # personal convictions, predictions with a number or date, dismissals. See SKILL.md Section 5.
]

CLAIMS = [
    # One row per dated or numeric call — the graph's checkable predictions layer.
    # {"who": "Jensen Huang", "claim": "China reaches native advanced lithography",
    #  "metric": "lithography capability", "target": "native/advanced", "by": "2030",
    #  "condition": None, "entity": "China"}
    # who + claim required; at least one of metric/target/by; entity = ticker/company/asset or None.
]

RELATIONS = [
    # Graph edges between named entities, only as stated in the video.
    # {"from": "Nvidia (NVDA)", "rel": "acquires", "to": "Hugging Face", "note": "..."}
    # rel ∈ acquires | invests_in | partners_with | supplies | customer_of | competes_with |
    #       owns_stake | endorses | criticizes
]

OTHER_NEWS = [
    # {"icon": "...", "title": "...", "tag": "..."} or leave as [] if everything folded into a theme
]

GLOSSARY = [
    # {"term": "...", "def": "..."} × as needed, one tightened sentence each
]
