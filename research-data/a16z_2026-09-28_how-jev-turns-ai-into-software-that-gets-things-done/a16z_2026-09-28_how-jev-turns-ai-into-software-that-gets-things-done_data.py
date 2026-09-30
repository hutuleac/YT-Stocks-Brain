META = {
    "title": "How Jev Turns AI Into Software That Gets Things Done",
    "channel": "a16z",
    "speakers": "Founder of Typesafe, ex-OpenAI (name garbled in captions); two a16z hosts",
    "date": "2026-09-28",
    "video_url": "https://www.youtube.com/watch?v=Ut3LOjKNJaE",
    "thread_line": "5 threads · 'where's all the automation?' · Jev as a smart-software primitive · reliability as the product · coding agents vs. the SaaS 'inverse apocalypse' · an ex-OpenAI founder's 'build prod, not god' worldview",
    "category": "dev",
}

SNAPSHOT = [
    "a16z interviews the founder of **Typesafe**, maker of **Jev**, an ex-OpenAI researcher behind RLHF-era ChatGPT work, ~42 min. Captions garble both names.",
    "The pitch: 'where is all the automation?' AI aces math benchmarks but can't run a drive-thru, and OpenAI has tried to automate customer service since 2020.",
    "Coding agents like Claude Code and Codex make 'just-in-time software' (Garry Tan's phrase) that is still ordinary code. Jev is instead a new primitive inside your code that expands what software can do.",
    "Jev is 'absolutely a classifier': natural-language intent plus a state machine in, a confident choice out. The founder's north star is intelligence per dollar.",
    "Reliability is the product: not just determinism but 'smart every time', good enough that developers program against it without testing example queries.",
    "Contrarian on SaaS: not an apocalypse but an 'inverse apocalypse'. SaaS companies are among AI's biggest winners because they already own the workflows and distribution.",
    "'We build prod, not god': the founder doesn't think we're on a path to recursive self-improvement, and expects more, better jobs.",
]

