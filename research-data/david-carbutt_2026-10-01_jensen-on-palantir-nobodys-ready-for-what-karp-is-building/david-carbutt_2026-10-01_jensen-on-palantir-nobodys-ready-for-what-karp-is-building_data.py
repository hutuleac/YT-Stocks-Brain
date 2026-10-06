META = {
    "title": "Jensen on Palantir: Nobody’s Ready for What Karp Is Building",
    "channel": "David Carbutt",
    "speakers": "David Carbutt",
    "date": "2026-10-01",
    "video_url": "https://www.youtube.com/watch?v=RkBHJZAying",
    "thread_line": "5 threads · submarine-yard pilot · ontology explained · Nvidia on both sides · growth metrics · deployment hurdles",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Pilot at General Dynamics Electric Boat, per the US Navy: Palantir cut build-schedule creation from about **160 hours** to under 10 minutes.",
    "Jensen Huang called Palantir's ontology \"probably the single most important enterprise stack in the world today\"; Nvidia now also uses Palantir in its own supply chain (disclosed September 2026).",
    "Ontology = linking company data (trucks, orders, customers, parts) so AI can follow a problem to its consequence and humans approve the action.",
    "Q2 2026: revenue up **93%** y/y, US commercial revenue **$764M** (+149%), 47% operating margin, net dollar retention **157%**, 653 US commercial customers (+35%).",
    "Palantir forecast about **$8.15B** revenue for 2026 (August); Gartner puts 2026 AI software spend at about $462B.",
    "Open questions: no disclosed Nvidia supply-chain improvement or Palantir revenue from it; deployments are complex and lengthy, and rivals and existing tools compete.",
]

