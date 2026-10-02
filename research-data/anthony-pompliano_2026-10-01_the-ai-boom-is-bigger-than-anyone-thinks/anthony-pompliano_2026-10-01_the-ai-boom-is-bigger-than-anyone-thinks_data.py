META = {
    "title": "The AI Boom Is Bigger Than Anyone Thinks",
    "channel": "Anthony Pompliano",
    "speakers": "Anthony Pompliano, Dan Ives",
    "date": "2026-10-01",
    "video_url": "https://www.youtube.com/watch?v=YdoMzkcGH1Q",
    "thread_line": "5 threads · Ives's early-innings AI bull case · regulatory capture & the White House meeting · Pomp's bear case on private labs (sovereign AI) · where to allocate · IVAI fund",
    "category": "market",
}

SNAPSHOT = [
    "**Dan Ives** (Yorkville Ives) says AI is *less than 15%* through a **$4-5T** multi-year spend cycle, with a **$5-6** tech-wide multiplier per capex dollar.",
    "He reads the AI-safety calls for slowdown as **regulatory capture** (\"pull the ladder up\") and backs the White House all-hands: slowing down means China wins.",
    "Host **Pomp** is the contrarian: he thinks the private labs face a plateauing-revenue, falling-token-price squeeze as firms move to **sovereign / applied AI**.",
    "Pomp's own data point: routing queries to his own models on his own hardware cuts cost about **97%** and raises accuracy; Ives agrees sovereign AI is the bigger debate than model-lab share.",
    "Ives's allocation: own **chips, hyperscalers, software/cyber, then energy and infrastructure**; the \"SaaS apocalypse\" was a fictional narrative.",
    "Macro is bearish on paper (oil ~$105-110, 10-year ~5.2%) yet Ives says the market is pricing a fourth industrial revolution.",
    "Ives pitches his new **Ives Ultra Fund (IVAI)**: a public permanent-capital vehicle holding private AI companies.",
]

