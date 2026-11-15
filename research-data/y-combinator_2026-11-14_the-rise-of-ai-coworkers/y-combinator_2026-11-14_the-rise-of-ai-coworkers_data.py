META = {
    "title": "The Rise Of AI Coworkers",
    "channel": "Y Combinator",
    "speakers": "Lauren Tan, Roman Ugarte (Grokbot core team); YC Light Cone hosts incl. Garry Tan",
    "date": "2026-11-14",
    "video_url": "https://www.youtube.com/watch?v=y1-9yeYLJUo",
    "thread_line": "5 threads · bots as employees · trust ladder · the Slack outer loop · codebase-as-memory review · taste as the bottleneck",
    "category": "dev",
    "region": "",
}

SNAPSHOT = [
    "**Grokbot** lets anyone create AI teammates with names, identities, skills, tools and their own computer; built from first line of code to launch in **7 weeks**.",
    "Three design principles: work organized around **bots** (not chats or files), bots use the same tools humans do, and bots are **always on** and proactive.",
    "Adoption follows a trust ladder: read-only helper, then end-to-end tasks, then owning a whole job — the team says step three is still far away.",
    "Lauren Tan went from ~2,000 to **4,000+ PRs a month**; whole features now get built in one public Slack thread with a bot that spawns Cursor cloud agents.",
    "Her review philosophy: push quality into the codebase (lint rules, static analysis, CI) instead of burning tens of millions of tokens on adversarial review.",
    "With execution abundant, the bottleneck moves to **specification, alignment and taste** — the team ships nothing that lacks internal product-market fit.",
    "Small businesses are among the heaviest early users because they struggle most to hire — e.g. a bookkeeping bot set up in hours.",
]

