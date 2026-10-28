META = {
    "title": "holy sh*t JENSEN!!!",
    "channel": "Meet Kevin",
    "speakers": "Kevin Paffrath (host), with clips of Jensen Huang from an Altimeter Capital interview",
    "date": "2026-10-27",
    "video_url": "https://www.youtube.com/watch?v=LpMoj9cnfCo",
    "thread_line": "4 threads · the 6-month capability break · enterprise spend as AI's second underwriter · Nvidia's 2-year order book · PEG math on NVDA vs AMD",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Kevin Paffrath reacts to Jensen Huang telling Altimeter Capital that **six months ago** \"this technology barely worked.\"",
    "His read: 2024-25 was an AI \"black hole\"; the memory-wall breakthrough at end-2025 enabled the Claude coding moment, and 2026 spread it to video, HR, legal, customer service and web design.",
    "He reverses his own thesis: AI capex is **not** underwritten only by OpenAI and Anthropic — enterprise spend on open-weight models is a second, broader underwriter.",
    "Now thinks the labor market rolls over **before** enterprise AI spend stops; jobs still absorbing layoffs, turn likely at least a year out.",
    "Nvidia's largest customers forecast 1-2 years out, so orders already reach into 2028-29; Vera Rubin Ultra is near order time, sight unseen.",
    "Consensus Nvidia 2026 earnings line moved from $253 to $383 since January (+50%), ~3x higher by 2029 per the Altimeter chart.",
    "PEG math: Nvidia 0.675 vs AMD 1.27 — he puts Nvidia fair value near $775 and AMD near $1,080; owns and keeps buying Nvidia, recently added Tesla.",
    "Keeps the \"buy the dip at 700\" call on QQQ (now ~720); an Iran deal would mean 700 is never seen again.",
]

