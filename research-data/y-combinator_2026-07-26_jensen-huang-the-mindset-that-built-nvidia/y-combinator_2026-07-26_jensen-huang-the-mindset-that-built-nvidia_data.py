META = {
    "title": "Jensen Huang: The Mindset That Built NVIDIA",
    "channel": "Y Combinator",
    "speakers": "Jensen Huang (Nvidia CEO), Y Combinator hosts",
    "date": "2026-07-26",
    "video_url": "https://www.youtube.com/watch?v=I4B37S1dyQQ",
    "thread_line": "5 threads · the wrong-technology origin · founder mindset · agents and systems thinking · jobs vs tasks · physical AI and open source",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Startup School 2026 fireside with Jensen Huang: Nvidia was founded on a **technology that turned out to be exactly wrong**, and survived by learning the right one from textbooks.",
    "His core idea: great companies come from a unique, deeply held perspective — Nvidia's was accelerating an *algorithm domain*, not building a chip.",
    "Founder style: be curious, learn in the weeds, 'fit the car to the driver', and attack hard problems with 'how hard can it be?' while building resilience one day at a time.",
    "Agents: the most useful future skill is systems thinking; **controllability** (changing one word in a plan and regenerating only that part) is the biggest breakthrough needed.",
    "Jobs: 'AI eliminates tasks, not jobs' — he cites software-engineer jobs up ~10% and radiology jobs up ~20% a year despite automation.",
    "Physical AI is already a ~$10B Nvidia business and 'our next $100 billion business', arriving in under ten years.",
    "CEO speaking about his own company: all figures and forecasts are Nvidia management's view.",
]

