META = {
    "title": "Martin Shkreli: Big Pharma's Blind Spot, Betting Against Quantum & What Prison Taught Him",
    "channel": "All-In Podcast",
    "speakers": "Martin Shkreli (guest); All-In hosts, with Brad",
    "date": "2026-10-12",
    "video_url": "https://www.youtube.com/watch?v=yZR8QW4qQmM",
    "thread_line": "5 threads · quantum short · photonics vs GPUs · pharma molecule arbitrage · AI demand & who over-earns · Dario, EA and prison",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Shkreli is **short quantum computing** — and admits he has lost millions of dollars on the trade so far.",
    "His case: quantum has one killer algorithm (Shor's factoring / ECDLP), runs at hundreds-to-thousands of hertz, has no RAM — he can't multiply 300 by 200 on any machine in the world.",
    "The real disruption he watches is **photonic computing**: matrix multiplication in light is 'free', and he expects H100s/B200s in the scrap heap within 20 years.",
    "Still long semis for now (Jevons paradox), but a 1,000x-more-efficient transformer would be bad for Nvidia — and he'd have called Yahoo and Cisco longs in 2000 too.",
    "Pharma playbook: big pharma sells drugs it doesn't value — he bought one from Bristol for ~$2M; that company is worth ~$6B today.",
    "AI demand is unlimited, TAM isn't capped at knowledge workers; **Meta** is his pick to over-earn; he owns OpenAI exposure.",
    "Calls Dario Amodei a fear-monger; says there won't be a single AI-relevant drug in the next 10 years.",
    "Prison lesson: his refusal to admit he wasn't a great trader is what put him there.",
]

