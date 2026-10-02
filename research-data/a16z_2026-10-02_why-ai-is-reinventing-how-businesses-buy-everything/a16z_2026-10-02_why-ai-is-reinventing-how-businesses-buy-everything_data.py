META = {
    "title": "Why AI Is Reinventing How Businesses Buy Everything",
    "channel": "a16z",
    "speakers": "Seema Amble (Partner, a16z), Vlad Keil (co-founder & CEO, Lio), a16z podcast host",
    "date": "2026-10-02",
    "video_url": "https://www.youtube.com/watch?v=OTQ-lFsq7zA",
    "thread_line": "5 threads · startups vs AI-boosted incumbents · the four-agent ladder · trust & human-in-the-loop negotiation · the last 20% beats DIY builds · procurement as a trillion-dollar boring market",
    "category": "market",
}

SNAPSHOT = [
    "a16z's Seema Amble (author of \"The incumbents are coming\") and Lio CEO Vlad Keil ask where an AI-native startup wins once incumbents bolt a frontier model onto their system of record.",
    "Her answer: incumbents are stuck inside their **system of record**. Startups win by owning the whole end-to-end job across billing, legal, finance and email.",
    "Seema's four-agent ladder runs **retrieval → process → policy → principal**. Most incumbents are still at retrieval with a little process, held back by internal conflicts more than by technology.",
    "In procurement, the system of record shows \"8K for aluminum\". It doesn't show the 30 meetings, 500 emails and 20 spreadsheets behind that number.",
    "Lio earns trust with human-in-the-loop negotiation that scales to 100k autonomous negotiations, starting with spend under $50K that enterprises never negotiated at all.",
    "A DIY build gets you 70% performance in 8 hours. But 70% performance still means 100% of the work gets re-checked, and the last 20% is the business.",
    "Vlad's thesis: procurement is boring, emotional and P&L-critical, since 1% in savings equals 10% more sales. He calls it a trillion-dollar opportunity.",
]

