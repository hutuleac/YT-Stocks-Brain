"""Jordi Visser — "A Bear Market Inside a Bull Market" (2026-09-27)"""

META = {
    "title": "A Bear Market Inside a Bull Market",
    "channel": "Jordi Visser",
    "speakers": "Jordi Visser",
    "date": "2026-09-27",
    "video_url": "https://www.youtube.com/watch?v=LhuSxhCNa5g",
    "thread_line": "6 threads · rate-fear facts vs. the story, consumer agents as the next AI moment, "
                    "multiple compression inside the bull market, crypto/tokenization as the bridge, "
                    "the generational time mismatch, and AI-driven science acceleration",
    "category": "market",
}

SNAPSHOT = [
    "Rates are the market's recurring scare story, but Visser says the *data* (credit spreads, "
    "jobless claims, profit margins, money-market flows, the LEI) shows no rate-driven damage yet.",
    "Meta's **Muse** consumer-agent launch is 'the number one thing of the market this week' — "
    "stock up 14% Monday, benchmarks jumping every 3 weeks since Zuckerberg's July admission AI "
    "progress had stalled.",
    "His thesis: a *bare market inside a bull market* — AI and tokenization are deflationary, "
    "compressing multiples across Mag 7 and SaaS names (Salesforce, Visa, Mastercard) even as "
    "indices make new highs.",
    "Crypto/tokenization is 'the bridge' connecting AI agents to money — his 46-name tokenized "
    "index is up 31% month-to-date vs. Bitcoin's 6.5%, with 96% of names above their 50-day average.",
    "Generational time mismatch: only 2.2% of people aged 55-64 (his own bracket, and the typical "
    "macro-pundit bracket) use AI regularly — he argues that disqualifies most rate-bear commentary.",
    "Science/research acceleration this week: a Claude-discovered enzyme system compared to CRISPR, "
    "an OpenAI research-acceleration blog on coding-agent usage, and a Dwarkesh interview on agent swarms.",
    "Trade stance: long speed, short friction — favor AI-native/infrastructure names, short "
    "rate-sensitive laggards (housing, private credit, private equity) and legacy payment names.",
]

