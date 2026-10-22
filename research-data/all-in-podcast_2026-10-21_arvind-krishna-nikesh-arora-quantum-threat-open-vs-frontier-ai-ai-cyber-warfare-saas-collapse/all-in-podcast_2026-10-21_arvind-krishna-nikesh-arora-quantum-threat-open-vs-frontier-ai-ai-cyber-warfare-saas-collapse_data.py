META = {
    "title": "Arvind Krishna & Nikesh Arora: Quantum Threat, Open vs Frontier AI, AI Cyber Warfare & SaaS Collapse",
    "channel": "All-In Podcast",
    "speakers": "Arvind Krishna (IBM CEO), Nikesh Arora (Palo Alto Networks CEO), All-In hosts",
    "date": "2026-10-21",
    "video_url": "https://www.youtube.com/watch?v=yzk44lz-RGI",
    "thread_line": "6 threads · quantum breaks crypto ~2030 · 75-90% of tokens go open-weight · AI cyber warfare · politics can't stop AI · vertical stacks win · SaaS consolidation",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Live All-In panel with IBM's **Arvind Krishna** and Palo Alto Networks' **Nikesh Arora**.",
    "Quantum: midpoint estimate 2030 for breaking today's cryptography — post-quantum code exists but \"people have been too lazy\"; Nikesh: \"we're already late.\"",
    "Arvind expects 75-90% of all token usage to move to open-weight models: 40x cheaper for 95% of the work, IP control, and a 6-12 month gap to the frontier.",
    "Frontier models are for wartime: Nikesh runs 20-40 MB endpoint models at $20-30/year, but throws frontier LLMs at an active breach.",
    "Mythos-style models make cyber asymmetric — attackers need one bug; ~60-80% of model-found vulnerabilities are real, ~20% hallucinated.",
    "Nobody is slowing down; Arvind sees no 50-state data-center ban, but up to 30 states could ban — and the other 20 \"rub their hands in glee.\"",
    "Vertical integration is back (IBM's 65-year mainframe, Nvidia \"at the dirt\"), and enterprises will collapse 500-5,000 software vendors onto 5-10 platforms.",
]

