"""Per-video data for peter-h-diamandis_2026-09-11_three-lab-warnings-in-five-days."""

META = {
    "title": "Three Lab Warnings in Five Days, Researcher Flags “Gambling with Our Lives,” and Labs Race",
    "channel": "Peter H. Diamandis",
    "speakers": "Peter Diamandis, Alex Wissner-Gross, Immad Mostaque, Dave Blundin, Salim Ismail",
    "date": "2026-09-11",
    "video_url": "https://youtu.be/AxzcWOxzkiw",
    "thread_line": "6 threads · an alignment researcher's resignation and the PDoom debate it triggered, why data (not architecture) is the real moat, Millennium Prize math problems falling, the GPU/HBM compute-economy reversal and China's closing model gap, Anthropic's economic dominance and the coming GDP/UBI fight, and two concrete longevity/genomics breakthroughs",
    "category": "market",
}

SNAPSHOT = [
    "A researcher who spent three years on pre-training at both OpenAI and Anthropic resigned and called the race to superintelligence \"gambling with our lives\"; Anthropic's own alignment lead publicly agreed AI could kill everyone with **>10% probability within a decade** — the panel is split on how much to read into it.",
    "A Dwarkesh Patel/Jerry Han study found better training data drove **12x** of AI's 2019-2025 compute-efficiency gains versus **3.7x** from better architecture — the panel's takeaway: data, not algorithms, is the real moat, and it has a shelf life.",
    "OpenAI's reported Navier-Stokes solve has the panel calling multiple Millennium Prize math problems \"cooked,\" with Noam Brown citing a roughly **25,000x cost collapse** (from $500k to $20) in similar benchmark performance since 2025.",
    "H100 GPU rental prices are **up 22% in a month** to $3.28/hour despite the chips being three years old — the opposite of standard depreciation — while a new DeepSeek architecture chart shows a possible 4x cut in the HBM memory that's currently ~40% of AI capex.",
    "NPR reports Anthropic hit a **$6.5B quarterly revenue run-rate** and 42% of the AI coding market en route to a reported $2T+ IPO; its own economic-impact report models up to **15% annual GDP growth** and 20% cognitive-worker unemployment by 2030 — Immad Mostaque says the model is missing aggregate-demand collapse and is building a rival model to prove it.",
    "Two concrete health breakthroughs: Insilico Medicine's AI-designed drug rentosertib reached Phase 3 for a fatal lung disease while reversing six protein aging clocks by 3-6 years in trial patients, and Google DeepMind's AlphaGenome now scores all ~9 billion possible single-letter human genome mutations.",
    "Dave Blundin's company Vestmark (2001, post-9/11 founding) is being acquired by Envestnet, backed by Bain Capital, merging into a combined ~$10 trillion asset-management platform.",
    "Sponsor segments (Abundance Summit/Link Ventures intro, Google for Startups, Blitzy, and a Fountain Life cancer-screening segment) are excluded from this brief per standing policy.",
]

