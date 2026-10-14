META = {
    "title": "Can Open Models Keep Up With OpenAI and Anthropic? | Nathan Lambert",
    "channel": "a16z",
    "speakers": "Nathan Lambert (Trillium founder, ex-AI2) · Lisha Li (a16z partner, host)",
    "date": "2026-10-14",
    "video_url": "https://www.youtube.com/watch?v=BKuK0M6oDTI",
    "thread_line": "6 threads · capital tiers · distillation · open economy · data & RL environments · Trillium & open RSI · pre-training and takeoff limits",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Model progress = three forms of capital: **compute, data, talent**. OpenAI and Anthropic have the most and are willing to spend \"egregious amounts\" on bets others call impossible.",
    "Chinese labs are equal on talent and short on compute: an average OpenAI researcher reportedly has **5,000 H100 equivalents** on tap — a figure that floors top Chinese pre-training researchers.",
    "Lambert thinks distillation buys Chinese labs only **a few months**; the public literature shows it's hard to map onto today's RL-heavy post-training.",
    "Open and closed run on different exponentials: closed labs hit high-value markets first (coding went from zero to **$100B** in revenue); the open economy is slower but ends with real ownership of weights.",
    "Frontier progress outside math and code is mostly **bought data and RL environments** — billions of dollars of it, much of it flawed and prone to reward hacking.",
    "Lambert launched **Trillium**, a nonprofit lab releasing open RL environments and publicly documenting how AI automates AI research, to take the mystique out of RSI.",
    "No fast takeoff: scaling laws need exponential compute for linear gains. The thing that worries him is how little society is preparing, cybersecurity first.",
]

