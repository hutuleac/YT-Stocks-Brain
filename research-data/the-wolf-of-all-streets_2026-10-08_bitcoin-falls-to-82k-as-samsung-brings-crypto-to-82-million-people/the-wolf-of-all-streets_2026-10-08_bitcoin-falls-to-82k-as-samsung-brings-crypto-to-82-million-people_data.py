META = {
    "title": "Bitcoin Falls To $82K As Samsung Brings Crypto To 82 Million People",
    "channel": "The Wolf Of All Streets",
    "speakers": "Scott Melker (host), Nick Ducoff (Solana Foundation)",
    "date": "2026-10-08",
    "video_url": "https://www.youtube.com/watch?v=_b0irsUgnIA",
    "thread_line": "4 threads · Samsung USDC on Solana · tokenized equities for US investors · bank adoption and chain consolidation · Bitcoin retest of $82K",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Bitcoin slipped to **$82K** (below $83K) as an Ethereum Foundation researcher's \"bunker mode\" call on AI-accelerated classical hacks divided crypto.",
    "**Samsung** is integrating USDC for cross-border remittances to 82M Galaxy users in 60+ countries from late October; the crypto layer is invisible to the user.",
    "**Securitize** is launching tokenized US stock trading for US investors on Solana, per the Wall Street Journal; ~95% of tokenized equity volume already runs on Solana.",
    "Solana Foundation's Nick Ducoff says 7 of 29 global systemically important banks build on Solana and expects half within a year.",
    "Both speakers expect layer-2 and private-chain consolidation; Ducoff argues settlement ends up on public rails.",
    "Scott Melker reads the Bitcoin weekly chart as a healthy retest of broken resistance; a dip to the 50 MA near $77K would not worry him, and he calls himself a buyer.",
    "Prediction markets price a return to $100K at 8% before Nov 2026, 22% before Dec 2026 and 32% by Jan 2027.",
]

