META = {
    "title": "Elon Just Said \"Never Seen Anything Like It\"",
    "channel": "Brighter with Herbert",
    "speakers": "Herbert (host), Jeff (supply-chain executive, CEO of a high-tech manufacturing consultancy)",
    "date": "2026-10-13",
    "video_url": "https://www.youtube.com/watch?v=5vfs1EsXPO8",
    "thread_line": "4 threads · SpaceX's $41.2B compute business · ARK's pricing-premium thesis · Terafab vs the chip industry's risk aversion · AI phones and Starlink Mobile spectrum",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "SpaceX's four biggest compute and hosting deals total **$41.2B a year** (~$3.43B/month); Elon: 'Revenue growth is insane. Never seen anything like it.'",
    "Anthropic is the biggest customer (~$15B/yr), then an unnamed customer (~$13.3B/yr from Dec 1), then Google and Reflection AI.",
    "CFO Bret Johnsen says SpaceX is on track for a $100B annual revenue run rate by year end.",
    "ARK's Brett Winton: SpaceX can charge a premium because unsold compute goes to its own AI — 'vertical integration is a superpower'.",
    "Elon says Terafab will start on standard tools, then build custom machines; the guest calls the chip industry's **risk aversion** the key insight.",
    "Qualcomm's CEO says AI companies want 100B-parameter models running on phones by 2028 and some are building phones.",
    "Phones arriving in 2027-2028 will carry chips for Starlink Mobile's higher-throughput spectrum, Elon confirmed.",
]

