META = {
    "title": "Anthropic’s IPO in Question,  Midterms Hit AI, Nasdaq Drops 5%, and RSI Accelerates | #309",
    "channel": "Peter H. Diamandis",
    "speakers": "Salim Ismail, Alex Wissner-Gross, Dave Blundin",
    "date": "2026-11-07",
    "video_url": "https://www.youtube.com/watch?v=WF-ADiC7Khs",
    "thread_line": "6 threads · midterms vs data centers · AI selloff · METR's RSI study · joules-to-GDP · compute scarcity · DNA screening · visible Dyson swarm",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Democrats swept the midterms; **56%** opposition to big tech and data centers made AI a ballot issue for the first time.",
    "Goldman Sachs: **45%** of planned US data-center buildout could face restrictions; pause candidates won or led in 12 governor races.",
    "Market reaction: Nasdaq -5.5%, S&P -4%+, big semis -12%, Nvidia -9.3%, Korea -6%.",
    "Anthropic IPO: panel split on a delay; bankers reportedly pushing the valuation down, Meta's IPO cited as the precedent.",
    "METR's 11-week study: Anthropic's AI development runs at **1.9x** its historical rate, ~80% of it from AI assisting AI research.",
    "Alex: so deep into recursive self-improvement that software alone gets us there even if all data-center construction stopped.",
    "Compute is sold out to a handful of buyers — Dave calls for a \"right to compute\".",
    "Also: new White House DNA-synthesis screening policy and a long-exposure photo showing ~1,400 satellites as a \"baby Dyson swarm\".",
]

