META = {
    "title": "Stanford HAI Managing Director: Are We Measuring AI Wrong? | Conversations in Action",
    "channel": "Imagination in Action",
    "speakers": "Vanessa Parli (Stanford HAI), John (host), Alex (co-interviewer)",
    "date": "2026-09-30",
    "video_url": "https://www.youtube.com/watch?v=6jbCrk13dio",
    "thread_line": "4 threads · benchmark obsolescence, measuring humans and wealth, sovereign AI, talent flows",
    "category": "dev",
}

SNAPSHOT = [
    "Interview with **Vanessa Parli**, managing director of Stanford HAI, which publishes the annual **AI Index** (launched 2017, spun out of the 5-yearly AI 100).",
    "Core tension: if AI moves daily, what is an **annual** report for? Her answer: independent, neutral, data-driven perspective that cuts through hype.",
    "Benchmarks are the weak spot: models saturate them within a year, and *passing the MCAT does not make a good doctor* — the field needs a science of measurement.",
    "Interviewer Alex pushes the Index to stop measuring AI capability and instead measure **real wealth creation**: \"we need something better than real GDP.\"",
    "The Index tracks sovereign AI via models, talent and compute; **AI talent inflow to the US fell ~80%** in recent years while India's rose.",
    "Science and medicine now get their own chapters (2026 report) because progress there is accelerating.",
]