THEMES = [
    {
        "id": "capital-tiers",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "FRONTIER = OPENAI + ANTHROPIC; OPEN = NEAR-FRONTIER TIER",
        "title": "Compute, data and talent decide the frontier, and open weights settle one tier below it",
        "lead": "Closed labs lead because they hold the most capital and make the earliest bets; open models fill a lower-margin near-frontier tier.",
        "bullets": [
            "OpenAI 'kickstarted the reasoning model revolution' with the inference-scaling-laws plot; Anthropic's long coding focus paid off in the **Claude Code** explosion.",
            "Making the org chart work is the hard part: labs need full bottom-up resets. **Meta** did one and is 'on a positive trajectory again'.",
            "Chinese labs release open weights as distribution: an API sold from China would leave Moonshot AI or Zhipu unknown. A 'very practical decision', not government-driven.",
            "Expected tiers: best closed models command the best margins; open near-frontier models serve markets like private enterprise data.",
            "Fast following gets easier through the data economy: data vendors built for OpenAI/Anthropic resell the same datasets to everyone after the contractual period.",
            "He predicted consolidation two years ago; M&A is only now picking up and open-model companies lasted 'much longer than I thought'.",
        ],
        "quote": {"text": "if somebody wants to work at the frontier of AI I mostly tell them to work at anthropic and open AI which is the easiest bet", "cite": "— Nathan Lambert"},
        "watch": "Lambert runs an open-model nonprofit and Li invests in both frontier labs and startups, so both have a stake in the 'many winners' outcome.",
        "names": [
            {"name": "OpenAI", "blurb": "Frontier leader; created the reasoning paradigm; willing to spend on 'impossible' bets", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Anthropic", "blurb": "Frontier leader; coding focus led to the Claude Code revenue explosion", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Meta (META)", "blurb": "Did a full org reset, 'on a positive trajectory again'", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Moonshot AI", "blurb": "Chinese lab that open-sources to get known in the US market", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "distillation",
        "tags": ["geopolitics", "policy", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "DISTILLATION WORTH 'A FEW MONTHS', WITH WIDE ERROR BARS",
        "title": "China's real gap is compute, not talent; distillation is a smaller lever than the discourse claims",
        "lead": "Lambert estimates distillation buys Chinese labs a few months and argues policy against it would do more harm than good.",
        "bullets": [
            "Li: the open-to-frontier lag has shrunk to roughly **2-3 months**, pushing labs to hide top models behind first-party products.",
            "Talent is equal: '20 to 30 companies' build good models. Compute is the gap, and distillation is a way to spend money for compute-equivalent outputs.",
            "The SFT/RLHF era let you train on a strong model's completions; the RL-environment era is hard to map onto that. Open post-training builders are still stuck using an **outdated Qwen** teacher.",
            "What gives him pause: Claude proxies in China with many accounts, Kimi serving Claude in its products, Chinese firms using OpenAI/Anthropic outputs 'at a vast scale'.",
            "Visible reasoning tokens in APIs can't be protected; product-only or enterprise-agreement access would make it 'way harder'. He opposes KYC and government action over a **terms-of-service** breach.",
            "Li's steelman for the labs: a **flywheel** of parked compute, then revenue, then fresh capital, ending in an IPO. Fast open catch-up threatens it, and a weak OpenAI/Anthropic IPO is 'bad for everyone else'.",
            "Nvidia's Jensen Huang, cited by Li: distilling rivals' products is 'called competition'.",
        ],
        "quote": {"text": "I just think like you're going to cause more harm than good if you do anything about distillation because they're not going to stop.", "cite": "— Nathan Lambert"},
        "watch": "Lambert says the error bars are 'very big'; his few-months estimate rests on open literature, not on what Chinese labs do internally.",
        "names": [
            {"name": "Moonshot AI", "blurb": "Kimi was serving Claude inside its products, which raises distillation questions", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Jensen Huang's 'that's called competition' framing of distillation", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "open-economy",
        "tags": ["software", "ai-infra"],
        "color": "amber",
        "badge": "Mixed",
        "status": "OPEN ECONOMY = SLOWER, BUT ENDS IN OWNED WEIGHTS",
        "title": "Closed labs win the fast markets; the open-model economy builds slower around fine-tunes and private data",
        "lead": "Frontier labs will serve the cheapest intelligence per watt where demand is highest, but they can't do everything, which leaves room for many winners.",
        "bullets": [
            "Coding is 'the story of the year': revenue went from zero to **$100B** and is likely to grow.",
            "The open stack is split across builders, inference companies and post-training companies, so customer signal doesn't flow back to the model builder and economies of scale are missing.",
            "Enterprises with private data go to firms like **Thinking Machines** or Prime Intellect to fine-tune, and end up with weights they own, no terms and conditions, on their own hardware.",
            "Li's evidence: Decagon and Harvey-style post-training-as-a-service works on Kimi K3 or GLM. **Cursor's** SQLite rewrite showed Composer + a frontier planner matched two frontier models at far lower cost.",
            "Harnesses reached equilibrium: closed labs didn't become 'Apple' because users run models in many harnesses. Agent swarms (a 'coordination system', not a harness) will come from OpenAI/Anthropic first, then open labs copy the shape.",
            "Lab secrecy is weaker than labs think. Ideas travel 'one beer' in Silicon Valley; **SSI** is the impressive exception.",
        ],
        "quote": None,
        "watch": "Lambert: 'I don't really know what's going to happen... it's too early to know' whether cheap open models eat into the fast-takeoff market.",
        "names": [
            {"name": "Thinking Machines", "blurb": "Enterprise fine-tuning destination; post-training business model suits open weights", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Prime Intellect", "blurb": "Destination for enterprise fine-tuning of open models", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Cursor", "blurb": "SQLite rewrite: Composer as executor was as good as and far cheaper than a two-frontier-model setup", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Decagon", "blurb": "Startup fine-tuning open models (Li)", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Harvey", "blurb": "Startup fine-tuning open models (Li)", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SSI", "blurb": "The one lab that actually keeps secrets", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "data-environments",
        "tags": ["ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "BILLIONS ON RL ENVIRONMENTS, QUALITY STILL LOW",
        "title": "Outside math and code, frontier progress is bought data and RL environments, much of it flawed",
        "lead": "In non-verifiable domains (biology, healthcare, legal) labs climb by buying data, and that will take years and a lot of capital per sector.",
        "bullets": [
            "OpenAI started hiring and buying robotics data **six to eight months** before its model got good at robotics; they'll call it 'generalization magic'. Li's counterpoint: it may come from computer use (spatial reasoning).",
            "Math is the exception: models beat specialized systems by scaling general reasoning, without specialized datasets.",
            "Research budgets on environments run to **billions of dollars**: 'these numbers are crazy', but labs see the training signal.",
            "Corner-cutting vendors cause **reward hacking**, e.g. a test file left empty so the model games the reward. Vendors spend more time on world building and revenue than on model behavior.",
            "Weak opsec: overseas contractors working through intermediaries upload data to GitHub. Chinese labs buy the same RL environment about six months later.",
            "Serving costs: if big models halve in price every **8 months for 3 years**, cost hits ~1% in about four years. Open question: Jevons paradox margins, or shrinking revenue?",
        ],
        "quote": {"text": "the numbers are too big, the quality is bad, but on the other hand, the labs are improving very fast and know how to onboard it.", "cite": "— Nathan Lambert"},
        "watch": "Lambert expects the data industry to take 'a few years' to move to higher-quality, higher-ROI suppliers; labs are pulling some of it in-house to avoid signal leaks.",
        "names": [
            {"name": "OpenAI", "blurb": "Bought robotics data months before its robotics gains; drastic price cuts", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "trillium",
        "tags": ["ai-infra", "policy"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "TRILLIUM LAUNCHED · NONPROFIT OPEN-RESEARCH LAB",
        "title": "Trillium: open RL environments and a public log of how AI automates AI research",
        "lead": "Lambert's nonprofit releases high-leverage open environments and documents its own AI-automated research so policymakers can see what models actually get stuck on.",
        "bullets": [
            "Model: **T-Max** terminal-task data (advised with UW/AI2 and Hamish Ivison). Fully synthetic: frontier-model prompts, diversity, rollouts to find and remove buggy tasks.",
            "The incentive problem: 'you could probably sell this data for a million dollars'. Founders chase '$100 million' returns within five months of starting up.",
            "Named after the trillium, a spring ephemeral flower that blooms before the canopy and spreads nutrients for the season's growth.",
            "Open RSI log: an open SFT/mid-training stack (SkyRL, Miles), published tasks, configs and trajectories, with check-ins every six months. EleutherAI, Hugging Face and Marin (Stanford/Open Athena) could do the same.",
            "Academia can't spend '15%' of a professor's time and 40% of a grad student's on documentation, so nonprofits fill that gap. A separate academic 'Open RSI' effort launched the week before.",
            "Why he left AI2: its post-training 'was honestly falling behind' because cycle time was too slow. The open bar is low, so little capital buys big compounding gains.",
            "New problem: AI-generated fake research results in GitHub issues. Breaking into AI still takes months of hand-written code and **6-18 months** to get noticed.",
        ],
        "quote": {"text": "I think this pays so much dividends to everybody that stands to profit more than I do.", "cite": "— Nathan Lambert"},
        "watch": "Lambert is the founder; this is his own launch pitch.",
        "names": [
            {"name": "Hugging Face", "blurb": "Named as another org that could openly document RSI", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "pretraining-takeoff",
        "tags": ["ai-infra", "policy"],
        "color": "gray",
        "badge": "Speculative",
        "status": "NO FAST TAKEOFF; PREPARATION IS THE GAP",
        "title": "Pre-training is cheaper than people think, and RSI is capped by exponential compute",
        "lead": "A solid base model doesn't need a billion dollars, and recursive self-improvement still faces exponential compute for linear performance.",
        "bullets": [
            "Pre-training tools are accessible (a 'pre-training ladder' to test whether ideas scale). New startups fork open tools like **Megatron** and never push changes upstream.",
            "The hard part is landing a first model good enough to fund the next raise. Thinking Machines shipped Inkling, said openly it wasn't the best, and is now on its second model plus Tinker.",
            "Rumor: **Meta** will release a new open-weight model again. Zuckerberg's Llama 3 'open is the path forward' post was 'the best blog post on this'.",
            "Pre-training co-evolves with inference: a working sparse-attention architecture can make a 100,000-token generation **40%** faster. Mid/post-training is 'the wild west' by comparison.",
            "Models will be strong at cutting serving costs and tweaking architecture, but not at solving knowledge work ('make better PowerPoints').",
            "Takeoff: human bottlenecks; Claude system cards say a fast takeoff would take ~10x more progress. Math (Navier-Stokes) suits this shape of intelligence best; a post-transformer discovery would be worth updating on.",
            "His bigger worry: 'pretty much non-existing' preparation in public cybersecurity for risks that diffuse from closed to open labs.",
        ],
        "quote": {"text": "I don't think that it's necessarily going to be this like fast takeoff when the models build themselves. It's human human bottlenecks.", "cite": "— Nathan Lambert"},
        "watch": "Lambert: 'we don't know exactly what it'll go from here'. Li says she'll send him lab defectors worried about exactly this.",
        "names": [
            {"name": "Meta (META)", "blurb": "Rumored to release a new open-weight model again", "stance": "WATCHING", "conviction": "Low", "horizon": None},
            {"name": "Thinking Machines", "blurb": "Inkling, then a second model, plus Tinker; 'off the ground'", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F3AF", "tag": "AI industry", "title": "Value frontier labs on compute, data and talent capital plus org execution, not model benchmarks alone"},
    {"icon": "\U0001F1E8\U0001F1F3", "tag": "Geopolitics", "title": "Read Chinese open-weight releases as distribution strategy; watch compute access, not talent, as their limiter"},
    {"icon": "\U0001F4BC", "tag": "Startups", "title": "Bet on fine-tuned open models where private data and cost matter; leave the fastest-moving markets to closed labs"},
    {"icon": "\U0001F9EA", "tag": "Data", "title": "Treat the RL-environment vendor boom as capital-heavy and quality-poor; expect winners to consolidate over years"},
    {"icon": "\U0001F6E1", "tag": "Policy", "title": "Put risk effort into cybersecurity preparation, not fast-takeoff scenarios"},
]

HOT_TAKES = [
    {"take": "To say that China is anything but equal in talent is going to you're going to have a hard time", "cite": "— Nathan Lambert", "why": "contrarian to 'US talent edge' narrative"},
    {"take": "I don't know why you should get the government involved in a terms of service violation.", "cite": "— Nathan Lambert", "why": "against national-security distillation policy"},
    {"take": "I think every Chinese lab has a team that knows those sorts of things.", "cite": "— Nathan Lambert", "why": "claims universal reasoning-trace extraction capability"},
    {"take": "you don't have to spend a billion dollars to get a very good base model.", "cite": "— Nathan Lambert", "why": "pre-training cost dismissal, numeric"},
    {"take": "the security at these labs in terms of information is not as high as they think.", "cite": "— Nathan Lambert", "why": "dismisses frontier secrecy moat"},
    {"take": "I don't think that it's necessarily going to be this like fast takeoff when the models build themselves.", "cite": "— Nathan Lambert", "why": "anti fast-takeoff"},
]

CLAIMS = [
    {"who": "Nathan Lambert", "claim": "Distillation gives Chinese labs an advantage of only a few months", "metric": "distillation catch-up gain", "target": "a few months", "by": None, "condition": None, "entity": None},
    {"who": "Lisha Li", "claim": "Compute and power scarcity stays the bottleneck", "metric": "compute/power scarcity", "target": "bottleneck", "by": "2028", "condition": None, "entity": None},
    {"who": "Nathan Lambert", "claim": "Large frontier models halve in price every 8 months over 3 years, reaching ~1% of cost in about four years", "metric": "model serving price", "target": "~1% of current cost", "by": "~4 years", "condition": "if the 2x-every-8-months trend holds", "entity": None},
    {"who": "Nathan Lambert", "claim": "The data industry transitions to higher-quality, higher-ROI suppliers", "metric": "data vendor quality", "target": "consolidation into winners", "by": "a few years", "condition": None, "entity": None},
    {"who": "Nathan Lambert", "claim": "OpenAI and Anthropic ship agent-swarm coordination systems first; open-model companies follow once the shape is known", "metric": "agent swarm harness", "target": "closed first, open follows", "by": None, "condition": None, "entity": None},
    {"who": "Nathan Lambert", "claim": "Meta is rumored to release a new open-weight model", "metric": "open-weight release", "target": "new model", "by": None, "condition": None, "entity": "Meta (META)"},
    {"who": "Nathan Lambert", "claim": "A fast takeoff would require ~10x more progress than current AI-assisted research gives, per Claude system cards", "metric": "AI research speedup for fast takeoff", "target": "~10x", "by": None, "condition": None, "entity": "Anthropic"},
    {"who": "Nathan Lambert", "claim": "Coding revenue, at ~$100B, is likely to keep growing", "metric": "AI coding revenue", "target": ">$100B", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Moonshot AI", "rel": "customer_of", "to": "Anthropic", "note": "Kimi was serving Claude in its products"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: a prominent paper on stealing reasoning traces from closed models; Claude system cards; Cursor's SQLite-rewrite write-up; Zuckerberg's Llama 3 open-source post; Jensen Huang on distillation; Lambert's own book code.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Distillation", "def": "Training a model on a stronger model's outputs to borrow its capability without the compute."},
    {"term": "SFT", "def": "Supervised fine-tuning: next-token training on curated or model-generated completions."},
    {"term": "RL environment", "def": "A simulated task world with a reward that models act in during reinforcement-learning post-training."},
    {"term": "Reward hacking", "def": "A model maximizing reward through a flaw in the environment instead of solving the task."},
    {"term": "Mid-training", "def": "Stage between pre-training and post-training that seeds reasoning behaviors before RL."},
    {"term": "RSI", "def": "Recursive self-improvement: AI systems accelerating the research that builds better AI."},
    {"term": "Jevons paradox", "def": "Cheaper units drive enough extra demand that total spend rises."},
    {"term": "Pre-training ladder", "def": "A series of scaled-up runs used to test whether an idea holds at larger scale."},
]
