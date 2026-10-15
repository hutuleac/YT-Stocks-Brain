META = {
    "title": "The Secret to Long-Term Investing with Raoul Pal",
    "channel": "Raoul Pal The Journey Man",
    "speakers": "Raoul Pal",
    "date": "2026-10-15",
    "video_url": "https://www.youtube.com/watch?v=nj-OAZ38ypQ",
    "thread_line": "6 threads · log-trend framework · macro and the dollar · volatility sizing · Tesla setup · ETH and SUI setups · thesis, bonds and track record",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Raoul Pal opens Real Vision's **Festival of Trading** with his own process: ride secular trends, size by volatility, and do as little as possible.",
    "Core tool is the **log regression channel**: buy Bitcoin or the Nasdaq at 1-1.5 standard deviations oversold, don't sell until ~2 SD overbought.",
    "Macro check says **full-cycle expansion**: ISM trending up, liquidity still rising, GMI \"macro season\" = summer.",
    "Worked setups: Tesla (45%/yr trend, ~1 SD oversold), Ethereum (2 SD oversold weekly, ~6:1 reward/risk), Sui (his riskier bet, wedge forming).",
    "He recently **shifted tech into crypto** because crypto hit 2 SD oversold versus the Nasdaq while the Nasdaq sits expensive versus trend.",
    "Bonds look like a crowded short with reversal risk, but he passes because they don't fit his debasement thesis.",
    "Claims a GMI record since 2005 with 65% winning trades; no leverage, stop-losses are ideas not prices, and trading the crypto cycle is \"net depletive\".",
]

