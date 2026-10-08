META = {
    "title": "NVIDIA's CEO Just Said the UNTHINKABLE",
    "channel": "David Carbutt",
    "speakers": "Jensen Huang (Nvidia), Satya Nadella (Microsoft), unnamed moderator",
    "date": "2026-10-08",
    "video_url": "https://www.youtube.com/watch?v=SWhLHDJh_og",
    "thread_line": "3 threads · Windows-to-CUDA history · agent security primitive (MXC) · hybrid local/cloud AI PC",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Jensen Huang and Satya Nadella appear together at a Microsoft-Nvidia launch of a new AI PC line, including a **Surface Laptop Ultra** and a workstation.",
    "Huang: Nvidia exists because of Windows; DirectX led to programmable shaders, then CUDA, which gave deep-learning pioneers their compute.",
    "Nadella: Azure's InfiniBand HPC build produced the supercomputer that went to OpenAI to train GPT.",
    "**MXC** is a new Windows primitive for agent containment, identity, observability and governance, integrated with Nvidia's OpenShell.",
    "Nadella frames **hybrid intelligence**: local and cloud models routed seamlessly, so no one thinks \"this runs locally, this runs in the cloud\".",
    "New device runs a single Nvidia superchip with **1 petaflop**, DirectX, OpenGL and every CUDA app natively, with 200+ applications tested.",
    "Agent liability and trust: Nadella expects insurance to price agent-delegated purchases.",
]

