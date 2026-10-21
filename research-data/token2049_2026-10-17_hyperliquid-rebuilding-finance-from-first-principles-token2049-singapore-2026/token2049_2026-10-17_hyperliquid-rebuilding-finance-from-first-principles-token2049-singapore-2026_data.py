META = {
    "title": "Hyperliquid: Rebuilding Finance from First Principles - TOKEN2049 Singapore 2026",
    "channel": "TOKEN2049",
    "speakers": "Jeff Yan, Hart Lambur",
    "date": "2026-10-17",
    "video_url": "https://www.youtube.com/watch?v=t5s7LICMJKE",
    "thread_line": "4 threads · HIP-3 real-world perps · why perps and HIP-4 outcomes · builder codes · regulation and agents",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Fireside between Hyperliquid founder Jeff Yan and Hart Lambur (founder of Across, a Hyperliquid-ecosystem project), a repeat of their 2025 talk.",
    "Hyperliquid is no longer just crypto perps: **HIP-3 real-world markets** were 51% of volume in July and 30-50% overall.",
    "Monthly volume is flat year on year while BTC and ETH are down 30-40%; USDC yield now adds revenue, first payment $15M (~$177M annualized).",
    "Perps framed as one canonical, non-expiring market per asset; HIP-4 outcomes add convex payoffs and could enable options.",
    "Builder codes let apps like Valr, MetaMask and Phantom plug in and charge fees with no negotiation; \"no one's competing with the internet\".",
    "Regulators moved fast: 42 SEC/CFTC letters or notices in a year; a permissioned HIP-3 variant is on testnet.",
    "Hart predicts regulated perps will be really big; Jeff declines to forecast beyond more on-chain upgrades of existing businesses.",
]

