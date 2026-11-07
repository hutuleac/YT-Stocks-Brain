"""Grow your WEALTH weekly video, 2026-11-07. Romanian auto-captions: brief in English, quotes verbatim Romanian without diacritics."""
META = {
    "title": "Membrii GYW",
    "channel": "Grow your WEALTH - Valentin Dragu si Alex Marian",
    "speakers": "Valentin Dragu, Alex Marian",
    "date": "2026-11-07",
    "video_url": "https://www.youtube.com/watch?v=mwWRC2GVAaQ",
    "thread_line": "5 threads · post-election selloff and fund liquidations · tech earnings triage · Anthropic IPO as AI bellwether · Paraguay bank and the reset thesis · Romania's pension-fund-driven bourse",
    "category": "market",
    "region": "ro",
}

SNAPSHOT = [
    "Filmed Friday after a brutal Thursday in which the US market lost about **$2 trillion**; the hosts call it a buying opportunity and expect a rebound.",
    "Valentin Dragu reads the US midterms as **Trump's loss, not the Republicans'**: the Iran war pushed up fuel and food prices, and Texas flipped entirely.",
    "Split power (Republican president, Democratic Congress) is framed as good for markets; Trump's statements should now move prices less.",
    "Earnings triage: Supermicro and ARM worth a look after the drop; Shopify overvalued; Qualcomm and Intel avoid; Apple's buyback keeps it resilient.",
    "Market gossip: Leopold's fund and about **six other funds** may have been liquidated in the selloff; 13F filings will tell.",
    "A troubled Paraguayan bank (**60%** of citizens cut off from funds) is read as a possible test run for a financial reset Dragu places around 2032.",
    "Anthropic's IPO is the AI bellwether: success means a **$1.6-2 trillion** market cap and a lift for semis, memory, AI infra and data-centre energy.",
    "Romania's BVB is decoupled from the economy: Pillar 2 pension funds keep buying scarce shares; nationalisation of those funds is the tail risk.",
]