THEMES = [
    {
        "id": "incumbents",
        "tags": ["software"],
        "color": "amber",
        "badge": "Contested",
        "status": "a16z THESIS — 'THE INCUMBENTS ARE COMING'",
        "title": "Incumbents plus a frontier model are tougher rivals, but they're stuck in one system of record",
        "lead": "Seema says incumbent-plus-model is the new third competitor, and the startup's opening is owning the end-to-end job no single system of record touches.",
        "bullets": [
            "The old frame, in partner Alex Rampell's phrase, was distribution vs innovation. Now an incumbent can layer a model on top (\"Claude plus **Salesforce**\") and keep the data and the users.",
            "Example: a customer charged after cancelling. Resolving it hits billing, chat history and the contract. That's knowledge across systems, not one record. In legal, the equivalent is owning everything from brief through trial.",
            "Vlad: the record says \"8K for aluminum.\" It hides a supplier asking 10K and a cost engineer's 3 weeks of spreadsheets and 3D modeling. Most procurement work happens outside the ERP.",
            "Incumbents have trust and distribution. Salesforce's Agentforce was an easy yes at almost no extra cost. But resolving the work cannibalizes workflow products sold to different buyers by different VPs.",
            "Vlad: incumbents can **destroy the trust** they have by shipping agents too early. A startup has to earn it.",
            "Some incumbents partner with OpenAI or Anthropic to supercharge their stack. Seema says they're \"held back,\" not holding back.",
        ],
        "quote": {"text": "The opportunity for the AI native startup is to say, we're going to own that entire end-to-end arc.", "cite": "— Seema Amble"},
        "watch": "a16z led Lio's $30M Series A, and Seema is on the investing side. This is a portfolio CEO and his investor making the startup-beats-incumbent case.",
        "names": [
            {"name": "Salesforce (CRM)", "blurb": "Agentforce: easy adoption through existing trust and near-zero added cost, but limited by internal product conflicts.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SAP (SAP), Oracle (ORCL)", "blurb": "The ERP systems of record that invoice agents push data back into. Most procurement work happens outside them.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "agent-ladder",
        "tags": ["software", "dev-workflow"],
        "color": "green",
        "badge": "Framework",
        "status": "FOUR AGENT TYPES",
        "title": "Retrieval, process, policy, principal: where judgment enters",
        "lead": "The four agent types differ in how much judgment they apply. Incumbents have mostly stopped at retrieval and a little process.",
        "bullets": [
            "A year ago Seema mocked the \"slap on a chatbot\" strategy: a chat window over the system of record that retrieves data and does light analytics.",
            "Outage example: **retrieval** confirms the contract and the outage, **process** applies the credit by the handbook, and **policy** judges whether 20 minutes counts as \"significant.\"",
            "**Principal** weighs going beyond policy, for example extra compensation to save the relationship after a terrible outage.",
            "Lio spans all four, depending on risk, budget approval and complexity. Some purchases run fully autonomously, others keep a human in the loop.",
            "Invoice agents were a \"side quest\": invoice software is 100% of today's market but only 20% of the job. The other 80% is exceptions like fraud and mismatches, the non-happy path.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "trust-loop",
        "tags": ["software"],
        "color": "green",
        "badge": "Recommendation",
        "status": "LIO PLAYBOOK",
        "title": "Earning trust: negotiate what was never negotiated, keep experts in the loop on the big deals",
        "lead": "No enterprise starts with autonomous negotiation. Lio starts where a bad agent costs nearly nothing, and uses human feedback to earn the next tier.",
        "bullets": [
            "Lio started 3 years ago, weeks before ChatGPT. Pitching slightly ahead of the curve let it ship each new agent tier weeks after customers confirmed the problem.",
            "With a human in the loop, the agent learns how a specific Fortune 10 company operates. Customers then trust it for 10k, 20k, then **100k negotiations**.",
            "Enterprises never negotiated spend below ~$50K. Vlad's \"hack\": send a $40K invoice and it gets paid, unless they run Lio. A bad agent there risks \"nearly zero.\"",
            "Relationship spend (e.g. the vendor who set up a16z's podcast studio) runs mostly autonomously, but with tone of voice tuned by procurement staff.",
            "On multi-million-dollar deals, experts always stay in the loop. Agents run for hours on 3D models and drawings, then ask a cost engineer for feedback.",
            "Seema: the bigger trust leap is external, letting a Lio agent negotiate with a third party. Many buyers feel burned by incumbents' past promises.",
        ],
        "quote": {"text": "No company and no enterprise starts with fully autonomous negotiation agents from day one.", "cite": "— Vlad Keil"},
        "watch": None,
        "names": [
            {"name": "Lio", "blurb": "a16z-backed procurement agents spanning retrieval through principal. Human-in-the-loop scaling to 100k negotiations; multi-agent end-to-end flows.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "multi-agent",
        "tags": ["software", "ai-infra"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "IN PRODUCTION — INDIRECT AND DIRECT SPEND",
        "title": "Why procurement needs a multi-agent system: the Boeing bolt, the late part, the oil index",
        "lead": "A human procurement task spans eight people, three departments and five tools, so only agents that share context in sequence can do it end to end.",
        "bullets": [
            "A Boeing bolt, fully autonomous: a photo or quote in, then agents check inventory and other plants, source suppliers, send RFQs, parse messy replies, negotiate or e-auction, and track shipment and invoice.",
            "A part arriving 2 weeks late can cause **hundreds of millions** in damage. The notice is one of 500 emails, and the ERP only stores the new date.",
            "Agents trade cost against reliability: a supplier missing 20% of goods may be 10x cheaper than one missing 1%. Context includes news and even Polymarket odds on disruptions.",
            "**Indirect** spend (MRO, factories, laptops, marketing) can mean 50,000 suppliers. **Direct** means 100-2,000 strategic suppliers, sometimes $1B on one, with 3-month negotiations.",
            "Direct deals are 90% preparation: 10 people for three months to pay $900M instead of $1B. Agents are back of house, with some real-time help.",
            "Real-time example: the supplier cites oil up 10%, but the part is 30% oil. So the fair increase is ~4%, not 10%.",
            "Seema's point: procurement used to sit \"in a box.\" Now it touches legal, finance, cost engineering and many systems, with specialists and generalists both involved.",
        ],
        "quote": {"text": "If they missed this email, hundreds of millions of damage.", "cite": "— Vlad Keil"},
        "watch": None,
        "names": [
            {"name": "Boeing (BA)", "blurb": "Vlad's example of a fully autonomous bolt purchase run end to end by agents.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Polymarket", "blurb": "Prediction-market odds on disruptions as one source of outside context for supplier decisions.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "last-20",
        "tags": ["software", "dev-workflow"],
        "color": "amber",
        "badge": "Contested",
        "status": "BUILD VS BUY",
        "title": "Models are a commodity, so the moat is the last 20%: harness, proprietary data, deployment",
        "lead": "Anyone can build 70% of a vertical agent in a day. The durable company owns the last 20% that gets it into production, and the customer dependence that follows.",
        "bullets": [
            "Lio's first viral product (quote into SAP), built by 3-4 engineers, is now an **8-hour** hiring test. A DIY build reaches 70% performance, but that still means 100% of the work gets checked.",
            "Seema: a Fortune 500 firm spent 3-4 months building its own cash-collection tool. It had poor context, two ERPs plus a third coming, and nobody to maintain mappings, so it dropped the effort.",
            "Lio uses models from all providers as a commodity. A harness gets some jobs to 100%, others stall at 80%, and that last 20% takes ~80% of the effort (Pareto). Like Harvey and Decagon, it's starting to fine-tune.",
            "The remaining gaps are **should-cost modeling** and price benchmarking. Those need proprietary cross-enterprise data, and BCG and McKinsey quotes can differ 10x for the same work.",
            "Vlad wants outcome-trained models that capture an expert's gut feel and output a price, not text. (The model name he cites is unclear in the captions.)",
            "Moats are hard to forecast. Seema's signal is dependence: an old CRM logged deals, while a new sales agent does the prep, outbound and inbound itself.",
            "Lio is 85% engineers. Forward-deployed engineers have one KPI: automate their own job. Seema contrasts this with paying Accenture for SAP customization.",
        ],
        "quote": {"text": "You will only reach 70% of the performance… 70% of performance doesn't mean 70% automation.", "cite": "— Vlad Keil"},
        "watch": None,
        "names": [
            {"name": "Harvey, Decagon", "blurb": "Vertical AI companies cited as now fine-tuning their own models.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Accenture (ACN)", "blurb": "The old route to SAP customization, which forward-deployed, software-driven setup is replacing.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "procurement-market",
        "tags": ["software", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "VLAD'S THESIS — 'TRILLION-DOLLAR OPPORTUNITY'",
        "title": "Boring, emotional, P&L-critical: why procurement is the trillion-dollar agent market",
        "lead": "Everyone hates procurement and no real revolution has hit it in 20 years. That makes it easy to impress and worth a lot, since 1% savings equals 10% more sales.",
        "bullets": [
            "There are 500-1,000 procurement tools, yet requesters, suppliers and procurement staff all hate the process. The tools made it more efficient but never changed the email, Teams, Excel and PowerPoint work.",
            "The last revolution was 20 years ago, plus a nicer UI 10 years ago. Seema recalls a Coupa user giving the \"most disgruntled customer call\" she'd ever done.",
            "**1% savings = 10% more sales** in P&L terms. It also governs how data centers, aircraft, cars and drones get built.",
            "Lio's third Bots & Buyers summit drew 100+ procurement leaders (CPOs and VPs) in New York. The next, in Munich, expects ~700. Attendees walk through physical booths to try the agents.",
            "Suppliers lag: sales usually leads procurement, but supplier teams use Granola-style recording tools without deployed agents. Big industrial buyers can dictate supplier tooling, so Lio aims to own **both sides**.",
            "Price is the one adversarial point. The other ~5,000 tasks behind it (speed, low friction) align both parties, so one platform can serve both sides, as two law firms could share open-issue tracking.",
        ],
        "quote": {"text": "You have like boring, highly emotional and then plus crazy business impact… a trillion dollar business opportunity.", "cite": "— Vlad Keil"},
        "watch": "The trillion-dollar figure is Vlad's own opinion ('that's my opinion') about the market he sells into.",
        "names": [
            {"name": "Coupa", "blurb": "Legacy procurement system of record. Seema's example of a deeply disgruntled user.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9ED", "tag": "Startups", "title": "Pick a job that spans several systems of record. The incumbent can't follow you across them."},
    {"icon": "\U0001F4B8", "tag": "Procurement", "title": "Start agent negotiation on spend under $50K that nobody negotiates today. The downside is near zero and the savings are pure upside."},
    {"icon": "\U0001F9EA", "tag": "Build vs buy", "title": "Before a DIY agent build, measure how much human re-checking 70% accuracy still requires."},
    {"icon": "\U0001F4CA", "tag": "Finance", "title": "Model procurement savings at 10x their face value in revenue terms when making the business case."},
    {"icon": "\U0001F465", "tag": "Org design", "title": "Give forward-deployed engineers the KPI of automating their own job."},
]

HOT_TAKES = [
    {"take": "Invoice software… that's like 100% of the software market, but it's actually only like 20% of the work of the job to be done.", "cite": "— Vlad Keil", "why": "dismisses an entire software category"},
    {"take": "I challenge someone to find someone who loves to work with procurement. No one does.", "cite": "— Vlad Keil", "why": "provocative about his own market"},
    {"take": "If you just manage to get like 1% savings it's like equals like 10% of sales.", "cite": "— Vlad Keil", "why": "numeric ROI claim"},
    {"take": "You have boring, highly emotional and then plus crazy business impact… a trillion dollar business opportunity.", "cite": "— Vlad Keil", "why": "market-size claim"},
]

CLAIMS = [
    {"who": "Vlad Keil", "claim": "AI procurement agents are a trillion-dollar business opportunity.", "metric": "procurement AI opportunity", "target": "$1T", "by": None, "condition": None, "entity": "Lio"},
    {"who": "Vlad Keil", "claim": "Lio's next Bots & Buyers summit, in Munich, draws ~700 people.", "metric": "event attendance", "target": "~700", "by": None, "condition": None, "entity": "Lio"},
    {"who": "Vlad Keil", "claim": "There will be agents on both the buyer and supplier sides of transactions.", "metric": "two-sided agent adoption", "target": "both sides", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Andreessen Horowitz", "rel": "invests_in", "to": "Lio", "note": "led Lio's $30M Series A"},
    {"from": "Lio", "rel": "competes_with", "to": "Coupa", "note": "legacy procurement system of record"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Seema Amble's essay \"The incumbents are coming\", and Alex Rampell's distribution-vs-innovation framing. Lio's practice of making forward-deployed engineers automate their own work is likened to Google's.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "System of record", "def": "The authoritative database (CRM, ERP) that stores the outcome of work, not the work itself."},
    {"term": "Principal agent", "def": "Seema's top agent tier: weighs going beyond policy, such as extra compensation to protect a relationship."},
    {"term": "Direct vs indirect procurement", "def": "Direct is parts that go into the product (few, strategic suppliers). Indirect is everything else, like MRO, services and office supplies."},
    {"term": "Should-cost modeling", "def": "Cost engineers estimating what a part should cost from drawings and input indices, before negotiating."},
    {"term": "RFQ", "def": "Request for quotation sent to suppliers to collect pricing."},
    {"term": "MRO", "def": "Maintenance, repair and operations supplies, a classic indirect-spend category."},
    {"term": "Forward-deployed engineer (FDE)", "def": "An engineer embedded with a customer to configure and deploy the product, ideally automating that setup over time."},
]