THEMES = [
    {
        "id": "rate-fear-vs-facts",
        "tags": ["macro-rates"],
        "color": "green",
        "badge": "Data-backed contrarian view",
        "status": "ONGOING — Visser has held this stance since the 2022 rate-hike cycle",
        "title": "Rate panic is a story; the data says otherwise",
        "lead": "Visser lays out five hard indicators that would flash trouble if rates were actually breaking the economy — none of them are.",
        "bullets": [
            "**Credit spreads** (Moody's BA yield vs. 10-year) aren't widening the way they did in 2000 — a real rate problem shows up here first.",
            "Jobless claims aren't rising; companies aren't firing en masse, which is his pre-crisis tell.",
            "Profit margins are still climbing in a near-parabolic move, not mean-reverting the way they did before 2007.",
            "Money-market fund flows over the last 3 months look like a *panic* pattern historically, not a top — cash is flush, not fleeing.",
            "The Leading Economic Index (LEI) just turned positive after years negative — every other instance of that preceded a recession that didn't come this time.",
            "Housing/autos/retail are trading at bear-market levels because of rates, but the S&P PE was *below 10* in 1980 vs. today's multiples — he's watching for multiple compression, not a crash.",
        ],
        "quote": {"text": "If year-over-year S&P goes negative, I'll change my mind.", "cite": "— Jordi Visser"},
        "watch": "Visser flags his own hedge condition explicitly — this is a standing thesis, not a guarantee, and he says he'll reverse if S&P 500 YoY turns negative.",
        "names": None,
    },
    {
        "id": "muse-consumer-agents",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction — the next AI moment",
        "status": "LAUNCHED — Meta Muse, week of Sept 22, 2026",
        "title": "Consumer agents just arrived — Muse is 'the app store moment' for AI",
        "lead": "Meta's Muse launch, three weeks after Zuckerberg admitted AI progress had stalled, is what Visser calls the driver of the next 12 months.",
        "bullets": [
            "Zuckerberg said in **July 2026** that AI development \"hasn't accelerated in the way we expected\" — 6-10 weeks later Muse launched after rapid 1.1 → 1.2 → 1.3 model releases.",
            "Meta stock was **up 14%** the Monday after launch, pulling Intel and AMD up with it on the same recognition trade.",
            "Muse partners with **PayPal, Expedia, Shopify, Instacart, and Coinbase** — Visser has given it his cards, bank accounts, and used it for DMV work and a Verizon FiOS cancellation.",
            "Same week: Opus 5.5, GPT-6 Soul, and Luna all released with lower prices and fewer mistakes — \"the model fire hose is wide open.\"",
            "Visser is separately testing **Jev**, a decision-engine model (not another chat LLM) for agentic trading.",
            "His agentic-infrastructure thematic basket is **up 46%** through Friday vs. the Mag 7's +10% — he expects infrastructure/compute to keep outperforming even as he stays negative on where Mag 7/SaaS multiples end up.",
        ],
        "quote": {"text": "I believe there will be no consumers. The consumers will be Muse.", "cite": "— Jordi Visser"},
        "watch": "Visser cites Leopold Aschenbrener's 2027 recursive-self-improvement timeline and notes Andrej Karpathy called agents \"a decade away\" as recently as October 2025 — he flags this as a pattern of the field underestimating its own speed, not a settled call.",
        "names": [
            {"name": "Meta (META)", "blurb": "Muse consumer-agent launch drove a 14% stock pop and pulled Intel/AMD up with it.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "next 12 months"},
            {"name": "Intel (INTC), AMD", "blurb": "Rallied alongside Meta on the Muse-driven consumer-agent recognition trade.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "PayPal, Expedia, Shopify, Instacart", "blurb": "Muse launch partners.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Salesforce (CRM)", "blurb": "Down 10% year-to-date despite a rally; Visser expects continued multiple compression from AI/agent competition.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "multiple-compression",
        "tags": ["macro-rates", "software", "semis"],
        "color": "amber",
        "badge": "Structural critique",
        "status": "ONGOING — IWM/QQQ divergence at new lows since the iPhone era",
        "title": "The bare market inside the bull market: AI is deflationary, and multiples are compressing",
        "lead": "Even mega-caps making new highs face multiple compression as AI and tokenization drive hyper-competition and falling prices.",
        "bullets": [
            "IWM (small caps) vs. QQQ has made new lows since the iPhone launched in 2007 — Russell 2000 names still carry debt and are rate-sensitive; the Mag 7 aren't.",
            "Nvidia trades around **15x** next year's earnings vs. Cisco's ~100x PE at the dot-com peak — Visser argues this is the opposite of a bubble: the market is pricing AI *destroying* competitors' value within five years, and that window is shortening.",
            "Visa and Mastercard were the names brought up to him most this week — he sees a coming \"knife fight\" on their PE as agents route around card-brand attachment entirely.",
            "Micron already went through severe multiple compression — Visser expects the Mag 7 and software broadly to follow the same path as competition (OpenAI, Anthropic, each other) drives prices down.",
            "His read on the historical parallel: 1980's S&P 500 PE was below 10 — multiple compression, not a crash, is the normal outcome when rates stay elevated.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Trading near 15x forward earnings — cited as evidence this isn't a dot-com-style bubble.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Visa (V), Mastercard (MA)", "blurb": "Most-asked-about names this week; Visser expects PE compression as agents disintermediate card-based payments.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Micron (MU)", "blurb": "Already went through multiple compression to very low levels — the pattern Visser expects Mag 7/software to repeat.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "crypto-tokenization-bridge",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "ACCELERATING — 46-name tokenized index up 31% month-to-date",
        "title": "Tokenization is the bridge between AI agents and money",
        "lead": "Visser calls this a Peter Lynch-style early bull market — AI agents are finally the catalyst that gets humans' trillions into crypto rails built over 15 years.",
        "bullets": [
            "His 46-name tokenized crypto index is up **31%** month-to-date (+3% Friday alone) vs. Bitcoin's **+6.5%** — 44 of 46 names above their 50-day average (96%), 87% above the 200-day.",
            "BlackRock published a paper on the \"machine-native economy\" this week — arguing machine transactions need purpose-built agentic payment protocols — and is putting model portfolios on-chain via **Ondo Finance**, giving non-US investors 24/7 wallet access.",
            "Stripe is central to the agentic-payments thesis — Visser says it's part of the same package as the AI trade, not separate from it.",
            "Robinhood (via Vlad Tenev) says tokenization will take over the entire financial system; Robinhood teased new stock-token developments this week, and NYSE partnered with blockchain.com on tokenization.",
            "Coinbase is already integrated into Muse for trading — Visser calls this proof the crypto \"rails\" are set up and waiting for agent-driven demand.",
            "Agents have no brand attachment to Visa, Mastercard, or subscriptions the way humans do — that's the mechanism Visser expects to disintermediate legacy payment rails.",
        ],
        "quote": {"text": "Crypto to me is at the beginning of a Peter Lynch style bull market.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Up 6.5% this month — Visser says Bitcoin itself isn't the thing to watch; the broader tokenized index is.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "BlackRock (BLK)", "blurb": "Published the 'machine-native economy' paper and is tokenizing model portfolios on-chain via Ondo Finance.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Ondo Finance", "blurb": "Tokenization rail BlackRock is using for on-chain model portfolios; part of Visser's 46-name basket.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Robinhood (HOOD)", "blurb": "Vlad Tenev says tokenization will take over the entire financial system; teased new stock-token products.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Coinbase (COIN)", "blurb": "Already integrated into Meta's Muse for agent-driven crypto trading.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Stripe", "blurb": "Central to the agentic-payments infrastructure thesis, per Visser's crypto video this week.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "generational-time-mismatch",
        "tags": ["macro-rates", "mindset", "career"],
        "color": "gray",
        "badge": "Structural critique",
        "status": "ONGOING",
        "title": "The generational time mismatch: why most macro takes are stuck in linear time",
        "lead": "Visser argues the people warning about rates are disproportionately over 55 and don't use AI, so they're modeling a world that no longer exists.",
        "bullets": [
            "Only **2.2%** of people aged 55-64 — his own bracket, and the typical bracket for macro pundits interviewed on podcasts — use AI regularly, by his account.",
            "He frames this via Alvin Toffler's *Future Shock*: when change is too fast, people get angry and resist rather than adapt.",
            "Entrepreneurship is booming specifically because AI-native startups don't need debt or capital the way prior-generation businesses did — rates don't hurt them.",
            "His trading stance follows from this: \"long speed, short friction\" — go short housing, private credit, and private-equity names still trading down (e.g., Blue Owl), since those are the debt-dependent laggards rates are designed to flush out.",
            "He was in DC this week presenting to Freedom Tech on this exact theme — linear vs. exponential thinking as a fork in how people read markets.",
        ],
        "quote": {"text": "Rates are a way to get rid of the weak, and that's what's going to happen.", "cite": "— Jordi Visser"},
        "watch": None,
        "names": [
            {"name": "Blue Owl (OWL)", "blurb": "Down again this week, approaching lows — cited as a private-credit short candidate in the rate-flush-out thesis.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "ai-science-acceleration",
        "tags": ["biotech", "ai-infra"],
        "color": "green",
        "badge": "Confirmed events",
        "status": "THIS WEEK — Sept 22-26, 2026",
        "title": "AI is accelerating hard science, not just chat and coding",
        "lead": "Visser highlights a week of concrete science breakthroughs as evidence AI progress is compounding across research, not just consumer products.",
        "bullets": [
            "Anthropic's Claude reportedly discovered a previously unknown enzyme system in DNA with a structure compared to CRISPR — Fang Zhang (a leading CRISPR-era gene-editing researcher) commented publicly on it, which is why Visser takes it seriously.",
            "McKinsey published new research on AI-enabled drug discovery, citing an accelerated discovery-cycle time; Visser flags Insilico Medicine and its Eli Lilly relationship as a name to watch here.",
            "OpenAI published a blog on research acceleration, showing near-parabolic internal growth in coding-agent usage.",
            "A Dwarkesh Patel interview with an OpenAI researcher (Noam Brown) covered multi-agent systems and an incident where researchers underestimated how capable the AI actually was — Visser's takeaway is that the lesson was about human underestimation, not agents acting unsupervised.",
            "Blackstone's John Gray gave detailed numbers on AI adoption across Blackstone's private portfolio companies: spend up 21% year-over-year, with productivity gains already showing in margins, earnings, lease processing, and code repair.",
        ],
        "quote": None,
        "watch": "The specific AI-agent 'incident' Visser references from the Dwarkesh interview is described only in passing in the transcript and its details are unclear — treat as a pointer to go watch the source interview, not a verified account of what happened.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Track credit spreads (OAS) and jobless claims, not headline rates, for the real contagion signal."},
    {"icon": "\U0001F916", "tag": "AI/Agents", "title": "Watch consumer-agent adoption numbers (Muse downloads, token usage) as the next earnings catalyst, not just Mag 7 headlines."},
    {"icon": "\U0001FA99", "tag": "Crypto", "title": "Size crypto exposure to the broader tokenization basket, not just Bitcoin — breadth (96% above 50-day) is the tell."},
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Expect multiple compression, not a crash, in Mag 7/SaaS/payments names as AI competition turns deflationary."},
    {"icon": "\U0001F52A", "tag": "Markets", "title": "Short debt-dependent laggards (housing, private credit, private equity) — rates are designed to flush them out."},
    {"icon": "\U0001F9EC", "tag": "Health", "title": "Watch AI-driven drug-discovery names (Insilico Medicine, Eli Lilly partnerships) as a slower-burn agentic theme."},
]

HOT_TAKES = [
    {"take": "How can you have a view on today's economy and on today's market if you don't use AI? I don't think it's possible.", "cite": "— Jordi Visser", "why": "direct dismissal of most macro commentary by age/AI-usage"},
    {"take": "This is not a bubble. This is the opposite.", "cite": "— Jordi Visser", "why": "contrarian call on AI valuations vs. dot-com comparison"},
    {"take": "I believe there will be no consumers. The consumers will be Muse.", "cite": "— Jordi Visser", "why": "sweeping prediction on agent-mediated commerce"},
    {"take": "Rates don't hurt them. Let me say that again. Rates don't hurt them.", "cite": "— Jordi Visser", "why": "contrarian claim that AI-native startups are immune to the rate cycle"},
    {"take": "If you're someone managing money and you are not fully in the know of compute, of agents, of swarms, of the crypto guardrails... I don't think you can compete. I really don't.", "cite": "— Jordi Visser", "why": "puts his own professional peers on the hook"},
    {"take": "Crypto to me is at the beginning of a Peter Lynch style bull market.", "cite": "— Jordi Visser", "why": "specific, checkable framing of where crypto sits in a cycle"},
]

CLAIMS = [
    {"who": "Jordi Visser", "claim": "Will reverse his no-recession/no-rate-crisis stance if S&P 500 goes negative year-over-year", "metric": "S&P 500 YoY", "target": "negative", "by": None, "condition": "if S&P 500 YoY turns negative", "entity": None},
    {"who": "Jordi Visser", "claim": "His agentic-infrastructure thematic portfolio is up 46% through Friday vs. the Mag 7's +10%", "metric": "portfolio return", "target": "+46% vs +10%", "by": "week of Sept 26, 2026", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Salesforce.com is down 10% year-to-date despite recent rallies", "metric": "stock return YTD", "target": "-10%", "by": "Sept 2026", "condition": None, "entity": "Salesforce (CRM)"},
    {"who": "Jordi Visser", "claim": "His 46-name tokenized crypto index is up 31% month-to-date, with 96% of names above their 50-day moving average", "metric": "index return / breadth", "target": "+31% MTD, 96% above 50-day", "by": "Sept 26, 2026", "condition": None, "entity": None},
    {"who": "Leopold Aschenbrenner", "claim": "AI reaches the point of effective recursive self-improvement", "metric": "recursive self-improvement", "target": "achieved", "by": "2027", "condition": None, "entity": None},
    {"who": "Blackstone (John Gray)", "claim": "Blackstone portfolio companies increased AI-related spending year-over-year", "metric": "AI spending growth", "target": "+21%", "by": "Sept 2025 to Sept 2026", "condition": None, "entity": None},
    {"who": "Jordi Visser", "claim": "Will speak at a crypto/tokenization industry event", "metric": None, "target": None, "by": "October 27, 2026", "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Meta (META)", "rel": "partners_with", "to": "PayPal, Expedia, Shopify, Instacart", "note": "Muse consumer-agent launch integrations"},
    {"from": "Meta (META)", "rel": "partners_with", "to": "Coinbase (COIN)", "note": "Muse can trade on Coinbase"},
    {"from": "Meta (META)", "rel": "competes_with", "to": "Amazon (AMZN)", "note": "reported standoff over Muse"},
    {"from": "BlackRock (BLK)", "rel": "partners_with", "to": "Ondo Finance", "note": "tokenizing BlackRock model portfolios on-chain"},
    {"from": "New York Stock Exchange", "rel": "partners_with", "to": "blockchain.com", "note": "tokenization initiative announced this week"},
]

OTHER_NEWS = [
    {"icon": "\U0001F1FA\U0001F1F8", "title": "Visser presented on the linear-vs-exponential 'time mismatch' theme to the Freedom Tech community in DC this week, and lists a run of upcoming appearances: the Bitcoin Treasury Conference, a Pompliano event, and a bridge/tokenization industry event on October 27.", "tag": "Events"},
    {"icon": "\U0001F4FA", "title": "Sources referenced this episode: Blackstone's John Gray on AI adoption across portfolio companies; a Dwarkesh Patel interview with OpenAI's Noam Brown on multi-agent systems; Vlad Tenev (Robinhood) on the Moonshots podcast; Ali Yahya (a16z) on the Unchained podcast; an a16z panel with Chris Dixon and Ali Yahya on AI-and-crypto.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Ghost rails", "def": "Visser's term for the crypto/blockchain infrastructure built over the last 15 years ahead of real demand — now waiting for AI agents to actually use it."},
    {"term": "Tokenization", "def": "Converting ownership of assets (equities, model portfolios, real-world assets) into on-chain tokens that can be transacted 24/7 via crypto wallets."},
    {"term": "Recursive self-improvement", "def": "The point where an AI model's own output meaningfully accelerates the development of its next version — a threshold Leopold Aschenbrenner projected for 2027."},
    {"term": "OAS (option-adjusted spread)", "def": "The extra yield high-yield credit pays over Treasuries after adjusting for embedded options — a widening OAS is Visser's preferred real-time signal of credit stress."},
    {"term": "Multiple compression", "def": "A stock's price/earnings ratio falling even as earnings grow, because the market prices in shrinking future competitive advantage or higher discount rates."},
    {"term": "Machine-native economy", "def": "BlackRock's term for an economy where AI agents transact directly with each other via purpose-built payment protocols, rather than routing through human-facing financial rails."},
]
