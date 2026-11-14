META = {
    "title": "14.11.2026 Nvidia nu mai vinde doar cipuri, ea finanteaza jumatate din industrie...",
    "channel": "GrowYourWealth",
    "speakers": "GrowYourWealth",
    "date": "2026-11-14",
    "video_url": "",
    "thread_line": "6 threads · the one-day rotation · Nvidia as the AI industry's lender · AMD and Broadcom stances · neoclouds as Nvidia's dependants · 10-year at 5.15% · portfolio levels into 17 November",
    "category": "market",
    "region": "ro",
}

SNAPSHOT = [
    "Source note: built from GrowYourWealth's pasted written note of 14 November (no video), so figures are as the author states them.",
    "The indexes had their first green week after four red ones (S&P 500 +2.5%), but Friday hit his positions: AMD **-8.75%**, Nebius -9.92%, semis -3.4%.",
    "The rotation out of Nvidia into AMD and Broadcom after Huang's resignation lasted one session; Nebius and IREN fell harder than Nvidia itself.",
    "His core point: Nvidia was also the AI industry's lender, with ~**$530B** of commitments and guarantees (WSJ, filings), and that funding channel overpowered the substitution trade.",
    "No buying before Nvidia reports on **17 November**; read the guarantee policy before the revenue line.",
    "Macro tightened too: October PPI at 6.5% year on year (highest since November 2022), the 10-year at ~5.15%, and markets price ~85% odds of a December hike.",
    "He holds his AI names, adds nothing, and keeps cash; the one exception is SpaceX below $130.",
]

