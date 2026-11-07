"""Anthony Pompliano x Jordi Visser, 2026-11-07, recorded Thursday after the midterms."""
META = {
    "title": "The Midterms Just Destroyed the AI Trade?",
    "channel": "Anthony Pompliano",
    "speakers": "Anthony Pompliano, Jordi Visser",
    "date": "2026-11-07",
    "video_url": "https://www.youtube.com/watch?v=TDOyoS4SMrk",
    "thread_line": "5 threads · midterms and the AI trade · 492 bonds and 8 call options · hedge-fund 'no mas' · liquidity turning for Bitcoin and gold · oil, Iran and inflation",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Jordi Visser: the blue wave (Texas flipped, Abbott was polling over 60%) slows the next two years of the AI buildout but doesn't change compute demand.",
    "His agentic portfolio has given back **over 60%** of its gains since the early-June peak; he keeps adding and every buy is underwater.",
    "Big idea (after Marc Andreessen): the S&P 500 is **492 bonds and eight call options**; public-company growth ends by 2030 as AI disrupts large workforces.",
    "Hedge funds hit their \"no mas\" moment after Marvell, Intel and the midterms; rumours of two major fund closures and Leopold's fund in trouble again.",
    "Liquidity headwinds are lifting: Brent fell **$20** in three days, DRAM inflation has peaked, tariffs roll off; positive for Bitcoin and gold.",
    "Bitcoin's three-wave correction is near its 200-day average (~73-74k); it trades as part gold, part Nasdaq.",
    "Multiples are compressing: Micron at a P/E of about **3**, Nvidia near single digits; Apple, Berkshire and Eli Lilly are the havens at all-time highs.",
]

