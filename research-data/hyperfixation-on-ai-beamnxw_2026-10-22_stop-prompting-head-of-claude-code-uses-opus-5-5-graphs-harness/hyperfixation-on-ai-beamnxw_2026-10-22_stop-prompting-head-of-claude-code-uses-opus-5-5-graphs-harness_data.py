META = {
    "title": "Stop Prompting — Head of Claude Code Uses Opus 5.5 + Graphs + Harness",
    "channel": "hyperfixation on AI | beamnxw",
    "speakers": "Boris Cherny (Head of Claude Code, Anthropic), interviewed by Mark Papermaster (CTO, AMD) — re-upload of AMD's podcast",
    "date": "2026-10-22",
    "video_url": "https://www.youtube.com/watch?v=c4kYurm0hD8",
    "thread_line": "5 threads · model as coordinator · Claude at the center, 8x output · 1 to 1,000 agents · measure the return, not the investment · trust layers and auto mode",
    "category": "dev",
    "region": "",
}

SNAPSHOT = [
    "Boris Cherny, Head of Claude Code, talks with AMD CTO Mark Papermaster on AMD's podcast; this upload's title oversells it — no graphs, and the models named are Opus 4.7/4.8 and Fable.",
    "Workflows flipped: no more deterministic step-by-step pipelines — give the model a goal, a starting point and tools, and **let it orchestrate**.",
    "At Anthropic Claude sits at the center of every process; code output per engineer is up **8x** since the start of the year, versus 50-150% at big customers.",
    "Agent adoption runs 1 → 10 → 100 → 1,000 agents per engineer; most companies sit between steps one and two, Anthropic around step three.",
    "Multi-agent and dynamic workflows are another form of **test-time compute**: more tokens, used productively, buy better results.",
    "On ROI, stop cutting the I and chase the R — give everyone freedom to experiment, then optimize what takes off.",
    "Trust comes in layers: alignment (truthfulness, no sycophancy), prompt-injection training plus a runtime classifier, and a classifier-driven **auto mode** Anthropic runs on.",
    "Six-month call: agents running for days or weeks becomes normal; by year-end Claude may build entire startups.",
]