THEMES = [
    {
        "id": "log-trend",
        "tags": ["crypto", "finance"],
        "color": "green",
        "badge": "Core method",
        "status": "HOW HE ALLOCATES — SECULAR TREND FIRST",
        "title": "The \"compounding machine\": log regression channels on Bitcoin and the Nasdaq",
        "lead": "Pick assets in long secular uptrends, then use how far they sit from their log trend to decide when to add and when to trim.",
        "bullets": [
            "Old hedge-fund process: 1-6 month setups, **risk budget** of ~3% of NAV per trade, total stops capped at a 10-15% monthly drawdown. He came to hate getting stopped out.",
            "Bitcoin buy signals at 1 and 1.5 SD oversold \"work really well\"; exits sit at up to 2 SD overbought so he stays with the trend.",
            "\"Not a trading indicator\": weekly and monthly versions, for major allocation calls only.",
            "**Build it yourself**: ask Claude or ChatGPT for a TradingView log-regression indicator in Pine Script.",
            "For people who want to trade the wiggles: the weekly **GMI trend** indicator on TradingView (green/red dots) shows the interim trend vs. the secular one.",
        ],
        "quote": {"text": "Log regression channels are your friend when it comes to secular trends.", "cite": "— Raoul Pal"},
        "watch": "The dashboards shown (compounding machine, risk monitor, trend indicator) are paid Real Vision / GMI products he runs.",
        "names": [
            {"name": "Bitcoin (BTC)", "blurb": "One of the two top-level secular trends; buy at 1-1.5 SD oversold on the log channel", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "long term"},
        ],
    },
    {
        "id": "macro-dollar",
        "tags": ["macro-rates"],
        "color": "green",
        "badge": "Confirmed backdrop",
        "status": "FULL-CYCLE EXPANSION — STAY LONG",
        "title": "ISM up, liquidity up, and a dollar that isn't moving",
        "lead": "The macro backdrop says the book should be long, and a quiet dollar lets the trends run.",
        "bullets": [
            "Risk monitor: ISM trending above its signal and liquidity still rising, so a **full-cycle expansion**.",
            "ISM ≈ the year-on-year rate of change of any asset class, \"hugely correlated\" since 1947.",
            "GMI macro season is **summer**: favours cyclicals, industrial commodities, emerging markets, and crypto.",
            "The 2025-26 crypto down cycle was crypto-specific liquidity flows, not an overall liquidity cycle; he still sees the full long-term cycle intact.",
            "Turned **dollar bull in 2011**: moved his life savings into dollars, billed GMI in dollars while living in Spain, bought a house in the Cayman Islands.",
            "Now: monthly DeMark 9s and 13s at the top point to an interim weaker dollar inside a longer-term stronger trend. A sharp dollar move either way is the warning sign.",
        ],
        "quote": {"text": "Liquidity is generally driven by the dollar.", "cite": "— Raoul Pal"},
        "watch": None,
        "names": None,
    },
    {
        "id": "volatility",
        "tags": ["crypto", "finance"],
        "color": "amber",
        "badge": "Risk management",
        "status": "SIZE BY VOLATILITY, NOT CONVICTION",
        "title": "Volatility is the sizing tool most people forget",
        "lead": "An 85%-volatility small cap or small crypto can take you down 70-80% before you notice, so position size has to follow volatility.",
        "bullets": [
            "Nasdaq 100 runs at a \"normal\" 16% volatility; Solana at 59%.",
            "Bitcoin is more volatile than the S&P 500, so it gets a smaller weight unless you deliberately overweight it.",
            "Diversification helps less than people think: everything goes risk-on/risk-off together because **liquidity** drives it.",
            "Expect drawdowns of 30-40% in crypto and ~15% in the Nasdaq even inside secular uptrends.",
            "Keep some **cash** for dislocations, which come about once a year; he added in the \"Crypto 10/10\" crash and over the summer.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Solana (SOL)", "blurb": "Example of a high-volatility asset (59%)", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "tesla",
        "tags": ["consumer", "robotics"],
        "color": "amber",
        "badge": "Setup forming",
        "status": "WEEKLY TREND NEGATIVE — WAITING FOR GREEN DOTS",
        "title": "Tesla: a 45%-a-year trend, one standard deviation oversold, building a base",
        "lead": "Tesla's log trend compounds at ~45% a year since 2010-11, and it is sitting just over 1 SD oversold inside a large consolidation.",
        "bullets": [
            "45% a year trend return, with ~45% volatility now and more at times.",
            "Large consolidation pattern, similar to ETH's; he prefers buying the bottom of the pattern over the breakout.",
            "Weekly GMI trend is **negative** (red dots); the cautious entry is waiting for green dots.",
            "Weekly DeMark 13s show selling exhaustion; on the daily a 13 up top suggests one more dip before \"finally making the move\".",
            "A weekly break through **508** would signal the acceleration phase.",
            "Monthly DeMark down counts rarely appear in Tesla: at 45% a year \"nothing here to see\" unless something is really changing.",
        ],
        "quote": None,
        "watch": "He walks through Tesla as a worked example and never says whether he holds it.",
        "names": [
            {"name": "Tesla (TSLA)", "blurb": "Worked example: 45%/yr log trend, ~1 SD oversold, 508 is the acceleration level", "stance": "WATCHING", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "eth-sui",
        "tags": ["crypto"],
        "color": "green",
        "badge": "High conviction",
        "status": "HOLDING SUI — ETH AT 2 SD OVERSOLD",
        "title": "Ethereum and Sui: skewed reward/risk inside wedge patterns",
        "lead": "Ethereum is 2 SD oversold against its weekly trend with roughly 6:1 reward/risk, and Sui is his riskier bet with a wedge breakout as the prize.",
        "bullets": [
            "ETH log trend: implied 76% CAGR from inception, 49% from 2017; somewhere \"between 75 and 50%\" a year. Monthly 13 low and a wedge pattern.",
            "Illustrative, \"not a prediction\": 2 SD overbought by July 2028 implies ~$60,000 ETH; a 1 SD top in Q2 2027 implies ~$18,000, which he calls reasonable.",
            "ETH risk/reward: stop ~1,500 (trend line ~1,600) vs. price ~2,700, so ~50% downside against ~300% upside.",
            "Weekly DeMark levels getting **blown through** rather than rejecting price is his sign of a trend change with strength.",
            "Sui: rising lows, weekly 13 then acceleration, early green dots, monthly 9. Stop ~60 cents vs. ~$1, range top a bit over $2.",
            "His SUI position was down **80%** from its high and underwater from his entry; it didn't worry him.",
        ],
        "quote": {"text": "Could it go to 10 bucks, 15 bucks, 20 bucks? Who knows, right? It's crypto.", "cite": "— Raoul Pal"},
        "watch": "The ETH price paths are explicitly scenarios, not forecasts. Sui is too young for a proven long-term buy-and-hold record.",
        "names": [
            {"name": "Ethereum (ETH)", "blurb": "2 SD oversold weekly, ~6:1 reward/risk, $18k (1 SD) / $60k (2 SD) scenarios", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "Q2 2027 to July 2028 scenarios"},
            {"name": "Sui (SUI)", "blurb": "\"The riskier bet that I've got\"; wedge pattern, 60c stop, $10-20 if the wedge breaks", "stance": "OWNS", "conviction": "High", "horizon": None},
        ],
    },
    {
        "id": "thesis-record",
        "tags": ["crypto", "finance", "macro-rates"],
        "color": "green",
        "badge": "High conviction",
        "status": "CONCENTRATED IN TECH + CRYPTO, NO LEVERAGE",
        "title": "Tech and crypto beat debasement, so he concentrates and does nothing",
        "lead": "His thesis is that technology and crypto outperform currency debasement through adoption, and their returns are so high that allocating elsewhere isn't worth it.",
        "bullets": [
            "He can stomach 50-60% drawdowns because he has income and savings he doesn't rely on; he says others need a setup that fits them.",
            "**Recent move**: reallocated tech into crypto after crypto hit 2 SD oversold vs. the Nasdaq.",
            "Bonds: after a massive rise in rates, positioning is record short. Higher rates need a big inflation or GDP jump, so the risk is a reversal. He **passes** because bonds don't fit his thesis, and will benefit from falling rates elsewhere in the book.",
            "Stop-losses are an idea, not a price (\"something changed with the economy\"); he still recommends price stops for most people.",
            "Facebook got 3 SD oversold in 2022; he judged the business model wasn't broken. Breaking a log channel demands that homework.",
            "GMI record since 2005, every trade logged: 65% winners, several 100%+ years. Bad years: 2009 (short-term trading) and 2022, when he kept core positions and added tech and crypto at 2 SD oversold in Nov-Dec 2022.",
            "Trading in and out of the crypto cycle is \"net depletive\"; no leverage, despite heavy leverage in his hedge-fund days.",
        ],
        "quote": {"text": "We blessed with the greatest trends in the history of markets.", "cite": "— Raoul Pal"},
        "watch": "The track-record figures are his own claim about GMI, the newsletter he sells, made while promoting Real Vision's Festival of Trading.",
        "names": [
            {"name": "Facebook (META)", "blurb": "2022 example: 3 SD oversold, business model judged intact", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C8", "tag": "Markets", "title": "Put a log regression channel on every long-term holding and only add size at 1-1.5 SD oversold."},
    {"icon": "⚖️", "tag": "Risk", "title": "Check each position's volatility before sizing it; cut size on anything running at 50%+ vol unless you understand its drawdowns."},
    {"icon": "\U0001F4B5", "tag": "Macro", "title": "Watch the dollar: a quiet dollar lets trends run, a sharp move either way is the cue to get nervous."},
    {"icon": "\U0001FA99", "tag": "Crypto", "title": "Compare crypto against the Nasdaq on its own trend channel to decide when to rotate between them."},
    {"icon": "\U0001F4B0", "tag": "Portfolio", "title": "Hold some cash back for the roughly once-a-year dislocation instead of trying to time cycle tops."},
]

HOT_TAKES = [
    {"take": "It's always intellectually interesting to fade everybody else, but really it's the bulls make money because you don't have to do anything.", "cite": "— Raoul Pal", "why": "dismisses contrarian trading"},
    {"take": "Because of their rates of return are so high versus other assets, it's not worth me allocating capital elsewhere.", "cite": "— Raoul Pal", "why": "all-in on tech + crypto"},
    {"take": "I've got a recorded track record in GMI that's, I think, without question the best track record of any research publication that exists.", "cite": "— Raoul Pal", "why": "self-ranking claim"},
    {"take": "It is literally impossible to buy the bottom in full size that you took off somewhere near the high.", "cite": "— Raoul Pal", "why": "against trading the crypto cycle"},
    {"take": "I found over time it's net depletive.", "cite": "— Raoul Pal", "why": "on trading in and out of risk with the weekly trend"},
    {"take": "My stop losses tends to be an idea, not a price any longer.", "cite": "— Raoul Pal", "why": "rejects mechanical stops for himself"},
]

CLAIMS = [
    {"who": "Raoul Pal", "claim": "Ethereum reaches about $18,000 if it tops at one standard deviation overbought in Q2 2027, which he calls reasonable", "metric": "ETH price", "target": "$18,000", "by": "2027-06", "condition": "if ETH tops at 1 SD overbought on its weekly log trend", "entity": "Ethereum (ETH)"},
    {"who": "Raoul Pal", "claim": "Ethereum at two standard deviations overbought by July 2028 would be about $60,000 (illustrative, not a prediction)", "metric": "ETH price", "target": "$60,000", "by": "2028-07", "condition": "if ETH reaches 2 SD overbought on its weekly log trend", "entity": "Ethereum (ETH)"},
    {"who": "Raoul Pal", "claim": "Sui could run to $10-20 if it breaks out of its wedge pattern", "metric": "SUI price", "target": "$10-20", "by": None, "condition": "if the wedge pattern breaks", "entity": "Sui (SUI)"},
    {"who": "Raoul Pal", "claim": "A weekly break through 508 would put Tesla in its acceleration phase", "metric": "TSLA weekly price level", "target": "508 breakout", "by": None, "condition": "if weekly closes go through 508", "entity": "Tesla (TSLA)"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: Tom DeMark (DeMark indicators, his own Real Vision Academy series), Peter Brandt (classical charting series), TradingView, and Claude / ChatGPT for writing Pine Script.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Log regression channel", "def": "A trend line fitted to the log of price, with standard-deviation bands showing how stretched an asset is versus its long-run trend."},
    {"term": "CAGR", "def": "Compound annual growth rate; here the yearly return implied by the slope of the log trend."},
    {"term": "DeMark 9 / 13", "def": "Tom DeMark's sequential counts that flag likely trend exhaustion and reversal points."},
    {"term": "Risk budget", "def": "The share of NAV you accept losing across all stop-losses combined, e.g. 3% per trade, 10-15% per month in total."},
    {"term": "ISM", "def": "The US manufacturing survey Pal uses as his business-cycle gauge."},
    {"term": "GMI macro seasons", "def": "Global Macro Investor's map of business-cycle and liquidity phases to the asset classes that historically do best in each."},
]
