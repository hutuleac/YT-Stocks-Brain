"""Data file for Valentin Dragu & Alex Marian (Grow Your Wealth) — SAPTAMANA CARE A SOCAT BURSELE!
Romanian-language video: brief in English, quotes and hot takes verbatim in Romanian (no diacritics)."""

META = {
    "title": "SAPTAMANA CARE A SOCAT BURSELE! (The Week That Shocked the Markets!)",
    "channel": "Grow your WEALTH - Valentin Dragu si Alex Marian",
    "speakers": "Valentin Dragu and Alex Marian (co-hosts)",
    "date": "2026-08-02",
    "video_url": "https://www.youtube.com/watch?v=nAuilj-6Gg8",
    "thread_line": "6 threads · US GDP slowdown and a Fed pause before the midterms, the human tragedy behind South Korea's KOSPI crash, Citadel's liquidation of Leopold Aschenbrenner's fund, Magnificent Seven earnings (strong Microsoft/Amazon, weak Apple and Meta), the 'total control' data-center theory, and the four big risks for the Bucharest Stock Exchange.",
    "category": "market",
    "region": "ro",
}

SNAPSHOT = [
    "US GDP slowed to 1.5% (from 2.1%) and PCE came in below expectations — the hosts read the combination as setting the stage for the Fed to signal no rate hikes before the midterm elections, a scenario they see as deliberately engineered.",
    "The FOMC held rates in the 3.50-3.75% band, with three members dissenting in favor of a hike; Kevin Warsh is described as extremely sparing with guidance, unlike his predecessor, leaving analysts without clear positioning signals.",
    "The episode's central and heaviest theme: the crash of South Korea's KOSPI, where Samsung and SK Hynix make up nearly 50% of the index — the hosts had repeatedly warned about this concentration risk and describe hundreds of thousands of retail investors losing their savings, with crisis hotlines activated after the wave of forced liquidations.",
    "Leopold Aschenbrenner's fund (a former OpenAI researcher) was effectively liquidated by Citadel/Ken Griffin, who bought its assets at about 30 cents on the dollar after a public statement that deepened the selloff — the assets rose 40-50% the very next day.",
    "Magnificent Seven earnings pointed in opposite directions: Microsoft (strong Azure, but reservations about its OpenAI tie) and Amazon (AWS a \"money machine\", possible $280-300 target) impressed; Apple (memory-driven price pressure, but it overtook Nvidia in market cap) and Meta (weak report, EPS miss) disappointed.",
    "The hosts speculate (explicitly flagged as personal opinion, not confirmed fact) that Big Tech's data centers could serve surveillance and national-security purposes beyond cloud and AI — citing an Amazon data center in England built for the British military.",
    "On Romania: four major risks for the Bucharest Stock Exchange (political, currency, country, regional), with a specific warning that nationalizing the Pillar II private pensions could crash the BVB twice as badly as the Seoul market.",
]

