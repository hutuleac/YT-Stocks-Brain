"""
Per-video data for youtube-research-brief.
"""

META = {
    "title": "Agentic AI Stocks to Buy! HOLY ROCKETSHIP",
    "channel": "Meet Kevin",
    "speakers": "Kevin Paffrath",
    "date": "2026-09-22",
    "video_url": "https://www.youtube.com/watch?v=r8pa1nIhprg",
    "thread_line": "5 threads: Meta's Muse app rockets to #1, Nvidia invades AMD's CPU turf, AMD looks overbought next to Nvidia, Intel/ARM ride the same CPU shift, and the 'stranded RAM' bull case for memory",
    "category": "market",
}

SNAPSHOT = [
    "Meta jumped **11.4%** and AMD jumped **9.95%** (crossing a $1T market cap) in the same session, both driven by agentic-AI enthusiasm.",
    "Meta's new Muse agent app hit #1 on the App Store free chart, passing ChatGPT (#2); Gemini sits at #8, Claude at #16.",
    "Nvidia is projecting **$20B** of CPU demand in 2026 alone — a business it had almost no revenue in a year ago — and is targeting 50% of the CPU TAM by 2030.",
    "AMD looks overbought (RSI ~73 daily) and priced richer than Nvidia on a PEG basis (~1.5-1.6x vs ~0.7-1.0x) despite far thinner margins.",
    "AMD gave Meta and OpenAI stock warrants at **$0.01/share** in exchange for multi-gigawatt chip-purchase commitments — a dilutive echo of Nvidia's own direct-investment ('circular financing') strategy with its customers.",
    "Intel is showing real pricing power: data center/AI revenue up **59%** YoY on only 9% more units shipped, amid a severe server-CPU supply shortage.",
    "A new bull case for memory: agentic AI can fill previously unused ('stranded') VRAM with parallel agent sessions, adding to already-tight DRAM/HBM supply.",
    "Kevin's price targets: Meta $1,800, Nvidia $600+ (first $10T company), AMD ~$944 — but he says he wouldn't add to AMD at current levels.",
]

