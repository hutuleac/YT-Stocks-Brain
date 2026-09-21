"""Data file for David Stout x School of Hard Knocks Podcast — He Started With a $400 Loan... Now His AI Company Is Worth $2.5 Billion."""

META = {
    "title": "He Started With a $400 Loan… Now His AI Company Is Worth $2.5 Billion | David Stout",
    "channel": "School of Hard Knocks Podcast",
    "speakers": "David Stout (WebAI founder/CEO, guest), James, Jack, and Josh (School of Hard Knocks Podcast hosts)",
    "date": "2026-07-15",
    "video_url": "https://www.youtube.com/watch?v=h-X3h9L4gU8",
    "thread_line": "5 threads · WebAI's origin story from a $400 grandfather loan to a $2.5B valuation built on edge/on-device AI, David Stout's thesis that specialized models beat general foundation-model intelligence, WebAI's upcoming local-AI consumer app launch, his critique of data center buildout economics, and lessons on fundraising, recruiting, and faith-driven leadership.",
    "category": "market",
}

SNAPSHOT = [
    "David Stout co-founded WebAI (with high school friend Ethan) starting with a $400 loan from his grandfather to buy a shared computer; the company is now informally valued around $2.5 billion, with Stout retaining roughly 50% ownership — he dropped out of a small Michigan business school (Davenport) after his freshman-year web services startup was already earning $750,000/year with 60 clients.",
    "WebAI's founding insight (circa 2016-2018) was that AI needed to run locally on-device rather than depend on distant data centers, since latency makes cloud-dependent computer vision (e.g. object detection for cameras) impractical — this 'edge AI' thesis was widely dismissed at the time, including reportedly by someone in a room at a16z who said the market wasn't big enough.",
    "Stout argues foundation-model 'general intelligence' from labs like Anthropic and OpenAI is becoming a commoditized level playing field, and that real competitive value is shifting to specialized, proprietary models trained on tacit, non-internet data (e.g. how a steel foundry is run, how chicken is packaged) — he cites Palantir CEO Alex Karp's public prediction that most AI companies won't exist in two years as directionally correct for generalist plays, though not for WebAI's specialization strategy.",
    "WebAI is launching a consumer product (expected August 2026) that runs entirely on-device with no data center dependency, letting users build 'personas' — specialized collaborative models trained on their own files and knowledge — arguing this shifts AI ownership from rented subscriptions to something users permanently own and can pass on.",
    "Stout is sharply critical of the current data center buildout, framing it (via a Union Pacific railroad analogy) as a capital-intensive bet likely to be technologically obsolete before it pays off, and cites a real example of a Northern Virginia plant nursery bulldozed for a data center on a former Civil War battlefield site as illustrative of the trade-offs being made.",
    "Closes on leadership and personal philosophy: recruited senior talent (including a former Pentagon Office of Strategic Capital director and a former SCSP AI strategist under Eric Schmidt) via referrals from board member Dave Burnham of Benchmark Capital, credits early investor David Schuman for taking a chance on an unknown Michigan founder, and discusses his Christian faith and mentorship as central to how he wants to lead and be remembered.",
]