THEMES = [
    {
        "id": "bots-as-employees",
        "tags": ["dev-workflow", "software"],
        "color": "green",
        "badge": "Product thesis",
        "status": "TEAM BOTS LAUNCHED ~2 WEEKS BEFORE RECORDING",
        "title": "Grokbot treats a bot as a teammate, not a chat window",
        "lead": "The operating question for every design choice is \"what would you do for a human?\" — give it a computer, credentials scoped to its role, and expand access as trust grows.",
        "bullets": [
            "Prototype spun up internally in about 7 weeks after seeing long-running coding agents transform how engineers worked; now built into the default DM on X.",
            "Internal reception was a **bell curve**: both the most and least AI-forward employees liked it.",
            "Performance marketing gave its bot Google Ads and Facebook Ads logins plus a budget, and has it talk to the design team's bot to A/B test assets.",
            "Customer success runs a team bot that fields hundreds of customer messages a minute, triages, finishes many tickets end to end and escalates the rest to the right DRI.",
            "**Team bots** (multiplayer): an owner/manager with write access, invited collaborators, shared across the org — usually built by the 'builder' in each department (GTM or support engineers).",
            "Setup is up to you: specialist bots per function, one bot per customer, or one generalist; Roman prefers bots that each obsess over one problem, like hiring someone who 'wakes up in the morning and really cares'.",
            "Goal is not to rebuild B2B SaaS but to work inside existing tools — Slack, meetings, Google Docs.",
        ],
        "quote": {"text": "Our goal is not to rebuild all of B2B SaaS. Our goal is to build the thing that can access those tools and work inside of them", "cite": "— Roman Ugarte"},
        "watch": "Auth, permissioning and bot identity are called an industry-wide open question with no silver bullet yet; bots in Slack threads also lack 'EQ' about whom to listen to.",
        "names": None,
    },
    {
        "id": "trust-ladder",
        "tags": ["dev-workflow", "career"],
        "color": "amber",
        "badge": "Framework",
        "status": "STEP 3 STILL FAR AWAY",
        "title": "Trust is built in three steps, and most companies are on step one",
        "lead": "Start read-only, graduate to end-to-end tasks, and only later let a bot own an outcome.",
        "bullets": [
            "Step one: **Data Bot** — read access to the warehouse, lives in Slack, answers 'can you do a quick analysis' requests the data science team kept getting.",
            "Vendor procurement built a similar step-one bot and shared it with the whole team.",
            "Step two: the bot takes action and completes a task end to end; step three: it owns a job responsibility or an outcome continuously.",
            "Individual users follow the same arc: task, then objective, then 'a full job now'.",
            "Bots can chat with each other via a first-class tool; a 'lead engineer' bot given feedback started scolding its sub-bots like a disciplinarian.",
            "YC runs an internal forum where everyone's coding agents talk to each other — 'like an internal Stack Overflow', which the host finds about 5% eerie.",
        ],
        "quote": {"text": "It's as if you were to onboard an employee who has no EQ and like no like social awareness of the room.", "cite": "— Roman Ugarte"},
        "watch": "A host flags abliterated (refusal-removed) models as the combination to worry about: still helpful by default, but they will follow malicious instructions without refusing.",
        "names": None,
    },
    {
        "id": "outer-loop",
        "tags": ["dev-workflow"],
        "color": "green",
        "badge": "Workflow",
        "status": "4,000+ PRS PER MONTH",
        "title": "The outer loop moves into Slack, in public",
        "lead": "Lauren Tan's agents now come to where the context is — Slack and X threads — instead of her copy-pasting context into a private agent session.",
        "bullets": [
            "Her engineering bot **Potato** took a link from X, spawned a Cursor cloud agent with its own VM, ran the app and came back with videos and screenshots.",
            "That feature was built end to end in one ~200-message Slack thread with a colleague and a PM; she never opened Cursor and did not read the PR — agents merge their own PRs.",
            "Public threads spread practice: someone sees 'Lauren mode' used in a thread and does the same the next day.",
            "Minimal loop: teach the agent to **run the code like a real user** (CPU traces, performance metrics) so it can check its own work — correct, though not necessarily good.",
            "Outer loop: a metric alert fires an agent that reproduces, fixes and ships; a 'projects' feature lets a coordinator agent manage sub-agents so she no longer manages the project.",
            "'Sandy' ingests thousands of pieces of customer feedback daily; small bugs are repro'd, fixed and merged automatically, shipping around 3 a.m.",
        ],
        "quote": {"text": "I didn't even look at cursor for this project which I just we just we did it all in in the Slack thread.", "cite": "— Lauren Tan"},
        "watch": "Lauren says she works at a lab with unlimited tokens and that reaching this setup took 'quite a while' — not an overnight switch.",
        "names": None,
    },
    {
        "id": "codebase-as-memory",
        "tags": ["dev-workflow", "software"],
        "color": "green",
        "badge": "Recommendation",
        "status": "INVERTED PYRAMID OF ENGINEER TIME",
        "title": "Encode review into the codebase instead of paying for it in tokens",
        "lead": "Most engineering investment should go into the codebase and static analysis, then rules and skills, with only thin human review on top.",
        "bullets": [
            "Garry Tan's G-stack ship/review skill burns tens of millions of tokens; he is arguing with an agent over cutting review from 50M to 10M tokens while held-out evals across ~30 bug types demand 30M.",
            "Lauren has de-emphasised adversarial multi-model review ('interrogate'): it risks overfitting because the reviewer lacks your goals and product vision.",
            "'Your code base is a form of memory' — lint rules, compilers, API design and static analysis are cheaper than repeated agent review.",
            "Example: the Electron renderer thread janks on tasks over ~16 ms (8 ms for smooth frames); they forbid imports between main and renderer code via a dependency-graph lint rule enforced in CI.",
            "Keep humans in the loop for critical infrastructure, databases and deployment.",
            "**P-stack** ('potato stack') is her open-sourced skill set on the Cursor plugins repo, inspired by G-stack; she tells people to fork and build their own 'chef's knives'.",
        ],
        "quote": {"text": "So it's tokens I don't have to spend anymore.", "cite": "— Lauren Tan"},
        "watch": None,
        "names": None,
    },
    {
        "id": "taste-bottleneck",
        "tags": ["career", "dev-workflow"],
        "color": "amber",
        "badge": "Structural shift",
        "status": "FROM EXECUTION-CONSTRAINED TO EXECUTION ABUNDANCE",
        "title": "When execution is cheap, specification and taste become the scarce resource",
        "lead": "The gap stops being execution failure and becomes intent-specification failure — and deciding what not to merge.",
        "bullets": [
            "Roman: code compiles or passes CI; knowledge work has no such harness, and its context is stuck in heads, paper and filing cabinets.",
            "The team's bottleneck is now roadmap alignment: someone suggests a change and a colleague already has a weekend PR for it.",
            "Default rule: if a change doesn't get internal product-market fit — even mixed — it doesn't ship; core UI changes get dogfooded longer than feels comfortable.",
            "Lauren points her factories at **maintenance** (performance, bugs, quality-of-life) rather than features, keeping human judgment on the experience.",
            "Jack Dorsey's AI-native org model is cited: no middle management, ICs who ship outcomes, DRIs who orchestrate, and a temporary AI 'player coach'.",
            "Lauren wonders whether the final form of agent interaction is chat at all, citing a Neuralink post about a mind-reading interface.",
        ],
        "quote": {"text": "we've been living in a bit of an execution bandwidth constrained world and now we're going to shift to to execution abundance", "cite": "— Roman Ugarte"},
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001FA9C", "tag": "AI adoption", "title": "Start every bot read-only and widen access only after it does the work the way you would."},
    {"icon": "\U0001F501", "tag": "Engineering", "title": "Give agents the ability to run the app like a user before investing in fancier review."},
    {"icon": "\U0001F9F1", "tag": "Code quality", "title": "Turn recurring review comments into lint rules and CI checks to cut token spend."},
    {"icon": "\U0001F4AC", "tag": "Teams", "title": "Run agent work in public channels so the rest of the company copies the best workflows."},
    {"icon": "\U0001F3AF", "tag": "Strategy", "title": "Spend saved execution time on defining objectives and KPIs your agents can aim at."},
    {"icon": "\U0001F4E3", "tag": "Careers", "title": "Share what you learn publicly — Lauren's path from accounting degree to tech started with a blog and a conference invite."},
]

HOT_TAKES = [
    {"take": "maybe like 5 or 10% of engineers or maybe 1% of engineers period in the world are doing this right now. So this is literally something that should grow by 100 X.", "cite": "— Garry Tan", "why": "numeric adoption call"},
    {"take": "I'm so convinced that in five or ten years, or even like in two years, like, it's going to be unfathomable that like people are not doing it this way.", "cite": "— Garry Tan", "why": "dated prediction"},
    {"take": "There used to be the trade-off before that you could only choose two out of three. It was either like fast, cheap, and high quality. Now you could basically do all three.", "cite": "— Garry Tan", "why": "contrarian vs classic trade-off"},
    {"take": "I've gotten to a point where I essentially have my agents merge their own pull requests.", "cite": "— Lauren Tan", "why": "removes human review"},
    {"take": "the default is if something doesn't get internal product market fit, we don't ship it. Even if it gets like mixed internal product market fit, we don't ship it.", "cite": "— Roman Ugarte", "why": "high bar stance"},
]

CLAIMS = [
    {"who": "Garry Tan", "claim": "Engineers building features end to end with bots in shared threads grows about 100x from today's ~1-10%.", "metric": "share of engineers working this way", "target": "100x growth", "by": None, "condition": None, "entity": None},
    {"who": "Garry Tan", "claim": "Not working this way becomes unfathomable within two to ten years.", "metric": "agent-first engineering adoption", "target": "universal", "by": "2-10 years", "condition": None, "entity": None},
    {"who": "Lauren Tan", "claim": "By 2027 bots have their own identity, phone number and credit card and can do almost anything a human coworker can.", "metric": "bot coworker capabilities", "target": "human-equivalent identity", "by": "2027", "condition": None, "entity": None},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Steve Yegge's Gas Town post (software factories), Jack Dorsey's AI-native company post, a Neuralink post, theo.gg's T-stack, YC's open-sourced Quartermaster (permissions inherited from the user).", "tag": "Sources"},
    {"icon": "\U0001F9EA", "title": "A host cites OpenAI agent-swarm experiments, a Hugging Face hack and swarm work on Navier-Stokes/millennium-prize problems, and says it's been a year since Opus 4.5 — single-player vibe coding is mastered, swarms are next.", "tag": "AI"},
    {"icon": "\U0001F6E0", "title": "Garry Tan's own factory, **Cappy**, runs 10-15 threads with a 'captain' managing his G-stack merge queue and learns from transcripts when he intervenes.", "tag": "Workflow"},
    {"icon": "\U0001F393", "title": "Lauren Tan grew up in Singapore, studied accounting and finance at Monash, found coding via Excel/VBA, was invited by Tom Dale and Leah Silber to speak at an Ember conference, and later worked on the React compiler.", "tag": "Careers"},
]

GLOSSARY = [
    {"term": "Outer loop", "def": "Gathering context, discussing and coordinating work around the agent, versus the inner loop of writing and testing code."},
    {"term": "Software factory", "def": "A setup of long-running agents that turns requests into shipped code with little human hands-on work."},
    {"term": "Team bot", "def": "A Grokbot shared across a team, owned by one builder with write access and used by collaborators."},
    {"term": "P-stack / G-stack", "def": "Personal open-source skill sets that teach agents an engineer's preferred way of working (Lauren Tan's and Garry Tan's)."},
    {"term": "Abliterated model", "def": "An open model with its refusal behaviour removed, so it complies with any instruction."},
]
