"""Data file for Jordi Visser (solo) — Situational Awareness, Hyperscaler Earnings and Warsh: A Bottom for AI Stocks?"""

META = {
    "title": "Situational Awareness, Hyperscaler Earnings and Warsh: A Bottom for AI Stocks?",
    "channel": "Jordi Visser",
    "speakers": "Jordi Visser (solo weekly market update)",
    "date": "2026-08-02",
    "video_url": "https://www.youtube.com/watch?v=VVfTS50v91I",
    "thread_line": "6 threads · why the Situational Awareness (Leopold Aschenbrenner) fund's forced unwind and Citadel/Millennium's takeover of its book likely mark a market-cleansing event, why elevated volatility is now structural rather than temporary, hyperscaler earnings ($1.7T combined backlog) as direct rebuttals to overbuild fears, token efficiency replacing token maxing as the real AI moat, Visser's technical bottom-hunting framework, and a Fed/dollar/credit-spread watchlist.",
    "category": "market",
}

SNAPSHOT = [
    "The Goldman Sachs VIP hedge-fund-crowded-positions index had its worst month on record (data back to 2001) relative to the S&P, worse than the Lehman month — banks including Goldman and JPMorgan issued volatility-triggered collateral calls, and Leopold Aschenbrenner's Situational Awareness fund had its stock portfolio bought out by Citadel (with Millennium also bidding) after large AI-related losses.",
    "Visser, who lived through LTCM, the 2007 quant unwind, and Archegos, reads this combination (multiple prime brokers marketing a distressed book, two of the largest multi-strategy funds absorbing it) as a high-probability market-cleansing event, not a sign of a broader systemic crisis — though he stresses this is a probability call, not a guarantee, and discloses he personally lost money and reduced positions this month too.",
    "His core argument is that elevated volatility (tech momentum's worst 18-day and 4-day unwinds on record, sector-neutral factor volatility near historic highs) reflects a permanent structural shift, not a temporary spike — cites his own 'Art of Unlearning the Fed' paper on why AI-compressed terminal value uncertainty keeps leverage/risk-management tighter going forward.",
    "Directly rebuts hyperscaler-overbuild skeptics using their own Q2 earnings language: Google, Amazon, Meta, and Microsoft all independently said demand exceeds available compute capacity, with a combined contracted backlog around $1.7 trillion — and Amazon/Google explicitly said the bulk of new demand is NOT from OpenAI or Anthropic, undercutting the 'circular financing' bear case.",
    "Cites David Sacks (All-In podcast) and Sam Altman (Invest Like the Best) on compute economics: Anthropic is on pace for ~$74B annualized revenue at the halfway mark of the year (aiming for a 10th consecutive 10x year toward $100B+) and OpenAI for ~$75B — with token efficiency, not raw token usage, becoming the real moat as compute stays scarce (his 'gas price and fuel efficiency' analogy).",
    "Technical framework: Visser uses a 'follow-through day' approach (waiting for a high-volume up day 4-10 sessions after a panic low) plus rate-of-change resets (63-day and 30-day) to scale back into positions — has rebuilt a much smaller Micron position (about 1/5th the size of his May position) and highlights Corning as a name that fully recovered after Meta's $6B fiber deal and an Nvidia partnership.",
    "Closing watchlist: Kevin Warsh's Fed held rates as expected (framed again as 'reform, not hawkish'), the dollar is at its most crowded short positioning in four years, a CCC-vs-high-yield credit spread divergence has Visser's attention (tangentially linked to reporting on the Dodgers/Guggenheim/Mark Walter and private credit), and the Clarity Act's passage odds remain below 40%.",
]

