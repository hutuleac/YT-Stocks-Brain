META = {
    "title": "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering — Frank Coyle, UC Berkeley",
    "channel": "AI Engineer",
    "speakers": "Frank Coyle",
    "date": "2026-08-08",
    "video_url": "https://www.youtube.com/watch?v=Z-c11pV_uvU",
    "thread_line": "5 threads · exam structure · stop-reason loops · specialized sub-agents · context isolation · CI and batch",
    "category": "dev",
    "region": "",
}

SNAPSHOT = [
    "Frank Coyle (Berkeley CS, 30+ years teaching) uses Anthropic's **Claude Certified Architect (CCA)** exam as a map of what agentic engineering will demand.",
    "The exam launched in March 2026: scenario-based, timed, proctored, **$99** for individuals, one attempt every 6 months.",
    "Five domains: agentic architecture **27%**, Claude Code config/workflow **20%**, plus prompt engineering and structured output, tool design/MCP integration, and context management/reliability.",
    "Exam draws **4 of 6** production scenarios; Coyle's method is to learn each scenario's *anti-pattern* first, because knowing what not to do points to the right answer.",
    "Core pattern: loop on the model's `stop_reason`; the LLM never executes tools, your code does.",
    "Core discipline: specialized agents with one or two tools, isolated context, compaction past ~150k tokens.",
    "Loops are not new: Böhm-Jacopini (1966) showed sequence + conditionals + loop is Turing complete; agents add the loop to prompts.",
]

