"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Your AI Strategy Is Measuring the Wrong Things",
    "channel": "Salim Ismail",
    "speakers": "Salim Ismail",
    "date": "2026-09-09",
    "video_url": "https://www.youtube.com/watch?v=Hvr8t-w9GCE",
    "thread_line": "6 threads · why company decisions run on narrative not evidence, the coordination-tax study, four metrics that actually measure AI transformation, and a free self-diagnostic tool",
    "category": "dev",
}

SNAPSHOT = [
    "Core claim: organizations have inverted the scientific method — **\"I have an opinion, now show me the evidence that confirms it\"** — and AI narratives are the newest, most visible version of this.",
    "Most \"data-driven\" investment decisions are ratification, not evidence: nobody is formally assigned to red-team the view before it's funded.",
    "A John Hopkins preprint found **74%** of workflows studied needed no back-and-forth coordination at all, yet unnecessary coordination still ate **24%-57%** of the work in those cases.",
    "The three metrics most companies track for AI (seats/licenses, token spend, task speed) all measure *effort*, not whether the organization got faster or cheaper end-to-end — he calls this \"token maxing.\"",
    "Four real metrics proposed instead: doing 50% of your week *differently* (not faster), workflow volume executed autonomously under human command, the human override rate over time, and an L0-L5 organizational readiness ladder.",
    "Ismail is promoting his new book *The Organizational Singularity* (follow-up to his 2014 *Exponential Organizations*) and a free diagnostic tool/skill called \"Building an EXO\" at openexo.com.",
    "Closes with a 3-question self-test (leaderboard question, geometry question, latency question) — a single \"yes\" on any of them caps an org below L3 regardless of AI spend.",
]

