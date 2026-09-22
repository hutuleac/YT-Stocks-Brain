"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Bitcoin Hits First Real Resistance After PUMPING 45% This Quarter | Gary Cardone",
    "channel": "The Wolf Of All Streets",
    "speakers": "Scott Melker, Andrew, Tilman, with guest Gary Cardone",
    "date": "2026-09-22",
    "video_url": "https://www.youtube.com/watch?v=mgrCrhbipoo",
    "thread_line": "6 threads: record ETF inflows and a Morgan Stanley retail signal, Gary Cardone's STRC arbitrage trade, Bitcoin's regime change from sell-rips to buy-dips, Wall Street's sovereign-wealth and collateral thesis, dry powder/compounding after Buffett's exit, and a scarce-assets-vs-cheap-services macro debate",
    "category": "market",
}

SNAPSHOT = [
    "Bitcoin hit its first real resistance near **$88,000** after pumping 45% this quarter; hosts are split on whether a healthy 15-20% pullback comes first or the move keeps grinding higher.",
    "Spot Bitcoin ETFs pulled in nearly **$9B** Monday (9th-largest inflow ever) with only $380M from IBIT — Morgan Stanley posted its biggest inflow day ever at $61.7M, more than double its prior record, read as genuine retail wealth-management demand rather than options/futures flow.",
    "The average Bitcoin ETF holder is back above water for the first time since January, with an estimated cost basis of **$81,722**.",
    "Gary Cardone detailed his STRC (Strategy preferred stock) arbitrage trade: borrowing cheap, collecting an **11.5%** yield, and netting roughly $750K instead of buying spot Bitcoin at $98K.",
    "Hosts frame this as a genuine regime change — Bitcoin has reclaimed every long-term moving average, ~180 'strategy' treasury companies are working through a ~600,000 BTC overhang, and old-school narrative-driven holders are capitulating (some rotating into Zcash) as Wall Street systematic buyers set the bottoms.",
    "Macro debate: Tilman argues continued money-printing means everything gets more expensive over the next 20 years, favoring scarce hard assets (Bitcoin, gold, silver, land); Gary counters that services and access are getting dramatically cheaper even as hard assets stay scarce.",
    "Side notes: Warren Buffett is stepping down as Berkshire chairman after a tenure Andrew pegs at a ~6.6 million% return; Trump's Intel equity stake is floated as a precedent for broader US government stakes in corporates.",
]

