META = {
    "title": "They JUST Accidentally Revealed the Truth: The AI Bubble",
    "channel": "Meet Kevin",
    "speakers": "Kevin Paffrath",
    "date": "2026-10-31",
    "video_url": "https://www.youtube.com/watch?v=R6CTLeHIJBY",
    "thread_line": "4 threads · SK Hynix tries to kill the memory cycle · AI demand read-through · NAND and agents · a 0.3 PEG",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Kevin reads SK Hynix's earnings call line by line and calls it one of the most bullish calls he has ever read.",
    "Over **50%** of 2027-2028 capacity is locked in long-term agreements with 14 customers, and customers are asking for longer ones.",
    "DRAM and HBM volume is effectively sold out through 2029; customer demand is more than double what Hynix can supply.",
    "Hynix's oversupply answer: more fabs doesn't mean more bits, because HBM takes 2-5x the wafers of DRAM.",
    "Read-through: hyperscaler cloud revenue +30-80%, cloud backlogs up 2-5x, and AI spend now spread across sovereign, on-prem and non-tech buyers.",
    "Kevin drops Anthropic/OpenAI as his AI-boom canary; the labor market stays as the other one.",
    "Valuation: about a 6 P/E on the ADR against ~19% average EPS growth, a ~0.3 PEG. Kevin owns no memory stocks but is 'salivating'.",
]