THEMES = [
    {
        "id": "midterms-ai",
        "tags": ["ai-infra", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "POST-MIDTERMS · RECORDED THURSDAY",
        "title": "The blue wave slows the AI buildout and sharpens the backlash against it",
        "lead": "Visser sees no hit to compute demand but expects heavier state regulation, more government involvement and margin pressure on data centres.",
        "bullets": [
            "Democrats were favoured; the surprise was the extent, especially **Texas**.",
            "Projects already under construction get finished; a new Texas governor will slow new ones by making builders pay for water and electricity, a margin cost.",
            "A possible data-centre moratorium puts doubt on 2028.",
            "\"AI is hated in this country\": affordability and wealth distribution got attached to AI at the polls.",
            "Government is more involved than a year ago (Intel, OpenAI, Anthropic) and won't allow a single AI winner; cyber risk is now extreme (the Binance hack cited).",
            "Microsoft offering buyouts to **27%** of employees is, to Visser, a warning sign of a \"dystopian\" period.",
            "Extremists are winning on both sides; from a 6% deficit neither big spending nor austerity works, so he sides with Lyn Alden's \"nothing stops this train\".",
        ],
        "quote": {"text": "progress is moving faster than humans can handle it. And those humans are government.", "cite": "— Jordi Visser"},
        "watch": "Visser runs an AI-heavy portfolio and sells research (22V Research); his read on AI headwinds comes from a book that is currently losing money.",
        "names": [
            {"name": "Microsoft (MSFT)", "blurb": "Buyouts offered to 27% of staff.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Binance", "blurb": "Hack cited as a cyber risk for every business.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "bonds-calls",
        "tags": ["ai-infra", "finance"],
        "color": "red",
        "badge": "Non-consensus",
        "status": "PAPER IN PROGRESS",
        "title": "The S&P 500 as 492 bonds and eight call options",
        "lead": "Visser is writing a paper arguing large public companies stop growing by 2030; only the AI spenders are call options, and they carry the risk.",
        "bullets": [
            "Idea from Marc Andreessen: 492 S&P names are bonds, eight (Mag 7 plus SpaceX) are call options.",
            "Bonds return inflation or less; Europe has done nothing since 2007; Ford and GM holders should expect S&P minus 3-5%.",
            "Nebius and CoreWeave are bonds, not call options; the infrastructure trade earns S&P-plus for only 2-3 more years.",
            "No more moats; Larry Page reportedly said he'd bankrupt Google racing to AGI (via Gavin Baker).",
            "Meta, Amazon, Google and Microsoft have all had ~10% one-day falls in the last 12 months; owning them now makes you a trader.",
            "S&P is up less than double digits while earnings grow close to **30%**: one of the worst years for multiples in history.",
            "Equal-weight S&P hit an all-time high the day after the midterms; AI holders had nowhere to hide.",
        ],
        "quote": {"text": "everything in the S&P 500 is basically 492 are bonds. Eight of them are call options which is exactly what I believe.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "SpaceX (SPCX)", "blurb": "A true call option but maybe the biggest government target.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Nebius (NBIS)", "blurb": "Priced like a bond, can't 10x.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "2-3 years"},
            {"name": "CoreWeave (CRWV)", "blurb": "Priced like a bond; debt issues flagged.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "2-3 years"},
            {"name": "Ford (F)", "blurb": "AI loser, sub-S&P returns.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": "decade"},
            {"name": "General Motors (GM)", "blurb": "AI loser, sub-S&P returns.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": "decade"},
            {"name": "Alphabet (GOOGL)", "blurb": "Racing to AGI regardless of cost.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "hedge-funds",
        "tags": ["finance", "semis"],
        "color": "red",
        "badge": "Red flag",
        "status": "DELEVERAGING",
        "title": "Hedge funds hit their 'no mas' moment",
        "lead": "Visser says peak hedge-fund leverage has passed for good, and the AI trade is unwinding through forced sellers, not broken fundamentals.",
        "bullets": [
            "\"Liberation day type panic selling\" on Thursday; rumours of two major hedge funds closing entirely or shutting equity books.",
            "Marvell's $100B+ acquisition (of a different part of the stack) and Intel set off the next leg down; Visser holds Marvell and calls the deal unnecessary.",
            "Situational Awareness reportedly in trouble again; with $100 of capital running $300-400 of positions, time runs out before fundamentals (e.g. Micron) can pay.",
            "Pressure points listed: CoreWeave debt, French debt, Marvell, Intel, Google falling.",
            "Still \"like LTCM\"; he doesn't think the AI trade is over or a bubble.",
            "Nvidia fell about 10% and Micron more than 10% on the day; Micron's P/E is about 3 and Visser doesn't expect it back to 10.",
            "Qualcomm fell 9% on earnings; it's tied to autos and phones, where memory costs hurt (Apple selling fewer phones), not the data-centre upside Marvell has.",
        ],
        "quote": {"text": "the peak of hedge fund leverage has passed. We will never ever ever again be as levered as we were in dollar terms overall.", "cite": "— Jordi Visser"},
        "watch": "The fund closures are rumours; Visser says from his hedge-fund days you never know what's true.",
        "names": [
            {"name": "Marvell (MRVL)", "blurb": "Held; dislikes the big acquisition.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Situational Awareness", "blurb": "Leopold's levered fund, reportedly in trouble again.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Micron (MU)", "blurb": "P/E about 3, multiple won't recover to 10.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Near single-digit P/E; multiple compression.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Intel (INTC)", "blurb": "Helped trigger the leg down.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Qualcomm (QCOM)", "blurb": "Autos and phones, lacks data-centre upside.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "liquidity",
        "tags": ["crypto", "macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "LIQUIDITY TURNING",
        "title": "Falling oil, DRAM and real yields turn liquidity back in Bitcoin's favour",
        "lead": "The headwinds that hurt Bitcoin and gold this year are fading, and the midterms removed bubble risk by pushing out capex.",
        "bullets": [
            "Bond yields rose while inflation expectations fell since March, driving real yields high; 1- and 2-year expectations are now below where the year started.",
            "Slower capex means less capital needed, less pressure on rates; Brad Gerstner puts the buildout at 50bp of GDP.",
            "DRAM price growth has peaked and turns negative into March; tariffs rolling off; oil base effects kick in after March.",
            "Gas fell from $4.40 to $4.10, futures imply $3.75 (~20% drop), so headline CPI should print sharply negative for November.",
            "Bitcoin: five waves up from June, three-wave correction to the 200-day near 73-74k (Elliott wave, learned via Paul Tudor Jones and Stan Druckenmiller).",
            "Bitcoin ETF outstanding shares hit all-time highs despite the drawdown; banks now push Bitcoin. Visser expects it to track gold up and any AI bounce.",
            "Treasury tweaked quarterly-refunding language as it did on Aug 4 before a buyback announcement; affordability may push intervention on the long end.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Growth asset without stock hurdles; liquidity turning.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "3 years"},
            {"name": "Gold", "blurb": "Bouncing; correlated with Bitcoin.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "~40 P/E, immune to AI, a haven.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Berkshire Hathaway (BRK.B)", "blurb": "Haven at all-time highs.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Eli Lilly (LLY)", "blurb": "At all-time highs; his biggest AI trade is doing well.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "oil-iran",
        "tags": ["energy", "geopolitics"],
        "color": "amber",
        "badge": "Speculative",
        "status": "IRAN TALKS SIGNAL",
        "title": "Iran blinked first, and the oil spike may be done",
        "lead": "For the first time Iran signalled readiness to talk; with Vance breaking from Trump, Visser sees less chance of oil moving higher.",
        "bullets": [
            "Brent fell $20 in three days right before the election, after Khamenei okayed talks; earlier drops came from Trump deal promises that never landed.",
            "JD Vance said the war cost the election, diverging from Trump with 2028 in view.",
            "Iran lost the strait, faces a US blockade, and bypass pipelines are 1.75-2.75 years out, so now is its best time to negotiate.",
            "Even when the strait was truly shut, oil never reached the levels people expected.",
            "Raymond James chart: Trump's approval tracked gas prices almost exactly; Pompliano notes young men swung back to blue.",
            "Visser has no oil position.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "ai-use",
        "tags": ["dev-workflow", "health"],
        "color": "gray",
        "badge": "Recommendation",
        "status": "AI THIS WEEK",
        "title": "Chart-to-data extraction and an AI health coach",
        "lead": "Both hosts now run real daily tasks through AI agents.",
        "bullets": [
            "Visser feeds charts from Bloomberg, FT and X into AI to extract approximate data, corrects it, then merges them into one chart; not possible six months ago.",
            "Olive-oil stain: he merged answers from ChatGPT, Gemini and Claude; corn starch plus Dawn worked.",
            "Pompliano built a Grok-based health coach pulling Garmin and Apple Health data, food photos and 12-month goals, with a website dashboard; it ordered his dinner.",
            "Visser journals everything in Muse, including quarterly blood work, Advil use and physical-therapy exercises.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Treat mega-cap tech as trading positions, not set-and-forget holdings"},
    {"icon": "\U0001F9EE", "tag": "Valuation", "title": "Separate the eight AI call options from the 492 bond-like names when sizing equity exposure"},
    {"icon": "₿", "tag": "Crypto", "title": "Watch Bitcoin's 200-day average near 73-74k as the test of the correction"},
    {"icon": "⛽", "tag": "Macro", "title": "Track the November CPI print for the falling-gas effect"},
    {"icon": "\U0001F3E6", "tag": "Market structure", "title": "Expect more forced selling while levered AI funds unwind"},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "Growth of nearly all large public companies will be done by 2030.", "metric": "public-company growth", "target": "ends", "by": "2030", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Hedge-fund leverage will never again reach its recent peak in dollar terms.", "metric": "hedge fund leverage", "target": "below peak", "by": None, "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "The AI infrastructure trade delivers S&P-plus returns for only 2-3 more years.", "metric": "infra trade returns", "target": "S&P-plus", "by": "2-3 years", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Tokenization and agentic commerce will happen over the next two years.", "metric": "tokenization adoption", "target": "happens", "by": "2028", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Headline CPI will print sharply negative for November.", "metric": "headline CPI", "target": "negative", "by": "2026-12", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Year-over-year oil turns negative once base effects kick in after March.", "metric": "oil YoY", "target": "negative", "by": "2027-03", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Micron's P/E will not get back to 10.", "metric": "Micron P/E", "target": "below 10", "by": None, "condition": None, "entity": "Micron (MU)"},
    {"who": "Jordi Visser", "claim": "Bitcoin's correction completes around the 200-day average at 73-74k.", "metric": "BTC price", "target": "73-74k", "by": None, "condition": "assuming equities find a low", "entity": "Bitcoin (BTC)"},
]

RELATIONS = [
    {"from": "Marvell (MRVL)", "rel": "acquires", "to": "a company in a different part of the stack", "note": "$100B+ deal"},
] if False else []

HOT_TAKES = [
    {"take": "the peak of hedge fund leverage has passed. We will never ever ever again be as levered as we were in dollar terms overall.", "cite": "— Jordi Visser", "why": "permanent call"},
    {"take": "AI is hated in this country. It is absolutely hated", "cite": "— Jordi Visser", "why": "political read"},
    {"take": "everything in the S&P 500 is basically 492 are bonds. Eight of them are call options which is exactly what I believe.", "cite": "— Jordi Visser", "why": "contrarian framework"},
    {"take": "Do I think uh micron will ever get to a 10p? No.", "cite": "— Jordi Visser", "why": "valuation call"},
    {"take": "if you don't think the government's going to get involved as this thing gets more dangerous, you're out of your mind.", "cite": "— Jordi Visser", "why": "policy call"},
    {"take": "June firework shows over. We're never again going to see what we saw in the first half for the Agentic Compute trade.", "cite": "— Jordi Visser", "why": "never-again call"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "tag": "Sources", "title": "Sources referenced: Marc Andreessen, Gavin Baker, Brad Gerstner, Lyn Alden, Raymond James, Bloomberg, Paul Tudor Jones and Stan Druckenmiller on Elliott wave, CZ on bank-account risk."},
    {"icon": "\U0001F602", "tag": "Culture", "title": "Midterm memes: \"If you're an AI, pivot to daycares\"; \"Trump got regime change in Texas before Iran\"; Musk and Rogan turned Texas blue."},
    {"icon": "\U0001F1F0\U0001F1F7", "tag": "Crypto", "title": "Korea had stepped back from Bitcoin; Visser: greed always brings people back."},
]

GLOSSARY = [
    {"term": "Elliott wave", "def": "Technical method where trends move in five-wave impulses and three-wave corrections."},
    {"term": "Real yield", "def": "Nominal bond yield minus inflation expectations."},
    {"term": "Equal-weight S&P", "def": "S&P 500 with every stock weighted the same, so mega-caps don't dominate."},
    {"term": "No mas", "def": "Roberto Duran's 1980 quit; Visser's word for funds giving up on risk."},
    {"term": "Quarterly refunding", "def": "Treasury's announcement of how it will finance the debt, including buybacks."},
]