THEMES = [
    {
        "id": "meta-muse-ads",
        "tags": ["ai-infra", "consumer"],
        "color": "green",
        "badge": "High conviction",
        "status": "HOLDING — Meta call made Aug 28 at $566, target raised to $1,800",
        "title": "Meta's Muse App Rockets to #1, Feeding an Ad-Stock Thesis",
        "lead": "Meta's new Muse agent app jumped past ChatGPT to the top of the App Store free charts, and Kevin argues agentic AI is quietly a bull case for advertising platforms, not just chipmakers.",
        "bullets": [
            "Muse launched September 8 and is now the #1 free app in the App Store, ahead of ChatGPT (#2); Gemini ranks #8, Claude (Anthropic) #16, Instagram #18.",
            "**Amazon** is now banning MetaMuse from crawling its site — as agents do more product browsing for users, fewer human eyeballs hit those pages, which Kevin says raises the value of app-store and platform advertising instead.",
            "Meta broke through 700 this week (hit 741), still has **$15B** of free cash flow and over 4 gigawatts of compute; its next Frontier LLM ('watermelon') is expected next month.",
            "Kevin's Meta call was made August 28 at ~$566 anticipating a breakout; next chart level flagged at 826.",
            "Other ad-platform beneficiaries he names in passing: Google and Netflix, plus Apple and Google as app-store gatekeepers.",
        ],
        "quote": {"text": "The more agents browse products for you, the less human eyeballs are on them.", "cite": "— Kevin"},
        "watch": None,
        "names": [
            {"name": "Meta (META)", "blurb": "Muse app hit #1 free in the App Store; Kevin holds a large position and raised his target to $1,800.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "Banned MetaMuse from crawling its site to protect product-page traffic.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
            {"name": "Google (GOOGL)", "blurb": "Gemini competing in the agent-app rankings; also named as an ad-platform beneficiary of the agent shift.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
            {"name": "Netflix", "blurb": "Named as an ad-platform beneficiary wherever human eyeballs still concentrate.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "nvidia-cpu-invasion",
        "tags": ["ai-infra", "semis"],
        "color": "amber",
        "badge": "Contested",
        "status": "DEVELOPING — Nvidia guiding $20B CPU demand for 2026",
        "title": "Nvidia Is Coming for AMD's CPU Turf",
        "lead": "Nvidia is projecting $20 billion of CPU demand in 2026 alone — nearly six months of AMD's total revenue — from a business it had almost no presence in a year ago.",
        "bullets": [
            "Since around March, workloads have been shifting toward CPUs because agentic AI (like Muse) runs efficiently there, unlike GPU-heavy training/chat workloads.",
            "Nvidia's **$20B** projected CPU demand for 2026 would rival roughly three quarters of AMD's entire gross profit, and is about 6 months of AMD's total revenue.",
            "Nvidia is targeting **50%** of the CPU TAM by 2030, up from the high-30s% today.",
            "AMD's Epyc Turin (5th-gen) chip is currently projected to reach ~50% of CPU TAM; it's x86, so it avoids ARM licensing fees.",
            "Benchmark trade-off: AMD's Helios rack system has 50% more high-bandwidth memory and scale-out bandwidth than Nvidia's Vera Rubin, and 10-15% more tokens/sec — but AMD's newer Venice chip claims 2.8x more agents-per-watt vs Vera (a newer-vs-older comparison, per Kevin).",
            "Supply commitments through ~2031: AMD has locked ~$30B (wafers/substrates/components) vs Nvidia's $334B in the same window — Nvidia has 11x AMD's committed supply while being only 5x its market cap.",
        ],
        "quote": None,
        "watch": "The Helios-vs-Vera-Rubin and Venice-vs-Vera benchmark comparisons mix chip generations (newer AMD product vs an older Nvidia chip) — Kevin flags this himself rather than treating it as apples-to-apples.",
        "names": None,
    },
    {
        "id": "amd-vs-nvidia-valuation",
        "tags": ["semis", "finance"],
        "color": "amber",
        "badge": "Contested",
        "status": "AMD overbought — RSI ~73 daily, ~70 weekly",
        "title": "AMD Looks Overbought and Overpriced Next to Nvidia",
        "lead": "AMD's margins have improved sharply but Nvidia is still dramatically more profitable, cheaper on a growth-adjusted basis, and better funded to lock in supply and customers.",
        "bullets": [
            "AMD gross margin climbed from 39.8% to **53.7%**, with 17.2% net margin (just out of a loss); Nvidia sits at 75% gross and 63% net.",
            "Operating income: AMD ~$2B in three months vs Nvidia ~$63B — roughly 30x.",
            "Valuation: AMD trades near a 1.5-1.6 PEG ratio vs Nvidia's ~0.7-1.0 — AMD is more than **2x** as expensive on a growth-adjusted basis.",
            "AMD gave Meta and OpenAI warrants to buy AMD shares at **$0.01/share** (exercisable for Meta through Feb 23, 2031, and OpenAI through Oct 5, 2030) in exchange for ~6 gigawatts of chip purchases — dilutive, and Kevin calls it a cash-poor version of what Nvidia does.",
            "Nvidia's own version: $42B of equity and $21B of debt purchased in other companies in six months, funded by $70B of free cash flow over that period — vs AMD's $4B FCF in six months (Nvidia ~17.5x richer on cash flow).",
            "Kevin's price targets: Nvidia $600+ (would make it the first $10T company) vs AMD ~$944 (current $747, ~82x current-year earnings against ~55% growth); he says he would **not add to AMD** at current levels — 'a little toasty and a little euphoric.'",
        ],
        "quote": None,
        "watch": "Kevin discloses he holds exposure to most of the names discussed here (Meta, AMD, Nvidia, Intel) and says he isn't short anything — a standing bias he states directly rather than hides.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Far cheaper than AMD on PEG despite better margins and cash flow; target $600+, potential first $10T company.", "stance": "OWNS", "conviction": "High", "horizon": None},
            {"name": "AMD (AMD)", "blurb": "Already holds a position but says he wouldn't add more here given overbought RSI and a richer PEG than Nvidia; target ~$944, ~50% implied upside.", "stance": "WATCHING", "conviction": "Medium", "horizon": "near-term"},
            {"name": "OpenAI", "blurb": "Received AMD warrants at $0.01/share tied to chip-purchase commitments, exercisable through Oct 5, 2030.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "intel-arm-pricing-power",
        "tags": ["semis", "ai-infra"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "Intel +12% and ARM +17% same session",
        "title": "Intel's Pricing Power and the ARM Land-Grab",
        "lead": "Severe server-CPU shortages are letting Intel raise prices even on consumer chips, while ARM licensing is quietly riding the same CPU shift through Apple, Google, Amazon, and Microsoft's own silicon.",
        "bullets": [
            "Intel data center/AI revenue rose **59%** YoY in Q2 2026 on only 9% more units shipped — implying ~48% pricing power; stock closed +12% (intraday +14%) that day.",
            "Intel's CEO cites a severe server CPU shortage, with existing capacity meeting only 50% of demand; Intel is raising PC CPU prices ~10%, with bigger increases planned for data-center chips.",
            "Intel is projected to double CPU sales between 2026 and 2027.",
            "ARM currently sits at ~17-18% of CPU TAM and is projected to grow to 40-50%, competing directly with x86 (AMD/Intel); ARM stock was up **17%** the same day.",
            "ARM-based chips now span the industry: Apple and Nvidia license ARM, Google has its own Axion chip, AWS has Graviton, and Microsoft has Cobalt.",
            "OpenAI reportedly bought tens of thousands of Apple Mac Studios and Mac minis for agentic AI compute, another line of ARM-adjacent demand.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "Intel (INTC)", "blurb": "Showing real pricing power amid a severe server CPU shortage; projected to double CPU sales 2026-2027.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": "2026-2027"},
            {"name": "ARM", "blurb": "Growing from ~17-18% to a projected 40-50% of CPU TAM as the architecture behind Apple, Nvidia, Google Axion, AWS Graviton, and Microsoft Cobalt.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "ARM licensee and CPU-shift beneficiary, plus an app-store ad beneficiary — but Kevin calls the stock 'a little pricey' and doesn't own it.", "stance": "WATCHING", "conviction": "Low", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Cobalt is its own ARM-based chip, part of the same architecture shift.", "stance": "CASUAL MENTION", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "stranded-ram-memory",
        "tags": ["ai-infra", "semis"],
        "color": "gray",
        "badge": "Speculative",
        "status": "UNSETTLED — Kevin explicitly torn on memory names",
        "title": "The 'Stranded RAM' Case for Memory Stocks",
        "lead": "Agentic AI may finally put idle VRAM capacity to work by running many parallel agent sessions on chips that were previously loading a model but not using all their memory.",
        "bullets": [
            "Most current chat workloads don't fill a chip's full VRAM (Kevin uses a hypothetical ~228GB Rubin-class chip) once the model and typical context are loaded, leaving 'stranded' unused capacity.",
            "Agentic AI can fill that stranded capacity by running several parallel agent sessions off one loaded model — a new source of demand for high-bandwidth memory (Micron, SK Hynix).",
            "DRAM prices are up ~95% in Q1 2026 and still rising; growth is expected to peak by the end of 2027 as more supply comes online.",
            "All three DRAM makers are reportedly sold out of high-bandwidth memory; SK Hynix's added capacity isn't expected online until 2028-2029.",
        ],
        "quote": None,
        "watch": "Kevin is explicitly more uncertain here than on the chip names — he says he's 'a little bit more torn' on memory stocks and doesn't stake a clear position.",
        "names": [
            {"name": "Micron (MU)", "blurb": "HBM beneficiary of the 'stranded RAM' agentic-AI bull case, but Kevin says he's undecided on the stock.", "stance": "UNCERTAIN", "conviction": None, "horizon": None},
            {"name": "SK Hynix", "blurb": "Sold out of high-bandwidth memory; new capacity doesn't come online until 2028-2029.", "stance": "UNCERTAIN", "conviction": None, "horizon": None},
        ],
    },
    {
        "id": "next-wave-plays",
        "tags": ["robotics", "semis"],
        "color": "gray",
        "badge": "Speculative",
        "status": "WATCHING — small/no positions disclosed",
        "title": "Next Up: Broadcom, Cerebras, and Robotics",
        "lead": "Beyond the AMD/Nvidia/Intel trio, Kevin flags Broadcom and Cerebras as the next names to watch, and robotics as the next theme past agentic AI.",
        "bullets": [
            "Broadcom is back at the '355 line' — Kevin doesn't own it but calls it 'the next boomer.'",
            "Cerebras has hit a floor in his view; he holds a small, DCA'd position and considers it a buy under ~$250.",
            "Robotics is framed as the next opportunity past agents, with Cerebras and Nvidia named as the two big robotics plays.",
            "Most ASIC designers in this space (unnamed individually beyond Broadcom) rely on TSMC to manufacture.",
        ],
        "quote": None,
        "watch": "Kevin explicitly does not own Broadcom and holds only a small Cerebras position — his conviction sizing here is much lower than for Meta, AMD, or Nvidia.",
        "names": [
            {"name": "Broadcom (AVGO)", "blurb": "Back at the 355 level; flagged as the next name to watch, not currently owned.", "stance": "WATCHING", "conviction": "Medium", "horizon": "near-term"},
            {"name": "Cerebras", "blurb": "Small DCA position; considers it a buy under $250 and one of the two big robotics plays alongside Nvidia.", "stance": "BUYING-ADDING", "conviction": "Low", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F3AF", "tag": "Markets", "title": "Don't chase AMD at these levels — it's overbought (RSI ~73 daily) and pricier than Nvidia on a PEG basis"},
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Track Nvidia's CPU push as a real threat to AMD/Intel, not a footnote — $20B guide for 2026, 50% TAM target by 2030"},
    {"icon": "\U0001F4F1", "tag": "Markets", "title": "Watch the ARM beneficiaries (Apple, Google Axion, AWS Graviton, Microsoft Cobalt), not just AMD/Intel's x86 fight"},
    {"icon": "\U0001F9E9", "tag": "Markets", "title": "Hold off on conviction in memory names until HBM supply clarity improves — even Kevin is undecided here"},
    {"icon": "\U0001F916", "tag": "Robotics", "title": "Size Cerebras and Broadcom as small, speculative positions, not core holdings, per Kevin's own disclosed sizing"},
]

HOT_TAKES = [
    {"take": "I would not add to AMD at this place. It could keep going. It just right now it feels a little toasty and a little euphoric.", "cite": "— Kevin", "why": "explicit near-term caution on a stock he already owns and just spent the whole video bullish on"},
    {"take": "This is an $1,800 stock.", "cite": "— Kevin (on Meta)", "why": "specific dated-feeling price target, more than double Meta's price at the time"},
    {"take": "Nvidia is expecting to blow up their CPU competition for a pure play... like AMD.", "cite": "— Kevin", "why": "contrarian framing of Nvidia as an AMD-killer rather than a pure GPU story"},
    {"take": "The ultimate winner is the ones selling the chipsets... and that seems to be AMD and Nvidia at the moment.", "cite": "— Kevin", "why": "dismisses the app/model layer (Muse, ChatGPT, Gemini) in favor of a hardware-only thesis"},
    {"take": "Robotics, you want Cerebras and you want Nvidia. Those are your big robotics plays.", "cite": "— Kevin", "why": "specific two-name call in a space he's only lightly positioned in (small Cerebras)"},
]

CLAIMS = [
    {"who": "Kevin", "claim": "Nvidia's CPU demand reaches $20B in calendar year 2026", "metric": "CPU demand", "target": "$20B", "by": "2026", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Kevin", "claim": "AMD revenue grows 72% next year to reach $88B for the full year", "metric": "revenue growth", "target": "72% / $88B", "by": "next year", "condition": None, "entity": "AMD (AMD)"},
    {"who": "Kevin", "claim": "Nvidia reaches 50% of the CPU TAM", "metric": "CPU TAM share", "target": "50%", "by": "2030", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Kevin", "claim": "Meta price target", "metric": "price target", "target": "$1,800", "by": None, "condition": None, "entity": "Meta (META)"},
    {"who": "Kevin", "claim": "AMD price target based on PEG-adjusted upside", "metric": "price target", "target": "$944", "by": None, "condition": None, "entity": "AMD (AMD)"},
    {"who": "Kevin", "claim": "Nvidia becomes the first $10 trillion market cap company", "metric": "market cap", "target": "$10T", "by": None, "condition": "if it reaches $600+/share", "entity": "Nvidia (NVDA)"},
    {"who": "Intel CEO", "claim": "Intel raises PC CPU prices and data-center CPU prices further still", "metric": "price increase", "target": "~10% (PC), more for data center", "by": None, "condition": "due to a severe server CPU supply shortage", "entity": "Intel (INTC)"},
    {"who": "Kevin", "claim": "DRAM pricing growth peaks", "metric": "DRAM price growth", "target": "peak", "by": "end of 2027", "condition": "as more supply comes online", "entity": None},
    {"who": "Kevin", "claim": "ARM grows its share of the CPU TAM", "metric": "CPU TAM share", "target": "40-50%", "by": None, "condition": None, "entity": "ARM"},
]

RELATIONS = [
    {"from": "AMD (AMD)", "rel": "supplies", "to": "Meta (META)", "note": "warrants to buy AMD at $0.01/share, exercisable through Feb 23, 2031, tied to a multi-gigawatt chip purchase commitment"},
    {"from": "AMD (AMD)", "rel": "supplies", "to": "OpenAI", "note": "warrants to buy AMD at $0.01/share, exercisable through Oct 5, 2030, tied to a chip purchase commitment"},
    {"from": "Nvidia (NVDA)", "rel": "invests_in", "to": "AI/data-center customers", "note": "$42B of equity and $21B of debt purchased in six months ending July 2026, funded by $70B of free cash flow"},
    {"from": "Amazon (AMZN)", "rel": "criticizes", "to": "Meta (META)", "note": "banned the MetaMuse app from crawling Amazon's site"},
    {"from": "AMD (AMD)", "rel": "acquires", "to": "ZT Group", "note": "general-purpose compute infrastructure for hyperscale data center customers"},
    {"from": "OpenAI", "rel": "customer_of", "to": "Apple (AAPL)", "note": "bought tens of thousands of Mac Studios and Mac minis for agentic AI compute"},
    {"from": "ARM", "rel": "competes_with", "to": "AMD (AMD)", "note": "ARM architecture vs x86 in the race for CPU TAM share"},
]

OTHER_NEWS = [
    {"icon": "\U0001F680", "title": "SpaceX was down about 1% the same day Meta rallied hard — Kevin reads it as rotation/horse-race dynamics ('everybody's going to Metamuse'), not a real fundamental read-through.", "tag": "Markets"},
    {"icon": "⚠️", "title": "Kevin reiterates he's buying the dip because he sees no current signs of his previously-flagged 'two paths to recession' — but says to stay watchful for when that changes.", "tag": "Macro"},
]

GLOSSARY = [
    {"term": "Stranded RAM", "def": "Unused VRAM/DRAM capacity left over after a model's weights and typical context window are loaded — agentic AI's parallel sessions can fill it, a new bull case for memory chips."},
    {"term": "PEG ratio", "def": "A stock's P/E ratio divided by its expected growth rate, used here to argue AMD is priced richer than Nvidia despite Nvidia's much larger market cap."},
    {"term": "Warrants (call options)", "def": "Rights AMD gave Meta and OpenAI to buy AMD shares at $0.01 each, in exchange for chip-purchase commitments — dilutive to existing AMD shareholders if exercised."},
    {"term": "CPU TAM", "def": "Total addressable market for CPUs in data centers — the pool Nvidia, AMD, Intel, and ARM licensees are now all competing to capture."},
    {"term": "Circular financing", "def": "A vendor investing in or extending credit to its own customers, who then use that money to buy the vendor's product — cited for both Nvidia's direct equity/debt purchases and AMD's warrant deals."},
]
