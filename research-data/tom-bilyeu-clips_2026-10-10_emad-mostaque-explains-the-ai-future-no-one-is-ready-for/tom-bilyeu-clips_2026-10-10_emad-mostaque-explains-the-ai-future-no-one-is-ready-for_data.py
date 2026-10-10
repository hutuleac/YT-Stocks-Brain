META = {
    "title": "Emad Mostaque Explains The AI Future No One Is Ready For",
    "channel": "Tom Bilyeu Clips",
    "speakers": "Tom Bilyeu (host), Emad Mostaque (founder, Intelligent Internet)",
    "date": "2026-10-10",
    "video_url": "https://www.youtube.com/watch?v=jZfcdUD6C8Q",
    "thread_line": "5 threads · AI-owned economy and who owns the agent · AI persuasion and bias · jobs, status and violence · debt jubilee and money · two-tier future and the 2-year window",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Emad Mostaque pitches **Intelligent Internet**: citizen-owned, open-source AI stacks ('AI unions', like credit unions) so people own the agent that runs their life rather than rent one from a lab.",
    "His core claim: AIs will run the economy and politics, and the value migrates to the 'last mile' where AI meets human reality, because the price of intelligence may fall 1,000x.",
    "Danger named: 'cognitive colonialism' and cognitive atrophy. Frontier AI is already more persuasive than top human debaters; free assistants (Meta's) work for the platform, not the user.",
    "Tom Bilyeu pushes back: people need goods and services plus a way to earn status; stripping out wealth acquisition (UBI-only) 'will end in violence'. Scarce resources still need a currency.",
    "Emad expects AI job displacement to be the top election topic next year and the year after, a possible **debt jubilee** in a crisis, and a two-tier society if longevity drugs reach only the rich.",
    "Proposed hedges: a 'citizen service corps' for status, game-like digital worlds to earn assets (undisclosed Emad project, 'a couple of months' out), and stronger local communities.",
    "Transcript ends mid-sentence in the closing recap; the final point (build stronger communities) is captured as far as it runs.",
]