THEMES = [
    {
        "id": "situational-awareness-unwind",
        "tags": ["finance", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — high-probability cleansing event, not confirmed",
        "title": "Situational Awareness's Forced Unwind Looks Like a Market-Cleansing Event",
        "lead": "**Visser draws directly on his own history through LTCM, the 2007 quant unwind, and Archegos** to argue the forced liquidation of Leopold Aschenbrenner's Situational Awareness fund — bought out by Citadel, with Millennium also bidding — has the hallmarks of a genuine bottom, not the start of a broader crisis.",
        "bullets": [
            "The Goldman Sachs VIP hedge-fund-crowded-positions index (tracking the most-owned hedge fund names, data back to 2001) had its worst relative month on record versus the S&P — worse than the month Lehman collapsed — with 7 of the 12 percentage points of damage occurring in just 4 trading days, the worst 4-day move on record including COVID.",
            "Banks including Goldman Sachs and JPMorgan issued volatility-triggered collateral/margin calls; Situational Awareness (reported ~$45B in positions, roughly half to three-quarters in a private Anthropic stake that couldn't be liquidated for cash) had to have its long/short stock book marketed by multiple prime brokers to meet those calls — Citadel ultimately bought the book, with Millennium Management also bidding.",
            "Key reassurance Visser flags: hedge fund strategies broadly were still up over 10% for the year even after the rough stretch, and Citadel/Millennium (both up big for the year and among the best risk managers globally) absorbing the distressed book suggests decompression over time rather than a systemic credit event — he explicitly says his base case is no major follow-on crisis.",
            "Uses Bloom Energy's price action relative to Adobe as a rough proxy for what he believes was a large piece of the fund's short book, noting the position gave back a sizable chunk of its 80%+ year-to-date gain right before the forced sale.",
            "States his own risk framework directly: he's not trying to pick the exact bottom, but multiple technical/positioning signals (crowded positions unwinding fastest on record, extreme rate-of-change resets, a panic-driven volume spike) together historically mark cleansing events rather than the start of something bigger.",
        ],
        "quote": {"text": "I do think there's a high probability that this was a cleansing event... but I'm not here to tell you everything is a guarantee. Everything I do is based on probabilities.", "cite": "— Jordi Visser"},
        "watch": "Visser explicitly says the unwind for people who genuinely need to exit is 'definitely not over' — his claim is only that the largest, most crowded piece of it likely already cleared through Citadel/Millennium absorbing the book.",
        "names": [
            {"name": "Bloom Energy (BE)", "blurb": "Used as a rough proxy for the Situational Awareness fund's largest short position, based on its price action relative to Adobe right before the forced liquidation.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "structural-volatility-shift",
        "tags": ["finance", "macro-rates"],
        "color": "amber",
        "badge": "Structural critique",
        "status": "WATCHING — expects volatility to stay structurally elevated",
        "title": "Elevated Volatility Is a Permanent Structural Shift, Not a Temporary Spike",
        "lead": "**Visser argues the market has moved to a permanently higher volatility regime** because AI is compressing 'terminal value' visibility for every company built on code — a risk-management problem that doesn't resolve once this particular unwind passes.",
        "bullets": [
            "Tech momentum's realized volatility jumped to levels (~108-110) far above prior highs (~70), and his equal-weighted composite of momentum/beta/quality/value factor volatility sits around 38, a level he says has been trending structurally higher for years and 'is never going away.'",
            "Revisits his 'Art of Unlearning the Fed' paper, connecting Treasury Secretary Bessent's own comments about needing forward-looking (not backward-looking academic) models: because AI compresses innovation cycles (what took 10 years now takes 1), terminal value for code-based businesses (his examples: Adobe, Salesforce) becomes much harder to estimate, which by itself produces multiple compression independent of earnings.",
            "Explains why this raises leverage risk specifically: 'ubiquitous AI risk tools create a false sense of confidence' because portfolio optimization software still relies on historical correlations and volatility that may no longer be representative — a bubble in optimization, in his framing, not a bubble in prices.",
            "Notes hedge fund leverage (per SEC Form PF data through Q3 2025) has risen broadly across equities, not just in the basis trade/fixed income — meaning the deleveraging pressure he describes is a multi-asset-class phenomenon, not isolated to one strategy type.",
            "Flags that as tokenization brings 24-hour trading, hedge funds (which operate on much shorter decision clocks than some of the assets they hold) may face new emotional/liquidity pressure from being unable to fully step away from markets, compounding the structural volatility shift further.",
        ],
        "quote": {"text": "Terminal value is gone forever. All of this stuff is happening... the market structure has changed forever because of AI. It is never going back.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": None,
    },
    {
        "id": "hyperscaler-backlog-rebuttal",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — demand explicitly not concentrated in OpenAI/Anthropic",
        "title": "Hyperscaler Earnings Directly Rebut the Overbuild Narrative — $1.7 Trillion Combined Backlog",
        "lead": "**Visser walks through Q2 hyperscaler earnings language almost verbatim** to argue the 'AI capex is overbuilt / revenues won't show up' bear case is contradicted by the companies' own reported numbers, not just his opinion.",
        "bullets": [
            "Quotes from the calls directly: Meta says there's 'nowhere near enough compute for all the demand' and explicitly chose not to rent out spare capacity (despite investor pressure to do so) because leadership expects personal-agent demand to absorb it; Google's Sundar Pichai says they 'continue to be supply constrained'; Microsoft says Azure capacity added mid-quarter 'was quickly monetized'; Amazon says it won't have enough AWS capacity to meet 2026 demand and likely not 2027 either, with 2027 capacity already substantially reserved.",
            "New backlog figures cited: roughly $500B for Amazon, $500B for Google, and a similarly large figure for Microsoft/Meta combined — totaling around $1.7 trillion in contracted backlog across the three-to-four hyperscalers discussed.",
            "Directly addresses circular-financing fears: Amazon and Google both explicitly said their new demand is not concentrated in OpenAI/Anthropic, with the majority of backlog growth coming from typical enterprise cloud contracts across a broad customer mix.",
            "Argues even Chinese open-source models ultimately require hyperscaler compute to actually run (via Bedrock or similar), since the model labs themselves aren't building meaningful compute capacity — reinforcing that hyperscalers remain the structural bottleneck regardless of which model 'wins' any given week.",
            "Frames much of the bearish financial media coverage as ignoring the actual earnings-call facts: 'if the people that have scared you are not writing about the facts in the earnings, then what they're saying is not facts.'",
        ],
        "quote": {"text": "If you don't like those hyperscalers, how about we go to Amazon? ... Don't be short these things. Honestly, like, what are you doing?", "cite": "— Jordi Visser"},
        "watch": "Visser acknowledges directly that there is a real risk 'if OpenAI and Anthropic go out of business,' given some backlog concentration concerns raised in prior weeks — he doesn't dismiss the risk entirely, just argues this week's specific earnings data undercuts the most common version of the bear case.",
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Reiterated as supply-constrained; backlog and demand commentary used to directly rebut prior-week skepticism about its earnings.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Meta (META)", "blurb": "Said demand for compute exceeds what it has, and deliberately chose not to rent out spare capacity given expected personal-agent demand.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Azure capacity added mid-quarter was 'quickly monetized'; traded higher after earnings contrary to capex-cut expectations.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "Won't have enough AWS capacity to meet 2026 demand, likely not 2027 either; 2027 capacity already substantially reserved.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "token-efficiency-moat",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — at least 2 more years before open-source hardware access closes the gap",
        "title": "Token Efficiency Is Becoming the Real Moat as Compute Stays Scarce",
        "lead": "**Citing David Sacks and Sam Altman, Visser argues the AI story is shifting from raw model competition to who can deliver the most intelligence per unit of scarce compute** — a dynamic he compares to fuel efficiency mattering more as gas prices rise.",
        "bullets": [
            "David Sacks (on All-In) reportedly said Anthropic — despite his personal criticism of the company — is the fastest-growing tech company in history, on pace for roughly $74B annualized revenue at the year's halfway mark (targeting another 10x year toward $100B+), with OpenAI on a similar ~$75B annualized pace — combined, roughly $175B in revenue from two companies that had none two years ago.",
            "Sam Altman (on Invest Like the Best) reportedly said OpenAI's conviction to secure massive compute came from watching an exponential model-improvement curve (especially around GPT-4), and that supply — not demand — is today's real bottleneck; near-term compute relief is more likely to come from software/token efficiency gains than from new hardware.",
            "Visser's gas-price analogy: at $1/gallon fuel efficiency doesn't matter, but at $10/gallon everyone pays a premium for the most efficient car — similarly, as compute stays scarce and expensive, users will pay up for the most token-efficient frontier model rather than settle for a cheaper, less efficient one, reinforcing the leaders' pricing power.",
            "Uses a hypothetical (a studio using ultra-efficient AI compute to make a $5B movie for a fraction of the cost) to argue that owning scarce, efficient compute doesn't just generate profit — it can be used to competitively destroy less-efficient rivals.",
            "Estimates at least two more years before hardware access broadens enough for open-source models to be run at scale outside the major labs' infrastructure — reinforcing why he doesn't see near-term disruption risk to hyperscalers from cheaper open models.",
        ],
        "quote": {"text": "If gas is a dollar a gallon, nobody cares about the fuel efficiency. When it's $10, everyone pays a premium for the car with the best mileage.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Anthropic", "blurb": "On pace for roughly $74B annualized revenue at the year's halfway mark, per David Sacks; described as the fastest-growing tech company in history.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "OpenAI", "blurb": "On pace for roughly $75B annualized revenue, per David Sacks; Sam Altman reportedly framed compute supply, not demand, as the current bottleneck.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "technical-bottom-signals",
        "tags": ["semis", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "BUYING-ADDING — small, scaled-in positions",
        "title": "Trading the Lows: Follow-Through Days, Rate-of-Change Resets, and Corning's Recovery",
        "lead": "**Visser lays out his specific technical framework for scaling back into positions** after a panic low, rather than trying to pick an exact bottom.",
        "bullets": [
            "Uses a 'follow-through day' approach (a technician's concept: a high-volume, meaningfully higher close roughly 4-10 sessions after a panic low, confirming an oversold bounce is becoming a real rally rather than short covering) — flags the day after Situational Awareness's panic-driven selloff as showing exactly this pattern on higher volume.",
            "His 63-day (3-month) and 30-day rate-of-change metrics on his thematic portfolio both fully reset (from +50% to roughly flat on the 63-day view) — used as his signal that both price and time conditions for a consolidation have now been met, not just price alone.",
            "Rebuilding Micron in small size (about 1/5th his May position), explicitly not trying to call the exact bottom — his stated view is $800 isn't the best entry but is a reasonable one on the way to an expected $1,500-1,600 over the next year; also added to Marvell and bought a small new position in Applied Optoelectronics (AOI).",
            "Highlights Corning as one of his 10-name concentrated basket: the stock fully recovered to its pre-selloff level after a $6 billion Meta optical-fiber deal (described as equivalent to roughly 100 million homes' worth of fiber) and a separate Nvidia partnership announcement.",
            "His screening method for 'combing through the rubble': names where price is above a still-rising 200-day moving average — his preferred structural signal — even after a sharp near-term pullback (30%+ monthly declines in some cases), cross-checked against earnings-call fundamentals.",
        ],
        "quote": {"text": "I'm not trying to pick the bottom of this. I'm trying to work into something where I don't think the upside is capped.", "cite": "— Jordi Visser"},
        "watch": "Visser is explicit he isn't fully convinced the absolute low is in for Micron specifically — he's starting to scale in on a risk/reward basis, not declaring victory.",
        "names": [
            {"name": "Micron (MU)", "blurb": "Rebuilding a small position (about 1/5th the May size); sees $800 as a reasonable, not optimal, entry toward an expected $1,500-1,600 within a year.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "12 months"},
            {"name": "Marvell (MRVL)", "blurb": "Added to this position during the selloff.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": None},
            {"name": "Applied Optoelectronics (AOI)", "blurb": "Bought a small new position this week.", "stance": "BUYING-ADDING", "conviction": "Low", "horizon": None},
            {"name": "Corning (GLW)", "blurb": "Fully recovered to pre-selloff levels after a $6B Meta optical-fiber deal and an Nvidia partnership announcement; one of his 10-name concentrated basket.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "fed-dollar-credit-watchlist",
        "tags": ["macro-rates", "geopolitics"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — one credit-market signal flagged, not yet confirmed",
        "title": "Fed, Dollar, and a Credit-Spread Divergence Worth Watching",
        "lead": "**A closing macro watchlist**: the Fed did exactly what was expected, but Visser flags one specific credit-market signal he's keeping an eye on even as he stays broadly bullish.",
        "bullets": [
            "The Fed held rates as expected under Kevin Warsh, again framed by Visser as 'reform, not hawkish' rather than a dovish-hawkish binary — ten-year rates sit near 4.70% and August inflation-expectation prints are running close to zero.",
            "The one credit signal that has his attention: a divergence between CCC-rated (option-adjusted spread) credit and broader high-yield spreads, which he says historically tends to be a leading indicator (weak credit starts moving first, then drags the rest) — explicitly ties this to broader private-credit concerns he's been tracking since software stocks fell earlier this year, name-checking unrelated reporting on the Dodgers/Guggenheim/Mark Walter as something worth reading, without drawing a firm conclusion from it.",
            "Dollar positioning is at its most crowded short level in roughly four years even as the dollar has weakened somewhat this week, partly on Bank of Japan speculation — flags the dollar-yen range as looking unusually tightly managed over the past several months.",
            "Recommends an Ezra Klein interview with former Australian PM Kevin Rudd on China's AI strategy as valuable context for understanding China's more open-source, abundance-focused approach versus the US's capitalist one — ties this back to his own long-standing Bitcoin thesis via a Schumpeter/creative-destruction lens.",
            "Notes rising cyber-incident activity (hacks affecting OpenAI, Hugging Face, and reportedly Claude) as worth monitoring, and puts Clarity Act passage odds below 40% — says this matters for crypto-industry entrepreneurs in the near term but not for his long-term Bitcoin thesis.",
        ],
        "quote": {"text": "The Fed did exactly what Wall Street was expecting. So why are the markets so vexed by Kevin Warsh again?", "cite": "— Jordi Visser"},
        "watch": "Visser is explicit the CCC/high-yield credit divergence and the Dodgers/Guggenheim private-credit reporting are things he's flagging to watch, not conclusions he's drawn — 'I don't know what it means, I just know the insurance industry fairly well.'",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Treat a forced hedge-fund liquidation absorbed by the largest, best-capitalized players as a likely cleansing signal, not automatically a systemic warning."},
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Use a 'follow-through day' and rate-of-change reset framework to scale into positions after a panic low, rather than trying to call the exact bottom."},
    {"icon": "\U0001F5A5️", "tag": "AI infra", "title": "Weight hyperscaler earnings-call language (demand vs. capacity, backlog composition) over secondhand commentary when assessing overbuild fears."},
    {"icon": "⛽", "tag": "AI infra", "title": "Track token efficiency, not just raw model benchmarks, as the emerging competitive moat as compute stays scarce."},
    {"icon": "\U0001F4B3", "tag": "Markets", "title": "Watch CCC-vs-high-yield credit spread divergence as an early warning indicator, independent of hyperscaler-specific credit spreads."},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "Goldman Sachs VIP hedge-fund index's monthly relative performance versus the S&P", "metric": "monthly relative return", "target": "-12%, the worst month on record since the index began in 2001, worse than the Lehman month", "by": None, "condition": None, "entity": None},
    {"who": "Google, Amazon, Meta, Microsoft (cited by Jordi Visser)", "claim": "combined contracted compute backlog across the hyperscalers", "metric": "contracted backlog value", "target": "roughly $1.7 trillion combined (~$500B Amazon, ~$500B Google, and a comparably large Microsoft/Meta figure)", "by": None, "condition": None, "entity": None},
    {"who": "David Sacks (cited by Jordi Visser)", "claim": "Anthropic's annualized revenue run-rate at the halfway point of the year", "metric": "annualized revenue", "target": "~$74 billion, targeting another 10x year toward $100B+", "by": "mid-2026", "condition": None, "entity": "Anthropic"},
    {"who": "David Sacks (cited by Jordi Visser)", "claim": "OpenAI's annualized revenue run-rate at the halfway point of the year", "metric": "annualized revenue", "target": "~$75 billion", "by": "mid-2026", "condition": None, "entity": "OpenAI"},
    {"who": "Jordi Visser", "claim": "Clarity Act passage probability", "metric": "passage probability", "target": "below 40%", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Citadel", "rel": "acquires", "to": "Situational Awareness (Leopold Aschenbrenner's fund)", "note": "Bought the fund's long/short stock portfolio after forced margin/collateral calls, per FT reporting"},
    {"from": "Meta (META)", "rel": "partners_with", "to": "Corning (GLW)", "note": "$6 billion optical fiber deal, equivalent to roughly 100 million homes' worth of fiber per Visser's LLM estimate"},
    {"from": "Nvidia (NVDA)", "rel": "partners_with", "to": "Corning (GLW)", "note": "Separate partnership announcement cited by Visser"},
]

HOT_TAKES = [
    {"take": "Compute demand is insatiable. I say it on every interview. I say it every week here.", "cite": "— Jordi Visser", "why": "His single most-repeated, explicitly falsifiable thesis, restated as the one thing he'd want people to remember if everything else he says is wrong."},
    {"take": "Terminal value is gone forever... the market structure has changed forever because of AI. It is never going back.", "cite": "— Jordi Visser", "why": "A sweeping, permanent structural claim about markets that goes well beyond a single trade call."},
    {"take": "I don't think we're mean reverting anymore. We've already seen a structural higher level here than it was.", "cite": "— Jordi Visser", "why": "A specific rejection of mean-reversion assumptions in volatility, directly contradicting how most quant risk models are built."},
    {"take": "If you don't like those hyperscalers... don't be short these things. Honestly, like, what are you doing?", "cite": "— Jordi Visser", "why": "A blunt, direct challenge to anyone shorting hyperscalers against their own earnings-call demand commentary."},
    {"take": "There is no doubt right now that the amount of capital that's being absorbed by AI is massive, and I do believe the disruption happening from AI is real.", "cite": "— Jordi Visser", "why": "A rare explicit acknowledgment of downside credit risk from someone otherwise arguing the bull case, tied to a specific (if unconfirmed) credit-market signal he's watching."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3A4", "title": "Sources referenced this episode: the All-In podcast (David Sacks on Kimi K3 and compute economics); Sam Altman's interview on Invest Like the Best; a widely-shared (1M+ views) contrarian X post from Dwarkesh on compute pricing power; investor Gavin Baker's public commentary on hyperscaler credit spreads; Ezra Klein's interview with former Australian PM Kevin Rudd on China's AI strategy.", "tag": "Sources cited"},
    {"icon": "\U0001F510", "title": "Rising cyber-incident activity flagged, including hacks affecting OpenAI, Hugging Face, and reportedly Claude — Visser says this is worth monitoring as AI infrastructure becomes a bigger attack surface.", "tag": "Cybersecurity"},
]

GLOSSARY = [
    {"term": "Follow-through day", "def": "A technical-analysis signal: a high-volume, meaningfully higher market close occurring roughly 4-10 trading sessions after a panic low, used as confirmation that an oversold bounce may be turning into a genuine rally rather than short covering."},
    {"term": "Rate of change (63-day / 30-day)", "def": "A momentum measure comparing a price level today against its level a set number of trading days earlier (63 days ≈ 3 months, 30 days ≈ 6 weeks); Visser uses extreme positive or negative readings to time when to reduce or add to positions."},
    {"term": "CCC / option-adjusted spread", "def": "The extra yield investors demand to hold the riskiest tier of high-yield (junk) bonds versus safer benchmarks; a widening or diverging spread here relative to broader high-yield debt is often an early credit-stress signal."},
    {"term": "Terminal value", "def": "The estimated value of a company's cash flows far into the future; Visser argues AI's pace of disruption makes this unknowable for many code-based businesses, which by itself compresses valuation multiples independent of near-term earnings."},
]
