META = {
    "title": "BREAKING: Elon Musk And Jensen Huang Speak At America.Gov Event, An AI-Powered Government Website",
    "channel": "Forbes Breaking News",
    "speakers": "Elon Musk (SpaceX/Tesla/xAI), Jensen Huang (Nvidia), Tom Brown (Anthropic co-founder), moderator (unnamed government host)",
    "date": "2026-09-29",
    "video_url": "https://www.youtube.com/watch?v=Gf-KssYwepc",
    "thread_line": "5 threads · power as the GDP lever · orbital compute & Starship · 'SI factories' reindustrialize · agent containment & the joint safety declaration · Opus 5.5 for ordinary Americans",
    "category": "market",
}

SNAPSHOT = [
    "Stage talk at the America.gov launch: **Elon Musk**, **Jensen Huang** and Anthropic co-founder **Tom Brown**, ~26 min, after a White House lunch.",
    "Elon's rule of thumb: every 1% more US power (~5 GW of the ~500 GW average) adds ~1% to GDP. China produces ~3x the electricity of the US.",
    "Jensen: each gigawatt yields ~$60B a year of output. Building 10-20 GW a year of 'SI factories' creates ~1M jobs, and 'the first time in 50 years we are re-industrializing'.",
    "SpaceX and Tesla aim for 200 GW a year of solar production. Starship reached orbit for the first time, carrying Starlink V3 satellites, and Elon targets a weekly or twice-weekly cadence next year.",
    "Nvidia's agent-safety stack pairs OpenShell for containment with BlueField chips for out-of-band monitoring. Jensen: safety vs. capability is a 'false choice'.",
    "The CEOs signed a joint SI safety declaration covering joint monitoring, third-party audits and 'grading each other's homework'.",
    "Tom Brown: Opus 5.5 handles longer delegated tasks. Jensen says a Claude research report takes him 3 minutes instead of 4-8 hours.",
]

