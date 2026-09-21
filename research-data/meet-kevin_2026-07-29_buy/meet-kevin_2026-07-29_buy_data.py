"""Data file for Meet Kevin (Kevin Paffrath) — Buy."""

META = {
    "title": "Buy.",
    "channel": "Meet Kevin",
    "speakers": "Kevin Paffrath (\"Meet Kevin\")",
    "date": "2026-07-29",
    "video_url": "https://www.youtube.com/watch?v=A7uq1yLpti8",
    "thread_line": "5 threads · 'the great suckening' (liquidity drained by $80B+ corporate capital raises) as the real driver of the AI-name selloff, South Korea's KOSPI memory-concentration unwind versus the S&P's minimal 2.5% memory weighting, SK Hynix's genuinely strong earnings despite a headline miss, a hawkish-hold Fed call with September as the real risk meeting, and a widening Iran conflict drawing in China and Russia.",
    "category": "market",
}

SNAPSHOT = [
    "Kevin's core thesis is 'the great suckening': roughly $185B+ pulled out of markets in about 8 weeks via corporate capital raises (Google $80B, SpaceX $85B, SK Hynix's $25B ADR listing, Meta) is the real driver of the recent selloff, not a broken AI thesis — combined with rising yields (40-60bps) from resumed Iran tension, this triggered a leveraged-ETF and hedge-fund deleveraging unwind (JPMorgan cited: hedge funds ~50% levered, leveraged ETFs delevered ~75%).",
    "Draws a sharp contrast between South Korea's KOSPI index (roughly 50% memory stocks via Samsung and SK Hynix) and the S&P 500 (only about 2.5% memory) — frames the Korean market's correction as a leverage/margin unwind in an overconcentrated index, not a memory-fundamentals problem, while noting the S&P 500 equal-weight index made fresh all-time highs during the same period.",
    "Defends SK Hynix's earnings in detail: despite a technical 5.4% revenue miss (attributed to high-bandwidth-memory contract pricing lagging 4x-higher DRAM/NAND spot prices), margins came in over 83% and the company signed 10 long-term HBM supply contracts — framed as smoothing out memory's usual boom-bust cyclicality, more like a defense contractor's backlog model.",
    "Predicts a 'hawkish hold' from the Fed this meeting (no hike today, roughly 35% market-implied odds), with Kevin Warsh buying time for two more employment data sets before the September 16 meeting, where market-implied hike odds jump to roughly 80% — separately flags a clear week-over-week labor market decay trend and 2026 tech layoffs already exceeding all of 2025's total.",
    "Iran conflict has resumed and is widening beyond a US-Israel-vs-Iran framing: cites a surprise attack on a Jordan airbase, a walked-back Ukrainian strike on an Iranian ship in the Caspian Sea, China reportedly selling Iran $60-80M in portable air-defense systems (MANPADS), and Russia enabling Iranian drone manufacturing — frames this as an emerging two-axis alignment (US/Israel/Ukraine vs. Russia/China/Iran).",
    "Separately flags CoStar falling 12% after-hours, tied to weak real estate transaction volumes (a rate-driven volume problem, not necessarily a price-decline problem) as a smaller but notable earnings miss the same week.",
]