THEMES = [
    {
        "id": "wrong-technology-origin",
        "tags": ["semis", "career", "mindset"],
        "color": "amber",
        "badge": "Personal story",
        "status": "FOUNDING STORY, 1993-1999",
        "title": "Nvidia's founding technology was wrong — Sega's $5 million bought time to learn the right one",
        "lead": "Nvidia started with an algorithm that was 'exactly wrong' and learned the correct 3D-graphics approach from three textbooks.",
        "bullets": [
            "1993: the idea was to turn every PC into a game console by reinventing a supercomputer-class graphics algorithm to fit in a PC.",
            "By 1995 they realized it didn't work — and none of them knew the right way; about 35-40 other companies already made PC 3D graphics.",
            "Jensen spent a couple hundred dollars at Fry's on three OpenGL and graphics-pipeline textbooks for the engineers: 'we learned it from a textbook'.",
            "Sega had contracted Nvidia for a roughly $12 million console project (the one that became Dreamcast, built by others); Jensen told Sega's CEO it couldn't be delivered, advised using someone else, and still asked for the money — about **$5 million** kept the company alive.",
            "Sega's stake was sold at Nvidia's 1999 IPO, when Nvidia was valued at $300 million; today it is worth well over a trillion dollars.",
            "Lesson: technology changes constantly; as long as you confront reality and can learn, the starting technology doesn't matter.",
        ],
        "quote": {"text": "The technology that founded the company turns out to be exactly wrong.", "cite": "— Jensen Huang"},
        "watch": "Founding-era figures are Jensen's recollection on stage; the 'sold for 15 million' figure was a host's question, not confirmed by him.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Founded on a wrong algorithm; Sega contract money kept it alive", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Sega", "blurb": "Contracted a ~$12M console project and paid about $5M though Nvidia couldn't deliver", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "founder-mindset",
        "tags": ["mindset", "career"],
        "color": "green",
        "badge": "Principle",
        "status": "FOUNDER ADVICE",
        "title": "Unique perspective, 'how hard can it be?', and fitting the car to the driver",
        "lead": "Great companies come from a unique perspective you deeply believe in — and Nvidia's was that the algorithm domain, not the chip, is the product.",
        "bullets": [
            "Accelerated computing across algorithm domains: 3D graphics, molecular dynamics, image processing, inverse physics, then deep learning.",
            "AlexNet insight: deep learning is a universal function approximator — a way of doing software that reshapes the whole stack (his 'five-layer cake'), which he says he saw about 15 years ago.",
            "He stays curious and learns details himself so he can serve the company and share insight — 'a personality technique, not a management technique'.",
            "Surfing analogy: you can't read the waves of fast-moving tech without being in the water.",
            "F1 analogy: build the company like a car you can drive; when he leaves, 'they'll just have to reshape the company for the next CEO'; 34 years of founder mode.",
            "Mindset for founders: believe you can learn; imagine 'how hard can it be?' — it will be much harder, so let the suffering arrive gradually and overcome 'that morning', not life in one day.",
            "He was too scared to read a 500-page how-to-start-a-company book; says fundraising questions still stump him — none of it mattered.",
            "He calls now the greatest time in 60 years to start a company, since the computer has been 'completely reset' by AI.",
        ],
        "quote": {"text": "Learning is the single greatest superpower.", "cite": "— Jensen Huang"},
        "watch": None,
        "names": None,
    },
    {
        "id": "agents-systems-thinking",
        "tags": ["ai-infra", "software", "dev-workflow"],
        "color": "green",
        "badge": "Moderate conviction",
        "status": "AGENTS, OPENCLAW AND HERMES",
        "title": "Systems thinking and controllability: what agents need next",
        "lead": "Low-level work will be automated agentically, so the most useful skill is systems design — and the biggest missing breakthrough is fine-grained control of agents.",
        "bullets": [
            "Chip designers now work as systems designers because synthesis automates gates and blocks; software will follow.",
            "Systems checklist he gives: inputs, outputs, rates, constraints, and whether the bottleneck is processor, memory or networking.",
            "Agents already show coarse recursive self-improvement: they update markdown files and long-term memory, compacted or turned into knowledge graphs, asynchronously.",
            "**Controllability**: change one word in a plan file (one pixel, triangle, CAD component or via) and only that part regenerates; agents needn't be 100% accurate — 80% or 99% with human help is enough.",
            "Nvidia studies agents because 'agents are the new software': systems take ~3 years to build and 2 to ramp, so it designs 5-10 years ahead (concurrency, sandboxes, MCP, working and long-term memory).",
            "Internally, Claude Code runs autonomously in sandboxes across Nvidia, and engineers choose Codex, Claude Code, Cursor or Cognition — 'a thousand flowers bloom'.",
            "He views OpenClaw as the 'Linux moment' and the OS for LLMs, told its creator Peter 'all of Nvidia's engineers are your engineers', and backs the Hermes team; Nvidia built a sandboxing toolkit around the harness.",
            "He urges companies to build their own domain-specific AI (Hermes, OpenClaw, LangChain deep agents) while still using ChatGPT and Claude; the host adds that markdown files are 'text is intelligence'.",
        ],
        "quote": {"text": "Controllability is probably the single biggest breakthrough that we need for agents at every single level.", "cite": "— Jensen Huang"},
        "watch": "Captions garble 'OpenClaw' as 'OpenCL' in several places; the brief reads them as OpenClaw from context. Nvidia sells the compute agents run on.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Designs systems 5-10 years ahead for agentic workloads; supports OpenClaw and Hermes", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "5-10 years"},
            {"name": "Anthropic", "blurb": "Claude Code used autonomously inside Nvidia; Claude recommended for everyone to use", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "OpenAI", "blurb": "ChatGPT and Codex named among tools to use", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Cursor", "blurb": "One of the coding tools Nvidia staff choose", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Cognition", "blurb": "One of the coding tools Nvidia staff choose", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "jobs-tasks-purpose",
        "tags": ["career", "policy", "software"],
        "color": "amber",
        "badge": "Counterintuitive take",
        "status": "AI AND EMPLOYMENT",
        "title": "'The narrative about AI destroying jobs is exactly backwards'",
        "lead": "AI eliminates tasks, not jobs, because a job has a purpose made of many tasks — and backlogs of ambition absorb the productivity gain.",
        "bullets": [
            "Software: coding is automated, yet software-engineer jobs are up about **10%** year over year, he says.",
            "Radiology: scan reading is automated, yet radiology jobs are up roughly **20%** in recent years because patient backlogs are huge.",
            "Law: Harvey was predicted to wipe out paralegals; paralegals are 'growing like crazy' as firms take on more cases.",
            "Mechanism: productivity raises growth, growth raises employment; there is more employment today than when he left school.",
            "Chip scale as proof of ambition: his generation designed ~1,000-transistor chips; a trillion-transistor chip is now 'not a thing'.",
            "Advice to the young: simple tasks (like long division or typing code) get automated; hard sciences, systems thinking and the intersections of tech and social problems remain — 'stay in school'.",
            "Caveat he states: automation is uneven, many tasks and every job will change, and new jobs will appear.",
        ],
        "quote": None,
        "watch": "The job-growth percentages are Jensen's on-stage figures with no source named; he sells the compute behind AI automation.",
        "names": [
            {"name": "Harvey", "blurb": "Cited as the legal AI predicted to eliminate paralegals, which instead grew", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "physical-ai-open-source",
        "tags": ["robotics", "ai-infra", "policy"],
        "color": "green",
        "badge": "High conviction",
        "status": "PHYSICAL AI AND OPEN SOURCE",
        "title": "Physical AI as the next $100 billion business, and why open source matters",
        "lead": "Nvidia says robotics and autonomous vehicles are already almost a $10 billion business and will be its next $100 billion one in under ten years.",
        "bullets": [
            "He says robotics had its 'ChatGPT moment' a couple of years ago: generating video of a moving finger implied a robot could be made to do the same.",
            "Three layers: real-to-sim environments, simulators (Isaac Sim, Cosmos world foundation models; grounded plus generative physics), and sim-to-real with reinforcement learning.",
            "Self-driving: chips are in Waymo, Tesla (car, now data center) and Mercedes; Nvidia open-sourced its Alpamayo reasoning self-driving stack for agriculture, mail delivery and warehouse robots.",
            "Alpamayo needs only about a million or a couple of million miles because a language model supplies prior knowledge to decompose unseen situations.",
            "Physical AI will take longer than two or three years and less than ten, and will 'be our next $100 billion business'.",
            "He made his first post on X in 2026, calling open weights and open source essential — mobile and cloud, Linux, Kubernetes, PyTorch and earlier frameworks were all open.",
        ],
        "quote": None,
        "watch": "Segment sizes and timing are Nvidia management's own estimates; the model name 'Alpamayo' is garbled in the captions and read from context.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Physical AI near $10B now, 'next $100 billion business' in under ten years", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "under 10 years"},
            {"name": "Waymo", "blurb": "Uses Nvidia chips in its self-driving cars", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Tesla (TSLA)", "blurb": "Nvidia was in the car and is now in Tesla's data center", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9ED", "tag": "Strategy", "title": "Define your company by a unique perspective and an algorithm domain, not by the product you ship today."},
    {"icon": "\U0001F6E0", "tag": "Agents", "title": "Invest in controllability: design agent workflows where you can change one input and regenerate only that part."},
    {"icon": "\U0001F9E0", "tag": "Careers", "title": "Build systems-thinking skills — inputs, outputs, rates, constraints — rather than syntax alone."},
    {"icon": "\U0001F916", "tag": "Robotics", "title": "Follow Nvidia's physical-AI segment and its $100B target as a read on robotics demand."},
    {"icon": "\U0001F4BC", "tag": "Labor", "title": "Separate task automation from job purpose when judging AI's effect on any profession."},
    {"icon": "\U0001F3AF", "tag": "Founders", "title": "Break each day into 'overcome this morning' rather than imagining the full difficulty up front."},
]

HOT_TAKES = [
    {"take": "The narrative about AI destroying jobs is exactly backwards.", "cite": "— Jensen Huang", "why": "Contrarian jobs claim"},
    {"take": "Controllability is probably the single biggest breakthrough that we need for agents at every single level.", "cite": "— Jensen Huang", "why": "Ranked claim"},
    {"take": "This will be our next $100 billion business.", "cite": "— Jensen Huang (on physical AI)", "why": "Dated numeric CEO call"},
    {"take": "I would say the ChatGPT moment of robots happened a couple of years ago already.", "cite": "— Jensen Huang", "why": "Timing claim"},
    {"take": "This is absolutely the single greatest time to start a company.", "cite": "— Jensen Huang", "why": "Strong ranking"},
]

CLAIMS = [
    {"who": "Jensen Huang", "claim": "Nvidia's physical-AI business becomes its next $100 billion business in less than ten years.", "metric": "Nvidia physical AI revenue", "target": "$100 billion", "by": "within 10 years", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Jensen Huang", "claim": "Nvidia's robotics, autonomous-vehicle and physical-AI business is already almost $10 billion.", "metric": "Nvidia physical AI revenue", "target": "~$10 billion", "by": None, "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Jensen Huang", "claim": "Practical physical AI will take longer than two to three years and less than ten.", "metric": "physical AI maturity", "target": "practical at scale", "by": "3-10 years", "condition": None, "entity": None},
    {"who": "Jensen Huang", "claim": "Software-engineer jobs are growing about 10% year over year despite coding automation.", "metric": "software engineer jobs", "target": "+10% year over year", "by": None, "condition": None, "entity": None},
    {"who": "Jensen Huang", "claim": "Radiology jobs have grown about 20% in recent years despite AI reading scans.", "metric": "radiology jobs", "target": "+20%", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Sega", "rel": "customer_of", "to": "Nvidia (NVDA)", "note": "contracted a ~$12M console project; paid about $5M"},
    {"from": "Waymo", "rel": "customer_of", "to": "Nvidia (NVDA)", "note": "Nvidia chips inside its cars"},
    {"from": "Tesla (TSLA)", "rel": "customer_of", "to": "Nvidia (NVDA)", "note": "Nvidia in the car, now in the data center"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: AlexNet; early chain-of-thought work from Stanford; the OpenClaw creator Peter and the Hermes agent team; open-source projects Linux, Kubernetes, PyTorch, TensorFlow, Torch, Caffe and Theano.", "tag": "Sources"},
    {"icon": "\U0001F4F1", "title": "Jensen made his first post on X in 2026 ('probably the last human on Earth'), announcing something he called important to the industry.", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "Accelerated computing", "def": "Augmenting CPUs with accelerators to solve problems that are otherwise too hard, organized around algorithm domains."},
    {"term": "Universal function approximator", "def": "A neural network that can learn almost any function from examples, which is how Jensen frames deep learning."},
    {"term": "Five-layer cake", "def": "His shorthand for the stack reinvented by AI: processor, middleware, algorithms, applications and industry use."},
    {"term": "Controllability", "def": "The ability to change one small input of an agent's plan and regenerate only the affected output."},
    {"term": "Physical AI", "def": "AI that understands and acts in the physical world, such as robots and self-driving cars."},
    {"term": "Sim-to-real", "def": "Training robots in simulation, then transferring the skill to the real world with reinforcement learning."},
]