THEMES = [
    {
        "id": "where-is-the-automation",
        "tags": ["software", "dev-workflow"],
        "color": "amber",
        "badge": "Structural critique",
        "status": "THESIS — AI IS SMART, SOFTWARE IS UNCHANGED",
        "title": "'Where is all the automation?' AI aces GPQA but can't run a drive-thru",
        "lead": "The founder argues the industry optimized for impressing human judges instead of automating real work, so software looks the same as it did 10 years ago.",
        "bullets": [
            "The elevator pitch is simply 'where the [expletive] is all the automation?' AI is 'unbelievably smart' yet useless for most work. The best most products manage is a side-panel chatbot that can only take some actions reliably.",
            "The canary in the coal mine: math and Google-proof Q&A (GPQA) are reportedly 'solved', 'but we still can't handle a drive-thru'. OpenAI has been trying to automate **customer service** since 2020.",
            "Since RLHF, the industry split into 'gigantic overpromise, underdeliver'. Because humans evaluate the models, labs optimized the judge instead of the automation. He calls GPT-3 'quite calibrated' for its day.",
            "The host pushes back that the real world has heavy-tailed data. The founder half-agrees about the long tail but rejects the data excuse: the intelligence for rote, simply specified work has 'been available in the models for quite a while'.",
            "The host's support example: vendors claimed 95% of help-desk calls automated, but most were password resets, and only ~50% by uniqueness. Automation should be an ROI call, in the Perl 'programmer virtues' tradition of laziness and hubris.",
            "The host's anecdote: a16z growth lead David George used Meta's Muse to finally cancel his New York Times subscription, 'the tip of the iceberg' of horrible tasks to automate. The founder warns against the AI habit of chasing outlier demos.",
        ],
        "quote": {"text": "AI is so unbelievably smart and yet it's so useless at all other stuff.", "cite": "— Typesafe founder"},
        "watch": "The founder won't name the diffusion-excuse makers ('I shouldn't name names'), and says their favorite use cases may not yet work reliably ('I'm not sure if they work').",
        "names": None,
    },
    {
        "id": "jev-primitive",
        "tags": ["dev-workflow", "software"],
        "color": "green",
        "badge": "Framework",
        "status": "LAUNCHED — 'CAUGHT FIRE' WITH DEVELOPERS",
        "title": "Jev: a classifier-shaped primitive that puts intelligence inside the program",
        "lead": "Instead of AI writing ordinary code faster, Jev is a library call where you describe intent in natural language, pass a state machine, and get back a confident choice.",
        "bullets": [
            "Garry Tan calls coding agents (Claude Code, Codex, Cursor) '**just-in-time software**': natural-language programming with the same expressive power as code. Jev aims for 'smart software' that expands what code itself can do.",
            "'Jev is absolutely a classifier… classifiers are sick.' It has the same interface as practical ML, and 'probably is better than having an MLE team from 2019' building narrow models, programmable on the fly.",
            "The design sits in the middle of a Venn diagram of 'what AI is good at' and 'what is valuable in code': probabilities yes, extrapolated floats no. The input is deliberately called 'state' because it's meant for program internals.",
            "North star: **intelligence per dollar**, though intelligence per second may matter more short-term. For now it behaves 'more like a database' because of millisecond latency, with a standard-library role as the goal.",
            "Why it's new: before, AI and software were 'ships in the night'. JSON-schema prompts failed, so output went to a human (chat) or another LLM (the agent while-loop). The host saw teams go through 'five stages of grief' before this.",
            "Uses are surprising even the founder, such as a voice computer controller deciding command vs. dictation on every utterance. Multiple-choice forms could disappear, the host notes 1980s 4GLs, and the dream is 'do what I mean'.",
            "It could open an era of probabilistic programming, which 'basically died in the 70s', or be called neurosymbolic. Co-founder Eric has a Bayesian background, but the founder's brand is 'incredible pragmatism', not biologically inspired AI.",
        ],
        "quote": {"text": "Programming is hyper-specifying valuable things and then infinitely replicating them. It's so freaking cool.", "cite": "— Typesafe founder"},
        "watch": "The a16z hosts call Typesafe 'more than a company… a whole movement'. Treat the enthusiasm as coming from supporters. The founder admits some flagship community uses may not be reliable yet.",
        "names": None,
    },
    {
        "id": "reliability-is-the-product",
        "tags": ["dev-workflow", "software"],
        "color": "green",
        "badge": "Recommendation",
        "status": "DESIGN PRINCIPLE — EVERY NINE COUNTS",
        "title": "Reliability is the product: 'smart every time', not just deterministic",
        "lead": "The founder frames Jev's moat as years of work on reliability, with layers well beyond uptime, and says a benchmaxed copycat will miss it.",
        "bullets": [
            "Reliability has layers: uptime/SLAs, then determinism (useful for unit tests, 'not real systems'), then **robustness**, meaning similar intelligence every time. Adding a UUID to a prompt shouldn't change the answer.",
            "A further unnamed layer is 'smart every time': the output needn't be identical, but it should be something a human would find understandable, so developers can program around it.",
            "The highest bar is developers programming against Jev without testing example queries, in a 'flow state' of trust. 'Every nine of reliability' unlocks new applications.",
            "Production needs composability and safety guarantees, at least statistical ones, when agents touch real resources. They 'could have released so much sooner' but held out for reliability.",
            "The host asks about hard guarantees (state consistency, durability, air traffic control). The founder's rule is 'automate the easy work before the hard work'. Systems engineers may want only 'approximate guesses' at many cost/speed tradeoffs.",
            "Networking analogy: think UDP vs TCP. Working back from an AI-everywhere economy, 'many nines' of AI calls will sit deep 'in the guts' of software, not facing humans, even if adoption starts at the top layer.",
        ],
        "quote": {"text": "If you don't understand that, it'll be very hard to make a copycat that's benchmaxed.", "cite": "— Typesafe founder"},
        "watch": None,
        "names": None,
    },
    {
        "id": "coding-agents-saas",
        "tags": ["software", "dev-workflow", "career"],
        "color": "amber",
        "badge": "Contested",
        "status": "COUNTER-CONSENSUS — SAAS 'INVERSE APOCALYPSE'",
        "title": "Coding agents write faster, not better. SaaS is a winner, not a casualty",
        "lead": "The panel argues AI coding automates a thin slice of work, while a primitive like Jev makes existing SaaS products dramatically more capable.",
        "bullets": [
            "Coding agents are 'really good at syntax', bad at semantics and 'incredibly bad at architecture', which the founder calls the most human, creative part. They may be at the 50th percentile, fine if speed is the priority (Codex working overnight).",
            "The host's study: the average PR at a large company is ~10 lines. AI coding optimizes a minimal slice and adds no new capabilities, and 'the software actually isn't getting better… arguably getting worse' and less secure.",
            "Coding agents triggered the 'SaaS apocalypse' sell-off, but SaaS companies cheered Jev. The founder buys 'software is cheap' but not 'easy to replicate', because 'a lot happens beneath the hood'.",
            "His call: SaaS 'will be one of the largest winners of the whole AI game'. SaaS companies know the boring workflows and have already paid the capex of reaching customers. He calls it an 'inverse apocalypse', and the hosts suggest 'SaaS-palooza'.",
            "The host sees a platform rebuild like the internet or mainframe-to-client/server, and cybersecurity may force rebuilding most critical infrastructure anyway.",
        ],
        "quote": {"text": "I think that SaaS will be one of the largest winners of the whole AI game.", "cite": "— Typesafe founder"},
        "watch": "The founder explicitly declines to forecast markets ('I'm not going to forecast anything about the financial markets'). The call is about capabilities, not stock prices. Jev isn't in coding agents' training data yet, which he'd find 'spooky'.",
        "names": None,
    },
    {
        "id": "prod-not-god",
        "tags": ["career", "mindset", "ai-infra"],
        "color": "gray",
        "badge": "Personal story",
        "status": "WORLDVIEW — NO RSI, MORE JOBS",
        "title": "'Build prod, not god': an ex-OpenAI RLHF researcher who stopped believing in the single super-brain",
        "lead": "Seeing RLHF generalize, then fall short of AGI, convinced the founder that the gap is useful automation rather than a coming superintelligence.",
        "bullets": [
            "Background: an award-winning mathlete who never liked math, a Kaggle win from 'automating the [expletive] out of it', and a forced NeurIPS talk. Kaggle host Isabelle Guyon (SVM co-inventor) adopted them into the AI community.",
            "Then a startup with Jeremy Howard, Google Brain, a stint retired, and OpenAI 'because AI is pretty damn fun'. They identify as a computer scientist first, still love giving algorithms interviews, and wouldn't recommend being CEO.",
            "In Q4 2021 RLHF generalized surprisingly well. The test query 'why is it important to eat socks before meditating?' (checked to not be on the internet) proved it wasn't cheating. They thought the model had 'a decent chance of being AGI', and when it wasn't, 'my whole world came crashing down'.",
            "RLHF generalizes well, but **RLVR** less so. Early OpenAI described AGI as 'Ilya and every if-statement', vague by design as a big tent.",
            "'For nuanced reasons I don't think we are on the path of RSI.' But OpenAI's AGI definition, automating most economically valuable work, is 'extremely doable'.",
            "The founder rejects the 'mono-model Kool-Aid' of one brain to rule them all and expects more, better jobs. Their 2017 talk was already titled roughly 'AI: modular in theory, flexible in practice'.",
        ],
        "quote": {"text": "For nuanced reasons, I don't think we are on the path of RSI.", "cite": "— Typesafe founder"},
        "watch": "The 'no RSI' view is stated as the founder's belief without the 'nuanced reasons' being laid out. It also suits a company selling practical tooling over frontier models.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9E9", "tag": "Dev workflow", "title": "Put model calls inside program logic as classifiers over explicit states, not just in chat sidebars or agent loops."},
    {"icon": "\U0001F4CF", "tag": "Reliability", "title": "Test AI components for robustness: an irrelevant prompt change (such as a UUID) shouldn't change the decision."},
    {"icon": "\U0001F3D7", "tag": "Coding agents", "title": "Let coding agents handle syntax and keep architecture decisions human-owned."},
    {"icon": "\U0001F4B0", "tag": "AI costs", "title": "Pick models by intelligence per dollar for embedded, high-volume calls, not by top benchmark score."},
    {"icon": "\U0001F9F9", "tag": "Automation", "title": "Automate the dull, well-specified tasks first, like cancellations and password resets, before chasing demo-worthy edge cases."},
]

