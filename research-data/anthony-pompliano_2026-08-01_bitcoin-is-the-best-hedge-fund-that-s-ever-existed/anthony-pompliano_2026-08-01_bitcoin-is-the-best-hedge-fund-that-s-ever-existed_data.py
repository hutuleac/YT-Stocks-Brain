"""Data file for Jordi Visser x Anthony Pompliano — Bitcoin Is The Best Hedge Fund That's Ever Existed."""

META = {
    "title": "Bitcoin Is The Best Hedge Fund That's Ever Existed",
    "channel": "Anthony Pompliano",
    "speakers": "Jordi Visser (guest, macro/portfolio manager), interviewed by Anthony Pompliano (host)",
    "date": "2026-08-01",
    "video_url": "https://www.youtube.com/watch?v=03S1ECNLBnA",
    "thread_line": "5 threads · the Leopold Aschenbrenner hedge-fund unwind as a leverage 'cleansing event,' the compute-scarcity case for why OpenAI and Anthropic 'gobble' rather than lend out compute, Warsh's Fed doing nothing on purpose, Bitcoin as the best hedge fund that's ever existed, and Visser's scarcity-investing playbook (Micron, GE Vernova, gold) for a world of AI-driven multiple compression.",
    "category": "market",
}

SNAPSHOT = [
    "Jordi Visser reads the Leopold Aschenbrenner hedge-fund forced-liquidation (down from +400%/$25B to reportedly ~$10B) as a leverage 'cleansing event' comparable to LTCM, the 2007 quant unwind, and Archegos — not evidence the AI thesis is broken, and he doesn't believe rumors that Citadel's Fed-hike leak was intentional.",
    "South Korea's market fell 45% in ~40 days (still up 56% YTD) with 1.2M leveraged retail accounts margin-called, and Japan lost ~$200B in a single day — Visser reads both as leverage/positioning stories layered on the same AI mid-cycle deceleration he's flagged before, not a US-contagion signal.",
    "Citing a widely-discussed contrarian piece (attributed to Dwarkesh Patel, echoed by Gavin Baker), Visser argues OpenAI and Anthropic are compute 'gobblers' who will control more of AI than people think — because finite compute goes to whoever pays most per token (his Disney-buys-all-the-compute analogy) — while xAI and Meta can afford to sell excess capacity since they don't need it yet.",
    "Warsh's Fed held rates by doing nothing and giving no forward guidance, which Visser reads as a deliberate delevering of the Fed's own balance sheet (paired with tokenization unlocking dormant asset value) rather than a hawkish or dovish signal.",
    "Central thesis: Bitcoin is 'the best hedge fund that's ever existed' and the only real store of value left as AI's deflationary pressure and 'multiple compression' erode every public company's terminal value over the next 5 years — he frames Michael Saylor/MicroStrategy's 2021 pivot as the template every business will eventually face.",
    "His portfolio response is 'scarcity investing': more Micron (bought the dip again), GE Vernova, Bitcoin, and gold as a secondary store of value — plus Ethereum and an eight-vertical, 40-name crypto basket he says is outperforming Bitcoin as agentic/stablecoin adoption accelerates.",
    "Explicitly flags his own knowledge gaps: hasn't researched BitTensor enough to have a view yet, and is still forming an opinion on how migration/remittances/border-erosion (prompted by Anthony's question about migrant flows into Spain) connects to the crypto/tokenization story.",
]

