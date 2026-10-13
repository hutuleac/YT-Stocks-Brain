META = {
    "title": "We have *JUST* 7 days left.",
    "channel": "Meet Kevin",
    "speakers": "Kevin Paffrath (Meet Kevin)",
    "date": "2026-10-13",
    "video_url": "https://www.youtube.com/watch?v=XHjzdg83n3k",
    "thread_line": "5 threads · the $140B 'suckening' and the Apple trade · Broadcom's casino comments and vendor financing · the 10-year peak and a bad CPI setup · an Iran deal window of Oct 20-27 · pipelines and the disinflation case",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "About **$140B** of AI capital raises in ~7 days (Broadcom deals tied to Anthropic and OpenAI, SpaceX $40B, Oracle pending) are pulling money out of stocks into higher-yielding bonds.",
    "SpaceX's 30-year bonds are down ~14.8% from par, pushing its borrowing yield to ~8% — mortgage-rate territory.",
    "His repeat trade: Apple rises when the raises hit (bounced off $332, up 14 points); he also called two Meta bounces off $717.",
    "Broadcom CEO Hock Tan's 'casino' comments were misread: the real story is a shift from a memory shortage to a **money shortage**.",
    "10-year at 5.21%, below his 5.27% peak call; a 41bp 2s10s spread and bull flattening read as the bond market pricing an Iran deal.",
    "CPI on Oct 14 is a lose-lose setup: high expected headline, core anchored so low that only ~0.1% or 0 pleases.",
    "Deal window: **Oct 20-27**, around the Fed meeting — a deal could make Warsh's hike 'one and done'.",
    "Gulf pipelines (+4M barrels/day export capacity by end-2027, +7M by end-2028) shrink Hormuz leverage; he sees oil, AI and rates converging toward disinflation.",
]