THEMES = [
    {
        "id": "gdp-fed-pauza",
        "tags": ["macro-rates"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCH — clear decision expected before the midterms",
        "title": "US GDP Slows, the Fed Prepares to Hold Off on Hikes Before the Midterms",
        "lead": "**The hosts read weak GDP plus below-forecast PCE as a framework deliberately built so the Fed can announce no rate hikes** — a scenario they say they anticipated since the start of the year.",
        "bullets": [
            "US GDP came in at 1.5% in the first Q2 estimate, down from 2.1% — \"not bad\" in itself, but the hosts distrust official statistics in any country.",
            "PCE (the Fed's preferred inflation gauge) also came in lower, lifting the market even before the GDP print — together read as a sign the Fed can't afford to hike without adding pressure to a slowing economy.",
            "The FOMC held rates in the 3.50-3.75% band, with three members dissenting for a hike — the hosts suggest (without being able to confirm) these members may be aligned with Citadel-linked interests.",
            "Kevin Warsh is described as far more reserved than his predecessor — he says pertinent things but gives no hint of future policy direction, leaving analysts without clear anchors.",
            "The hosts tie the whole sequence (problems created, then \"rescue solutions\") to a broader strategy led by Trump with Bessent (Treasury) and Warsh (Fed), with results clarifying closer to the midterms.",
        ],
        "quote": {"text": "Se creeaza o problema destul de grea, se creeaza o panica, o frica, pentru ca ulterior sa se vina cu o solutie pozitiva si lucrurile sa revina la normal.", "cite": "— Alex Marian"},
        "watch": "The hosts openly say they distrust official statistics and treat their reading as symbolic/political, not an economic certainty.",
        "names": None,
    },
    {
        "id": "kospi-tragedie",
        "tags": ["semis", "finance"],
        "color": "red",
        "badge": "Confirmed event, devastating impact",
        "status": "WATCH — a lesson for global investors",
        "title": "South Korea: the KOSPI Crash Becomes a Human Tragedy, Not Just a Market Correction",
        "lead": "**The hosts had warned repeatedly that the KOSPI was dangerously concentrated** (Samsung and SK Hynix make up nearly 50% of its weight) — and when the correction came, it brought mass forced liquidations and personal tragedies.",
        "bullets": [
            "Memory is cyclical by nature; when such a sector dominates an index and corrects, a 40-50% drop for the whole market becomes possible — exactly the scenario the hosts flagged beforehand.",
            "The South Korean government banned leveraged ETFs only after the crisis had already hit — the hosts call the measure late and useless at that point.",
            "Cited estimate: 3-5% of South Korea's population (potentially hundreds of thousands of people/families) were liquidated, some losing life savings and even homes; crisis hotlines and AI monitoring systems were set up to prevent suicides.",
            "SK Hynix as a specific example: after a weak report, the CEO chose to buy company shares in the middle of the turmoil instead of waiting a few days to calm the market — a company that, ironically, had recently also listed in the US, feeding the hype before the crash.",
            "The hosts tie it to human greed in general (\"the good is the enemy of the good\") — investors who, after big gains, added borrowed money and leveraged ETFs instead of locking in profits, repeating mistakes from past crashes (including Japan's).",
        ],
        "quote": {"text": "Ne apropiem de un moment in care cresterile nu sunt normale si vom avea o corectie.", "cite": "— Alex Marian"},
        "watch": "The hosts stress that South Koreans' general discipline didn't protect them from this specific market mistake — it's about market structure and greed, not national character.",
        "names": [
            {"name": "Samsung Electronics", "blurb": "With SK Hynix, nearly 50% of the KOSPI — sector concentration identified as the structural cause of major correction risk.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "SK Hynix", "blurb": "Weak report followed by an aggressive rebound; cited as a success story turned tragedy for South Korean retail investors.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "leopold-citadel",
        "tags": ["finance"],
        "color": "red",
        "badge": "Confirmed event, ethically contested",
        "status": "WATCH — market mechanism exposed, not necessarily fixed",
        "title": "Leopold Aschenbrenner's Fund 'Executed' by Ken Griffin and Citadel",
        "lead": "**A young former OpenAI researcher who grew a fund from a few hundred million to about $10 billion got caught overexposed on margin and leveraged products** — and Citadel, run by Ken Griffin, seized the moment.",
        "bullets": [
            "Ken Griffin made a public statement just as the market was falling hard and the Fed was meeting, arguing it was a good time to raise the policy rate — a statement that deepened declines in SK Hynix, SanDisk and other exposed names.",
            "Citadel also controls one of the largest market makers (Citadel Securities), giving it visibility into global investor positioning — the hosts read the combination of the public statement and the market-making activity as possibly coordinated.",
            "Griffin took over Aschenbrenner's fund assets at about 30 cents on the dollar (a ~70% discount) — the day after the deal, those assets were already worth 40-50% more.",
            "The hosts note Citadel Securities Hong Kong had trouble with the Korean regulator in 2023 over non-compliant practices and lost market-maker access in Korea — while they can't prove a direct link, they find it plausible Citadel also played a role in the Korean drop through other funds.",
            "Practical lesson for retail investors: you can't compete with players who see positioning data in real time — the only reasonable strategy is a long-term view, solid core positions and avoiding margin/leverage, rather than trying to anticipate their moves.",
        ],
        "quote": {"text": "Consider ca unul dintre actorii principali care a cauzat scaderea din South Korea este Citadel, chiar daca prin alte fonduri prin care are acces.", "cite": "— Valentin Dragu"},
        "watch": "The hosts openly admit they can't prove a direct link between Citadel and the South Korean drop — a motivated suspicion, not proof.",
        "names": None,
    },
    {
        "id": "mag7-earnings",
        "tags": ["ai-infra", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCH — diverging reactions within the group",
        "title": "Magnificent Seven: Microsoft and Amazon Shine on Cloud, Apple Passes Nvidia, Meta Disappoints",
        "lead": "**An earnings season with clearly different directions inside the group**: cloud (Azure, AWS) remains the profit engine, while Apple and Meta face specific problems.",
        "bullets": [
            "Microsoft reported well on Azure, but the positive reaction came in a market already rebounding hard — the hosts stay cautious about the Microsoft-OpenAI partnership (\"almost anything OpenAI touches is like a virus\"), preferring the Anthropic tie; Microsoft also announced a Revolut partnership giving some users free ChatGPT access.",
            "Amazon reported spectacularly on AWS (\"a money machine\"), with openly acknowledged very high capex — the hosts see a real chance the stock quickly reaches $280-300 if capex starts to ease.",
            "Apple had a weak report, with pressure on future phone prices from higher memory costs and a strategy unlike the rest of the group (buybacks, dividends, modest AI spend) — it still overtook Nvidia as the most valuable company by market cap, though the hosts see the roles possibly flipping back soon.",
            "Bloom Energy rebounded spectacularly (+40% in two days) after a good report tied to power-supply contracts for data centers — the hosts recommend neither buying nor selling, but say a 40% move in two days isn't healthy and raises correction risk for new buyers.",
            "Meta closed the list with the group's weakest report (EPS miss despite good revenue growth) — the hosts expect two to three more quarters of negative sentiment before a possible turnaround, comparing it to the earlier metaverse retreat.",
        ],
        "quote": {"text": "Amazon Web Services produce, este o masina de facut bani, ceea ce pune intr-o postura extrem de pozitiva evolutia pretului actiunii pe mai departe.", "cite": "— Valentin Dragu"},
        "watch": "The Bloom Energy view is explicitly neutral — the hosts decline to recommend buying or selling, flagging only the elevated risk of the recent move.",
        "names": [
            {"name": "Microsoft (MSFT)", "blurb": "Good Azure-driven report, but the hosts stay cautious about the OpenAI tie and don't expect a fast run to $500.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "AWS called a \"money machine\"; possible $280-300 target if capex eases.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Weak report, memory-driven phone price pressure, but overtook Nvidia in market cap.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Temporarily passed by Apple in market cap; the hosts see the roles possibly flipping back soon.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Meta (META)", "blurb": "Weakest Magnificent Seven report; negative sentiment expected to last two to three more quarters.", "stance": "NEGATIVE VIEW", "conviction": "High", "horizon": "2-3 quarters"},
            {"name": "Bloom Energy (BE)", "blurb": "+40% in two days after a good report on data-center power contracts — a move explicitly flagged as unhealthy/risky.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "OpenAI", "blurb": "Association viewed warily by the hosts (\"like a virus\"), unlike Anthropic.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "centre-date-control",
        "tags": ["ai-infra", "policy"],
        "color": "gray",
        "badge": "Speculative",
        "status": "PERSONAL OPINION — explicitly flagged as such",
        "title": "The 'Total Control' Data-Center Theory — Explicit Speculation, Not Confirmed Fact",
        "lead": "**The hosts advance a theory they openly admit may sound like a \"conspiracy\"**: that the data centers Big Tech is building could serve surveillance and national-security purposes beyond cloud and AI.",
        "bullets": [
            "The argument starts from a personal source (an acquaintance who worked at an Amazon data center in England built for the UK military and security sector) and from the observation that Meta gives very little detail about many of its facilities.",
            "The hosts note Meta, like other big tech firms, has historically had ties to the US security community — a known fact, not news, but used as further support for their theory.",
            "They tie the speculation to a broader pattern of projects hard to fully understand right now: Optimus (Tesla's humanoid robot), robotaxis and full self-driving, data-carrying Starlink satellites — all pieces of a bigger puzzle they find hard to decode.",
            "They openly acknowledge the tension in this kind of talk and connect it (without claiming a direct link) to separate discussions of expanded video surveillance, using South Korea's crisis hotlines and monitoring as an example of heavier surveillance being seen as \"normal.\"",
        ],
        "quote": {"text": "Consider ca toate aceste centre de date care sunt sustinute cu banii companiilor mari vor fi acele centre de date care vor fi folosite pentru noua paradigma... pentru un control total.", "cite": "— Valentin Dragu"},
        "watch": "The hosts apologize in advance and openly admit the theory may sound like a conspiracy — presented clearly as speculative personal opinion, not established fact.",
        "names": None,
    },
    {
        "id": "bvb-riscuri",
        "tags": ["policy", "finance", "romania"],
        "color": "red",
        "badge": "Flagged risk",
        "status": "WATCH — four risks identified, no BVB positions",
        "title": "Four Major Risks for the Bucharest Stock Exchange and the Specter of Pension Nationalization",
        "lead": "**The hosts neither hold nor recommend BVB exposure**, citing four specific structural risks and a concrete warning about a possible nationalization of the Pillar II private pensions.",
        "bullets": [
            "The four BVB risks: political risk (the biggest), currency risk (the leu-euro rate), country risk (a possible rating downgrade) and regional risk (an area where problems could escalate).",
            "The biggest single danger: if the Romanian government seriously discussed nationalizing Pillar II private pensions, the fund managers would be forced to sell heavily with too few buyers — a scenario that could crash the BVB twice as badly as Seoul, though the hosts stress they aren't saying it will happen, only weighing the risk.",
            "Ad-hoc technical analysis: the BVB chart overlaid on the KOSPI looks worryingly similar in the hosts' view, though they note a key structural difference — the BVB has none of the derivatives or leverage that amplified the Korean crash.",
            "Explicit personal motive: one host was exposed to the BVB in the past and exited after a government ordinance that left him better off, but notes many other retail investors were hurt by the same measure.",
            "Broader conclusion: Romania's small number of investors relative to its population means it can't repeat the Korean tragedy at the same scale, but the economic, political and real-estate situation is \"not exactly good\" short term, with hope for improvement over the next two years.",
        ],
        "quote": {"text": "In acel moment, bursa de la Bucuresti va ajunge de doua ori mai rau decat bursa de la Seul din Coreea.", "cite": "— Valentin Dragu"},
        "watch": "The hosts are explicit that pension nationalization is a risk they're weighing, not an announced or confirmed event.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Check an index's sector concentration (like the KOSPI with Samsung/SK Hynix) before treating it as diversified."},
    {"icon": "\U0001F3E6", "tag": "Macro", "title": "Read GDP and PCE together, not just Fed statements, to anticipate rate pauses before major political events."},
    {"icon": "⚠️", "tag": "Markets", "title": "Avoid margin and high-leverage products, especially in volatility deliberately driven by large institutional players."},
    {"icon": "☁️", "tag": "AI infra", "title": "Separate cloud-division performance (Azure, AWS) from the rest of the business when reading a Magnificent Seven report — that's where the real profit engine shows."},
    {"icon": "\U0001F1F7\U0001F1F4", "tag": "Romania", "title": "Monitor talk about Pillar II private pensions as a political-risk signal for the BVB, beyond routine economic news."},
]

CLAIMS = [
    {"who": "Valentin Dragu / Alex Marian", "claim": "The Fed won't raise rates before the midterm elections.", "metric": "number of rate hikes", "target": "zero hikes", "by": "2026-10", "condition": "based on the framing of the recent GDP/PCE figures", "entity": None},
    {"who": "Valentin Dragu / Alex Marian", "claim": "Amazon stock can quickly reach a higher target.", "metric": "price target", "target": "$280-300", "by": None, "condition": "if capital expenditure eases slightly", "entity": "Amazon (AMZN)"},
    {"who": "Valentin Dragu / Alex Marian", "claim": "The KOSPI risks a further major correction if the memory sector corrects.", "metric": "further downside potential", "target": "40-50%", "by": None, "condition": "given Samsung+SK Hynix at nearly 50% of the index", "entity": None},
    {"who": "Valentin Dragu", "claim": "A nationalization of Pillar II pensions would crash the BVB worse than the KOSPI.", "metric": "relative severity of a possible correction", "target": "twice as bad as the Seoul market", "by": None, "condition": "hypothetical scenario, explicitly unconfirmed", "entity": None},
]

RELATIONS = [
    {"from": "Citadel Securities", "rel": "acquires", "to": "Leopold Aschenbrenner's fund", "note": "Assets taken over at about 30 cents on the dollar after a forced liquidation, following a public statement by Ken Griffin"},
    {"from": "Amazon (AMZN)", "rel": "owns_stake", "to": "Anthropic", "note": "Holds Anthropic shares, cited by the hosts as a reason for more trust than the OpenAI tie"},
    {"from": "Microsoft (MSFT)", "rel": "partners_with", "to": "OpenAI", "note": "Partnership mentioned with explicit reservations by the hosts"},
]

HOT_TAKES = [
    {"take": "Cam tot ceea ce atinge OpenAI este ca un virus. Nu prea este bine sa te asociezi cu numele OpenAI.", "cite": "— Alex Marian", "why": "Firm negative stance on a Microsoft business partner, said by name."},
    {"take": "Consider ca unul dintre actorii principali care a cauzat scaderea din South Korea este Citadel, chiar daca prin alte fonduri prin care are acces.", "cite": "— Valentin Dragu", "why": "Specific accusation against a major market player, admitted to be unprovable."},
    {"take": "Consider ca toate aceste centre de date vor fi folosite pentru noua paradigma in care va trai societatea, pentru un control total.", "cite": "— Valentin Dragu", "why": "Speculative personal theory the host admits may sound like a conspiracy, but holds anyway."},
    {"take": "In momentul in care ai facut foarte multi bani deja, poate ar fi bine sa marchezi profitul si sa securizezi acei bani.", "cite": "— Alex Marian", "why": "Direct advice against greed, applied to Korean investors who didn't lock in gains."},
    {"take": "Arata a Cospi. BVB-ul arata a Cospi din Coreea.", "cite": "— Alex Marian", "why": "Worrying technical comparison between the Romanian market and an index that just crashed."},
]

OTHER_NEWS = [
    {"icon": "\U0001F4F1", "title": "Microsoft and OpenAI announced a partnership with Revolut giving some Revolut users free ChatGPT access for a period (possibly a year).", "tag": "Product partnership"},
    {"icon": "\U0001F30D", "title": "A tangent on migration waves in Spain and Italy and the related political tensions (mentioning Italy's new general, seen as firm against illegal immigration, unlike Spain's socialist government) — tied by the hosts to a broader discussion of surveillance and social control.", "tag": "Discussion"},
]

GLOSSARY = [
    {"term": "Leveraged ETF", "def": "An exchange-traded fund that multiplies (usually 2x or 3x) the daily move of an underlying asset or index — amplifying both gains and losses, and a major factor in the South Korean crash."},
    {"term": "Market maker", "def": "A firm that provides liquidity by constantly buying and selling shares, earning the spread on very large volumes — Citadel Securities is one of the largest globally."},
    {"term": "Pillar II private pensions", "def": "The mandatory, privately managed part of Romania's pension system, funded from part of employees' social contributions — nationalization would mean moving these assets to the state budget."},
    {"term": "BVB", "def": "Bursa de Valori Bucuresti, the Bucharest Stock Exchange."},
    {"term": "Capex (capital expenditure)", "def": "A company's spending on infrastructure (data centers, equipment) — mentioned repeatedly in the context of the Magnificent Seven's huge AI and cloud spend."},
]
