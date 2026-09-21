"""
Data file for Jordi Visser weekly update, 2026-09-20: "The Market Didn't Crash, Humanity Didn't
Die — But Crypto Just Broke Out"
"""

META = {
    "title": "The Market Didn't Crash, Humanity Didn't Die — But Crypto Just Broke Out",
    "channel": "Jordi Visser",
    "speakers": "Jordi Visser",
    "date": "2026-09-20",
    "video_url": "https://www.youtube.com/watch?v=BkNzS8Ia-7k",
    "thread_line": "5 threads · crypto-as-the-AI-trade thesis, AI-doom bear porn dismissed as noise, "
                    "why rate hikes and $105 oil no longer move the AI trade, Mag7/portfolio positioning, "
                    "and the agentic-AI infrastructure build-out into biotech and consumer agents",
    "category": "market",
}

SNAPSHOT = [
    "A week of maximal bad-news headlines (AI pause, a 10% AI-extinction claim, oil spiking, a hawkish Fed hike, "
    "10-year rates at 2007 levels) produced a quiet, flat week for stocks — Visser reads that resilience as bullish, not complacent.",
    "**Crypto is the week's real story**: his 46-name crypto index broke to new highs for the year, up **8.4%** on the day, "
    "+14% month-to-date, +32% year-to-date, with Bitcoin +53%, Ethereum +66%, Solana +38% quarter-to-date.",
    "Core thesis: crypto was built for AI agents, not humans — it's the '**ghost city**' infrastructure phase (his China analogy) "
    "waiting for agent-driven demand to fill it, the same 16-year lag as the dot-com build-out to the iPhone/App Store.",
    "He has rotated his own book from **~80% AI trade / 20% crypto** to roughly **20% AI / crypto+silver as the largest weight**, "
    "while still holding Nvidia, Marvell, and Eli Lilly as core AI names.",
    "Dismisses the week's AI-doom headlines (Anthropic researcher's 10% extinction estimate, Dario Amodei's \"slow down\" comment, "
    "agent-swarm fears) as noise engineered for engagement, not tradeable signal.",
    "Argues the AI trade has effectively no rate sensitivity — Nvidia alone is worth more than the entire consumer discretionary "
    "sector — so this week's hawkish 25bp hike and $105+ oil didn't dent Mag7, which sit near all-time highs.",
    "Frames the move as the early agentic-AI economy: Leopold Aschenbrenner's 'automated AI researcher' milestone (Navier-Stokes "
    "solved by 10,000 agents in 88 hours), new consumer-agent launches (Meta's Muse, startup Instinct), and a biotech/IP revaluation thesis anchored on Eli Lilly.",
]