THEMES = [
    {
        "id": "great-suckening",
        "tags": ["finance", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — expects unwind to ease around August 3",
        "title": "'The Great Suckening': Liquidity Drained by $185B+ in Capital Raises Is Driving the Selloff",
        "lead": "**Kevin's central explanation for the AI-name selloff:** it's not a broken thesis, it's roughly $185 billion pulled out of the market in about 8 weeks through a wave of well-timed corporate capital raises, compounded by rising yields from resumed Iran tension.",
        "bullets": [
            "Cites a specific list of raises in a tight window: Google raised $80 billion, SpaceX raised $85 billion, SK Hynix listed a $25 billion ADR, and Meta separately went to markets — all timed, in his view, to capture a 'frothy' fundraising environment before conditions worsened.",
            "Yields rose roughly 40-60 basis points across the curve during the same period (equivalent to about two Fed rate cuts' worth of tightening), driven mostly by the resumption of Iran-related tension, compounding the liquidity drain.",
            "Cites JPMorgan data that hedge funds are now roughly 50% levered and leveraged ETFs have delevered by about 75% — framing the resulting selloff as a leverage-driven mechanical unwind, not a fundamentals repricing.",
            "Key distinction he draws: the S&P 500 equal-weight index (RSP) made fresh all-time highs repeatedly during this same stretch — the pain, in his framing, is concentrated specifically in the largest, most-levered hardware/AI names, not the broad market.",
            "Expects the deleveraging phase to ease around August 3, which he calls short-term bullish for a bounce/recovery in the affected hardware names specifically — distinct from his separate, longer-term (2-5 year) concern about labor market decay.",
        ],
        "quote": {"text": "There should be no freaking surprise the stock market is having trouble going to all-time new highs on hardware.", "cite": "— Kevin Paffrath"},
        "watch": "Kevin is explicit this is a short-term, technical bullish call (a bounce/recovery in oversold names) layered on top of a separate, more cautious 2-5 year view on labor market weakness — the two aren't the same call.",
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Raised $80 billion, cited as one of the largest contributors to recent market liquidity drain.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SpaceX", "blurb": "Raised $85 billion, cited alongside Google as a major liquidity-draining capital raise.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Meta (META)", "blurb": "Also went to capital markets to raise money during the same window; earnings due within days of this video.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "kospi-concentration",
        "tags": ["semis", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — leverage unwind, not a memory-demand problem",
        "title": "KOSPI's 50% Memory Concentration vs. the S&P's 2.5% — a Leverage Unwind, Not a Fundamentals Break",
        "lead": "**Kevin draws a direct index-composition comparison to argue the Korean memory-stock selloff is structurally different from anything happening in the US market.**",
        "bullets": [
            "South Korea's KOSPI index had become roughly 50% memory stocks, driven almost entirely by Samsung and SK Hynix — he compares this to imagining half the S&P 500 being one single sector, calling the concentration itself the core risk factor.",
            "By contrast, memory represents only about 2.5% of the S&P 500 — meaning even a violent memory-sector unwind has structurally limited ability to drag down the broader US index the way it can crater the KOSPI.",
            "Frames the Korean selloff explicitly as a leverage/margin/debt unwind within an overconcentrated index rather than a genuine memory-demand or pricing problem — 'earnings have been fan-frickin-tastic,' in his words, even as the stocks got hit.",
            "Reiterates that DRAM and NAND prices are up roughly 4x year-over-year, underscoring that the selloff is a positioning/leverage story layered on top of, not a reflection of, weak underlying memory fundamentals.",
        ],
        "quote": {"text": "Imagine memory literally being 50% of the S&P 500. That'd be crazy.", "cite": "— Kevin Paffrath"},
        "watch": None,
        "names": [
            {"name": "Samsung Electronics", "blurb": "One of two companies (with SK Hynix) responsible for KOSPI's roughly 50% memory-sector concentration.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "sk-hynix-deep-dive",
        "tags": ["semis"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — headline miss masks genuinely strong underlying results",
        "title": "SK Hynix's Earnings Were Actually Great — the Headline Miss Is a Pricing-Mix Artifact",
        "lead": "**Kevin walks through why SK Hynix's technical revenue miss overstates any real weakness**, arguing the underlying margin and contract data tell a much stronger story.",
        "bullets": [
            "SK Hynix missed revenue by roughly 5.4%, but posted margins over 83% — a very strong result by any standard, and one he says got lost in the headline-miss framing.",
            "Attributes the revenue miss specifically to high-bandwidth memory (HBM) pricing: unlike DRAM and NAND (which trade near spot prices, up roughly 4x year-over-year), HBM sells on long-term contracts that lag current spot pricing, partly on the expectation that prices will normalize.",
            "SK Hynix signed 10 new long-term HBM supply contracts this quarter — compares this to a defense contractor's backlog model, smoothing out memory's usual boom-bust cyclicality rather than fully capturing today's elevated spot prices.",
            "Notes SK Hynix carries a higher proportion of HBM in its mix compared to Micron, which explains part of the difference in how the two companies' revenue lines react to the same spot-price environment — flags this as worth tracking across the sector.",
        ],
        "quote": {"text": "83% margin is so freaking good. It is such good margin.", "cite": "— Kevin Paffrath"},
        "watch": None,
        "names": [
            {"name": "SK Hynix", "blurb": "Missed revenue by 5.4% (a pricing-mix artifact from HBM long-term contracts) but posted 83%+ margins and signed 10 new long-term HBM contracts.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Micron (MU)", "blurb": "Referenced for comparison, carrying a lower proportion of HBM in its product mix than SK Hynix.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "fed-hawkish-hold",
        "tags": ["macro-rates"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — September 16 flagged as the real risk meeting",
        "title": "Fed Preview: A 'Hawkish Hold' Today, With September as the Real Risk Meeting",
        "lead": "**Kevin's specific, dated Fed call:** no hike at this meeting, but a deliberately non-committal tone from Kevin Warsh that leaves the door wide open for September.",
        "bullets": [
            "Predicts Warsh holds rates (market pricing implies roughly 35% odds of a hike today) while explicitly avoiding forward guidance, buying time to see two more full months of employment data (July and August) before the September 16 meeting.",
            "Flags a clear week-over-week decay trend in labor data even as headline numbers (like ADP at 15K) stay roughly stable versus the prior week — treats this decay trend, not the headline print, as the more important signal for long-term positioning.",
            "Notes market-implied odds of a hike jump to roughly 80% for the September 16 meeting, up sharply from today's ~35% — largely because 'any reason to hold is starting to evaporate' given the resumed Iran conflict's inflationary pressure.",
            "Separately flags that 2026 has already produced more technology-sector layoffs than all of 2025 combined, pushing back on venture-capital claims (citing a Ramp study) that AI is a net job creator in the near term — argues that's likely true over 50-100 years but the opposite in the near term.",
        ],
        "quote": {"text": "No hike today, but get ready September — especially with the resumption of the Iran war. Any reason to hold is starting to evaporate, which isn't good.", "cite": "— Kevin Paffrath"},
        "watch": "Kevin explicitly separates his short-term bullish call (post-deleveraging bounce) from his medium-term caution on the labor market — he says labor weakness won't get priced into stocks over 1-6 months, but matters for not being reckless with leverage over a 2-5 year horizon.",
        "names": None,
    },
    {
        "id": "iran-widening",
        "tags": ["geopolitics"],
        "color": "red",
        "badge": "Flagged risk",
        "status": "WATCHING — conflict widening beyond a two-party framing",
        "title": "Iran Conflict Widens: China and Russia Backing Iran Against a US-Israel-Ukraine Axis",
        "lead": "**Kevin argues the Iran conflict is more geopolitically expansive than the simple 'US/Israel vs. Iran' framing** most coverage uses.",
        "bullets": [
            "CENTCOM reported a surprise attack on an airbase in Jordan (missiles/rockets intercepted); the administration is separately threatening to confiscate soldiers' phones after images of Iranian strikes appeared on social media, out of concern it helps Iran fine-tune targeting.",
            "A reported Ukrainian strike on an Iranian ship in the Caspian Sea was walked back by Ukraine as a mistake — Kevin reads this skeptically as a possible deliberate 'soft test' of how Iran would react, while noting he doesn't want to be overly cynical about it.",
            "China is reported to be selling Iran $60-80 million worth of MANPADS (portable air-defense rocket launchers), and Russia is reported to be enabling Iranian drone manufacturing — both read as further evidence of China and Russia aligning with Iran's side.",
            "Frames the resulting picture as two loose axes forming: the US, Israel, and Ukraine on one side, and Russia, China, and Iran on the other — explicitly flags this pattern as 'starting to sound like' an escalation toward broader conflict, without predicting that outcome directly.",
        ],
        "quote": {"text": "On one axis you've got the US, Israel, and Ukraine, and on the other axis you have Russia, China, and Iran. That's starting to sound like things are going more in the direction of World War III.", "cite": "— Kevin Paffrath"},
        "watch": "Kevin explicitly frames this as pattern-matching on his part, not a confirmed prediction — he stops short of forecasting a broader war.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4B8", "tag": "Markets", "title": "Track corporate capital-raise volume as a liquidity-drain indicator before assuming an AI-name selloff reflects broken fundamentals."},
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Compare an index's sector concentration (like KOSPI's memory weighting) before reading a single-country selloff as a global demand signal."},
    {"icon": "\U0001F4BE", "tag": "Semis", "title": "Separate HBM long-term-contract pricing from DRAM/NAND spot pricing when judging whether a memory company's revenue miss reflects real weakness."},
    {"icon": "\U0001F3E6", "tag": "Macro", "title": "Watch September 16 (not this meeting) as the real Fed decision point, given the odds gap between today (~35%) and then (~80%)."},
    {"icon": "\U0001F30D", "tag": "Geopolitics", "title": "Track third-party involvement (China, Russia) in the Iran conflict as a widening-risk signal, not just US-Israel-Iran headlines."},
]

CLAIMS = [
    {"who": "Kevin Paffrath", "claim": "Fed rate decision at this meeting and the following one", "metric": "rate-hike probability", "target": "no hike today (~35% implied odds); ~80% implied odds of a hike by the September 16 meeting", "by": "September 16, 2026", "condition": None, "entity": None},
    {"who": "Kevin Paffrath", "claim": "market deleveraging/liquidity unwind eases around a specific date", "metric": "timing of recovery", "target": "improvement expected around August 3, 2026", "by": "August 3, 2026", "condition": "his own technical/timing call", "entity": None},
    {"who": "Kevin Paffrath, citing SK Hynix results", "claim": "SK Hynix revenue miss versus estimates", "metric": "revenue miss", "target": "-5.4%", "by": None, "condition": "attributed to HBM long-term contract pricing lagging DRAM/NAND spot pricing", "entity": "SK Hynix"},
    {"who": "JPMorgan (cited by Kevin Paffrath)", "claim": "hedge fund leverage and leveraged-ETF deleveraging levels", "metric": "leverage level", "target": "hedge funds ~50% levered; leveraged ETFs delevered ~75%", "by": None, "condition": None, "entity": None},
    {"who": "Kevin Paffrath", "claim": "2026 technology-sector layoffs versus 2025", "metric": "layoff count comparison", "target": "2026 year-to-date layoffs already exceed all of 2025", "by": "2026", "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "China", "rel": "supplies", "to": "Iran", "note": "Reportedly selling $60-80 million worth of MANPADS (portable air-defense systems), per Kevin Paffrath"},
    {"from": "Russia", "rel": "supplies", "to": "Iran", "note": "Reportedly enabling Iranian drone manufacturing, per Kevin Paffrath"},
]

HOT_TAKES = [
    {"take": "There should be no freaking surprise the stock market is having trouble going to all-time new highs on hardware.", "cite": "— Kevin Paffrath", "why": "A direct, checkable explanation (liquidity drain from capital raises) offered against a more common 'broken AI thesis' narrative."},
    {"take": "I really think he's going to hawk to us.", "cite": "— Kevin Paffrath", "why": "A specific, dated prediction about Kevin Warsh's tone at that day's FOMC meeting, made before the decision was announced."},
    {"take": "When the labor market rolls, it rolls fast.", "cite": "— Kevin Paffrath", "why": "A blunt warning about nonlinear labor-market risk, used to justify a cautious multi-year (not short-term) stance on leverage."},
    {"take": "CTAs are saying they're going to be selling in every scenario next week... I consistently inverse that. You should probably too.", "cite": "— Kevin Paffrath", "why": "An explicit, actionable contrarian trading heuristic stated as his own personal practice."},
    {"take": "That's starting to sound like things are going more in the direction of World War III.", "cite": "— Kevin Paffrath", "why": "A stark geopolitical escalation claim, immediately followed by his own hedge that he's pattern-matching, not forecasting with confidence."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3E2", "title": "CoStar fell 12% after-hours on weak results, which Kevin attributes to low real estate transaction volumes (driven by high rates) rather than falling property prices — he notes prices haven't fallen in the specific markets he tracks.", "tag": "Earnings"},
]

GLOSSARY = [
    {"term": "The great suckening", "def": "Kevin Paffrath's term for a wave of large corporate capital raises (Google, SpaceX, SK Hynix, Meta) pulling liquidity out of the broader market within a short window, which he argues is the real driver behind a stock selloff rather than deteriorating fundamentals."},
    {"term": "HBM (high bandwidth memory) vs. spot pricing", "def": "HBM is typically sold on multi-year contracts at prices that lag current spot market rates, unlike standard DRAM/NAND which trade closer to spot price — this can make a memory company's revenue appear weaker than spot-price trends alone would suggest."},
    {"term": "CTA (Commodity Trading Advisor)", "def": "A systematic/trend-following trading fund type; Kevin references CTA positioning reports as a contrarian indicator, saying he tends to bet against their consensus stated positioning."},
    {"term": "MANPADS", "def": "Man-Portable Air-Defense Systems — shoulder-fired, portable surface-to-air missile launchers used to shoot down low-flying aircraft."},
]