THEMES = [
    {
        "id": "early-innings",
        "tags": ["ai-infra", "semis"],
        "color": "green",
        "badge": "High conviction",
        "status": "IVES: THIRD INNING, MULTI-YEAR BULL MARKET",
        "title": "AI spend is less than 15% done and the trade is broadening",
        "lead": "Ives sees a multi-year tech bull market with equilibrium in chips not before late 2028 or early 2029.",
        "bullets": [
            "Last quarter's hyperscaler monetization (Microsoft named) was the *inflection point*; now it's about second, third and fourth derivatives.",
            "Spend trend: **$4-5 trillion** over the next 3-4 years, with **<15%** done; each capex dollar carries a **$5-6** multiplier across tech.",
            "His Asia checks show **13-to-1** chip demand-to-supply; he calls it the third inning, not sixth or seventh.",
            "Even if **10-15%** of data centers get voted down, he expects ~**800,000** data centers built in the next 12-18 months (\"the hearts and lungs of a new economy\").",
            "Trade is spreading from memory to Dell, Cisco, HP, then energy and infrastructure; Nvidia is \"way cheaper\" than 6-12 months ago.",
            "Only ~**4-5%** of US companies have gone down the AI path; another 60-70% of enterprises are still to come, plus Europe, India and the Middle East.",
            "Consumer side is just starting: Apple's install base (1.5B iPhones, 2.5B iOS devices) makes it a \"toll collector on the consumer AI highway\".",
        ],
        "quote": {"text": "We're less than 15% through what the spending trend's going to be the next 3 to 4 years. It's 4 to 5 trillion dollars.", "cite": "— Dan Ives"},
        "watch": "Ives runs the Ives Ultra Fund (IVAI) and is a long-time public tech-bull voice; his framing is a bullish thesis, not a neutral forecast.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Cheaper than 6-12 months ago; leader of physical AI wave; Jensen \"the adult in the room\".", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "2-3 years"},
            {"name": "AMD", "blurb": "Lisa Su is \"just starting\" on the chip side; you have to own chips.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Microsoft (MSFT), Amazon (AMZN), Alphabet (GOOGL)", "blurb": "Hyperscalers reinserting themselves on install base as AI adoption spreads.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Dell Technologies (DELL), Cisco (CSCO)", "blurb": "Infrastructure names where the AI trade is showing up.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Install base makes it a consumer AI toll collector; \"finally actually having AI\".", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "regulatory-capture",
        "tags": ["policy", "geopolitics"],
        "color": "amber",
        "badge": "Contested",
        "status": "WHITE HOUSE ALL-HANDS · MIDTERM CYCLE",
        "title": "Slowdown talk is regulatory capture, and slowing means China wins",
        "lead": "Both hosts distrust the labs' calls for regulation but disagree on who's leading and why.",
        "bullets": [
            "Ives: leaders of the \"F1 race\" (Anthropic, OpenAI) want to stop others catching up, i.e. *throwing sand in the gears*; \"you go to the top floor and then you pull the ladder up\".",
            "Pomp's framework: money-losing, negative-cash-flow labs call for slowdown; profitable Meta and Google don't. Funding via non-dilutive capital decides which side you're on.",
            "Ives disagrees that the labs only trail: he says Anthropic and OpenAI have a clear lead in pure models and enterprise, but the gap is narrowing vs Meta and Google.",
            "Ives credits Meta's Zuckerberg with ignoring the slowdown (his image: Ferrari in the left lane vs a minivan at 55 mph) and says the essay-driven weekend sell-off was a bear peak.",
            "Midterm logic: dystopian talk gets data centers shut down locally, and \"every data center that gets shut down, China wins\"; Ives wants self-regulation, not Beltway grandstanding.",
            "Ives credits Jensen Huang and Palantir's Alex Karp as the two who understand it best (global/sovereign view), with Jensen \"the calming force\".",
        ],
        "quote": {"text": "Every data center that gets shut down, China wins.", "cite": "— Dan Ives"},
        "watch": "Ives's \"Anthropic and OpenAI are leading\" view differs from Pomp's, who thinks the private labs are in more trouble than people realize.",
        "names": [
            {"name": "Meta (META)", "blurb": "Zuckerberg did not call for a slowdown; Ives says ~20% added to Meta's stock after the essay; Muse seen as positive for AI overall.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Palantir (PLTR)", "blurb": "Karp understands sovereign AI; Ives says Palantir could be a \"category changer\" as free cash flow ramps.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "private-lab-pressure",
        "tags": ["ai-infra", "software"],
        "color": "red",
        "badge": "Pomp's bear case",
        "status": "THE COUNTER-THESIS",
        "title": "Private labs face plateauing revenue, price war and sovereign AI",
        "lead": "Pomp argues the general-intelligence-for-everything premise is weakening: token price and consumption per customer are both falling.",
        "bullets": [
            "Pomp's model: **revenue = token price x consumption**; frontier-quality token prices are falling while per-customer consumption drops, so lab revenue \"has been plateauing\" (Anthropic in particular).",
            "His case study, Silvia: started 100% as a ChatGPT wrapper, moved to Claude (compute went from zero to **hundreds of thousands of dollars/month**), then built its own models and harness.",
            "Routing queries to its own models on its own hardware cuts cost about **97%**, and Silvia says it's more accurate on tax, mortgage and credit cards; \"six, seven, eight engineers beat a trillion dollar company\" on applied tasks.",
            "A new tool called Jev went from not on the chessboard to a reported **$100M run rate** in its first week; his engineers now route some queries to it where frontier models were cost-prohibitive. He calls it \"death by 1,000 cuts\".",
            "Pomp's caution: *a good product does not equal a good company*; he cites trends in the S-1 as headwinds (his words, not specified).",
            "Ives's counter: Anthropic and OpenAI built enterprise sales forces early and the consumer isn't where they monetize; the data layer, not the model, is the value chain.",
            "Ives sees sovereign AI as \"the golden goose\", the bigger debate than model-lab share; open source is needed for token cost (the 2007 iPhone-price analogy).",
        ],
        "quote": {"text": "A good product does not equal a good company.", "cite": "— Anthony Pompliano"},
        "watch": "Pomp runs Silvia, a company that benefits from sovereign/applied AI, and personally invests in data businesses; his data points are his own company's numbers.",
        "names": [
            {"name": "Anthropic", "blurb": "Ives: IPO \"shocked if it doesn't happen\" this year, after the midterms; Pomp: revenue plateau and customers consuming fewer tokens.", "stance": "UNCERTAIN", "conviction": "None", "horizon": "IPO before year-end / after midterms"},
            {"name": "OpenAI", "blurb": "Part of the private-lab duopoly framing; said it won't IPO this year per Pomp.", "stance": "UNCERTAIN", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "allocation",
        "tags": ["software", "finance", "robotics"],
        "color": "green",
        "badge": "Recommendation",
        "status": "PORTFOLIO FRAMING",
        "title": "How Ives allocates: own the core, rotate into what's next",
        "lead": "Own chips and hyperscalers, accept software and cyber rebounded from \"dead\", and look ahead to energy and physical AI.",
        "bullets": [
            "Allocation is by **second/third/fourth derivatives**; large-cap tech is \"starting to flex its muscles again\".",
            "\"The SaaS apocalypse\" was a fictional narrative: he points to Salesforce, ServiceNow and Palantir as proof.",
            "Cybersecurity was \"done\" in April (Anthropic eating its lunch); CrowdStrike, Palo Alto and Zscaler have since rebounded.",
            "Tesla: the transition from EV player to robotaxis/autonomy/Optimus is what to watch; \"once the transition has happened, you've already missed it\".",
            "Expect new stocks \"we're not talking about today\" in 18-24 months, especially in the consumer-agent category.",
            "Personal-agent market (Pomp notes the Grok box and others skip charging consumers): Ives calls it \"a whole 'nother area of investing\".",
            "Jobs: more jobs created than taken over the next decade in Ives's view; Pomp says his company has more agents than humans yet is hiring faster.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Salesforce (CRM), ServiceNow (NOW)", "blurb": "Cited as proof the SaaS-apocalypse narrative was wrong.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "CrowdStrike (CRWD), Palo Alto Networks (PANW), Zscaler (ZS)", "blurb": "Cyber stocks that rebounded after the April \"Anthropic is eating their lunch\" fear.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Tesla (TSLA)", "blurb": "Watch the EV-to-robotaxi/Optimus transition before it's priced in.", "stance": "WATCHING", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "macro-vs-ai",
        "tags": ["macro-rates", "energy"],
        "color": "amber",
        "badge": "Contested",
        "status": "OIL ~$105-110 · 10-YR ~5.2-5.3%",
        "title": "A bearish macro backdrop the market is looking through",
        "lead": "Pomp lists every headwind; Ives says the market is pricing a fourth industrial revolution anyway.",
        "bullets": [
            "Pomp's bear case on paper: rates up, oil about $105-110, 10-year **5.2-5.3%**, home prices \"falling\", Iran still going, a K-shaped economy.",
            "Pomp's test: told that 6 months ago, you'd have guessed the S&P and Nasdaq **15%** lower.",
            "Ives: the 10-year is high *because of* growth, more debt raises, the data-center build-out and capex.",
            "He argues bears \"called 10 of the last 2 downturns\" and scare retail; catastrophist narratives create the opportunities.",
            "Tech will \"plow through and be the leader of this market\" despite 10-year oil and geopolitics.",
        ],
        "quote": {"text": "Bears have called 10 of the last two downturns.", "cite": "— Dan Ives"},
        "watch": None,
        "names": None,
    },
    {
        "id": "ivai-fund",
        "tags": ["finance", "ai-infra"],
        "color": "gray",
        "badge": "Product",
        "status": "TICKER IVAI",
        "title": "The Ives Ultra Fund: private AI exposure in a public wrapper",
        "lead": "Ives launched a $200M special-purpose investment fund to give retail and advisors access to private AI companies.",
        "bullets": [
            "Pomp describes it as SPAC-like but an investment fund: **$200 million** raised, ticker **IVAI**, permanent capital.",
            "Ives calls it the first public company to invest in private AI tech companies; a \"Swiss Army knife\" portfolio of large known names and potential \"next Palantirs\".",
            "Pitch: SPV 1, 2, 3 exist for institutions; retail has no path in, so \"why can't people in the public own these\"?",
            "Pomp calls it a step in the public/private blending trend (tokenization, similar funds) and says Ives is the right person to source the companies.",
            "Ives expects SpaceX, OpenAI and Anthropic going public to be \"very good for the market\" and a \"golden age\" for AI listings.",
            "Pomp notes the Oura IPO was pulled despite a claimed 4x oversubscription; Ives says Anthropic isn't comparable and the IPO window opens after the midterms.",
        ],
        "quote": None,
        "watch": "Ives is the fund's principal and the product is promoted in the same conversation as his bullish private-AI thesis; the host also has private AI investments (e.g. a data company).",
        "names": [
            {"name": "SpaceX", "blurb": "Ives: SpaceX, OpenAI and Anthropic going public is good for the market.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Own chips and hyperscalers as the core; treat memory, Dell, Cisco and cyber as the broadening trade Ives points to."},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Read lab calls for regulation through a regulatory-capture lens before treating them as safety signals."},
    {"icon": "\U0001F9EE", "tag": "AI economics", "title": "Model lab revenue as token price x consumption and track per-customer token usage, not just headline run-rate."},
    {"icon": "\U0001F6E1️", "tag": "Enterprise", "title": "Test routing narrow workloads to your own applied models; Pomp saw ~97% cost savings with better accuracy."},
    {"icon": "\U0001F6A8", "tag": "IPOs", "title": "Don't assume good product means good company; watch Anthropic's S-1 trends after the midterms."},
    {"icon": "\U0001F30D", "tag": "Macro", "title": "Weigh the macro bears against capex data; Ives expects chip equilibrium only in late 2028-early 2029."},
]

HOT_TAKES = [
    {"take": "We're less than 15% through what the spending trend's going to be the next 3 to 4 years. It's 4 to 5 trillion dollars.", "cite": "— Dan Ives", "why": "numeric forward call"},
    {"take": "You don't have equilibrium till late 2028, early 2029 in terms of chips.", "cite": "— Dan Ives", "why": "dated"},
    {"take": "More jobs will be created by AI than taken away over the next decade.", "cite": "— Dan Ives", "why": "contrarian dated call"},
    {"take": "The SaaS apocalypse was a fictional narrative.", "cite": "— Dan Ives", "why": "dismissal"},
    {"take": "I think that the private large lab models are in way more trouble than people realize.", "cite": "— Anthony Pompliano", "why": "contrarian call"},
    {"take": "A good product does not equal a good company.", "cite": "— Anthony Pompliano", "why": "dismissal"},
]

CLAIMS = [
    {"who": "Dan Ives", "claim": "AI capex over the next 3-4 years reaches $4-5 trillion, with less than 15% done.", "metric": "AI capex", "target": "$4-5T", "by": "3-4 years", "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "Each dollar of AI capex generates a $5-6 multiplier across the rest of tech.", "metric": "capex multiplier", "target": "$5-6 per $1", "by": None, "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "The chip market doesn't reach supply-demand equilibrium until late 2028 or early 2029.", "metric": "chip equilibrium", "target": "equilibrium", "by": "late 2028 / early 2029", "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "About 800,000 data centers get built in the next 12-18 months even if 10-15% are voted down.", "metric": "data centers built", "target": "800,000", "by": "12-18 months", "condition": "10-15% voted down", "entity": None},
    {"who": "Dan Ives", "claim": "Anthropic IPOs before year-end or soon after the midterms.", "metric": "IPO", "target": "occurs", "by": "after the midterms", "condition": None, "entity": "Anthropic"},
    {"who": "Dan Ives", "claim": "Asia checks show 13-to-1 chip demand-to-supply.", "metric": "demand/supply", "target": "13:1", "by": None, "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "More jobs are created by AI than taken over the next decade.", "metric": "net jobs", "target": "net positive", "by": "next decade", "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "New stocks not currently discussed emerge in the consumer-agent category.", "metric": "new AI stocks", "target": "emerge", "by": "18-24 months", "condition": None, "entity": None},
    {"who": "Anthony Pompliano", "claim": "Sovereign AI routing cuts cost about 97% versus frontier models.", "metric": "inference cost", "target": "97% saving", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Anthropic", "rel": "competes_with", "to": "OpenAI", "note": "described as the two leading private labs"},
    {"from": "Meta (META)", "rel": "competes_with", "to": "Alphabet (GOOGL)", "note": "gap to the leading labs narrowing, per Ives"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Ray Dalio / Dario Amodei essays on AI risk (names garbled in captions), the All-In podcast appearance by Jensen Huang, S-1 filings.", "tag": "Sources"},
    {"icon": "\U0001F4A1", "title": "Data licensing: Pomp says someone asked to license his podcast as training data; \"data is data\" and \"data is the new oil and gold\".", "tag": "Data"},
    {"icon": "\U0001F6E0️", "title": "Pomp says he retrained as a software engineer over 6 months; an engineer told him \"show me what you've built\" is the first hiring question, so the lines are blurring.", "tag": "Careers"},
    {"icon": "\U0001F5FA️", "title": "Europe is \"building Blockbuster videos\"; Middle East skewed to US tech; India still deciding US vs China.", "tag": "Geopolitics"},
    {"icon": "\U0001F4F1", "title": "iPhone-price analogy: priced double in 2007-08, you don't get 1.5B iPhones; token pricing needs open source for the same reason.", "tag": "Analogy"},
]

GLOSSARY = [
    {"term": "Sovereign AI", "def": "Companies or nations owning their own models and data rather than renting a frontier lab's intelligence."},
    {"term": "Regulatory capture", "def": "Incumbents backing regulation that raises barriers for later entrants."},
    {"term": "Token consumption", "def": "Volume of tokens a customer sends through a model; Pomp says it leads revenue."},
    {"term": "Applied AI", "def": "A model trained for one specific use case rather than general intelligence."},
    {"term": "IVAI", "def": "Ticker of the Ives Ultra Fund, a public permanent-capital vehicle holding private AI companies."},
]