THEMES = [
    {
        "id": "leopold-cleansing-event",
        "tags": ["finance", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — more liquidations expected into early August",
        "title": "Leopold Aschenbrenner's Forced Unwind Was a Leverage 'Cleansing Event,' Not a Broken Thesis",
        "lead": "**Visser, who lived through LTCM, the 2007 quant unwind, and Archegos, reads the Leopold Aschenbrenner blowup the same way:** crowded leveraged positioning forced a liquidation once prime brokers saw the exposure and started hedging — the AI mid-cycle slowdown was the trigger, not the cause.",
        "bullets": [
            "Reportedly up ~400% through June with ~$25B in the fund he started 2-3 years ago, Leopold's fund gave back a large share of gains (widely reported near 70-80%) in a four-day move that intensified in the two hours after the Fed decision — Visser says he's still up roughly 80% year-to-date.",
            "Visser doesn't believe (and says nobody will ever confirm) the theory that Citadel intentionally leaked a surprise-rate-hike story to force Leopold's hand — points out the market-implied hike probability was already close to 40% independent of any leak.",
            "July saw a 'record factor unwind' as narratives cycled weekly (Anthropic in trouble, hyperscalers in trouble, open-source threat) even though nothing fundamental changed — same pattern as Liberation Day's 20% drawdown with no change to earnings or the economy.",
            "Structural read: hedge fund gross leverage hit an all-time high this year (Goldman Sachs called it the largest 5-month increase in gross exposure on record) at the same time terminal value (the ability to value a company 3 years out) was falling — a mismatch he says guarantees more 'speed crashes,' not fewer.",
            "Expects prime brokers to extend less leverage going forward given quarterly-liquidity hedge funds can't exit AI-adjacent positions fast enough when momentum unwinds — predicts multiple compression in indices and more Leopold-style blowups within individual funds, not a return to prior leverage levels.",
            "On his own trading: bought more Micron into this specific weakness (a second purchase after an initial nibble two weeks earlier), and plans a 'Combing Through the Carnage' report naming which AI names technically held up versus broke down.",
        ],
        "quote": {"text": "This was a cleansing event in my opinion. It doesn't mean that we're not going to see continued volatility.", "cite": "— Jordi Visser"},
        "watch": "Visser explicitly says nobody will ever know whether Citadel's rate-hike commentary was coincidental or targeted — he treats the conspiracy theory as unconfirmable, not as fact.",
        "names": [
            {"name": "Micron (MU)", "blurb": "Bought further into this week's weakness after an initial small purchase two weeks earlier — a second, deliberate add on the dip.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "compute-gobblers",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — compute scarcity thesis, not yet fully proven in ARR",
        "title": "OpenAI and Anthropic Are Compute 'Gobblers,' Not Lenders — and That's the Bull Case",
        "lead": "**A contrarian piece Visser cites approvingly (attributed to Dwarkesh Patel, echoed by investor Gavin Baker) argues finite compute concentrates power with whoever can pay the most per token** — which favors OpenAI and Anthropic over hyperscalers currently willing to lend out spare capacity.",
        "bullets": [
            "Disney thought experiment: if compute is scarce enough that a single buyer could corner it, a studio able to make a $3B movie for $50M in tokens would happily outbid everyone else for that capacity given its ticket-pricing power — the same logic Visser says explains Micron's unprecedented memory margins right now.",
            "Amazon, Microsoft, and Google's combined contracted compute backlog is 'nearing $2 trillion'; adding Oracle pushes the total over $2 trillion — all four said on earnings calls that CapEx is matched to existing orders, and none of them cut CapEx this quarter.",
            "Sam Altman, in an interview with Patrick O'Shaughnessy, admitted OpenAI — the most aggressive spender in the space — 'underestimated the amount of supply' needed; Visser says Dario Amodei is now 'scrambling to find compute from anywhere' after warning last year that OpenAI was overspending.",
            "Explains why xAI and Meta can afford to sell excess compute (to Anthropic and to Google's cloud arm, respectively) while OpenAI and Anthropic cannot: xAI doesn't need its full buildout yet (humanoids, full self-driving come later) and Meta's current need is smaller than what it's already built for personal agents.",
            "Frames the current bottleneck as barely first-inning: coding agents are the only mature use case so far — voice-native personal agents (a working Siri or Alexa) require hardware and on-device memory that doesn't exist yet, which is why he says supply won't catch demand for a long time.",
            "Direct rebuttal to overbuilt-capacity skeptics: 'every single smart person that's involved with building this stuff and seeing the demand is saying they can't keep up with it' — contrasts this with investor emails claiming the industry has already overbuilt.",
        ],
        "quote": {"text": "Compute scarcity is a reality, and I don't care what anyone says about all the CDS on the hyperscalers and all of this.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Anthropic", "blurb": "Framed as a compute 'gobbler' advantaged by scarcity, though Dario Amodei is described as actively scrambling for more capacity.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "Raised $80 billion and bought excess compute capacity from SpaceX despite being a major cloud provider without enough of its own.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "warsh-does-nothing",
        "tags": ["macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — rate cuts + balance-sheet runoff conditional on inflation/labor data",
        "title": "Warsh 'Stole the Show by Doing Nothing' — a Deliberate Delevering of the Fed's Own Balance Sheet",
        "lead": "**Visser reads the Fed's no-hike, no-forward-guidance decision as intentional structural reform**, not indecision — the market had already tightened on its own (10-year and 2-year yields both rose), so the Fed didn't need to act.",
        "bullets": [
            "Argues Warsh is right that old academic models built on stale, revisable government data can't keep pace with an economy where AI compresses years of change into months — market pricing had ~40% odds of a hike going into the meeting with no pre-released guidance, which Visser expects adds more volatility going forward, not less.",
            "Connects this to hedge fund leverage: the Fed itself was a source of system-wide leverage via QE (growing its balance sheet whenever assets fell); Warsh wants the opposite — a smaller, less-levered Fed balance sheet.",
            "Ties the delevering to tokenization: Visser believes Warsh and Treasury Secretary Bessent both see tokenization unlocking money supply from dormant assets (via fractionalized, tradeable ownership), which lets the Fed shrink its role without tightening conditions.",
            "On the K-shaped economy: attributes it partly to two decades of Fed balance-sheet expansion since the financial crisis; expects balance-sheet runoff plus eventual rate cuts (once inflation and labor data cooperate) to help redistribute wealth rather than worsen the K-shape.",
            "Notes hyperscaler credit-default-swap spreads widening is not a red flag in his view — it reflects unprecedented capital-market tapping (citing Google's $80B raise) that takes time to digest, on 'the best balance sheets in the world,' not distress.",
        ],
        "quote": {"text": "I actually like what Kevin Warsh is doing. I believe using old academic models is going to be a problem.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": None,
    },
    {
        "id": "bitcoin-best-hedge-fund",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "OWNS — Bitcoin, gold, Ethereum, 40-name crypto basket",
        "title": "Bitcoin Is 'The Best Hedge Fund That's Ever Existed' — the Scarcity Trade for a World of Multiple Compression",
        "lead": "**Visser's central 5-year thesis:** AI's deflationary pressure will eventually compress the terminal value of every public company and business idea, which is why he's rotating into things that can't be out-competed — Bitcoin, gold, and physical scarcity (Micron, GE Vernova).",
        "bullets": [
            "Compares Bitcoin's own drawdown history (giving back 70-80% of early gains, then continuing to compound) directly to Leopold's trajectory, arguing Bitcoin's return profile is what kept 'famous investors' from ever backing it — those return patterns don't happen, until eventually the market starts pricing in the asset anyway.",
            "Big-picture math: total global household net worth is roughly $700 trillion against a ~$3 trillion crypto market; his call is this total stays roughly flat while wealth redistributes, and crypto's share could reach ~$100 trillion within a decade as AI-native, low-headcount private businesses (his own company, Cursor, Anthropic, OpenAI as examples) capture more value that stays privately owned rather than needing to IPO.",
            "Frames Michael Saylor's 2021 MicroStrategy pivot as the template every business faces: he couldn't compete with Microsoft's scale (competitive disruption) or with zero interest rates (currency debasement), so he moved treasury into something non-disputable — Visser expects most businesses to face this same choice within 5 years as AI-native competitors proliferate.",
            "Names his scarcity basket explicitly: Bitcoin, gold (as a secondary store-of-value pick, chosen over other crypto because he can't be confident Ethereum, Solana, Sui, or BitTensor will still be relevant in 3 years), Micron, and GE Vernova — all things tied to physical constraints AI can't deflate away quickly.",
            "Ethereum is outperforming Bitcoin, which he reads as a signal the crypto ecosystem's 'network effects' (agentic volume, stablecoin adoption, Stripe's acquisition activity in payments) are kicking in; his 40-name, eight-vertical crypto basket is also outperforming Bitcoin on the same signal.",
            "Explicitly flags a research gap: he hasn't spent enough time on BitTensor (the most AI-crypto-overlapping asset) to have a real view yet, and is deliberately researching China's AI strategy (via an Ezra Klein interview with former Australian PM Kevin Rudd) before forming a stronger opinion on how geopolitics factors into his crypto allocation.",
        ],
        "quote": {"text": "You don't find Bitcoin, Bitcoin finds you. You don't find Bitcoin until you're either personally or your business has been so destructed that you can't get out of a hole.", "cite": "— Jordi Visser, quoting Michael Saylor"},
        "watch": "Visser is explicit that his BitTensor view isn't formed yet and that his crypto-share-of-wealth number ($100 trillion in a decade) is his own working framework, not a modeled forecast.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Central store-of-value holding; framed as the best hedge fund that's ever existed and the asset least exposed to AI-driven multiple compression.", "stance": "OWNS", "conviction": "High", "horizon": "5 years"},
            {"name": "Ethereum (ETH)", "blurb": "Outperforming Bitcoin; read as evidence agentic/stablecoin network effects are kicking in across his 40-name basket.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Gold", "blurb": "Chosen as his secondary store-of-value pick over other crypto assets given uncertainty about which altcoins survive 3 years out.", "stance": "OWNS", "conviction": "Medium", "horizon": "3 years"},
            {"name": "Micron (MU)", "blurb": "Core 'scarcity' holding tied to physical memory constraints AI can't deflate away quickly.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "GE Vernova (GEV)", "blurb": "Named alongside Micron as a physical-scarcity holding within his AI-infrastructure thesis.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "BitTensor", "blurb": "The most AI-crypto-overlapping asset on his radar, but he says he hasn't researched it enough yet to hold a real view.", "stance": "UNCERTAIN", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Read hedge-fund blowups like Leopold's as leverage-cleansing events, not thesis breaks, before assuming the underlying trade is dead."},
    {"icon": "\U0001F5A5️", "tag": "AI infra", "title": "Track hyperscaler contracted backlog (~$2T+) and public compute-lending signals (who's hoarding vs. selling capacity) as the real gauge of AI demand, not sentiment."},
    {"icon": "\U0001F3E6", "tag": "Macro", "title": "Treat Fed 'no action' meetings as potentially deliberate policy (balance-sheet delevering) rather than indecision — re-read the framing, not just the rate decision."},
    {"icon": "\U0001F4B0", "tag": "Crypto", "title": "Size Bitcoin and gold as the scarcity hedge against AI-driven multiple compression, distinct from higher-beta altcoin bets."},
    {"icon": "\U0001F50D", "tag": "Markets", "title": "Say 'not enough research yet' out loud (as Visser does on BitTensor) rather than forming a view before doing the work."},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "crypto's share of global household wealth over the next decade", "metric": "total crypto market value", "target": "~$100 trillion (from ~$3 trillion)", "by": "within a decade", "condition": "his own redistribution framework, assuming total household net worth (~$700T today) stays roughly flat", "entity": None},
    {"who": "Sam Altman (cited by Jordi Visser)", "claim": "OpenAI underestimated the compute supply it would need", "metric": "compute supply estimate", "target": None, "by": None, "condition": "admitted in an interview with Patrick O'Shaughnessy", "entity": "OpenAI"},
    {"who": "Jordi Visser", "claim": "hyperscaler contracted compute backlog", "metric": "contracted order value", "target": "~$2 trillion across Amazon, Microsoft, Google, plus Oracle pushing it over $2T", "by": None, "condition": None, "entity": None},
    {"who": "Leopold Aschenbrenner (cited by Jordi Visser)", "claim": "AGI arrival and government involvement timeline, from his 'Situational Awareness' paper", "metric": "AGI arrival", "target": None, "by": "2027", "condition": "Visser says events are tracking slightly ahead of this forecast", "entity": None},
]

RELATIONS = [
    {"from": "SpaceX", "rel": "supplies", "to": "Anthropic", "note": "Sold excess compute capacity it doesn't yet need for humanoids/FSD, per Jordi Visser"},
    {"from": "SpaceX", "rel": "supplies", "to": "Alphabet (GOOGL)", "note": "Sold excess compute capacity to Google's cloud arm despite Google being a major cloud provider itself, per Jordi Visser"},
]

HOT_TAKES = [
    {"take": "Bitcoin is the best hedge fund that's ever existed.", "cite": "— Jordi Visser", "why": "The episode's title claim — a direct, checkable comparison between Bitcoin's return/drawdown profile and history's most talked-about hedge fund run."},
    {"take": "Over the course of the next 5 years, AI will destroy all public companies — meaning it will destroy the growth certainty of all companies going forward.", "cite": "— Jordi Visser", "why": "A dated, sweeping structural call about every public company's terminal value, not just a sector view."},
    {"take": "Compute scarcity is a reality, and I don't care what anyone says about all the CDS on the hyperscalers.", "cite": "— Jordi Visser", "why": "A flat dismissal of a live bear-case data point (widening hyperscaler CDS spreads) that others read as a warning sign."},
    {"take": "I actually like what Kevin Warsh is doing. I believe using old academic models is going to be a problem.", "cite": "— Jordi Visser", "why": "An explicit endorsement of the Fed doing nothing, against a market that wanted a clearer signal."},
    {"take": "I don't know if Ethereum is safe [as a 3-year store of value]. I don't know if Solana is. I don't know if Sui is. I don't know if BitTensor is.", "cite": "— Jordi Visser", "why": "A notably candid admission of uncertainty about assets he otherwise actively covers and holds."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3A4", "title": "Sources referenced this episode: a contrarian compute-scarcity piece attributed to Dwarkesh Patel (echoed by investor Gavin Baker) anchors the 'gobblers vs. lenders' theme; Sam Altman's interview with Patrick O'Shaughnessy on Invest Like the Best; Ezra Klein's interview with former Australian PM Kevin Rudd on China's AI/socialism strategy; David Friedberg's 'molecules to bits' framing from the All-In podcast.", "tag": "Sources cited"},
    {"icon": "\U0001F30D", "title": "Prompted by footage of migrants arriving in Spain, Anthony and Jordi discussed how digitized money and AI-native, low-headcount businesses are eroding the economic reasons people historically had to migrate — cites Marco Papic's 2021 paper on the metaverse and border erosion as an early, largely-correct framework.", "tag": "Discussion"},
    {"icon": "\U0001F3AE", "title": "Visser cites Axie Infinity's real economic impact on the Philippines (a play-to-earn game that briefly reshaped household income there) as a preview of gaming/crypto economies with real financial stakes, alongside Fortnite as an already-normalized 'metaverse' behavior.", "tag": "Reference"},
]

GLOSSARY = [
    {"term": "Factor unwind", "def": "A rapid, broad-based reversal in stocks that share a common characteristic (e.g. high momentum, AI exposure) as leveraged funds holding similar positions are forced to sell at the same time."},
    {"term": "Terminal value", "def": "The estimated value of a company's cash flows far into the future; Visser argues AI is making this unknowable for most public companies, which should structurally compress valuation multiples even as near-term earnings grow."},
    {"term": "CDS (credit default swap) spread", "def": "The cost of insuring against a company's debt default; widening spreads on hyperscaler debt are read by bears as a distress signal, but by Visser as a byproduct of unprecedented capital-raise volume being digested by the market."},
    {"term": "Tokens per watt", "def": "A measure of AI compute efficiency — how much useful model output (tokens) a given unit of energy produces — cited as the metric that will matter most once compute becomes the binding constraint on AI economics."},
]
