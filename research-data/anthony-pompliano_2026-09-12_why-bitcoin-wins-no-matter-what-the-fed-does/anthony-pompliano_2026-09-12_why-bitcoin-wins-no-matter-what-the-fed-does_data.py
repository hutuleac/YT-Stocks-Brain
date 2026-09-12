"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Why Bitcoin Wins No Matter What The Fed Does",
    "channel": "Anthony Pompliano",
    "speakers": "Anthony Pompliano, Jordi Visser",
    "date": "2026-09-12",
    "video_url": "https://www.youtube.com/watch?v=Uzc3tBB9pLg",
    "thread_line": "6 threads · rates don't matter to an AI/digital economy, Ethereum's quarter, Robinhood's tokenization bridge, a week of AI escalation (Astra, Navier-Stokes, hacks), Bessent/Trump/Warsh aligned on AI+crypto, and the $2T club of unprofitable giants",
    "category": "market",
}

SNAPSHOT = [
    "Jordi Visser's core thesis: the economy is now digital, not rate-sensitive (no housing/auto debt cycle), so **25 basis points** of Fed action is irrelevant next to 30%+ earnings growth and an accelerating AI trade.",
    "**Ethereum** is the best-performing major asset (>$100B) quarter-to-date — roughly double Bitcoin's return — while the S&P 500 and Nasdaq are both flat, a low-correlation setup Visser reads as bullish for both once stocks catch up.",
    "**Robinhood** is being reframed as an Apple-style multi-revenue platform (prediction markets now out-earning stock trading), with Robinhood Chain on Ethereum/Arbitrum as the tokenization bridge between crypto-native and traditional finance communities.",
    "A single week of AI escalation: OpenAI's **Astra** release, a reported Navier-Stokes solve via ~100,000 GPUs, Jensen Huang declaring AGI reached, an ex-Anthropic employee's doomer exit, and real-world hacks (Boston Scientific, a UK power plant, Iran allegedly feeding war plans to Claude).",
    "Visser argues Bessent, Trump, and Fed nominee Kevin Warsh are functionally aligned on \"we can't lose the AI race to China\" and pro-crypto positioning — making the bear case a bet against the White House, not just the market.",
    "The Clarity Act (crypto market-structure legislation) is priced below 20% to pass this year on prediction markets; Visser thinks passage would trigger a faster-than-expected Bitcoin move by unlocking pension-fund allocation.",
    "Visser's \"$2 trillion club\" — Bitcoin, SpaceX, Anthropic, OpenAI — is roughly $8T combined and largely unprofitable, which he compares to Amazon's multi-decade unprofitable run before its 17,000% rise.",
    "A recurring meta-point: Visser splits people into \"static\" (linear, textbook, doomer) vs. \"dynamic\" (adaptive, online, AI-native) thinkers, and says most bearish takes on rates/oil/AI come from the static camp.",
]

