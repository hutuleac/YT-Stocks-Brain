META = {
    "title": "China se prăbușește, retailul se joacă cu focul by AM (27.10.2026)",
    "channel": "AM",
    "speakers": "AM",
    "date": "2026-10-27",
    "video_url": "",
    "thread_line": "6 threads · retail options and 3x leverage records · China's historic crash · Brazil election shock · Meta's $35B raise and AI money circularity · ASTS, Rocket Lab, Nebius and Tesla · Anthropic's S-1",
    "category": "market",
    "region": "ro",
}

SNAPSHOT = [
    "Source note: built from AM's pasted written/AI-assisted material (no captions or video link), so figures are as AM states them.",
    "AM's stance: be patient, **buy in small tranches and never exhaust liquidity**; the Robinhood (HOOD) report is the key data point on whether retail is tired or liquidated.",
    "Retail options volume hit 61% of total volume on Citadel's platform, and the ten largest US leveraged equity ETFs drew $12B in a month (SOXL took $9B in two weeks, a record); AM reads this as a caution signal.",
    "China is in a historic crash: STAR50 -40% in under four months from ~250x earnings, ~$3.5T lost since May, and real estate investment -21% year on year, worse than any 2008 reading.",
    "Brazil: Lula's 51.8% to 48.2% win sent Brazilian equity ETFs down as much as 27% after markets priced a Bolsonaro victory; lesson is never to position aggressively on one political scenario.",
    "Meta plans ~$35B of equity raises (plus a possible $60B Class C program) as NVDA, AMD and AVGO signal interest in buying up to $5B of its shares, which AM calls circular AI money.",
    "Anthropic's S-1 shows $16.3B H1 revenue but ~$265.6B of minimum compute commitments; AM calls the valuation \"a bad joke\" and won't buy at listing.",
]