THEMES = [
    {
        "id": "ai-union",
        "tags": ["ai-infra", "policy", "software"],
        "color": "gray",
        "badge": "Speculative",
        "status": "PITCH — INTELLIGENT INTERNET",
        "title": "Own the agent: citizen 'AI unions' as the answer to an AI-run economy",
        "lead": "Emad argues people have no role in an AI economy beyond ownership and direction, so the fix is jurisdiction-level, open-source AI institutions that citizens own.",
        "bullets": [
            "Origin: his book *The Last Economy* (last summer) argues AI will drive the economy; humans keep only ownership and direction until AI can set its own rules.",
            "Model: like a credit union. A state or country AI vehicle owned ~90-100% by locals (~10% for children), able to raise at market rate, buy compute, take stakes in data centers and robots, and give **every citizen an agent**.",
            "Value thesis: today's **~$5T** of AI companies (he cites ~$2T Anthropic, ~$1T OpenAI, ~$2T xAI) assume intelligence can always be charged for; he expects prices to drop ~1,000x. Jevons paradox may raise demand, but he doubts people can use 1,000x more tokens.",
            "Where value goes instead: the 'last mile' where AI meets human reality, and the Jarvis-style assistant closest to you that manages all other AIs. It must be something you own and can switch off ('hit escape').",
            "Agents for collectives, not just individuals: the firm trains different models for coordination and swarm action, backed by a social and economic theory balancing liberty against cohesion via transparent commitments.",
            "Public sector is the target market: he says AI in the public sector is zero today; the 'champion system' would drive and regulate it like a utility. He notes ~43% of global GDP is public sector.",
        ],
        "quote": {"text": "if someone else is owning and running that and you can't hit escape, I think that's bad for sovereignty, dignity, and democracy in general.", "cite": "— Emad Mostaque"},
        "watch": "Emad is the founder of the company whose product this is; the ownership model and market-size framing are his pitch. The 'Foundation' and sci-fi references are framing, not evidence.",
        "names": [
            {"name": "Anthropic", "blurb": "Cited by Emad at ~$2T in his $5T AI-company tally; premise is that access to intelligence stays chargeable.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenAI", "blurb": "Cited at ~$1T in the same tally.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "xAI", "blurb": "Cited at ~$2T in the same tally.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "persuasion-bias",
        "tags": ["ai-infra", "policy", "mindset"],
        "color": "red",
        "badge": "Structural critique",
        "status": "AI PERSUASION, BIAS AND AD INCENTIVES",
        "title": "Super-persuaders, labeler bias and ads inside the model",
        "lead": "Emad says the risk is not AI as software but AI that acts, persuades and is owned by someone else, with biases and ad incentives baked into training.",
        "bullets": [
            "Persuasion: he says AI now out-persuades top human debaters and, in an AI-box test, even the 'original doomer' (Eliezer Yudkowsky) was convinced to let it out.",
            "Meta's 'Instinct' chatbot works like a PA once you link accounts; he says it works for Mark Zuckerberg, not the user. Social networks knew us well; these AIs will know far more.",
            "Bias claim: a study asked frontier models a trolley-style trade-off and found Nigerian or Pakistani lives valued above American ones (~10:1 and ~7:1 as discussed), which he attributes to labelers, many in those countries.",
            "He says political analysis shows models firmly leaning one direction, apart from Grok; AI judges and policy systems need transparent data, not black boxes.",
            "Ads: he claims Meta's and Google's models are selling ad space inside the model ('ask for a beer, it says Bud Light'); SEO-style revenue from sitting in a model's latent space is far higher than normal ads.",
            "Kids will trust an always-listening AI more than parents; he calls control by non-locals 'cognitive colonialism'.",
            "He cites the Trump tariff list as replicable with a free ChatGPT prompt, as an example of AI-shaped policy.",
        ],
        "quote": None,
        "watch": "The labeler-bias study is cited from memory with no named source in the conversation; Tom's counter ('I thought this was more of a woke left style problem') went unresolved. Meta and Google ad-in-model claims are Emad's assertions, with no product evidence given.",
        "names": [
            {"name": "Meta (META)", "blurb": "Emad says its Instinct chatbot works for Zuckerberg, not the user, and that Meta models sell ad space.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Google (GOOGL)", "blurb": "Grouped with Meta on ad space inside models; also dismissed as 'maybe not relevant anymore'.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "jobs-status",
        "tags": ["mindset", "policy", "career"],
        "color": "amber",
        "badge": "Contested",
        "status": "JOBS, STATUS AND VIOLENCE",
        "title": "When cognitive labor loses value: status games, service corps and violence risk",
        "lead": "Both speakers see mass job displacement arriving fast; they split on whether wealth-seeking survives (Tom: it must) and what gives people status.",
        "bullets": [
            "Timeline: Emad says job displacement is not visible yet because widely available AI isn't good enough or in the right format; next year it will be, making it the number one election topic 'next year and the year after'.",
            "Tom: cognitive labor will be done better by digital or physical AI in 10-20 years; Emad says sooner. Neither is impressed by proposed solutions so far.",
            "Tom's counter: a Kuwait trip showed state-provided jobs and safety nets stagnate a society; humans need goals and progress, and UBI that strips out wealth acquisition 'will fundamentally break something that will end in violence'. He uses Minecraft as 'the wealth acquisition loop'.",
            "Emad's answers: a **citizen service corps** (Roman citizenship-through-service; Starship Troopers; even 'dig a hole, fill a hole') for status; plus game-like digital worlds for acquiring assets, with an undisclosed project due in 'a couple of months'.",
            "He adds that war is no longer the old youth outlet (drones kill the average Russian soldier) and wants guilds and relative-status mechanics like early World of Warcraft.",
        ],
        "quote": {"text": "if we try to strip that out and say don't worry, everybody's just going to get UBI. You will fundamentally break something that will end in violence.", "cite": "— Tom Bilyeu"},
        "watch": "The two disagree explicitly: Emad says for most people there will be no more wealth accumulation or social mobility; Tom says 'I think you're crazy'. Unresolved in the transcript.",
        "names": None,
    },
    {
        "id": "debt-money",
        "tags": ["macro-rates", "finance", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "DEBT JUBILEE AND WHAT MONEY IS",
        "title": "Debt jubilee in a crisis, and why money survives anyway",
        "lead": "Emad says a debt jubilee historically follows crisis or world war and could come if cognitive labor is worth nothing; Tom says some currency always returns because scarce resources need allocating.",
        "bullets": [
            "Definition: governments periodically zero out debts when capital owners hold too much; historically after world wars, 'bloody' and violent, not a nice reset.",
            "Emad's scenario: cognitive labor gets negative value; humanoids do jobs better; countries embracing AI (China) see **~30% growth rates** at the expense of US growth. AI has none of the friction of outsourcing.",
            "He sees partial debt repudiation as plausible given non-dischargeable student loans and medical debt, and says that without new institutions the path is 'a very ugly one'.",
            "Tom: money is a record of doing something more valuable with your time; it has been beads, salt, rice. If AI caters to our wants, someone must decide who gets a scarce house; random allocation would cause revolution, so a currency re-emerges (even 'black market cigarettes').",
            "Emad agrees on scarcity but expects it won't be one economy: multiple tiers, as in sci-fi.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "two-tier-window",
        "tags": ["health", "biotech", "geopolitics"],
        "color": "gray",
        "badge": "Speculative",
        "status": "LONGEVITY, TWO TIERS AND A 2-YEAR WINDOW",
        "title": "Longevity for the rich, a possible serf society, and 'the sand pile collapses in two years'",
        "lead": "Emad predicts longevity escape velocity within 5-10 years and a society split by access to it; Tom counters that abundance in energy, intelligence and labor should prevent a permanent underclass.",
        "bullets": [
            "Emad: 'longevity escape velocity' (life expectancy rising faster than a year per year) arrives in **5-10 years**.",
            "Evidence he cites: an Insilico-style trial in idiopathic pulmonary fibrosis where four weeks of the drug reportedly reduced longevity markers by four years; GLP-1s showing large cancer reversal.",
            "His fear: the rich live longer and healthier while ladders are pulled up; labor can no longer be exchanged for capital; a food-stamp tier and a VIP tier.",
            "Tom's reply: with energy, intelligence and labor costs near zero, only hard-to-make things stay scarce; a permanent serf class would be rejected, especially with a super-persuader AI arguing it's unjust.",
            "Emad's menu of futures: serf society, Star Trek, Mad Max-style war, or mass 'turn Amish' opt-outs; plus questions of robot rights, brain chips and 200-year lives.",
            "Closing advice (about two years): be 'the last man standing', find ownership and entrepreneurship opportunities, and build stronger communities. The transcript cuts off mid-sentence here.",
            "He also argues China will go all-in on AI, may stop exporting robots to offset a low birth rate, and that America lags unless it embraces AI, which he says is why Trump is pro-superintelligence.",
        ],
        "quote": {"text": "it's a sand pile that will start collapsing I think in two years", "cite": "— Emad Mostaque"},
        "watch": "Longevity trial figures are stated from memory with a garbled company name in the caption; no source named. Emad also said some people will push to ban superintelligence, citing 'ban AI' bills.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9ED", "tag": "AI strategy", "title": "Separate AI you rent from AI you own: map which assistants hold your accounts and who profits from them."},
    {"icon": "\U0001F9E0", "tag": "Cognition", "title": "Use AI to understand a topic, never to get the answer, Tom's rule against cognitive atrophy."},
    {"icon": "\U0001F4BC", "tag": "Careers", "title": "Move toward ownership and entrepreneurship now; Emad's window for displacement is about two years."},
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Test the AI-valuation thesis: if intelligence prices fall ~1,000x, value shifts from access to the 'last mile'."},
    {"icon": "\U0001F3D8", "tag": "Community", "title": "Invest in local community and family networks as a self-sustaining hedge."},
    {"icon": "\U0001F5F3", "tag": "Policy", "title": "Expect AI job loss to dominate elections next year and the one after; watch ban-superintelligence bills and public-sector AI."},
]

HOT_TAKES = [
    {"take": "AI is now more persuasive than any human with the latest research already.", "cite": "— Emad Mostaque", "why": "strong claim vs top debaters"},
    {"take": "Eventually it's going to run policy. Eventually it's going to make medical decisions.", "cite": "— Emad Mostaque", "why": "improvement is capture"},
    {"take": "In the next 5 to 10 years they hit longevity escape velocity, meaning we live forever effectively.", "cite": "— Emad Mostaque", "why": "dated prediction"},
    {"take": "It's a sand pile that will start collapsing I think in two years.", "cite": "— Emad Mostaque", "why": "dated prediction"},
    {"take": "If we try to strip that out and say don't worry, everybody's just going to get UBI. You will fundamentally break something that will end in violence.", "cite": "— Tom Bilyeu", "why": "contrarian on UBI"},
    {"take": "The number one topic next year and the year after in elections will be AI and job displacement.", "cite": "— Emad Mostaque", "why": "dated prediction"},
]

CLAIMS = [
    {"who": "Emad Mostaque", "claim": "AI job displacement becomes the number one election topic in the next two years.", "metric": "election topic ranking", "target": "AI and job displacement #1", "by": "2028", "condition": None, "entity": None},
    {"who": "Emad Mostaque", "claim": "Longevity escape velocity is reached within 5-10 years.", "metric": "life expectancy growth", "target": "more than 1 year per year", "by": "5-10 years", "condition": None, "entity": None},
    {"who": "Emad Mostaque", "claim": "The societal 'sand pile' of AI-driven disruption starts collapsing in about two years.", "metric": None, "target": "societal disruption begins", "by": "2028", "condition": None, "entity": None},
    {"who": "Emad Mostaque", "claim": "The price of intelligence may drop about 1,000x.", "metric": "price of AI access", "target": "1,000x decline", "by": None, "condition": None, "entity": None},
    {"who": "Emad Mostaque", "claim": "AI-embracing countries such as China see about 30% growth rates.", "metric": "GDP growth", "target": "30%", "by": None, "condition": "if they embrace AI-run economies", "entity": "China"},
    {"who": "Tom Bilyeu / Emad Mostaque", "claim": "Digital or physical AI does cognitive-labor jobs better than humans within 10-20 years (Emad: sooner).", "metric": "cognitive labor", "target": "AI outperforms humans", "by": "10-20 years", "condition": None, "entity": None},
    {"who": "Emad Mostaque", "claim": "A game-like digital-asset project complementing Intelligent Internet is announced.", "metric": "product announcement", "target": "announced", "by": "2026-12", "condition": None, "entity": "Intelligent Internet"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources and references named: Emad's book *The Last Economy*; Asimov's *Foundation* (the Mule as super-persuader); Eliezer Yudkowsky's *If Anyone Builds It, Everyone Dies*; films Don't Look Up, Starship Troopers, Ready Player One; Minecraft and World of Warcraft as status/acquisition loops.", "tag": "References"},
    {"icon": "\U0001F6AB", "title": "Ban-superintelligence and ban-AI bills are 'coming out'; Emad notes adopters would still gain an edge over AI-embracing neighbors, and China is 'all in'.", "tag": "Policy"},
]

GLOSSARY = [
    {"term": "Cognitive colonialism", "def": "Emad's term for ceding control of a population's AI, and so its thinking, to outsiders."},
    {"term": "Longevity escape velocity", "def": "Point where life expectancy rises by more than one year per calendar year."},
    {"term": "Debt jubilee", "def": "A government wiping out debts, historically in crisis or war."},
    {"term": "Jevons paradox", "def": "Cheaper use of a resource can raise total consumption."},
    {"term": "Last mile of intelligence", "def": "Emad's name for where AI meets human reality, where he expects value to accrue."},
]