THEMES = [
    {
        "id": "rates-dont-matter",
        "color": "green",
        "badge": "High conviction",
        "status": "FED DECISION PENDING — 81% odds of a 25bp hike (Polymarket, morning of taping)",
        "title": "\"Why anyone would care about 25 basis points is beyond me\"",
        "lead": "Visser's central argument: this economy no longer transmits through interest rates, so the market's rate/oil anxiety is a category error.",
        "bullets": [
            "**Zero** measured rate-sensitivity in the AI trade, per Visser's own weekend research video — despite recurring \"these companies can't handle higher rates, their CDS is blowing out\" chatter.",
            "**Core CPI at 2.4%** year-over-year; Kevin Warsh has publicly disputed how core PCE is calculated and is assembling a group to rework the metric.",
            "Oil's sixth-month contract is up **20%** year-over-year despite doomer predictions (including a widely-wrong call that California would run out of gasoline in July); pipelines are reportedly being built to reduce the Strait of Hormuz's strategic importance.",
            "Contrast with 2022: that hiking cycle came off ultra-low rates, no AI capex boom, a fresh recession, and ~9-10% inflation — a fundamentally different setup than today's 25bp debate.",
            "Historically 10-year yields ran ~200bp above nominal GDP (which would put them near 8% now); that relationship broke in 1997 during the **Asian financial crisis** and never fully returned outside recessions — Visser reads today's lower yields as the economy no longer being housing/auto-debt sensitive.",
            "The S&P 500 was roughly unchanged since **June 2nd** as of taping, despite the AI progress described below — Visser's evidence that the market is completely mispriced relative to what's actually happening.",
            "His framework for why people get this wrong: **static** thinkers (tariffs → inflation, full stop) vs. **dynamic** thinkers (tariffs → does domestic manufacturing respond? do other policy tools blunt it?) — he maps most AI/crypto-adjacent, terminally-online people as dynamic and most traditional-finance doomers as static.",
            "He mocks the **midterm-elections-will-kill-this-rally** narrative (Dems expected to win) as another static, headline-driven worry that will just get retroactively credited to \"Trump paid for it\" once the market moves higher anyway.",
        ],
        "quote": {"text": "This is not an interest rate sensitive market... the AI trade has nothing to do with tenure rates at this point.", "cite": "— Jordi Visser"},
        "watch": "This is Visser's own framing of \"restrictive\" thresholds and rate sensitivity — a real, disputed macro question, not a settled fact.",
        "names": None,
    },
    {
        "id": "market-structure",
        "color": "amber",
        "badge": "Structural critique",
        "status": None,
        "title": "AI agents are front-running hedge funds' own drawdown rules",
        "lead": "Visser breaks market participants into three buckets, and says AI agents are exploiting the predictable, rules-bound reactions of human traders.",
        "bullets": [
            "Bucket one: active hedge fund traders bound by hard drawdown limits (e.g. a 5% cap on a market-neutral book) who must react emotionally to data like PPI prints.",
            "Bucket two: AI agents with no emotional constraints, whose only job is to front-run the predictable reactions of bucket one — sell when the humans sell, then reverse the next day with no memory of yesterday.",
            "Bucket three: retail/long-horizon traders (Visser now counts himself here) who can treat the resulting herky-jerky, low-consistency moves as entry-point opportunities rather than signals.",
            "Visser's read: this dynamic is making short-term trading harder for professional managers, while rewarding people who can ignore the noise and hold a medium-term view (e.g. \"S&P earnings up 20% next year, no recession\").",
        ],
        "quote": None,
        "watch": "Visser's own trading experience runs a hedge-fund/prop background; this is his read on market microstructure, not disclosed order-flow data.",
        "names": None,
    },
    {
        "id": "ethereum-robinhood",
        "color": "green",
        "badge": "High conviction",
        "status": "Q3-TO-DATE — Ethereum ~2x Bitcoin's return; S&P 500/Nasdaq roughly flat",
        "title": "Ethereum's outperformance and Robinhood's tokenization bridge",
        "lead": "Visser's two live examples of tokenization actually happening: Ethereum's standout quarter and Robinhood's business-model shift.",
        "bullets": [
            "**Ethereum (ETH)** is the best-performing major asset (>$100B market cap) quarter-to-date, roughly double Bitcoin's gain, while the S&P 500 and Nasdaq sit near flat — a low-correlation setup Visser thinks precedes stocks catching up alongside crypto.",
            "**Robinhood (HOOD)** now earns more revenue from prediction markets than from stock trading, and Morgan Stanley upgraded the stock this week — explicitly *not* for crypto revenue, but because Robinhood is becoming Apple-like: multiple service revenue streams.",
            "Robinhood Chain (built on Ethereum via Arbitrum) is driving 24/7 active trading volumes, currently dominated by memecoins — which Visser frames as the leading edge of a broader tokenization wave, not the point itself.",
            "He contrasts Robinhood's collaborative trading-community culture (from attending a Robinhood event) with the traditionally combative culture of Wall Street trading floors.",
            "Robinhood, Moomoo, and Interactive Brokers now all offer agentic/paper-trading tools; Visser is releasing a GitHub-based backtesting tool for subscribers and frames agentic trading practice as an entrepreneurship on-ramp for kids (he mentions his son uses agents daily).",
        ],
        "quote": {"text": "Robinhood merges not just these technologies together — I think it merges this community aspect.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Ethereum (ETH)", "blurb": "Best-performing major asset quarter-to-date, ~2x Bitcoin's return."},
            {"name": "Robinhood (HOOD)", "blurb": "Morgan Stanley-upgraded on multi-revenue-stream thesis; prediction markets now outearn stock trading."},
            {"name": "Bitcoin (BTC)", "blurb": "Underperformed Ethereum this quarter but still outpaced flat US equity indices."},
        ],
    },
    {
        "id": "valuing-crypto",
        "color": "gray",
        "badge": "Speculative framework",
        "status": None,
        "title": "\"We don't know what the metrics are\" — valuing crypto like the 1990s internet",
        "lead": "Visser is writing a paper on how to value crypto, built around an analogy to how nobody could value the internet in the 1990s either.",
        "bullets": [
            "In the dot-com era, Amazon was valued on \"eyeballs\" and clicks — metrics that, in hindsight, meant nothing; Visser thinks crypto is at the same pre-metric stage now.",
            "He interviewed a figure with roots in Napster, the Ethereum Foundation, and the Solana Foundation for the paper (name garbled in captions as \"William Goyabber\" — likely blockchain writer William Mougayar) about valuing Ethereum as an ecosystem comparable to the early internet.",
            "Visser ran that person's ~2015 TED talk on blockchain through ChatGPT against what's actually happened since: roughly **8.5/10** on the overall vision, but only **5/10** when broken into individual predicted components.",
            "His framing: the world is shifting from valuing companies on revenue to valuing them on **trust** and **velocity/volume of flow** — with Bitcoin and Ethereum benefiting most from the trust side as AI-era hacking risk rises.",
        ],
        "quote": None,
        "watch": "The interviewee's name could not be confidently resolved from auto-captions; treat the attribution as approximate.",
        "names": None,
    },
    {
        "id": "ai-week",
        "color": "amber",
        "badge": "Contested event",
        "status": "WEEK OF SEPTEMBER 8, 2026",
        "title": "A week's worth of AI progress — and AI risk — compressed into days",
        "lead": "Visser: \"There was like a year's worth of progress in the last seven days,\" citing a cluster of releases, claims, and security incidents.",
        "bullets": [
            "OpenAI's **Astra** release: Visser calls it a step-function beyond Grok (\"Grockbot\"), combining agentic execution, chat, image generation, and work tools in one system; he cites Greg Brockman's TBPN interview describing everything now converging inside ChatGPT.",
            "OpenAI reportedly solved the **Navier-Stokes equation** using brute-force compute (~100,000 GPUs) — Visser argues this reopens terminal-value questions for physical/mining companies 5+ years out, though not near-term earnings.",
            "Jensen Huang publicly declared OpenAI had reached AGI the same week Bessent made his \"I am the house\" comment — timing Visser reads as the market completely mispricing the pace of AI progress.",
            "A separate controversy: accusations that OpenAI may have trained on mathematician-submitted problems before appearing to \"solve\" a century-old open problem — an open ethics question, not a settled one.",
            "Security incidents same week: Boston Scientific hacked and warned it won't hit earnings guidance for the rest of the year (also hitting Stryker's stock); a UK power plant hack; and a report that Iran fed war plans and target lists to Claude, which reportedly flagged the activity rather than assisting.",
            "An ex-Anthropic employee who quit after six weeks claiming AI \"will kill everybody\" was amplified by the doomer crowd; Visser and Pompliano treat this skeptically as more attention-driven than substantive, alongside a Paul Tudor Jones WSJ op-ed and a Greg Jensen (Bridgewater) warning, both flagged the same week.",
        ],
        "quote": {"text": "I don't know if you heard the Boston Scientific news this week... they had a hacking and they basically said they're not going to meet their earnings numbers for the rest of this year.", "cite": "— Jordi Visser"},
        "watch": "The Navier-Stokes solve, the Iran/Claude story, and the OpenAI training-on-submissions allegation are all reported/discussed claims from this news cycle, not independently verified by the hosts.",
        "names": [
            {"name": "OpenAI", "blurb": "Astra release and reported Navier-Stokes solve; also Jensen Huang's AGI claim about the company."},
            {"name": "Anthropic (via Claude)", "blurb": "Reportedly flagged Iran's alleged attempt to use Claude for war planning; also the ex-employee doomer exit story."},
            {"name": "Boston Scientific, Stryker", "blurb": "Boston Scientific hacked, warned on earnings; Stryker's stock affected in sympathy."},
            {"name": "Galvanic", "blurb": "Critical-infrastructure cybersecurity startup Jordi Visser is an investor in, founded by an ex-White House staffer."},
        ],
    },
    {
        "id": "washington-alignment",
        "color": "green",
        "badge": "High conviction",
        "status": None,
        "title": "Bessent, Trump, and Warsh are effectively long AI and crypto",
        "lead": "Visser's argument: betting bearish on AI or crypto right now means betting against an aligned White House, Treasury, and incoming Fed chair.",
        "bullets": [
            "Bessent said this week the **US \"cannot lose the AI race to China\"**; Visser notes AI company leadership is in constant, direct contact with the White House.",
            "Bessent, on Steve Bannon's War Room, said: \"if the Bloomberg terminal bros are upset with me, then so be it\" — Visser reads this as Bessent finding his political voice and becoming the more assertive half of a \"carrot and stick\" duo with Trump.",
            "Kevin Warsh (Fed nominee) is described as pro-crypto, pro-Bitcoin, and a believer — per Alan Greenspan's precedent — that the Fed must adapt its framework to AI-driven productivity change.",
            "Visser dismisses the Michael Burry / Jim Chanos bear case (that AI chips depreciate too fast to justify capex) by citing Gavin Baker's point (via a Patrick O'Shaughnessy podcast conversation about a month prior) that H100 resale/rental prices are *higher* now than a year ago, while cloud providers' underlying costs are falling — implying faster-than-expected profits.",
            "Visser also frames Fed politics bluntly: he expects Kevin Warsh not to raise rates for the same reason Powell cut before the last election — \"if you have a job, you have a boss.\"",
        ],
        "quote": {"text": "Why would you bet against this? Like, why would you be fighting against it?", "cite": "— Jordi Visser"},
        "watch": "This is Visser's political read on Fed independence and administration alignment — a contested framing, not a factual claim about Fed decision-making.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Track Ethereum's relative strength vs. Bitcoin this quarter as a signal for whether stocks join the next crypto leg up."},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Watch Clarity Act headlines specifically — Polymarket has it under 20% for this year, so any positive surprise is a real catalyst, not priced in."},
    {"icon": "\U0001F916", "tag": "AI", "title": "Treat this week's AI headline cluster (Astra, Navier-Stokes, AGI claims, hacks) as a pace-of-change signal, not a single verified fact set — cross-check before acting on any one claim."},
    {"icon": "\U0001F4B8", "tag": "Macro", "title": "Stop weighting a 25bp Fed move heavily in a portfolio thesis if earnings growth and AI capex are the actual drivers of this cycle."},
    {"icon": "\U0001F3E6", "tag": "Companies", "title": "Reassess Robinhood as a multi-revenue platform business (prediction markets, tokenization, agentic trading) rather than a commission-free brokerage."},
]

