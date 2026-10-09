"""Data file for Valuetainment — Elon Musk's Next Target: The Cell Phone Industry."""

META = {
    "title": "Elon Musk’s Next Target: The Cell Phone Industry | Starling Wants to Dominate AT&T & Verizon",
    "channel": "Valuetainment",
    "speakers": "Patrick Bet-David (host), Tom Ellsworth, Adam and Vinnie (panel)",
    "date": "2026-10-09",
    "video_url": "https://www.youtube.com/watch?v=-DmKbC5Slsw",
    "thread_line": "4 threads · SpaceX's ~$8B low-band spectrum deal and the 7% carrier selloff, dead zones as the consumer pain point, a possible Tesla phone and Musk's flywheel versus Apple, and Musk's growing concentration of power.",
    "category": "market",
}

SNAPSHOT = [
    "SpaceX agreed to buy roughly **$8B of nationwide 800 MHz low-band spectrum** from Grain Management (up to 14 MHz paired), on top of ~$19.6B of earlier EchoStar spectrum; Verizon fell 7.3%, AT&T 7.8%, T-Mobile 7%.",
    "The trigger phrase for the panel was **'advanced terrestrial deployment'**: service from space and from the ground, filling dead zones in cities and concrete buildings.",
    "Tom's explanation of the drop: a stock prices today's business plus future speculation, and the 7% is future business investors now doubt (the Nvidia-to-Google chip headline as the mirror image).",
    "The panel's own poll: **86% would switch** to Starlink if dead zones disappeared; Tom says it's too late for rivals to respond, and that habit and age are the only brakes.",
    "Tom puts the odds of a **Tesla phone at 70% and rising**, and calls it embarrassing for Apple, whose last big categories were Watch (2015), AirPods (2016) and Vision Pro (2024).",
    "Patrick frames Musk's 'flywheel' (rockets, Starlink, mobile, AI, Tesla, robots, X) as possibly passing Apple and Amazon, with a darker note on one person's concentration of power.",
]