THEMES = [
    {
        "id": "shipyard-pilot",
        "tags": ["software", "ai-infra", "policy"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "NAVY PILOT · DECEMBER 2025 INVESTMENT",
        "title": "Palantir cut submarine build scheduling from 160 hours to under 10 minutes",
        "lead": "A faster schedule is real, but the prize is helping the yard decide what to change when people, parts or priorities move.",
        "bullets": [
            "Site: General Dynamics Electric Boat, which builds America's nuclear submarines; figure is per the US Navy.",
            "A schedule must combine people, parts and equipment, so one late delivery cascades into later work.",
            "In December 2025 the Navy announced **$448 million** into ShipOS using Palantir to improve shipbuilding and the supply chain.",
            "Carbutt's caveat: a faster plan only matters if people can act on the result.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Palantir (PLTR)", "blurb": "Software behind the Navy shipyard scheduling pilot and ShipOS.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "General Dynamics (GD)", "blurb": "Electric Boat subsidiary hosted the scheduling pilot.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ontology-nvidia",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "Partnership",
        "status": "NVIDIA ON BOTH SIDES",
        "title": "The ontology links data to decisions, and Nvidia now uses it in its own supply chain",
        "lead": "Nvidia sells the compute; Palantir tries to connect that compute to daily business decisions, with humans keeping the final call.",
        "bullets": [
            "Jensen Huang: Palantir's ontology is \"probably the single most important enterprise stack in the world today\", said when announcing a commercial partnership bringing Nvidia compute and AI models into Palantir software.",
            "Truck analogy: shipping, finance, maintenance and orders each hold a piece; the ontology links them so a breakdown traces to affected customers, and actions follow with permissions and approvals.",
            "Value comes from consequence: a delivery carrying parts that keep a factory running outranks one that can wait a day.",
            "September 2026: Nvidia spoke publicly about using Palantir on its supply chain (materials, sites, capacity, commitments).",
            "Planners accept, edit or override recommendations; decisions, expectations and outcomes are recorded and fed back.",
            "No measured shipment improvement and no Palantir revenue figure for the Nvidia work were disclosed; Carbutt says the benefit could be far larger than planning-time savings if it works.",
        ],
        "quote": {"text": "Probably the single most important enterprise stack in the world today.", "cite": "— Jensen Huang, on Palantir's ontology (as relayed by David Carbutt)"},
        "watch": "Nvidia is both supplier and customer in this partnership, so the endorsement comes from a party with a commercial stake.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Supplies compute and models to Palantir and uses Palantir in its own supply chain.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "growth-metrics",
        "tags": ["software", "finance"],
        "color": "green",
        "badge": "Reported figures",
        "status": "Q2 2026 RESULTS AND FORECAST",
        "title": "Fast growth, 47% operating margin and 157% net dollar retention",
        "lead": "Company-wide figures can't isolate the Nvidia partnership or the ontology, but they show expansion that isn't service-heavy.",
        "bullets": [
            "Q2 2026 revenue up **93%** year over year (the caption's dollar figure is garbled, so not stated here).",
            "US commercial revenue **$764M**, up 149%: a growing business beyond government.",
            "Operating margin **47%** under standard accounting rules.",
            "Net dollar retention **157%**: $100 from a customer group becomes $157 the next 12 months; not every customer grew 57%.",
            "653 US commercial customers, up 35% (US commercial only; retention is company-wide).",
            "August forecast: about **$8.15B** revenue for 2026.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "expansion-hurdles",
        "tags": ["software", "consumer"],
        "color": "amber",
        "badge": "Contested",
        "status": "CAN IT TRAVEL ACROSS INDUSTRIES?",
        "title": "From shipyards to retail: the market is large, but deployment is the hard part",
        "lead": "Repeatable benefits, not demos, decide whether spending outlasts the AI excitement.",
        "bullets": [
            "October 2025: Lowe's said it was building a digital replica of its global supply chain with Palantir; no measured saving was given.",
            "Gartner's September forecast: worldwide AI software spend of about **$462B** in 2026, far beyond Palantir's reach alone.",
            "Palantir warns deployment can be complex and lengthy; its boot camps aim to reach a use case in **5 days**.",
            "Implementation needs agreed data ownership and decision rights; a workshop win is different from daily use.",
            "Competition: customers may solve the problem with tools they already pay for.",
            "Karp (August): customers' competitive advantage should never become training data for future models; Carbutt notes cloud and on-premises options and that this is not a universal guarantee.",
        ],
        "quote": None,
        "watch": "Carbutt sells YouTube-growth services and a Palantir course to his audience.",
        "names": [
            {"name": "Lowe's (LOW)", "blurb": "Building a digital replica of its supply chain with Palantir (Oct 2025).", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F6A2", "tag": "Markets", "title": "Judge Palantir on repeat use inside customers: watch net dollar retention and US commercial growth."},
    {"icon": "\U0001F50D", "tag": "AI infra", "title": "Look for Nvidia supply-chain results that Palantir can cite; none is disclosed yet."},
    {"icon": "\U0001F9E9", "tag": "Software", "title": "Ask whether an AI tool links data to decisions and approvals, not just answers."},
    {"icon": "\U0001F6D2", "tag": "Retail", "title": "Track Lowe's and other supply-chain deployments for measured savings."},
    {"icon": "⏱️", "tag": "Execution", "title": "Test deployment speed claims (5-day boot camps) against how long customers take to go live."},
]

HOT_TAKES = [
    {"take": "Palantir has more to build on than an impressive demonstration that still needs to find a workable business.", "cite": "— David Carbutt", "why": "positive read of the business"},
]

CLAIMS = [
    {"who": "Palantir (cited by David Carbutt)", "claim": "Palantir forecast about $8.15 billion of revenue for 2026", "metric": "2026 revenue", "target": "$8.15B", "by": "2026", "condition": None, "entity": "Palantir (PLTR)"},
    {"who": "Gartner Research", "claim": "Worldwide AI software spending in 2026 will be roughly $462 billion", "metric": "AI software spend", "target": "$462B", "by": "2026", "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Nvidia (NVDA)", "rel": "partners_with", "to": "Palantir (PLTR)", "note": "Nvidia compute and models inside Palantir software"},
    {"from": "Nvidia (NVDA)", "rel": "customer_of", "to": "Palantir (PLTR)", "note": "uses Palantir on its own supply chain"},
    {"from": "Lowe's (LOW)", "rel": "partners_with", "to": "Palantir (PLTR)", "note": "digital replica of global supply chain, Oct 2025"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: US Navy (pilot figure and $448M ShipOS announcement), Gartner (September AI software forecast), Jensen Huang and Alex Karp statements.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Ontology (Palantir)", "def": "A model linking a company's data to real-world objects (trucks, orders, customers, parts) so problems trace to consequences and actions."},
    {"term": "Net dollar retention", "def": "Revenue this year from last year's customers as a percentage of what they paid before; 157% here."},
    {"term": "ShipOS", "def": "The Navy shipbuilding and supply-chain program using Palantir, backed by a $448M December 2025 investment."},
]