THEMES = [
    {
        "id": "windows-cuda-history",
        "tags": ["ai-infra", "semis", "software"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "MICROSOFT-NVIDIA LAUNCH, OCT 2026",
        "title": "Windows made Nvidia; Azure's HPC build made OpenAI's supercomputer",
        "lead": "Both CEOs frame the AI PC as the next step of a 30-year joint arc from DirectX to CUDA to GPT.",
        "bullets": [
            "Huang: Nvidia was founded in 1992-93 because of Windows 3.1; Windows 95 and **DirectX/Direct3D** connected the GPU to the PC.",
            "DX8 co-invented with Microsoft the first programmable GPU (programmable shaders), which led to CUDA and enabled Krizhevsky, Sutskever, LeCun and Ng to do deep learning.",
            "Nadella: Azure was the first cloud user of InfiniBand for HPC, which produced the first supercomputer given to OpenAI to train GPT.",
            "Four years ago the pair discussed building the perfect PC for the agent era, with Nvidia's creative and engineering tools (Blender, Unreal, Omniverse and others) on the same machine as the AI.",
            "Nadella: Windows has been with him 34 years and will be for 34 more; Windows never leaves code or frameworks behind.",
        ],
        "quote": {"text": "If not for Windows, Nvidia wouldn't have been founded.", "cite": "— Jensen Huang"},
        "watch": "Both speakers sell the product on stage together, and Nvidia and Microsoft are each other's partners and customers in the OpenAI supply chain.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Built the PC superchip and CUDA stack; Huang tells the origin story", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Windows, Azure and Surface hardware partner", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "OpenAI", "blurb": "Received the first Azure InfiniBand supercomputer to train GPT", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "agent-security-mxc",
        "tags": ["software", "ai-infra", "policy"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "ANNOUNCED OCT 2026",
        "title": "MXC makes the OS the security layer for AI agents",
        "lead": "Nadella and Huang argue agents cannot diffuse without containment, identity and governance built into the operating system.",
        "bullets": [
            "MXC is a new Windows primitive for agent containment at the microVM, VM and **Windows session** levels.",
            "Chain Nadella lays out: containment, then an agent identity separate from the user, then observability of its \"exhaust\", then policy governance, plus token-spend tracking.",
            "Nvidia's OpenShell is natively integrated with MXC; the design is meant to be heterogeneous, not Microsoft-only.",
            "Coding agents came first and run on the local harness with full file-system access, which is why the desktop needs the primitive most.",
            "Nadella: agents will be the biggest users of file systems, and better tool users than people (people know 10-15% of an app's features).",
            "Delegation authority is the first decision; Nadella expects insurance markets to price agent-made purchases, with protocols like OAuth as the easy part.",
        ],
        "quote": {"text": "MXC is going to revolutionize how agents are built and deployed.", "cite": "— Jensen Huang"},
        "watch": "Huang and Nadella present their own jointly built product as foundational; the liability question is described as unresolved.",
        "names": [
            {"name": "Microsoft (MSFT)", "blurb": "MXC primitive in Windows", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "OpenShell integrated with MXC", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "hybrid-ai-pc",
        "tags": ["ai-infra", "semis", "software"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "NEW HARDWARE, OCT 2026",
        "title": "Hybrid intelligence: one superchip PC runs local and cloud models together",
        "lead": "The new PC unifies gaming, workstation and AI compute so agents and tools run side by side on-device.",
        "bullets": [
            "A demo moved between ComfyUI, Blender, Photoshop and Unreal with local models, then cloud rendering with a cloud service called Astra; days of work took hours.",
            "The superchip delivers **1 petaflop**; the DGX-1 that started the AI revolution was 1 petaflop, a quarter-billion dollars and 500 lb.",
            "Huang: the only computer running DirectX, OpenGL and every CUDA application natively; 4,000+ engineering years and 200+ apps tested.",
            "Every major laptop, desktop and workstation maker joined the launch.",
            "Nadella compares it to Mosaic uniting terminal, PC and Usenet: users won't distinguish local from cloud.",
            "Local inference is described as \"tokens for free\" by a GitHub presenter; the tax-filing demo had an agent gather files from downloads, cloud and email into a container.",
        ],
        "quote": {"text": "There will never be a moment where we look and say, oh, this runs locally, this runs in the cloud.", "cite": "— Satya Nadella"},
        "watch": "The \"free tokens\" line is a presenter's claim at the launch; no pricing or shipment dates were given.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Superchip and DGX heritage", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Adobe (ADBE)", "blurb": "Photoshop in the demo", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Autodesk (ADSK)", "blurb": "Design tools named among workstation apps", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Siemens", "blurb": "Design tools named among workstation apps", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F5A5", "tag": "AI infra", "title": "Track the Surface Laptop Ultra and Nvidia-based workstation launch for shipping dates and pricing."},
    {"icon": "\U0001F512", "tag": "Software", "title": "Watch adoption of MXC and OpenShell as the enterprise gate for deploying agents."},
    {"icon": "\U0001F4B0", "tag": "Policy", "title": "Follow agent-liability and insurance pricing as a missing piece of agentic commerce."},
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Note the pitch for a CUDA-native PC as a demand driver beyond data centers."},
]

HOT_TAKES = [
    {"take": "If not for Windows, Nvidia wouldn't have been founded.", "cite": "— Jensen Huang", "why": "Origin claim"},
    {"take": "MXC is going to revolutionize how agents are built and deployed. Without it, complete non-starter.", "cite": "— Jensen Huang", "why": "Strong product claim"},
    {"take": "There will never be a moment where we look and say, this runs locally, this runs in the cloud.", "cite": "— Satya Nadella", "why": "Prediction"},
    {"take": "Insurance will price this.", "cite": "— Satya Nadella", "why": "Prediction on agent liability"},
    {"take": "These agents are going to be better users of tools than us.", "cite": "— Jensen Huang", "why": "Contestable claim"},
]

CLAIMS = [
    {"who": "Satya Nadella", "claim": "Insurance markets will price the risk of agents transacting on a user's behalf.", "metric": "agent liability pricing", "target": "insurance-priced", "by": None, "condition": None, "entity": None},
    {"who": "Satya Nadella", "claim": "Windows will still be with him in 34 more years.", "metric": "Windows longevity", "target": "34 more years", "by": None, "condition": None, "entity": "Microsoft (MSFT)"},
]

RELATIONS = [
    {"from": "Microsoft (MSFT)", "rel": "partners_with", "to": "Nvidia (NVDA)", "note": "AI PC, MXC and OpenShell integration"},
    {"from": "Microsoft (MSFT)", "rel": "supplies", "to": "OpenAI", "note": "Azure InfiniBand supercomputer built for GPT training"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources: no outside publications cited; the DGX-1 and Mosaic are historical references.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "MXC", "def": "A Windows primitive for agent containment, identity, observability and governance."},
    {"term": "OpenShell", "def": "Nvidia's agent runtime, integrated natively with MXC."},
    {"term": "Hybrid intelligence", "def": "Routing work between local and cloud models without the user choosing."},
]