THEMES = [
    {
        "id": "six-month-break",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "JENSEN: \"IT WASN'T BUT 6 MONTHS AGO\"",
        "title": "Jensen admits AI \"barely worked\" six months ago — and Kevin says that's the whole bull case",
        "lead": "The capability jump of the last six months, not the 2023-25 spend, is what justifies AI capex now.",
        "bullets": [
            "Jensen called 2023 the year of the chatbot and 2024 the year of agents; Kevin calls **2024-25 a black hole** where spending outran results.",
            "Breaking the **memory wall** at end-2025 sent memory stocks \"berserk\" and enabled longer context with fewer coding hallucinations.",
            "In 2026 the gains spread past coding to video, HR, customer service, legal document editing and web design — a 50-page contract no longer needs one-paragraph-at-a-time edits.",
            "Claude Fable on medium mode or Opus 5.5 can now edit a video, build a site or an app; good coders keep jobs because someone still decides what to build.",
            "Model-agnostic: Muse, Grokbot or Claude all feed the same market — bears whose view is set by 2023-24 hallucinations should retry.",
            "Anthropic's Q2 2026 revenue spike makes **pre-Q2-lap** the ideal IPO window, before year-over-year growth optics fade.",
        ],
        "quote": {"text": "It wasn't but 6 months ago. This technology barely worked.", "cite": "— Jensen Huang (Altimeter Capital interview)"},
        "watch": "Jensen has been selling AI since 2023 and Kevin says he's \"going to be biased\" — the admission is notable precisely because of who says it.",
        "names": [
            {"name": "Anthropic", "blurb": "IPOing ahead of its Q2 lap; Kevin finds it 'less interesting' than 6 months ago as the market broadens — must become the daily-use platform incl. cheaper models", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "enterprise-underwriter",
        "tags": ["ai-infra", "macro-rates"],
        "color": "green",
        "badge": "View change",
        "status": "KEVIN REVERSES HIS \"FRONTIER-ONLY\" CANARY",
        "title": "Enterprise open-weight spend joins OpenAI and Anthropic as AI's underwriter",
        "lead": "Kevin drops his thesis that only frontier labs keep the AI spending going — enterprises buying hardware for open-weight models now carry it too.",
        "bullets": [
            "His two canaries: the **labor market** and the frontier underwriters (OpenAI, Anthropic); Jensen called it a mistake to think a couple of companies fund the buildout.",
            "Builders list: Anthropic, OpenAI, SpaceX, Meta, Microsoft, Amazon, Google; ASIC designers Marvell, Broadcom, Oracle; chips AMD, Nvidia; memory Micron.",
            "Enterprise demand is why Dell and AMD are doing so well — open-weight models get within ~90% of the frontier, or ~6 months behind it, on owned chips.",
            "Fable at **$50 per million output tokens** is ~100x the cost of a recent Qwen model from Alibaba.",
            "Labor: 16,750 jobs created in the latest print, pacing ~60,000/month; layoffs still being absorbed, turn \"at least a year out.\"",
            "Jensen: cloud computing for the next generation is \"AWS for today\" and about a third of Nvidia's business.",
        ],
        "quote": {"text": "It is wrong to say it is only the frontier. It is not only the frontier. It is also enterprise spend.", "cite": "— Kevin Paffrath"},
        "watch": None,
        "names": [
            {"name": "OpenAI", "blurb": "one of the two frontier 'underwriters' Kevin no longer sees as the sole funder", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Dell (DELL)", "blurb": "doing well on enterprise AI spend", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Alibaba (BABA)", "blurb": "Qwen open-weight models ~100x cheaper per token than Fable", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Marvell (MRVL), Broadcom (AVGO), Oracle (ORCL)", "blurb": "custom ASIC / larger infrastructure plays in the builder stack", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Micron (MU)", "blurb": "memory slot in the builder stack", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Meta (META), Microsoft (MSFT), Amazon (AMZN), Alphabet (GOOGL)", "blurb": "hyperscalers funding the buildout alongside the labs", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "order-book",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "ORDERS REACH INTO 2028-29",
        "title": "Nvidia's 2-year order book and a $100B Vera Rubin Ultra check, sight unseen",
        "lead": "Nvidia's largest customers forecast two years out, giving it visibility into 2029 and pushing consensus earnings sharply higher.",
        "bullets": [
            "Customers forecast at least a year ahead, the largest two years — Kevin reads that as orders across 2027-28 bleeding into **2029**.",
            "Jensen: for **Vera Rubin Ultra** it's \"close to placing order time\"; buyers commit $100B sight unseen because Grace Blackwell and Vera Rubin delivered.",
            "Altimeter chart: Nvidia's 2026 earnings line was $253 at the start of the year, now $383 — ~50% higher, and ~3x higher by 2029.",
            "Kevin credits the jump to the functionality inflection: \"the AI is getting good.\"",
        ],
        "quote": {"text": "Because Nvidia builds it, you know it's going to be better than Vera Rubin.", "cite": "— Jensen Huang"},
        "watch": "Kevin frames this as Jensen \"building the pitch for Nvidia\" on reputation; the forward-order claim is the CEO's own.",
        "names": None,
    },
    {
        "id": "peg-valuation",
        "tags": ["semis", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "OWNS NVDA, KEEPS BUYING",
        "title": "PEG math says Nvidia is half AMD's price — Kevin targets $775 NVDA, ~$1,080 AMD",
        "lead": "On price-to-earnings-growth, Nvidia at 0.675 is half AMD's 1.27, and both look cheap against a ~2.4 fair PEG.",
        "bullets": [
            "Nvidia growth forecasts 69.51%, 34.82%, 18.32%, 15.13% average **34.43%**; Jan-27 PE ~23.3 at a $218 share price → PEG 0.675.",
            "AMD growth 55.88%, PE 71 → PEG 1.27; he flags **Ryzen Pro** as under-watched because it's buried in the gaming segment.",
            "At a 2.4 PEG Nvidia is worth ~$775 — an over-$10T company he concedes \"sounds crazy\"; AMD roughly doubles to ~$1,080.",
            "AMD moves faster on momentum as the smaller company; Kevin owns Nvidia and keeps buying, recently bought more Tesla.",
            "Morning day-call: AMD and Bloom Energy as the plays — AMD closed up ~5% intraday.",
            "Tesla is his way to get SpaceX exposure ahead of the merger (covered in a separate video).",
            "QQQ: buy the dip at 700, now ~720 after repeated bounces off that shelf; an Iran deal means 700 is gone for good.",
        ],
        "quote": None,
        "watch": "Kevin holds Nvidia and Tesla and runs a paid stock service; he says \"maybe I'm too bullish here\" twice.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "PEG 0.675; fair value ~$775 on a 2.4 PEG; owns and keeps buying", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "next hardware super cycle"},
            {"name": "AMD (AMD)", "blurb": "PEG 1.27 on 55.88% growth; ~$1,080 fair value; Ryzen Pro under-watched", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "2-3 years"},
            {"name": "Tesla (TSLA)", "blurb": "recently bought more; his preferred SpaceX proxy", "stance": "BUYING-ADDING", "conviction": "Medium", "horizon": None},
            {"name": "SpaceX (SPCX)", "blurb": "exposure via Tesla ahead of the merger", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Bloom Energy (BE)", "blurb": "day-call pick alongside AMD", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": "intraday"},
            {"name": "QQQ", "blurb": "buy the dip at 700; bullish next 2-3 years if labor holds", "stance": "BUYING-ADDING", "conviction": "High", "horizon": "2-3 years"},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9EA", "tag": "AI tools", "title": "Re-test AI on a real document or video task if your view was set in 2023-24."},
    {"icon": "\U0001F4BC", "tag": "Macro", "title": "Watch layoff absorption, not frontier-lab news, as the first sign the AI trade is turning."},
    {"icon": "\U0001F4CA", "tag": "Valuation", "title": "Compare chip stocks on PEG, not PE alone — growth changes the ranking."},
    {"icon": "\U0001F3E2", "tag": "Markets", "title": "Track enterprise hardware names (Dell, AMD) as the read on open-weight demand."},
    {"icon": "\U0001F4C5", "tag": "AI infra", "title": "Follow Vera Rubin Ultra order timing as a gauge of 2028-29 Nvidia visibility."},
]

HOT_TAKES = [
    {"take": "I call 24 and 25 a black hole.", "cite": "— Kevin Paffrath", "why": "dismisses two years of AI spending"},
    {"take": "I actually think it's more likely the labor market rolls over before enterprises stop spending.", "cite": "— Kevin Paffrath", "why": "sequencing call on the AI cycle"},
    {"take": "Nvidia on a fair valuation could be $775.", "cite": "— Kevin Paffrath", "why": "3.5x price target"},
    {"take": "If we get an Iran deal, I don't think we'll ever see 700 again.", "cite": "— Kevin Paffrath", "why": "conditional QQQ floor call"},
    {"take": "Anthropic is actually less interesting now than it was 6 months ago.", "cite": "— Kevin Paffrath", "why": "contrarian on the hottest IPO"},
    {"take": "My opinion is if you want more SpaceX exposure, you buy Tesla.", "cite": "— Kevin Paffrath", "why": "proxy trade call"},
]

CLAIMS = [
    {"who": "Kevin Paffrath", "claim": "Nvidia's fair value at a 2.4 PEG is about $775 per share", "metric": "NVDA share price", "target": "$775", "by": "next hardware super cycle", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Kevin Paffrath", "claim": "AMD's fair value is roughly double, about $1,080", "metric": "AMD share price", "target": "$1,080", "by": None, "condition": None, "entity": "AMD (AMD)"},
    {"who": "Kevin Paffrath", "claim": "QQQ will not trade at 700 again if an Iran deal happens", "metric": "QQQ price floor", "target": "above 700", "by": None, "condition": "an Iran deal", "entity": "QQQ"},
    {"who": "Kevin Paffrath", "claim": "AI stocks / QQQ look like a long-term opportunity over the next 2-3 years", "metric": "QQQ", "target": "higher", "by": "2-3 years", "condition": "labor market doesn't roll over", "entity": "QQQ"},
    {"who": "Kevin Paffrath", "claim": "The labor market rolls over before enterprise AI spend stops; the turn is at least a year out", "metric": "labor market turn", "target": "rolls over", "by": "at least 1 year", "condition": None, "entity": None},
    {"who": "Jensen Huang", "claim": "Vera Rubin Ultra is close to placing-order time", "metric": "Vera Rubin Ultra orders", "target": "orders placed", "by": "near term", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Altimeter Capital (cited by Kevin Paffrath)", "claim": "Nvidia consensus earnings sit ~50% above January expectations for 2026 and ~3x higher by 2029", "metric": "NVDA consensus earnings", "target": "$383 (2026)", "by": "2029", "condition": None, "entity": "Nvidia (NVDA)"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4FA", "title": "Sources referenced: Altimeter Capital interview \"Jensen Huang: Does AI revenue justify capex?\" (clips and earnings chart); Kevin's own earlier video on playing the SpaceX merger via Tesla.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "PEG ratio", "def": "Price-to-earnings divided by expected earnings growth rate; Kevin treats ~2.4 as fair for these chips."},
    {"term": "Memory wall", "def": "The bottleneck where memory bandwidth/capacity, not compute, limits model context and performance."},
    {"term": "Open-weight model", "def": "A model whose weights are released so enterprises can run it on their own hardware (e.g. Qwen)."},
    {"term": "Q2 lap", "def": "The point where a strong quarter becomes the year-over-year comparison base, making growth look slower."},
]
