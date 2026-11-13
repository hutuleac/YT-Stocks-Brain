META = {
    "title": "Recursive self-improvement has started",
    "channel": "Dwarkesh Patel",
    "speakers": "Dwarkesh Patel",
    "date": "2026-11-13",
    "video_url": "https://www.youtube.com/watch?v=1NHPDzpfR6Y",
    "thread_line": "5 threads · AI already speeding AI · median 2028 · spark vs software-only singularity · transfer to messy domains · verifiable proxies + bottlenecks",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Dwarkesh has reversed his view of the last year and a half: AIs as good as the best humans at AI research are a couple of years away, possibly months. His median is **2028**.",
    "Evidence it has started: METR found Anthropic's progress on well-scoped tasks has **doubled** in a year, mostly from AI-driven R&D, and Claude now leads 26% of Anthropic's AI R&D, up from under 1% in February.",
    "Math went from failing four-digit addition in 2023 to OpenAI solving a Millennium Prize problem in **88 hours**; he argues AI research is similarly verifiable.",
    "After automation, it's a coin flip between a **software-only singularity** and a \"spark\" that compresses 3-6 years of progress into one year, about GPT-3.5 to GPT-6 Astra.",
    "Expect AIs at least as good as the best experts in every field by **2030**, plausibly next year; he gives at least 25% to AI research not being automated until after 2032.",
    "Continual learning, his old objection, may be solved by scaling in-context learning or by the automated researchers themselves.",
]

