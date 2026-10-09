"""Data file for a16z — Former Intel CEO: Why This is the Best Time to Build Hardware."""

META = {
    "title": "Former Intel CEO: Why This is the Best Time to Build Hardware",
    "channel": "a16z",
    "speakers": "Pat Gelsinger (Playground Global, ex-Intel CEO), Guido Appenzeller and Raghu Raghuram (a16z)",
    "date": "2026-10-09",
    "video_url": "https://www.youtube.com/watch?v=1Q_7yU7FZ1k",
    "thread_line": "6 threads · AI makes chip design easy so fab, packaging and racks become the bottleneck, ~100 AI chip startups will consolidate, memory is due its first real innovation in 30 years, optics replace copper for scale-up around 2028-29, energy and power delivery cap the AI build-out, and a 'VMware for agents'.",
    "category": "market",
}

SNAPSHOT = [
    "Gelsinger's frame: when AI makes a step easy, the **bottleneck moves** — chip design now takes ~3 months, but fab, advanced packaging and rack integration still take ~9 months, so he wants new lithography and cheaper prototyping.",
    "He expects the field of roughly **100 AI inference chip vendors to consolidate**: workloads keep shifting, capital and scale favor few winners, and big buyers (OpenAI, Nvidia, Anthropic) will pick favorites; Guido argues AI-written kernels make heterogeneity cheaper.",
    "HBM is 'a hideous memory' yet the best available; zero major new memories in 30 years, but the memory industry has added ~$2.5T of market cap in four years, so **memory innovation is 'nigh upon us'**.",
    "He is against optics off-package memory and processing-in-memory, favors **2-4 high memory stacks**, and wants optics for all I/O (not the core compute-memory complex).",
    "Optical scale-up (NPO/CPO) is his **2028-29** conversion point; copper reach is shrinking, and he says NVL72 cost the industry an extra 18 months.",
    "Energy capacity equals economic capacity: US capacity grew ~4%/yr, gas-turbine lead times are ~8 years, and he expects more **data-center project defaults** for lack of power; 800V DC and vertical GaN rebuild power delivery.",
    "Closing thesis: agent swarms need their own virtualization layer (a 'VMware for agents', 'vMotion for agents') with policies, security and dashboards.",
]