THEMES = [
    {
        "id": "hip3-rwa",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "Confirmed traction",
        "status": "HIP-3 LIVE SINCE LATE 2025",
        "title": "HIP-3 turned Hyperliquid from crypto perps into a real-world asset venue",
        "lead": "Builder-deployed markets for oil, equities and pre-IPO names now carry up to half of all volume.",
        "bullets": [
            "Monthly volume is about flat versus a year ago while Bitcoin and ETH prices fell 30-40%; HIP-3 markets are 30-50% of volume and **51%** in July.",
            "Trade XYZ was a standout deployer behind most of that July share; oil on weekends, 24/7 equities and pre-IPO perps are live.",
            "USDC held on Hyperliquid now earns yield for the protocol: first payment about $15M, annualizing to $177M; Jeff credits Coinbase and Circle stepping up and calls it a first of its kind.",
            "Traditional players are following: CME moving toward 24/7 markets, equities heading 24/7, and Robinhood and Kalshi launching perps.",
            "Team is still about 11-12 people, \"a little bigger\", hiring selectively; Jeff says revenue is a byproduct, the North Star is building new things.",
        ],
        "quote": {"text": "the gimmick here is not a gimmick", "cite": "— Hart Lambur"},
        "watch": "Hart Lambur's Across is part of the Hyperliquid ecosystem; Jeff Yan is the protocol's founder.",
        "names": [
            {"name": "Hyperliquid (HYPE)", "blurb": "HIP-3 markets 51% of volume in July; USDC yield ~$177M annualized", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Coinbase (COIN)", "blurb": "Praised with Circle for stepping up on USDC for Hyperliquid", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Circle (CRCL)", "blurb": "Issuer of USDC; praised as the premier compliant stablecoin", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Robinhood (HOOD)", "blurb": "Launching perps, vertically integrated", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Kalshi", "blurb": "Launching perps, vertically integrated", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "CME Group (CME)", "blurb": "Moving toward 24/7 markets", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "perps-hip4",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "Framework",
        "status": "HIP-4 LAUNCHED MAY",
        "title": "Why perps work, and what HIP-4 outcome markets add",
        "lead": "One canonical market per asset concentrates liquidity; outcomes add the convexity perps lack.",
        "bullets": [
            "A perp never expires, so users make no contract or strike choice and market makers do not fragment liquidity; much of finance boils down to predicting one number.",
            "BitMEX is the shared origin story; last year they called equity perps a big deal and say they were right.",
            "Perps are not \"all you need\": a genuine need exists for convex payoffs (capped downside, higher upside probability).",
            "HIP-4 outcomes: binary or scalar, built on spot trading, fungible and tokenized, no liquidation; launched quietly in May.",
            "Combined with builder codes anyone can \"rent\" the ecosystem for a prediction market; Jeff sees HIP-4 as the primitive for options, with delta-one hedging and portfolio margin on the same protocol.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "BitMEX", "blurb": "Origin of the perp product both speakers recall", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "builder-codes",
        "tags": ["crypto", "software"],
        "color": "green",
        "badge": "Strategic bet",
        "status": "OPEN PROTOCOL VS VERTICAL STACK",
        "title": "Builder codes: Hyperliquid as a Unix-style layer instead of a competitor",
        "lead": "Apps charge fees on their own flow while Hyperliquid handles the order book and clearing.",
        "bullets": [
            "Two visions: a vertically integrated fintech stack (Robinhood, Kalshi) versus composable primitives like Unix or Lego.",
            "Front ends already plugged in: Valr, MetaMask, Phantom, FOMO; Valr was a first-of-its-kind integration despite being a possible competitor.",
            "Builders keep their users and distribution; nobody wants to write an order book or clearing logic again.",
            "Hart: no global financial brand has ever existed, so local trusted brands like Valr in South Africa can sit on a global layer.",
            "Jeff admits a trust component and \"a long way to go\".",
        ],
        "quote": {"text": "No one's competing with the internet, right?", "cite": "— Jeff Yan"},
        "watch": "The \"Valor\" in the captions is the South African exchange Valr.",
        "names": [
            {"name": "Valr", "blurb": "South African exchange, first-of-kind integration", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "regulation-agents",
        "tags": ["policy", "crypto"],
        "color": "amber",
        "badge": "Forward look",
        "status": "PREDICTIONS FOR 2027",
        "title": "Regulation moves fast, permissioned markets arrive, agents wait on on-chain money",
        "lead": "Hart bets on regulated perps; Jeff stays vague on predictions.",
        "bullets": [
            "42 letters or notices from the SEC or CFTC in a year relevant to DeFi and perps, against a decade for the Bitcoin ETF.",
            "HIP-3 permissioned variant is on testnet, opt-in for deployers; liquidity can coexist with international markets.",
            "Hart predicts regulated perps will be really big, driven by institutions adopting the perp structure rather than US access alone.",
            "Jeff: agents are already superhuman in places and the real blocker is that money is not on-chain; \"people overthink the AI thing\".",
            "Jeff's own forecast: more on-chain upgrades of existing businesses, framed as \"crazy that happened in 1 year\".",
        ],
        "quote": None,
        "watch": "Regulatory strategy was explicitly not discussed.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Crypto", "title": "Track HIP-3 share of Hyperliquid volume as the real-world asset adoption gauge."},
    {"icon": "\U0001F4B5", "tag": "Crypto", "title": "Follow USDC yield payments as a new protocol revenue line."},
    {"icon": "\U0001F9F1", "tag": "Markets", "title": "Watch builder-code integrations by wallets and local exchanges."},
    {"icon": "⚖️", "tag": "Policy", "title": "Watch SEC and CFTC output and the permissioned HIP-3 testnet."},
    {"icon": "\U0001F3AF", "tag": "Markets", "title": "Expect HIP-4 outcomes to become the base for options."},
]

HOT_TAKES = [
    {"take": "No one's competing with the internet", "cite": "— Jeff Yan", "why": "positioning claim"},
    {"take": "my prediction is that regulated perps are going to be really big", "cite": "— Hart Lambur", "why": "dated-ish call"},
    {"take": "I predict that we will have trouble predicting what the thing is.", "cite": "— Jeff Yan", "why": "anti-prediction"},
]

CLAIMS = [
    {"who": "Hart Lambur", "claim": "Regulated perps will be really big, driven by institutional adoption", "metric": "regulated perps", "target": "really big", "by": "2027", "condition": None, "entity": "Hyperliquid (HYPE)"},
    {"who": "Jeff Yan", "claim": "More existing businesses will upgrade onto Hyperliquid within a year", "metric": "on-chain adoption", "target": "more", "by": "2027", "condition": None, "entity": "Hyperliquid (HYPE)"},
]

RELATIONS = [
    {"from": "Hyperliquid (HYPE)", "rel": "partners_with", "to": "Circle (CRCL)", "note": "USDC yield to the protocol"},
    {"from": "Hyperliquid (HYPE)", "rel": "partners_with", "to": "Coinbase (COIN)", "note": "USDC yield to the protocol"},
    {"from": "Valr", "rel": "partners_with", "to": "Hyperliquid (HYPE)", "note": "builder-code integration"},
    {"from": "MetaMask", "rel": "partners_with", "to": "Hyperliquid (HYPE)", "note": "builder-code integration"},
    {"from": "Phantom", "rel": "partners_with", "to": "Hyperliquid (HYPE)", "note": "builder-code integration"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: BitMEX, Trade XYZ, Coinbase and Circle; no outside publications named.", "tag": "References"},
]

GLOSSARY = [
    {"term": "HIP-3", "def": "Hyperliquid Improvement Proposal letting builders deploy their own perp markets, including real-world assets."},
    {"term": "HIP-4", "def": "Proposal for outcome (binary or scalar) markets on Hyperliquid's order book."},
    {"term": "Builder codes", "def": "Protocol-level fees apps can charge on flow routed through Hyperliquid."},
    {"term": "Convexity", "def": "A non-linear payoff, such as a capped downside or higher odds of upside."},
]