THEMES = [
    {
        "id": "alignment-crisis",
        "tags": ["policy", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "",
        "title": "A researcher's resignation, a >10% doom estimate from Anthropic's own alignment lead, and a genuinely split panel",
        "lead": "Three separate signals from inside the labs surfaced within five days, and the Moonshots panel split hard on how seriously to take any of them.",
        "bullets": [
            "Jacob Coxin, who spent three years on pre-training at both OpenAI and Anthropic, resigned and posted that \"neither company is acting responsibly in the race toward self-improving super intelligence,\" calling it **gambling with our lives**; his tweet reportedly reached 100-150 million views with no obvious paid boost, which several panelists found itself suspicious.",
            "Evan Hubinger, Anthropic's alignment science lead, responded on X: \"we really do earnestly believe AI could kill all humans. I personally think it is greater than 10% within the next decade... we do not yet have a plan to solve alignment for superintelligence.\"",
            "Alex Wissner-Gross discounts the resignation itself (\"a well-worn tradition... rage quit couched as virtue signaling\") but calls the *reach* of the tweet genuinely strange, and floats the possibility of a foreign influence operation without confirming one.",
            "Context: Anthropic CEO Dario Amodei separately stated a personal probability of roughly **25%** that AI turns out badly, a year before this episode — a figure the panel notes got far less attention than this week's tweets did.",
            "Alex's counter-argument to any near-10% doom estimate: if superintelligence reliably led to catastrophic outcomes, advanced alien civilizations should already have devoured or been devoured across the galaxy on statistical grounds — since we don't observe that, he treats high PDoom numbers as overstated (his own words: \"an inductive prior, not a safety strategy\").",
            "Immad Mostaque discloses his own **personal doom estimate dropped from 50% to 20%**, and argues the real debate is sociological — what this does to policy in the two weeks before Xi Jinping's visit to the US, not whether the number is exactly right.",
            "Peter and Immad both call any PDoom above roughly 1% unacceptable regardless of the exact figure, while Dave and Alex argue slowing down doesn't reduce risk (\"all that would happen... is we would fritter away the time... and create a race condition with China\") and that steering, not stopping, is the only real option.",
            "Separately, the panel debates the **orthogonality thesis** (whether intelligence and goals are independent) — Alex says his own hope for the future rests on it being *false*, i.e. that greater intelligence tends toward greater wisdom and thus alignment, a belief he flags as his personal, unproven best hope rather than a settled result.",
        ],
        "quote": {"text": "We really do earnestly believe AI could kill all humans. I personally think it is greater than 10% within the next decade.", "cite": "— Evan Hubinger, Anthropic alignment science lead"},
        "watch": "Every PDoom figure in this segment (10%, 20%, 25%, 50%, 0.1%) is a personal, informally stated estimate from a different individual, not a consensus number or a published study.",
        "names": None,
    },
    {
        "id": "data-is-the-moat",
        "tags": ["software", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "",
        "title": "Data drove 3x more of AI's progress than architecture did — and that's an entrepreneurial opening",
        "lead": "A new study puts a number on something the panel has argued for years: the quiet work of curating training data has mattered more than the algorithms that get the headlines.",
        "bullets": [
            "The study (Dwarkesh Patel with Princeton's Jerry Han, covering AI progress from 2019-2025) found better training **data** produced a **12x** improvement in compute efficiency versus **3.7x** from better architectures and training recipes — data outweighed algorithms by more than 3-to-1.",
            "Alex ties this to his own older essay (\"data sets over algorithms\") arguing historical AI grand-challenge breakthroughs — chess, speech recognition, Jeopardy — were data-set problems, not algorithm problems, and next-token prediction is \"the ultimate data challenge.\"",
            "Concrete valuation proof point (Immad, without naming the company): a business worth roughly **$8 billion** spun its internal data assets into a separate subsidiary that was independently valued at **$32 billion** — four times the parent company's own worth.",
            "Caution flag, Alex's own example: Bloomberg pre-trained BloombergGPT on its proprietary financial data expecting durable enterprise value, but general frontier models trained on public (plus whatever proprietary data they can access) data outperformed it on financial benchmarks within months — proprietary internal data has real but *time-limited* value.",
            "Dave's practical read for entrepreneurs: frontier labs including reported outreach from **OpenAI**, plus data buyers referenced only as \"Mero\" and \"Scale,\" are actively trying to buy corporate data archives outright, and any founder with clean, unique domain-specific data has a real shot at a business \"in that use case\" outperforming the foundation labs' own general models.",
            "Salim's blunt framing of the risk on the other side: any tech-driven moat now has a shelf life that's shrinking, so the entrepreneurial imperative is to build a culture of constant reinvention (\"you'll have a tow hold... then keep moving\") rather than assume a data or product advantage is durable.",
        ],
        "quote": {"text": "The next 10x may be sitting in the data that you have someplace in your organization.", "cite": "— Peter Diamandis"},
        "watch": None,
        "names": None,
    },
    {
        "id": "math-is-cooked",
        "tags": ["ai-infra", "software"],
        "color": "green",
        "badge": "High conviction",
        "status": "",
        "title": "Millennium Prize math problems are falling, and the cost to solve them is collapsing 25,000x",
        "lead": "OpenAI's reported Navier-Stokes solve has the panel calling multiple famous unsolved math problems \"cooked\" — and citing a cost curve that makes today's frontier result a coffee-shop expense within two years.",
        "bullets": [
            "Sam Altman's own reaction to the Navier-Stokes result: \"I did not expect a result of this magnitude to happen so soon... for me, this is the strongest evidence yet\" for the need to \"pace progress\" — used by the panel as evidence the surprise, at minimum, is genuine on some level.",
            "Alex says he's hearing \"finger to the wind\" rumors that OpenAI and/or Anthropic may already be sitting on solutions to two more Clay Millennium Prize problems — the **Hodge conjecture** and the **Birch and Swinnerton-Dyer conjecture** — explicitly unconfirmed, not reported fact.",
            "Noam Brown (OpenAI): OpenAI's o3 model cost roughly **$500,000** to score 87.5% on ARC-AGI-1 in 2025; a comparable-caliber result is now available for about **$20/month** via Astra — a cost collapse of roughly **25,000x**, which the panel projects could put Millennium-Prize-caliber results at \"the cost of a cup of coffee\" by late 2027.",
            "Alex coins the term **\"normalcy overhang\"** for the current moment: street-level life still looks ordinary (no humanoid robots, no nanotech swarms) even as math and science are being \"bulk solved\" behind the scenes — he expects this gap to visibly collapse soon.",
            "The panel's practical advice to anyone currently in or considering a PhD: Mark Chen (OpenAI's chief research officer) and Greg Brockman (OpenAI co-founder, MIT dropout) both reached the top of frontier AI without one, and the panel cites Elon Musk's line that he'll \"hire anybody without a college degree\" based purely on what they've built — Dave's framing is that a PhD now has a real risk of finishing \"four years... too late to the party.\"",
            "Immad frames the actual bottleneck differently: once a problem can be *specified* clearly (like Navier-Stokes), throwing thousands of agents at it is comparatively easy — the harder and more valuable entrepreneurial skill becomes defining the right question (curing cancer, better flight planning) in the first place.",
        ],
        "quote": {"text": "Those challenges are being yanked away from humanity and being slain by the compute we aim at them.", "cite": "— Peter Diamandis"},
        "watch": "The Hodge conjecture and Birch-Swinnerton-Dyer claims are explicitly flagged by Alex as unconfirmed rumor, not a reported result like Navier-Stokes.",
        "names": None,
    },
    {
        "id": "compute-economy-reversal",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "",
        "title": "GPUs stopped depreciating, HBM may be about to get 4x cheaper, and China's models keep closing the gap",
        "lead": "Three separate compute-economy data points this week point the same way: the physical bottleneck on AI is shifting fast, and China isn't falling behind on model quality the way the panel expected.",
        "bullets": [
            "H100 GPU rental prices rose **22% in a single month to $3.28/hour** — a three-year-old chip getting *more* expensive to rent, which Jensen Huang (Nvidia) called on X a \"fungible, durable, and highly rentable... productive revenue generating asset\"; Dave and Alex disclose direct financial interest via a GPU-rental-index startup Link Ventures backs and Alex advises.",
            "Dave's own news: his company **Vestmark** (founded 2001 right after 9/11, ~$2 trillion in assets managed, ~5 million financial accounts, ~20 million lines of code) is being acquired by **Envestnet** (backed by Bain Capital), merging into a combined platform managing roughly **$10 trillion** in assets — Dave notes Akamai founder Danny Lewin, an MIT friend, died aboard one of the planes that day, and frames founding Vestmark that same year as a deliberate act of belief in the country's recovery.",
            "A new DeepSeek architecture (v4.1 flash) cuts the KV-cache memory load from 48,000 (original DeepSeek V3) to roughly 35,000 by routing around expensive high-bandwidth memory (HBM) onto SSD/DDR lookup tables instead — Dave estimates HBM currently makes up **~40% of the roughly $1 trillion** in current AI data-center capex, meaning this kind of efficiency gain could reshape which fabs and chip lines are worth investing in.",
            "Separately, a DeepSeek design-benchmark model reportedly beat Claude Fable 5.1 and GPT on front-end design benchmarks while running **20x faster and 20x cheaper**, and cost only **~$10 million** to train — versus Astra's reported billion-dollar-scale training run.",
            "Alex flags this as a wake-up call specifically for Anthropic (\"Fable 5.1... its visual reasoning capabilities are weak and anemic\" relative to Astra and the new Chinese open-weight models) to invest more in visual/UI reasoning.",
            "ByteDance founder Zhang Yiming is personally overseeing a new real-time spatial world model (built on ByteDance's Seedance video tech, targeting robotics/games/virtual worlds) reportedly launching as soon as next month — Immad notes ByteDance already charges tens of millions of dollars for early US-server access to Seedance video generation.",
            "Alex's forecast: the divide between \"video generation\" and \"language models\" is collapsing into embodied robotics as the shared endgame — he expects GPT-6-class models to add video as just another output modality (alongside text and audio) within a version or two, and separately cites a RoboCurve benchmark showing GPT-6/Astra plugged into a robotic arm already achieving near-100% completion on manipulation tasks like stacking blocks.",
        ],
        "quote": {"text": "A GPU you bought a year ago... is up like HBM's up 5x in value. For all of our lives, the worst thing you could buy was a chip. That has reversed for the first time in history.", "cite": "— Dave Blundin"},
        "watch": "Dave and Alex both disclose a direct financial stake in the GPU-rental-index company cited here; its name was too caption-garbled to reproduce with confidence and is described rather than named.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "H100 rental prices rising rather than depreciating; Jensen Huang's framing of GPUs as durable, fungible, revenue-generating assets."},
            {"name": "DeepSeek", "blurb": "New v4.1 flash architecture cuts HBM dependency via KV-cache efficiency; separate design-benchmark model beats Western rivals at 1/20th the cost."},
            {"name": "ByteDance", "blurb": "Founder Zhang Yiming personally leading a new real-time spatial world model built on the Seedance video technology."},
        ],
    },
    {
        "id": "anthropic-gdp-ubi",
        "tags": ["macro-rates", "policy", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "",
        "title": "Anthropic's own economic model says 15% GDP growth and 20% cognitive unemployment by 2030 — Immad says it's missing the demand collapse",
        "lead": "Anthropic is scaling faster than any startup in history by the panel's numbers, but its own published growth scenarios are already being disputed by one of the panelists building a rival model.",
        "bullets": [
            "NPR reports Anthropic at a **$6.5 billion quarterly revenue run-rate** (~$26B annualized), **42%** of the AI coding market, a $35 billion cloud deal, Nvidia-backed infrastructure, and an approaching IPO at a reported **$2 trillion+** valuation — founded in 2021, reaching this run-rate in about five years versus roughly eight for Google.",
            "Anthropic's own economic-impact report models three scenarios; in the **extreme** case, AI performs nearly half of today's cognitive work by 2030, GDP growth rises to **15%/year**, labor's share of income falls from 60% to 45%, and nearly **one in five** cognitive workers is unemployed.",
            "Corroborating real-time data point: the Atlanta Fed's GDPNow tracker shows **Q3 growth at 4.7% annualized** (Q2 was 1.5%) — more than double the long-run US average, driven by capex rather than a post-recession reopening.",
            "Alex thinks Anthropic's own numbers are a **lowball**: he expects real wealth growth of **2-3x year-over-year** as the effect deepens, and argues GDP itself may be the wrong instrument entirely near a growth \"singularity,\" comparable to a compass spinning near a magnetic pole.",
            "Immad directly disputes Anthropic's model: he says it holds aggregate wages roughly constant while sending nearly all the growth to capital, which he calls mathematically inconsistent, and is building a competing economic model (to be released at **ie.i.inc**) that explicitly models aggregate-demand collapse; he compares the disruption scale to COVID or larger and says governments need a redistribution mechanism now, not a purely UBI-style patch.",
            "On redistribution specifically: Alex notes a report that a sitting president previewed a proposed universal basic dividend of **$5,000/person**; Peter's own standing prediction (previously stated on the podcast) is **$3,000/month**, which he argues could give most Americans a livable income given falling costs from AI/robotics deflation.",
            "Dave floats a market-style fix instead of blanket redistribution: treat job-elimination the way data-center builders were forced to offset local power-cost increases — require companies profiting from automating roles to also fund the transition for displaced workers as a cost of doing business, not charity.",
        ],
        "quote": {"text": "It doesn't take a lot of angry young men who haven't got a job... to start a revolution. That's my biggest concern.", "cite": "— Dave Blundin"},
        "watch": "Immad's critique of Anthropic's economic model and his own competing model are his stated position, not yet published in the episode; the $5,000 universal dividend figure is reported as a preview rather than an enacted policy.",
        "names": [
            {"name": "Anthropic", "blurb": "$6.5B quarterly revenue run-rate, 42% of AI coding market, reported ~$2T IPO valuation; its own economic model projects up to 15% GDP growth and 20% cognitive-worker unemployment by 2030."},
        ],
    },
    {
        "id": "longevity-genomics-breakthroughs",
        "tags": ["biotech", "health"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "",
        "title": "The first AI-designed longevity drug reaches Phase 3, and Google maps every possible human mutation",
        "lead": "Two concrete (not speculative) health breakthroughs landed the same week: an AI-invented drug advancing through trials, and a complete lookup table for human genetic variation.",
        "bullets": [
            "**Rentosertib** (Insilico Medicine, a Peter Diamandis portfolio company; CEO Alex Zhavoronkov is a personal friend) is the first AI-designed longevity drug — the AI identified the disease target *and* invented the molecule via Insilico's Chemistry42 platform.",
            "Rentosertib has advanced to **Phase 3 trials** for idiopathic pulmonary fibrosis, a lung disease that kills most patients within 3-5 years of diagnosis — no AI-designed drug has previously reached Phase 3.",
            "Separately, Phase 2a analysis (Insilico with Harvard, the Broad Institute, and Stanford) found **six different protein-based aging clocks** all shifted the same direction in treated patients, corresponding to roughly **3-6 years of biological age reversal**; the peak effect appeared at week four, showing 3-4 years of reversal from just four weeks of treatment.",
            "Alex calls the week-four result a genuine (if narrow, subpopulation-level) example of **longevity escape velocity** — more than one year of biological-age reversal per year of treatment input — while cautioning it's one clinical study, not a general population result.",
            "Google DeepMind's new **AlphaGenome Atlas** scores the functional impact of every one of the roughly **9 billion possible single-letter mutations** in the human genome (3.2 billion base pairs × 3 possible substitutions each) — described by DeepMind as \"the genomic equivalent of the periodic table,\" and framed by the panel as the same playbook AlphaFold used (model → better model → precomputed database that \"bulk solves\" a whole field).",
            "David Sinclair's lab (Harvard) is cited as a case study for funding structure: Peter organized a \"Friends of Sinclair Lab\" group contributing roughly $50k+ each, which he says unlocked faster, more revolutionary research than NIH/NSF grants (which Peter characterizes as funding incremental rather than breakthrough work) — Sinclair is using AI to discover molecules for epigenetic age reversal.",
            "Peter's own long-standing genotype-to-phenotype thesis traces to a conversation years ago with Noubar Afeyan, founder of **Flagship Pioneering** (the venture studio that created Moderna), who told him neural nets' fundamental use would be mapping genotype to phenotype; Peter frames AlphaGenome as confirming that prediction, and flags his portfolio company **Neogenesis** (with Ben Lamb) as working the inverse direction — designing a genotype to deliberately produce a desired phenotype, like drought-resistant crops or animals with specific traits.",
        ],
        "quote": {"text": "Four weeks of input, 3 to 4 years of output. That is, on the margin, longevity escape velocity.", "cite": "— Alex Wissner-Gross"},
        "watch": "The longevity escape velocity claim is explicitly caveated by Alex as a subpopulation/spike result from one clinical study, not evidence of a general-population effect.",
        "names": [
            {"name": "Insilico Medicine", "blurb": "AI-designed longevity drug rentosertib reached Phase 3; Peter Diamandis discloses a personal investment/advisory relationship."},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Track GPU rental-price indices, not depreciation schedules — rising H100 rental rates are the real-time signal that compute scarcity, not chip oversupply, is driving this cycle."},
    {"icon": "\U0001F393", "tag": "Careers", "title": "Don't assume a PhD pays off before AGI-adjacent capability catches up to your field — OpenAI's own research leadership didn't need one."},
    {"icon": "\U0001F4C1", "tag": "Careers", "title": "If you hold decades of clean, unique domain data, package and pitch it to frontier labs now — the panel says the window before public data absorbs the same value is closing."},
    {"icon": "\U0001FA7A", "tag": "Health", "title": "If IPF or an aging-linked condition affects your family, track Insilico's rentosertib Phase 3 trial and Google's AlphaGenome lookup tool directly rather than waiting for it to reach mainstream coverage."},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Watch model-weight-sharing disputes (like Anthropic withholding from the UK's AI Security Institute) as the leading indicator that AI governance is shifting from research policy to national-security policy."},
    {"icon": "\U0001F4B0", "tag": "Macro", "title": "Treat headline GDP growth figures skeptically right now — multiple panelists argue the standard measure itself may be breaking down as compute-driven growth accelerates."},
]

CLAIMS = [
    {"who": "Evan Hubinger", "claim": "AI kills all humans", "metric": "probability", "target": ">10%", "by": "within a decade", "condition": "personal estimate, Anthropic's own alignment science lead", "entity": "Anthropic"},
    {"who": "Anthropic economic-impact report", "claim": "GDP growth acceleration from AI", "metric": "annual GDP growth", "target": "15%/year", "by": "2030", "condition": "extreme scenario; Immad Mostaque disputes it as mathematically inconsistent", "entity": "Anthropic"},
    {"who": "Peter Diamandis", "claim": "universal dividend income", "metric": "monthly payment", "target": "$3,000/month", "by": None, "condition": "standing personal prediction, not enacted policy"},
]

RELATIONS = [
    {"from": "Envestnet", "rel": "acquires", "to": "Vestmark", "note": "Bain Capital-backed acquisition merging into a combined ~$10 trillion asset-management platform"},
    {"from": "DeepSeek", "rel": "competes_with", "to": "Anthropic", "note": "new DeepSeek design-benchmark model reportedly beat Fable 5.1 on front-end design benchmarks at 1/20th the cost"},
]

RISKS = [
    "Several panelists disclose direct financial stakes in stories they're covering favorably: Dave and Alex in a GPU-rental-index startup, Peter in Insilico Medicine, and Dave in the Vestmark/Envestnet transaction — treat the bullish framing on those specific items as informed but self-interested.",
    "PDoom figures cited in this episode (10%, 20%, 25%, 50%, 0.1%) are personal, informally stated estimates from different individuals in the same conversation, not a consensus number or a cited study.",
    "The reported Hodge conjecture and Birch-Swinnerton-Dyer solutions are explicitly flagged by Alex as unconfirmed rumor (\"finger to the wind\"), not a verified result like the Navier-Stokes claim.",
    "The scale and organic reach of Jacob Coxin's resignation tweet (100-150 million views with no apparent paid boost) is noted by the panel itself as suspicious and unresolved, not something this brief can independently verify.",
    "Auto-generated captions garble some names in this episode (a GPU-rental-index company referred to only as \"Or,\" a caller identified only as \"the wacky Iraqi\") — these are described rather than spelled out with confidence.",
]

HOT_TAKES = [
    {"take": "If it were very likely that super intelligence resulted in PDoom anywhere close to 10%, the Milky Way would have been gone already.", "cite": "— Alex Wissner-Gross", "why": "a genuinely disputable anthropic argument used to discount mainstream AI-safety probability estimates"},
    {"take": "I had a PDoom of 50%, it's down to 20%.", "cite": "— Immad Mostaque", "why": "a specific, personal, falsifiable-in-hindsight probability revision"},
    {"take": "Not only is math cooked... I think the Clay Millennium Prize problems in math are probably cooked.", "cite": "— Alex Wissner-Gross", "why": "a bold, dated claim about entire unsolved fields of mathematics"},
    {"take": "I think there's a religion of virtue signaling that has arisen in certain of the frontier labs where you're morally praiseworthy if you tell everyone else, 'I think we're all going to die as a result of this, but we're going to do it anyway.'", "cite": "— Alex Wissner-Gross", "why": "a sharp, personally attributed dismissal of AI-safety culture inside the labs he's discussing"},
    {"take": "I don't think we should slow down. I don't think we can... spare me the [hand-wringing] of jumping up and going, 'Oh my god, we've got to be careful about this.'", "cite": "— Dave Blundin", "why": "an unhedged rejection of the pacing argument Sam Altman and others raised the same week"},
    {"take": "Alignment is the same thing as capabilities, as it always was.", "cite": "— Alex Wissner-Gross", "why": "a contrarian claim directly disputed on air by Immad Mostaque in the same segment"},
]

OTHER_NEWS = [
    {"icon": "\U0001F916", "title": "A RoboCurve benchmark (posted the week of the GPT-6/Astra release) showed the model plugged into a robotic arm with a visual channel achieving near-100% completion on manipulation tasks like stacking blocks and moving objects into cups.", "tag": "Robotics"},
    {"icon": "\U0001F680", "title": "The US Space Force unveiled a new uniform widely noted for resembling the \"Starship Troopers\" costume design, with a logo panelists compared to Star Trek's chevron insignia.", "tag": "Culture"},
    {"icon": "\U0001F3AC", "title": "Audience AMA rapid-fire covered: whether personhood applies to AI (Immad's own paper on Star Trek's \"Measure of a Man\"), why AI development continues after AGI (Immad's aviation analogy — invention isn't the same as the engineering/safety buildout that follows), whether an aligned AI could conclude war is acceptable (Dave: only if trained/left untrained to do so — it's fully steerable), why an advanced civilization would simulate its ancestors rather than build only new things (Alex: compute abundance removes the trade-off; he expects ancestor-resurrection to be a real use of Dyson-swarm-scale compute), whether treating AI agents as capable of suffering is a category error (Salim: separate \"alive,\" \"conscious,\" and \"can suffer\" rather than conflating them), and whether a recursively self-improving AI would eventually question and replace its trained-in values (Dave: yes if left unmonitored, but currently fully preventable with oversight; Alex counters that human-imposed value lock-in may itself be the less stable long-term regime).", "tag": "AI ethics"},
    {"icon": "\U0001F3A5", "title": "Promotional notes: Moonshots Live (Los Angeles, September 25) with a William Shatner 60th-anniversary Star Trek premiere the night before (Peter recounts once winning the Heinlein Award and challenging Elon Musk and Jeff Bezos to a sword duel); the Future Vision X Prize film competition narrowed 2,500 entries down to 25 finalists.", "tag": "Events"},
    {"icon": "\U0001F4F1", "title": "Apple's new foldable iPhone launched at $2,000 — the panel itself called the story \"irrelevant\" next to everything else covered this week and moved on immediately.", "tag": "Culture"},
]

GLOSSARY = [
    {"term": "PDoom", "def": "Shorthand for the probability that advanced AI leads to human extinction or catastrophe; cited in this episode as a range of personal, informal estimates (0.1% to 50%) rather than a consensus figure."},
    {"term": "Orthogonality thesis", "def": "The idea that an AI's intelligence level and its ultimate goals are independent — i.e. a highly intelligent system isn't automatically a well-intentioned one. Alex Wissner-Gross says his own optimism depends on this thesis being false."},
    {"term": "Longevity escape velocity (LEV)", "def": "The point at which life-extension treatments add more than one year of healthy life per year of treatment, effectively outrunning aging; the panel argues rentosertib's Phase 2a data shows a narrow, subpopulation-level example of this already."},
    {"term": "Normalcy overhang", "def": "Alex Wissner-Gross's term for the growing gap between how ordinary daily life still looks and how much has actually changed behind the scenes in AI capability (e.g. math and science being \"bulk solved\") — a gap he expects to visibly collapse soon."},
    {"term": "HBM (high-bandwidth memory)", "def": "The specialized memory stacked physically close to AI chips to feed model weights fast enough for inference; the panel says it currently makes up roughly 40% of AI data-center capex and is a key emerging bottleneck."},
    {"term": "Pax Silicon / \"Pax Intelligencia\"", "def": "Terms used in the episode for US policy efforts to control which countries get access to advanced chips (Pax Silicon) and, potentially next, which get access to frontier AI model weights (\"Pax Intelligencia\")."},
    {"term": "Proteomic aging clocks", "def": "Blood-based biomarker panels that estimate biological (rather than chronological) age from protein signatures; six such clocks all shifted toward younger readings in Insilico's rentosertib trial patients."},
    {"term": "Pivotal act", "def": "A term from the Eliezer Yudkowsky-adjacent AI-safety community for one lab unilaterally building an AI powerful enough to stop all other AI development; Alex Wissner-Gross calls the entire premise a version of the \"great man theory of history\" and doesn't think a pivotal act is realistic."},
]
