META = {
    "title": "AI Productivity Is Real. 83% of Stocks Are 10% Off Highs. Why Does Barry Ritholtz Like Bonds Again?",
    "channel": "Excess Returns",
    "speakers": "Barry Ritholtz (Ritholtz Wealth Management), Dave Nadig, Matt Zeigler (host)",
    "date": "2026-10-13",
    "video_url": "https://www.youtube.com/watch?v=WwGqcY0-_78",
    "thread_line": "6 threads · AI gives no alpha · narrow breadth and a $5.2T IPO wall · AI-buildout bonds and obsolete data centers · AI inside an advisory firm · dynamic pricing arms race · Ritholtz loves bonds",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Three-way panel: AI made advisers and analysts faster, but **nobody has turned it into alpha** — AI stock-picking ETFs are 'meh'.",
    "Ritholtz: at all-time highs, 83% of S&P 500 stocks were 10% off 52-week highs in Q3 and 42% were 20% off — narrowing breadth is a warning, not a bear call.",
    "If SpaceX, Anthropic and OpenAI list at discussed valuations, the three total $5.2T vs $4.1T for every US tech IPO from 1980-2025.",
    "Nadig's worry is a **K-shaped capital market**: mega AI IPOs and their valuations soak up capital and become collateral and index anchors.",
    "A-rated AI data-center bonds yield more than Treasuries; Ritholtz doubts giant data centers survive 10-20 years of Moore's law.",
    "Inside Ritholtz Wealth, Enterprise Claude on a data lake turned a weeks-long six-person rebalance screen into a same-day answer.",
    "Consumers vs retailers is an AI arms race: dynamic pricing at Walmart, Uber and McDonald's drive-thrus, and Meta's Muse agent as a data play.",
    "Ritholtz: 'I love bonds' — munis at a 8-8.5% tax-equivalent yield in high-tax states; first time this century bonds are attractive.",
]