THEMES = [
    {
        "id": "rsi-started",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "UNDERWAY AT THE FRONTIER",
        "title": "AI is already speeding up AI research",
        "lead": "Lab data from the last few months shows AI doing a growing share of frontier AI R&D.",
        "bullets": [
            "METR spent three months inside Anthropic: progress on well-scoped tasks is **2x** a year ago, with a majority of the acceleration likely from Anthropic's use of AI for R&D.",
            "OpenAI's heaviest 10% of researchers went from about $1,000 a day of internal coding agents at the start of summer to over **$7,000 a day** by end of August.",
            "Anthropic says Claude now leads **26%** of its AI R&D work, up from under 1% in February.",
            "Math timeline: no reliable four-digit addition (2023), barely any high-school competition problems (2024), IMO gold (2025), niche open problems this year, then a Millennium Prize problem in 88 hours a month ago.",
            "Toby Ord says AI shows little ability to ask powerful questions; Dwarkesh's reply is that it solved a Millennium Prize problem anyway, and ML research cares about recipes that work, not theory.",
            "The transformer was a combination of known ideas plus half a dozen tweaks found through many experiments, which he argues \"Claude 7\" could have found (via Sholto Douglas and Chris Olah).",
        ],
        "quote": {"text": "AI research is actually surprisingly similar to the kind of mathematical progress which current AIs are disproportionately good at", "cite": "— Dwarkesh Patel"},
        "watch": None,
        "names": [
            {"name": "Anthropic", "blurb": "METR-measured 2x progress; Claude leads 26% of R&D", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "OpenAI", "blurb": "Agent spend per heavy researcher $1K to $7K a day; Millennium Prize problem", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "timeline",
        "tags": ["ai-infra"],
        "color": "amber",
        "badge": "Forecast",
        "status": "MEDIAN 2028",
        "title": "When AI matches the best human AI researchers",
        "lead": "His median is 2028, with real odds on 2027 and a quarter chance of after 2032.",
        "bullets": [
            "Median **2028**, assuming labs go full steam and aren't slowed by themselves or a government.",
            "In every verifiable domain (competitive programming, well-scoped math), AI went from worse than most humans to better than the best within a few years.",
            "2027 is plausible: some top forecasters expect it next year, and a former guest notes in a blog post that a smooth near-doubling naively implies extreme superintelligence within a year.",
            "At least **25%** chance it doesn't happen until after 2032, mainly if continual learning stays unsolved.",
            "Speedups: AIs already work about 10x human speed around the clock (about **50x** more work per week); about 80% of a lab's algorithmic progress comes from its top 50 researchers, and every copy would be top-tier.",
            "Countervailing trend: labs already quadruple R&D compute and double headcount each year just to keep the same rate.",
        ],
        "quote": {"text": "we should not be surprised and we should be ready for a world in which we get to this milestone next year.", "cite": "— Dwarkesh Patel"},
        "watch": "His own uncertainty about simple takeoff modeling is why his median isn't 2027.",
        "names": None,
    },
    {
        "id": "spark-vs-singularity",
        "tags": ["ai-infra", "semis"],
        "color": "gray",
        "badge": "Speculative",
        "status": "50/50",
        "title": "Spark or software-only singularity",
        "lead": "Whether AI improves faster than ideas get harder to find decides months versus years to superintelligence.",
        "bullets": [
            "Software-only singularity: without more compute, the swarm builds smarter versions of itself until it **scrapes the physical limits** of current chips within months.",
            "Spark: about **3-6 years** of progress in one year, then a slowdown until more compute arrives, still a GPT-3.5 to GPT-6 Astra jump in 12 months.",
            "A post-spark mind would out-design Nvidia on accelerators, out-earn Citadel and Jane Street with equal market access, and find a room-temperature superconductor.",
            "Global AI compute has grown about **3x a year** for five years; post-spark AIs would design chips and fabs and teleoperate robots to build them.",
            "Top human performance in all domains within months of development: still 2028-2029 in his median case.",
        ],
        "quote": {"text": "I think it's basically a coin toss.", "cite": "— Dwarkesh Patel"},
        "watch": None,
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "A post-spark AI would out-design it on accelerators", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Citadel, Jane Street", "blurb": "Benchmarks a superhuman trader would beat", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "transfer",
        "tags": ["ai-infra", "career"],
        "color": "gray",
        "badge": "Speculative",
        "status": "ARGUMENT",
        "title": "From verifiable tasks to messy real-world skill",
        "lead": "Scaled RL builds general learning skill, so AIs ramp quickly in hard-to-verify domains like business, law and trading.",
        "bullets": [
            "During RSI, AIs will build **tens of thousands** of times more RL environments, like simulated economies of millions of AIs where one is told to co-found a company.",
            "Backtest training: rediscover general relativity from data before 1700, or predict the Cuban missile crisis from every newspaper up to 1962.",
            "Transfer is already visible: Claude Code or Codex orient in unseen projects, and new models help with non-code research.",
            "Evolution, with a crude verifier, built a general learner; labs optimize transfer deliberately, with held-out hard tasks.",
            "Young people ramp fast (Napoleon by 27, Rockefeller running a top refinery by 25), and an AI CEO could read every company email and interview every employee in parallel on day one.",
        ],
        "quote": {"text": "There's no reason to think that humans are at the ceiling of learning quickly from experience.", "cite": "— Dwarkesh Patel"},
        "watch": None,
        "names": None,
    },
    {
        "id": "proxies-bottlenecks",
        "tags": ["ai-infra", "dev-workflow"],
        "color": "amber",
        "badge": "Contested",
        "status": "OBJECTIONS ANSWERED",
        "title": "Why AI research is verifiable, and the bottlenecks",
        "lead": "Pre-training, post-training and inference all have measurable proxies; continual learning, taste, data and compute slow but don't stop RSI.",
        "bullets": [
            "Pre-training: RL a model to minimize compute to reach a fixed loss, and even train taste (predict whether a gain at 100M parameters holds at 10B).",
            "Magic says it matched DeepSeek V4 Pro-class open models with half of GPT-3's compute, about **$500,000** today. Smaller models also tighten the loop, so giant runs get obsoleted mid-flight.",
            "Post-training: measure RL efficiency, on-the-fly learning (ByteDance's EdgeBench), and Anthropic's internal benchmark of about **500** real research problems solved this year.",
            "Continual learning, his main doubt last December, may be solved by months-long effective context or by AIs themselves, \"cartwheeling\" next to Usain Bolt.",
            "Data: with Jerry Han (Princeton) he found data improvements gave over **3x** the algorithmic progress of model improvements in pre-training; DeepSeek credits synthesized data and environments with essentially all of its RL gains.",
            "Compute: if labs keep quadrupling, by end of 2027 OpenAI could give 10,000 agents a GPT-3-size run each per day. The 2017 transformer took 3 days on 8 P100s (about $50 today); GPT-4's loss was predicted from 10,000x smaller models.",
        ],
        "quote": {"text": "The gods above must work from the same principles as the ants below.", "cite": "— Dwarkesh Patel, quoting an AI researcher"},
        "watch": None,
        "names": [
            {"name": "DeepSeek", "blurb": "Paper: data and environment synthesis drove its RL gains", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "ByteDance", "blurb": "Released an on-the-fly learning benchmark", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C5", "tag": "AI timelines", "title": "Plan for AI matching top AI researchers by 2028, and keep a 2027 contingency."},
    {"icon": "\U0001F4CA", "tag": "AI", "title": "Track lab R&D share metrics like Claude's 26%; they are the leading indicator of RSI."},
    {"icon": "⚡", "tag": "Compute", "title": "Watch compute growth: it decides whether a spark keeps going after the software gains slow."},
    {"icon": "\U0001F9E0", "tag": "Careers", "title": "Expect messy, experience-based fields to fall within months of deployment, not decades."},
]

HOT_TAKES = [
    {"take": "we're only a couple years away and possibly only a couple months away from AIs that are as good as the best humans at AI research.", "cite": "— Dwarkesh Patel", "why": "timeline call"},
    {"take": "by 2030 and plausibly as early as next year, we'll have AIs that are at least as good as the best human experts in every field.", "cite": "— Dwarkesh Patel", "why": "dated"},
    {"take": "If I had to pick my median year for when automated researchers will be as good as the very best human AI researchers at doing AI research, I'd guess 2028.", "cite": "— Dwarkesh Patel", "why": "dated"},
    {"take": "It would make more money than the current human versions of Citadel and Jane Street if it was given equal access to the market.", "cite": "— Dwarkesh Patel", "why": "bold"},
]

CLAIMS = [
    {"who": "Dwarkesh Patel", "claim": "Automated researchers match the best human AI researchers", "metric": "AI research ability", "target": "best human level", "by": "2028", "condition": "labs not slowed", "entity": None},
    {"who": "Dwarkesh Patel", "claim": "At least 25% chance top AI research isn't automated until after 2032", "metric": "probability", "target": ">=25%", "by": "2032", "condition": None, "entity": None},
    {"who": "Dwarkesh Patel", "claim": "AIs at least as good as the best human experts in every field", "metric": "expert-level AI", "target": "all fields", "by": "2030", "condition": None, "entity": None},
    {"who": "Dwarkesh Patel", "claim": "50% chance of a software-only singularity versus a 3-6 year spark after AI research is automated", "metric": "probability", "target": "50%", "by": None, "condition": "AI research automated", "entity": None},
    {"who": "Dwarkesh Patel", "claim": "OpenAI could give 10,000 agents a GPT-3-size training run each per day", "metric": "compute per agent", "target": "GPT-3-size run per day", "by": "2027-12", "condition": "labs keep quadrupling compute", "entity": "OpenAI"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: METR, OpenAI and Anthropic uplift posts, Toby Ord's essay, Chris Olah, Sholto Douglas, 3Blue1Brown's compression video, the GPT-4 paper, and a DeepSeek RL paper.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "RSI", "def": "Recursive self-improvement: AI doing the research that makes better AI."},
    {"term": "Software-only singularity", "def": "AI improving faster than ideas get harder to find, reaching superintelligence on fixed compute."},
    {"term": "Spark", "def": "Dwarkesh's term for a one-year burst of 3-6 years of progress that then slows until more compute arrives."},
    {"term": "Sample efficiency", "def": "How much data a model needs to learn a capability; the flip side of online learning."},
    {"term": "muP", "def": "A parameterization that lets small models predict optimal hyperparameters for a 100x larger run."},
]
