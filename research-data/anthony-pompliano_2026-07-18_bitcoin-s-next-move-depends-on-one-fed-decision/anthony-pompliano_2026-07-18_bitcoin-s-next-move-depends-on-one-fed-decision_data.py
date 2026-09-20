"""Data file for Jordi Visser x Anthony Pompliano — Bitcoin's Next Move Depends On One Fed Decision."""

META = {
    "title": "Bitcoin's Next Move Depends On One Fed Decision",
    "channel": "Anthony Pompliano",
    "speakers": "Jordi Visser (guest, macro/portfolio manager), interviewed by Anthony Pompliano (host)",
    "date": "2026-07-18",
    "video_url": "https://www.youtube.com/watch?v=fEnq13uJBD0",
    "thread_line": "5 threads · the AI mid-cycle slowdown as a deleveraging (not a thesis break), why Chinese open-source models won't crack the Fortune 500, cooling inflation and a reform-minded Warsh Fed, Bitcoin as the one AI-proof moat while rotating back into memory, and embodied AI as the next semiconductor-driven trade",
    "category": "market",
}

SNAPSHOT = [
    "Jordi Visser's core read: the AI-name selloff (Micron, Marvell, Caterpillar, Modine, etc.) is a deleveraging and a 'second derivative' earnings deceleration, not a broken thesis — he compares it to Nvidia's 2024 pause after its 12x run, and says the 'fireworks show is over' even as names 'hang in there' above long-term ranges.",
    "He's focused on memory (Micron, Samsung, ASML all beat) as the part of the AI trade that hasn't yet seen its earnings 'step-up function'; he restarted a small Micron position this week, funding the research through a personal 100-name portfolio.",
    "On Kimi K3 (Chinese open-source model): he doesn't think it displaces US frontier models inside the Fortune 500, citing hardware access barriers, tooling/bureaucracy, and an under-discussed 'cultural weights' problem in models trained on Eastern-world data.",
    "Cooling inflation data (core services, median, trimmed-mean, CPI core, sticky, trueflation all down; only PCE core is up) plus Kevin Warsh's Fed commentary is read as a reform story, not a hawkish/dovish one — July rate-hike odds are down to ~10%.",
    "He argues today's felt 'inflation' is mostly psychological — people anchoring on pre-COVID prices — and separately reframes the AI/dot-com bubble comparison around demographics (passive, already-wealthy boomers vs. active day-traders) and a coming 'multiple compression' story as AGI approaches.",
    "Crypto allocation is Bitcoin, Ethereum, and MicroStrategy; Bitcoin is framed as the one asset with a genuine AI-proof moat, and Ethereum is highlighted as outperforming Bitcoin on a ~20% month-to-date move tied to agentic/tokenization demand.",
    "He's avoiding SaaS seat-based software entirely on AI-disruption risk, isn't worried about hyperscaler debt (cites ~$2T in contracted RPOs), and expects the next capital rotation to be into embodied AI/robotics — played for now through the semiconductor/infrastructure trade rather than robotics stocks directly.",
]