THEMES = [
    {
        "id": "power-equals-gdp",
        "tags": ["energy", "ai-infra", "geopolitics"],
        "color": "green",
        "badge": "High conviction",
        "status": "THESIS — 1% MORE POWER ≈ 1% MORE GDP",
        "title": "Power is the binding constraint: every 5 GW is ~1% of US GDP, and China has 3x the electricity",
        "lead": "Both CEOs put energy at the base of the stack. The US wins on chips, algorithms and software but has to scale power generation and fabs to keep up with China.",
        "bullets": [
            "Jensen: superintelligence reinvents every layer of the computing stack, and generative computing runs on energy first, then land, power and shell, then chips, algorithms and apps. The US is world-class in chip design and algorithms, so the job is enabling power delivery.",
            "Jensen credits **Trump's pro-energy stance**: without it 'it would have been impossible' to build the data centers.",
            "Elon: 'we're winning on software… anything intellectual or digital', but China has about 3x US electricity production. The long-term challenge is power plus enough logic and memory fab capacity in the US 'or a safe region'.",
            "Elon's math: US average consumption is ~500 GW, so 5 GW of steady-state supply is 1% more power, which he says maps to ~1% more GDP because intelligence per watt keeps rising (better GPUs, better algorithms).",
            "Moderator: SpaceX's publicly discussed 10 GW would be ~25% of all US power additions, with rocket engineers helping build turbines. Elon: that's ~2% of GDP 'with the Rubin'.",
            "Jensen's version: 1% of US GDP is ~$300B, so 5 GW ≈ $300B, or roughly **$60B per gigawatt** per year (his first guess was $40-50B).",
        ],
        "quote": {"text": "I would bet anyone that 1% increase in power usage corresponds to roughly 1% increase in GDP.", "cite": "— Elon Musk"},
        "watch": "Both speakers sell into this math: Jensen supplies the GPUs whose output per watt drives the $/GW figure, and Elon is building the 10 GW. The GDP-per-watt ratio was worked out live on stage.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Jensen: rising compute per watt is what turns each GW into ~$60B a year of output; Rubin cited for the 10 GW math.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "orbital-compute-starship",
        "tags": ["space", "energy", "ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "STARSHIP FIRST ORBIT — STARLINK V3 DEPLOYED",
        "title": "SpaceX and Tesla target 200 GW a year of solar for orbital compute, and Starship is now in orbit",
        "lead": "Elon argues space unlocks far more energy than the ground, and that high returns on AI compute already justify today's launch costs.",
        "bullets": [
            "SpaceX with Tesla aims for **200 GW of solar production a year**. In space panels get nameplate output or better, versus 1/5 to 1/8 on the ground plus 'enormous batteries', because 'it's essentially always sunny in space'.",
            "Orbital compute 'is going to be a very big deal'. Google is about to send TPUs up, and an H100 went into orbit last year. Jensen: 'Putting Nvidia computing in space is the best way to get there.'",
            "Launch costs are still high, but compute returns are so good that orbit is 'quite affordable… this is the perfect time to do it'.",
            "Monday's flight took Starship to orbit for the first time and deployed **Starlink V3** satellites with a 737-sized wingspan, the largest payload to orbit since Skylab. Elon expects a weekly or twice-weekly cadence next year.",
            "Starship's job list: ~1 million tons to the Moon or Mars for a self-growing city, plus 'at least a few hundred gigawatts a year' of AI compute. 200 GW a year would be a 40% annual jump in US energy use, and 'it might end up being a terawatt one day'.",
        ],
        "quote": {"text": "It's essentially always sunny in space.", "cite": "— Elon Musk"},
        "watch": "Every figure here is Elon's own target for his own companies (SpaceX, Tesla), stated at a promotional government event.",
        "names": [
            {"name": "SpaceX", "blurb": "First orbital Starship flight carried Starlink V3; weekly cadence targeted next year; launch vehicle for hundreds of GW a year of orbital compute.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "weekly launches in 2027"},
            {"name": "Tesla (TSLA)", "blurb": "Partner with SpaceX on a 200 GW/year solar production target.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "Sending TPUs into orbit; Elon: 'Google agrees' on orbital compute.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "si-factories-jobs",
        "tags": ["ai-infra", "energy", "career"],
        "color": "green",
        "badge": "High conviction",
        "status": "10-20 GW/YEAR BUILDOUT — ~1M JOBS",
        "title": "'SI factories' are re-industrializing small-town America with blue-collar jobs",
        "lead": "Jensen renames data centers 'superintelligence factories' and pitches them as the first real US re-industrialization in 50 years, and Elon says xAI's host region now has more jobs than people.",
        "bullets": [
            "Jensen: they're not data centers but **SI factories**, because they produce economic value instead of storing data. Each one is a power plant, computing, networking and cooling in one complex system.",
            "The US is building 10-20 GW a year, which Jensen estimates creates ~1 million jobs in power plants, construction, cooling and pipe-fitting. That's 'the first time in 50 years we are re-industrializing the United States'.",
            "Jensen wants an economy 'that includes white collar jobs and blue collar jobs'. The industry must do better partnering with communities as data centers arrive 'so quickly'.",
            "Elon on **Colossus** and Macrohard: the region went from unemployment to a job shortage, 'there's more jobs than there are people', and xAI 'might have doubled their tax budget'. It offers half-price Starlink and is building a $250M water recycling plant.",
            "Jensen: for the first time, market forces fund sustainable energy (fusion, fission, small and large reactors, battery storage) without government subsidies.",
            "The moderator credits the two with 'more than $5T' of 401(k) wealth. Elon: 'Jensen's done five trillion by himself.' Jensen: 'around three and a half'.",
        ],
        "quote": {"text": "If you do things for the community, they will reciprocate.", "cite": "— Elon Musk"},
        "watch": "The community benefits at Colossus are the operator's own account, and the ~1M jobs figure is Jensen's on-stage estimate ('let's just estimate').",
        "names": [
            {"name": "xAI", "blurb": "Colossus/Macrohard: turned regional unemployment into a job shortage, roughly doubled the local tax base, $250M water recycling plant.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "agent-safety-declaration",
        "tags": ["policy", "ai-infra", "software"],
        "color": "amber",
        "badge": "Confirmed event",
        "status": "JOINT SI SAFETY DECLARATION SIGNED",
        "title": "Contain and monitor: Nvidia's agent-safety stack and a joint declaration where labs grade each other's homework",
        "lead": "Jensen frames agent safety as containment plus out-of-band monitoring, and the CEOs left a White House lunch with a signed joint safety declaration.",
        "bullets": [
            "Jensen's model: training is 'fairly safe', but during evaluation and deployment the agent must be tightly contained and monitored in real time. 'Even though you have it contained, you should never trust that it's contained.' It's like giving an employee limited rights and checking on them.",
            "Nvidia's new **open agent safety framework** uses OpenShell, a 'browser for agents' that isolates them with only the rights they need, and a **BlueField** chip that watches the agent out-of-band and escalates policy violations.",
            "The analogy from Nvidia's blog: fear of stolen credit cards once held back the internet, and making it safe enabled Amazon, Netflix, Google and X. Jensen: safety and capability are 'one and the same'. Autopilot is both more advanced and safer, and the trade-off 'those are false choices'.",
            "Jensen on values ('say something controversial'): an SI with judgment is like a **steak knife** that cuts medium-well but refuses rare meat. In cybersecurity a defender's moves look like an attacker's, so he questions 'how much judgment you really want these tools to have'.",
            "The **joint declaration** covers joint monitoring, board special committees and 'grading each other's homework'. It also requires internal controls, documented product intentions, internal and third-party external audits, and sharing best practices. Jensen: 'a lot of teeth' and it should be the industry standard. The White House will publish it soon.",
        ],
        "quote": {"text": "Even though you have it contained, you should never trust that it's contained.", "cite": "— Jensen Huang"},
        "watch": "Nvidia's safety answer is also a new product line (BlueField, OpenShell). The declaration text wasn't read out, and the official who convened it is garbled in the captions.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Launched an open agent safety framework: OpenShell containment plus BlueField out-of-band monitoring.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "opus-everyday",
        "tags": ["software", "consumer", "health"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "OPUS 5.5 RELEASED THIS WEEK",
        "title": "Opus 5.5 means longer delegated tasks and cheaper software, and Jensen uses Claude for weekend research",
        "lead": "Tom Brown pitches steady 'more IQ points per release' progress. The CEOs' own examples are research reports and medical second opinions.",
        "bullets": [
            "Tom Brown (Anthropic co-founder): Opus 5.5 'continues the normal progress'. The visible change is being able to delegate longer tasks than before.",
            "The less visible change: a huge amount of software will be written by models, so everyday products get higher quality and cheaper over time.",
            "Jensen uses **Claude** for comparative research: he lists every question, asks for a report with charts, and gets in about 3 minutes what used to take 4-8 hours of weekend reading.",
            "Elon: AI will become essential in professional and private life. He's heard 'many' cases where people submitted X-rays or MRIs, the AI caught what a doctor missed, and 'but for AI, they would have died'.",
            "The moderator cites stories of superintelligence finding life-saving new uses for existing drugs.",
        ],
        "quote": {"text": "Nothing gives me more joy than… just watch it go, and it comes back and it creates a beautiful report.", "cite": "— Jensen Huang"},
        "watch": "The medical rescue stories are anecdotes Elon has heard ('I've heard many such cases'), not cited cases. Tom Brown is promoting his own company's model.",
        "names": [
            {"name": "Anthropic", "blurb": "Opus 5.5: longer delegable tasks; Jensen uses Claude for research reports.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "⚡", "tag": "Energy", "title": "Size AI-infrastructure theses on gigawatts of power added, not chip counts; ~$60B of output per GW is the stated yardstick."},
    {"icon": "\U0001F680", "tag": "Space", "title": "Watch Starship's cadence in 2027: weekly launches are the gate for any orbital-compute thesis."},
    {"icon": "\U0001F3ED", "tag": "Industry", "title": "Look at power-plant, cooling and construction trades as the direct beneficiaries of a 10-20 GW/year buildout."},
    {"icon": "\U0001F6E1", "tag": "AI security", "title": "Contain agents and monitor them out-of-band, and assume containment can fail."},
    {"icon": "\U0001F4DD", "tag": "Productivity", "title": "Delegate multi-question comparative research to a frontier model as one structured prompt with a report and charts."},
]

HOT_TAKES = [
    {"take": "I would bet anyone that 1% increase in power usage corresponds to roughly 1% increase in GDP.", "cite": "— Elon Musk", "why": "quantified macro claim he offers to bet on"},
    {"take": "This is the first time in 50 years we are re-industrializing the United States.", "cite": "— Jensen Huang", "why": "sweeping historical claim"},
    {"take": "The idea that if you advance capability it somehow compromises safety… those are false choices.", "cite": "— Jensen Huang", "why": "rejects the core safety-vs-speed premise"},
    {"take": "There's a question in my mind yet about how much judgment you really want these tools to have.", "cite": "— Jensen Huang", "why": "against giving models values, the opposite of Anthropic-style constitutions"},
    {"take": "Starship… will launch at least a few hundred gigawatts a year of AI compute… it might end up being a terawatt one day.", "cite": "— Elon Musk", "why": "extreme scale claim"},
]

CLAIMS = [
    {"who": "Elon Musk", "claim": "Each 1% increase in US power use (~5 GW) yields ~1% GDP growth; 10 GW adds ~2%.", "metric": "GDP per GW", "target": "~1% GDP per 5 GW", "by": None, "condition": None, "entity": None},
    {"who": "Jensen Huang", "claim": "Each gigawatt of AI capacity generates about $60B of economic output per year.", "metric": "annual output per GW", "target": "~$60B", "by": None, "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Jensen Huang", "claim": "A 10-20 GW/year US buildout creates about 1 million jobs.", "metric": "jobs from buildout", "target": "~1,000,000", "by": None, "condition": "at 10-20 GW/year", "entity": None},
    {"who": "Elon Musk", "claim": "SpaceX and Tesla reach 200 GW per year of solar production.", "metric": "solar production", "target": "200 GW/year", "by": None, "condition": None, "entity": "SpaceX"},
    {"who": "Elon Musk", "claim": "Starship reaches a weekly or twice-weekly launch cadence next year.", "metric": "Starship cadence", "target": "weekly to twice weekly", "by": "2027", "condition": None, "entity": "SpaceX"},
    {"who": "Elon Musk", "claim": "Starship launches at least a few hundred GW a year of AI compute, possibly a terawatt eventually.", "metric": "orbital compute launched", "target": "few hundred GW/year to 1 TW", "by": None, "condition": None, "entity": "SpaceX"},
    {"who": "Elon Musk", "claim": "A self-growing Moon or Mars city needs about 1 million tons delivered to the surface.", "metric": "tonnage to surface", "target": "~1,000,000 tons", "by": None, "condition": None, "entity": "SpaceX"},
    {"who": "Elon Musk", "claim": "The White House publishes the joint SI safety declaration.", "metric": "declaration publication", "target": "published", "by": "soon", "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "SpaceX", "rel": "partners_with", "to": "Tesla (TSLA)", "note": "joint 200 GW/year solar production target"},
]

OTHER_NEWS = [
    {"icon": "\U0001F1FA\U0001F1F8", "title": "The event launched **America.gov**, an AI-powered government website. The moderator framed the US as leading every tech revolution (Wright brothers, the Moon, the internet) and called the 'super intelligence' rebrand 'good branding'. Tom Brown arrived late after a wrong turn.", "tag": "Policy"},
]

GLOSSARY = [
    {"term": "SI factory", "def": "Jensen's term for AI data centers, which produce economic value (tokens, intelligence) rather than store data."},
    {"term": "OpenShell", "def": "Nvidia's containment layer, a 'browser for agents' that isolates them and limits their rights."},
    {"term": "BlueField", "def": "Nvidia's DPU chip, used here to monitor agent behavior out-of-band, outside the agent's sandbox."},
    {"term": "Out-of-band monitoring", "def": "Watching a system from separate hardware it can't reach or tamper with."},
    {"term": "Nameplate capacity", "def": "A generator's rated maximum output; ground solar delivers a fraction of it."},
    {"term": "Colossus / Macrohard", "def": "xAI's large compute clusters, which Elon says transformed their host region's job market."},
]