THEMES = [
    {
        "id": "spacex-compute",
        "tags": ["ai-infra", "space"],
        "color": "green",
        "badge": "High conviction",
        "status": "$41.2B/YR FROM FOUR DEALS",
        "title": "SpaceX's compute business: $41.2B a year before it reaches space",
        "lead": "Four compute and hosting contracts already make SpaceX one of the most lucrative data-center businesses, per the hosts.",
        "bullets": [
            "Anthropic ~$15B/yr; an unnamed new hosting customer ~$13.3B/yr starting Dec 1; Google and Reflection AI fill out the four.",
            "Separately, $6.7B of cloud services revenue contracted over six months, capacity ramping in October.",
            "200,000 Nvidia GB300s come online in November, possibly another batch in December; Vera Rubins next.",
            "Guest: reaching ~2.5-2.6 GW this year would beat the company's own summer projection.",
            "CFO **Bret Johnsen**: on track for a $100B annual revenue run rate by year end.",
            "Guest ranks compute bring-up third in difficulty for Elon's companies, behind Starship and Tesla FSD.",
        ],
        "quote": {"text": "Revenue growth is insane. Never seen anything like it.", "cite": "— Elon Musk (quoted by Herbert)"},
        "watch": "The guest expects discontinuities and daily noise, citing a Financial Times story on OpenAI accounting he calls FUD.",
        "names": [
            {"name": "SpaceX (SPCX)", "blurb": "$41.2B/yr from four compute deals; $100B run-rate target", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "by year end"},
            {"name": "Anthropic", "blurb": "Largest compute customer, ~$15B/yr", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "Compute customer", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Reflection AI", "blurb": "Compute customer", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "GB300 and Vera Rubin supplier", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "pricing-premium",
        "tags": ["ai-infra", "finance"],
        "color": "green",
        "badge": "Positive view",
        "status": "ARK ANALYSIS",
        "title": "'We'll use it ourselves': why SpaceX can charge a premium for compute",
        "lead": "ARK argues internal demand plus a strong balance sheet lets SpaceX price compute well above rental-only neoclouds.",
        "bullets": [
            "Brett Winton (ARK Invest): short-term deals, the Nvidia relationship and the ability to shift capacity to internal use let SpaceX command 'massively premium pricing'.",
            "ARK's chart shows Google and Anthropic paying more than other providers charge — a ~93% pricing premium.",
            "Guest: AI-only labs rely on neoclouds that lack Elon's hardware scaling experience with the SpaceX and xAI team.",
            "Fast access to the newest chips is a flywheel that adds revenue certainty — 'not risk-free'.",
            "Guest: TV analysts keep calling the end of the buildout while those with the most visibility say it has 'barely begun'.",
        ],
        "quote": {"text": "the people that have the most visibility to it are telling you it's, you know, it's barely begun", "cite": "— Jeff (guest)"},
        "watch": "ARK's premium assumes SpaceX keeps scaling its fleet.",
        "names": [
            {"name": "ARK Invest", "blurb": "Brett Winton's pricing-premium analysis", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "xAI", "blurb": "Team behind the compute bring-up", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "terafab",
        "tags": ["semis"],
        "color": "amber",
        "badge": "Speculative",
        "status": "RESEARCH LAB AT GIGA TEXAS",
        "title": "Terafab bets that chipmaking's risk aversion is beatable",
        "lead": "Elon plans to start on standard tools, then modify or build machines wherever production is limited, with a full iteration loop in one building.",
        "bullets": [
            "Touring Intel, Samsung and TSMC fabs, Elon saw 'not a ton of customized equipment' — everyone buys the same ASML and vendor tools.",
            "Plan: logic, memory, packaging and lithography masks in one building at Giga Texas so test-new-mask-new-chip loops run fast.",
            "Host: today's chip iteration takes 2-3 years; Elon is reportedly aiming for ~10 iterations a year.",
            "Guest pushes back: a factory tour hides process know-how, and Intel, Samsung and TSMC nodes differ in yields and cycle times.",
            "Guest's key point: **risk aversion** in silicon and consumer electronics leaves incumbents open to being leapfrogged; vertical integration means owning your schedule, not waiting in a foundry queue.",
            "Tesla's AI4, AI5 and AI6 still go through outside fabs with their design-for-manufacturability limits; after that it 'could be interesting'.",
            "Elon's recruiting pitch: Terafab's output value would rank in the top 20 of country GDPs.",
        ],
        "quote": {"text": "I still have a tremendous amount to learn about chipm I I don't know how to make chips to be clear", "cite": "— Elon Musk"},
        "watch": "Elon admits he has 'no idea how to make chips'; the guest expects failures, mitigated by failing fast.",
        "names": [
            {"name": "Tesla (TSLA)", "blurb": "Co-builder of Terafab; AI4/AI5/AI6 made at outside fabs", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "TSMC (TSM), Samsung, Intel (INTC)", "blurb": "Fabs Elon toured; risk-averse incumbents", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "ASML", "blurb": "Standard lithography tools every fab buys", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ai-phones",
        "tags": ["consumer", "space"],
        "color": "gray",
        "badge": "Speculative",
        "status": "PHONES 2027-2028",
        "title": "AI phones and Starlink Mobile: the device question",
        "lead": "Always-on local AI and native Starlink spectrum could reshape what a phone is, and SpaceX can play both sides.",
        "bullets": [
            "AT&T's CEO said Starlink Mobile can't get through walls; SpaceX then agreed to buy spectrum that does — Elon calls it 'the last critical piece' for full US coverage.",
            "Elon confirmed phones arriving in 2027-2028 will have chipsets for Starlink's higher-throughput spectrum.",
            "Qualcomm CEO Cristiano Amon: AI companies want a 100B-parameter model running on a phone all the time by 2028, and some are starting to make phones.",
            "Guest (who launched phones globally): RAM and memory costs are 'through the roof'; premium foldables like the iPhone Duo near $2,000; makers must show what local inference unlocks.",
            "Modems are hard — Apple is ramping its own, Motorola and Samsung have done them — so AI device makers will likely still talk to Qualcomm.",
            "Always-on high-bandwidth connectivity changes the on-device vs hosted split, giving SpaceX leverage either way.",
        ],
        "quote": None,
        "watch": "Whether SpaceX builds its own device is the hosts' open question, not a stated plan.",
        "names": [
            {"name": "Qualcomm (QCOM)", "blurb": "AI companies asking for on-phone 100B models by 2028", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": "by 2028"},
            {"name": "AT&T (T)", "blurb": "CEO doubted Starlink Mobile indoors", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Ramping its own modem", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4B0", "tag": "Space", "title": "Track SpaceX against its $100B year-end revenue run-rate target"},
    {"icon": "\U0001F5A5️", "tag": "AI infra", "title": "Compare compute prices: premium pricing only holds while internal AI demand absorbs unsold capacity"},
    {"icon": "\U0001F3ED", "tag": "Semis", "title": "Watch Terafab's iteration speed, not its first chip, as the real signal"},
    {"icon": "\U0001F4F1", "tag": "Devices", "title": "Look for 2027-2028 phones with native Starlink spectrum chipsets"},
]

HOT_TAKES = [
    {"take": "SpaceX's data center business might just be the most lucrative business ever.", "cite": "— Herbert", "why": "superlative claim"},
    {"take": "SpaceX is the most misunderstood company still", "cite": "— Herbert", "why": "contrarian framing"},
    {"take": "that risk aversion puts those companies at risk of being leapfrogged", "cite": "— Jeff (guest)", "why": "warning to incumbent chipmakers"},
    {"take": "the Financial Times not knowing how to read an accounting statement for Open AI", "cite": "— Jeff (guest)", "why": "dismisses FT reporting"},
]

CLAIMS = [
    {"who": "Bret Johnsen (cited by Herbert)", "claim": "SpaceX reaches a $100B annual revenue run rate by year end", "metric": "annual revenue run rate", "target": "$100B", "by": "2026-12", "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Herbert", "claim": "Unnamed hosting customer starts paying SpaceX ~$13.3B a year", "metric": "hosting revenue", "target": "$13.3B/yr", "by": "2026-12-01", "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Herbert", "claim": "200,000 Nvidia GB300s come online at SpaceX", "metric": "GPUs online", "target": "200,000", "by": "2026-11", "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Jeff (guest)", "claim": "SpaceX/xAI reaches 2.5-2.6 GW of compute this year", "metric": "compute capacity", "target": "2.5-2.6 GW", "by": "2026-12", "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Cristiano Amon", "claim": "AI companies want 100B-parameter models running continuously on phones", "metric": "on-device model size", "target": "100B parameters", "by": "2028", "condition": None, "entity": "Qualcomm (QCOM)"},
    {"who": "Elon Musk", "claim": "Phones shipping in 2027-2028 include chipsets for Starlink Mobile's higher-throughput spectrum", "metric": "Starlink spectrum chip support", "target": "native", "by": "2027-2028", "condition": None, "entity": "SpaceX (SPCX)"},
]

RELATIONS = [
    {"from": "Anthropic", "rel": "customer_of", "to": "SpaceX (SPCX)", "note": "~$15B/yr compute"},
    {"from": "Alphabet (GOOGL)", "rel": "customer_of", "to": "SpaceX (SPCX)", "note": "compute deal"},
    {"from": "Reflection AI", "rel": "customer_of", "to": "SpaceX (SPCX)", "note": "compute deal"},
    {"from": "Nvidia (NVDA)", "rel": "supplies", "to": "SpaceX (SPCX)", "note": "GB300s, Vera Rubin next"},
    {"from": "AT&T (T)", "rel": "competes_with", "to": "SpaceX (SPCX)", "note": "CEO doubted Starlink Mobile indoor coverage"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Elon's X posts and his X Takeover live interview, ARK's Brett Winton, a Qualcomm CEO interview, the Financial Times (OpenAI accounting), and an X account tallying the deals.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Neocloud", "def": "A GPU-rental cloud provider serving AI labs, outside the big hyperscalers."},
    {"term": "Vertical integration", "def": "Owning every stage of production, so you set your own schedule instead of waiting in a supplier's queue."},
    {"term": "Design for manufacturability", "def": "A fab's rules on what a chip design may include so it can be produced reliably."},
    {"term": "Local inference", "def": "Running an AI model on the device itself rather than in the cloud."},
]