THEMES = [
    {
        "id": "opinion-first-culture",
        "color": "red",
        "badge": "Structural critique",
        "status": "PATTERN, NOT ONE COMPANY",
        "title": "Companies Run on \"Opinion First, Evidence Second, Selected for Fit\"",
        "lead": "Decks get built to support a senior leader's pre-formed view, not to test it, and everyone in the room calls the result \"data-driven.\"",
        "bullets": [
            "**Opening thesis** (from a prior Moonshots podcast appearance he references): 50 years ago the sequence was \"show me the evidence, I'll form an opinion\"; today it's reversed, and social media \"put a rocket on it\" because nuance has no viral coefficient.",
            "In practice: a senior person forms a view, an analyst is asked to build a deck that supports it (not test it) — knowing which chart to cut and which slide with a hard question gets moved to the appendix.",
            "His direct test for the reader: *in your last big investment decision, was anyone formally assigned and paid to argue against it* — to red-team it? For most orgs, no.",
            "**\"If nobody owns the counter case, you don't have an evidence culture, you have a ratification process.\"** He's explicit this isn't about stupid executives — the incentives are structural, rewarding confidence stories because that's what moves budget.",
        ],
        "quote": {"text": "50 years ago the sequence was show me the evidence and I'll form an opinion. Today we say, I have an opinion, now show me the evidence that confirms it.", "cite": "— Salim Ismail"},
        "watch": None,
        "names": None,
    },
    {
        "id": "three-fake-ai-metrics",
        "color": "amber",
        "badge": "Structural critique",
        "status": "\"TOKEN MAXING\"",
        "title": "Seats, Spend, and Task Speed Are the Three Metrics Everyone Tracks — and All Three Are Wrong",
        "lead": "Every AI metric he hears from client companies measures *effort*, not whether the organization actually got faster, cheaper, or better.",
        "bullets": [
            "**Seats**: how many employees have a license/are weekly-active — a measure of software distribution, tells you nothing about whether the company works differently.",
            "**Spend**: token consumption as a badge of AI adoption — he's seen companies run internal leaderboards on token burn, which is literally paying a bonus for burning inference (**\"Goodhart's law with a budget line\"**).",
            "**Task speed**: the most seductive because it's real — a report that took 3 days now takes 20 minutes — but the actual question is whether *cycle time* changed, or whether the faster report just sits in an approval queue for the same 9 days it always did.",
            "He gives his own org as the example: people send him work much faster now, but *he's* the bottleneck reading/processing it, so overall decision cycle time hasn't moved even though individual output sped up — \"token maxing\": high visible individual productivity, flat results at the firm level.",
        ],
        "quote": None,
        "watch": "He frames this as observed pattern across \"almost every organization\" he talks to, not a formal survey — treat as anecdotal client-conversation evidence, not a study.",
        "names": None,
    },
    {
        "id": "coordination-tax-study",
        "color": "amber",
        "badge": "Preprint evidence",
        "status": "2026 PREPRINT, UNREPLICATED",
        "title": "A John Hopkins Preprint Found 74% of Workflows Need No Coordination at All",
        "lead": "A study on where organizational coordination is actually necessary found most of it is avoidable — and avoidable coordination still imposes a real, measurable tax where it happens anyway.",
        "bullets": [
            "Study by a researcher he names as Haran Jou at John Hopkins (published as a 2026 preprint) examined which workflows across a large group of organizations actually require coordination — meetings, handoffs, alignment calls before something can move.",
            "Finding: roughly **74%** of the workflows examined were *monotonic* — they could run forward without any back-and-forth coordination.",
            "Where coordination was avoidable but happened anyway, it imposed a tax of **24%-57%** of the work on that workflow.",
            "He flags the caveat himself: it's a preprint on a sample, will get replicated, numbers may move — but calls that the point: **\"it's an evidentiary claim which means it can be checked and revised and argued with. You cannot check a vibe.\"**",
        ],
        "quote": None,
        "watch": "Preprint, not peer-reviewed; author name and institution are from auto-captions and may be misheard/misspelled — treat the specific name as approximate, the 74%/24-57% figures as his stated reading of the study.",
        "names": None,
    },
    {
        "id": "four-real-metrics",
        "color": "green",
        "badge": "Recommendation",
        "status": "WHAT TO MEASURE INSTEAD",
        "title": "Four Metrics That Actually Measure AI Transformation",
        "lead": "Replace seats/spend/speed with measures of whether work itself changed, not just whether it got faster.",
        "bullets": [
            "**Doing it differently, not faster** (credited to Michelle Krivcovich): 50% of your time should be spent *differently* because of AI access — a different sequence of activities in your week, not the same work 50% quicker. His test: what did you do this week you wouldn't have done 18 months ago, and what did you stop doing entirely?",
            "**Workflow volume under autonomous execution** (credited to Mark Jenkins at OpenText): stop counting how many employees/companies use AI assistants or agents; measure the volume of *workflows* safely executed end-to-end by autonomous agents under human command — every word load-bearing: workflows (not tasks), safely (provably happened), executed (reached its own outcome), under human command (someone is accountable).",
            "**Human override rate**: when an agent runs alongside an existing process, track how often people correct it, week over week. A falling rate means the system is learning the business; a flat rate after 3 months means \"you've bought software, you've not built capability\" — and it can't be gamed because the corrections are made by your own people doing their own work.",
            "**The L0-L5 readiness ladder** (his firm's framework, released this year): L0 theater, L1 personal productivity, L2 team workflow, L3 organizational infrastructure, L4 compounding operating system/durable advantage, L5 virtually self-driving. His claim: no organization on Earth is at L5 yet, and most companies with a loud AI narrative are actually sitting at L1.",
        ],
        "quote": {"text": "Stop measuring how many employees are using AI, measure the volume of workflows that is executed by AI under human supervision.", "cite": "— Salim Ismail, citing Mark Jenkins"},
        "watch": None,
        "names": None,
    },
    {
        "id": "organizational-singularity-book",
        "color": "gray",
        "badge": "Self-promotion, disclosed",
        "status": "NEW BOOK + FREE TOOL",
        "title": "The Organizational Singularity — a Sequel to Exponential Organizations, Built as a Diagnostic Skill",
        "lead": "His 2014 book described the pattern of fast-scaling organizations but gave no instruments to measure against it; this one is built around a free, installable diagnostic instead.",
        "bullets": [
            "*Exponential Organizations* (2014) gave people vocabulary for how the fastest-growing companies scaled, but was descriptive — he says people would call themselves an \"exponential organization\" and have no answer when he asked about revenue-per-employee.",
            "New book has three pieces: EXO 3.0 (the target architecture, with an \"MTP\" encoded as a protocol agents can read), the Intelligence Stack (the operating system every agent/workflow plugs into), and Rewrite (the playbook/sequence to get from current state to EXO 3.0).",
            "The diagnostics are the part he says matters most: a readiness score with anchored descriptors (so a \"4\" means the same thing in finance as in operations), covering the dabbling test, token-maxing test, override grade, and the L0-L5 ladder.",
            "The whole operating model — diagnostics, scorecards, agent specs, data-governance test, full playbook — is packaged as a free installable skill called \"Building an EXO,\" runnable inside Claude, Codex, and (he says) soon Grok — available at openexo.com/resource-hub, no email or sales call required to run the diagnostic.",
        ],
        "quote": None,
        "watch": "He directly discloses the conflict: \"I'm not going to pretend this is charity. We build a business on the far side of this work, and some of you will end up working with us\" — the tool is a funnel into his consulting practice, by his own statement.",
        "names": None,
    },
    {
        "id": "three-question-test",
        "color": "amber",
        "badge": "Self-diagnostic",
        "status": "RUN IN ~4 MINUTES",
        "title": "The Three-Question Test: Leaderboard, Geometry, Latency",
        "lead": "A single \"yes\" on any of these three questions caps an organization below L3 no matter how much it's spending on AI.",
        "bullets": [
            "**Leaderboard question**: are you formally or informally rewarding anyone for an input — usage, tokens, pilots, agents deployed? A yes means you're paying for the appearance of transformation.",
            "**Geometry question**: do your agents sit one-per-department inside the existing org chart, reporting into the structure you already had? A yes means, in his phrase, **\"you've electrified the old factory\"** — put a motor on every machine and left the drive shaft running down the ceiling.",
            "**Latency question**: are individual tasks measurably faster while end-to-end cycle time is unchanged? A yes means you've moved the queue, not removed the problem.",
            "His framing: three yeses (or three honest \"I don't knows\") is transformation theater, and none of the three failures is fixable by buying another tool — each is a decision-architecture problem.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F3AF", "tag": "AI strategy", "title": "Audit which of the three fake metrics (seats, token spend, task speed) is on your dashboard right now, and be honest about it — none of them measure whether the org got faster or cheaper."},
    {"icon": "\U0001F4CA", "tag": "AI strategy", "title": "Start tracking human override rate on any agent running alongside a live process — a flat rate after 3 months means you bought software, not capability."},
    {"icon": "\U0001F465", "tag": "Org design", "title": "Assign and protect a formal red-team role on your next major investment decision — someone paid to argue against it and expected to win sometimes."},
    {"icon": "\U0001F9EE", "tag": "Org design", "title": "Run the 3-question test (leaderboard/geometry/latency) on your own org before your next leadership meeting — a single yes caps you below L3 regardless of spend."},
    {"icon": "\U0001F501", "tag": "Careers", "title": "Ask what 50% of your week you're now doing differently (not just faster) because of AI access — if you can't name it, you're dabbling, not transformed."},
]

RISKS = [
    "This is disclosed self-promotion: Ismail names his own consulting business as the reason the diagnostic tool exists (\"we build a business on the far side of this work\") — the framework and metrics he recommends are also the product he sells.",
    "The coordination-tax study (74% monotonic, 24%-57% tax) is a single 2026 preprint he cites from memory in conversation, not a report he's reading from — he flags it as unreplicated himself.",
    "The researcher's name (heard as \"Haran Jou\") and the two metric sources (\"Michelle Krivcovich\", \"Mark Jenkins at OpenText\") come through auto-captions and may be misspelled or mistranscribed — treat the specific spellings as approximate, the ideas attributed to them as his own paraphrase in conversation.",
    "Figures like the L0-L5 ladder and the override-rate metric are his firm's own framework, presented with conviction but without independent validation data in this video.",
]

HOT_TAKES = [
    {"take": "You've just paid a bonus for burning inference. That's Goodhart's law with a budget line.", "cite": "— Salim Ismail", "why": "dismissive, specific dig at token-consumption leaderboards"},
    {"take": "If nobody owns the counter case, you don't have an evidence culture, you have a ratification process.", "cite": "— Salim Ismail", "why": "flat claim that most companies' decision process is fake evidence-based"},
    {"take": "You've electrified the old factory. You've put a motor on every machine and left the drive shaft running down the ceiling. This is not going to work over time.", "cite": "— Salim Ismail", "why": "confident prediction that department-embedded agents fail structurally"},
    {"take": "Most companies with a loud AI narrative are sitting at L1.", "cite": "— Salim Ismail", "why": "direct, checkable dismissal of most companies' AI claims"},
    {"take": "A single yes puts you below L3, no matter what you are spending.", "cite": "— Salim Ismail", "why": "hard, falsifiable threshold claim"},
    {"take": "Charging for the thermometer would not be very fair, it would be kind of absurd.", "cite": "— Salim Ismail", "why": "stakes a public position on why his own diagnostic is free, on the record"},
]

OTHER_NEWS = []

GLOSSARY = [
    {"term": "Goodhart's law", "def": "When a measure becomes a target, it stops being a good measure — invoked here for token-consumption leaderboards that reward burning inference rather than useful output."},
    {"term": "Monotonic workflow", "def": "A workflow that can run forward to completion without back-and-forth coordination (meetings, handoffs, alignment calls) — the John Hopkins preprint found ~74% of workflows studied fit this category."},
    {"term": "L0-L5 ladder", "def": "Ismail's readiness scale for AI-driven organizations: L0 theater, L1 personal productivity, L2 team workflow, L3 organizational infrastructure, L4 compounding operating system, L5 virtually self-driving."},
    {"term": "Token maxing", "def": "His term for high visible token spend and individual output paired with flat results at the level of the whole firm."},
]