THEMES = [
    {
        "id": "spectrum-deal-selloff",
        "tags": ["space", "consumer", "policy"],
        "color": "amber",
        "badge": "Confirmed event",
        "status": "SPACEX LOW-BAND SPECTRUM DEAL — OCT 2026",
        "title": "SpaceX buys ~$8B of low-band spectrum and the three US carriers fall about 7% each",
        "lead": "The market read the deal as SpaceX becoming a phone carrier, not just a coverage add-on.",
        "bullets": [
            "Deal: roughly **$8B** of nationwide **800 MHz** low-band spectrum from **Grain Management**, giving SpaceX up to 14 MHz of paired spectrum.",
            "It sits on top of ~**$19.6B** of earlier spectrum purchases tied to EchoStar and FCC approval for a **15,000-satellite** Gen 2 Starlink mobile constellation.",
            "Stock reaction: Verizon **-7.3%**, AT&T **-7.8%**, T-Mobile **-7%**.",
            "Tom: what 'freaked everybody out' was the line that spectrum would be coupled to an **advanced terrestrial deployment** — Grain's own legal advisor flagged service from both space and Earth.",
            "Tom's reading: if a building is too deep for Starlink from outside, the terrestrial side fills the gap, so it's a blanket from space plus gap-filling in cities.",
            "Why the drop went beyond today's earnings: stocks price current business plus future speculation; the 7% is lost future business (he contrasts Nvidia rising on a future chip sale to Google, 9,000 chips).",
            "Panel notes it's service first: no phone has been announced, and rivals today are terrestrial networks while satellite phones have been niche emergency tools.",
        ],
        "quote": {"text": "He is trying to literally become your phone company.", "cite": "— Patrick Bet-David"},
        "watch": "The panel offers no stated position in SpaceX or the carriers. The host plugs his own consulting and merchandise in the video; those segments are excluded.",
        "names": [
            {"name": "SpaceX (SPCX)", "blurb": "Buying ~$8B of 800 MHz spectrum; Starlink mobile constellation approved for 15,000 satellites.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Verizon (VZ)", "blurb": "Fell 7.3% on the news; 'shivering' per the panel.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "AT&T (T)", "blurb": "Fell 7.8% on the news; panelists' own carrier with dead zones.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "T-Mobile (TMUS)", "blurb": "Fell 7%; its older spectrum is part of the 'terrestrial' angle discussed.", "stance": "NEGATIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "EchoStar (SATS)", "blurb": "Source of ~$19.6B of earlier SpaceX spectrum purchases.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Grain Management", "blurb": "Seller of the ~$8B low-band spectrum.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "dead-zones-switching",
        "tags": ["consumer", "space"],
        "color": "green",
        "badge": "Positive view",
        "status": "CONSUMER SWITCHING CASE",
        "title": "Dead zones are the pain point: 86% in the panel's poll would switch",
        "lead": "The panel treats coverage gaps as the wedge, with Starlink's in-flight performance as proof of quality.",
        "bullets": [
            "Panelists name local dead zones on AT&T: Palm Beach drives, LA's 210 freeway, parts of Dallas, South Florida near the airport, even a home backyard; Tom's sister loses signal on the 405.",
            "Starlink on a private jet gives Zoom calls and fast internet, while cable/'infinity' home internet 'sucks right now' (Patrick).",
            "Poll result: **86%** would leave their carrier if Starlink eliminated 100% of dead zones (Patrick jokes the 14% are people who want Social Security to continue).",
            "Brake on switching: habit and age — 'people don't like change', though some switch for features (Patrick returned to AT&T for five-to-seven-way calls).",
            "Tom: competitors' response is 'too late'; Patrick asks who launches rivals' satellites (answer: they're terrestrial).",
        ],
        "quote": None,
        "watch": "The poll is the panel's own YouTube audience, not a market survey.",
        "names": None,
    },
    {
        "id": "tesla-phone-flywheel",
        "tags": ["consumer", "robotics", "ai-infra"],
        "color": "amber",
        "badge": "Speculative",
        "status": "TESLA PHONE AND THE MUSK FLYWHEEL",
        "title": "A Tesla phone at 70% odds, and Musk's flywheel versus Apple's",
        "lead": "Tom thinks a Tesla phone is 'on the bench', and the panel sees Musk assembling a flywheel that could pass Apple and Amazon.",
        "bullets": [
            "Patrick's sequencing analogy: Tesla built chargers everywhere, then rivals needed them; carrier first, then a phone.",
            "Tom: **70% and rising** that a Tesla phone ships; he points to a seen prototype and says it's 'not a teaser'.",
            "Patrick: this is embarrassing for **Apple**, which 'stayed on the phone side'; its cadence is Watch 2015, AirPods 2016, Vision Pro 2024, Home Hub in 2026 ('hardly a major category').",
            "Flywheel (Adam's AI-built diagram): SpaceX launches, Starlink connects, the mobile company connects phones, AI supplies intelligence, leading to revenue and scale.",
            "Patrick's ranking today: Apple's flywheel #1, **Amazon #2**; Musk's could pass both quickly; Disney was top-10 but slipping.",
            "A client he met on a call spent two hours in a Tesla on full self-drive — Patrick's example of lock-in (Tesla + Starlink + phone + car).",
        ],
        "quote": {"text": "Elon is expanding his flywheel... somebody who owns a Tesla, buy Starlink, buy a phone. The phone talks to the car.", "cite": "— Patrick Bet-David"},
        "watch": "Tom's 70% is a gut estimate; no Tesla phone has been announced.",
        "names": [
            {"name": "Tesla (TSLA)", "blurb": "Panel sees a Tesla phone at ~70% odds and self-drive lock-in for its flywheel.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Seen as strongest flywheel today but stuck on the phone side; slow new categories.", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "Ranked #2 flywheel (Amazon retail plus AWS).", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Example of a stock rising on future sales (9,000 chips to Google).", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "musk-power",
        "tags": ["geopolitics", "policy"],
        "color": "red",
        "badge": "Cautionary tale",
        "status": "CONCENTRATION OF POWER — PANEL OPINION",
        "title": "One company stack, 'world leader of all presidents'?",
        "lead": "Patrick says Musk's reach across rockets, telecom, AI and social media makes governments dependent on him, which cuts both ways.",
        "bullets": [
            "Patrick relays a conversation with a chief of staff to a world leader in a war: they 'know Trump won't be here for two more years' and Musk 'will be a problem for 20, 30 years'.",
            "His line: Musk 'is slowly becoming the world leader of all presidents'; 'they got to come to him'.",
            "Stack named: rockets, SpaceX, Boring Company, Neuralink, Tesla, phones, robots, X.",
            "He likes Musk's conservative lean 'at face value' but warns that if he 'turns sour' it 'could go ugly very quickly'.",
        ],
        "quote": {"text": "He is slowly becoming the world leader of all presidents.", "cite": "— Patrick Bet-David"},
        "watch": "The chief-of-staff account is Patrick's second-hand anecdote with no name given; the panel presents it as opinion.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4E1", "tag": "Telecom", "title": "Track the SpaceX spectrum deal's terrestrial piece; coverage in buildings is what threatens carriers, not outdoor satellite."},
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Read the ~7% carrier selloff as a repricing of future subscribers, not current earnings."},
    {"icon": "\U0001F4F1", "tag": "Consumer", "title": "List your own dead zones; if Starlink fixes them, your switching cost is mostly habit."},
    {"icon": "\U0001F697", "tag": "Tesla", "title": "Treat a Tesla phone as unannounced speculation (panel guess: 70%) until a product shows up."},
    {"icon": "\U0001F3AF", "tag": "Strategy", "title": "Map your own business flywheel and moat; the panel's point is that scale stacks across products."},
]

HOT_TAKES = [
    {"take": "I think it's 70% and rising every minute.", "cite": "— Tom Ellsworth", "why": "Odds on a Tesla phone"},
    {"take": "It's too late.", "cite": "— Tom Ellsworth", "why": "Says carriers can't compete with SpaceX"},
    {"take": "He is slowly becoming the world leader of all presidents.", "cite": "— Patrick Bet-David", "why": "Claim of Musk's power"},
    {"take": "Very quickly Elon's flywheel could pass everybody up.", "cite": "— Patrick Bet-David", "why": "Predicts Musk flywheel beats Apple and Amazon"},
]

CLAIMS = [
    {"who": "Tom Ellsworth", "claim": "A Tesla phone will be released.", "metric": "Tesla phone launch probability", "target": "70%", "by": None, "condition": None, "entity": "Tesla (TSLA)"},
    {"who": "Patrick Bet-David", "claim": "Musk's flywheel passes Apple and Amazon as the most powerful in the world.", "metric": "flywheel ranking", "target": "#1", "by": None, "condition": None, "entity": "SpaceX (SPCX)"},
    {"who": "Tom Ellsworth", "claim": "Verizon, AT&T and T-Mobile cannot respond effectively to SpaceX's carrier entry.", "metric": "carrier competitive response", "target": "too late", "by": None, "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "SpaceX (SPCX)", "rel": "competes_with", "to": "Verizon (VZ)", "note": "mobile service entry"},
    {"from": "SpaceX (SPCX)", "rel": "competes_with", "to": "AT&T (T)", "note": "mobile service entry"},
    {"from": "SpaceX (SPCX)", "rel": "competes_with", "to": "T-Mobile (TMUS)", "note": "mobile service entry"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4A1", "title": "Patrick's flywheel example: 25 relationships built early in his insurance career (quarterly lunches, no asks) fed referrals that led to a $50M contact; he is talking to publishers about a flywheel book.", "tag": "Careers"},
    {"icon": "\U0001F4DA", "title": "Sources referenced: a news article on the SpaceX/Grain deal (Grain's legal advisor quoted), the panel's own poll and chief-of-staff anecdote; no other outside sources named.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Low-band spectrum", "def": "Lower-frequency radio spectrum (e.g. 800 MHz) that passes through walls better than high-band."},
    {"term": "Paired spectrum", "def": "Matched uplink and downlink frequency blocks used together for a two-way service."},
    {"term": "Flywheel", "def": "Patrick's term for a business loop where each product feeds the next and makes leaving harder."},
]