THEMES = [
    {
        "id": "ai-deleveraging",
        "tags": ["semis", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — bottoming process, not a thesis break",
        "title": "The AI Selloff Is a Deleveraging and a 'Second Derivative' Slowdown, Not a Broken Thesis",
        "lead": "**Visser's framing of the AI-name drawdown:** leveraged players (single-name retail, closed-out Korean margin accounts, market-neutral hedge funds, systematic quant strategies) are unwinding into a volatility spike, layered on top of a genuine earnings deceleration.",
        "bullets": [
            "Compares it directly to Nvidia's 2024 pause: Nvidia went up 12x from ChatGPT to June 2024, then 'only' 48% more over the next two years — still 20%+ annual returns, but not the 12x pace; he says most AI/semi names are now going through the same deceleration.",
            "Silver, gold, and the technology momentum factor all saw their biggest drawdowns in 30 years within a 20-day window; the AI-factor vol is up near 100 versus Bitcoin's vol still around 30.",
            "Micron went from 100 to 1,200 and back to 800 as of the morning of taping — a 30-50% giveback depending on the name — but is still far above its 200-day moving average and was flat in price since 2017 before this run.",
            "His framework for picking winners: focus on companies that **haven't yet seen their earnings 'step-up function'** — Nvidia stopped beating by wide margins after its 2024 peak, while memory (Micron, Samsung, ASML) is still blowing away numbers.",
            "About 40% of S&P 500 companies have reported this quarter with a 16% earnings beat ratio so far, concentrated in banks and insurance — he expects another strong earnings quarter overall.",
            "Restarted a small Micron position this week at a higher average price than where he sold it, citing six weeks of consolidation/deleveraging as reason for renewed confidence; maintains a personal 100-name portfolio to track which AI names are actually re-accelerating.",
        ],
        "quote": {"text": "I think the fireworks show is over, and I think from this point on, some names will do well, some names won't do well.", "cite": "— Jordi Visser"},
        "watch": "Visser flags this as a 30-60% retracement he expects names to 'hang in there' through, not a confirmed bottom — Micron could still sell off another 20% before the memory trade turns.",
        "names": [
            {"name": "Micron (MU)", "blurb": "Restarted a small position this week after a 30-50% giveback from highs; sees memory as the AI trade's next earnings step-up.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "12-18 months"},
            {"name": "Nvidia (NVDA)", "blurb": "Used as the reference case for the 'second derivative' slowdown — no personal position stated.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "open-source-china-cultural-weights",
        "tags": ["ai-infra", "geopolitics"],
        "color": "gray",
        "badge": "Speculative framework",
        "status": "WATCHING — enterprise adoption barrier, not a benchmark question",
        "title": "Kimi K3 Won't Crack the Fortune 500 — and 'Cultural Weights' Are an Underrated Barrier",
        "lead": "**Visser doesn't think Chinese open-source models like Kimi K3 displace US frontier models inside large enterprises**, even where benchmarks are competitive, because the barrier is access, tooling, and bureaucracy — not intelligence.",
        "bullets": [
            "Kimi K3 requires enough local hardware/GPUs to even run it, unlike Anthropic's cloud-hosted models — that alone isolates it from most enterprise use today.",
            "Cites Brad Gerstner's All-In podcast appearance repeatedly: AI is 'the largest TAM that will ever exist' on intelligence, and while open-source usage/token share is already high, actual Fortune 500 enterprises have been reducing open-source use, not increasing it, over the last six months.",
            "Visser's own Fortune 500 experience: long procurement bureaucracy for deciding on a model or software makes a wholesale switch to an unfamiliar Chinese open-source stack unlikely any time soon.",
            "Raises 'cultural weights' as a mostly undiscussed risk — a model trained on more socialist/Eastern-world data could embed different default responses than a Western enterprise wants, comparable to concerns already raised about the Google or TikTok algorithm.",
            "Visser separately warns that self-hosting a model locally doesn't guarantee safety from data exposure once any part of the system touches the internet (agents with credit-card or wallet access, in particular) — undercuts the 'self-host = safe' argument for going open-source.",
            "Discusses Silvian's (his own company's) model router — directing simple queries to cheaper/open-source models and complex ones to the highest-intelligence model — as the more likely path: enterprises adopt a harness/router on the back end rather than employees choosing an open-source model directly.",
        ],
        "quote": {"text": "I don't see the Fortune 500 companies in the United States switching to a Chinese model anytime soon.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": None,
    },
    {
        "id": "inflation-warsh-reform",
        "tags": ["macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — July rate hike priced near 10%",
        "title": "Inflation Data Cools Across the Board; Warsh's Fed Comments Are a Reform Story, Not a Rate Call",
        "lead": "**Nearly every inflation measure came in soft this week except one**, and Visser reads Kevin Warsh's follow-up commentary as a structural reform of how the Fed uses data, not a hawkish or dovish signal.",
        "bullets": [
            "Median inflation, trimmed mean, CPI core, sticky inflation, and 'trueflation' all fell this week; PCE core is the lone measure still at its highs for the year — 2-year inflation swaps also ended the week lower than they started.",
            "Warsh's message, per Visser: the Fed has been dangerously backward-looking, relying on government data that gets revised months later — untenable at the pace AI moves the economy.",
            "July rate-hike odds have fallen to roughly 10%; Visser doesn't expect a hike in September or October either, reasoning the Fed would move before the midterms if it moved at all.",
            "Visser is bullish on Warsh specifically for being young enough to take AI seriously (unlike Jerome Powell, who he says didn't focus on AI until Q3/Q4 last year) and for having a capital-markets background similar to Treasury Secretary Bessent's.",
            "Separately reframes 'felt inflation' as largely psychological: a Jay-Z concert street-interview segment found people citing the *cumulative* five-to-six-year price increase (anchored on pre-COVID prices, e.g. a Tesla Model S refresh costing more than in 2021) rather than the current 3.5-3.9% inflation rate itself.",
            "Ties current 'debasement trade' logic (lower rate-hike odds, big fiscal deficits) directly to crypto: a positive setup that 'we haven't seen play out yet,' evidenced by Bitcoin holding up unusually well during this AI-driven deleveraging.",
        ],
        "quote": {"text": "I think when you go through the inflation data... I'm leaning towards the fact that the inflation side is a non-story for the rest of the year.", "cite": "— Jordi Visser"},
        "watch": "Visser calls the psychological-inflation read his own theory, not a cited study — anchored on anecdotal vox-pop interviews and his own recent car-purchase experience.",
        "names": None,
    },
    {
        "id": "bitcoin-moat-crypto-rotation",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "OWNS — Bitcoin, Ethereum, MicroStrategy",
        "title": "Bitcoin Is 'The Only Thing That Has a Moat' Against AI Disruption",
        "lead": "**Visser's central crypto thesis:** as AGI approaches, every asset eventually runs into a problem where AI disrupts its business model — except Bitcoin, which has no earnings or moat to disrupt in the first place.",
        "bullets": [
            "His crypto allocation is Bitcoin, Ethereum, and MicroStrategy; everything else in his portfolio he frames as either an AI trade or a crypto trade (explicitly includes Eli Lilly and silver as 'AI trades').",
            "Ethereum has outperformed Bitcoin recently, up close to 20% month-to-date as of the prior close — on pace for its best month since August of the prior year — which he ties to AI-agent and tokenization demand for on-chain 'block space.'",
            "On a volatility-adjusted basis, Bitcoin can be sized roughly 3x larger than an AI-thematic position (Bitcoin vol near 30 vs. the AI-factor vol near 100) — his rule for how he's currently allocating between the two.",
            "Flags the Stripe bid for PayPal as a signal of the crypto/AI-agent crossover; runs a 'crypto 40' equal-weight basket (including PayPal and Robinhood among six related names) built specifically around this agentic crossover thesis.",
            "Believes AGI within 3 years makes most public companies' terminal value unknowable past that horizon (extends a 'can't view Adobe or Salesforce past 3 years' framework to physical/energy companies too) — Bitcoin is the explicit exception because it isn't a disruptable business.",
            "Is 'above the 200-day moving average' as his trigger for adding more aggressively to Ethereum; until then he says he's trading it actively rather than treating the bottom as confirmed.",
        ],
        "quote": {"text": "This is the reason why I say Bitcoin is the only thing that has a moat — what's an asset that I don't have to worry about it being disrupted by AI, but I still have to invest.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Core holding; framed as the only asset structurally immune to AI disruption.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Ethereum (ETH)", "blurb": "Owns; adding more aggressively once it clears its 200-day moving average.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": None},
            {"name": "MicroStrategy (MSTR)", "blurb": "Third leg of his crypto allocation alongside BTC and ETH.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Eli Lilly (LLY)", "blurb": "Held as what he calls an 'AI trade,' not a healthcare pick.", "stance": "OWNS", "conviction": "Low", "horizon": None},
            {"name": "Silver", "blurb": "Held as another position he classifies as an 'AI trade.'", "stance": "OWNS", "conviction": "Low", "horizon": None},
            {"name": "PayPal (PYPL)", "blurb": "One name in his 'crypto 40' basket built around the AI-agent/crypto crossover; Stripe reportedly bid for it.", "stance": "WATCHING", "conviction": "Low", "horizon": None},
            {"name": "Robinhood (HOOD)", "blurb": "Another of the six names in his crypto-40/agentic-crossover basket.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Adobe (ADBE)", "blurb": "Cited as a poster child for SaaS terminal-value risk from AI disruption; he has no position and avoids the sector.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "next 3 years"},
            {"name": "Salesforce (CRM)", "blurb": "Cited alongside Adobe as an SaaS name whose terminal value he can't underwrite past 3 years given AI disruption risk.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "next 3 years"},
            {"name": "Anthropic", "blurb": "Doesn't buy the extrapolation to $1T ARR next year, but thinks a doubling to ~$200B is plausible via Jevons paradox.", "stance": "UNCERTAIN", "conviction": "Medium", "horizon": "next 12 months"},
        ],
    },
    {
        "id": "embodied-ai-next-trade",
        "tags": ["robotics", "semis"],
        "color": "gray",
        "badge": "Speculative framework",
        "status": "WATCHING — playing it through semis, not robotics stocks yet",
        "title": "The Next Trade Is Embodied AI — For Now, Played Through Semiconductors",
        "lead": "**Visser's fracking analogy for AI infrastructure:** oil demand only decoupled from price once fracking exploded the *supply* side — and he argues compute/chip supply hasn't yet caught up to exponential token demand the same way.",
        "bullets": [
            "Draws a direct parallel to Micron being flat in price from 2017 to this run: companies whose stock doesn't move for seven years don't build new capacity, which is why memory supply lagged demand so badly.",
            "Token demand is 'going parabolic' because it's driven by machines running 24/7, not humans — cites his own company Silvian's rising token usage (not just cost) as a live example of that dynamic.",
            "Names FSD, humanoids, and consumer agents as three separate upcoming demand waves that all require materially more tokens/compute than exists today.",
            "Cites Elon Musk building 'Terafab' as evidence the chip shortage is the actual bottleneck for the robotics trade, not the robots themselves.",
            "His current approach: play embodied AI through the semiconductor/AI-infrastructure trade rather than buying robotics-specific stocks directly, because he doesn't want to repeat the SaaS-style stock-picking fight he's avoiding elsewhere.",
            "Separately distinguishes this AI buildout from the dot-com bubble on demographics (today's wealth is concentrated in passive, already-rich boomers rather than actively gambling retail) and argues the real risk ahead is market **multiple compression**, not an earnings collapse, as AGI approaches.",
        ],
        "quote": {"text": "So eventually, and I'm sure I will, start buying some of these robotics things — because I do think the next trade is embodied AI.", "cite": "— Jordi Visser"},
        "watch": "Visser frames this as a not-yet-executed intention ('I'm sure I will start buying') rather than a current position.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Track memory earnings (Micron, Samsung, ASML) for the 'step-up function' before adding to AI/semis rather than chasing the names that already had their 3-10x move."},
    {"icon": "\U0001F4B0", "tag": "Crypto", "title": "Size Bitcoin roughly 3x an AI-thematic position on a volatility-adjusted basis while AI-factor vol sits near 100 and Bitcoin vol sits near 30."},
    {"icon": "\U0001F3E6", "tag": "Macro", "title": "Watch September/October Fed meetings, not July, for the next real rate-hike risk — July odds are already down near 10%."},
    {"icon": "\U0001F30F", "tag": "AI ethics", "title": "Weigh a model's 'cultural weights' (what values are baked into its training data) before adopting an open-source model, not just its benchmark scores."},
    {"icon": "\U0001F6D1", "tag": "Markets", "title": "Avoid seat-based SaaS names (Adobe, Salesforce-style) until AI-driven terminal-value risk is actually priced in."},
    {"icon": "\U0001F916", "tag": "Robotics", "title": "Play embodied AI for now through the semiconductor/infrastructure trade — chip supply, not robot design, is the current bottleneck."},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "Anthropic's ARR is more likely to double than to reach a trillion dollars next year", "metric": "annual recurring revenue", "target": "~$200 billion (a doubling)", "by": "next 12 months", "condition": "contrasted against market extrapolations of $1 trillion", "entity": "Anthropic"},
    {"who": "Demis Hassabis (cited by Jordi Visser)", "claim": "AGI timing, forecast since 2010", "metric": "AGI arrival", "target": None, "by": "~2030", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "market-implied odds of a July Fed rate hike", "metric": "probability", "target": "~10%", "by": "July 2026", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "hyperscaler contracted compute demand already committed", "metric": "contracted RPO value", "target": "~$2 trillion across Amazon, Microsoft, Google, Oracle", "by": None, "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Ethereum's month-to-date performance as of the prior close", "metric": "monthly return", "target": "~20% MTD, best month since August of the prior year if it holds", "by": "end of July 2026", "condition": None, "entity": "Ethereum (ETH)"},
]

RELATIONS = [
    {"from": "Stripe", "rel": "acquires", "to": "PayPal (PYPL)", "note": "Reported bid discussed by Jordi Visser as a signal of the crypto/AI-agent crossover; Stripe is privately held"},
    {"from": "Apple (AAPL)", "rel": "partners_with", "to": "Alphabet (GOOGL)", "note": "Using the Gemini model to power Siri, per Jordi Visser"},
]

HOT_TAKES = [
    {"take": "I think the fireworks show is over.", "cite": "— Jordi Visser", "why": "A flat, checkable call on AI-name momentum right as the group is bouncing off a 30-50% giveback."},
    {"take": "This is the reason why I say Bitcoin is the only thing that has a moat.", "cite": "— Jordi Visser", "why": "A structural claim that puts Bitcoin in a different risk category than every equity in his own portfolio."},
    {"take": "I don't see the Fortune 500 companies in the United States switching to a Chinese model anytime soon.", "cite": "— Jordi Visser", "why": "A direct, contrarian-to-the-hype call against Kimi K3 and Chinese open-source models displacing US frontier labs."},
    {"take": "I actually think he's the right person for the job.", "cite": "— Jordi Visser", "why": "A personal endorsement of Kevin Warsh as Fed chair, staked on being 'young enough' to take AI seriously."},
    {"take": "I think this is more of a psychological inflation thing.", "cite": "— Jordi Visser", "why": "Dismisses the headline inflation debate in favor of his own anchoring theory, going against how most guests frame the CPI fight."},
    {"take": "So eventually, and I'm sure I will, start buying some of these robotics things — because I do think the next trade is embodied AI.", "cite": "— Jordi Visser", "why": "A forward-looking personal commitment to a trade he hasn't put capital into yet."},
]

OTHER_NEWS = [
    {"icon": "\U0001F399", "title": "Sources referenced this episode: Brad Gerstner's appearance on the All-In podcast anchors Jordi Visser's TAM and enterprise-adoption argument throughout; Demis Hassabis's essay on AGI (forecasting it since 2010) is cited as the most credible AGI-timing signal he tracks.", "tag": "Sources cited"},
    {"icon": "\U0001F3A4", "title": "Anthony Pompliano ran street interviews at a Jay-Z concert asking attendees why prices feel so expensive — used to argue that what people call 'inflation' is mostly a cumulative five-to-six-year price increase, not the current inflation rate.", "tag": "Field reporting"},
]

GLOSSARY = [
    {"term": "Second derivative slowdown", "def": "When a metric is still growing but at a decelerating rate — Visser's framing for AI earnings that are up hugely year over year but by a shrinking percentage each cycle, as opposed to an outright decline."},
    {"term": "Step-up function (earnings)", "def": "A sudden, large jump in a company's earnings beat rate, as opposed to a gradual improvement — Visser looks for names that haven't had this jump yet as his stock-picking filter within AI/semis."},
    {"term": "Jevons paradox", "def": "The pattern where making a resource more abundant and efficient increases total demand for it rather than reducing it — cited here as the reason AI/compute demand keeps outrunning cost declines."},
    {"term": "Debasement trade", "def": "Positioning in assets (Bitcoin, gold, equities) expected to rise in nominal terms as currency purchasing power falls due to deficit spending and money printing."},
    {"term": "Cultural weights", "def": "Visser's term for default values or worldview baked into a model's training data (e.g. capitalist vs. socialist framing) that could surface unpredictably in a model's responses, distinct from its raw intelligence or benchmark performance."},
]