THEMES = [
    {
        "id": "hynix-kill-cycle",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "SK HYNIX EARNINGS CALL",
        "title": "SK Hynix is trying to kill memory's boom-bust cycle with longer contracts and custom HBM",
        "lead": "Long-term agreements plus custom chips turn a cyclical commodity into contracted, sticky supply.",
        "bullets": [
            "The fear: memory has a classic glut cycle (2014, 2023, the dot-com bust). Shortage, everyone builds, demand slows, prices fall off a cliff.",
            "Over 50% of Hynix's 2027-2028 production is under long-term agreements with **14 customers**, including nearly all major cloud providers, and it is in talks to extend terms.",
            "Custom HBM is the lock-in: like the ASICs Marvell and Broadcom build for Anthropic and OpenAI, Hynix will tailor memory per customer as Nvidia and others weigh 'de-speccing' to avoid stranded memory when bandwidth is the bottleneck.",
            "Capex rises significantly in 2027 vs 2026, including a ramp of the first fab in Yongin, but free cash flow is still exploding after capex.",
            "Shareholder returns: ~45 billion expected to be returned soon and 50% of free cash flow going back to shareholders.",
            "Oversupply answer: more fabs don't mean more bits, since HBM uses about 2-5x the wafers of DRAM. Hynix also stays on its 6F process rather than risk yield and cost problems at 4F.",
        ],
        "quote": {"text": "these companies are trying to kill the boom and bust cycle for memory", "cite": "— Kevin Paffrath"},
        "watch": "Kevin flags that an earnings call is a sales pitch for the stock: 'more fabs ≠ more supply' is management's bullish case, and if the AI trade slows it all unwinds, probably into a recession.",
        "names": [
            {"name": "SK Hynix (000660.KS)", "blurb": "LTAs on >50% of 2027-28 capacity; sold out through 2029; ~6 P/E.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "through 2029"},
            {"name": "Marvell (MRVL), Broadcom (AVGO)", "blurb": "Custom ASIC makers for Anthropic and OpenAI, the template for custom HBM.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Spec changes on how much memory to put on chips; GPUs command a premium over ASICs for flexibility.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ai-demand-readthrough",
        "tags": ["ai-infra", "macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "SOLD OUT THROUGH 2029",
        "title": "The memory call says AI demand is broadening, not peaking",
        "lead": "Hynix sees demand at more than double its supply, and spending spread across so many buyers that no single pullback breaks it.",
        "bullets": [
            "Major hyperscale customers report 30-80% year-on-year cloud revenue growth; other cloud order backlogs grew 2-5x.",
            "DRAM and HBM volume effectively sold out through 2029; HBM4 prices expected to rise; customer volume requests are more than double current supply.",
            "Broadening: sovereign AI, on-prem and non-tech companies now buy, so one company cutting back no longer swings total demand. More multi-site, mid-size data centers will bring power online faster.",
            "Kevin's ADU analogy: Reinvest files six applications hoping to get three. Spread sites the same way so a couple of permit denials don't matter.",
            "Kevin changed his second canary: Anthropic and OpenAI matter less with Microsoft, Gemini, Amazon, SpaceX and Grok competing. 'It's not just Oracle, it's everyone.' The labor market stays canary one.",
            "Google Workspace upsell as a live check: 'AI expanded access' at $24/month per seat unlocks up to 200 Argon (Gemini 4) responses. Per-seat AI add-ons are where Google prints money.",
            "GDP backdrop: Atlanta Fed Q3 real GDP estimate at 3.3%, down from as high as 6% earlier in the quarter.",
        ],
        "quote": {"text": "I almost want to be bearish because of how bullish it is.", "cite": "— Kevin Paffrath"},
        "watch": None,
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Per-seat AI add-ons in Workspace; Kevin says Google 'prints money' this way.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Anthropic (ANT), OpenAI", "blurb": "Dropped as Kevin's AI-boom canary as competition broadens.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "No longer the single name that moves the AI market.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "nand-agents",
        "tags": ["semis", "dev-workflow"],
        "color": "green",
        "badge": "Contested",
        "status": "BULLISH NAND · DRAM SUPPLY THESIS INTACT",
        "title": "Agents are quietly pushing memory onto SSDs, which is the NAND bull case",
        "lead": "Inference is saturating RAM, so cache spills to storage, and Hynix earns 21% of its income from NAND.",
        "bullets": [
            "Kevin: machines running agents without a good SSD bog down or crash, because agents offload memory to the SSD in the background; his M4 Max handles it, cheap laptops (Apple Neos) won't.",
            "Hynix says NAND demand rises as inference grows, since cache gets stored off memory instead of leaving systems memory-locked.",
            "Primer: DRAM, DDR5 and HBM are memory; NAND is the storage cell, the SSD is the product, NVMe is the interface.",
            "Kevin still holds his thesis that DRAM supply will explode; Hynix counters that bigger HBM stacks absorb DRAM bits.",
        ],
        "quote": None,
        "watch": "Kevin's DRAM-supply-glut thesis and Hynix's 'net fewer bits' counter are unresolved.",
        "names": None,
    },
    {
        "id": "hynix-valuation",
        "tags": ["semis"],
        "color": "amber",
        "badge": "Speculative",
        "status": "DOES NOT OWN · 'SALIVATING'",
        "title": "A 6 P/E and 0.3 PEG: the market is pricing a memory crash that the call says isn't coming",
        "lead": "Analysts bake in a down year in 2029, which Kevin calls 'loony tunes' against a sold-out order book.",
        "bullets": [
            "ADR math (10:1 ratio, Kevin says to fact-check him): $162.73 divided by ~27.1 of EPS ≈ a 6 P/E.",
            "Consensus EPS growth: +35%, +22%, -18% (2029), +38% (2030), about 19% a year on average; Kevin expects better.",
            "6 P/E / 19% growth ≈ a **0.3 PEG**, 'so discounted for cyclicality it's insane'.",
            "Context: Kevin was a memory bear since summer and called the run a meme move (like GameStop at $400), urging trailing stops. He owns no memory or storage stocks.",
        ],
        "quote": {"text": "I want to be clear, I don't own any memory or storage plays, but I have to say your boy is salivating.", "cite": "— Kevin Paffrath"},
        "watch": "His ADR conversion is back-of-envelope and he says so; he holds no position.",
        "names": [
            {"name": "SK Hynix (000660.KS)", "blurb": "~0.3 PEG; analysts forecast a negative 2029.", "stance": "WATCHING", "conviction": "Medium", "horizon": "2027-2030"},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4DC", "tag": "Semis", "title": "Read memory makers' long-term-agreement coverage, not spot prices, to judge whether the cycle is really broken."},
    {"icon": "\U0001F9EE", "tag": "Valuation", "title": "Run the PEG on SK Hynix yourself before trusting a 6 P/E, because the ADR ratio trips people up."},
    {"icon": "\U0001F4BE", "tag": "AI infra", "title": "Add NAND/storage to the AI-inference watchlist, not just HBM."},
    {"icon": "\U0001F426", "tag": "Macro", "title": "Track the labor market as the AI-boom canary now that no single lab drives demand."},
    {"icon": "\U0001F4BB", "tag": "Hardware", "title": "Buy a machine with a fast SSD and plenty of memory if you run agents locally."},
]

HOT_TAKES = [
    {"take": "This was probably one of the most bullish earnings calls that I've ever read.", "cite": "— Kevin Paffrath", "why": "strong bull call from a self-described memory bear"},
    {"take": "Dude, this is trading for a point three peg. This has been so discounted for cyclicality. It's insane.", "cite": "— Kevin Paffrath", "why": "valuation call vs analyst consensus"},
    {"take": "The analyst expectations are just loony tunes right now.", "cite": "— Kevin Paffrath", "why": "dismisses consensus 2029 decline"},
    {"take": "I believe there has been a massive inflection in the last 6 months in how good AI is. And I think that's the contrarian piece is that most people don't even notice it yet.", "cite": "— Kevin Paffrath", "why": "contrarian adoption claim"},
]

CLAIMS = [
    {"who": "SK Hynix (cited by Kevin Paffrath)", "claim": "DRAM and HBM volume is effectively sold out through 2029.", "metric": "DRAM/HBM volume", "target": "sold out", "by": "2029", "condition": None, "entity": "SK Hynix (000660.KS)"},
    {"who": "SK Hynix (cited by Kevin Paffrath)", "claim": "Over 50% of 2027-2028 capacity is committed under long-term agreements.", "metric": "capacity under LTAs", "target": ">50%", "by": "2028", "condition": None, "entity": "SK Hynix (000660.KS)"},
    {"who": "SK Hynix (cited by Kevin Paffrath)", "claim": "Capex increases significantly in 2027 versus 2026, ramping the first Yongin fab.", "metric": "capex", "target": "significant increase", "by": "2027", "condition": None, "entity": "SK Hynix (000660.KS)"},
    {"who": "SK Hynix (cited by Kevin Paffrath)", "claim": "HBM4 prices are expected to increase.", "metric": "HBM4 price", "target": "higher", "by": None, "condition": None, "entity": "SK Hynix (000660.KS)"},
    {"who": "Analyst consensus (cited by Kevin Paffrath)", "claim": "SK Hynix EPS grows 35%, 22%, then falls 18% in 2029 before growing 38% in 2030.", "metric": "EPS growth", "target": "+35/+22/-18/+38%", "by": "2030", "condition": None, "entity": "SK Hynix (000660.KS)"},
    {"who": "Kevin Paffrath", "claim": "SK Hynix will beat the ~19% average EPS growth analysts expect.", "metric": "average EPS growth", "target": ">19%", "by": "2030", "condition": None, "entity": "SK Hynix (000660.KS)"},
]

RELATIONS = [
    {"from": "Marvell (MRVL)", "rel": "supplies", "to": "Anthropic (ANT)", "note": "custom ASICs"},
    {"from": "Broadcom (AVGO)", "rel": "supplies", "to": "OpenAI", "note": "custom ASICs"},
    {"from": "SK Hynix (000660.KS)", "rel": "supplies", "to": "Nvidia (NVDA)", "note": "HBM; spec changes on memory per chip"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: the SK Hynix earnings call transcript, a Bloomberg Tech clip, the Atlanta Fed GDP estimate, and Google Admin's Workspace pricing.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "LTA", "def": "Long-term agreement: a multi-year supply contract that locks in volume with a customer."},
    {"term": "HBM", "def": "High bandwidth memory: stacked DRAM packaged next to AI accelerators, using ~2-5x the wafers of standard DRAM."},
    {"term": "ASIC", "def": "Application-specific chip that does one job very well but loses value if needs change."},
    {"term": "6F / 4F", "def": "DRAM cell-layout geometries; 4F packs more cells but carries yield and cost risk."},
    {"term": "NAND / SSD / NVMe", "def": "Storage cell technology, the finished drive, and the PCIe interface it connects through."},
    {"term": "PEG", "def": "P/E divided by expected EPS growth rate; under 1 suggests growth is cheap."},
]