THEMES = [
    {
        "id": "no-ai-alpha",
        "tags": ["finance", "software"],
        "color": "gray",
        "badge": "Contested",
        "status": "EVERYONE GOT THE SAME TOOLS",
        "title": "AI made analysts faster, not smarter than the market",
        "lead": "Nadig says the LLM-replaces-analysts hype of three years ago produced no black-box funds that win.",
        "bullets": [
            "Everyone uses it for the obvious jobs — summarizing prospectuses and 10-Ks — so any edge evens out fast, as it did with high-frequency trading and ML trade sizing.",
            "The packaged attempts (an Amplify AI stock-picking ETF and a second AI-picks issuer) have a 'pretty meh' record: winning windows, then stock pickers and indexers beat them.",
            "Real AI alpha, if it exists, will sit inside a **Jim Simons-style hedge fund** and be known only after the fact.",
            "Ritholtz cites JPMorgan's head of fixed income Bob Michele (~$1 trillion in assets) telling interns AI is what spreadsheets were for his generation.",
        ],
        "quote": {"text": "You're not going to be replaced by AI. You're going to be replaced by someone who uses AI better than you do.", "cite": "— Barry Ritholtz"},
        "watch": None,
        "names": [
            {"name": "JPMorgan (JPM)", "blurb": "Fixed-income head Bob Michele's AI-for-interns speech", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "breadth-ipo-wall",
        "tags": ["finance", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "S&P 500 AT ALL-TIME HIGHS, Q3 2026",
        "title": "Breadth is narrowing while a $5.2T AI IPO wall arrives",
        "lead": "Ritholtz shrugs at Mag 7 concentration but flags breadth; Nadig fears the IPO wave starves everything that isn't AI.",
        "bullets": [
            "Ritholtz: 'nothing's more bullish than all-time highs', and the Mag 7 earned their weight through 891 acquisitions in 20 years — any one could be split into 10-20 S&P companies.",
            "But in Q3, 83% of S&P 500 stocks were 10% below 52-week highs and 42% were 20% below — a warning, not the end of the bull market.",
            "Ritholtz: back out AI capex and data-center spending and the economy is slightly contracting.",
            "Zeigler: passive investing plus the AI trade now does the capital allocation; ~two-thirds of profits and capex flow to AI (citing Michael Cembalest's 'Smothering Heights').",
            "SpaceX is already public; if Anthropic (~$2T) and OpenAI (~$1.2T) list at discussed valuations, the three total **$5.2T** vs $4.1T for all US tech IPOs 1980-2025 (not inflation-adjusted).",
            "Nadig: those valuations become collateral and anchor huge indexes; non-AI firms can't show 100% forward growth and get starved — a K-shaped capital market.",
        ],
        "quote": {"text": "going public at a trillion dollars is still bonkers", "cite": "— Barry Ritholtz"},
        "watch": "Ritholtz concedes the $2T and $1.2T figures may be wildly wrong — 'maybe it's half'.",
        "names": [
            {"name": "SpaceX (SPCX)", "blurb": "Already public; 'who will be left holding the bag'", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Anthropic", "blurb": "~$2T discussed IPO valuation", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "OpenAI", "blurb": "~$1.2T discussed IPO valuation", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "ai-bonds-obsolescence",
        "tags": ["ai-infra", "macro-rates"],
        "color": "red",
        "badge": "Speculative",
        "status": "AI BUILDOUT DEBT SCALING",
        "title": "A-rated AI buildout bonds may be financing tomorrow's empty warehouses",
        "lead": "Ritholtz questions whether trillions of AI data-center debt deserves its rating if efficiency shrinks the need for the buildings.",
        "bullets": [
            "Among drivers of higher yields: Japanese bonds paying yield for the first time in decades, plus a flood of AI data-center bonds.",
            "These are 'theoretically A-rated' corporates yielding much more than Treasuries; the buildout scales from ~$0.5T to $4-7T depending on who you believe.",
            "Moore's law argument: in 10-20 years nobody needs a seven-football-field data center — someone owns a warehouse and uses 5-10% of it.",
            "Nadig: markets underrate efficiency gains — a recent inference approach was 'orders of magnitude more efficient', and such shifts are deflationary.",
        ],
        "quote": {"text": "is that really A-rated? Are people reaching for yield", "cite": "— Barry Ritholtz"},
        "watch": None,
        "names": None,
    },
    {
        "id": "ai-in-the-practice",
        "tags": ["finance", "dev-workflow"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "LIVE AT RITHOLTZ WEALTH",
        "title": "Inside an advisory firm: a data lake plus Claude turned weeks into a day",
        "lead": "The panel's productivity gains are real, and the most human one is remembering clients' lives.",
        "bullets": [
            "Ritholtz Wealth built a data lake from Schwab, Fidelity, Orion and Salesforce, queried with **Enterprise Claude**.",
            "One screen: households off target allocation by 3/5/10%, over 60 or retiring within 5 years, $10M+, worried about capital gains — weeks for six people manually, answered the same day.",
            "Context: rebalancing studies by Meb Faber (Cambria), Corey Hoffstein and Wes Gray (Alpha Architect); direct indexing used to harvest losses.",
            "Zeigler: podcast-side productivity 2-3x; advisory work 30-40%; the step change is tools talking to each other, slowed by compliance — expected within a year.",
            "Both: AI-pulled meeting notes surface life events (a kid's MCATs, a trip to France) so the whole team shows up informed; Ritholtz pairs the rebalance with a Ben Carlson client note.",
            "Nadig is skeptical of AI that critiques adviser-client conversations; respects Shaping Wealth (Brian Portnoy), wary of weekend vibe-coded tools.",
            "Clients now bring AI-assisted questions (e.g. Treasury vs regular money market in a high-tax state — a couple of basis points).",
        ],
        "quote": {"text": "finally the future that Star Trek promised is here", "cite": "— Barry Ritholtz"},
        "watch": "Ritholtz runs the firm he's describing and hosts a podcast promoting its work.",
        "names": [
            {"name": "Anthropic", "blurb": "Claude is Ritholtz's main tool; ChatGPT is 'the B team'", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Charles Schwab (SCHW)", "blurb": "Data source for the firm's data lake", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "pricing-arms-race",
        "tags": ["consumer", "policy"],
        "color": "red",
        "badge": "Contested",
        "status": "EARLY LAWSUITS AND STATE ACTION",
        "title": "AI agents vs dynamic pricing: a consumer-retailer arms race",
        "lead": "Agents like Meta's Muse could shop for you, but the panel says retailers and platforms hold the power — and the data.",
        "bullets": [
            "Zeigler: a data analyst priced a CPI-style grocery basket by zip code through Kroger's public API via Claude — Meta Muse could build and order the cart.",
            "Ritholtz (from Lindsay Owens's book): **Walmart** prices mayonnaise higher if tuna is already in your cart.",
            "Uber quoted $200, a Lyft black car $130 — same car, same driver; McDonald's drive-thrus read plates and price by zip code.",
            "Sam Rines (now WisdomTree) has tracked 'price over volume' since 2020-21; shrinkflation and dynamic pricing are a quarter to a third of price increases, per Ritholtz.",
            "Nadig: consumers are 'coming completely unarmed'; Amazon already blocks agents from scraping or buying.",
            "Trust: Ritholtz trusts Apple on privacy, Google 'mostly non-evil', Meta not at all — Muse data will be sold to advertisers.",
            "Populist backlash is coming (Mamdani, AOC); hamburger meat is $20/lb at his butcher, a meatloaf $53 — scarcity pricing fits a Rolex or Porsche GT3, not mac and cheese.",
        ],
        "quote": {"text": "I think consumers are coming completely unarmed", "cite": "— Dave Nadig"},
        "watch": None,
        "names": [
            {"name": "Meta (META)", "blurb": "Muse agent; ad model makes it the wrong steward of shopping data", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Walmart (WMT)", "blurb": "Cart-aware dynamic pricing", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Uber (UBER)", "blurb": "$200 vs Lyft's $130 for the same ride", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "McDonald's (MCD)", "blurb": "License-plate zip-code pricing", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "Blocks shopping agents to keep power", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Trusted on privacy", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Kroger", "blurb": "Public price API", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ritholtz-bonds",
        "tags": ["macro-rates", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "FIRST TIME THIS CENTURY",
        "title": "Ritholtz: 'I love bonds' — paid to wait for the first time in 25 years",
        "lead": "An equity guy says investment-grade bonds now compete with stocks on after-tax yield.",
        "bullets": [
            "The 10-year over 5% has been rare for 25 years; munis at 4.5-4.75% equal an **8-8.5% tax-equivalent yield** in high-tax coastal states.",
            "Approach: SMAs owning the bonds directly, 5-7 year duration, A-rated — ignore volatility and collect par at maturity.",
            "TIPS suit people on fixed incomes wanting a known inflation hedge; high-grade corporates yes, junk no.",
            "Avoid 'wacky circular AI-funded stuff' that looks like Microsoft but is an SPV in the background.",
            "Not calling the end of equities or the bottom in bonds; his secular-bull policy had refused stock-to-bond rebalancing 'until now'.",
            "Zeigler is excited too but still light on bonds — 'equities forever', for now.",
        ],
        "quote": {"text": "This is the first time this century bonds are attractive.", "cite": "— Barry Ritholtz"},
        "watch": "End-of-show disclaimer: securities discussed may be held by the hosts' firms or clients.",
        "names": [
            {"name": "Microsoft (MSFT)", "blurb": "AI SPV debt that only looks like Microsoft credit", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Track breadth (share of S&P stocks 10-20% off highs), not Mag 7 weight"},
    {"icon": "\U0001F3E6", "tag": "Fixed income", "title": "Price munis on tax-equivalent yield and hold to maturity in an SMA"},
    {"icon": "⚠️", "tag": "Credit", "title": "Read the issuer behind AI data-center debt — an SPV is not the hyperscaler"},
    {"icon": "\U0001F9F0", "tag": "Advisory", "title": "Pool custodian, CRM and portfolio data in one place before layering AI on it"},
    {"icon": "\U0001F6D2", "tag": "Consumer", "title": "Compare apps on every ride or order — dynamic pricing punishes loyalty"},
]

HOT_TAKES = [
    {"take": "I love bonds. I've never been able to say that in public before.", "cite": "— Barry Ritholtz", "why": "equity guy turning to bonds"},
    {"take": "back out AI capex and and data center spending and the economy is slightly contracting", "cite": "— Barry Ritholtz", "why": "macro claim"},
    {"take": "I just can't imagine that 20 years from now or even 10 years from now, we need a seven football fieldsiz data center", "cite": "— Barry Ritholtz", "why": "bearish on data-center longevity"},
    {"take": "I think mostly that is a failed experiment", "cite": "— Dave Nadig", "why": "dismisses AI stock-picking funds"},
    {"take": "If you think Claude or Perplexity or Chad or anything is just a substitute for Google, well, congratulations. You're in kindergarten.", "cite": "— Barry Ritholtz", "why": "dismissive of transactional AI use"},
    {"take": "this is like a K-shaped K-shaped capital markets problem alongside the K-shaped income problem", "cite": "— Dave Nadig", "why": "structural warning"},
]

CLAIMS = [
    {"who": "Barry Ritholtz", "claim": "SpaceX, Anthropic and OpenAI would total $5.2T at discussed valuations, above all US tech IPOs 1980-2025 combined", "metric": "combined market cap at IPO", "target": "$5.2T", "by": None, "condition": "if Anthropic and OpenAI list at currently discussed valuations", "entity": None},
    {"who": "Barry Ritholtz", "claim": "Giant data centers will be largely unneeded within 10-20 years as chips get more efficient", "metric": "data-center capacity needed", "target": "5-10% of today's builds", "by": "10-20 years", "condition": None, "entity": None},
    {"who": "Barry Ritholtz", "claim": "AI buildout financing scales from about half a trillion to $4-7 trillion", "metric": "AI buildout spending", "target": "$4-7T", "by": None, "condition": None, "entity": None},
    {"who": "Matt Zeigler", "claim": "Wealth-management tools start talking to each other, a step-function productivity gain", "metric": "advisory tool integration", "target": "step change", "by": "within a year", "condition": None, "entity": None},
    {"who": "Barry Ritholtz", "claim": "5-7 year A-rated bonds held to maturity deliver par plus 8-8.5% tax-equivalent muni yields in high-tax states", "metric": "tax-equivalent muni yield", "target": "8-8.5%", "by": None, "condition": "high-tax state, held to maturity", "entity": None},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "⚾", "title": "Nadig's Claude hacks: pre-filled baseball scorecards from an MLB feed, and a Sonos tie-in that mutes the TV between innings — built in three prompts.", "tag": "AI tools"},
    {"icon": "\U0001F52D", "title": "Ritholtz built a Drake-equation dashboard with sliders, then an 'inverse Drake' to disconfirm his own Rare Earth thesis (galactic center radiation, binary stars, metal-poor outer arms, supernovae).", "tag": "AI tools"},
    {"icon": "\U0001F4DD", "title": "Ritholtz has Claude fill forms (Canada's R105, New York's MV102), format podcast transcripts after Descript, and organize his daily '10 things to read' from Instapaper — hours down to five minutes.", "tag": "Workflow"},
    {"icon": "\U0001F4E7", "title": "His reply to off-target podcast PR pitches is an AI prompt to research Masters in Business guests; he hears back rarely — except from managers of ~$900B-scale firms (about 30 firms run $1T+).", "tag": "Workflow"},
    {"icon": "\U0001F3B2", "title": "Nadig's line between automation and fun: a 7-year FinTwit D&D campaign's transcripts are searchable, but he won't let AI min-max his character. 'Imagination gap' is the real AI divide.", "tag": "Culture"},
    {"icon": "\U0001F697", "title": "Ritholtz avoids AI on Bring a Trailer and Chrono24 for fear of new rabbit holes; recalls bidding $500K on a ~$2M Mercedes 300 SL and on a Singer 911.", "tag": "Collectibles"},
]

OTHER_NEWS += [
    {"icon": "\U0001F393", "title": "Zeigler's ideas: build an MCP server over podcast transcripts, and use Claude to recruit Yale/Harvard MBA interns for tool-building (competing with McKinsey and GSAM).", "tag": "AI tools"},
    {"icon": "\U0001F941", "title": "Zeigler researches music rabbit holes in Perplexity projects (drummers vs the Linn drum machine, 1979-84; Mellencamp's 'Jack and Diane'); his wife calls him 'gainfully unemployed'. He also turns family vacation photos into AI Star Wars and mutant scenes.", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "Market breadth", "def": "How many stocks participate in a rally; narrow breadth means few names carry the index."},
    {"term": "K-shaped", "def": "A split where one group (big AI firms, high earners) pulls away while the rest stagnates."},
    {"term": "Tax-equivalent yield", "def": "The taxable yield a tax-free muni matches after your federal and state tax rate."},
    {"term": "SMA", "def": "Separately managed account where you own individual bonds and can hold them to par."},
    {"term": "Dynamic pricing", "def": "Prices that change by person, basket, location or moment, set by algorithm."},
    {"term": "Price over volume", "def": "Firms keeping prices high and accepting lower unit sales, relying on affluent buyers."},
]