THEMES = [
    {
        "id": "selloff",
        "tags": ["finance", "macro-rates", "policy"],
        "color": "green",
        "badge": "Buy the dip",
        "status": "THURSDAY SELLOFF · FILMED FRIDAY",
        "title": "A forced-selling Thursday, read as an outsized buying opportunity",
        "lead": "The hosts treat the $2T wipeout as mechanical liquidation, not a broken market, and expect a strong rebound.",
        "bullets": [
            "Market lost about $2 trillion on Thursday; stop-losses and margin calls fired simultaneously in a very short window.",
            "Rumour: **Leopold**'s fund was liquidated (positions in SanDisk, Micron, CoreWeave and Nebius all down over 40%); Dragu thinks six more funds went too.",
            "Funds with a few billion under management are small vs. total AUM but large for a single moment of simultaneous selling.",
            "Red lines: trouble at JPMorgan, Goldman Sachs, Morgan Stanley, Bank of America, State Street or Citadel would mean deeper damage to market structure.",
            "History: markets rise about 80% of the time; Dragu calls Thursday \"o oportunitate iesita din comun\".",
            "UK raised rates for the first time since 2023; Dragu sees a one-off move to align with the ECB, BoJ and Fed after Jackson Hole, not domestic inflation pressure.",
        ],
        "quote": {"text": "A fost o vanzare masiva. Au fost curatati foarte multi investitori.", "cite": "— Valentin Dragu"},
        "watch": "The fund liquidations are the hosts' own read of price action; they say 13F filings will confirm or deny. The channel is sponsored by XTB.",
        "names": [
            {"name": "JPMorgan (JPM)", "blurb": "Named as a systemic red line; Democrats reportedly want an investigation.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Citadel", "blurb": "Market maker that must not show stress.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "midterms",
        "tags": ["geopolitics", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "US MIDTERMS · NOVEMBER 2026",
        "title": "Trump lost the midterms for the Republicans, and the Iran war did it",
        "lead": "Fuel and food price spikes from the Iran war turned voters against Trump; divided government should calm markets.",
        "bullets": [
            "Republicans lost everything in Texas (governor, both Senate seats, House); fuel is a big share of a Texan's budget.",
            "Alex Marian suggests Democrats could hold power for **eight years**.",
            "Split power forces negotiation via the presidential veto; one-colour control is \"the worst\" for markets.",
            "Trump's \"ping-pong\" statements on Iran helped insiders with early access but hurt most investors; they should now carry less weight.",
            "Dragu expects Nancy Pelosi to trade more aggressively with Democrats in power, and says to follow her moves.",
            "Iran conflict may restart before the new Congress sits in January; Israel-Palestine \"will never\" calm, per Dragu.",
        ],
        "quote": {"text": "Din punctul meu de vedere, Trump a pierdut alegerile pentru republicani.", "cite": "— Valentin Dragu"},
        "watch": None,
        "names": None,
    },
    {
        "id": "earnings",
        "tags": ["semis", "consumer"],
        "color": "amber",
        "badge": "Mixed",
        "status": "EARNINGS WEEK",
        "title": "Earnings triage: Supermicro and ARM yes, Shopify, Qualcomm and Intel no",
        "lead": "Price paid matters more than business quality; Dragu separates fundamentals-driven names from hype-driven ones.",
        "bullets": [
            "Apple: weak-ish report, higher memory costs could lift iPhone prices; buyback and no aggressive AI capex protect it. Hosts admit a poor track record calling its correction.",
            "Shopify: decent report, slight revenue miss, after a run to about $172-180; overvalued and high-beta, only for aggressive investors after more correction.",
            "Supermicro beat strongly; Dragu shifts view to positive and expects a rebound, though not adding it to portfolio or analysis.",
            "Intel fell about 30% on earnings to about $55.6; rally was hope on US-government protection. Sees $70-80, not $120; foundry contracts (SpaceX, likely Tesla) are the later catalyst.",
            "Intel's CEO buying shares is called a strong signal; the bounce is still \"pur tehnic\".",
            "ARM: about 90% owned by SoftBank, only ~10% floats, so moves are extreme; Masayoshi Son pledged shares to fund OpenAI but says he won't repeat his Nvidia mistake.",
            "Lesson recalled: after a 30% one-day drop they exited Trade Desk for good; Tesla shows years of chop when price front-runs promises.",
        ],
        "quote": {"text": "Contează foarte mult la ce pret o cumparam.", "cite": "— Valentin Dragu"},
        "watch": "Dragu also opened an undisclosed new position in a stock that reported well and fell Thursday, in a portfolio he aims to grow through end-2028.",
        "names": [
            {"name": "Supermicro (SMCI)", "blurb": "Strong beat; view upgraded, rebound expected.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "near term"},
            {"name": "ARM (ARM)", "blurb": "Thin float, buyable after correction.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Buyback keeps it resilient; memory costs transitory.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Shopify (SHOP)", "blurb": "Overvalued, high beta.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Qualcomm (QCOM)", "blurb": "Avoid despite SpaceX contracts.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Intel (INTC)", "blurb": "Hype-driven; technical bounce only.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "2-4 quarters"},
            {"name": "SoftBank", "blurb": "Pledged ARM shares to invest in OpenAI.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "anthropic-ipo",
        "tags": ["ai-infra", "finance"],
        "color": "green",
        "badge": "Bellwether",
        "status": "IPO PENDING",
        "title": "Anthropic's IPO decides the next leg of the AI trade",
        "lead": "A successful listing would signal AI still matters to business and could ignite semis, memory and data-centre energy.",
        "bullets": [
            "Expected to be the second-largest IPO in history; pre-IPO CFD was down about 9% when the episode was prepared.",
            "Success = market cap of **$1.6-2 trillion**, close well above listing price and hold the uptrend in following days.",
            "Investment banks with heavy AI exposure will push for a successful listing; pattern noted: big correction before SpaceX's IPO in spring, now before Anthropic, likely before OpenAI's next year.",
            "Dragu won't buy at listing; he'll wait for a lock-up release.",
        ],
        "quote": None,
        "watch": "XTB, the channel's sponsor, offers the pre-IPO Anthropic CFD the hosts discuss.",
        "names": [
            {"name": "Anthropic (ANT)", "blurb": "IPO seen as AI bellwether; not buying at listing.", "stance": "WATCHING", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "reset",
        "tags": ["finance", "geopolitics"],
        "color": "red",
        "badge": "Speculative",
        "status": "LONG-RANGE THESIS",
        "title": "A Paraguayan bank run as a dress rehearsal for a financial reset",
        "lead": "Dragu reads the Paraguay bank freeze like Iceland in 2007-08: a small, isolated failure that can be the start.",
        "bullets": [
            "A major Paraguayan bank has **60%** of citizens without access to their funds; officials resigned.",
            "Dragu's reset window ends around **2032**; until then, accumulate as many assets as possible, because few can buy afterwards.",
            "A reset comes with a crash and enough pain that people accept any solution offered.",
            "Keep cash at home for one to two months; gold or silver coins are useless for buying bread in a crisis.",
            "Alex Marian recalls being locked out of Revolut for days during a Google-linked glitch.",
            "Drivers cited: state and corporate debt, data centres, cameras, 5G+ networks and satellites reshaping the social order.",
        ],
        "quote": {"text": "O resetare vine cu un cres, vine cu o durere foarte mare.", "cite": "— Valentin Dragu"},
        "watch": "Dragu says Paraguay doesn't confirm the thesis, only raises a question mark; the start year of his window is garbled in the captions.",
        "names": None,
    },
    {
        "id": "romania",
        "tags": ["romania", "finance"],
        "color": "amber",
        "badge": "Watch",
        "status": "BVB · LEU",
        "title": "Bucharest stocks ride pension-fund flows, decoupled from a struggling economy",
        "lead": "Pillar 2 funds must deploy contributions into a thin market, lifting prices regardless of fundamentals.",
        "bullets": [
            "A fund with RON 2 million to put into Petrom (SNP) has to pay up until it finds sellers; retail holders are few.",
            "Funds now tilt more to government bonds, likely by arrangement with the finance ministry.",
            "Tail risk: the state could nationalise Pillar 2 funds out of need for cash, a disaster for the BVB.",
            "Dollar strength vs the leu comes through EUR/USD (DXY up on the war); Dragu credits the BNR for holding the euro rate.",
            "Recovery path: a Democratic US mending ties with Europe, German stimulus, Ukraine reconstruction; first signs maybe within two years.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "OMV Petrom (SNP)", "blurb": "Example of scarce float bid up by pension funds.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Separate fundamentals-driven names from hype names before buying this dip"},
    {"icon": "\U0001F50D", "tag": "Market structure", "title": "Check upcoming 13F filings to confirm which funds were liquidated"},
    {"icon": "\U0001F916", "tag": "AI", "title": "Watch the Anthropic IPO's first days as the signal for semis and AI infra"},
    {"icon": "\U0001F4B5", "tag": "Personal finance", "title": "Keep one to two months of cash at home, not only digital balances"},
    {"icon": "\U0001F1F7\U0001F1F4", "tag": "Romania", "title": "Price Pillar 2 nationalisation risk into BVB exposure"},
]

CLAIMS = [
    {"who": "Valentin Dragu", "claim": "The market will rebound strongly after Thursday's selloff.", "metric": "US equities", "target": "strong rebound", "by": "2026-11", "condition": None, "entity": None},
    {"who": "Valentin Dragu", "claim": "Intel can recover to $70-80 but not back to $120.", "metric": "INTC price", "target": "$70-80", "by": None, "condition": None, "entity": "Intel (INTC)"},
    {"who": "Valentin Dragu", "claim": "No strong Intel earnings for the next two to four quarters.", "metric": "Intel earnings", "target": "weak", "by": "2-4 quarters", "condition": "until the foundry division lands contracts", "entity": "Intel (INTC)"},
    {"who": "Valentin Dragu", "claim": "A successful Anthropic IPO means a $1.6-2 trillion market cap.", "metric": "market cap at IPO", "target": "$1.6-2T", "by": None, "condition": None, "entity": "Anthropic (ANT)"},
    {"who": "Valentin Dragu", "claim": "A financial reset with a crash could arrive by around 2032.", "metric": "financial reset", "target": "occurs", "by": "2032", "condition": None, "entity": None},
    {"who": "Valentin Dragu", "claim": "Romania's economy could show first signs of recovery within two years.", "metric": "Romanian economy", "target": "recovery signs", "by": "2028", "condition": "if Europe and Germany recover", "entity": None},
    {"who": "Alex Marian", "claim": "OpenAI will IPO next year, preceded by a large correction.", "metric": "OpenAI IPO", "target": "listing", "by": "2027", "condition": None, "entity": "OpenAI"},
]

RELATIONS = [
    {"from": "SoftBank", "rel": "owns_stake", "to": "ARM (ARM)", "note": "about 90%, shares pledged"},
    {"from": "SoftBank", "rel": "invests_in", "to": "OpenAI", "note": None},
    {"from": "Qualcomm (QCOM)", "rel": "supplies", "to": "SpaceX (SPCX)", "note": "contracts"},
]

HOT_TAKES = [
    {"take": "Din punctul meu de vedere, Trump a pierdut alegerile pentru republicani.", "cite": "— Valentin Dragu", "why": "political attribution"},
    {"take": "Nu vad Intel inapoi la 120 $.", "cite": "— Valentin Dragu", "why": "price call"},
    {"take": "Niciodata nu se va gasi linistea atata timp cat palestinienii sunt pe acel teritoriu impreuna cu evreii", "cite": "— Valentin Dragu", "why": "absolute geopolitical call"},
    {"take": "Statul din nevoia disperata de bani la un moment dat ar putea sa nationalizeze aceste fonduri de pensie privata.", "cite": "— Valentin Dragu", "why": "Romania tail risk"},
    {"take": "Ziua de ieri o o consider o oportunitate iesita din comun", "cite": "— Valentin Dragu", "why": "buy-the-dip call"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "tag": "Sources", "title": "Sources referenced: Jackson Hole central-bank meeting; upcoming 13F filings; hosts' own members-only video and Monday newsletter."},
]

GLOSSARY = [
    {"term": "Margin call", "def": "Broker sells a leveraged account's positions until the margin owed is recovered."},
    {"term": "13F", "def": "Quarterly SEC filing disclosing large US funds' holdings."},
    {"term": "Pilon 2", "def": "Romania's mandatory private pension pillar, managed by private administrators."},
    {"term": "Lock-up", "def": "Period after an IPO during which insiders cannot sell shares."},
]