HOT_TAKES = [
    {"take": "OpenAI has been trying to automate customer service since 2020.", "cite": "— Typesafe founder", "why": "ex-OpenAI jab at the lab's track record"},
    {"take": "It doesn't matter how much AI coding agents you use, the software actually isn't getting better. Maybe you're writing it faster. It's arguably getting worse.", "cite": "— a16z host", "why": "against the coding-agent consensus"},
    {"take": "Jev is absolutely a classifier. Classifiers are sick.", "cite": "— Typesafe founder", "why": "embraces the dismissive label"},
    {"take": "For nuanced reasons, I don't think we are on the path of RSI.", "cite": "— Typesafe founder", "why": "rejects the recursive self-improvement narrative"},
    {"take": "I think that SaaS will be one of the largest winners of the whole AI game.", "cite": "— Typesafe founder", "why": "opposite of the SaaS-apocalypse view"},
    {"take": "They're really good at syntax… I would say incredibly bad at architecture.", "cite": "— Typesafe founder", "why": "on coding agents"},
]

CLAIMS = [
    {"who": "Typesafe founder", "claim": "SaaS companies end up among the largest winners of AI rather than casualties.", "metric": "SaaS position in AI", "target": "among largest winners", "by": None, "condition": None, "entity": None},
    {"who": "Typesafe founder", "claim": "AI is not on a path to recursive self-improvement, while automating most economically valuable work is achievable.", "metric": "RSI", "target": "not on path", "by": None, "condition": None, "entity": None},
    {"who": "Typesafe founder", "claim": "Multiple-choice forms in software disappear, replaced by natural-language input mapped to structured output.", "metric": "multiple-choice UI", "target": "disappears", "by": None, "condition": None, "entity": None},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "People and sources referenced: Garry Tan ('just-in-time software'), Isabelle Guyon, Jeremy Howard, Ilya Sutskever (the early OpenAI AGI quip), a16z's David George, and the Perl-era 'three virtues of a programmer'.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Just-in-time software", "def": "Garry Tan's description of coding agents: software generated on the fly from natural language."},
    {"term": "RLHF", "def": "Reinforcement learning from human feedback, the ChatGPT-era training method the founder says generalizes well."},
    {"term": "RLVR", "def": "Reinforcement learning from verifiable rewards; the founder has seen it generalize less well than RLHF."},
    {"term": "RSI", "def": "Recursive self-improvement, AI improving itself in a runaway loop."},
    {"term": "GPQA", "def": "The 'Google-proof' graduate-level Q&A benchmark."},
    {"term": "Benchmaxing", "def": "Tuning a model to top benchmarks rather than to work reliably."},
    {"term": "4GL", "def": "Fourth-generation language, 1980s-era 'say what you want' programming languages."},
    {"term": "Probabilistic programming", "def": "Programs that reason over probabilities; an older research line the founder sees reviving."},
    {"term": "SaaS apocalypse", "def": "The market fear that cheap AI-written software destroys SaaS companies' value."},
]