THEMES = [
    {
        "id": "samsung-usdc",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "LIVE LATE OCTOBER 2026",
        "title": "Samsung puts USDC remittances inside the wallet of 82M Galaxy users",
        "lead": "Stablecoin adoption is arriving as invisible plumbing, not as a crypto app people have to learn.",
        "bullets": [
            "Eligible Galaxy users can send **USDC** abroad, or local-currency payouts to bank accounts, in 60+ countries from late October.",
            "Users see only a Samsung wallet; USDC and Solana stay abstracted away, which Melker calls the long-boring-path fix for the UX problem.",
            "Before this, Solana had 13M stablecoin holders and about $15B of stablecoins in circulation.",
            "Ducoff's ceiling: roughly 2B Samsung device holders worldwide.",
            "Cross-border is \"the killer use case\"; he cites splitting a bill across USD, GBP, EUR and JPY accounts, and Venmo's PYUSD support on Solana.",
            "Western Union and MoneyGram have already built on Solana (one further remitter name is garbled in the captions).",
            "Meme coins as onboarding: the Trump memecoin drop led MoonPay to KYC 3M investors in a day.",
        ],
        "quote": {"text": "Memecoins proved the technology.", "cite": "— Nick Ducoff"},
        "watch": "Ducoff leads the Solana Foundation, so every claim about Solana's share and fit comes from the ecosystem's own promoter.",
        "names": [
            {"name": "Samsung", "blurb": "Integrating USDC remittances into Samsung Wallet for 82M Galaxy users", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "late Oct 2026"},
            {"name": "Circle (CRCL)", "blurb": "USDC is the stablecoin Samsung is using", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Solana (SOL)", "blurb": "Rail Samsung's flow settles on; the Foundation's guest frames it as most-used chain", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "PayPal (PYPL)", "blurb": "Venmo supports PYUSD on Solana", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Western Union (WU)", "blurb": "Built on Solana for remittances", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "MoonPay", "blurb": "KYC'd 3M investors in one day for the Trump memecoin", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "tokenized-equities",
        "tags": ["crypto", "finance", "policy"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "WSJ REPORT OCT 8, 2026",
        "title": "Securitize brings tokenized US stocks to US investors on Solana",
        "lead": "The first retail-facing test of tokenized equities for US holders, and Solana already carries most of the volume.",
        "bullets": [
            "Per the Wall Street Journal, Securitize will offer tokenized trading for a dozen or so equities: the FANG stocks and big AI hyperscalers.",
            "Users KYC on Securitize's site, then connect a wallet or use Securitize's own; prior tokenized equities mostly served non-US holders.",
            "The stocks are planned to trade on the tokenized stock venue (TSV) NYSE is launching with OKX.",
            "The SEC granted the \"innovation exemption\" a couple of weeks ago; Melker notes it is not yet a formal rule, but players are acting as if it will be.",
            "About 95% of tokenized-equity volume is on Solana, with roughly $700M of tokenized equity supply and $4.3B of real-world assets (about $1B at start of year).",
            "Melker cites 1.2M holders (all-time high), with 775K joining in September alone.",
            "Four models are emerging: the wrapper model (permissionless), Securitize as regulated transfer agent (Computershare partnership), the TSV with OKX and ICE, and DTC's entitlement model in street name.",
            "ADR premium example: about 30% on SK Hynix in the US; Ducoff wants tokenization to \"collapse\" that fee capture.",
        ],
        "quote": None,
        "watch": "The 95% volume share and holder counts are the Solana Foundation's and Melker's figures, not independent data.",
        "names": [
            {"name": "Securitize", "blurb": "Launching US-investor tokenized stock trading on Solana; transfer-agent model", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Intercontinental Exchange (ICE)", "blurb": "NYSE parent; part of the TSV with OKX", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OKX", "blurb": "Partner in the NYSE tokenized stock venue", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "DTCC", "blurb": "Entitlement model, settling on tokenized rails", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Charles Schwab (SCHW)", "blurb": "Seen as the next likely entrant once Securitize proves the model", "stance": "WATCHING", "conviction": "Low", "horizon": None},
            {"name": "Computershare", "blurb": "Announced partnership with Securitize", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "banks-consolidation",
        "tags": ["crypto", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "BREAKPOINT LONDON NOV 16-17, 2026",
        "title": "Banks adopt Solana while consortium chains and layer 2s fight for relevance",
        "lead": "Ducoff says institutions are converging on public rails; Melker agrees the chain count shrinks.",
        "bullets": [
            "Ducoff: **7 of 29** global systemically important banks build on Solana, expected to be half within a year.",
            "Named work: Morgan Stanley has a SOL ETF and E*Trade buy/sell/hold; JPMorgan issued Galaxy commercial paper bought by Franklin Templeton and Coinbase, plus a DvP settlement program.",
            "Also: Citi published a trade-finance pilot paper; Societe Generale has a euro stablecoin; State Street a money fund; Standard Chartered custody; BNY custody, stablecoin mint/burn and fund administration.",
            "Competing efforts Melker lists: a big-bank stablecoin consortium, a regional-bank \"bank chain\", OpenUSD from a Stripe-led fintech consortium, and Circle's Arc and Tempo.",
            "Ducoff's counter: OUSD launched on Solana with the deepest liquidity; Securitize's private chain Converge and Abstract's token now scale on or around Solana.",
            "Pudgy Penguins' owner shut down its Abstract chain after tens of millions in losses; Melker takes it as the layer-2 narrative dying outside corporate-sponsored chains.",
            "Ducoff: Vitalik abandoning the L2 roadmap pressured those networks; the 2021 fear of too little block space flipped into overbuilding.",
            "On DTCC settling on tokenized rails, Melker relays a Securitize executive's view that it is just a plumbing upgrade in a closed garden.",
        ],
        "quote": {"text": "the Solana Foundation is still very committed to the original vision... a global state machine where there can be a single venue where all liquidity can be and all users can be.", "cite": "— Nick Ducoff"},
        "watch": "Ducoff leads the Solana Foundation and the bank list is his own summary.",
        "names": [
            {"name": "JPMorgan (JPM)", "blurb": "Commercial paper on Solana and a DvP settlement program", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Morgan Stanley (MS)", "blurb": "SOL ETF and E*Trade buy/sell/hold", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Citi (C)", "blurb": "Trade-finance pilot white paper on Solana", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Societe Generale", "blurb": "Euro stablecoin on Solana", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "State Street (STT)", "blurb": "Money fund on Solana", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Standard Chartered", "blurb": "Custody for Solana", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "BNY (BK)", "blurb": "Custody, stablecoin mint/burn, fund administration", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Stripe", "blurb": "Leads the OpenUSD fintech consortium", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Ethereum (ETH)", "blurb": "Vitalik dropped the L2 roadmap", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "bitcoin-retest",
        "tags": ["crypto", "macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "BTC UNDER $82K ON OCT 8, 2026",
        "title": "Bitcoin dips to $82K: a healthy retest, and Melker is buying",
        "lead": "Melker reads the pullback as a retest of broken resistance, not a new bear leg.",
        "bullets": [
            "Weekly chart: lower highs and lows from the ~$126-127K high, then a break above ~$82.8K and a retest of it last week.",
            "Price now trades slightly below that level; in the prior bear market, the same pattern dipped below the line several times before rising.",
            "A move down to the **50 MA near $77K** would not surprise him; \"once you make that higher high... dips are for buying.\"",
            "He says Arch Public was buying again and had sold right at $88K.",
            "Prediction markets: $100K before Nov 2026 8%, before Dec 2026 22%, by Jan 2027 32%; he thinks sentiment is too negative.",
            "Ducoff: hyperscalers drained liquidity from crypto; the dollar-debasement trade then pushed rates up, after which crypto caught a bid.",
            "Melker's cycle worry: he called the four-year cycle dead last October and now wonders if it is about to cycle up.",
            "Coindesk: Justin Drake's \"bunker mode\" call says AI could enable classical hacks before quantum; Ducoff only says Solana has strong quantum resistance and core devs track it.",
        ],
        "quote": {"text": "Nothing's better marketing than higher prices.", "cite": "— Scott Melker"},
        "watch": "Melker declares himself a Bitcoin buyer; Ducoff's \"bear market since January\" framing comes from a Solana promoter.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Retest of ~$82K; 50 MA near $77K", "stance": "BUYING-ADDING", "conviction": "High", "horizon": None},
            {"name": "Solana (SOL)", "blurb": "Ducoff: Solana ETPs launched in the US last November; Bitwise product has over $1B AUM", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Bitwise", "blurb": "Solana ETP with over $1B AUM, gathered in a bear market", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4F1", "tag": "Crypto", "title": "Watch Samsung's late-October USDC launch as the first mass-market test of invisible stablecoin rails."},
    {"icon": "\U0001F4C8", "tag": "Tokenization", "title": "Track Securitize's US launch and the NYSE/OKX tokenized venue for signs of Schwab or E*Trade following."},
    {"icon": "\U0001F3E6", "tag": "Banks", "title": "Count bank announcements at Breakpoint London (Nov 16-17) against the 7-of-29 baseline."},
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Mark $82.8K and the 77K 50 MA as the levels that decide whether the retest holds."},
    {"icon": "\U0001F9F1", "tag": "Crypto", "title": "Treat new layer-2s and consortium chains skeptically; consolidation is the stated base case."},
]

HOT_TAKES = [
    {"take": "Memecoins proved the technology.", "cite": "— Nick Ducoff", "why": "Defends meme coins as the proof of scale"},
    {"take": "I think that Solana will be a winner regardless.", "cite": "— Nick Ducoff", "why": "Says Solana wins whichever tokenized-equity model prevails"},
    {"take": "Seven of the 29 globally systemically important banks are building on Solana, and I expect half within a year.", "cite": "— Nick Ducoff", "why": "Numeric prediction"},
    {"take": "Anything old that doesn't have a robust team and security budget is basically just going to get hacked and drained to zero or disappear.", "cite": "— Scott Melker", "why": "Strong claim on legacy chains"},
    {"take": "I am a Bitcoin buyer right now.", "cite": "— Scott Melker", "why": "Explicit position on a dip"},
    {"take": "I don't think that's going to be DTCC chain, personally.", "cite": "— Scott Melker", "why": "Dismisses the incumbent settlement chain"},
]

CLAIMS = [
    {"who": "Nick Ducoff", "claim": "Half of the 29 global systemically important banks will be building on Solana within a year.", "metric": "GSIBs building on Solana", "target": "about half (from 7 of 29)", "by": "2027-10", "condition": None, "entity": "Solana (SOL)"},
    {"who": "Nick Ducoff", "claim": "Samsung's USDC cross-border remittance launch goes live in 60+ countries.", "metric": "Samsung USDC remittances", "target": "launch in 60+ countries", "by": "2026-10", "condition": None, "entity": "Samsung"},
    {"who": "Nick Ducoff", "claim": "Real-world assets on Solana keep growing about 4x per year from $4.3B.", "metric": "RWA on Solana", "target": "4x annual growth", "by": None, "condition": "at the current rate", "entity": "Solana (SOL)"},
    {"who": "Nick Ducoff", "claim": "The Solana Breakpoint conference in London draws a similar crowd to last year's 7,000 attendees from 100+ countries and carries big announcements.", "metric": "Breakpoint attendees", "target": "about 7,000", "by": "2026-11-16", "condition": None, "entity": "Solana (SOL)"},
    {"who": "Scott Melker", "claim": "A pullback to the 50-day moving average near $77K would not change the bullish structure.", "metric": "BTC 50 MA", "target": "$77K", "by": None, "condition": "if Bitcoin keeps retesting $82.8K", "entity": "Bitcoin (BTC)"},
    {"who": "Prediction markets (cited by Scott Melker)", "claim": "Bitcoin crosses $100K again before Nov 2026 at 8%, before Dec 2026 at 22%, before Jan 2027 at 32%.", "metric": "BTC crosses $100K", "target": "8% / 22% / 32%", "by": "2027-01", "condition": None, "entity": "Bitcoin (BTC)"},
]

RELATIONS = [
    {"from": "Samsung", "rel": "partners_with", "to": "Circle (CRCL)", "note": "USDC remittances in Samsung Wallet"},
    {"from": "Securitize", "rel": "partners_with", "to": "OKX", "note": "Stocks planned for NYSE/OKX tokenized venue"},
    {"from": "Securitize", "rel": "partners_with", "to": "Computershare", "note": "Announced partnership"},
    {"from": "Western Union (WU)", "rel": "customer_of", "to": "Solana (SOL)", "note": "Remittances built on Solana"},
]

OTHER_NEWS = [
    {"icon": "\U0001F6A8", "title": "Ethereum Foundation researcher Justin Drake's \"bunker mode\" call: AI could enable classical hacks on crypto before quantum is a threat (Coindesk).", "tag": "Security"},
    {"icon": "\U0001F3AF", "title": "Upcoming guests: Matt Hogan, Peter Schiff (Melker says gold bugs agree with Bitcoiners on 99% but differ on the asset) and Hunter Biden.", "tag": "Media"},
    {"icon": "\U0001F3BE", "title": "Bar hedged on a Knicks championship with prediction markets and offered free beer; Ducoff's example of blockchain as an innovation lab.", "tag": "Prediction markets"},
    {"icon": "\U0001F4DA", "title": "Sources cited: Coindesk, Wall Street Journal, Securitize's Carlos (from Consensus), Ducoff's Maslow-style pyramid for blockchains.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Tokenization super cycle", "def": "Ducoff's term for assets such as equities and the dollar moving onto blockchains at scale."},
    {"term": "TSV", "def": "Tokenized stock venue that NYSE is launching with OKX."},
    {"term": "Innovation exemption", "def": "SEC relief permitting tokenized equities, granted weeks ago but not yet a formal rule."},
    {"term": "SPL tokens", "def": "Solana's token program, used to hold and trade tokenized equities and real-world assets."},
    {"term": "DvP", "def": "Delivery versus payment, a settlement structure JPMorgan is running on Solana."},
    {"term": "ADR premium", "def": "Extra cost US investors pay for foreign shares via ADRs, cited at about 30% on SK Hynix."},
]