THEMES = [
    {
        "id": "midterms-data-centers",
        "tags": ["policy", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "DEMS SWEEP · DATA CENTERS ON THE BALLOT",
        "title": "Midterms turn data centers into the binding constraint",
        "lead": "Community and political resistance may now limit AI infrastructure more than chips or capital — and the buildout shifts to states that want it.",
        "bullets": [
            "Salim: the vote was driven mainly by war, inflation and tariffs, but **56%** opposed big tech and data centers; Goldman Sachs estimates 45% of planned US buildout could face restrictions.",
            "Dave: first time he's seen a technical topic dominate an election — a senator wants a moratorium; the big news is **Texas**, while Elon put Colossus in Tennessee.",
            "Dave: Democrats are attacking tech firms that historically backed them — and those firms now own the media, unlike Big Oil.",
            "Alex's grand bargain: states with powered land should ask hyperscalers for free school lunches, county medical care or tax rebates \"before it all just moves to orbit\".",
            "Industry response: Elon calls orbital data centers attractive; OpenAI's community compact on energy costs and its CFO says no slowdown; Google's **$17B** Wyoming data center; Meta warns of construction challenges.",
            "Dave: Canada has the best per-capita power in North America (Eric Schmidt has said so for two years); projects started now come online around the next election.",
            "Salim: European energy CEOs he met in Madrid weren't even looking at building more generation; one Spanish party now wants to keep nuclear running.",
        ],
        "quote": {"text": "the flops must flow", "cite": "— Alex Wissner-Gross"},
        "watch": "Alex calls space compute almost a foregone conclusion; Dave says best case it's a couple percent of compute in two years.",
        "names": [
            {"name": "Goldman Sachs (GS)", "blurb": "45% of planned buildout could face restrictions", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SpaceX (SPCX)", "blurb": "3.6 GW on Earth, targeting 13 GW by end of next year; orbital compute", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "$17B Wyoming data center", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenAI", "blurb": "Community compact to cover energy costs", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Meta (META)", "blurb": "Warned of construction challenges", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ai-selloff-ipo",
        "tags": ["semis", "finance"],
        "color": "red",
        "badge": "Confirmed event",
        "status": "NASDAQ -5.5% · NVDA -9.3%",
        "title": "The AI selloff and Anthropic's IPO math",
        "lead": "Markets priced in slower power and construction on planned-but-unapproved projects; the panel doesn't see approved builds stopping.",
        "bullets": [
            "Nasdaq -5.5%, S&P -4%+, big semis -12%, **Nvidia -9.3%**, Korea -6%.",
            "Dave: Nvidia and hyperscalers slid for 4-5 weeks before the vote, popped on election day, then dropped — the market prices in giving China a leg up.",
            "Dave: short-term effect may be pricier AI and fewer breakthroughs; Elon says ~**15 GW** of compute sits idle without a liquid-cooled data center.",
            "IPO: Dave expects a push-through since the roadshow started after Polymarket odds were clear; Alex sees bankers forcing the valuation down but urgency before January rules.",
            "Meta precedent per Dave: priced down, traded down, then up \"20 30x\" — \"the best buy in the history of the world\" if you waited a few weeks.",
            "Alex likens Anthropic/OpenAI's regulatory headwind to mobile threatening Facebook at its IPO.",
        ],
        "quote": None,
        "watch": "Dave notes Dario is now in a quiet period, so the lab can't say much publicly.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Fell 9.3% after the election", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Anthropic", "blurb": "IPO roadshow under valuation pressure", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "rsi-metr",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "METR: 1.9x · ~80% AI-ASSISTED",
        "title": "METR measures recursive self-improvement at Anthropic",
        "lead": "The panel argues RSI is already here — compute is being pulled inward to AI researchers, and software alone now carries progress.",
        "bullets": [
            "METR's 11-week independent study: Anthropic's development at ~**1.9x** its historical rate, ~80% attributed to AI assisting AI research; no bottleneck seen over the next year.",
            "Alex: we're within 10-15% of where AI 2027 predicted for November 2026; METR's code-named Model 4 sits above the trend line.",
            "Dave: Anthropic's internal token use up **235x** in 6 months; if the AI has even 1 good idea in 10 versus Noam Brown's 6, it's a multi-billion-person research force.",
            "Alex: Navier-Stokes reportedly took 10,000 agents, the later \"slop drop\" three agent-hours per problem — models now have research taste, trainable from 1-in-10 to 9-in-10 good ideas.",
            "Alex: the biggest RSI output so far is a legible shift to **looped transformers**; he predicts the end-state architecture will be \"impossibly beautiful\" and explainable — Claude Shannon could have derived it; Dave: the transformer is far simpler than Maxwell's equations.",
            "Dave: hard takeoff looks like labs selling products (drugs, a Jony Ive device) instead of compute; most people's first AI contact will be a talking avatar.",
            "Dave's aviation warning: don't let AI end as a cancelled-flight queue — divert compute to making it feel good.",
        ],
        "quote": {"text": "We're at super intelligence escape velocity at this point", "cite": "— Alex Wissner-Gross"},
        "watch": "Salim notes full autonomous RSI is unproven and Rome argues diminishing returns.",
        "names": [
        ],
    },
    {
        "id": "joules-to-gdp",
        "tags": ["software", "energy"],
        "color": "gray",
        "badge": "Speculative",
        "status": "NEW BENCHMARK · 220 TASKS",
        "title": "Economic value per joule as an AI benchmark",
        "lead": "A new paper scores models by dollars per unit of energy — and Chinese open-weight models win on efficiency.",
        "bullets": [
            "220 professional tasks across 44 occupations: **GLM 5.2** led at ~$70 per task; the smaller Gemma 4 31B gave 2.5x more value per joule.",
            "Alex: Chinese open-weight models beat American ones per watt, likely from constrained training compute — he'd rather track dollars in vs dollars out, as reversible computing could beat the Landauer limit.",
            "Dave: small task models vs frontier is a foot race; Elon cites ~100x gains for task-specific models; Liquid AI is having \"a field day\" — firms will spend $300,000 of tokens, not $10M.",
            "Salim's provocation: Anthropic ~**$8B** revenue per GW vs New York City's $1.2T GDP on 5.5 GW — a city looks ~30x more energy-efficient.",
            "Dave: wrong math — half a billion tokens equalled ~5,000 workers for ~$5,000, \"a buck a day\"; value delivered far exceeds what Anthropic collects.",
            "Alex: Anthropic's compute ~4 GW by year-end, aiming at **16-18 GW** in 2027-2028.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Liquid AI", "blurb": "Small task models in demand", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "compute-scarcity",
        "tags": ["ai-infra", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "COMPUTE SOLD OUT FOR YEARS",
        "title": "Compute sold out — the case for a right to compute",
        "lead": "A few buyers have reserved nearly all chips and capacity, starving startups, and the panel fears a nuclear-style 50-year freeze.",
        "bullets": [
            "Dave: Google, Anthropic and xAI have reserved basically all compute and chips for years — TSMC's capacity would be locked up if it did multi-year deals; \"almost like Rockefeller era again\".",
            "Salim: a pilot client was told by a cloud it wasn't big enough as a customer.",
            "Dave: his NVL72 (72 GB300 GPUs) comes online Feb 1, only via an inside contact; neoclouds are having a rough month, but **Modal** is \"just killing it\".",
            "Alex: restricted supply should push compute prices up, a healthy signal toward offshore, underwater, underground or space; GPUs regulated like uranium would be the nightmare.",
            "Dave: a bakery without AI faces a 30-50% operating-margin disadvantage; he cites Michael Saylor's Ayn Rand award speech on being cut off by Google, Apple and Microsoft.",
            "Alex's \"Frontier Liberation Front\": keeping the frontier competitive matters more than any single lab, given the safety cartel risk.",
        ],
        "quote": {"text": "you don't want to get deplatformed from all the GPUs", "cite": "— Dave Blundin"},
        "watch": "Alex and Dave flag a financial interest in the GPU-access discussion (disclosure cut off mid-sentence).",
        "names": [
            {"name": "xAI", "blurb": "Among the buyers reserving compute for years", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "TSMC (TSM)", "blurb": "Capacity effectively spoken for", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Modal", "blurb": "Huge growth, buying all compute it can", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "dna-dyson",
        "tags": ["biotech", "space"],
        "color": "gray",
        "badge": "Policy watch",
        "status": "NSTM-6 ISSUED · ~1,400 SATELLITES",
        "title": "DNA-synthesis choke points and the visible Dyson swarm",
        "lead": "Regulating physical outputs beats regulating thoughts, and the orbital compute layer is already visible to the naked eye.",
        "bullets": [
            "White House NSTM-6: federally funded researchers must use approved synthesis providers; screening for sequences of **50+ nucleotides**, customer verification, 8-year record retention.",
            "Alex: like Treasury's yellow anti-counterfeit dots on printers — controlling actions beats a \"safety cartel\" of government-approved compute; expects licensed robot makers with 90-day command retention next.",
            "Dave: automated synthesis machines should log to a registry with class 1-4 device tiers.",
            "Photographer Brendan Larson stacked 578 photos over 2 hours above Mount Taranaki: ~15,000 trails from ~1,400 satellites.",
            "Alex: Starlink, Elon's AI satellites and StarCloud are the \"baby Dyson swarm\"; sun-synchronous orbit is roomy enough to ease Kessler worries; Dave recommends Star Walk-style apps.",
            "Alex: see it at Acadia National Park's night-sky festival; a compute halo will glow at dawn and dusk.",
        ],
        "quote": None,
        "watch": "Alex discloses a financial interest in a space-compute company he names alongside StarCloud.",
        "names": [
            {"name": "StarCloud", "blurb": "Part of the orbital compute layer", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F3AF", "tag": "Markets", "title": "Separate approved data-center builds from planned-but-unzoned ones when sizing the selloff."},
    {"icon": "\U0001F3AF", "tag": "Policy", "title": "Track which states court data centers (Tennessee, Virginia) versus restrict them (Texas)."},
    {"icon": "\U0001F3AF", "tag": "IPOs", "title": "Watch Anthropic's IPO pricing; a cut price echoes Meta's post-IPO dip."},
    {"icon": "\U0001F3AF", "tag": "AI compute", "title": "Lock in compute access early — supply is reserved for years."},
    {"icon": "\U0001F3AF", "tag": "Efficiency", "title": "Benchmark small task models on value per dollar before paying for frontier tokens."},
]

CLAIMS = [
    {"who": "Dave Blundin", "claim": "Anthropic will push its IPO through rather than delay.", "metric": "IPO timing", "target": "no delay", "by": None, "condition": None, "entity": "Anthropic"},
    {"who": "Alex Wissner-Gross", "claim": "Frontier labs should solve the top 5,000 diseases in silico within one to two years.", "metric": "diseases solved in silico", "target": "5,000", "by": "1-2 years", "condition": None, "entity": None},
    {"who": "Dave Blundin", "claim": "Orbital compute is a couple percent of all compute in two years, best case.", "metric": "share of compute in space", "target": "a couple percent", "by": "2 years", "condition": None, "entity": None},
    {"who": "SpaceX (cited by Salim Ismail)", "claim": "SpaceX targets 13 GW of terrestrial data-center capacity by end of next year.", "metric": "data-center capacity", "target": "13 GW", "by": "2027-12", "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Alex Wissner-Gross", "claim": "Frontier models move to continuous real-time release.", "metric": "frontier release cadence", "target": "continuous", "by": "2027-03", "condition": None, "entity": None},
    {"who": "Alex Wissner-Gross", "claim": "Within a few years humanity can launch relativistic von Neumann probes.", "metric": "von Neumann probes", "target": "capability", "by": "a few years", "condition": None, "entity": None},
    {"who": "Alex Wissner-Gross", "claim": "Anthropic's compute footprint reaches 16-18 GW.", "metric": "compute footprint", "target": "16-18 GW", "by": "2027-2028", "condition": None, "entity": "Anthropic"},
    {"who": "Dave Blundin", "claim": "Compute scarcity lasts three to seven years.", "metric": "compute shortage", "target": "persists", "by": "3-7 years", "condition": None, "entity": None},
    {"who": "Alex Wissner-Gross", "claim": "Regulators will require licensed robot makers with recorded actuation logs.", "metric": "robot licensing regime", "target": "introduced", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
]

HOT_TAKES = [
    {"take": "it was the best buy in the history of the world if you just waited out a few weeks after the IPO", "cite": "— Dave Blundin", "why": "Meta IPO precedent for Anthropic"},
    {"take": "Solve the top 5,000 diseases. Market the heck out of it to the general public", "cite": "— Alex Wissner-Gross", "why": "fix for AI backlash"},
    {"take": "we can I think at this point just through pure software improvements get to where we're going probably without any new data centers", "cite": "— Alex Wissner-Gross", "why": "RSI hot tip"},
    {"take": "I think we're on a collision course with the Fermy paradox", "cite": "— Alex Wissner-Gross", "why": "von Neumann probes"},
    {"take": "you will not be able to operate like even a bakery if you're deprived of AI", "cite": "— Dave Blundin", "why": "right to compute"},
    {"take": "This is this is a a cyclical blip on top of a secular trend in the middle of a singularity.", "cite": "— Alex Wissner-Gross", "why": "election backlash"},
]

OTHER_NEWS = [
    {"icon": "\U0001F30C", "title": "Alex: the overlooked sci-fi scenario is the Fermi paradox — few years from relativistic von Neumann probes; Salim's closing: institutions are sublinear, so be active, not passive.", "tag": "Space"},
    {"icon": "\U0001F399", "title": "Dave: the podcast genre survives because people need to be inspired by people, with far more AI content in the middle; Alex disputes the premise.", "tag": "Media"},
    {"icon": "\U0001F4DA", "title": "Sources referenced: Goldman Sachs, Polymarket, METR, AI 2027, Eric Schmidt, Noam Brown, Michael Saylor's speech, Philip Johnston, Ray Kurzweil's law of accelerating returns.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "RSI", "def": "Recursive self-improvement: AI doing most of the research that improves AI."},
    {"term": "Dyson swarm", "def": "A dense orbital layer of solar-powered compute and satellites."},
    {"term": "Looped transformer", "def": "A transformer that reuses its layers iteratively instead of a single pass."},
    {"term": "Landauer limit", "def": "Minimum energy to erase one bit; reversible computing could sidestep it."},
    {"term": "Kessler syndrome", "def": "Cascading orbital debris collisions that make an orbit unusable."},
    {"term": "NSTM-6", "def": "White House policy on synthetic DNA/RNA screening for federally funded research."},
]
