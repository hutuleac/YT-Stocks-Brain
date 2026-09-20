"""Data file for Dan Ives x Anthony Pompliano — Wall Street's Top AI Bull Reveals the Real Bottleneck (It's Not Chips)."""

META = {
    "title": "Wall Street's Top AI Bull Reveals the Real Bottleneck (It's Not Chips)",
    "channel": "Anthony Pompliano",
    "speakers": "Dan Ives (guest, partner/senior managing director at Yorkville Ives), interviewed by Anthony Pompliano (host)",
    "date": "2026-07-27",
    "video_url": "https://www.youtube.com/watch?v=agIvg0DkW50",
    "thread_line": "5 threads · why Chinese open-source models don't crack Anthropic/OpenAI's moat, the AI stack fracturing instead of one model 'eating everything,' the real bottlenecks (memory, power, data centers, not chips), the Mag 7 capex-vs-cash-flow debate, and Dan Ives' 'third inning' call plus his new Yorkville Ives merchant bank.",
    "category": "market",
}

SNAPSHOT = [
    "Dan Ives dismisses Chinese open-source models (the 'mini DeepSeek moment') as a threat to Anthropic/OpenAI: the moat is proprietary data and enterprise relationships, not raw model performance, and models broadly get cheaper and more commoditized over time regardless of origin.",
    "He rejects a 'fat AI model' thesis (one model eating the whole stack, echoing crypto's discredited 'fat protocol' thesis) — expects the stack to fracture into models, infrastructure, and specialized applications, which he sees as healthy for pricing and innovation.",
    "His real-bottleneck ranking: memory (no equilibrium until 2028-2029), power/energy (needs 3-4x more supply), and getting data centers physically built in the US — not chip supply, which he says is running at roughly 12-to-1 demand-to-supply on his recent Asia trip.",
    "Flags New York's data-center moratorium and broader political grandstanding as the single most dangerous risk to US AI leadership — the first time in 30 years the US leads China on tech, in his framing, and one it could squander through NIMBYism.",
    "On the Mag 7 free-cash-flow cliff funding a semiconductor revenue boom: he calls it a deliberate 10-20 year bet (echoing Apple's 2008 iPhone bet and Microsoft's early cloud pivot), reads Anthropic's revenue deceleration as healthy competition rather than a red flag, and thinks memory names may already be 'overdone' relative to underappreciated hyperscalers.",
    "Predicts the AI trade is still in the 'third inning' (his Vegas-1955-building-the-strip analogy), expects monetization proof points across hyperscalers and software in the second half of the year, and flags energy (not chips) as the multi-year bottleneck race still 2-3 years from mattering.",
    "Personal/career note: Ives is launching a new 'modern merchant bank,' Yorkville Ives, combining investment banking, research, and direct investing, focused on tech/energy/infrastructure/healthcare.",
]

