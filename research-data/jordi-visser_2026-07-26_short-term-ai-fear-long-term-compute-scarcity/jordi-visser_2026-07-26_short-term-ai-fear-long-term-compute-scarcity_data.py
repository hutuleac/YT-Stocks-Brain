"""Data file for Jordi Visser (solo) — Short-Term AI Fear, Long-Term Compute Scarcity."""

META = {
    "title": "Short-Term AI Fear, Long-Term Compute Scarcity",
    "channel": "Jordi Visser",
    "speakers": "Jordi Visser (solo)",
    "date": "2026-07-26",
    "video_url": "https://www.youtube.com/watch?v=QHRUwziQ-oE",
    "thread_line": "6 threads · China's full state backing of its AI/stock market as evidence this is a real two-horse race, Google's backlog exploding from $106B to $514B despite negative free cash flow, 'QE for the mind' as the new EPS-engineering lever, renewed compute-scarcity evidence (Kimi K3, GPU tightening, Vera Rubin ramp), why oil/inflation/Fed fears are overblown noise, and a crypto update (Clarity Act stalling, Dogecoin's longest-ever streak below its 20-day).",
    "category": "market",
}

SNAPSHOT = [
    "Visser pushes back hard on the idea China isn't racing the US in AI: the Chinese state is directly supporting its stock market and its AI companies (DeepSeek, Moonshot) with capital, changed listing standards, and insurer buying, because China needs a stable asset class given its falling housing market — this makes it explicitly a two-country race with different strategies (China favoring open-source abundance, the US favoring capitalist monetization).",
    "Google's headline negative free cash flow got attention, but Visser walks through the underlying numbers: revenue growth of 24% (82% in cloud), a backlog that exploded from $106B to $514B in one year, and roughly 70-75% odds (per his own AI-assisted analysis) that the capex program proves value-creative over a 3-5 year horizon — the real risk flagged is chip obsolescence and backlog concentration in OpenAI/Anthropic.",
    "Revisits his 'QE for the mind' thesis from last November: instead of cheap-debt-funded buybacks (the old QE/ZIRP playbook), AI-driven expense cuts now offer far more EPS leverage — a 5% expense reduction can yield a 20% EPS jump for revenue-heavy, labor-heavy companies (cites UPS, Cisco, Jabil, Centene, Walmart as candidates).",
    "More compute-scarcity evidence stacked up this week: Kimi K3 needs too much hardware for most people to actually run it (so it isn't disrupting US labs' daily usage), Moonshot paused new Kimi subscriptions due to demand exceeding capacity, GPU availability is tightening back up, and Nvidia's Vera Rubin ramp is described as in full production.",
    "Frames oil, inflation, and Fed-hike fears as recurring short-term noise investors keep falling for: oil rallied back toward its highs but inflation swaps and breakevens haven't budged, wages/labor participation remain weak, and Visser puts July Fed hike odds at ~35-36% while arguing it wouldn't meaningfully hurt markets even if it happens.",
    "Portfolio notes: Marvell remains his largest position (betting on an optical/photonics step-up still not reflected in earnings), added Applied Optoelectronics (AOI) this week, and released a new Vera Rubin research report covering ~25 names outside his core 100-name portfolio.",
    "Crypto: Bitcoin and Ethereum both had quiet weeks holding recent gains (Bitcoin stable around $64,000) but remain technically in bear markets until they clear their 200-day moving averages; Dogecoin — his 'retail energy' gauge — has now spent 67 days below its 20-day moving average, the longest streak in its history, which he reads as retail still being absent from the market.",
]