THEMES = [
    {
        "id": "webai-origin-edge-ai",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "Confirmed trajectory — from $400 loan to ~$2.5B valuation",
        "title": "From a $400 Grandfather Loan to a $2.5B AI Company, Built on an Edge-AI Bet Nobody Wanted",
        "lead": "**WebAI's founding thesis was contrarian from day one:** AI needed to run on local devices, not distant data centers, at a time (2016-2018) when most investors doubted AI was even real, let alone that on-device AI was a viable market.",
        "bullets": [
            "Stout and co-founder Ethan met in high school, ran a profitable web services company together as college freshmen ($750K/year, 60 clients), then pivoted to studying machine learning around 2016 after Stout grew bored with easy website work and wanted a harder, more overlooked problem.",
            "The founding epiphany: trying to run early computer-vision models (a 'darknet' object-detection model, similar to what powers Tesla's driving system) in a college dorm on an i3 processor revealed that sending video data to a distant data center and back introduced too much latency to be usable — this became WebAI's singular focus: making AI work directly on-device.",
            "The idea was initially rejected broadly, including reportedly at an a16z meeting where someone in the room said edge AI wasn't a big enough market — Stout frames this as a case where founders should distinguish between 'nobody cares because it's a bad idea' and 'nobody understands it yet,' the latter being where real opportunity often hides.",
            "The pivotal fundraising moment came from proving the technology (a working demo of AI running on a laptop with no cloud) rather than pitching an idea — Stout argues raising money on an unproven idea is how founders lose disproportionate equity, since investors price in the risk they're absorbing.",
            "Early investor David Schuman (an early backer of Oura Ring) discovered Stout via an NSA report on AI researchers and personally traveled to Michigan to meet him, despite other Bay Area funds reportedly telling Schuman there were no credible AI scientists in Michigan — several of those same funds have since invested in WebAI.",
        ],
        "quote": {"text": "Your job as a founder is to reduce risk every day. That means you retain more, your company is worth more.", "cite": "— David Stout"},
        "watch": "WebAI's $2.5B figure is described in the interview as a 'public valuation' but the company has no public stock ticker — it reflects private/secondary market pricing, not a listed equity valuation.",
        "names": [
            {"name": "Palantir (PLTR)", "blurb": "Cited for comparison on public-sector growth speed; CEO Alex Karp's predictions on AI company survival discussed at length.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "specialized-models-thesis",
        "tags": ["ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — foundation model economics under pressure",
        "title": "'General Intelligence Doesn't Win': Why Specialized Models Beat Foundation Labs",
        "lead": "**Stout's core business thesis is that frontier foundation models (Claude, GPT) are becoming a commoditized level playing field**, and that durable competitive advantage will come from narrow, proprietary specialization instead.",
        "bullets": [
            "Argues that once every company has access to the same frontier-level model (his example: two competitors both using the same 'Opus'-tier model), the model itself stops being a differentiator — the only edge left is which questions you know to ask and what proprietary, non-internet data you can bring to it.",
            "Cites Palantir CEO Alex Karp's public statement that most AI companies won't exist within two years as directionally true, specifically for companies whose entire value proposition is wrapping a generic foundation model with no real specialization — notes Karp himself described Palantir as having been a 'delivery mechanism' for Anthropic six months earlier, then treating Anthropic as a supply-chain risk more recently.",
            "Describes WebAI's own approach as training specialized models on genuinely tacit industry knowledge unavailable on the public internet (how a steel foundry is run, how chicken is packaged), explicitly contrasted with legal-AI company Harvey — Stout frames WebAI's approach as a level beyond that, since Harvey still runs on a third-party model backend rather than fully proprietary infrastructure.",
            "Cites Meta's internal AI spend (reportedly $50,000 per employee per year on token usage) as an unsustainable cost structure that will push companies toward owning rather than perpetually renting intelligence — predicts foundation-model 'rental' will get displaced by locally-owned, specialized models the way contractors historically fought to own their own tools rather than being locked into an employer's equipment.",
            "Frames this as analogous to early-20th-century coal miners rioting for the right to own their own tools rather than depend on the mining company's — argues people will eventually want to 'own their own IQ points' rather than indefinitely rent access to centralized intelligence.",
        ],
        "quote": {"text": "Once everyone has the same intelligence, how do you defeat your competitor? You can't.", "cite": "— David Stout"},
        "watch": "Stout's framing of foundation labs as structurally weak is explicitly his own competitive thesis as a rival AI company founder, not a neutral analysis — he has direct financial incentive to argue specialization beats generality.",
        "names": [
            {"name": "Anthropic", "blurb": "Cited as an example of the shifting relationship dynamic with Palantir (from 'delivery mechanism' to 'supply chain risk'); framed by Stout as part of the foundation-model commoditization story.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Meta (META)", "blurb": "Cited for its reported ~$50,000/employee/year AI token spend as an example of unsustainable foundation-model rental costs.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenAI", "blurb": "Referenced generally alongside Anthropic as part of the foundation-model layer Stout expects to get commoditized.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "consumer-launch-personas",
        "tags": ["ai-infra", "dev-workflow"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — consumer launch expected August 2026",
        "title": "WebAI's Consumer Launch: On-Device 'Personas' You Own Instead of Rent",
        "lead": "**WebAI's first-ever consumer product, expected in August 2026, runs entirely on-device (including in airplane mode)** and lets users build specialized, personally-owned collaborative models called 'personas.'",
        "bullets": [
            "The product downloads a model directly onto the user's machine (Mac Studio-class local hardware is cited as a practical entry point); no data center round-trip is required once the model is loaded, and the app automatically selects the right combination of specialized sub-models to answer a given query.",
            "Describes 'personas' as a new model type distinct from simple prompt-engineered chatbot personalities — each persona has its own access to specific knowledge bases and files, letting a user build genuinely specialized expert models (e.g. an aircraft-engine expert vs. a marketing expert) rather than one generalized assistant.",
            "Frames the business model shift explicitly: rather than a recurring subscription with usage caps ('$20 more to keep going after midnight'), ownership of the model itself becomes the product — Stout predicts a future where individuals sell or subscribe others to time on their own personally-trained AI models as a genuine income source.",
            "Recommends small businesses buy low-cost local AI hardware now (citing the 'Mac Mini + Openclaw' local-automation trend) to get ahead of token-cost caps and velocity limits that constrain cloud-subscription AI usage, arguing the hardware itself remains a useful asset regardless of how AI strategy evolves.",
            "Positions this as reversing a growing dependency risk: current AI subscriptions are effectively steeply subsidized ('Uber rideshare prices for a Ferrari') by labs burning cash, and Stout expects that subsidy to be unsustainable — recommends using current cheap access to build tacit skills and knowledge bases now, before pricing normalizes.",
        ],
        "quote": {"text": "The distribution of intelligence, for the first time, is going to be owned by the user — that's really exciting.", "cite": "— David Stout"},
        "watch": "The August 2026 launch date and specific product claims are Stout's own stated plans as of this interview, not independently verified shipped features.",
        "names": None,
    },
    {
        "id": "data-center-critique",
        "tags": ["energy", "policy"],
        "color": "red",
        "badge": "Flagged risk",
        "status": "WATCHING — Stout expects local/edge compute to undercut the buildout thesis",
        "title": "'We're Making a Bad Investment as a Country': Stout's Data Center Critique",
        "lead": "**Stout argues the current data center buildout boom is a risky, capital-intensive bet on infrastructure that may become technologically obsolete** before it fully pays for itself — drawing a direct historical parallel to railroad overbuild.",
        "bullets": [
            "Uses the Union Pacific railroad analogy: railroads were essential infrastructure investment in their era, but today's railroad beds are mostly repurposed as bike paths — argues data centers risk a similar fate if on-device/local AI (his own company's bet) reduces the need for centralized compute over the coming years.",
            "Cites a specific real-world example: a Northern Virginia plant nursery (roughly 100 acres, owned by a co-host's mother) was reportedly bought outright for $160 million specifically to be demolished for data center construction, on land near a Civil War battlefield — used to illustrate the land-use and opportunity-cost tradeoffs of the current buildout pace.",
            "Frames data centers explicitly as the direct successor to room-sized early mainframe computers — physically massive, power- and cooling-intensive centralized processing hubs that current AI queries depend on end-to-end.",
            "Argues the efficiency alternative (better local/edge processing, or eventually more radical options like undersea or space-based compute) is a real long-term risk to the current buildout thesis, and that 'we're going to destroy a lot of jobs' and stranded capital if the industry over-invests in a centralized model that gets displaced by more efficient distributed compute.",
        ],
        "quote": {"text": "We're building all these data centers and thinking they're going to be there for a while... this bet is not only risky, it's a gamble that's very unlikely to be the core of our society.", "cite": "— David Stout"},
        "watch": "This is explicitly Stout's own contrarian, business-interested view (as the founder of an edge/on-device AI company) rather than an industry consensus position.",
        "names": None,
    },
    {
        "id": "leadership-recruiting-faith",
        "tags": ["career"],
        "color": "green",
        "badge": "Recommendation",
        "status": "Ongoing personal practice",
        "title": "Fundraising Scars, Recruiting Top Talent, and Leading Through Faith",
        "lead": "**Stout closes on the human side of building a ~200-person, multi-billion-dollar company**: absorbing dozens of investor rejections, recruiting senior talent through trusted referrals, and grounding his leadership in his Christian faith.",
        "bullets": [
            "Estimates a roughly 20-to-1 no-to-yes ratio is normal for venture-backed founders, and frames early rejections (including one from a top-tier fund) as painful but often partially correct at the time — argues founders should neither dismiss investor 'no's entirely nor give them too much credit, since many funds that initially passed later invested once the thesis proved out.",
            "Credits board member Dave Burnham (an early Benchmark Capital partner, reportedly Steve Jobs' go-to talent advisor for hiring decisions) as the source of his approach to recruiting — used referrals from Burnham's network to recruit a former Pentagon Office of Strategic Capital director and a former SCSP AI strategist under Eric Schmidt to build WebAI's defense/public-sector team, which he says became one of the fastest-growing public-sector software businesses on record.",
            "Describes his leadership style as flexible, humble, and servant-leadership oriented, running weekly multi-hour leadership meetings during peak morning focus hours rather than frequent 1-on-1s, given the company now has roughly 200 employees supporting a multi-billion-dollar valuation.",
            "Credits his Christian faith (reinforced by mentors including Henry Kerr) as central to how he wants to lead and be remembered, while explicitly acknowledging that some of the worst business behavior he's personally encountered has come from people who publicly advertise their faith — frames consistent, observable behavior over time as the only credible proof of character.",
            "Closing message: wants to be remembered as someone who cared deeply about people, treated them with respect, and fought for a future where AI ownership is broadly distributed rather than concentrated in a small number of centralized companies or individuals.",
        ],
        "quote": {"text": "Morality cannot be regulated. I believe the best possible future for AI is one that mimics the Second Amendment — you have the right to own AI, and we should have the right to own our own intelligence.", "cite": "— David Stout"},
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4BB", "tag": "AI infra", "title": "Buy low-cost local AI hardware now to start offsetting token-cost and rate-limit risk before cloud-subscription pricing normalizes."},
    {"icon": "\U0001F3AF", "tag": "Careers", "title": "Build proprietary, tacit-knowledge datasets specific to your business rather than betting long-term on generic foundation-model access."},
    {"icon": "\U0001F4B0", "tag": "Careers", "title": "Prove a technology with a working demo before fundraising on an idea alone — it materially changes how much equity you have to give up."},
    {"icon": "\U0001F3E2", "tag": "Energy", "title": "Watch on-device/edge AI adoption trends as a real long-term risk factor for centralized data center buildout economics."},
    {"icon": "\U0001F91D", "tag": "Careers", "title": "Recruit senior talent through trusted referral networks (a strong board member's Rolodex) rather than cold outbound alone."},
]

CLAIMS = [
    {"who": "David Stout", "claim": "WebAI's current informal valuation", "metric": "company valuation", "target": "$2.5 billion", "by": None, "condition": "described as a 'public valuation' but WebAI is a private company with no listed stock ticker", "entity": None},
    {"who": "David Stout, citing Meta's reported spend", "claim": "Meta's per-employee AI token spend", "metric": "annual spend per employee", "target": "~$50,000/year", "by": None, "condition": None, "entity": "Meta (META)"},
    {"who": "Alex Karp (cited by David Stout)", "claim": "most AI companies will not exist in the near future", "metric": "company survival", "target": "most current AI companies gone", "by": "within ~2 years of his statement", "condition": "Karp's own publicly stated view, cited secondhand by Stout", "entity": None},
    {"who": "David Stout", "claim": "WebAI's consumer product launch timing", "metric": "launch date", "target": "August 2026", "by": "August 2026", "condition": "his own stated internal timeline as of this interview", "entity": None},
]

RELATIONS = [
    {"from": "Palantir (PLTR)", "rel": "customer_of", "to": "Anthropic", "note": "Described by David Stout as having been a 'delivery mechanism' for Anthropic six months prior to this interview, per Alex Karp's own comments"},
]

HOT_TAKES = [
    {"take": "Morality cannot be regulated. I believe the best possible future for AI is one that mimics the Second Amendment — you have the right to own AI.", "cite": "— David Stout", "why": "A specific, provocative policy framing for AI ownership rights, not a generic optimism statement."},
    {"take": "There's nothing about AI that scares me. There are things about people and companies that scare me.", "cite": "— David Stout", "why": "A direct rejection of AI-risk framing in favor of a specific institutional-power critique."},
    {"take": "Once everyone has the same intelligence, how do you defeat your competitor? You can't.", "cite": "— David Stout", "why": "A checkable, contrarian business thesis directly against the value of frontier foundation-model access, made by a competing AI company's founder."},
    {"take": "We're making a bad investment as a country [on data centers].", "cite": "— David Stout", "why": "A blunt, specific criticism of a multi-hundred-billion-dollar national infrastructure trend, backed by a historical analogy."},
    {"take": "Some of the people who have treated me the worst in business have been people who advertise faith.", "cite": "— David Stout", "why": "A candid, self-critical admission that cuts against his own stated Christian identity rather than flattering it."},
]

OTHER_NEWS = []

GLOSSARY = [
    {"term": "Edge AI", "def": "AI processing that happens directly on a local device (phone, laptop, camera) rather than being sent to a remote data center — reduces latency and removes dependency on network connectivity and centralized compute."},
    {"term": "Tokens (AI usage)", "def": "The unit AI providers use to price and meter usage of their models; heavy or unpredictable usage can push a company's variable AI costs well beyond a flat subscription fee."},
    {"term": "Persona (WebAI)", "def": "WebAI's term for a specialized, locally-run collaborative AI model trained on a specific user's or domain's own knowledge base, as distinct from a single general-purpose assistant."},
]