THEMES = [
    {
        "id": "quantum-threat",
        "tags": ["software", "policy"],
        "color": "red",
        "badge": "Red flag",
        "status": "DARPA QBI: ~13 OF A COUPLE HUNDRED LEFT",
        "title": "Quantum breaks today's cryptography around 2030 — replace the stack now",
        "lead": "Arvind puts the midpoint at 2030 for a working quantum computer that breaks current encryption, and Nikesh says that means migration is already late.",
        "bullets": [
            "DARPA's Quantum Benchmarking Initiative started with a couple hundred companies; ~13 remain. Debate is 2028, 2029 or 2033 — midpoint 2030, when \"it will break today's cryptography.\"",
            "Harvest now, decrypt later: a stolen encrypted hard disk can be kept for 5 years and broken then. Post-quantum cryptography is well understood and the code is written — \"the wake-up moment is now.\"",
            "PQC is quantum-proof at the same rigor as today's crypto vs classical computers — grounded in complexity-theory assumptions, not a theorem-level proof.",
            "Milestones: today's machines are error-ridden \"toys\"; expect error-correction claims next year and one or two real progress by 2027. Gate computations sit ~10,000 — adding a zero a year means 10M by 2029. ~10,000 physical qubits ≈ ~200 logical.",
            "Nikesh: every vendor holds crypto keys across the whole IT stack; you can't rebuild it in a year, so swap in quantum-safe infrastructure now (post-quantum key wrapping as a stopgap). He guesses 50% of current IT spend goes to non-quantum-safe infrastructure.",
            "Can AI break crypto first, after the OpenAI math drop? Arvind: an AI can discover quantum algorithms but can't run them efficiently on classical hardware (Richard Feynman's point) — 1,000-10,000x slower; a better prime-distribution predictor is possible but impractical \"if it takes 10 years to break one key.\"",
        ],
        "quote": {"text": "if you pick the middle point, let's call it 2030, well, it will break today's cryptography. That's not a supposition, that's just a reality.", "cite": "— Arvind Krishna"},
        "watch": "Arvind runs a quantum business and Nikesh sells security infrastructure — both benefit from an early migration cycle.",
        "names": [
            {"name": "IBM (IBM)", "blurb": "Arvind's company; quantum computing builder", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "open-weight",
        "tags": ["software", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "OPEN-WEIGHT GAP TO FRONTIER: 6-12 MONTHS",
        "title": "Open-weight models will take 75-90% of tokens; frontier models are for emergencies",
        "lead": "Both CEOs conclude that most enterprise inference moves to self-run open-weight models, with frontier LLMs reserved for high-stakes moments.",
        "bullets": [
            "Nikesh's phase one: let teams use the best, easiest model to learn — 20,000-ish employees only discovered AI in the last 12-18 months. Don't cost-optimize during experimentation.",
            "Production: Palo Alto inspects hundreds of MB of traffic per endpoint for $20-30 a year with a 20-40 MB on-device model; routing that through OpenAI tokens would let OpenAI \"generate all their revenue in 1 year from one company.\" Compress small models until 99.9% accurate — \"you don't need a Ferrari for every task.\"",
            "Flip side: during a breach worth billions, customers say use whichever model — agent swarms and the top frontier LLM. Peacetime defender models will be open-weight, trained on proprietary data, for auditability and explainability.",
            "Arvind's economics: ~$20 per million tokens (up to $50) for frontier, vs **Kimi K3** (~800B parameters) self-hosted with a week of optimization at ~$1-2 — up to 40x cheaper for 95% of the work.",
            "IP: logged chain of thought gives away your IP, and no frontier lab will let you run their model yourself. Geopolitics: the best open-weight models are Chinese — low danger sandboxed and self-run; Western equals likely within a year or two.",
            "Arvind: \"Developers are lazy\" and default to the most expensive model unless controlled; frontier in production is worth it only for a tiny number of use cases.",
        ],
        "quote": {"text": "I don't know whether it'll be 75% to 90%, but that's the range I would put of all token usage will go to open weight models", "cite": "— Arvind Krishna"},
        "watch": None,
        "names": [
            {"name": "OpenAI", "blurb": "Token pricing makes frontier models impractical for always-on enterprise inspection", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "cyber-warfare",
        "tags": ["software", "geopolitics"],
        "color": "red",
        "badge": "Red flag",
        "status": "MYTHOS-ERA VULNERABILITY HUNTING",
        "title": "AI cyber warfare: attackers need one bug, defenders need all of them",
        "lead": "Models trained on everyone's code now find vulnerabilities at scale, and the panel's answer borrows from warfare: alliances, cheap defense, and technological superiority.",
        "bullets": [
            "Coding agents learned good code from users who don't have zero data retention (Claude Code users included), so they also learned bad code — Mythos' first trick was finding it, while hallucinating ~30% of the time.",
            "Room estimate: ~60-80% of model-found vulnerabilities are real, ~20% hallucinated; nobody patches with Claude Code without re-testing.",
            "Host: zero-data-retention terms (which Marc Benioff pushes hard for) don't rule out generating synthetic data — \"there's all these trapdoors.\" Nikesh: frontier labs \"are not going to get into my business.\"",
            "Nikesh: pool vulnerabilities through trusted parties and distribute patches to everyone at once, as threat intel already works.",
            "Arvind's war lessons: alliances stronger than the attacker; erase asymmetry by making defense as cheap as attack; and technological superiority (World War II, Korea, Iraq) is how wars are won.",
            "IBM: agents write about half its code and it's better, because agents run evals — but only flaws we know how to find are caught; full verification is computationally infeasible except where inputs are limited.",
            "Accountability: you can't unleash software and say \"oops\" — \"agent 74565 from my harness wrote it\" doesn't remove the company's product liability.",
        ],
        "quote": {"text": "the reason it's perfect for attackers is they just need one vulnerability.", "cite": "— Nikesh Arora"},
        "watch": "Nikesh says cyber valuations are inflated by the Mythos event while his own company sells the defense.",
        "names": [
            {"name": "Anthropic", "blurb": "Mythos model exposed vulnerability-finding at scale", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "politics-compute",
        "tags": ["policy", "geopolitics", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "CONGRESSMAN FLOATS 50-STATE DATA-CENTER BAN BY Q4",
        "title": "Nobody is stopping AI — the fight is over data centers, compute access and labor",
        "lead": "No country will pause, so the open questions are which states block data centers, who gets compute, and which nations accept labor displacement.",
        "bullets": [
            "Nikesh: \"nobody's stopping\" — the narrative over-rotated to AI's dark side; the Wright brothers didn't build TSA first. Arvind: Japan, China, India won't slow down; Europe shows what regulating first does to a tech economy.",
            "Host: a senior member of Congress said one of the biggest CEOs is \"completely freaked out about cyber,\" and floated a 50-state data-center ban by Q4.",
            "Arvind: AI and data-center regulation is \"driven by populism, not by any reality\"; hearings have run since 2022. No chance all 50 ban, but 30 could — \"the remaining 20 will rub their hands in glee.\" An election could shift the current balance.",
            "Nikesh: the haves-vs-have-nots risk isn't price but supply — compute concentrates in two countries, so a European company far from \"the epicenter\" may simply not get access.",
            "Arvind: it's the classic labor-vs-capital trade-off; capital-intensive sides won in each of seven or eight cycles since the 1700s, and nations that protect every existing job will lose.",
        ],
        "quote": {"text": "On data centers, I think there's no chance all 50 will ban. Is it possible 30 will ban? Yes.", "cite": "— Arvind Krishna"},
        "watch": "The Congress member and the CEO are unnamed, relayed secondhand by the host.",
        "names": None,
    },
    {
        "id": "vertical-stacks",
        "tags": ["semis", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "THE CONGLOMERATE IS BACK",
        "title": "Vertical integration wins — from IBM's mainframe to Nvidia \"at the dirt\"",
        "lead": "Controlling the whole stack lets you pick which layer to commoditize and move profit between layers; the AI application layer is heading the same way.",
        "bullets": [
            "IBM's mainframe has lasted 65 years because it was vertically integrated — in the '60s IBM went \"all the way to dirt\" (sand, wafers, fabs, chips, metal); today only fabs are outsourced, for scale.",
            "Nvidia is the modern version: Jensen bought **Hugging Face** and funds everyone in the ecosystem so they stay on his stack, shifting profit away from any layer under attack.",
            "Nikesh: it's open stack vs closed stack, not open vs closed models — context and memory can't be separated from reasoning, so routing models via OpenRouter becomes impossible over time.",
            "Pricing moves to cost per action across the full prompt-to-outcome path; memory makes switching stacks too costly — the personal agent trained on your context and APIs is the moat.",
            "In the next 3 months, every frontier lab goes full-court press on the Muse personal-agent concept now that Facebook showed it works — \"the largest battle of consumer control\"; every iPhone app has to become headless.",
        ],
        "quote": {"text": "if you control the vertical stack, you can decide which part of the stack to commoditize.", "cite": "— Arvind Krishna"},
        "watch": None,
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Modern vertically integrated stack; bought Hugging Face, funds the ecosystem", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "IBM (IBM)", "blurb": "Mainframe lasted 65 years through vertical integration", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Hugging Face", "blurb": "Bought by Nvidia, per the panel", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenRouter", "blurb": "Model-routing becomes impossible as context and memory bind to reasoning", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Meta (META)", "blurb": "Facebook showed the Muse personal-agent concept works", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "saas-consolidation",
        "tags": ["software", "finance"],
        "color": "red",
        "badge": "Negative view",
        "status": "M&A: ATTRACTIVE IN JANUARY, NOT A MONTH AGO",
        "title": "SaaS faces huge disruption; 500-5,000 vendors collapse onto 5-10 platforms",
        "lead": "Both CEOs expect enterprise software to consolidate hard, with only ultra-reliable systems of record safe from AI-built replacements.",
        "bullets": [
            "Nikesh: customers shouldn't buy 40 cyber products and stitch them. At Fidelity Investments he saw 23 home-grown systems that today would be one CRM — Salesforce, Microsoft Dynamics or Oracle.",
            "Cyber is enjoying better valuations \"because of the the AI mythos event\" — which \"will rationalize over time\" as everyone spends unlimited money on cyber.",
            "Outside cyber, terminal value of software is unclear; it's not clear what survives the next 5-8 years — \"huge disruption in the SaaS space over the next few years.\"",
            "Arvind: the average enterprise uses 500-5,000 vendors — a massive attack surface; replace 490 with minor AI capabilities and keep 5-10 main platforms, whether it takes 6 months or 6 years.",
            "Safe zone: interaction-rich software is replaceable, but systems needing 10^-15 reliability (retail-banking lookups, closing the books) are hard to replace and need a digital twin for years before cutover, with no cost advantage.",
            "M&A: Arvind found multiples very attractive at the start of the year, \"not so attractive a month ago.\"",
        ],
        "quote": {"text": "I think there's going to be huge disruption in the SaaS space over the next few years.", "cite": "— Nikesh Arora"},
        "watch": "Both run consolidating platforms that gain from vendor consolidation.",
        "names": [
            {"name": "Salesforce (CRM)", "blurb": "Consolidated CRM platform example", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "Consolidated CRM platform example", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Dynamics as a consolidated CRM platform example", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F510", "tag": "Security", "title": "Start the post-quantum migration now — inventory crypto keys and wrap traffic in post-quantum keys as a stopgap."},
    {"icon": "\U0001F4B0", "tag": "AI costs", "title": "Benchmark a self-hosted open-weight model against frontier tokens before scaling any production workload."},
    {"icon": "\U0001F6A8", "tag": "Cyber", "title": "Reserve frontier models and agent swarms for live incidents; re-test every AI-found vulnerability before patching."},
    {"icon": "\U0001F4C9", "tag": "Software", "title": "Stress-test SaaS holdings: interaction-heavy tools are exposed, ultra-reliable systems of record less so."},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Map data-center exposure by state — local bans are plausible even if a national one isn't."},
]

HOT_TAKES = [
    {"take": "if you pick the middle point, let's call it 2030, well, it will break today's cryptography. That's not a supposition, that's just a reality.", "cite": "— Arvind Krishna", "why": "dated quantum call"},
    {"take": "if he says it's 2029-30, we're already late.", "cite": "— Nikesh Arora", "why": "urgency call"},
    {"take": "I don't know whether it'll be 75% to 90%, but that's the range I would put of all token usage will go to open weight models", "cite": "— Arvind Krishna", "why": "numeric share call against frontier labs"},
    {"take": "Developers are lazy. They're going to use the most expensive the most expensive answer unless you put a control on it.", "cite": "— Arvind Krishna", "why": "provocative"},
    {"take": "The regulation question on AI and data centers is driven I'm going to be sorry and cynical is driven by populism, not by any reality.", "cite": "— Arvind Krishna", "why": "political dismissal"},
    {"take": "I think there's going to be huge disruption in the SaaS space over the next few years.", "cite": "— Nikesh Arora", "why": "SaaS bear call"},
]

CLAIMS = [
    {"who": "Arvind Krishna", "claim": "A quantum computer breaks today's cryptography around 2030 (range 2028-2033).", "metric": "cryptographically relevant quantum computer", "target": "breaks current crypto", "by": "2030", "condition": None, "entity": None},
    {"who": "Arvind Krishna", "claim": "Someone claims real quantum error correction next year, and one or two make verified progress by 2027.", "metric": "quantum error correction", "target": "demonstrated on running hardware", "by": "2027", "condition": None, "entity": None},
    {"who": "Arvind Krishna", "claim": "Quantum gate computations scale from ~10,000 to 10 million by 2029.", "metric": "quantum gate computations", "target": "10 million", "by": "2029", "condition": "if a zero is added each year", "entity": None},
    {"who": "Arvind Krishna", "claim": "75-90% of all token usage goes to open-weight models.", "metric": "open-weight share of tokens", "target": "75-90%", "by": None, "condition": None, "entity": None},
    {"who": "Arvind Krishna", "claim": "Western open-weight models match the Chinese ones within a year or two.", "metric": "Western open-weight capability", "target": "parity with Chinese open-weight", "by": "1-2 years", "condition": None, "entity": None},
    {"who": "Arvind Krishna", "claim": "Up to 30 US states could ban data centers, but not all 50.", "metric": "states banning data centers", "target": "up to 30", "by": None, "condition": None, "entity": None},
    {"who": "Member of Congress (cited by an All-In host)", "claim": "A 50-state ban on data centers could come by Q4.", "metric": "states banning data centers", "target": "50", "by": "2026-Q4", "condition": None, "entity": None},
    {"who": "Arvind Krishna", "claim": "Enterprises consolidate from 500-5,000 software vendors to 5-10 main platforms.", "metric": "software vendors per enterprise", "target": "5-10 platforms", "by": "6 months to 6 years", "condition": None, "entity": None},
    {"who": "Nikesh Arora", "claim": "Every frontier lab goes full-court press on Muse-style personal agents.", "metric": "frontier-lab personal-agent push", "target": "every lab", "by": "3 months", "condition": None, "entity": None},
    {"who": "Nikesh Arora", "claim": "Huge disruption hits the SaaS space; it's unclear what software survives.", "metric": "SaaS disruption", "target": "huge", "by": "5-8 years", "condition": None, "entity": None},
    {"who": "Nikesh Arora", "claim": "Cyber valuations lifted by the Mythos event will rationalize over time.", "metric": "cyber valuations", "target": "rationalize lower", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Nvidia (NVDA)", "rel": "acquires", "to": "Hugging Face", "note": "as stated by the panel"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4E2", "title": "Sources referenced: DARPA's Quantum Benchmarking Initiative, the OpenAI math drop, Richard Feynman on simulating across architectures, Marc Benioff on zero data retention, and an unnamed senior AI researcher who argued AI models will break crypto before quantum computers do.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Post-quantum cryptography (PQC)", "def": "Encryption designed to resist attacks from quantum computers; the algorithms and code already exist."},
    {"term": "Logical qubit", "def": "An error-corrected effective qubit; ~10,000 noisy physical qubits might yield ~200 logical."},
    {"term": "Harvest now, decrypt later", "def": "Stealing encrypted data today to break it once quantum computers arrive."},
    {"term": "ZDR", "def": "Zero data retention: a model provider promises not to store or train on customer data."},
    {"term": "Open-weight model", "def": "A model whose weights you can download and run yourself, unlike closed frontier models."},
    {"term": "Headless app", "def": "An app exposed through APIs for agents to use, without its own front-end."},
    {"term": "Cost per action", "def": "Pricing AI by completed task, prompt to outcome, rather than by token."},
]