THEMES = [
    {
        "id": "china-state-backing",
        "tags": ["geopolitics", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — capital needs intensifying on both sides",
        "title": "China Is Fully State-Backing Its AI Race and Its Stock Market — This Is a Two-Horse Race",
        "lead": "**Visser directly rebuts the idea that China isn't racing the US in AI**, walking through a week of evidence that Chinese state capital is directly propping up both its stock market and its leading AI companies.",
        "bullets": [
            "China's state-owned funds bought nearly 9 billion shares to support the market this week, is changing listing standards to speed index inclusion, and state-backed insurers publicly committed to boosting equity holdings — Visser ties this to China's falling housing market creating pressure for a stable alternative asset class.",
            "DeepSeek (called China's most important AI company) closed a $7B+ funding round in June with an unusual structure where the Chinese government was the only outside party granted voting rights — its associated hedge fund reportedly fell 16% over the week discussed.",
            "Moonshot AI (maker of Kimi K3) is seeking a $50 billion valuation in pre-IPO rounds — Visser contrasts this directly with Anthropic's reported $350 billion valuation to illustrate the capital-scale gap between the two countries' AI ecosystems, even as both sides race to raise more.",
            "Frames China's strategic bet as open-source/abundance-focused versus the US's capitalist/monetization-focused approach, and explicitly says he thinks the US approach will run into difficulty generating the revenue levels people currently assume.",
            "Connects this to why he isn't worried about widening hyperscaler bond spreads or the broader wave of capital raises (Google's $80B raise, Chinese AI raises, OpenAI, Anthropic, SpaceX's $116B unlock) — he frames all of this issuance as liquidity being temporarily absorbed during low-volume summer trading, not a funding crisis.",
        ],
        "quote": {"text": "This is important for you guys to think about... China was heavily involved in supporting [its AI companies] because they've got their own issues if their stock market goes down.", "cite": "— Jordi Visser"},
        "watch": "Visser is explicit that China and the US are pursuing different strategic goals (open-source abundance vs. capitalist monetization), not identical playbooks — the 'race' framing doesn't imply either side is copying the other.",
        "names": [
            {"name": "Anthropic", "blurb": "Not bearish on the company, but its growth rate is expected to fall short of levels discussed just a month prior, given intensifying competition.", "stance": "UNCERTAIN", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "google-backlog-vs-fcf",
        "tags": ["ai-infra", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — verdict hinges on contracted demand converting, not any single FCF print",
        "title": "Google's Backlog Exploded From $106B to $514B — the Negative Free Cash Flow Headline Misses the Story",
        "lead": "**Visser runs Google's own earnings numbers, and separately an AI model, through a probability exercise** to argue the negative-free-cash-flow headline making rounds on social media misses the actual state of the business.",
        "bullets": [
            "Revenue growth is 24% in aggregate (17% search, 82% cloud, 13% YouTube ads) — the issue isn't growth, it's that Google remains capacity-constrained even after heavy spending, which is why it's renting expensive third-party compute (including from SpaceX) to bridge the gap.",
            "Free cash flow was negative for the first time this quarter (operating cash flow $39B vs. capex $45B), but Visser notes this reflects deliberate reinvestment, not distress — the company isn't managing toward near-term positive free cash flow and has ample ability to raise capital if needed.",
            "The contracted backlog grew from $106B to $514B in a single year — called 'unprecedented' — with over half (~$260B) expected to be recognized as revenue over the next 12 months against roughly $200B in expected spend.",
            "Ran the earnings through an AI model for an unbiased read: it independently identified the backlog as 'the whole ball game,' noted improving (not deteriorating) unit economics, and flagged that Google is renting Nvidia chips from SpaceX for roughly $920 million a month — also caught that reported EPS included ~$99B of one-time equity-stake gains, with operational EPS closer to $2.85, slightly below consensus.",
            "That same model put odds at roughly 70-75% that the capex program proves value-creative over a 3-5 year horizon — flagging three specific risks: chip obsolescence (useful life assumptions of 4-6 years being optimistic), ~$1 trillion in off-balance-sheet commitments industry-wide, and backlog concentration risk if it's heavily weighted toward OpenAI/Anthropic specifically.",
        ],
        "quote": {"text": "The exploding backlog supports the thesis that returns will materialize over the five to seven-year depreciation window if conversion rates hold.", "cite": "— Jordi Visser"},
        "watch": "Visser explicitly frames this as a probabilistic bet (70-75%, not certainty) and names the specific failure modes (chip obsolescence, off-balance-sheet commitments, backlog concentration) rather than dismissing the bear case outright.",
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Backlog grew from $106B to $514B in one year despite a headline-negative free cash flow quarter; ~70-75% odds the capex program proves value-creative over 3-5 years.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "3-5 years"},
        ],
    },
    {
        "id": "qe-for-the-mind",
        "tags": ["ai-infra", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — margin benefit not yet reflected in most companies' results",
        "title": "'QE for the Mind': AI-Driven Expense Cuts Are the New EPS-Engineering Lever",
        "lead": "**Visser revisits a paper he wrote last November** arguing AI-enabled cost-cutting now offers a more powerful earnings lever than the cheap-debt buyback playbook that defined the QE/ZIRP era.",
        "bullets": [
            "Old playbook: borrow at 2%, buy back stock effectively yielding 6%, and earnings per share rises even if the underlying business is flat — pure financial leverage.",
            "New playbook, per a paper by Daniel Cornum that Visser cites: because margins are already thin for many large, labor-heavy companies, even a cost reduction under 1% of revenue can increase profits by more than 25%; a 5% expense reduction can yield roughly a 20% EPS jump.",
            "Argues the biggest AI winners may end up being low-margin, high-friction, high-headcount businesses (not tech names) — asked an AI model to identify S&P 500 companies fitting this profile and got UPS, Cisco, Jabil, Centene, and Walmart as examples.",
            "The central adoption challenge isn't teaching employees to use a tool — it's embedding agents directly into workflows as infrastructure, not optional software, which is why most companies haven't yet shown this margin benefit in their results.",
            "Corporate profit margins measured off GDP statistics are at all-time highs and still accelerating — Visser uses this as his key recession-probability gauge, since historically both profit margins and profits themselves decline meaningfully before a recession, and neither is happening now.",
        ],
        "quote": {"text": "You get far more leverage with reducing your expenses through AI [than through financial leverage], and how it flows to the top to the bottom line.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": None,
    },
    {
        "id": "compute-scarcity-evidence",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "BUYING-ADDING — added a new optical name this week",
        "title": "More Compute-Scarcity Evidence: Kimi K3's Hardware Wall, GPU Tightening, Vera Rubin Ramp",
        "lead": "**A cluster of data points this week reinforces Visser's core compute-scarcity thesis** — even a genuinely competitive Chinese model can't be used by most people without dedicated hardware, and physical capacity keeps lagging demand.",
        "bullets": [
            "Kimi K3 needs enough hardware that Visser (who uses Anthropic, OpenAI, Perplexity, Grok, and Gemini daily) says he personally cannot use it, unlike the smaller Kimi K2.5 which fits on his own hardware — argues this makes K3 potentially negative for OpenAI/Anthropic specifically but net positive for essentially every other company, since it demonstrates frontier capability is achievable outside the two leaders.",
            "Moonshot AI (Kimi's maker) paused new subscriptions this week because demand pushed close to their current capacity limits within 48 hours of a product update — cited as direct proof compute remains the binding constraint even for a fast-growing challenger, not just US incumbents.",
            "GPU availability, which had loosened briefly, tightened back up according to Visser's tracked data — he separately cites (with the caveat that it's unverified) reports that Nvidia could produce roughly 1,000 Vera Rubin racks per day, equivalent to about $630B per quarter, as evidence Vera Rubin is in full production.",
            "Portfolio action: Marvell remains his largest position on a specific step-up-function bet in optical/photonics that hasn't shown up in earnings yet; added Applied Optoelectronics (AOI) this week after screening for names with a large-enough technical correction combined with a plausible earnings catalyst.",
            "Released a new Vera Rubin research report (three to four months in the making) covering roughly 25 names outside his core 100-name thematic portfolio, aimed at giving hedge funds and mutual funds more names to evaluate on the 800V DC infrastructure theme.",
        ],
        "quote": {"text": "This is not disrupting the business... you still need the compute power.", "cite": "— Jordi Visser"},
        "watch": "The Nvidia Vera Rubin production-rate figure (1,000 racks/day) is explicitly flagged by Visser as unverified/speculative, not confirmed company guidance.",
        "names": [
            {"name": "Marvell (MRVL)", "blurb": "Remains his largest position on an anticipated optical/photonics earnings step-up not yet reflected in results.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Applied Optoelectronics (AOI)", "blurb": "New addition this week after screening for a sufficiently large technical correction plus a plausible earnings catalyst.", "stance": "BUYING-ADDING", "conviction": "Medium", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Reportedly in full Vera Rubin production, with an unverified production-rate figure cited (~1,000 racks/day).", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "short-term-noise",
        "tags": ["macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — expects continued chop, not a major correction",
        "title": "Oil, Inflation, and Fed Fears Are Recurring Short-Term Noise Against a Secular Earnings Boom",
        "lead": "**Visser's closing macro argument:** as long as earnings and profit margins keep climbing, headline-driven fears (oil spikes, Fed hike odds, credit-spread widening) are noise that markets have repeatedly overreacted to and then reversed.",
        "bullets": [
            "86% of reporting S&P 500 companies have beaten estimates (roughly an 8:1 beat-to-miss ratio), well above the 1-year (80%), 5-year (78%), and 10-year (76%) averages — earnings strength, in his view, remains the dominant story regardless of near-term AI-name chop.",
            "Oil rallied back toward its highs (December contract), but one-year inflation swaps, two-year breakevens, and TIPS haven't moved with it — his conclusion is that 'smart people are not paying attention to what oil is doing' when forecasting inflation, since the same pattern (oil spikes, inflation-fear headlines, then reversal) has repeated multiple times already.",
            "Wages and labor-force participation remain structurally weak, which he uses to argue the labor market doesn't support a hawkish Fed turn regardless of headline noise; puts July Fed hike odds at roughly 35-36%, up modestly, but argues even a hike wouldn't meaningfully damage markets.",
            "Dismisses Oracle's widening CDS spreads (tied to a $7B guarantee) as trivial 'in a world of hundreds of billions of dollars' — groups this with hyperscaler bond-spread widening generally as a recurring scare story he doesn't find credible given balance sheet quality.",
            "Uses a rolling 63-day (3-month) return chart on the S&P since 2019 to make a broader point: even in a secular bull market averaging 15% annualized, double-digit negative 3-month stretches happen almost every year — meaning short-term drawdowns in his own thematic portfolio (which he expects to outperform the S&P by at least 15%/year over the next 3-5 years) don't invalidate the longer thesis.",
        ],
        "quote": {"text": "Don't let this hype that goes through X's perma-bear porn get you in this position.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Oracle (ORCL)", "blurb": "CDS spreads widening on a $7B guarantee — dismissed by Visser as a trivial figure relative to the scale of hyperscaler balance sheets.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "crypto-clarity-act-stalls",
        "tags": ["crypto", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "OWNS — Bitcoin and Ethereum, both still technically bear markets",
        "title": "Clarity Act Stalls Below 50%, Bitcoin and Ethereum Hold Gains, Dogecoin Signals Retail Is Still Absent",
        "lead": "**A mixed crypto update:** legislative progress on the Clarity Act stalled even as institutional voices push for it, while Bitcoin and Ethereum quietly held recent gains without confirming a real trend change.",
        "bullets": [
            "Treasury Secretary Bessent said he believes the Clarity Act is 'at the one-yard line' in the Senate, but Visser notes probability markets still have it below 50% (falling back into the 30s) — Goldman's David Solomon separately called for advancing the crypto bill.",
            "Cites Sandy Kaul's writing on why agentic AI needs crypto/blockchain rails, using the memory-limitation analogy from the film '50 First Dates' to explain why consumer AI agents need massive persistent memory (remembering every past interaction, not just one session) before they can truly function — ties this directly to expected future crypto transaction volume growth.",
            "S&P launched its first-ever crypto index tied to Bitcoin this week — cited as further mainstream institutional legitimization alongside Japan, South Korea, and now Russia's parliament passing a law regulating its crypto market.",
            "Bitcoin held stable around $64,000 and Ethereum bounced off its lows, but Visser repeats that both remain technically in bear markets until they clear their 200-day moving averages.",
            "Dogecoin (his preferred 'retail energy' gauge, chosen because retail speculative behavior shows up there before broader crypto) has now spent 67 consecutive days below its 20-day moving average — the longest such streak in its history — which he reads as clear evidence retail investors remain absent from the market.",
        ],
        "quote": {"text": "The energy in retail is still non-existent until we start seeing Dogecoin trend positively.", "cite": "— Jordi Visser"},
        "watch": "Visser is explicit that Bitcoin and Ethereum 'are not out of their bear market' despite the quiet, stable price action — holding gains is not the same as confirming a new uptrend in his framework.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Held stable around $64,000; still technically in a bear market until it clears its 200-day moving average.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Ethereum (ETH)", "blurb": "Bounced off its lows; still technically in a bear market until it clears its 200-day moving average.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Dogecoin (DOGE)", "blurb": "67 consecutive days below its 20-day moving average, the longest streak in its history — used as a gauge for absent retail speculative energy.", "stance": "WATCHING", "conviction": "Low", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F1E8\U0001F1F3", "tag": "Geopolitics", "title": "Track Chinese state support for its AI companies and stock market as a real signal of AI-race intensity, not a side story."},
    {"icon": "\U0001F4CA", "tag": "AI infra", "title": "Read hyperscaler earnings by backlog growth and conversion odds, not the headline free-cash-flow print alone."},
    {"icon": "\U0001F4B0", "tag": "Markets", "title": "Screen for labor-heavy, thin-margin companies (not just tech) as candidates for an AI-driven EPS re-rating."},
    {"icon": "\U0001F6E2️", "tag": "Markets", "title": "Discount oil-price-driven inflation panic unless inflation swaps and breakevens actually move with it."},
    {"icon": "₿", "tag": "Crypto", "title": "Watch Dogecoin's moving-average behavior as a specific gauge for whether retail speculative energy has returned to markets."},
]

CLAIMS = [
    {"who": "Jordi Visser (AI-assisted analysis)", "claim": "probability Google's capex program proves value-creative", "metric": "probability", "target": "70-75%", "by": "3-5 year horizon", "condition": "his own AI-assisted analysis of Google's earnings", "entity": "Alphabet (GOOGL)"},
    {"who": "Jordi Visser", "claim": "Google's contracted backlog growth", "metric": "backlog value", "target": "$106 billion to $514 billion in one year", "by": None, "condition": None, "entity": "Alphabet (GOOGL)"},
    {"who": "Jordi Visser", "claim": "his thematic portfolio's expected outperformance versus the S&P 500", "metric": "annualized outperformance", "target": "at least 15%/year above the S&P", "by": "next 3-5 years", "condition": "his own forecast", "entity": None},
    {"who": "Jordi Visser", "claim": "probability of a July Fed rate hike", "metric": "hike probability", "target": "~35-36%", "by": "July 2026", "condition": None, "entity": None},
    {"who": "Nvidia (per reports cited by Jordi Visser)", "claim": "Vera Rubin rack production capacity", "metric": "production rate", "target": "~1,000 racks/day, equivalent to ~$630 billion/quarter", "by": None, "condition": "explicitly flagged by Visser as unverified/speculative", "entity": "Nvidia (NVDA)"},
]

RELATIONS = [
    {"from": "China (state)", "rel": "invests_in", "to": "DeepSeek", "note": "$7B+ funding round with the government as the only outside party granted voting rights"},
    {"from": "SpaceX", "rel": "supplies", "to": "Alphabet (GOOGL)", "note": "Renting Nvidia chips to Google for roughly $920 million a month, per Jordi Visser"},
]

HOT_TAKES = [
    {"take": "Even though there's two different goals... this is a race. This is important to understand.", "cite": "— Jordi Visser", "why": "A direct rebuttal to a specific, named counter-narrative he says he keeps hearing that China isn't racing the US in AI."},
    {"take": "I am not a bear on Anthropic, but I do believe their growth rate will never get to the levels that people had talked about just a month ago.", "cite": "— Jordi Visser", "why": "A specific, checkable downgrade of consensus growth expectations for a single named company."},
    {"take": "We will forever be short compute... this is about demand outpacing efficiency gains.", "cite": "— Jordi Visser", "why": "A sweeping, open-ended structural claim about the AI compute market staked as his core long-term thesis."},
    {"take": "By 2030, I'm definitely worried about what will happen to all public companies, including the infrastructure companies. Actually, I think I'm one of the more bearish people when we get to 2030.", "cite": "— Jordi Visser", "why": "A notable self-disclosed long-horizon bearishness that cuts against his own near-term bullish AI-infrastructure calls."},
    {"take": "Don't let this hype that goes through X's perma-bear porn get you in this position.", "cite": "— Jordi Visser", "why": "A blunt dismissal of a specific class of bearish social-media commentary, staked against his own contrary reading of the same data."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3A4", "title": "Sources referenced this episode: a Daniel Cornum paper (via Aaron Levy) on why low-margin businesses may become AI's biggest winners; three podcasts synthesized via a 'mosaic' prompting method (All-In, Moonshots with Emad Mostaque, and Stephen Hoe/Steve of Silicon Data on the token index); Sandy Kaul's writing on agentic AI and crypto infrastructure; a Michael Dell chart on video-generation compute demand.", "tag": "Sources cited"},
    {"icon": "\U0001F310", "title": "S&P launched its first-ever crypto index tied to Bitcoin this week; Russia's parliament passed a law regulating its crypto market, joining Japan and South Korea in recent regulatory moves.", "tag": "Regulatory"},
]

GLOSSARY = [
    {"term": "Jevons paradox", "def": "The pattern where making a resource cheaper and more efficient increases total demand for it rather than reducing it — cited as the reason cheaper AI models expand the total addressable market instead of shrinking it for existing leaders."},
    {"term": "QE for the mind", "def": "Jordi Visser's term (from a November paper) for AI-driven expense reduction functioning as a new EPS-growth lever, replacing the cheap-debt-funded buyback playbook that defined the QE/ZIRP era."},
    {"term": "ROIC (return on invested capital)", "def": "A measure of how efficiently a company turns invested capital into profit — used here to assess whether hyperscaler AI capex is being allocated toward projects with credible expected returns."},
    {"term": "Backlog (RPO)", "def": "Remaining performance obligations — contracted revenue a company expects to recognize in the future but hasn't yet billed; used as the key forward-looking demand signal for cloud/AI infrastructure providers."},
]