THEMES = [
    {
        "id": "etf-flows-institutional",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "CONFIRMED — Monday inflows spread broadly across issuers",
        "title": "A Record ETF Day That Actually Looks Like Retail Demand",
        "lead": "Monday's near-$9B Bitcoin ETF inflow was unusually spread across issuers rather than concentrated in IBIT, which the hosts read as real wealth-management demand rather than options-driven flow.",
        "bullets": [
            "Spot Bitcoin ETFs took in nearly **$9B** Monday, the ninth-largest inflow day ever; only $380M of it came from IBIT, with the rest spread across the top five issuers.",
            "**Morgan Stanley (MS)** posted its biggest single-day inflow since its spot Bitcoin ETF launched — $61.7M, more than double its prior record of $30M — and the fund has seen zero dollars of outflows since inception.",
            "Fidelity, ARK, and Bitwise all had large inflow days too; Andrew calls the Morgan Stanley number 'as pure retail demand as we're going to see,' likely driven more by clients asking advisers than advisers pitching clients.",
            "The average Bitcoin ETF holder is back above water for the first time since January, with an estimated ETF cost basis of $81,722 — well below the current price.",
            "Andrew expects a run of big inflow days over the next couple of weeks as Q3-into-Q4 portfolio reviews prompt more allocation decisions.",
        ],
        "quote": {"text": "That's retail demand, right? Like that's what jumped out to me is that Morgan Stanley number is absolutely retail demand.", "cite": "— Andrew"},
        "watch": None,
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "Spot ETFs pulled in ~$9B in a single day, with the average holder back in profit for the first time since January.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Morgan Stanley (MS)", "blurb": "Posted its largest-ever single-day Bitcoin ETF inflow, read as a genuine retail wealth-management demand signal.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
            {"name": "Fidelity", "blurb": "Reported large Bitcoin ETF inflows alongside Morgan Stanley on the same day.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
            {"name": "ARK", "blurb": "Reported large Bitcoin ETF inflows the same day.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
            {"name": "Bitwise", "blurb": "Reported large Bitcoin ETF inflows the same day.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "gary-strc-trade",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "High conviction",
        "status": "HOLDING — plans to convert to cash at $99.50-100",
        "title": "Gary Cardone's STRC Arbitrage: Getting Paid to Wait for Bitcoin",
        "lead": "Instead of buying Bitcoin directly near its highs, Gary Cardone used Strategy's yield-bearing preferred stock to collect a double-digit yield while still being able to convert into Bitcoin later.",
        "bullets": [
            "Gary bought Strategy's STRC preferred stock near its $100 par value rather than buying **$98,000** Bitcoin roughly six to nine months ago, and has collected about $750K in dividends since, acquiring 12 Bitcoin along the way.",
            "He's borrowing from Coinbase at 7.5% and from his bank at 5.5% while STRC pays him 11.5% — capturing the spread while removing volatility exposure from the underlying trade.",
            "Plan: convert out of STRC back to cash once it hits $99.50-$100 (his cost basis), then redeploy into Bitcoin if the price is right.",
            "He pushes back on critics who called this a 'sailor-paid shill' setup or warned Strategy would be liquidated, arguing the math (not personality) always supported holding STRC through the dip.",
            "General framing: this is a Wall-Street-style arbitrage tool that lets a Bitcoiner reach into both the crypto and equity/credit markets simultaneously, rather than a bet on price direction alone.",
        ],
        "quote": {"text": "I've made $750,000 on STRC while I didn't know what the market was doing. I was confused.", "cite": "— Gary Cardone"},
        "watch": None,
        "names": [
            {"name": "Strategy (MSTR)", "blurb": "Its STRC preferred stock delivered Gary an 11.5% yield and ~$750K in dividends while he waited out Bitcoin's dip instead of buying spot at $98K.", "stance": "BUYING-ADDING", "conviction": "High", "horizon": None},
            {"name": "Coinbase (COIN)", "blurb": "Lending platform Gary borrows against at 7.5% as part of the STRC arbitrage spread.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "regime-change-price-action",
        "tags": ["crypto"],
        "color": "amber",
        "badge": "Contested",
        "status": "DEVELOPING — near-term pullback debated, longer trend seen as intact",
        "title": "Bitcoin's Regime Change: From Sell-the-Rip to Buy-the-Dip",
        "lead": "Bitcoin has reclaimed every long-term moving average and hosts argue the market has structurally flipped from a bear-market sell-rallies posture to a bull-market buy-dips one, even as a near-term pullback looks likely.",
        "bullets": [
            "Bitcoin is up ~45% this quarter and hit resistance near $88,000-90,000, having reclaimed every one of its long-term moving averages — a level Andrew calls a genuine higher high.",
            "Andrew's statistical framing: after a 40%+ move in a two-week span, Bitcoin is roughly **90% more likely** to retrace back down 10% than to continue up another 10% from current levels, since risk/reward resets with every big move.",
            "Supply overhang: roughly 180 'strategy' (MicroStrategy-style) treasury companies are working through pressure to sell down a combined ~600,000 BTC; one such company (heard on captions as 'Satsuma') reportedly imploded, with about 600 BTC coming back onto the market.",
            "Gary won a bet with his brother that Bitcoin would hit $75,000 before $81,700 — it happened within two days, briefly touching $75,000 for only about 20 seconds before squeezing away.",
            "Old-school, narrative-driven Bitcoiners are capitulating out of coins and some have rotated into Zcash, chasing an 'anarchist coin' narrative Gary calls naive; hosts read this OG capitulation as a genuine changing-of-the-guard moment for the asset.",
            "Both hosts expect any pullback to be a slow bleed into the low-to-mid 70s rather than a violent single-day crash, and would be surprised to revisit $75,000 within the next 90 days.",
        ],
        "quote": {"text": "In a bear market, you were looking to sell rips. Now you should be looking to buy dips.", "cite": "— Andrew"},
        "watch": "Andrew flags that the exact identity and spelling of the imploded treasury company referenced in this segment is uncertain from the audio — treated here as a described event, not a confirmed company name.",
        "names": [
            {"name": "Zcash", "blurb": "Old-school Bitcoin narrative holders are rotating into it, which Gary dismisses as an 'incredibly naive, very childlike' anarchist-coin narrative.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "wall-street-structural-thesis",
        "tags": ["crypto", "policy"],
        "color": "amber",
        "badge": "Speculative",
        "status": "EARLY — collateral market and sovereign-stake ideas not yet realized",
        "title": "Bitcoin as Collateral, and a Sovereign Wealth Fund Twist",
        "lead": "Hosts argue Bitcoin's next major adoption unlock is becoming usable loan collateral like real estate, and float the idea that a more interventionist US government could eventually add Bitcoin to a strategic reserve.",
        "bullets": [
            "Tilman's thesis: real estate created wealth largely because it's liquid collateral you can HELOC against the next day; once banks offer preferred lending rates against Bitcoin collateral (cheaper to repossess, easier to price), Bitcoin becomes a genuine household-name collateral asset.",
            "Gary is already doing this manually via STRC/Bitcoin-backed borrowing at 5.5-7.5%, well below the 11.5% yield he's collecting — a preview of what mainstream bank lending against Bitcoin could look like.",
            "Tilman raises the idea that Trump's Intel equity stake could be a precedent for broader US government stakes in corporates (10% stakes, or steering money-market/401k flows into US equities) to compete with sovereign-backed rivals like China's state-supported companies.",
            "Gary adds that this could extend to Bitcoin directly — a government strategic Bitcoin reserve alongside equity stakes — framing it as a diversification play he hadn't previously considered but now sees as plausible.",
        ],
        "quote": {"text": "One day, the collateral value of Bitcoin will be absolutely the creme de la creme collateral.", "cite": "— Gary Cardone"},
        "watch": "This entire thread is speculative extrapolation from a single cited precedent (the Intel stake) — no policy or lending product discussed here currently exists.",
        "names": [
            {"name": "Intel (INTC)", "blurb": "Cited as the precedent for the Trump administration taking direct equity stakes in US companies.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "dry-powder-compounding",
        "tags": ["finance", "crypto"],
        "color": "gray",
        "badge": "Speculative",
        "status": "CONCEPTUAL — volatility-harvesting thesis, not a specific trade",
        "title": "Dry Powder, Compounding, and Buffett's Exit",
        "lead": "Hosts frame patient capital and systematic volatility-harvesting — not appreciation bets — as the next edge in markets, with Warren Buffett's own track record as the reference case.",
        "bullets": [
            "Warren Buffett is stepping down as Berkshire Hathaway chairman; Andrew estimates Berkshire returned roughly **6.6 million%** over his ~50-60 year tenure, and Gary calls him 'a vulture investor' who specialized in buying distressed assets cheap, not a passive value holder.",
            "Berkshire's cash pile fell from **$397B to $360B** in a single quarter as it began deploying some of its record dry-powder position.",
            "Tilman cites Citadel's purchase of a blown-up $30B hedge fund's book 'on pennies on the dollar' as the same dry-powder principle in action — whoever holds cash when a forced seller appears sets the terms.",
            "Tilman's broader thesis: AI/automation now make it possible to systematically harvest market volatility (an 'eighth wonder of the world' compounding effect) across many uncorrelated markets simultaneously, rather than relying on a single long-term appreciation bet.",
            "Gary pushes back that 'volatility is vitality' isn't true for most retail investors — for them, he argues, volatility is really just fear, and discipline (waiting for real pullbacks, not chasing) matters more than any systematic volatility strategy.",
        ],
        "quote": {"text": "He who has the gold makes the rules.", "cite": "— Tilman"},
        "watch": None,
        "names": [
            {"name": "Berkshire Hathaway (BRK.B)", "blurb": "Buffett stepping down as chairman after an estimated 6.6 million% tenure return; cash fell from $397B to $360B in the latest quarter.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "scarce-assets-vs-cheap-services",
        "tags": ["macro-rates", "crypto"],
        "color": "amber",
        "badge": "Contested",
        "status": "DISAGREEMENT — Gary and Tilman split on the inflation/deflation framing",
        "title": "Will Everything Get More Expensive — or Just Hard Assets?",
        "lead": "Tilman and Gary openly disagree on the next decade's inflation story: Tilman sees broad-based price increases from continued money-printing, while Gary sees services and access getting dramatically cheaper even as scarce hard assets hold their premium.",
        "bullets": [
            "Tilman's view: continued government money-printing to service debt with cheaper dollars means everything will be more expensive in 20 years, and Bitcoin should catch more of that inflation 'fever' than most assets since it has no cost of carry.",
            "Gary disagrees on the general claim, arguing the next 5-10 years will be deflationary for services and access — citing free access to an MIT-level education and direct access to high-profile people that used to require years of relationship-building.",
            "Both agree scarce hard assets are the exception: gold at $4,500 is delivering ~60% margins for producers, and oil at $150 a barrel would represent roughly a 300% return on production cost — both examples where rising prices pull in capital until competition compresses the trade.",
            "Gary frames shorting America itself as 'insane' given the scale of forthcoming reinvestment (public and possibly government-directed) into US corporates.",
        ],
        "quote": {"text": "Everything will be more expensive when we [look] in 20 years than it is now. Period. Everything.", "cite": "— Tilman"},
        "watch": "This is an explicit on-air disagreement between the two hosts, not a resolved consensus view.",
        "names": [
            {"name": "Gold", "blurb": "Cited as a scarce hard asset benefiting from the same dynamic as Bitcoin — trading at $4,500 with ~60% producer margins.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Silver", "blurb": "Grouped with gold as a scarce hard asset that benefits from continued money-printing.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Crypto", "title": "Don't chase Bitcoin above resistance — the hosts' own math favors waiting for a 15-20% pullback before adding"},
    {"icon": "\U0001F4B0", "tag": "Finance", "title": "Treat MicroStrategy/Strategy's preferred stock (STRC) as a yield-plus-optionality alternative to buying spot Bitcoin at elevated prices"},
    {"icon": "\U0001F3DB️", "tag": "Policy", "title": "Watch for a broader US sovereign-equity-stake pattern beyond Intel as an early but real policy signal"},
    {"icon": "\U0001F50D", "tag": "Crypto", "title": "Read issuer-level ETF flow data (like Morgan Stanley's record day), not just aggregate or IBIT headlines, for the clearest retail-demand signal"},
    {"icon": "\U0001F3B0", "tag": "Careers", "title": "Size positions so you're never 'scared money' at the table — risk management matters more than being right about direction"},
]

HOT_TAKES = [
    {"take": "No one should chase Bitcoin ever again. It is a lie. I am not going to buy $120,000 Bitcoin. I'm not doing it, dude. I'm going to wait for it to come back to me.", "cite": "— Gary Cardone", "why": "explicit, exposed refusal to buy at current-style highs from someone who trades the asset actively"},
    {"take": "I'm looking for a $17,000 pullback before I even think about something... we've gone up 40%. I want to see a 20% pullback.", "cite": "— Gary Cardone", "why": "specific numeric target that can be checked against what actually happens"},
    {"take": "We are 90% more likely to go back down to 75 than we are to go back up to 95.", "cite": "— Andrew", "why": "precise statistical claim staked publicly, easy to hold him to"},
    {"take": "Everybody wants to be James Win. No one wants to be Warren Buffett.", "cite": "— Gary Cardone", "why": "blunt dismissal of trading culture that plenty of the audience would push back on"},
    {"take": "[Old-school Bitcoiners rotating into Zcash] I just think it's incredibly naive, very childlike, very foolish.", "cite": "— Gary Cardone", "why": "directly dismisses a segment of his own audience's investment thesis"},
    {"take": "I think everything in the next 5 to 10 years is going to be extremely cheap.", "cite": "— Gary Cardone", "why": "direct, on-air disagreement with Tilman's inflation call, staked with concrete examples (free MIT-level education)"},
]

CLAIMS = [
    {"who": "Andrew", "claim": "Bitcoin ETFs see a run of large inflow days over the next couple of weeks", "metric": "ETF inflows", "target": "large", "by": "next 2 weeks", "condition": None, "entity": "Bitcoin (BTC)"},
    {"who": "Andrew", "claim": "Bitcoin outperforms broader markets but not by 4-5x over the next few years", "metric": "relative outperformance vs. broader markets", "target": "1.75x-1.95x, not 4-5x", "by": "3-5 years", "condition": None, "entity": "Bitcoin (BTC)"},
    {"who": "Andrew", "claim": "BlackRock's ETF and options structure caps how explosive a Bitcoin rally can get", "metric": "annual return", "target": "will not exceed 250% in a year", "by": "next 3 years", "condition": "given BlackRock's product and options structure", "entity": "Bitcoin (BTC)"},
    {"who": "Andrew", "claim": "After the recent 40%+ move, Bitcoin is far more likely to retrace than to continue rallying near-term", "metric": "retracement probability", "target": "~90% vs ~10%", "by": None, "condition": None, "entity": "Bitcoin (BTC)"},
    {"who": "Gary Cardone", "claim": "Will convert his STRC position to cash once it reaches his cost basis", "metric": "exit price", "target": "$99.50-$100", "by": None, "condition": None, "entity": "Strategy (MSTR)"},
    {"who": "Andrew", "claim": "Bitcoin is unlikely to revisit $75,000 in the near term", "metric": "price level", "target": "$75,000", "by": "next 90 days", "condition": "would be a surprise if it happened", "entity": "Bitcoin (BTC)"},
    {"who": "Tilman", "claim": "Roughly 1% of daily US equity trading volume represents a systematic 401k bid, and a similar dynamic will grow in Bitcoin", "metric": "systematic bid flow", "target": "~1% of daily volume", "by": "next 10 years", "condition": None, "entity": "Bitcoin (BTC)"},
]

RELATIONS = [
    {"from": "Trump administration", "rel": "owns_stake", "to": "Intel (INTC)", "note": "cited as the precedent for potential broader US government equity stakes in corporates"},
]

OTHER_NEWS = [
    {"icon": "\U0001F3AF", "title": "Andrew's company Arch Public is hosting a client event in Tampa on October 15 for its top concierge clients, built around its Bitcoin-accumulation and equity/ETF cash-flow algorithm products.", "tag": "Startups"},
]

GLOSSARY = [
    {"term": "STRC", "def": "Strategy's (formerly MicroStrategy) yield-bearing preferred stock, paying holders a fixed dividend (discussed here at 11.5%) while trading near its $100 par value."},
    {"term": "Dry powder", "def": "Cash held in reserve so an investor can act decisively when a high-quality entry opportunity appears, rather than being forced to sell into a bad market."},
    {"term": "VWAP", "def": "Volume-weighted average price — a benchmark used here to show how far above typical trading activity Bitcoin's recent move stood."},
    {"term": "HELOC", "def": "A home-equity line of credit — cited as the model for what Bitcoin-collateralized lending could look like once banks treat it as standard collateral."},
    {"term": "Cost basis", "def": "The average price an investor (or, here, an ETF's aggregate holder base) paid for an asset, used to gauge whether a position is currently in profit or loss."},
]