THEMES = [
    {
        "id": "quantum-short",
        "tags": ["semis", "software"],
        "color": "red",
        "badge": "High conviction",
        "status": "SHORT QUANTUM COMPANIES — LOSING MONEY ON IT SO FAR",
        "title": "Quantum computing is one magic trick, not a business",
        "lead": "Shkreli is short quantum-computing stocks because the machines are only exponentially faster at one class of problem — factoring — and slower at everything else.",
        "bullets": [
            "The field exists because of **Peter Shor's** algorithm; quantum turns integer factorization and the elliptic-curve discrete log problem (ECDLP) from exponential into polynomial time.",
            "Modern machines run at hundreds to thousands of hertz, single-core, single-threaded — they'll 'never beat a million Nvidia machines' at sorting or general work.",
            "No quantum RAM, so problems need tiny inputs; he hears OpenAI turns down every quantum pitch.",
            "He and his wife Chelsea (early OpenAI, taught quantum with Scott Aaronson at MIT) tried every quantum computer in the world — none could multiply 300 by 200.",
            "Google has a few prototypes, IBM a small cloud; Big Tech's reason to spend hundreds of millions a year is 'someday there might be something' — 'not a great business'.",
            "Host counter: we're at the transistor stage, no gates/OS/software yet. His reply: would you go long punch cards, vacuum tubes, mercury delay lines? Those were stocks once (CTR became IBM).",
            "Lost millions shorting quantum names — 'we gained billions in insight'.",
        ],
        "quote": {"text": "We cannot multiply 300 by 200 on any of these.", "cite": "— Martin Shkreli"},
        "watch": "He is short the sector and says the trade has cost him millions so far — timing, not thesis, is the open question by his own admission. He also floated that quantum CEOs might go to jail; no company was named.",
        "names": [
            {"name": "Alphabet (GOOGL)", "blurb": "Only a few quantum prototypes; spends heavily on 'someday'", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "IBM (IBM)", "blurb": "Runs a small quantum cloud; Shkreli skeptical of the spend", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Named among quantum spenders; also authored the AOC optical-computing paper", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "photonics-vs-gpus",
        "tags": ["semis", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "LONG SEMIS NOW — PHOTONICS THE 20-YEAR THREAT",
        "title": "Photonic matmul could scrap today's GPUs; still long semis on Jevons",
        "lead": "AI is matrix multiplication, light does it near-instantly, so Shkreli thinks building space and nuclear capacity for GPUs is insane — yet he stays long semis for now.",
        "bullets": [
            "'Every time somebody uses the word AI, I think of the word matmul' — a GPU spends 99.9% of its time multiplying matrices, in n-cubed time (a 1,000x1,000 multiply = a billion operations).",
            "A **Microsoft** paper on analog optical computing (AOC) says matmuls in light are 'free' and instant; he may start a company in the space.",
            "Photonic startups he named (captioned 'Neurofas', 'Opticore', 'Lumi') aim to build photonic matmul cores that 'run circles around' Nvidia — nonlinearity and storage still unsolved.",
            "Sam Altman said on a rival podcast that photonic computing could be the future.",
            "Jevons paradox argues for more demand; Alexandr Wang told him it'll be a millionx compute improvement — but there aren't a million times more people.",
            "Valley talk of transformers 1,000x more efficient: 'that's bad for Nvidia, there's no doubt'.",
            "Self-check: he'd probably have called Yahoo and Cisco longs in 2000 too.",
        ],
        "quote": {"text": "I think it's insane that we're thinking about space. I think it's insane we're thinking about nuclear.", "cite": "— Martin Shkreli"},
        "watch": "He is weighing starting a photonic-computing company himself, so his bear case on GPUs doubles as a pitch for that space.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Still a long for now via semis; a 1,000x better transformer would hurt it", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Cisco (CSCO)", "blurb": "2000-bubble analogy; gets 'a little bit' out of the AI build like the internet", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "pharma-arbitrage",
        "tags": ["biotech", "finance"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "SPARSENTAN — NOW FDA-APPROVED",
        "title": "Big pharma's blind spot: buying shelved molecules for pennies",
        "lead": "The alpha was in private molecule deals, not public stocks — big pharma sells drugs it doesn't value, and re-aiming them at a new disease creates billions.",
        "bullets": [
            "Bought a drug from Bristol for **$2M**; that first startup's company is public today and worth ~$6B.",
            "Pfizer 'would sell you a drug for a million bucks that was worth a billion dollars. They didn't care.'",
            "Sparsentan (he named it): Bristol developed it for hypertension, a 'sleepy' market; he moved it to **FSGS**, which never had an approved drug — now FDA-approved, a blockbuster, for ~30,000 patients.",
            "The bottleneck was vetting assets (papers, patents, university and company BD), so in 2015 he started a side NLP company on Watson to read medicine's ~40M papers.",
            "Royalty Pharma's comparable win: bought NYU's Remicade royalty at about 1x earnings and it 20x'd.",
            "Career path: joined Jim Cramer's hedge fund at 16 (Cramer made 23% a year net of fees), then a Tiger cub, then his own fund — realized he was a better entrepreneur than trader.",
        ],
        "quote": {"text": "We found that the the marketplace for molecules had huge amounts of alpha.", "cite": "— Martin Shkreli"},
        "watch": None,
        "names": [
            {"name": "Bristol-Myers Squibb (BMY)", "blurb": "Sold him the drug that became sparsentan", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Pfizer (PFE)", "blurb": "Example of big pharma underpricing its molecules", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Royalty Pharma (RPRX)", "blurb": "Remicade royalty bought at ~1x earnings, then 20x'd", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "ai-demand-winners",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "OWNS OPENAI EXPOSURE — META THE OVER-EARNER",
        "title": "Infinite demand for intelligence, and Meta over-earns",
        "lead": "Shkreli sees no ceiling on AI demand and thinks the internet is the right analog: consumers win most, but Meta is the company that over-earns.",
        "bullets": [
            "Jensen said ~$400B of venture money has been redirected into AI; Shkreli agrees VCs are effectively funnelling LP money into tokens but sees no valuation trap.",
            "Capping the TAM at knowledge workers is 'a mistake' — 'there is infinite demand for intelligence and infinite demand for work'.",
            "McDonald's could rationally spend $10B on 10M GPUs to pick its next sandwich instead of hiring McKinsey — NPV-positive if more tokens keep giving better answers.",
            "A friend who 'invented the reasoning model at OpenAI' left to start **Core Automation**; the vision is AI starting businesses — a whole S&P 500 inside one lab.",
            "Internet analogy: the winners are consumers and businesses; Cisco-type suppliers get 'a little bit'.",
            "Meta wins on distribution and product chops shown with Muse (credited to Alex); 'we're still in day one', chatbots will look primitive.",
            "Owns OpenAI 'through a few different ways'; calls Sam Altman's hardware hedge 'really brilliant'.",
            "Piled in after the selloff around Dario's essay, which he called 'ridiculous'.",
        ],
        "quote": {"text": "There is infinite demand for intelligence and infinite demand for work.", "cite": "— Martin Shkreli"},
        "watch": None,
        "names": [
            {"name": "Meta (META)", "blurb": "His pick to over-earn: distribution plus product chops (Muse)", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "OpenAI", "blurb": "Owns exposure 'through a few different ways'; hardware hedge 'brilliant'", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Core Automation", "blurb": "Friend's under-the-radar startup from the OpenAI reasoning-model inventor", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "dario-ea-prison",
        "tags": ["policy", "mindset"],
        "color": "red",
        "badge": "Contested",
        "status": "OPINION — E/ACC VS EA",
        "title": "Dario is a fear-monger; ego, not genius, is what sinks smart people",
        "lead": "Shkreli calls AI-safety alarmism nerd self-importance, dismisses AI drug discovery for a decade, and says his own downfall was refusing to admit he wasn't a great trader.",
        "bullets": [
            "Credits Dario Amodei with a trillion-dollar company but 'kind of hates the guy': a fear-monger who left OpenAI to start 'Pandora's box 2'.",
            "Dario said ~2 years ago we'd be fully unemployed within one to five years — 'he's got three years left' — and that AI would cure all diseases.",
            "Claims to have helped start **e/acc** as a counter-insurgency to effective altruism; 'there'll be time to panic, it's just not now' — physical AI is where the real risk sits.",
            "Credits Meta, the president and Jensen with 'the spine' to call AI doom nonsense; thinks OpenAI doesn't believe it but stays close to Anthropic's line.",
            "Blames Nick Bostrom's *Superintelligence* for scaring Elon; cites the Buffett line about shooting the Wright brothers.",
            "On SBF, Elizabeth Holmes and Raj Rajaratnam: gifted people carry an 'albatross' of having to live up to something; he advises SBF on how to tough it out.",
            "Prison taught him people everywhere share the same longings — friends who stopped calling, people they miss.",
        ],
        "quote": {"text": "That simple refusal to admit that put me in prison.", "cite": "— Martin Shkreli"},
        "watch": "Shkreli says Chelsea, his wife, was among the first people at OpenAI, and he owns OpenAI exposure — context for his attacks on Anthropic's founder.",
        "names": [
            {"name": "Anthropic", "blurb": "Founder Dario called a fear-monger; origin story criticized", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9EE", "tag": "Quantum", "title": "Ask what quantum actually does faster than GPUs before paying for the story — Shkreli's answer is factoring only."},
    {"icon": "\U0001F4A1", "tag": "Semis", "title": "Watch photonic-matmul startups and efficiency jumps in transformers as the real long-run risk to Nvidia, not demand."},
    {"icon": "\U0001F48A", "tag": "Biotech", "title": "Look for value in drugs big pharma shelves or under-prices — re-targeting at an orphan disease is the lever."},
    {"icon": "\U0001F4C8", "tag": "AI", "title": "Size AI demand beyond knowledge workers; ask who over-earns on distribution, not who builds the pipes."},
    {"icon": "\U0001F9E0", "tag": "Mindset", "title": "Separate what you're good at from what you need to be seen as — that gap is where Shkreli says he went wrong."},
]

HOT_TAKES = [
    {"take": "They'll never beat an Nvidia machine. They'll never beat a million Nvidia machines.", "cite": "— Martin Shkreli", "why": "dismissal of a whole sector he's short"},
    {"take": "I do think in in 20 years these H100s are in the scrap heap.", "cite": "— Martin Shkreli", "why": "dated call on GPU obsolescence"},
    {"take": "I don't think there'll be a single AI relevant drug in the next 10 years.", "cite": "— Martin Shkreli", "why": "contrarian, dated, falsifiable"},
    {"take": "I think it's meta", "cite": "— Martin Shkreli, on who over-earns from AI", "why": "single-name pick"},
    {"take": "I think he's a fear-mongerer.", "cite": "— Martin Shkreli, on Dario Amodei", "why": "personal attack on a lab founder"},
    {"take": "If there's a thousand times more efficient transformer, that's bad for Nvidia.", "cite": "— Martin Shkreli", "why": "bear case on a long he holds"},
]

CLAIMS = [
    {"who": "Martin Shkreli", "claim": "Today's Nvidia GPUs (H100, B100, B200) will be in the scrap heap, displaced by better approaches such as photonics.", "metric": "H100/B200 relevance", "target": "obsolete", "by": "20 years", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Martin Shkreli", "claim": "There won't be a single AI-relevant drug in the next 10 years.", "metric": "AI-relevant approved drugs", "target": "0", "by": "10 years", "condition": None, "entity": None},
    {"who": "Martin Shkreli", "claim": "Quantum computers will never beat Nvidia machines outside factoring-type problems.", "metric": "general compute vs Nvidia", "target": "never", "by": None, "condition": None, "entity": None},
    {"who": "Martin Shkreli", "claim": "A 1,000x more efficient transformer would hurt Nvidia.", "metric": "transformer efficiency", "target": "1,000x", "by": None, "condition": "if such a transformer arrives", "entity": "Nvidia (NVDA)"},
    {"who": "Martin Shkreli", "claim": "Computational complexity terms will become common parlance.", "metric": "public use of complexity terms", "target": "mainstream", "by": "5-10 years", "condition": None, "entity": None},
    {"who": "Dario Amodei (cited by Martin Shkreli)", "claim": "We will be fully unemployed within one to five years (said ~2 years ago).", "metric": "unemployment", "target": "full", "by": "~3 years left", "condition": None, "entity": "Anthropic"},
]

RELATIONS = [
    {"from": "Martin Shkreli", "rel": "criticizes", "to": "Anthropic", "note": "calls Dario Amodei a fear-monger"},
    {"from": "Martin Shkreli", "rel": "owns_stake", "to": "OpenAI", "note": "'through a few different ways'"},
    {"from": "Martin Shkreli", "rel": "endorses", "to": "Meta (META)", "note": "the company that over-earns from AI"},
    {"from": "Anthropic", "rel": "competes_with", "to": "OpenAI", "note": "founded by OpenAI leavers — 'Pandora's box 2'"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4BF", "title": "Shkreli on the one-copy Wu-Tang Clan album he bought: 'It's not a good record.'", "tag": "Culture"},
    {"icon": "\U0001F4DA", "title": "Sources referenced: Peter Shor's algorithm, Scott Aaronson, the CLRS algorithms textbook, Microsoft's AOC paper, Nick Bostrom's *Superintelligence*, Sam Altman on a rival podcast, Alexandr Wang, Jensen Huang on venture flows.", "tag": "Sources"},
    {"icon": "\U0001F680", "title": "Hosts asked about **Elon's** proposal of competitor peer review as a middle ground on AI safety; Shkreli answered with the EA critique instead.", "tag": "AI policy"},
]

GLOSSARY = [
    {"term": "Shor's algorithm", "def": "Quantum algorithm that factors integers in polynomial time — the main reason quantum computing exists as a field."},
    {"term": "ECDLP", "def": "Elliptic-curve discrete log problem; the hardness behind most crypto signatures, also breakable by a large quantum computer."},
    {"term": "Matmul", "def": "Matrix multiplication — the operation GPUs spend ~99.9% of AI time on, n-cubed in conventional hardware."},
    {"term": "Photonic computing", "def": "Doing computation, especially matmul, with light instead of electrons."},
    {"term": "Jevons paradox", "def": "Efficiency gains increase total consumption of a resource rather than reducing it."},
    {"term": "FSGS", "def": "Focal segmental glomerulosclerosis, a kidney disease with no approved drug before sparsentan."},
    {"term": "e/acc", "def": "Effective accelerationism — move-fast counter-movement to effective altruism's AI-safety focus."},
    {"term": "Tiger cub", "def": "Hedge fund founded by an alum of Julian Robertson's Tiger Management."},
]