RISKS = [
    "Visser is a working money manager and content creator (Sylvia/CFOSylvia.com) with a direct commercial interest in bullish AI/crypto conviction landing with his audience.",
    "Several factual claims this episode (the Navier-Stokes solve, the Iran/Claude story, OpenAI training on submitted math problems) are relayed from the week's news cycle and discussed as-reported, not verified firsthand by either speaker.",
    "Auto-captions garbled at least one proper noun (the crypto valuation researcher's name) badly enough that the attribution above is a best-effort guess, not a confirmed identification.",
    "Political framing (Fed independence, Bessent/Trump/Warsh alignment) reflects Visser's own read of incentives, not disclosed policy intent from any of the named officials.",
]

HOT_TAKES = [
    {"take": "Why anyone would care about this when earnings are growing 30 plus% is beyond me.", "cite": "— Jordi Visser", "why": "Dismisses the entire Fed-rate-debate as irrelevant noise — a call he's on the hook for if rate moves do matter."},
    {"take": "I feel bad for their children's portfolios 'cause it's probably not going to work out for them.", "cite": "— Jordi Visser", "why": "Direct dismissal of AI/crypto bears as generationally wrong, not just tactically wrong."},
    {"take": "If clarity goes through, I think crypto would go up far faster than people realize.", "cite": "— Jordi Visser", "why": "A specific, falsifiable magnitude/timing call tied to a named legislative catalyst."},
    {"take": "I don't think it's going to happen... I kind of hope it does happen so we can just get rid of it.", "cite": "— Jordi Visser", "why": "A direct, checkable prediction against the 81% market-implied odds of a 25bp hike."},
    {"take": "The reason the market isn't higher is because of the worries people have. No question about it.", "cite": "— Jordi Visser", "why": "States a causal market claim with total certainty rather than as one hypothesis among several."},
]

OTHER_NEWS = [
]

GLOSSARY = [
    {"term": "Clarity Act", "def": "Proposed US crypto market-structure legislation; Visser sees its passage as the key near-term catalyst for pension-fund entry into crypto."},
    {"term": "Robinhood Chain", "def": "Robinhood's blockchain infrastructure, built on Ethereum via Arbitrum, hosting 24/7 tokenized trading currently dominated by memecoin volume."},
    {"term": "Static vs. dynamic thinkers", "def": "Visser's framework for people who reason linearly from past patterns (static) versus those who adapt reasoning to new information and feedback loops (dynamic)."},
    {"term": "$2 trillion club", "def": "Visser's grouping of Bitcoin, SpaceX, Anthropic, and OpenAI — all roughly $2T valuations, none profitable at that scale, together worth roughly $8T."},
]