THEMES = [
    {
        "id": "crypto-ai-trade",
        "tags": ["crypto", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "BUYING — largest portfolio weight, rotated out of AI infrastructure names",
        "title": "Crypto index breaks to new highs — Visser calls it \"the most important macro trade\"",
        "lead": "Crypto isn't a side bet on AI — Visser argues it's the actual AI trade, and this week it broke out.",
        "bullets": [
            "His 46-name crypto index (6 public stocks — Coinbase, Robinhood, Circle — plus tokens) made new highs for the year: "
            "**+8.4%** on the day, +14% month-to-date, +32% year-to-date; 43 of 46 names above their 50-day moving average.",
            "Quarter-to-date: **Ethereum +66%**, **Bitcoin +53%**, **Solana +38%** — the three layer-ones he says to focus on.",
            "Thesis: crypto \"was built for AI\" — wealthy institutions holding the $900 trillion fiat system never needed it, "
            "but AI agents transacting digitally do, and that demand is only now arriving.",
            "Ghost-city analogy: like Chinese infrastructure built 2003–2013 ahead of demand, or dot-com buildout before the 2007 iPhone, "
            "crypto's 16-year infrastructure phase is ending as agent-driven usage (tokenization, stablecoins, on-chain velocity) shows up.",
            "Portfolio rotation: roughly **80% AI / 20% crypto** earlier this year is now **~20% AI**, with crypto and silver making up most of the book; "
            "still adding to crypto, not adding to AI infrastructure names at current levels.",
            "Upcoming regulatory tailwinds: US markets expand to **23-hour weekday trading on December 6**, and the SEC rolled out a **5-year exemption for tokenized stocks** — though the Clarity Act itself did not pass this week.",
        ],
        "quote": {"text": "10% chance AI kills humanity. 100% chance crypto was built for AI.", "cite": "— Jordi Visser"},
        "watch": "This is Visser's own concentrated, actively-traded position (he names it explicitly) — not a neutral index; he's been telegraphing this specific pivot since May/June.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Up 53% quarter-to-date; Visser sees another ~15% upside from the current breakout level.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "12+ months"},
            {"name": "Ethereum (ETH)", "blurb": "Up 66% quarter-to-date; one of the three layer-ones he's focused on.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "12+ months"},
            {"name": "Solana (SOL)", "blurb": "Up 38% quarter-to-date.", "stance": "BUYING-ADDING", "conviction": "Medium", "horizon": "12+ months"},
            {"name": "Coinbase, Robinhood, Circle", "blurb": "The public-stock names inside his 46-name crypto index.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Silver", "blurb": "Now makes up most of his portfolio alongside crypto, following the rotation out of AI names.", "stance": "BUYING-ADDING", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "ai-doom-noise",
        "tags": ["ai-infra", "geopolitics"],
        "color": "amber",
        "badge": "Contested",
        "status": "DISMISSED — treated as noise, not a tradeable signal",
        "title": "\"Bear porn\" week — AI-extinction and agent-swarm headlines dismissed as engineered fear",
        "lead": "A week stacked with doom headlines moved hedge fund inboxes but not the market — Visser says that's the tell.",
        "bullets": [
            "An Anthropic researcher's **10% AI-extinction estimate** and Dario Amodei's public call to \"slow down\" drove a rotation "
            "(software up, semis down ~10% relative underperformance) but no lasting damage.",
            "Elon Musk, in a Ted Cruz interview, put the odds at **10-20% chance of AI-driven human extinction within 10 years**, but an **80-90% chance of extreme prosperity** — Visser calls the expected value \"basically all upside.\"",
            "Other viral doom content cited: a claim of no jobs by 2028 (87M views), an \"Anthropic co-founder warns AI agent swarms could seize the internet within a year\" story, and a Hugging Face incident he says triggered real (but overstated) fear.",
            "Visser's read: this content pattern is not new — a \"why AI will save the world\" piece from June 2023 (three months after ChatGPT) shows the doom cycle has repeated for years, and it's timed ahead of the US midterms.",
            "*Geopolitical angle*: he argues adversarial states (Russia, China, Iran) benefit from Americans doubting AI/data-center buildout, so skepticism of the narrative's timing and virality (172M views on one clip) is warranted.",
            "Names the recurring bear voices he dismisses as \"bear porn\": Michael Burry, Jim Chanos on an AI bubble, Jeffrey Hinton's long-running AI-danger warnings, and Ray Dalio's US debt-crisis thesis — versus a largely unreported cancer-vaccine breakthrough (11M views) he says gets buried by doom content.",
        ],
        "quote": {"text": "Everything I read on AI is just a complete gobbledegook of garbage.", "cite": "— Jordi Visser"},
        "watch": "This is Visser's own dismissal, not a resolved debate — the underlying safety concerns (Anthropic's, Hinton's) are from credentialed researchers inside the labs, not fringe accounts.",
        "names": [
            {"name": "Anthropic", "blurb": "Researcher's 10% extinction estimate and Dario Amodei's \"slow down\" comment drove this week's bear narrative; Visser still credits them (with OpenAI) as ahead on frontier capability.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "OpenAI", "blurb": "Named alongside Anthropic as the two labs \"solving the math prizes,\" i.e. with a durable capability lead over open source.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "no-rate-sensitivity",
        "tags": ["macro-rates", "energy"],
        "color": "green",
        "badge": "High conviction",
        "status": "CONFIRMED EVENT — 25bp hawkish hike, 10yr at 2007 levels, oil above $105",
        "title": "Hawkish hike, $105 oil, 10-year at 2007 levels — and the AI trade shrugged",
        "lead": "The macro backdrop looked like a sell signal on paper; Visser says the AI trade has stopped being rate-sensitive.",
        "bullets": [
            "Fed delivered a hawkish 25bp hike; 10-year rates hit their highest level since 2007, oil rose to $105 (Brent briefly $110), yet the S&P finished the week down only ~30bp.",
            "Nvidia's **$5.25 trillion** market cap alone now exceeds the entire consumer discretionary household-durables/retail/restaurant sector (~$1.5 trillion, ex-Amazon) — his argument for why Mag7 has no meaningful rate sensitivity.",
            "Unlike 2008, households have record home equity and locked-in low mortgage rates, so rate-sensitive balance-sheet stress isn't present; gas as a share of disposable income is near historic lows despite the oil spike.",
            "Credit signals confirm calm: HYG relative to his high-yield proxy made new highs, and bond volatility barely moved despite Iran-related oil risk.",
            "The AAII bear reading hit 53 combined with VIX below 20 and S&P above its 50-week average — a combination Visser says has only occurred 9 times in 35 years, with historically strong forward returns (~89% positive, cites a ~50.5% average gain).",
            "Cites economist Mark Zandi's read as accurate point-by-point: economy near full potential, full employment, inflation above 3% driven mainly by energy/tariffs, and AI infrastructure investment now propping up a non-AI economy that's otherwise struggling.",
        ],
        "quote": None,
        "watch": "The AAII/VIX statistical setup is base-rate reasoning over a small sample (9 occurrences) — real, but not a guarantee.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "At $5.25T market cap, cited as evidence the AI trade has decoupled from rate sensitivity; still one of his two largest holdings.", "stance": "OWNS", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "mag7-portfolio",
        "tags": ["ai-infra", "semis", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "HOLDING — reduced AI weight from ~80% to ~20% of portfolio",
        "title": "Mag7 rarely all trade above their 50-day — Visser reads the current stretch as a breakout signal",
        "lead": "All seven Mag7 names have been above their 50-day moving average together on only 8 days all year — and it's happening again now.",
        "bullets": [
            "That all-seven-above-50-day condition occurred just 8 days in 2026 (about 4.5% of trading days); the last prior instance was June 4.",
            "Visser traces much of this year's AI-bubble bearishness to Oracle's CDS blowing out in October of last year, arguing that set the tone even as the group has since rallied.",
            "His own holdings: still owns **Nvidia** and **Marvell** as his two biggest AI-adjacent positions, plus **Eli Lilly** as a large position he considers an AI/biotech name; still holds **Fluence** despite it being down ~80%.",
            "He does not think stocks repeat the Q1 2026 magnitude of AI-driven rally, and isn't adding to AI names at current levels — the incremental capital is going to crypto instead.",
            "Robotics/physical systems named as the next vertical to watch, with **Tesla** flagged as a likely beneficiary.",
        ],
        "quote": {"text": "I don't think we will ever have another big bull market in stocks like the one we saw in the first quarter of this year for AI.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Marvell (MRVL)", "blurb": "One of his two largest AI-adjacent holdings alongside Nvidia.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Eli Lilly (LLY)", "blurb": "Large position he considers part of his AI/consumer-agent thesis via IP and biotech collaboration value.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Fluence", "blurb": "Still held despite being down roughly 80%.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "Its October CDS blowout is, in Visser's view, the origin point of this year's AI-bubble bearishness.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Tesla (TSLA)", "blurb": "Flagged as a name to watch as robotics/physical-systems agents become the next vertical.", "stance": "WATCHING", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "agentic-buildout",
        "tags": ["ai-infra", "biotech", "robotics"],
        "color": "green",
        "badge": "High conviction",
        "status": "EARLY STAGE — Visser says this was expected for 2027, arriving now",
        "title": "The \"automated AI researcher\" milestone is here early — Navier-Stokes solved by agent swarms",
        "lead": "Leopold Aschenbrenner's 2024 roadmap put this milestone in 2027; Visser says the Navier-Stokes and consumer-agent launches this week show it's arriving now.",
        "bullets": [
            "Citing hedge fund manager Leopold Aschenbrenner's 2024 \"Situational Awareness\" paper, Visser frames the current moment as the **automated AI researcher** inflection point — the trigger for a broader economic step-change (GDP, cognitive labor, robotics).",
            "Cites a swarm of **10,000 AI agents solving the Navier-Stokes problem in 88 hours** as evidence — comparing the organizational model to the Manhattan Project's ~600 scientists working in parallel under Groves.",
            "Consumer-agent launches this week: Meta's **Muse** agent and startup **Instinct** (fundraising at a $2.5B valuation), following Mark Zuckerberg's June comment that Meta was \"way behind on the AI side.\"",
            "Biotech/IP thesis: agent-driven collaboration revalues intellectual property — Eli Lilly's continuous IP acquisition and its \"Tune Lab\" biotech collaboration model are his example; he expects breakout, Moderna-style non-fundamental repricing rather than steady appreciation.",
            "Broken macro chain: earnings growing near 30% with essentially zero net hiring outside healthcare — Visser argues the traditional liquidity → GDP → hiring chain no longer applies because agent labor is substituting for headcount.",
            "US corporate earnings and software revenue-per-employee are both breaking out of multi-decade channels, which he reads as the productivity signature of agent adoption rather than a bubble.",
        ],
        "quote": {"text": "We're past humans adopting it. That's why this is working.", "cite": "— Jordi Visser"},
        "watch": "The Navier-Stokes and \"automated AI researcher\" framing rests entirely on Aschenbrenner's roadmap and unverified claims about the agent swarm result — Visser presents it as fact without independent sourcing.",
        "names": [
            {"name": "Meta (META)", "blurb": "Launched its Muse personal AI agent last week, following Zuckerberg's June admission Meta was behind on AI agents.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4B0", "tag": "Crypto", "title": "Treat crypto as the AI trade itself, not a side bet — track the 46-name breakout and BTC/ETH/SOL quarter-to-date moves, not just headline Bitcoin price."},
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Stop reading rate hikes and oil spikes as automatic AI-trade sell signals — Mag7's lack of rate sensitivity held through this week's hawkish hike and $105 oil."},
    {"icon": "\U0001F9E0", "tag": "AI ethics", "title": "Discount viral AI-extinction and agent-swarm headlines as engagement bait rather than tradeable risk unless the market itself reacts — it didn't this week."},
    {"icon": "\U0001F3E5", "tag": "Biotech", "title": "Watch Eli Lilly and similar IP-heavy biotech names for Moderna-style non-fundamental repricing as agent-driven collaboration revalues intellectual property."},
    {"icon": "\U0001F4CA", "tag": "Macro", "title": "Note the rare AAII-bear/low-VIX/structural-bull combination as a historically bullish setup rather than a reason to de-risk."},
    {"icon": "\U0001F916", "tag": "Careers", "title": "Expect earnings growth to keep decoupling from hiring as agent labor substitutes for headcount outside healthcare."},
]

HOT_TAKES = [
    {"take": "10% chance AI kills humanity. 100% chance crypto was built for AI.", "cite": "— Jordi Visser", "why": "provocative framing pairing an extreme doom stat with an extreme certainty claim"},
    {"take": "Everything I read on AI is just a complete gobbledegook of garbage.", "cite": "— Jordi Visser", "why": "blanket dismissal of a wide body of commentary, including credentialed researchers"},
    {"take": "I don't think we will ever have another big bull market in stocks like the one we saw in the first quarter of this year for AI.", "cite": "— Jordi Visser", "why": "a specific, checkable forward call about the ceiling on AI-stock returns"},
    {"take": "There's a 10-20% chance advanced AI leads to human extinction within the next 10 years... but an 80-90% chance of extreme prosperity.", "cite": "— Elon Musk", "why": "numeric extinction-probability claim from a high-profile figure, cited approvingly by Visser"},
    {"take": "This is far more important than AI.", "cite": "— Jordi Visser", "why": "ranks understanding crypto/tokenization above understanding AI for financial advisors' careers"},
    {"take": "We're past humans adopting it. That's why this is working.", "cite": "— Jordi Visser", "why": "asserts non-human (agent) demand, not human adoption, is now the driver — a falsifiable claim about what's driving usage"},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "Bitcoin has further upside from the current breakout level", "metric": "Bitcoin price upside", "target": "another ~15%", "by": None, "condition": None, "entity": "Bitcoin (BTC)"},
    {"who": "Jordi Visser", "claim": "His agentic infrastructure portfolio will outperform the S&P 500", "metric": "outperformance vs S&P 500", "target": "20-40% per year", "by": None, "condition": None, "entity": None},
    {"who": "Elon Musk", "claim": "Advanced AI carries a meaningful chance of causing human extinction, offset by a much larger chance of extreme prosperity", "metric": "extinction probability", "target": "10-20%", "by": "next 10 years", "condition": None, "entity": None},
    {"who": "US Securities and Exchange Commission", "claim": "SEC rolled out an exemption period for tokenized stocks", "metric": "exemption length", "target": "5 years", "by": None, "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "US equity markets will expand to near round-the-clock weekday trading", "metric": "trading hours", "target": "23-hour weekday trading", "by": "December 6, 2026", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Crypto reached its most important macro inflection point, as he predicted in May/June", "metric": "inflection point timing", "target": "achieved", "by": "September-October 2026", "condition": None, "entity": "Bitcoin (BTC)"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F399", "title": "Jensen Huang spoke at the All-In Summit this week (Trump called in during the appearance); Visser points listeners to that interview and Brad Gerstner's, which he called \"very balanced,\" over the doom headlines.", "tag": "AI"},
]

GLOSSARY = [
    {"term": "Ghost city", "def": "Visser's recurring analogy (from Chinese infrastructure built 2003-2013 ahead of demand) for crypto today: the infrastructure is built, but usage — now expected to come from AI agents — hasn't filled it in yet."},
    {"term": "Automated AI researcher", "def": "A milestone from Leopold Aschenbrenner's 2024 \"Situational Awareness\" paper describing AI systems capable of autonomous research; Visser argues this year's model releases show it arriving earlier than the paper's 2027 estimate."},
    {"term": "Recursive self-improvement (RSI)", "def": "AI systems accelerating their own capability gains, which Visser cites as the reason frontier labs are releasing models faster than expected and why safety concerns have intensified."},
    {"term": "AAII bear reading", "def": "A weekly retail-investor sentiment survey; a high bear reading combined with low VIX and a structural bull market (S&P above its 50-week average) is a historically rare, bullish-skewed setup Visser cites this week."},
    {"term": "HYG relative to EF", "def": "Visser's proxy for high-yield credit spreads (HYG ETF vs. his equity-yield benchmark), used to gauge whether credit markets are signaling stress independent of rates.", },
]