THEMES = [
    {
        "id": "suckening",
        "tags": ["ai-infra", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "~$140B RAISED IN ~7 DAYS",
        "title": "The 'suckening': $140B of AI raises drain stocks — and lift Apple",
        "lead": "Mega AI capital raises force higher bond yields that pull money out of chip stocks, and Apple is the reliable beneficiary.",
        "bullets": [
            "Raises: a Broadcom deal tied to Anthropic (~$40B), one tied to OpenAI, SpaceX $40B, and an Oracle raise still pending — about $140B.",
            "SpaceX's 30-year bonds fell ~14.8% below par, lifting the effective yield to ~8%.",
            "Pattern: Nvidia, AMD and chip stocks suffer; Apple rallies — it bounced off $332 on the announcements and is up 14 points since.",
            "Investors cherry-pick software too: Salesforce, Palantir, and **Meta**, where he called bounces after the $717 close two days running.",
            "Meta's 'Watermelon' code-name frontier model and Muse drove the rally; Muse users are offered the Max plan free for a year — 'really smart by Zuck', since people forget and renew.",
        ],
        "quote": {"text": "Apple loves it when everyone else gets sucked dry of capital.", "cite": "— Kevin Paffrath"},
        "watch": "The trade calls come from his paid Alpha report, which he promotes in the video.",
        "names": [
            {"name": "Apple (AAPL)", "blurb": "Rallies whenever AI capital raises hit", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "short term"},
            {"name": "Meta (META)", "blurb": "'Pretty bullish'; called bounces off $717", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "SpaceX (SPCX)", "blurb": "$40B raise; 30-year bonds ~14.8% below par, ~8% yield", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "Pending raise", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA), AMD", "blurb": "Chip stocks that suffer during the raises", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Salesforce (CRM), Palantir (PLTR)", "blurb": "Software names investors cherry-pick", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "broadcom-casino",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "STOCK ROLLED OVER",
        "title": "Broadcom's 'casino' comment was right — and the stock is cheap",
        "lead": "Paffrath backs Hock Tan: markets gamble on noise while the real constraint shifts from memory to money.",
        "bullets": [
            "The market fell when one investor put OpenAI's annual recurring revenue at $70B and another at $50B net — 'ridiculous', he says.",
            "Tan is bullish on long-term AI but says productivity needs time; the bottleneck moves from a **memory shortage** to a money shortage.",
            "Broadcom runs vendor financing: raises ~$40B, sells chips to Anthropic, books revenue now and holds the receivables.",
            "He calls it 'dirt cheap' on its PEG ratio versus growth expectations, if reasonable growth continues.",
            "Thesis: models from OpenAI, Anthropic, Grok and Muse keep improving, so the growth doubters are wrong.",
        ],
        "quote": {"text": "we're going to move on from this sort of memory shortage to a money shortage", "cite": "— Kevin Paffrath"},
        "watch": "Vendor financing means Broadcom carries the credit risk on customer receivables.",
        "names": [
            {"name": "Broadcom (AVGO)", "blurb": "Misread CEO comments; vendor financing; 'dirt cheap'", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Anthropic", "blurb": "Chip buyer financed via Broadcom's ~$40B raise", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "OpenAI", "blurb": "$70B vs $50B ARR dispute moved the market", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "rates-cpi",
        "tags": ["macro-rates"],
        "color": "amber",
        "badge": "Contested",
        "status": "CPI DUE OCT 14, 2026",
        "title": "10-year peaked at 5.27%; CPI setup is lose-lose",
        "lead": "Long yields rolling over is bullish, but tomorrow's CPI expectations leave almost no room for a good surprise.",
        "bullets": [
            "10-year at 5.21%, below his 5.27% peak call made ~3 weeks ago; the slope flattened and is now turning down.",
            "2s10s spread at 41bp: 2-year stable, 10-year falling — a 'slightly bullish' flattening as long-run inflation expectations ease near peak oil and CPI.",
            "CPI forecast is 'bizarre': headline month-over-month expected high, core anchored so low only ~0.1% or 0 would please.",
            "Weekly ADP: 24.75K jobs/week, prior revised from 23.75K to 25.25K, partly from AI construction — keeps him on the bull side.",
            "Fed is hiking over geopolitics and AI investment it can't control, risking the labor market; Kevin Warsh's hike re-anchored expectations.",
            "Markets price multiple hikes; a weak CPI plus an Iran deal makes it **one and done** — a 'reverse Volcker' viewer suggests.",
        ],
        "quote": {"text": "Dude, the expectations for tomorrow's CPI report just suck.", "cite": "— Kevin Paffrath"},
        "watch": "He says he'd rather be 'transparent and wrong' and keeps his old calls online; he set a buy-the-dip threshold for paid members only.",
        "names": None,
    },
    {
        "id": "iran-window",
        "tags": ["geopolitics", "energy"],
        "color": "gray",
        "badge": "Speculative",
        "status": "DEAL WINDOW OCT 20-27",
        "title": "An Iran deal between Oct 20 and 27 is his base case",
        "lead": "Loud public threats from both sides mean leftover details are being finished behind closed doors, Paffrath argues.",
        "bullets": [
            "Window sits around the Fed meeting: with a hot CPI, only a Trump-Iran deal avoids an October hike; with a mild one, a deal before the midterms could mean no December hike.",
            "Both sides reportedly accepted parts of each other's proposals.",
            "Noise: Iran calls MI5's foiled attack on a UK air base hosting US bombers a false flag; threats to the US-escorted Strait of Hormuz 'shuttle'; Iran fortifying nuclear sites.",
            "Trump: strike again after the midterms, a third carrier sent to the region.",
            "US position is the strongest ever: a working naval blockade plus truck routes via Pakistan, Afghanistan and Iraq squeezed; the Supreme Leader admitted supply-chain struggles in early September (IRGC-linked comments).",
            "He calls attacking Iran and scrapping the JCPOA without a replacement 'probably a mistake', but says the Iran-as-superpower view is overblown.",
        ],
        "quote": {"text": "the more aggressive this talk gets in public, the closer we are to just finishing some leftover details", "cite": "— Kevin Paffrath"},
        "watch": "He says he's 'willing to be wrong'; no deal means 'massive problems' and a higher 10-year.",
        "names": None,
    },
    {
        "id": "pipelines-disinflation",
        "tags": ["energy", "geopolitics", "macro-rates"],
        "color": "green",
        "badge": "Positive view",
        "status": "PIPELINES BY 2027-2028",
        "title": "Gulf pipelines defuse Hormuz and set up a disinflation convergence",
        "lead": "Diversified export routes shrink Iran's main weapon, and cheaper oil plus AI deflation could bring rates down.",
        "bullets": [
            "CSIS: the post-war threat is to Gulf energy infrastructure; Tehran's strongest weapon is weaponizing the Strait of Hormuz.",
            "New pipelines could add ~4M barrels/day of export capacity by end-2027 and ~7M by end-2028, routing to the Red Sea and Mediterranean.",
            "Pipelines can be attacked (as in Saudi Arabia) but are buried, with only pumping stations exposed, and no sailors die.",
            "Gulf states are tired of Iranian attacks and don't want Iran to have nukes.",
            "Convergence: lower oil, AI deflation after the infrastructure buildout, and rate relief — good for real estate, stocks and the economy.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Watch Apple vs chip stocks on the next big AI raise announcement"},
    {"icon": "\U0001F4CA", "tag": "Macro", "title": "Read the Oct 14 CPI on core, not headline — core is the bar that matters"},
    {"icon": "\U0001F30D", "tag": "Geopolitics", "title": "Mark Oct 20-27 for an Iran deal before the Fed meeting"},
    {"icon": "\U0001F4B5", "tag": "Credit", "title": "Track SpaceX's 30-year bond yield as a gauge of AI capital stress"},
    {"icon": "\U0001F6E2️", "tag": "Energy", "title": "Follow Gulf pipeline capacity as the long-run oil-price lever"},
]

HOT_TAKES = [
    {"take": "the best window to get a deal is between the 20th and the 27th", "cite": "— Kevin Paffrath", "why": "dated geopolitical call"},
    {"take": "this is a dirt cheap stock", "cite": "— Kevin Paffrath", "why": "Broadcom after rollover"},
    {"take": "I think that Trump has finally gotten the United States in the best possible position for negotiating with Iran", "cite": "— Kevin Paffrath", "why": "political call"},
    {"take": "this idea that Iran is going to become a superpower, I think is is uh overblown", "cite": "— Kevin Paffrath", "why": "dismissal"},
    {"take": "I actually think they might end up being one and done", "cite": "— Kevin Paffrath", "why": "Fed path call"},
]

CLAIMS = [
    {"who": "Kevin Paffrath", "claim": "US-Iran deal lands between Oct 20 and Oct 27", "metric": "Iran deal", "target": "signed", "by": "2026-10-27", "condition": None, "entity": "Iran"},
    {"who": "Kevin Paffrath", "claim": "10-year Treasury yield peaked at 5.27%", "metric": "10-year yield", "target": "5.27% peak", "by": None, "condition": None, "entity": None},
    {"who": "Kevin Paffrath", "claim": "Fed's hiking cycle ends after one hike", "metric": "Fed rate hikes", "target": "1", "by": None, "condition": "weak CPI plus an Iran deal", "entity": None},
    {"who": "Kevin Paffrath", "claim": "Only an Iran deal prevents an October Fed hike if CPI runs hot", "metric": "October Fed decision", "target": "no hike", "by": "2026-10", "condition": "hot CPI on Oct 14 and a deal before the meeting", "entity": None},
    {"who": "Kevin Paffrath", "claim": "October CPI print released, with expectations he says leave no room to win", "metric": "CPI", "target": None, "by": "2026-10-14", "condition": None, "entity": None},
    {"who": "Kevin Paffrath", "claim": "Gulf pipelines add oil export capacity outside Hormuz", "metric": "export capacity", "target": "+4M bpd / +7M bpd", "by": "2027-12 / 2028-12", "condition": None, "entity": None},
    {"who": "Kevin Paffrath", "claim": "Broadcom is undervalued relative to growth", "metric": "valuation", "target": "re-rating higher", "by": None, "condition": "if reasonable growth continues", "entity": "Broadcom (AVGO)"},
]

RELATIONS = [
    {"from": "Broadcom (AVGO)", "rel": "supplies", "to": "Anthropic", "note": "vendor financing tied to a ~$40B raise"},
    {"from": "Broadcom (AVGO)", "rel": "supplies", "to": "OpenAI", "note": "second financing deal"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: CSIS (Gulf energy threat), the *Wall Street Journal* (Supreme Leader on supply chains), MI5 (UK base plot), ADP weekly data, SocialBlade (channels deleting old videos).", "tag": "Sources"},
    {"icon": "\U0001F4F9", "title": "Paffrath says 99.9% of his right and wrong calls stay online; only a few old videos (e.g. on Dave Ramsey, Grant Cardone) were pulled — unlike channels whose deleted videos show as negative views on SocialBlade.", "tag": "Media"},
    {"icon": "✈️", "title": "Back from vacation in Boston, Cambridge and Salem; American Airlines basic economy was 'pretty damn good'.", "tag": "Travel"},
]

GLOSSARY = [
    {"term": "The suckening", "def": "Paffrath's term for large AI capital raises pulling money out of stocks into bonds."},
    {"term": "Par value", "def": "A bond's face value (100); trading below par raises the yield for new buyers."},
    {"term": "2s10s spread", "def": "Gap between 10-year and 2-year Treasury yields; a falling 10-year with a stable 2-year is a bull flattening."},
    {"term": "Vendor financing", "def": "A supplier funds the customer's purchase, booking revenue now and holding the receivable."},
    {"term": "PEG ratio", "def": "Price/earnings divided by expected earnings growth; below 1 suggests cheap for its growth."},
]