THEMES = [
    {
        "id": "china-open-source-no-crack",
        "tags": ["ai-infra", "geopolitics"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — moat holds, model layer still commoditizing",
        "title": "Chinese Open-Source Models Are a 'Mini DeepSeek Moment,' Not a Crack in the Armor",
        "lead": "**Ives' response to the Chinese open-weight scare:** Anthropic and OpenAI are 'playing a whole different game' that isn't measured by raw model benchmarks — the real value sits in proprietary data and enterprise relationships, which open-source competition doesn't touch.",
        "bullets": [
            "Points out the irony of US labs crying foul over Chinese model 'distillation' while Anthropic itself just settled a $1.5 billion case with 500,000 authors over training-data use — 'people in glass houses shouldn't throw stones.'",
            "China's models improving despite being cut off from top Nvidia chips (using Huawei and other lower-tier silicon) is read as a sign models will keep getting smarter and cheaper across the board, which he frames as bullish for adoption, not bearish for the leaders.",
            "Notes American open-source is essentially absent from the conversation — Meta's Llama took 'a shot' at the category and stepped back, while Nvidia (per Jensen Huang) is comfortable backing open source generally since cheaper, more widely used models grow the whole industry it sells chips into.",
            "Raises the 'cultural weights' problem directly (echoing Anthony's own Silvian build): whether Chinese open-source models carry implicit socialist/Eastern-world defaults the way TikTok's algorithm carries implicit bias — expects the world to bifurcate into cordoned-off model ecosystems (US/China today, eventually Middle East, Europe, even country-specific models).",
            "For the first time in 30 years, he says, the US is unambiguously ahead of China on tech — the risk isn't the Chinese models themselves, it's the US undermining its own lead through policy overreaction or self-inflicted bottlenecks.",
        ],
        "quote": {"text": "The reality is like Anthropic and OpenAI, they're playing a whole different game. No one will compare from a model perspective to where they are.", "cite": "— Dan Ives"},
        "watch": None,
        "names": [
            {"name": "Anthropic", "blurb": "Read as structurally insulated from Chinese open-source competition by its data/enterprise moat; recently settled a $1.5B authors' copyright case.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Meta (META)", "blurb": "Llama cited as America's one real open-source swing, which Ives implies underperformed expectations ('back to the drawing board').", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Comfortable with open-source proliferation since cheaper/more numerous models grow overall chip demand.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "fat-ai-model-fracture",
        "tags": ["ai-infra", "software"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — stack fracturing thesis vs. 'model eats everything' bulls",
        "title": "No 'Fat AI Model': the Stack Is Fracturing Into Models, Infrastructure, and Specialized Apps",
        "lead": "**Ives borrows crypto's discredited 'fat protocol' thesis as a warning:** the bet that a handful of frontier models will capture nearly all AI value is, in his view, the same mistake crypto investors made betting value would concentrate at the base-layer protocol instead of spreading to applications.",
        "bullets": [
            "Draws the direct parallel: crypto's 'fat protocol thesis' (value accrues to Bitcoin/Ethereum-style base layers) didn't play out — value spread into applications and infrastructure instead, and he expects the same fracture in AI rather than a handful of labs 'eating the whole stack.'",
            "Cites Sierra (Bret Taylor's company) publishing an engineering blog describing roughly 20 different models routed per query as the emerging pattern — a query might best be answered by Claude, ChatGPT, Kimi K3, or something else, decided by a model router rather than a single default model.",
            "Argues this makes the model router itself the new 'general purpose' layer, while individual models get super-specialized — proprietary data, agentic file systems, memory systems, and workflow-specific tuning become the real differentiator between two companies using the identical underlying model.",
            "Rejects the earlier PR-driven fear that AI would 'eat everyone's lunch' (including cybersecurity) — says cybersecurity budgets will likely double because of AI, not shrink, and expects a wave of disintermediated SaaS ('SaaS apocalypse') alongside genuinely new company formation, not a winner-take-all outcome.",
            "Sees Anthropic's own revenue growth deceleration as healthy evidence of this fracture already happening — competition and more players is bullish for the ecosystem even if it dents any single company's growth rate.",
        ],
        "quote": {"text": "I just don't see that world happening — I see it being very much fractured, and I think that's good because it ultimately creates better performance, better applications, and lower cost for the customer.", "cite": "— Dan Ives"},
        "watch": None,
        "names": None,
    },
    {
        "id": "real-bottlenecks",
        "tags": ["semis", "energy", "policy"],
        "color": "red",
        "badge": "Confirmed constraint",
        "status": "WATCHING — memory until 2028-2029, power 2-3 years out",
        "title": "The Real Bottlenecks Are Memory, Power, and Data Centers — Not Chips",
        "lead": "**Ives' bottleneck ranking inverts the popular narrative:** chip supply/demand is roughly 12-to-1 on his own recent Asia trip, but he says memory, energy, and getting data centers physically permitted and built in the US are the constraints that actually matter.",
        "bullets": [
            "Memory is 'the biggest bottleneck' — too few players (SK Hynix, Micron, Samsung) and no equilibrium expected until 2028-2029; separately notes the stocks may have gotten 'overdone' on the memory side relative to underappreciated hyperscalers.",
            "Energy is the next-biggest debate: the buildout needs 3-4x more power to support even 20-25% of companies fully embracing AI, spanning natural gas, nuclear fission, and eventually nuclear fusion — he expects this to become the dominant constraint in roughly 2-3 years.",
            "Data center construction in the US is flagged as the single most dangerous political risk to the AI buildout — cites New York's proposed moratorium specifically, with capacity simply shifting to Tennessee or Texas if blocked, and frames it as the actual US-vs-China battleground (the US already leads on chips, models, hyperscalers, and IP; China leads on robotics and energy).",
            "Makes an explicit local-economics case for data centers: lower concentrated-area property taxes, direct job creation plus a construction-industry boom, and a 'ripple effect' pulling other businesses to locate nearby (cites the Austin, Texas metro area as the pattern), comparing the opportunity to reviving Midwest factory towns hollowed out by offshoring.",
            "Calls the US-China race for AI dominance a 'pole position' the US could still lose by self-sabotage — warns against big model labs lobbying to ban Chinese open-source models on one side and local communities lobbying for data-center bans on the other, both turning to government referee intervention instead of letting the market run.",
        ],
        "quote": {"text": "I just think the biggest bottleneck in this country is energy. I don't even think there's a debate.", "cite": "— Dan Ives"},
        "watch": "Ives concedes some data-center concerns (water use, cooling, noise) are legitimate and deserve vetting — his objection is to blanket political moratoriums, not to any scrutiny at all.",
        "names": [
            {"name": "Micron (MU)", "blurb": "Named among memory players whose stock charts 'look like cartoons' — Ives flags the group as possibly overdone near-term despite a genuine multi-year supply shortage.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "mag7-capex-bet",
        "tags": ["finance", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — 18-24 month window to prove monetization",
        "title": "Mag 7 Free Cash Flow Is Falling Off a Cliff to Fund Semis — Ives Calls It a Decade-Long Bet",
        "lead": "**Ives frames the Mag 7 capex-vs-free-cash-flow chart** (cash flow collapsing while semiconductor revenue explodes in the opposite direction) as a deliberate multi-decade bet, comparable to Apple's 2008 iPhone bet or Microsoft's early cloud pivot, not reckless overspending.",
        "bullets": [
            "Companies are making '10-year, 20-year bets,' financed partly through debt and equity raises, because their own enterprise conversations show them what the demand pipeline actually looks like — Oracle is called out as the 'poster child' for taking on debt against $300B+ in OpenAI-related deal commitments and getting punished for it in its stock.",
            "Draws historical parallels for gut-check periods: Nvidia doubling down on AI in 2022 despite being 'a gaming GPU company'; Apple releasing the iPhone into the 2008 financial crisis when critics said to refocus on core products; Microsoft's Satya Nadella pushing into cloud when critics said to stick to Windows.",
            "His test for whether the bet is wrong: by this point in the cycle, companies would already be seeing warning signs (no ROI, pullback signals) — instead he cites Palantir, Snowflake, and Databricks as evidence enterprises are increasingly seeing real ROI from AI spend, which is why capex keeps climbing rather than getting cut.",
            "Expects 'gut check moments' to continue around Chinese models and the capex debate, but says the second half of the year is when monetization bets need to start showing results across hyperscalers, software, and the broader stack — the actual test of the thesis.",
            "Disagrees with the view that Mag 7/big tech has become less important relative to idiosyncratic memory and chip names — argues hyperscalers remain the biggest ultimate winners in the AI buildout, not just the suppliers underneath them.",
        ],
        "quote": {"text": "This is it's building the Las Vegas. It's like we're in Vegas 1955 building the strip. That's essentially what we're doing.", "cite": "— Dan Ives"},
        "watch": "Ives' own north star for validation (H2 monetization proof) hasn't happened yet as of this conversation — this is a call to watch for, not a result already confirmed.",
        "names": [
            {"name": "Oracle (ORCL)", "blurb": "Named as the 'poster child' for AI capex risk — took on significant debt against $300B+ of OpenAI-linked deal commitments; stock got hit as a result.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Cited as the 2022 example of a company making a bet ('gaming GPU company' pivoting hard into AI) that looks obvious only in hindsight.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Palantir (PLTR)", "blurb": "Cited as evidence enterprises are seeing real AI ROI, supporting continued capex.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Snowflake (SNOW)", "blurb": "Cited alongside Palantir and Databricks as proof points of enterprise AI ROI.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "third-inning-yorkville",
        "tags": ["finance", "career"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — monetization proof due H2 2026",
        "title": "'Still Third Inning': Ives' Next-6-Months Call, Plus His New Merchant Bank",
        "lead": "**Ives' headline prediction:** the AI trade has more volatility and 'narrative' risk ahead, but is still early in a cycle he now calls the genuine fourth industrial revolution — and he's building a new bank to back it.",
        "bullets": [
            "Predicts continued 'gut check moments' around Chinese models, the capex debate, and investor patience with free cash flow, but expects monetization bets to start proving out across hyperscalers and software in the second half of the year.",
            "Says he's now more confident this is the genuine 'fourth industrial revolution' than he was 18 months ago, based on enterprises actually adopting AI at scale rather than just talking about it — dismisses bubble comparisons as describing a 'vastly different' market than 2000.",
            "Volatility is framed as something the best investors want, not fear — warns that social-media narrative reactions (e.g. Nvidia's stock the hours after an earnings call) are a trap; the actual signal is in capex trends and conference-call commentary across sectors, not just tech.",
            "Announces his move to launch Yorkville Ives, a new 'modern merchant bank' combining investment banking, proprietary research, and direct investing (skin in the game) — targeting tech, energy, infrastructure, and healthcare, positioned as a boutique 'SWAT team' rather than a scaled bank.",
        ],
        "quote": {"text": "I would say much more confident that this is truly the fourth industrial revolution today than maybe a year and a half ago.", "cite": "— Dan Ives"},
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F30F", "tag": "AI ethics", "title": "Weigh a model's 'cultural weights' before enterprise adoption — the same concern Ives raises for Chinese open-source models as TikTok's algorithm."},
    {"icon": "\U0001F4BE", "tag": "Markets", "title": "Watch memory equilibrium timing (2028-2029) and power buildout (3-4x needed) as the real AI bottlenecks, not chip announcements."},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Track data-center moratorium fights (New York and beyond) as a genuine US-China competitiveness risk, not just local NIMBY noise."},
    {"icon": "\U0001F4B0", "tag": "Markets", "title": "Judge Mag 7 capex by H2 2026 monetization proof points across hyperscalers and software, not by the free-cash-flow chart alone."},
    {"icon": "\U0001F3B0", "tag": "Markets", "title": "Treat AI-stack investing as a 'fracturing' bet (apps, infra, specialized workflows) rather than a bet on a handful of models eating everything."},
]

CLAIMS = [
    {"who": "Dan Ives", "claim": "chip demand-to-supply ratio observed on his recent Asia trip", "metric": "demand:supply ratio", "target": "~12:1", "by": None, "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "memory market reaches supply/demand equilibrium", "metric": "equilibrium timing", "target": None, "by": "2028-2029", "condition": None, "entity": None},
    {"who": "Dan Ives", "claim": "power needed to support broader AI adoption", "metric": "energy supply multiple needed", "target": "3-4x current supply", "by": None, "condition": "if 20-25% of companies fully embrace AI", "entity": None},
    {"who": "Dan Ives", "claim": "AI monetization bets prove out across hyperscalers and software", "metric": "monetization evidence", "target": None, "by": "second half of 2026", "condition": None, "entity": None},
    {"who": "Anthropic (cited by Dan Ives)", "claim": "authors' copyright settlement over training data", "metric": "settlement value", "target": "$1.5 billion", "by": None, "condition": "covering roughly 500,000 authors", "entity": "Anthropic"},
]

RELATIONS = [
    {"from": "Oracle (ORCL)", "rel": "customer_of", "to": "OpenAI", "note": "$300B+ in contracted compute deals cited by Dan Ives as the source of Oracle's added debt load"},
    {"from": "Meta (META)", "rel": "competes_with", "to": "Anthropic", "note": "Llama positioned as Meta's open-source answer to closed-source frontier labs, per Dan Ives"},
]

HOT_TAKES = [
    {"take": "People in glass houses shouldn't throw stones.", "cite": "— Dan Ives", "why": "A pointed jab at US labs complaining about Chinese model 'distillation' right after Anthropic's own $1.5B authors settlement."},
    {"take": "I just don't see that world happening — I see it being very much fractured.", "cite": "— Dan Ives", "why": "A direct rejection of the 'a few models eat the whole AI stack' bull case, staking a contrarian structural view."},
    {"take": "I just think the biggest bottleneck in this country is energy. I don't even think there's a debate.", "cite": "— Dan Ives", "why": "Ranks energy above chips and even memory as the constraint that matters most — checkable against how the buildout actually plays out."},
    {"take": "For the first time in 30 years, the US is ahead of China when it comes to tech.", "cite": "— Dan Ives", "why": "A strong, specific, checkable historical claim about the balance of tech power."},
    {"take": "It's very dangerous when the political piece gets in the technology piece.", "cite": "— Dan Ives", "why": "A blunt warning aimed at both AI-lab lobbying against Chinese models and local moratoriums against data centers — an equal-opportunity criticism."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3E6", "title": "Dan Ives is launching Yorkville Ives, a new 'modern merchant bank' combining investment banking, research, and direct investing, focused on tech, energy, infrastructure, and healthcare.", "tag": "Career move"},
    {"icon": "\U0001F5FD", "title": "Governor Hochul's proposed New York data-center moratorium is singled out as the most dangerous near-term policy risk to US AI infrastructure buildout, with capacity shifting to Tennessee or Texas if enacted.", "tag": "Policy watch"},
]

GLOSSARY = [
    {"term": "Fat protocol thesis", "def": "A crypto-era theory that value accrues mainly to base-layer protocols (e.g. Bitcoin, Ethereum) rather than the applications built on top; Ives argues AI is proving the same thesis wrong by fracturing value across models, infrastructure, and apps."},
    {"term": "Cultural weights", "def": "Implicit values or worldview embedded in a model's training data (e.g. capitalist vs. socialist defaults) that can surface in its answers without being explicitly programmed — raised as an underrated risk of adopting foreign open-source models."},
    {"term": "Model router", "def": "A system that directs each user query to whichever underlying model (open-source, closed-source, cheaper, or more powerful) is best suited to answer it, rather than routing every query to one default model."},
    {"term": "SaaS apocalypse", "def": "The thesis that AI will disintermediate large swaths of seat-based software-as-a-service companies by automating the workflows their software used to support."},
]