THEMES = [
    {
        "id": "exam-structure",
        "tags": ["career", "dev-workflow"],
        "color": "green",
        "badge": "Recommendation",
        "status": "RELEASED MARCH 2026",
        "title": "The CCA exam is a free syllabus for agentic engineering, whether or not you sit it",
        "lead": "Anthropic knows how people actually use its system, so the exam's blueprint shows where agent projects break.",
        "bullets": [
            "Released March 2026; scenario-based, timed, proctored; open to companies in the Anthropic ecosystem, individuals pay **$99** and can retake every 6 months.",
            "Multiple choice, but built on realistic constraints rather than trivia.",
            "Domain weights: agentic architecture 27%, Claude Code configuration/workflow 20%; the rest covers prompt engineering with structured JSON output, tool design and Model Context Protocol integration, and context management/reliability.",
            "Six production scenarios are published; each exam randomly picks four and centers all questions on them.",
            "Coyle's frame: design patterns arrived with 1990s object-oriented programming; agents now have patterns *and* anti-patterns, and anti-patterns are the shortcut to right answers.",
            "His motivation: computer science is no longer a guaranteed pathway to a job, so he is hunting for ways to ready students for agentic AI.",
        ],
        "quote": {"text": "Nothing is a mistake. There's no win and no fail. There's only make.", "cite": "— Sister Corita Kent, quoted by Frank Coyle"},
        "watch": None,
        "names": None,
    },
    {
        "id": "stop-reason-loop",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Structural pattern",
        "status": "SCENARIO 1: CUSTOMER SUPPORT AGENT",
        "title": "Loop on stop_reason; the LLM never runs your tools",
        "lead": "The anti-pattern is firing the agent once and using whatever comes back; the pattern is a while-true loop gated by the stop reason.",
        "bullets": [
            "Loops are the hot idea (Boris Cherny: his job is writing loops; Peter Steinberger: he designs loops that prompt agents), but Coyle says they are not new.",
            "**Böhm and Jacopini, 1966:** sequence, if-then conditionals and a loop are all a language needs to be Turing complete; agents finally add the loop to prompts and conditionals.",
            "The LLM is a probabilistic next-word predictor that can only talk back: it extracts tool parameters, your code executes the tool.",
            "Loop shape: call model with messages, read `stop_reason`; if `tool_use`, run the tool, feed the result back, continue; otherwise end the loop.",
            "After the loop, check confidence: keep the answer or escalate to a human (human-in-the-loop point).",
            "Always check the stop reason: running out of tokens also stops the model, and the partial response needs action.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "specialized-agents",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Structural pattern",
        "status": "SCENARIO 3: MULTI-AGENT RESEARCH",
        "title": "One agent loaded with every tool is the anti-pattern; give each agent one job and only a slice of context",
        "lead": "Specialize, don't overload: a carpenter who also brings plumbing and electrical tools is not the pro you want.",
        "bullets": [
            "Questions to settle: hub-and-spoke layout, who is the orchestrator, how much each agent should know.",
            "Functional-programming echo: functions do one thing; agents get one job with **one or two tools**.",
            "Context means tokens, tokens mean money, and more context confuses the model: a million-token window is not a reason to fill it.",
            "Critic example: pass only the claim and the evidence, not the reasoning that produced the claim.",
            "Reason: agents that collaborate drift into **groupthink** and converge on one idea, like a party where everyone wants pizza.",
            "Each agent gets only its own slice.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "context-isolation",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Structural pattern",
        "status": "SCENARIO 4: DEVELOPER PRODUCTIVITY",
        "title": "Isolate subtask output and compact long sessions",
        "lead": "Anti-patterns: dump every subtask's full output into the main thread, and let context grow unbounded.",
        "bullets": [
            "Same lesson as multithreaded programming: threads sharing memory force locks and synchronization; keep threads, and agents, independent.",
            "Pattern: **context fork** a log-scanning agent into a separate thread; only its summary of errors returns to the main context.",
            "Check the token count and set a limit: past about **150,000 tokens**, run a compact.",
            "Anthropic's compaction internals aren't known to Coyle; compaction exists but he doesn't know how it is implemented.",
            "Hierarchical `CLAUDE.md` (scenario 2, code generation): Anthropic recommends rules at the project top level, in the project folder, and within directories.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "ci-and-batch",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Recommendation",
        "status": "SCENARIO 5: CLAUDE CODE IN CI",
        "title": "No interactive mode in a pipeline; use batch for 50% cheaper tokens",
        "lead": "Interactive mode makes Claude stop and ask permission, which breaks a pipeline; configure it to run straight through.",
        "bullets": [
            "Anti-pattern: always interactive modes in a CI pipeline.",
            "Batch mode: submit prompts as a batch for **50%** fewer token cost, with results promised within at least 24 hours.",
            "Use it for work that can wait: overnight, vacation, a day off.",
            "Final scenario thread: patterns for structured data extraction.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4DD", "tag": "Careers", "title": "Read the CCA exam domains as a skills checklist, even if you never sit the $99 exam."},
    {"icon": "\U0001F501", "tag": "Agents", "title": "Gate every agent loop on stop_reason; handle tool_use, end, and out-of-tokens separately."},
    {"icon": "\U0001F9F0", "tag": "Agents", "title": "Split overloaded agents into single-purpose ones with one or two tools each."},
    {"icon": "\U0001F9EA", "tag": "Context", "title": "Fork noisy subtasks and return only a summary; compact past ~150k tokens."},
    {"icon": "⚙️", "tag": "CI", "title": "Run Claude Code non-interactively in pipelines and push delay-tolerant work to batch for half the cost."},
    {"icon": "\U0001F6A7", "tag": "Learning", "title": "Study anti-patterns first: what not to do narrows the right answer."},
]

HOT_TAKES = [
    {"take": "Loops are the new big thing, right? Well, no, they're not.", "cite": "— Frank Coyle", "why": "pushes back on the loop-hype from Cherny and Steinberger"},
    {"take": "Computer science is no longer the magic pathway to a job.", "cite": "— Frank Coyle", "why": "career claim from a long-time CS professor"},
    {"take": "Even though, oh, a million token context window, I can put everything in there. No, no, don't put everything in there.", "cite": "— Frank Coyle", "why": "contradicts the big-context habit"},
]

CLAIMS = [
    {"who": "Frank Coyle", "claim": "Running prompts through batch mode costs 50% fewer tokens with results promised within 24 hours", "metric": "batch token cost", "target": "-50%", "by": None, "condition": None, "entity": None},
    {"who": "Frank Coyle", "claim": "Compaction should run once context passes about 150,000 tokens", "metric": "compaction threshold", "target": "150,000 tokens", "by": None, "condition": None, "entity": None},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Boris Cherny and Peter Steinberger (the loops-over-code quotes), Böhm and Jacopini (1966), Thomas Edison and Sister Corita Kent (quotes), and a free conference booklet by Sam Bagwell whose company offers custom context-compression logic via an extendable base class (page 32).", "tag": "Sources"},
    {"icon": "\U0001F3B7", "title": "Coyle's site is named for John Coltrane's \"A Love Supreme\"; contact via his Berkeley email.", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "CCA", "def": "Claude Certified Architect, Anthropic's scenario-based, proctored certification exam released March 2026."},
    {"term": "stop_reason", "def": "The field telling why the model stopped (e.g. tool_use, out of tokens), which drives the agent loop."},
    {"term": "Context fork", "def": "Running a subtask in a separate thread so its tokens never pollute the main context; only a summary returns."},
    {"term": "Compaction", "def": "Anthropic's algorithms that condense a large context into a smaller one."},
    {"term": "Hub and spoke", "def": "Multi-agent layout where an orchestrator delegates to specialized worker agents."},
    {"term": "CLAUDE.md", "def": "Markdown rules file for Claude Code, layered at project, folder and directory levels."},
    {"term": "Böhm-Jacopini theorem", "def": "1966 proof that sequence, conditionals and loops suffice for Turing completeness."},
]