THEMES = [
    {
        "id": "bottleneck-moves",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "AI CHIP-DESIGN TOOLS — DESIGN FAST, MANUFACTURE SLOW",
        "title": "AI makes chip design easy, so fab, packaging, racks, power modeling and memory become the limits",
        "lead": "Gelsinger can design a chip in 3 months with AI tools but needs 9 more months to use it at scale, and that gap is where the opportunity sits.",
        "bullets": [
            "Raghu/Guido frame: 'whenever you have the technology to make something easy, the bottleneck moves somewhere else'; AI is already strong at software layers and kernels.",
            "Logic design can be largely done with AI tools and a few experts, so the 486 era comparison holds (the 486 introduced modern EDA); **analog (SerDes) is still not automatable** without lots of silicon data.",
            "Timeline: **~3 months design, ~3 months out of fab, ~3 months advanced packaging**, then rack-scale integration — 'nothing's a chip anymore, it's a rack'.",
            "Wants new lithography and flows that avoid **$50M mask costs** before prototyping, compressing the cycle to 1-2 months; at 18 months to scale, the workload assumptions are stale (Graphcore as the cautionary example).",
            "Power modeling is poor: no good 3D tools for dissipation hotspots, so designers guard-band ~40% of the power envelope.",
            "His own early career: Intel technician at 18, engineer number four on the 386, architect/design manager on the 486 (built Intel's HDL, compiler and placement/routing with Berkeley, cited Alberto Sangiovanni-Vincentelli's group).",
        ],
        "quote": {"text": "Nothing's a chip anymore. It's a rack. It took me 3 months to design it, but it's 9 months until I can actually start to use it.", "cite": "— Pat Gelsinger"},
        "watch": "Gelsinger is a general partner at Playground Global, which funds hardware startups across these bottlenecks (memory, power, superconducting compute).",
        "names": [
            {"name": "Intel (INTC)", "blurb": "Gelsinger's career employer; 386/486 design history.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Playground Global", "blurb": "Gelsinger's venture firm; backs hardware startups across compute, memory and power.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "chip-consolidation",
        "tags": ["semis", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "ABOUT 100 AI INFERENCE ACCELERATORS TODAY",
        "title": "Roughly 100 AI chip vendors will narrow to a few winners",
        "lead": "Gelsinger gives three reasons the field converges; Guido pushes back that AI-written software makes heterogeneity cheaper.",
        "bullets": [
            "**Reason 1:** workload shifts (prefill vs decode vs 'midfill', reasoning models wanting CPU-like compute) make fine-grained specialization unsustainable.",
            "**Reason 2:** models are hitting LLM limits (3D, molecules, imaging), and HPC-style **64-bit precision** returns, e.g. chemistry algorithms after AI picks the five domains to test.",
            "**Reason 3:** scale needs capital and workloads; 100 vendors 'defies logic' and big buyers like OpenAI, Nvidia and Anthropic will back specific chips with software co-design.",
            "Guido's counter: a first-tier chip startup is defined by its anchor customer, and an agent swarm can write an optimized kernel overnight, easing the software constraint on heterogeneity.",
            "Gelsinger's reply: ~18 months to build, and **$50B** of capex plus data-center power commitments favor few architectures; big players absorb heterogeneity (Nvidia with Groq), so in two years 'you won't tell what Groq is inside Nvidia'.",
            "Training and inference will blur via **continuous learning**, weakening the case for separate inference architectures; Guido notes diffusion vs 15-trillion-parameter LLM workloads may still need different cards, Gelsinger sees only limited room.",
        ],
        "quote": {"text": "Historically, there have not been a hundred competing processor vendors in any industry ever.", "cite": "— Pat Gelsinger"},
        "watch": "Both the host and guest invest in AI chip startups ('you funded your fair share too').",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Absorbing heterogeneity (Groq); NVL72 called an engineering marvel and manufacturing nightmare; named as a picker of winners.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Groq", "blurb": "Referenced as what Nvidia folded in; 'two years from now you won't tell what Groq is inside Nvidia'.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenAI", "blurb": "Named as a big buyer that will pick chip winners.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Anthropic", "blurb": "Named as a big buyer that will pick chip winners.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Graphcore", "blurb": "'Wasn't a bad design but the world moved on' — long build cycle as the risk.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "memory-innovation",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "FIRST NEW MEMORY INNOVATION IN ~30 YEARS",
        "title": "Memory: HBM is 'hideous' but stays, and real innovation is finally funded",
        "lead": "AI is a memory-bound workload, memory vendors are among the most valuable companies, and the money now justifies breaking the physics.",
        "bullets": [
            "Zero major new memory types in 30 years (DRAM, SRAM, flash); Gelsinger has been involved in **five new memory attempts** (Optane died) and knows ~100 more.",
            "HBM drawbacks: poor bit density, shoreline-bandwidth limits, power and thermals (DRAM dislikes heat) — 'the best one we have', like democracy.",
            "Memory was a one-in-five-years profit industry; now **all three big memory vendors are in the top 20** most valuable companies, with ~**$2.5T** added in four years.",
            "Gelsinger's picks: bring memory and compute together (D-Matrix), stacking, **ferroelectrics**, non-capacitive high-density memory; he has seeded a stealth memory company; skeptical of flash/MRAM speed.",
            "Stack height: yield must improve exponentially with layers, so he expects **2-4 stacks** of memory (a 16 or 32 stack is 'crazy'); a package already totals ~8 layers with power and RDL.",
            "Against: all-optical memory off package (O-E-O conversion losses, femtojoules per compute vs per-bit comms ~1,000x worse) and PIM (constrains workloads; around 25-30 years and 'still hanging around').",
            "Heat and cooling: new materials such as diamond and liquid cooling are 'plumbing' for engineers.",
        ],
        "quote": {"text": "Memory innovation for the first time in 30 years is nigh upon us.", "cite": "— Pat Gelsinger"},
        "watch": "Gelsinger's firm backs D-Matrix and a stealth memory startup he mentions; his skepticism of PIM and optical memory is a stated view, which he allows he 'could be wrong' on.",
        "names": [
            {"name": "D-Matrix", "blurb": "Playground portfolio company bringing memory and compute together.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "optics-copper",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "OPTICAL SCALE-UP — 2028-29 TIMEFRAME",
        "title": "Optics replace copper in scale-up around 2028-29, and optical circuit switching fits AI flows",
        "lead": "Copper reach is collapsing, so everyone moves to NPO/CPO — Gelsinger's 25-year bet on 'the death of copper' is finally coming due.",
        "bullets": [
            "Copper is becoming a waveguide: making copper work at **5 m** now costs more than optical at **100 m**.",
            "He says NVL72 'should never have been built' — an engineering marvel and manufacturing nightmare that cost the industry **~18 months**, and a mature optical supply chain would have made better scale-up.",
            "Expected conversion: NPO/CPO in **2028-29**, which Nvidia has indicated and 'everybody else expects'; issues: thermals (optics hate heat), laser capacity, package integration, 10M-GPU scale.",
            "AI traffic is large and predictable, so **optical circuit switching** fits (Nick McKeown's framing); the boundary between scale-up and scale-out dissolves with a big enough radix.",
            "All I/O to optical, but not the core compute-memory complex.",
        ],
        "quote": {"text": "I declared the death of copper about 25 years ago. Eventually, I'll be right.", "cite": "— Pat Gelsinger"},
        "watch": None,
        "names": [],
    },
    {
        "id": "energy-power",
        "tags": ["energy", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "ENERGY AS THE UPPER BOUND ON AI",
        "title": "Energy capacity caps the AI build-out and power delivery gets rebuilt",
        "lead": "In an AI age 'energy capacity equals economic capacity', and Gelsinger expects projects to default where power doesn't show up.",
        "bullets": [
            "US energy capacity was flat for **10-15 years** (coal offline as fast as renewables came on) and now grows ~**4% per year**.",
            "Gas turbine lead times are about **8 years**; nuclear last came online in the US ~20 years ago; renewables depend on China.",
            "Prediction: more **defaults on data-center projects** for lack of power, a headwind and upper bound; he says early indicators are already visible (the caption for the example is garbled).",
            "**800V DC** data centers remove conversion steps ('revenge of Edison'); vertical GaN could go 800 to 48/12/5 V in one step; solid-state transformers and switches rebuild the grid side.",
            "Compute efficiency has flatlined: power per teraflop has not improved across five Nvidia generations; he points to a superconducting startup (Snowcap) aiming at ~1,000x better power performance.",
            "'Power's cool again' — turbines, refrigerants and cooling become exciting hardware again.",
        ],
        "quote": {"text": "Why build a new data center and buy the million GPUs if I can't power them?", "cite": "— Pat Gelsinger"},
        "watch": "Gelsinger's firm backs a superconducting company (Snowcap) and a vertical GaN power company, which colors his energy picks.",
        "names": [
            {"name": "Snowcap", "blurb": "Playground superconducting company aiming for a fundamental power-physics change.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "vmware-for-agents",
        "tags": ["software", "ai-infra"],
        "color": "gray",
        "badge": "Speculative",
        "status": "VIRTUALIZATION FOR AGENT SWARMS",
        "title": "A 'VMware for agents': virtualization and management rebuilt for AI agents",
        "lead": "Every innovation leads to the next abstraction, and agent swarms need security, performance, migration and policy layers.",
        "bullets": [
            "A host asks about 'VMs are back' — Gelsinger says the virtual machine is a **foundational abstraction** that deserves a place in the hierarchy.",
            "Agent questions: who manages agents, sets security profiles and monitors performance? Every element of virtualization and management must be recreated.",
            "Design constraint flips: VMs now serve agents instead of hardware and humans; Guido notes agents are less patient and pick offerings, changing form factor and go-to-market.",
            "Concept: **vMotion for agents**, with humans setting policy (he cites Dario Amodei's constitution), guardrails and dashboards.",
            "A host jokes it's 'time to go back and run VMware again'.",
        ],
        "quote": {"text": "Who's going to manage the agents? Who's going to create the security profiles around all of the agents?", "cite": "— Pat Gelsinger"},
        "watch": "Gelsinger is a former VMware CEO and now an investor who says such companies will break through.",
        "names": [
            {"name": "VMware", "blurb": "Gelsinger's former company; abstraction model used as the template for agent management.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9F1", "tag": "Semis", "title": "Look at fab time, advanced packaging and rack integration, not design speed, as the real constraint on new AI chips."},
    {"icon": "\U0001F9E0", "tag": "AI chips", "title": "Treat the 100-vendor accelerator field as temporary; favor teams with anchor customers, scale capital and software co-design."},
    {"icon": "\U0001F4BE", "tag": "Memory", "title": "Track stack-height limits (2-4 high), ferroelectric and new-memory startups as the next memory cycle."},
    {"icon": "\U0001F4A1", "tag": "Optics", "title": "Plan for NPO/CPO scale-up around 2028-29 and watch laser capacity and thermal limits."},
    {"icon": "⚡", "tag": "Energy", "title": "Price in power availability, not just GPUs, when underwriting data-center projects; expect defaults where energy is missing."},
    {"icon": "\U0001F916", "tag": "Software", "title": "Look for agent management, security and policy layers as the next virtualization-style category."},
]

HOT_TAKES = [
    {"take": "Historically, there have not been a hundred competing processor vendors in any industry ever. This is a temporary thing. It'll converge back.", "cite": "— Pat Gelsinger", "why": "Predicts AI chip startup shakeout"},
    {"take": "In reality, I should have never built an NVL72. It's an engineering marvel and it's a manufacturing nightmare.", "cite": "— Pat Gelsinger", "why": "Criticizes Nvidia's flagship rack design"},
    {"take": "I declared the death of copper about 25 years ago. Eventually, I'll be right.", "cite": "— Pat Gelsinger", "why": "Optics-replace-copper call"},
    {"take": "Memory innovation for the first time in 30 years is nigh upon us.", "cite": "— Pat Gelsinger", "why": "Predicts a break from 30 years of no new memory"},
    {"take": "I think you're going to see more and more defaults happening on many of those data center projects because the energy won't be there.", "cite": "— Pat Gelsinger", "why": "Predicts project defaults"},
    {"take": "Most PIM ideas have been around for 25-30 years, and 25-30 years from now they'll still be hanging around.", "cite": "— Pat Gelsinger", "why": "Dismisses processing-in-memory"},
]

CLAIMS = [
    {"who": "Pat Gelsinger", "claim": "Industry moves to near-package or co-packaged optics for scale-up as the conversion point.", "metric": "NPO/CPO scale-up adoption", "target": "conversion point", "by": "2028-2029", "condition": None, "entity": None},
    {"who": "Pat Gelsinger", "claim": "The roughly 100 AI inference accelerator vendors narrow to a few winners.", "metric": "number of AI chip vendors", "target": "few winners", "by": "2-4 years", "condition": None, "entity": None},
    {"who": "Pat Gelsinger", "claim": "More data-center projects default because power is unavailable.", "metric": "data-center project defaults", "target": "increase", "by": None, "condition": "energy not available", "entity": None},
    {"who": "Pat Gelsinger", "claim": "Memory stacks settle at 2-4 high, not 16-32 high.", "metric": "memory stack height", "target": "2-4 high", "by": None, "condition": None, "entity": None},
    {"who": "Pat Gelsinger", "claim": "A major new memory type emerges after ~30 years without one.", "metric": "new memory architecture", "target": "emerges", "by": None, "condition": None, "entity": None},
    {"who": "Pat Gelsinger", "claim": "Design-to-silicon-at-scale time can be compressed from nine months to one or two months.", "metric": "fab-to-scale cycle", "target": "1-2 months", "by": None, "condition": "new lithography and cheaper prototyping flows", "entity": None},
    {"who": "Pat Gelsinger", "claim": "Vertical GaN can convert 800V to 48V, 12V or 5V in one step.", "metric": "800V DC conversion steps", "target": "one step", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Playground Global", "rel": "invests_in", "to": "D-Matrix", "note": "Gelsinger: 'we have a company D-Matrix'"},
    {"from": "Playground Global", "rel": "invests_in", "to": "Snowcap", "note": "superconducting computing company"},
]

OTHER_NEWS = [
    {"icon": "\U0001F393", "title": "Gelsinger's origin: won a scholarship at 16, started at Intel at 18 as a technician; studied at Stanford while at Intel (advisor John Hennessy, Ed McCluskey on built-in self test); he mentions an a16z academy for talent aged 16-22.", "tag": "Careers"},
    {"icon": "\U0001F4DA", "title": "Sources/people referenced: Dario Amodei (constitution), Nick McKeown (AI traffic and switching), Alberto Sangiovanni-Vincentelli (EDA), John Hennessy, Ed McCluskey, OpenAI (speculative decoding discussion).", "tag": "Sources"},
    {"icon": "\U0001F4A1", "title": "Kernel writing: Guido cites an example where humans can't program a chip anymore but an agent swarm can overnight.", "tag": "AI"},
]

GLOSSARY = [
    {"term": "NPO / CPO", "def": "Near-package and co-packaged optics: optical I/O placed next to or inside the chip package."},
    {"term": "Scale-up vs scale-out", "def": "Scale-up is the tightly coupled network inside a rack or pod; scale-out links many racks, now converging."},
    {"term": "OCS", "def": "Optical circuit switching: fixed optical paths suited to large, predictable AI traffic flows."},
    {"term": "PIM", "def": "Processing-in-memory: pushing compute into memory chips to reduce bandwidth needs."},
    {"term": "800V DC", "def": "High-voltage direct-current data-center power that removes conversion steps."},
    {"term": "Prefill / decode / midfill", "def": "Phases of LLM inference (prompt processing, token generation, and a proposed middle tier)."},
]