THEMES = [
    {
        "id": "benchmarks-broken",
        "tags": ["ai-infra", "policy"],
        "color": "amber",
        "badge": "Structural critique",
        "status": "AI INDEX 2026",
        "title": "Benchmarks are saturated, flawed and need rethinking",
        "lead": "Every year's benchmarks get surpassed, so the field of benchmarking itself must be reconsidered now that AI is out of the lab.",
        "bullets": [
            "The Index adds new benchmarks each year because models have **surpassed human capability** on the prior ones; the lesson is asking what they actually measure.",
            "Alex cites recent revelations around *Epoch's FrontierMath Tier 4* that the benchmark was broken, so models sit below 100% because definitions were wrong — \"the benchmarks themselves are cooked.\"",
            "Parli: benchmarks like *ImageNet* (2012) were built for labs and did push research forward, but flaws are now known; it's \"a call to action.\"",
            "Stanford researchers are working on a **science of measurement** that predicts real-world deployed performance.",
            "Her example: a model that passes the **MCAT** is not thereby a good doctor.",
            "Alex's challenge: AI can already write the report; asked what she'd do with a hypothetical billion dollars, Parli says not all of it can be automated and she'd fund more robust datasets plus Stanford research on education and scientific discovery.",
        ],
        "quote": {"text": "If a model can pass the MCAT, that does not make it a good doctor.", "cite": "— Vanessa Parli"},
        "watch": "Alex frames recursive self-improvement as already here; Parli doesn't endorse that framing.",
        "names": None,
    },
    {
        "id": "measure-humans-wealth",
        "tags": ["macro-rates", "career"],
        "color": "gray",
        "badge": "Recommendation",
        "status": "PROPOSED DIRECTION, NOT BUILT",
        "title": "Measure the human side: augmentation and real wealth, not just AI capability",
        "lead": "Alex argues AI capability measurement is solved and the Index's biggest unmet gap is measuring real wealth creation.",
        "bullets": [
            "Parli agrees the Index is shifting toward humans: data gaps are largest in **education**, e.g. tracking CS education in K-12 globally; the data doesn't reflect the field.",
            "Work on **human-AI augmentation** cited: Stanford economist Erik Brynjolfsson, computer scientist Diyi Yang, and Anthropic research on how people use AI to augment themselves.",
            "Alex: GDP, nominal and real, \"goes haywire in the presence of true abundance\"; some forecasts say the economy triples year over year, but we can't measure it.",
            "Parli points him to Brynjolfsson's **GDP-B** project on the value of digital goods; Alex has read the papers.",
            "Alex wants a **real-time index of superintelligence**, noting the Fed releases GDP several times a month; Parli says upstream data checking is slow (\"just because you have data doesn't mean it's showing the thing you want\"), and Alex retorts that this is what AI is good at.",
        ],
        "quote": {"text": "We need something better than real GDP.", "cite": "— Alex"},
        "watch": "Parli declined to answer how to measure real wealth growth under superintelligence.",
        "names": None,
    },
    {
        "id": "sovereign-ai-talent",
        "tags": ["geopolitics", "policy"],
        "color": "amber",
        "badge": "Confirmed event",
        "status": "AI INDEX DATA",
        "title": "Sovereign AI, export controls and the talent shift",
        "lead": "The Index tracks sovereignty through models, talent and compute, and the talent data is moving sharply away from the US.",
        "bullets": [
            "The 2026 Index added a qualitative **AI sovereignty** section because the phrase is not well defined; the HAI policy team also released a report on how people use the term.",
            "Measured pieces so far: model development, in-country talent and in-country compute — not yet a single sovereignty metric.",
            "New talent data (from a firm tracking AI publications and patents): **inflow of AI talent into the US dropped 80%** over a few years (she can't recall exact numbers), while inflow into **India** is rising significantly.",
            "John's question: US export controls on Nvidia chips to China arguably pushed China toward more efficient open-source models. Parli: the Index didn't foresee it, but it raises questions on **effectiveness of export controls**.",
            "Alex: talent counts alone don't capture innovation, since anyone can now work with AI.",
        ],
        "quote": None,
        "watch": "The talent data vendor name is garbled in the captions and omitted; the 80% figure is Parli's approximate recall.",
        "names": None,
    },
    {
        "id": "why-annual-report",
        "tags": ["career", "dev-workflow"],
        "color": "green",
        "badge": "Principle",
        "status": "AI INDEX 2017-2026",
        "title": "Why an annual, independent index still matters",
        "lead": "Independent, neutral, comprehensive data gives perspective that daily AI-generated output can't replace.",
        "bullets": [
            "HAI is one of five Stanford units, created ~7-8 years ago as a cross-campus AI initiative; the AI Index is led by internal and external people from industry, academia and policy.",
            "AI 100 comes out every 5 years (next soon); the Index spun out because that cadence was too slow — and \"even now seems too long.\"",
            "An April road show takes the Index to different continents.",
            "Advice to graduating students: don't get caught up in hype, see what has happened and what's coming.",
            "Science and medicine began as highlights in the tech-performance chapter ~3 years ago, became a standalone chapter 2 years ago, and in 2026 split into separate science and medicine chapters.",
            "Next step: John and Alex plan a MIT-Stanford HAI collaboration update at Davos in January; Alex notes the irony of \"an AI index that's not using very much AI.\"",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CF", "tag": "AI evals", "title": "Treat a benchmark score as a proxy, and test models on your own real-world tasks."},
    {"icon": "\U0001F4B9", "tag": "Macro", "title": "Look beyond real GDP for AI-driven value, e.g. Brynjolfsson's GDP-B on digital goods."},
    {"icon": "\U0001F30D", "tag": "Geopolitics", "title": "Follow talent flows (US down, India up) as a sovereignty indicator, not just chips."},
    {"icon": "\U0001F4DA", "tag": "Research", "title": "Read the Stanford HAI AI Index each April for neutral, data-driven AI trends."},
    {"icon": "\U0001F9EC", "tag": "Science", "title": "Follow the science and medicine chapters: Stanford now treats them as separate fast-moving fields."},
]

HOT_TAKES = [
    {"take": "I think you're measuring the wrong thing.", "cite": "— Alex", "why": "challenges the Index's whole focus"},
    {"take": "Assume that measures of AI capabilities are thoroughly cooked. This is a solved problem.", "cite": "— Alex", "why": "dismisses AI capability measurement"},
    {"take": "Recursive self-improvement is here. The AI is improving day by day.", "cite": "— Alex", "why": "strong framing claim"},
    {"take": "GDP, nominal and real, arguably goes haywire in the presence of true abundance.", "cite": "— Alex", "why": "contrarian macro claim"},
]

CLAIMS = []

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Stanford AI Index and AI 100, Epoch's FrontierMath Tier 4 benchmark, ImageNet (2012), Erik Brynjolfsson's GDP-B, Diyi Yang, Anthropic's augmentation research, HAI policy team's AI-sovereignty report.", "tag": "Sources"},
    {"icon": "\U0001F3AF", "title": "Stated as a gap: **K-12 CS education data** is hard to get globally and the Index's chapter doesn't reflect the field's real state.", "tag": "Data gap"},
]

GLOSSARY = [
    {"term": "AI Index", "def": "Stanford HAI's annual data-driven report on the state of AI, launched 2017."},
    {"term": "AI 100", "def": "Stanford's five-yearly report on AI progress from which the AI Index spun out."},
    {"term": "GDP-B", "def": "Brynjolfsson's project valuing digital goods that standard GDP misses."},
    {"term": "Sovereign AI", "def": "A national capability over models, talent and compute; the term itself is not yet well defined."},
]