THEMES = [
    {
        "id": "retail-leverage-hood",
        "tags": ["finance", "consumer"],
        "color": "red",
        "badge": "High conviction",
        "status": "RETAIL OPTIONS 61% · HOOD REPORT IS KEY",
        "title": "Retail is trading options and 3x leverage at record pace",
        "lead": "AM treats the record retail leverage as a caution signal and waits for Robinhood's report to see if retail is exhausted or already liquidated.",
        "bullets": [
            "Strategy: patience, small tranches, buy through the next 15-20 days of events, but never exhaust liquidity; the HOOD report is vital because it shows in black and white whether retail has tired or been liquidated.",
            "Retail options activity reached **61%** of total volume on Citadel's platform last week, near the all-time high, +16 points in 12 months and 10 points above the 2020 pandemic peak.",
            "SPY and QQQ made up 47% of retail options trades; 1.7 index and ETF contracts traded per single-stock contract.",
            "The ten biggest US leveraged equity ETFs drew $12B in a month while their assets fell $20B; SOXL (3x semis) took $9B in two weeks, the largest two-week inflow ever, and TQQQ $1.3B. They took in $19B over five months.",
            "AM's read: people buying 3x products on every dip is not a health signal; he doesn't play that game and doesn't buy 3x leverage on emotion.",
        ],
        "quote": {"text": "sub nicio forma nu ne epuizam lichiditatile.", "cite": "— AM"},
        "watch": "AM runs a subscriber-focused service and says he invests in small tranches in companies he holds with conviction.",
        "names": [
            {"name": "Robinhood (HOOD)", "blurb": "Its report will show whether hyperactive retail is spent or liquidated.", "stance": "WATCHING", "conviction": "Medium", "horizon": "next report"},
            {"name": "SOXL", "blurb": "3x semiconductor ETF with record $9B two-week inflow.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "TQQQ", "blurb": "3x Nasdaq ETF with $1.3B in two weeks.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "china-crash",
        "tags": ["geopolitics", "finance", "ai-infra"],
        "color": "red",
        "badge": "High conviction",
        "status": "STAR50 -40% · REAL ESTATE -21%",
        "title": "China's historic crash makes the 2008 comparison fair",
        "lead": "Chinese tech valuations collapsed and the property slump is deeper than any 2008 reading.",
        "bullets": [
            "STAR50 fell **40%** in under four months after trading near 250x earnings; Chinese stocks lost about $3.5T from the May peak and CSI 300 entered a bear market.",
            "MiniMax and Zhipu lost $150B combined from their highs; several AI hardware companies fell 50-60%. The AI story survives, but investors stopped paying any price.",
            "Property investment fell 21% year on year in the first nine months of 2026, worse than -20% in eight months and than -16% in the 2020 pandemic; real estate has shrunk every month since early 2022, the longest streak on record. In 2008 the measure never fell below +1%.",
            "AM expects the topic to return often in coming months because markets are looking at AI and America instead.",
        ],
        "quote": {"text": "Criza Chinei din 2008 se intampla acum", "cite": "— AM"},
        "watch": "The index and property figures are as AM states them without sources.",
        "names": [
            {"name": "MiniMax", "blurb": "Lost $150B with Zhipu from highs.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Zhipu", "blurb": "Lost $150B with MiniMax from highs.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "brazil-election",
        "tags": ["geopolitics", "policy", "finance"],
        "color": "amber",
        "badge": "Confirmed event",
        "status": "LULA WINS · BRAZIL ETFS -27%",
        "title": "Lula's win catches Brazil positioning on the wrong foot",
        "lead": "Markets had priced a Bolsonaro win, and equity ETFs fell as much as 27% on the surprise.",
        "bullets": [
            "Luiz Inácio Lula da Silva beat Flávio Bolsonaro **51.8% to 48.2%** for an unprecedented fourth term.",
            "Markets had positioned for tighter fiscal policy and lower rates, with Lula's odds down to about 10% before the vote; Brazilian equity ETFs dropped as much as 27%.",
            "Lula is the first candidate in modern Brazilian democracy to lose the first round and win the runoff.",
            "AM's lesson: never position aggressively on a single political scenario, however sure the odds look.",
        ],
        "quote": {"text": "nu te pozitionezi niciodata agresiv pe un singur scenariu politic", "cite": "— AM"},
        "watch": None,
        "names": None,
    },
    {
        "id": "ai-money-circularity",
        "tags": ["ai-infra", "finance", "semis"],
        "color": "amber",
        "badge": "Contested",
        "status": "META ~$35B RAISE · SPACEX $40B LEASE",
        "title": "Big money keeps flowing into AI infrastructure, and it is circular",
        "lead": "Chip suppliers want Meta's stock while Meta raises ~$95B of capacity to buy their chips.",
        "bullets": [
            "Meta filed an S-3 shelf and plans ~**$35B**: $22.5B of Class A common via forward sales and $12.5B of depositary shares in mandatorily convertible preferred.",
            "NVDA, AMD and AVGO expressed non-binding interest in buying up to $5B of Meta shares combined; Meta also prepares a possible $60B program of non-voting Class C shares from Q1 2027, about $95B of equity capacity against $135-145B of 2026 capex.",
            "AM's point: when chip suppliers buy stock in their client and the client raises nearly $100B to buy chips from them, money circulates inside one AI ecosystem; he doesn't say the model fails, only to be aware of the circularity.",
            "AVGO closed a $63B deal to finance AI chips for Anthropic. Oracle unveiled Fusion Companion and Fusion Agentic Home at Oracle AI World, letting ChatGPT run workflows across finance, HR, supply chain, sales and service with enterprise permissions.",
            "SpaceX signed a firm commitment with an Apollo-managed entity to finance GPU clusters and data-center equipment via leasing, ~$40B of principal over 5 to 5.25 years; closing expected before year-end, deliveries and lease payments from H1 2027, financing cost not yet set.",
        ],
        "quote": {"text": "banii se rotesc in interiorul aceluiasi ecosistem AI", "cite": "— AM"},
        "watch": None,
        "names": [
            {"name": "Meta (META)", "blurb": "~$35B equity raise, shelf registration, possible $60B Class C program.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Nvidia (NVDA)", "blurb": "Non-binding interest in Meta shares (up to $5B with AMD and AVGO).", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "AMD", "blurb": "Non-binding interest in Meta shares.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Broadcom (AVGO)", "blurb": "Interest in Meta shares; $63B deal financing AI chips for Anthropic.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Oracle (ORCL)", "blurb": "Fusion Companion and Agentic Home let ChatGPT execute enterprise workflows.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SpaceX", "blurb": "~$40B GPU lease financing from Apollo; entering compute economy.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": "close by year-end"},
            {"name": "Apollo Global Management (APO)", "blurb": "Entity it manages buys the equipment and leases it to SpaceX.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "portfolio-operators",
        "tags": ["space", "ai-infra", "consumer"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "ASTS BRAZIL · NEUTRON · NEBIUS · TESLA UPGRADE",
        "title": "ASTS, Rocket Lab and Nebius deliver; Barclays upgrades Tesla to $450",
        "lead": "AM's holdings are delivering operationally, and Barclays turns bullish on Tesla.",
        "bullets": [
            "AST SpaceMobile got Brazilian approval for 30 MHz of S-band and secondary access to up to 20 MHz of 700 MHz, signed four regional mobile operators and plans four ground stations for BlueBird satellites in a market of 200M+ lines; about half of Brazil's highway network lacks 4G or 5G.",
            "Rocket Lab's Neutron: Stage 2 and the Thrust Module arrived at Launch Complex 3 and go straight to the pad for testing; with no classic strongback, testing the single pad connection now could avoid costly launch delays.",
            "Nebius has about $8B in cash and expects over $9B in customer prepayments, avoiding the fragile, undercapitalized neocloud problems Elon warned about; Token Factory could earn more from the same GPUs as inference demand grows.",
            "Barclays (analyst Dan Levy) upgraded TSLA to Overweight from Equal Weight and raised the target to **$450** from $370, citing a potential SpaceX combination premium, better auto demand, strong energy, sharp robotaxi mileage inflection and FSD adoption above 75% of new North American deliveries.",
        ],
        "quote": {"text": "Nebius are o sansa reala sa devina un gigant al economiei AI.", "cite": "— AM"},
        "watch": "ASTS, RKLB and NBIS are what AM calls \"our companies\", so he is positioned in them.",
        "names": [
            {"name": "AST SpaceMobile (ASTS)", "blurb": "Brazil spectrum approval and four operator deals.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Rocket Lab (RKLB)", "blurb": "Neutron stages delivered to Launch Complex 3.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Nebius (NBIS)", "blurb": "~$8B cash, $9B+ prepayments, Token Factory.", "stance": "OWNS", "conviction": "Medium", "horizon": None},
            {"name": "Tesla (TSLA)", "blurb": "Barclays upgrade to Overweight, $450 target.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Barclays (BCS)", "blurb": "Upgraded Tesla; analyst Dan Levy.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "anthropic-s1-am",
        "tags": ["ai-infra", "software"],
        "color": "amber",
        "badge": "Contested",
        "status": "ANTHROPIC S-1 · TICKER ANT",
        "title": "Anthropic's S-1: staggering growth, huge commitments, AM won't buy at listing",
        "lead": "Revenue is exploding, but $265.6B of minimum commitments and a rich valuation keep AM on the sidelines.",
        "bullets": [
            "Listing on the Nasdaq Global Select Market as **ANT**, led by Goldman Sachs, Morgan Stanley and J.P. Morgan; price range and share count not yet disclosed.",
            "Revenue: H1 2026 $16.3B vs $1.16B in H1 2025; 2025 $4.59B vs $386M in 2024. Customers over $100K: 11,900+ (from 950+); over $1M: 1,900+; over $10M: about 250. $13.1B (80% of H1) from consumption, $3.2B (20%) from subscriptions.",
            "Losses: H1 operating loss $693M and net loss **$80.7B**, of which $72.4B is a fair-value accounting adjustment on convertible notes tracking its rising valuation; 2025 also included a $1.5B Bartz copyright settlement.",
            "Compute: $8.9B spent in H1; minimum future commitments of $114.5B to Google through July 2033, $110B to Amazon through April 2036 and $44.9B to Microsoft through May 2033, about $265.6B owed regardless of use.",
            "Balance sheet: $131.7B cash and short-term investments plus up to $77B of note facilities ($20B Google, $15B Amazon, $42B Broadcom). Public benefit corporation; Class F (Founder LLC, Dario and Daniela Amodei plus 5 co-founders) holds 50.1% of votes, Class N partner shares are non-voting, Amazon capped at 12% and Google at 14.99%; ~5,300 employees; 5% of shares go to the Anthropic Public Benefit Fund.",
            "The S-1 itself warns advanced AI could pose catastrophic or existential risks to humanity.",
        ],
        "quote": {"text": "evaluarea cu care Anthropic vrea sa iasa pe piata este o gluma proasta", "cite": "— AM"},
        "watch": "AM doesn't negotiate with the market: he would revisit if the price becomes rational.",
        "names": [
            {"name": "Anthropic", "blurb": "S-1 filed; $16.3B H1 revenue, $265.6B minimum commitments; AM won't buy at listing.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "at listing"},
            {"name": "Alphabet (GOOGL)", "blurb": "Anthropic owes it at least $114.5B to 2033; owns up to 14.99%.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "$110B minimum commitments through 2036; capped at 12%.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "$44.9B minimum commitments through May 2033.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001FA99", "tag": "Strategy", "title": "Buy in small tranches in names you hold with conviction and keep liquidity in reserve through the next 15-20 days."},
    {"icon": "\U0001F4F0", "tag": "Retail", "title": "Read Robinhood's report for signs that retail is exhausted or liquidated before adding risk."},
    {"icon": "\U0001F6A8", "tag": "Leverage", "title": "Avoid 3x ETFs bought on emotion; record inflows into SOXL and TQQQ signal euphoria."},
    {"icon": "\U0001F30F", "tag": "Geopolitics", "title": "Do not size aggressively on a single political outcome, as Brazil's result showed."},
    {"icon": "\U0001F4CB", "tag": "IPOs", "title": "Wait on the Anthropic IPO and read its commitments before paying for the growth story."},
]

HOT_TAKES = [
    {"take": "Noi nu jucam jocul acesta.", "cite": "— AM", "why": "Rejects participation in retail leverage."},
    {"take": "evaluarea cu care Anthropic vrea sa iasa pe piata este o gluma proasta", "cite": "— AM", "why": "Dismisses Anthropic's valuation."},
    {"take": "acesta nu este un semnal de sanatate, ci unul de prudenta pentru noi", "cite": "— AM", "why": "Reads record retail leverage as a warning."},
    {"take": "nu cumparam levier 3x pe emotie", "cite": "— AM", "why": "Explicit stance against 3x products."},
]

CLAIMS = [
    {"who": "AM", "claim": "The Robinhood report shows whether retail has tired or been liquidated, and matters more than other data in the next weeks.", "metric": "Robinhood report", "target": "retail exhaustion signal", "by": "2026-11", "condition": None, "entity": "Robinhood (HOOD)"},
    {"who": "Barclays (cited by AM)", "claim": "Tesla price target is $450, up from $370, with an Overweight rating.", "metric": "TSLA price target", "target": "$450", "by": None, "condition": None, "entity": "Tesla (TSLA)"},
    {"who": "SpaceX (cited by AM)", "claim": "The $40B Apollo GPU lease closes before year-end, with deliveries and lease payments from H1 2027.", "metric": "SpaceX Apollo lease", "target": "~$40B principal", "by": "2026-12", "condition": None, "entity": "SpaceX"},
    {"who": "Meta (cited by AM)", "claim": "Meta spends $135-145B on capital expenditure in 2026.", "metric": "Meta 2026 capex", "target": "$135-145B", "by": "2026", "condition": None, "entity": "Meta (META)"},
    {"who": "Meta (cited by AM)", "claim": "Meta launches a possible $60B non-voting Class C share program from Q1 2027.", "metric": "Class C share program", "target": "$60B", "by": "2027-03", "condition": None, "entity": "Meta (META)"},
]

RELATIONS = [
    {"from": "Apollo Global Management (APO)", "rel": "invests_in", "to": "SpaceX", "note": "~$40B GPU lease financing via an Apollo-managed entity"},
    {"from": "Broadcom (AVGO)", "rel": "supplies", "to": "Anthropic", "note": "$63B deal to finance AI chips"},
    {"from": "Nvidia (NVDA)", "rel": "invests_in", "to": "Meta (META)", "note": "non-binding interest in up to $5B of shares with AMD and AVGO"},
    {"from": "Anthropic", "rel": "customer_of", "to": "Alphabet (GOOGL)", "note": "$114.5B minimum compute commitment through July 2033"},
    {"from": "Anthropic", "rel": "customer_of", "to": "Amazon (AMZN)", "note": "$110B minimum commitment through April 2036"},
    {"from": "Anthropic", "rel": "customer_of", "to": "Microsoft (MSFT)", "note": "$44.9B minimum commitment through May 2033"},
]

OTHER_NEWS = [
    {"icon": "\U0001F9ED", "title": "AM's closing frame: China shows the price of paying anything for a story, Brazil the cost of one scenario, and 3x retail the euphoria that rarely ends well; opportunities keep appearing for the prepared.", "tag": "Outlook"},
]

GLOSSARY = [
    {"term": "S-3 shelf", "def": "An SEC registration letting a company issue securities later without fixing size, price or timing now."},
    {"term": "Forward sale agreement", "def": "A deal to sell shares at a future date at a price set today, used to raise equity in stages."},
    {"term": "Strongback", "def": "The structure supporting a rocket on the pad; Neutron doesn't use a classic one."},
]