THEMES = [
    {
        "id": "one-day-rotation",
        "tags": ["semis", "ai-infra"],
        "color": "red",
        "badge": "Confirmed risk",
        "status": "CONFIRMED — ROTATION FADED IN ONE SESSION",
        "title": "The Nvidia-to-AMD/Broadcom rotation lasted exactly one day",
        "lead": "The market assumed money leaving Nvidia would land in AMD and Broadcom; prices show it reversed the next day, and the neoclouds got none of it.",
        "bullets": [
            "Since the resignation: NVDA -6.26% (to $162.85, -12.75% on the week), AMD -3.41%, AVGO **+0.52%**, NBIS -25.09%, IREN -12.81%, SOXX -3.93%.",
            "Thursday AMD +5.86% and AVGO +5.54%; Friday they gave it all back, and AMD closed under its pre-resignation $552.90.",
            "AMD's ~19% weekly gain came Monday to Wednesday on the post-election rebound and CoreWeave results, not on Huang leaving; SOX rose 10.6% in four days then lost 3.6% Friday (MarketWatch).",
            "Flows don't confirm it either: SOXX took in nearly $4B in one day on 11 November (ETF.com), before the resignation; he found no verified data for 12-13 November.",
            "Breadth on Friday: 58% of 5,078 stocks fell, tech -1.42%, consumer staples +1.44%. He calls it a rotation into defensives, not a flight from the market.",
        ],
        "quote": {"text": "Avem o saptamana in care piata a schimbat subiectul din mers, iar noi am aflat asta ultimii.", "cite": "— GrowYourWealth"},
        "watch": None,
        "names": [
            {"name": "SOXX", "blurb": "Semis ETF: +9.35% on the week but -3.93% since the resignation.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "nvidia-lender",
        "tags": ["semis", "finance"],
        "color": "red",
        "badge": "Confirmed risk",
        "status": "WATCH — NVIDIA GUARANTEE POLICY ON 17 NOV",
        "title": "Nvidia as the AI industry's central bank: investor, guarantor, supplier and buyer of last resort",
        "lead": "Per the WSJ, Nvidia guaranteed financing for customers that couldn't afford its GPUs, so the money leaves Nvidia and comes back as revenue. A tighter tap slows the whole capex cycle.",
        "bullets": [
            "Commitments and guarantees reached ~**$530B**, from $184B a quarter earlier (Yahoo Finance count). Q2 filings: $279B for memory and wafers (from $119B), up to $105B guarantee for OpenAI's Ohio site, $36B to buy unused neocloud capacity, against $91B of on-balance-sheet debt.",
            "WSJ: some deals were pushed by Huang's son-in-law Nico Caprez (VP since January), whose team promised small clouds credit support within weeks. CFO **Colette Kress** questioned how guarantees were priced and cut the OpenAI Ohio guarantee from $250B to $105B; Huang reportedly told her she looked like a deer in headlights.",
            "Kress, the CFO who questioned the deals, now runs the company. Huang himself reportedly warned that hyperscalers were building their own chips while component commitments piled up like an avalanche.",
            "CoreWeave example: Nvidia owns a stake, sells it chips and agreed to buy up to **$6.3B** of unused capacity through 2032. OpenAI: guarantee plus all the chips plus a $1.5B investment in the builder.",
            "Cracks: Nvidia reportedly paused some financing in August; nearly half of the $80B of data-center bonds issued this year rated junk; CoreWeave five-year CDS above 1,000 bp (CNBC); OpenAI reportedly raised less than planned at a lower valuation.",
            "His verification split: the $279B (10-Q, $366B total future commitments), $105B (staged, not a current loss) and $36B (capacity resellable) are in filings. The $530B mixes unlike obligations and is not a loss figure; the Huang-Kress account is press reporting, not proven fraud.",
            "Goldman Sachs (James Schneider) expects existing commitments honoured but new multi-party deals at this scale to be harder.",
        ],
        "quote": {"text": "Nvidia este simultan investitor, garant al finantarii, furnizor si client de rezerva in cadrul aceleiasi tranzactii.", "cite": "— GrowYourWealth"},
        "watch": "The WSJ account of internal disputes and the son-in-law's role is press reporting; the author flags it himself as unproven governance allegations.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Off-balance-sheet guarantees nearly 6x on-balance-sheet debt; reports 17 November with ~$109B consensus.", "stance": "UNCERTAIN", "conviction": "Medium", "horizon": "17 November report"},
            {"name": "CoreWeave (CRWV)", "blurb": "Nvidia-backed neocloud; CDS above 1,000 bp, down ~17% at lows this week.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "OpenAI", "blurb": "Up to $105B Nvidia guarantee for Ohio; reportedly raised less at a lower valuation.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Goldman Sachs (GS)", "blurb": "Schneider: harder for Nvidia to strike new multi-party deals.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "amd-broadcom",
        "tags": ["semis"],
        "color": "green",
        "badge": "Owns",
        "status": "HOLD — NO ADDS BEFORE 17 NOV",
        "title": "AMD: constructive, not adding. Broadcom: the best risk-reward in the group",
        "lead": "Substitution away from Nvidia is real but slow, measured in quarters; he expects to see it in numbers only in 2027.",
        "bullets": [
            "He recalls calling in 2025 that AMD would beat Nvidia from $170-180 and rotating losers like CleanSpark into it; he added Broadcom aggressively in the last month.",
            "AMD Q3: revenue $13.4B (+45%), data center **$8.5B** (+97%) on MI450; Q4 guide ~$17B ±3%. Anthropic, Meta, Microsoft, OpenAI and Oracle run on early Helios racks; the 6 GW OpenAI deal starts with 1 GW of MI450 at end-2026.",
            "Why no adds to AMD: up from its ~$188 52-week low, highest beta of his chip names, Northland flags rising inventory days, and China export curbs could force Nvidia to dump GPU stock. Wedbush target $600, average $657 (CNBC/FactSet).",
            "Broadcom: AI semis $16.7B in Q3 (**+221%**), Q4 guide $21.7B; Hock Tan sees supply for ~$115B in FY2027 and visibility to $230B in 2028. Custom XPUs for Google, Meta, OpenAI and Anthropic plus Tomahawk 6 Ethernet; Evercore: a weaker Nvidia favours Ethernet.",
            "Broadcom risk: Rothschild cut it to Neutral (target $398.47) on OpenAI/Anthropic dependence, tighter AI funding and Google designing more in-house; average target ~$526, the stock flat on the year.",
        ],
        "quote": {"text": "Substitutia este reala, dar eu cred ca o vom vedea in cifre abia in 2027.", "cite": "— GrowYourWealth"},
        "watch": None,
        "names": [
            {"name": "AMD (AMD)", "blurb": "Large holding; constructive but not adding before 17 November.", "stance": "OWNS", "conviction": "High", "horizon": "2027"},
            {"name": "Broadcom (AVGO)", "blurb": "Added aggressively last month; best risk-reward in the group.", "stance": "OWNS", "conviction": "High", "horizon": "FY2027-2028"},
            {"name": "CleanSpark (CLSK)", "blurb": "Losing position he was willing to rotate into AMD in 2025.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "neoclouds",
        "tags": ["ai-infra", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCH — FUNDING WITHOUT NVIDIA",
        "title": "Nebius and IREN are Nvidia's customers, not its competitors",
        "lead": "For the neoclouds the Nvidia crisis is mainly a risk: GPUs are the collateral for their debt, so fears of Nvidia dumping inventory raise everyone's cost of credit.",
        "bullets": [
            "Nebius: in March Nvidia paid $2B for a pre-funded warrant on 21.07M shares (**$94.94**/share, ~8.3%, 6-K); at $115.88 Nvidia is still in profit. The real exposure is priority Rubin/Vera access and lender credibility.",
            "Nebius says 75-85% of its $40-45B 2027 capex is covered by prepayments and asset-backed financing on Microsoft and Meta contracts (Reuters), so the hyperscaler is the main guarantor. It did cut 2026 guidance to $3.0-3.2B on third-party capacity delays; Q3 revenue ~$980.8M beat.",
            "IREN: Nvidia is a customer ($3.4B over five years, ~$0.7B a year) and holds a right to buy 30M shares at $70, ~74% out of the money at $18.17. The $9.7B Microsoft deal uses GB300s bought via Dell with 20% prepaid.",
            "IREN risks: a more cautious Nvidia under new leadership, GPU financing costs with $6B of FY2027 capex still only targeted, and the January deadline for $4B+ contracted ARR.",
            "He holds both for hyperscaler contracts, land and power, not for Nvidia's trouble, and won't add until there's evidence of funding that doesn't depend on Nvidia.",
        ],
        "quote": {"text": "Un investitor care vinde NVDA nu are absolut niciun motiv sa cumpere clientul ei.", "cite": "— GrowYourWealth"},
        "watch": None,
        "names": [
            {"name": "Nebius (NBIS)", "blurb": "Held; -25% since the resignation; 2027 capex mostly backed by Microsoft/Meta contracts.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "IREN (IREN)", "blurb": "Held; Nvidia is a customer; January ARR deadline.", "stance": "OWNS", "conviction": "Medium", "horizon": "January 2027"},
            {"name": "Microsoft (MSFT)", "blurb": "Anchor customer behind Nebius and IREN contracts.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Dell (DELL)", "blurb": "Supplies the GB300s for IREN's Microsoft contract.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "rates-macro",
        "tags": ["macro-rates"],
        "color": "red",
        "badge": "Confirmed risk",
        "status": "WATCH — DECEMBER FED HIKE ODDS",
        "title": "The 10-year at 5.15%: the second front for long-duration AI builders",
        "lead": "A higher benchmark rate raises funding costs and hurts companies whose profits sit in the future (Oracle, Nebius, IREN), even while demand grows.",
        "bullets": [
            "October PPI (BLS, 13 November): +0.3% m/m, **+6.5% y/y** (highest since November 2022), services +0.2%, final-demand goods +0.5%.",
            "Derivatives price ~85% odds of a 25 bp December hike and ~15% of 50 bp.",
            "US 10-year ~5.15% (+29 bp on the week), 2-year ~4.87% (+35 bp), VIX futures 19.11, Nvidia 2031 bond yield 5.717%.",
            "Brent ~$95.84 and WTI ~$88.56, down a second week from high levels; the dollar hit a 19-month high, which shifts euro and lei returns for European holders.",
        ],
        "quote": {"text": "Cash-ul nu mai este o pierdere, este o arma.", "cite": "— GrowYourWealth"},
        "watch": None,
        "names": None,
    },
    {
        "id": "portfolio-levels",
        "tags": ["ai-infra", "space"],
        "color": "blue",
        "badge": "Developing",
        "status": "PLAN — HOLD, CASH, WAIT FOR 17 NOV",
        "title": "Portfolio roll call and the levels he's watching",
        "lead": "He protects capital: no new buys except SpaceX below $130, cash kept, balance sheets checked.",
        "bullets": [
            "SpaceX $139.11 (-0.59%), ~$1.89T market cap, held up well. Oracle $125.35, TTM revenue ~$71.78B, P/E ~19.7, watched on OCI growth, contracts turned into cash, capex and its financing. Vertiv **$202.07** (-3.61%) on a $196-214.49 range. Ondas $5.16 (-3.01%) on margins and losses.",
            "Others in brief: Tesla (autonomy, robotics, energy), Meta (ad cash funds AI), Palantir (growth vs valuation), SoFi and Robinhood hurt as Bitcoin fell under $70,000, Rocket Lab, AST SpaceMobile (-5.5% Friday, Barron's), Centrus Energy (nuclear fuel).",
            "Levels: Broadcom above $330 (12 Nov high $369.82), AMD vs $552.90, Nebius vs $94.94 and $109, IREN vs its $17.16 52-week low, S&P 500 7,561.67-7,592.40, Nasdaq 25,136.27-25,366.09, ORCL $121.76-128 (Wednesday high $130.77), VRT $196-214.49, ONDS $5.02-5.33.",
            "Credit is the thermometer: the Nvidia 2031 bond yield and CoreWeave CDS. He also watches Congress hearings and the text of export restrictions.",
            "Scenarios (4-8 weeks). Base: Nvidia in line, honours existing commitments with no new ones, AMD/AVGO stabilise, neoclouds stay pressured. Bull: a credible CEO fast (press says the board approached Arm's Rene Haas, unconfirmed) plus a strong Anthropic IPO lifts everything. Bear: guarantee cuts, Congress revelations or hard export curbs, and the neoclouds may need dilutive equity.",
        ],
        "quote": {"text": "Noi nu trebuie sa castigam fiecare sedinta bursiera.", "cite": "— GrowYourWealth"},
        "watch": "These are his own holdings, so every stance here is a disclosed position.",
        "names": [
            {"name": "SpaceX (SPCX)", "blurb": "Held; the only stock he'd buy now, below $130.", "stance": "BUYING-ADDING", "conviction": "Medium", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "Held; cheap-looking P/E means little if capex eats free cash flow.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Vertiv (VRT)", "blurb": "Held; structural power and cooling demand, sensitive to capex delays.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Ondas (ONDS)", "blurb": "Held; revenue and orders accelerating, margins in focus.", "stance": "OWNS", "conviction": "Low", "horizon": None},
            {"name": "Tesla (TSLA)", "blurb": "Held; autonomy, robotics, energy.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "Meta (META)", "blurb": "Held; ad cash funds AI.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "Palantir (PLTR)", "blurb": "Held; judged on growth, margins, valuation.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "SoFi (SOFI)", "blurb": "Held; rate- and risk-appetite sensitive.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "Robinhood (HOOD)", "blurb": "Held; hit by Bitcoin under $70k.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "Rocket Lab (RKLB)", "blurb": "Held; space exposure.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "AST SpaceMobile (ASTS)", "blurb": "Held; -5.5% Friday.", "stance": "OWNS", "conviction": "None", "horizon": None},
            {"name": "Centrus Energy (LEU)", "blurb": "Held; nuclear fuel supply chain.", "stance": "OWNS", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C4", "tag": "Markets", "title": "On 17 November read Nvidia's guarantee and ecosystem-investment language before the revenue line."},
    {"icon": "\U0001F6AB", "tag": "Markets", "title": "Don't chase one-day chip rallies or buy neoclouds just because they fell most."},
    {"icon": "\U0001F50D", "tag": "Analysis", "title": "Screen AI names on who funds the growth: free cash flow, debt, commitments and real utilisation."},
    {"icon": "\U0001F321️", "tag": "Credit", "title": "Track the Nvidia 2031 bond yield and CoreWeave CDS as the real temperature of neocloud funding."},
    {"icon": "\U0001F4B5", "tag": "Macro", "title": "Hold cash while the 10-year sits near 5.15%; it's optionality, not a drag."},
]

HOT_TAKES = [
    {"take": "Rotatia a durat o singura sedinta.", "cite": "— GrowYourWealth", "why": "Against the market's Nvidia-to-AMD rotation story."},
    {"take": "Nvidia a fost banca centrala a AI-ului.", "cite": "— GrowYourWealth", "why": "Reframes Nvidia's risk as a funding risk for the whole sector."},
    {"take": "Un investitor care vinde NVDA nu are absolut niciun motiv sa cumpere clientul ei.", "cite": "— GrowYourWealth", "why": "Dismisses the neocloud-benefits trade."},
    {"take": "Substitutia este reala, dar eu cred ca o vom vedea in cifre abia in 2027.", "cite": "— GrowYourWealth", "why": "Dated call on AMD/Broadcom share gains."},
]

CLAIMS = [
    {"who": "GrowYourWealth", "claim": "Nvidia reports on 17 November with a ~$109B revenue consensus; the guarantee policy decides whether the AI complex breathes.", "metric": "Nvidia quarterly revenue", "target": "~$109B consensus", "by": "2026-11-17", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "GrowYourWealth", "claim": "Substitution away from Nvidia shows in AMD and Broadcom numbers only in 2027.", "metric": "share gains vs Nvidia", "target": "visible in results", "by": "2027", "condition": None, "entity": "AMD (AMD)"},
    {"who": "GrowYourWealth", "claim": "Base case for 4-8 weeks: Nvidia reports in line and honours existing commitments without new ones; AMD and Broadcom stabilise; Nebius and IREN stay under pressure.", "metric": "Nvidia new guarantees", "target": "none", "by": "4-8 weeks", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "GrowYourWealth", "claim": "Nebius and IREN stay under pressure until there's evidence of financing that doesn't depend on Nvidia.", "metric": "neocloud share prices", "target": "under pressure", "by": "4-8 weeks", "condition": "until non-Nvidia funding is shown", "entity": "Nebius (NBIS)"},
    {"who": "GrowYourWealth", "claim": "He would buy SpaceX only below $130.", "metric": "buy level", "target": "<$130", "by": None, "condition": "if it drops below $130", "entity": "SpaceX (SPCX)"},
    {"who": "GrowYourWealth", "claim": "Broadcom's rotation is over if the stock falls below $330.", "metric": "AVGO level", "target": "$330", "by": None, "condition": None, "entity": "Broadcom (AVGO)"},
    {"who": "Hock Tan (cited by GrowYourWealth)", "claim": "Broadcom AI semis revenue roughly doubles to ~$115B in FY2027, with visibility to $230B in 2028.", "metric": "Broadcom AI revenue", "target": "$115B / $230B", "by": "2028", "condition": None, "entity": "Broadcom (AVGO)"},
    {"who": "GrowYourWealth", "claim": "Markets price ~85% odds of a 25 bp Fed hike in December and ~15% of 50 bp.", "metric": "Fed hike", "target": "25 bp (85%)", "by": "2026-12", "condition": None, "entity": None},
    {"who": "GrowYourWealth", "claim": "IREN faces a January deadline for $4B+ of contracted ARR.", "metric": "contracted ARR", "target": ">$4B", "by": "2027-01", "condition": None, "entity": "IREN (IREN)"},
]

RELATIONS = [
    {"from": "Nvidia (NVDA)", "rel": "owns_stake", "to": "CoreWeave (CRWV)", "note": "also sells it chips and backstops up to $6.3B of unused capacity to 2032"},
    {"from": "Nvidia (NVDA)", "rel": "owns_stake", "to": "Nebius (NBIS)", "note": "$2B pre-funded warrant, ~8.3% at $94.94"},
    {"from": "Nvidia (NVDA)", "rel": "customer_of", "to": "IREN (IREN)", "note": "$3.4B over five years plus a 30M-share right at $70"},
    {"from": "Nvidia (NVDA)", "rel": "supplies", "to": "OpenAI", "note": "all chips for Ohio plus up to $105B guarantee and $1.5B in the builder"},
    {"from": "Microsoft (MSFT)", "rel": "customer_of", "to": "IREN (IREN)", "note": "$9.7B contract on GB300s via Dell"},
    {"from": "Dell (DELL)", "rel": "supplies", "to": "IREN (IREN)", "note": "GB300 GPUs, 20% prepaid"},
    {"from": "Broadcom (AVGO)", "rel": "supplies", "to": "Anthropic (ANT)", "note": "custom XPUs; Anthropic is its future biggest XPU customer"},
    {"from": "AMD (AMD)", "rel": "supplies", "to": "OpenAI", "note": "6 GW deal, first 1 GW of MI450 at end-2026"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4F0", "title": "Sources cited: Wall Street Journal, MarketWatch, CNBC, Yahoo Finance, ETF.com, Reuters, Barron's, FactSet, BLS, Nvidia 10-Q and Nebius 6-K filings, plus analysts at Goldman Sachs, Wedbush, Northland, Evercore and Rothschild.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Neocloud", "def": "GPU cloud providers such as CoreWeave, Nebius and IREN that rent AI compute, largely debt-financed."},
    {"term": "Off-balance-sheet guarantee", "def": "A promise to pay if a customer defaults or capacity goes unused; it costs money only when triggered."},
    {"term": "CDS", "def": "Credit default swap, the price of insuring a company's debt against default; above 1,000 bp signals stress."},
    {"term": "Pre-funded warrant", "def": "A right to shares paid almost entirely up front, as Nvidia did for its Nebius stake."},
    {"term": "XPU", "def": "Broadcom's custom AI accelerators designed for a specific customer such as Google or Anthropic."},
    {"term": "PPI", "def": "Producer Price Index, US wholesale inflation published by the BLS."},
]