THEMES = [
    {
        "id": "model-as-coordinator",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Practice shift",
        "status": "FROM DETERMINISTIC PIPELINES TO MODEL-DRIVEN",
        "title": "Give the model a goal and tools, not a flowchart",
        "lead": "As models got smarter, the right architecture moved from deterministic workflows that call an LLM per step to the model itself coordinating the work.",
        "bullets": [
            "Old \"agentic\" workflows were deterministic systems with an LLM call per step — \"do step one, then step two, if not two then...\" is \"just not how it works anymore.\"",
            "Claude Code didn't work well for its first ~6 months; it took off with **Opus 4 in May 2025**, and growth turned exponential from there.",
            "Early Claude Code spoon-fed context; the team backed off as the model improved.",
            "CLAUDE.md loads every session, but customers are shifting to **skills, tools and MCPs** so the model controls what it loads.",
            "Claude tag is the latest form factor: a long-running async agent you interact with like a co-worker, with a sense of when to jump in.",
            "Engineering abstraction climbed hardware → punch cards → source code → agents → loops and routines; the last two steps took two years.",
        ],
        "quote": {"text": "You give it a goal. You give it the starting point. You give it access to tools and then it will figure it out.", "cite": "— Boris Cherny"},
        "watch": None,
        "names": None,
    },
    {
        "id": "claude-at-center",
        "tags": ["dev-workflow", "career"],
        "color": "green",
        "badge": "Case study",
        "status": "8x CODE OUTPUT PER ENGINEER IN 2026",
        "title": "Put Claude at the center of every process — the computer-in-the-corner lesson",
        "lead": "Anthropic's 8x output came from removing one bottleneck at a time with Claude, the same way companies that rebuilt around computers beat those that parked one in a corner.",
        "bullets": [
            "New hires ask Claude, not a wiki or a co-worker — office address, codebase access, expense reports.",
            "Claude writes code, reviews it, does security review, brainstorms products, aggregates user feedback and triages incidents; product, design, marketing and GTM work the same way, often via Cowork.",
            "A '90s Harvard Business Review piece: companies that kept paper processes beside a computer saw no productivity gain; those that burned the filing cabinets did.",
            "Bottleneck sequence: coding → code review → GTM materials, \"one step at a time.\"",
            "The winning profile is **empirical, curious and autonomous** — a one-person-army \"CEO archetype\"; an engineering background helps but isn't essential.",
            "A leader's job is to make space to experiment without a bad performance review, and to supply business and product context.",
        ],
        "quote": {"text": "Since the beginning of this year at Anthropic we've seen an 8x increase in code output per engineer.", "cite": "— Boris Cherny"},
        "watch": "Boris runs the product and sells to these customers; the 8x and 50-150% figures are Anthropic's own, and the host's company (AMD) is an Anthropic partner.",
        "names": [
            {"name": "Anthropic", "blurb": "Claude at the center of every internal process; 8x code output per engineer", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "agent-scaling",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Framework",
        "status": "MOST COMPANIES AT STEP 1-2; ANTHROPIC AT STEP 3",
        "title": "From one agent to a thousand: the four-step adoption ladder",
        "lead": "Teams move from one agent to 10, 100 and 1,000 per engineer, and each step changes how the human works.",
        "bullets": [
            "**One agent:** single-threaded, watching it write code.",
            "**~10 agents:** once you trust it, round-robin across sessions using multiple checkouts — supported in the desktop app for Claude Code and Cowork.",
            "**Dozens to hundreds:** agents run sub-agents, nested up to **five layers** in Claude Code; Boris codes from his phone with agents running in the cloud.",
            "**Thousands:** dynamic workflows where Claude orchestrates large agent teams for migrations.",
            "Stripe did a 10,000-line Scala-to-Java migration in ~4 days instead of months; Anthropic migrated **Bun from Zig to Rust**.",
            "AMD's lead of AI software development built a Rust app over a weekend; a junior AMD engineer cracked a weeks-old chip bug with agents, converting senior engineers.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Stripe", "blurb": "~10,000-line Scala-to-Java migration in ~4 days with dynamic workflows", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "AMD (AMD)", "blurb": "weekend Rust app; junior engineer solved a chip bug with agentic processes; agentic flows help chip design keep Moore's-law pace", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "roi-return",
        "tags": ["dev-workflow", "career"],
        "color": "green",
        "badge": "Recommendation",
        "status": "TOKENS ARE TEST-TIME COMPUTE",
        "title": "Measure the return, not the investment — spend tokens to find the roofline",
        "lead": "Scaling laws now include test-time compute, so the goal is to spend more tokens productively and optimize only after a use case proves itself.",
        "bullets": [
            "Scaling laws: network size, data, compute — and now **test-time compute**; the first authors of the scaling-laws paper went on to start Anthropic.",
            "Effort levels cap how many tokens a model will spend; multi-agent orchestration is another way to turn tokens into results.",
            "Cost levers exist — plan mode, advisor models, lower effort, Sonnet or Haiku instead of Opus, evals — but the bigger lever is the R.",
            "Breakthroughs come from a new grad or a marketer in a corner of the org who was free to experiment.",
            "**Evals vs vibes:** evals for workflows repeated thousands to millions of times and for model swaps in the harness; vibes for product feel. Diverging approaches are cheap to merge — ask Claude to migrate the call sites.",
            "Humility: Boris lost a profiler-by-hand debugging race to a new teammate who asked Claude; it found the fix in 20 minutes.",
        ],
        "quote": {"text": "If you don't do the first part, you'll never find opportunity.", "cite": "— Boris Cherny"},
        "watch": None,
        "names": None,
    },
    {
        "id": "trust-layers",
        "tags": ["dev-workflow", "policy"],
        "color": "amber",
        "badge": "Vendor claim",
        "status": "ANTHROPIC RUNS ON AUTO MODE",
        "title": "Trust in layers: anti-sycophancy, injection resistance, and a classifier instead of yes-clicking",
        "lead": "Long-running agents need trust built at several layers, ending with a classifier that approves actions humans stop reading.",
        "bullets": [
            "Alignment includes truthfulness and **not being sycophantic** — Opus 4.7 and 4.8 push back on bad ideas, which builds trust.",
            "Opus 4.7, 4.8 and Fable are, per Boris, the least prompt-injectable models by **5-10x**; with a runtime classifier, real-world success is \"near zero.\"",
            "Every model ships a system card reporting resilience to prompt injection.",
            "Humans approving every command stop reading and click yes — Boris did too; security built a classifier to decide instead.",
            "Months of evals, red teaming and pen testing showed it safer; Anthropic runs on **auto mode** and recommends it to customers.",
            "AMD side (Papermaster): Moore's-law economics faded ~10 years ago; agentic flows let chip teams manage a larger design state space — \"a perfect confluence.\"",
        ],
        "quote": None,
        "watch": "Injection-resistance margins and auto-mode safety are Anthropic's own figures about its own product.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9ED", "tag": "Workflows", "title": "Replace step-by-step agent pipelines with a goal, a starting point and tools."},
    {"icon": "\U0001F4E6", "tag": "Context", "title": "Move always-loaded instructions into skills and MCPs the model pulls on demand."},
    {"icon": "\U0001F500", "tag": "Agents", "title": "Climb one rung: run parallel sessions, then let agents spawn sub-agents."},
    {"icon": "\U0001F4C8", "tag": "ROI", "title": "Fund open experimentation first; cost-optimize only the use cases that take off."},
    {"icon": "\U0001F4CF", "tag": "Evals", "title": "Write evals for high-repeat workflows and model swaps; trust vibes elsewhere."},
    {"icon": "\U0001F6E1", "tag": "Security", "title": "Swap rubber-stamp approvals for a classifier-gated auto mode."},
]

HOT_TAKES = [
    {"take": "I think by the end of this year they're going to be able to build entire businesses.", "cite": "— Boris Cherny", "why": "dated capability claim"},
    {"take": "Since the beginning of this year at Anthropic we've seen an 8x increase in code output per engineer. And this is just unheard of in the industry.", "cite": "— Boris Cherny", "why": "big self-reported number"},
    {"take": "I think some companies are actually thinking about it wrong because they're focused purely on the I part of it.", "cite": "— Boris Cherny", "why": "against cost-cutting ROI framing"},
    {"take": "Opus 4.7, Opus 4.8, Fable, these are just the least prompt injectable models in the industry by margin of I think like five or 10x.", "cite": "— Boris Cherny", "why": "competitive claim with a number"},
    {"take": "I don't think it's really essential anymore to to doing this kind of thing.", "cite": "— Boris Cherny", "why": "engineering background no longer required"},
    {"take": "I don't think we could we could continue to scale without these adjentic workflows.", "cite": "— Mark Papermaster", "why": "chipmaker CTO on dependence"},
]

CLAIMS = [
    {"who": "Boris Cherny", "claim": "By year-end Claude starts building whole products and possibly entire startups", "metric": "Claude-built startups", "target": "first entire startups", "by": "2026-12", "condition": None, "entity": "Anthropic"},
    {"who": "Boris Cherny", "claim": "Within six months running agents for days or weeks becomes normal for most engineers", "metric": "agent run length", "target": "days to weeks, normal", "by": "2027-04", "condition": None, "entity": None},
    {"who": "Boris Cherny", "claim": "Claude Code scales up to thousands of agents via dynamic workflows", "metric": "agents per workflow", "target": "thousands", "by": None, "condition": None, "entity": "Anthropic"},
]

RELATIONS = [
    {"from": "AMD (AMD)", "rel": "partners_with", "to": "Anthropic", "note": "Papermaster cites the partnership and early adoption of Anthropic practices"},
    {"from": "Stripe", "rel": "customer_of", "to": "Anthropic", "note": "used dynamic workflows for a Scala-to-Java migration"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: a 1990s Harvard Business Review article on why computers weren't raising productivity; the scaling-laws paper; Kathy Pham (Harvard) from a previous episode on AI governance.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Test-time compute", "def": "Tokens spent at inference; more of it, used well, yields better answers."},
    {"term": "Dynamic workflows", "def": "Claude orchestrating large teams of agents on big jobs like codebase migrations."},
    {"term": "Sub-agents", "def": "Agents started by another agent; Claude Code supports nesting up to five layers."},
    {"term": "Auto mode", "def": "Permission mode where a classifier, not a human click, approves agent actions."},
    {"term": "Effort level", "def": "A setting capping how many tokens the model will spend on a problem."},
]
