"""Data file for George Buhnici (Curiosity 335) — China leads in AI, Apple sues OpenAI, the price per kWh, 1-gigabit Starlink.
Romanian-language video: brief in English, quotes and hot takes verbatim in Romanian (no diacritics)."""

META = {
    "title": "China Lider la AI, Apple da in judecata OpenAI, Pretul la KWh, Starlink de 1 Gigabit #CURIOSITY 335",
    "channel": "George Buhnici",
    "speakers": "George Buhnici (host), Radu (co-host)",
    "date": "2026-07-18",
    "video_url": "https://www.youtube.com/watch?v=UBdx_0BfpZ4",
    "thread_line": "6 threads · Kimi K3 beats Fable 5 and GPT-5.6 on benchmarks, the xAI/Grok data-collection scandal, Apple suing OpenAI over trade secrets, energy and data centers in Romania, rising RAM prices plus Samsung leaks, and a record Microsoft Patch Tuesday.",
    "category": "market",
    "region": "ro",
}

SNAPSHOT = [
    "George Buhnici makes a risky call (flagged as such) that US tech stocks will open lower after the launch of Kimi K3, a Chinese model from Moonshot AI that beats both Fable 5 (Anthropic) and GPT-5.6 on benchmarks at a similar or lower price.",
    "xAI (Grok) is caught aggressively collecting data from users' repositories (a documented case where a developer found his entire codebase in an xAI Google Drive bucket) — xAI responded with a free opt-out, but only on enterprise plans.",
    "Apple sues OpenAI for trade-secret theft, alleging among other things that its former hardware VP, now OpenAI's hardware chief, asked candidates to bring real Apple equipment to get hired — tension heightened by the Jony Ive-Sam Altman AI hardware partnership.",
    "Nvidia is in advanced talks with the Romanian state about data-center investment, but Buhnici stresses Romania lacks the stable, cheap power required — especially with Cernavoda's reactor 1 entering refurbishment and reactors 3-4 still unbuilt.",
    "RAM prices keep rising (an estimated 13-18% in Q3 after +60% in Q2), with an HBM (high bandwidth memory) shortage forecast through 2027; first specs for the Samsung Galaxy Z Fold 8 and Z Fold 8 Ultra are circulating.",
    "Microsoft had its largest Patch Tuesday on record (570 vulnerabilities, two zero-days already exploited), and Accenture lost 35GB of code and keys — amid a broader wave of AI-assisted cyberattacks (including ransomware-as-a-service like Jade Puffer).",
    "SpaceX scrubbed the Starship v3 test flight at T-0 (Raptor engines failed to start), a flight meant to launch the first terabit-class Starlink V3 satellites (10x the previous generation's capacity, theoretical latency down to 5ms).",
]

THEMES = [
    {
        "id": "kimi-k3-frontier",
        "tags": ["ai-infra", "geopolitics"],
        "color": "red",
        "badge": "Confirmed event, uncertain impact",
        "status": "WATCH — Buhnici made a risky market call",
        "title": "Kimi K3 Beats Fable 5 and GPT-5.6 — Chinese Labs Reach Price and Performance Parity",
        "lead": "**Buhnici opens with a risky call, flagged as such:** the overnight launch of Kimi K3 (Moonshot AI) will shake up how US labs price their AI models.",
        "bullets": [
            "Kimi K3 (2.8 trillion parameters, 1-million-token context window) shows up on the Arena AI leaderboard tens of points above Fable 5 (Anthropic) and GPT-5.6 on extra high, plus above GLM 5.2 — on subscriptions somewhat cheaper than Anthropic's.",
            "Radu tempers the hype: the real gap is about 40-50 points out of 1,600+, proportionally smaller than the chart suggests — \"like braking distance, 54m versus 56m,\" not a crushing lead.",
            "xAI's Grok 4.5 is now available on Romanian IPs (it was US-only), and Buhnici declares it his new default model for an open-code agent, just $1 more per million tokens than Sonnet.",
            "Chinese labs already cover 80% of the efficient open-source model market, and Moonshot AI said it will publish Kimi K3's weights by month-end, allowing it to run on your own hardware.",
            "Buhnici speculates (flagged as speculation) that part of Chinese models' performance may come from distillation — training on US models' answers obtained through bulk-bought subscriptions or a third party (returning to an earlier discussion of SK Telecom and Project Glasswing).",
            "Official context for Fable's temporary withdrawal last month: the US government reportedly warned that access to the model was being exploited by a Chinese competitor, prompting an export ban before it returned to Anthropic subscriptions on July 18.",
        ],
        "quote": {"text": "Cred ca stirea asta o sa schimbe radical felul in care companiile americane fac pricing-ul si abonamentele la modelele de inteligenta artificiala.", "cite": "— George Buhnici"},
        "watch": "Buhnici explicitly labels the market call \"risky\" and asks to be checked on it later — a declared bet, not a certainty.",
        "names": [
            {"name": "Anthropic", "blurb": "Fable 5 beaten on benchmarks by Kimi K3; back in subscriptions on July 18 after a temporary withdrawal tied to a security incident.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "xai-data-collection",
        "tags": ["ai-infra", "policy"],
        "color": "red",
        "badge": "Confirmed privacy risk",
        "status": "WATCH — opt-out only on enterprise plans",
        "title": "xAI Aggressively Collects Grok Users' Data — Opt-Out Only on Enterprise Plans",
        "lead": "**A publicly documented case showed xAI copying far more data than needed** from a repository connected to Grok, raising a broader question about what happens to data uploaded to any free or even paid AI service.",
        "bullets": [
            "A developer (called \"Cyber Satoshi\" in the discussion) found while working with Grok that his whole code database had been copied into an xAI Google Drive bucket, though the task needed only ~115-120KB of context.",
            "xAI publicly said it offers opt-out and zero data retention (ZDR), but Buhnici and Radu note the free opt-out only works on enterprise plans — on free and Pro plans, everything you enter stays on their servers.",
            "Buhnici's general rule: \"when it's free, you're the product\" — and it applies just as much to paid Pro/business plans, whose privacy clauses allow partial data retention to improve the service.",
            "Radu adds a less discussed angle: even on enterprise ZDR, some information still flows back to the provider, as far as legally allowed, to improve the model — the fine print is everywhere, just better hidden.",
            "Practical conclusion for anyone building something innovative: the only relatively safe way to protect a real competitive edge is running models locally, at the cost of less knowledge than a frontier cloud model.",
        ],
        "quote": {"text": "Cand vezi gratis, tu esti produsul de foarte multe ori.", "cite": "— George Buhnici"},
        "watch": None,
        "names": None,
    },
    {
        "id": "apple-vs-openai",
        "tags": ["ai-infra", "policy"],
        "color": "red",
        "badge": "Confirmed litigation, in court",
        "status": "WATCH — lawsuit ongoing",
        "title": "Apple Sues OpenAI for Trade-Secret Theft",
        "lead": "**The Apple-OpenAI tension has reached court:** Apple accuses OpenAI of systematic trade-secret theft, with concrete allegations tied to Apple's former hardware VP, now OpenAI's hardware chief.",
        "bullets": [
            "Tang Tan, former Apple VP of hardware and now OpenAI's hardware chief, allegedly asked job candidates to bring real equipment (laptops, parts) from their workplaces — one employee, Cheng Liu, allegedly stole a laptop to convince Tan to hire him.",
            "Buhnici stresses the ethical contrast: stealing from a former employer normally disqualifies a candidate; here it seems to have been met \"with open arms and bonuses.\"",
            "Tension grew when Jony Ive (Apple's former chief designer) signed with Sam Altman to build AI hardware — seen by Apple as a direct attack on its turf (direct-to-consumer hardware), not a harmless collaboration.",
            "Separately, the (officially unconfirmed) proposal resurfaces that Sam Altman asked Donald Trump for the US state to take a 5% stake (expandable to 10%) in AI labs through a public fund, modeled on Norway's oil fund or Alaska's — making the state a shareholder with a direct interest in the sector's profits, not just a regulator.",
        ],
        "quote": {"text": "Vino cu secretele companiei la care ai lucrat si o sa fii mai bine rasplatit — nu e o problema de etica, e mai adanca de atat.", "cite": "— George Buhnici"},
        "watch": "The case is explicitly ongoing — Buhnici himself says he has \"no idea\" who will win, only that the dispute is already in court.",
        "names": [
            {"name": "Apple (AAPL)", "blurb": "Sued OpenAI for trade-secret theft, including allegations tied to its former hardware VP.", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "energie-centre-date-romania",
        "tags": ["energy", "policy", "romania"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCH — Romania lacks the power infrastructure yet",
        "title": "Nvidia Discusses Investing in Romania, but Power Is the Real Bottleneck",
        "lead": "**An Nvidia vice-president held talks with Romanian officials** about Romania becoming \"the Norway of Central and Eastern Europe\" for data centers — but Buhnici argues the lack of stable, cheap power makes that impossible in the short term.",
        "bullets": [
            "Any hyperscaler (a company investing heavily in AI infrastructure) needs a high-voltage grid connection permit for megawatt-to-gigawatt loads — the consumption of whole cities — in an area with steady, predictably priced power.",
            "Nuclearelectrica took a loan (possibly from the World Bank) to refurbish Cernavoda reactor 1 — which, with reactors 3 and 4 still unbuilt, would leave Romania with only reactor 2 running in the short term.",
            "He ties this directly to the recent episode when the price per kWh hit €1 at peak after a Cernavoda reactor shut down — Buhnici doesn't think it was an isolated accident and expects it to recur.",
            "His long-term fix: urgent power generation from any source except coal (natural gas, untapped hydro in unprotected areas, geothermal — citing untapped potential north of Bucharest, now used only for spa hot water).",
            "Extra concern: if the US state becomes a shareholder in AI labs (see previous theme), the Romanian parallel is that the state has long owned Hidroelectrica and Nuclearelectrica without making the needed investments — \"for years we only cared about extracting profit... without investing.\"",
        ],
        "quote": {"text": "Pana nu dam drumul la reactoarele 3 si 4, nu cred ca ne permitem deocamdata sa primim centre de date in Romania.", "cite": "— George Buhnici"},
        "watch": "The Nvidia-Romanian state talks are described as \"advanced\" but unconfirmed and unfinished — there is no public agreement yet.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Advanced, unconfirmed talks with Romanian officials about data-center investment tied to power generation.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ram-samsung-starlink",
        "tags": ["semis", "space"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCH — prices keep rising, Starship launch rescheduled",
        "title": "RAM Keeps Getting Pricier, Galaxy Z Fold 8 Specs Leak, Starlink V3 Delayed",
        "lead": "**Three separate hardware threads point the same way:** production constraints (memory, batteries, rocket engines) remain the industry's real bottleneck, not lack of demand.",
        "bullets": [
            "RAM prices are expected to rise 13-18% in Q3 2026 after +60% in Q2 — per Tom's Hardware, the HBM (high bandwidth memory) shortage will last into 2027; Buhnici advises not buying new PC memory now if you can avoid it.",
            "First leaked specs for the Samsung Galaxy Z Fold 8 and Z Fold 8 Ultra: only a 4,800mAh battery on the standard model (5,000mAh on the Ultra), 45W charging — which Buhnici calls insufficient and disappointing versus earlier generations and rivals.",
            "Fold 7 vs Fold 8 Ultra shows minor differences (same 3nm processor, near-identical screen) — the main real upgrades being battery (4,400 to 5,000mAh) and wireless charging (60W); the launch price (€2,200 vs €1,100 now for the Fold 7) is seen as excessive.",
            "SpaceX test flight 13 (Starship v3) was scrubbed at T-0 because some Raptor engines didn't start — the mission was to test an engine relight for better splashdown control and launch the first 20 Starlink V3 satellites.",
            "Starlink V3 promises 1 terabit per satellite (from 96GB before, a 10x jump), satellites of nearly 2 tonnes (3x heavier), and theoretical latency down to 5 milliseconds — close to fiber, for objects orbiting at 27,000 km/h.",
        ],
        "quote": {"text": "Pretul nu se opreste din crescut pentru ca n-ar fi siliciu — avem nisip — ci pentru ca s-a lovit de zidul din portofelul nostru.", "cite": "— George Buhnici"},
        "watch": "The Starlink V3 figures (1 terabit, 5ms latency) are explicitly theoretical maximums reached only in tests so far, not guaranteed production performance.",
        "names": None,
    },
    {
        "id": "cybersecurity",
        "tags": ["ai-infra", "policy"],
        "color": "red",
        "badge": "Confirmed risk",
        "status": "WATCH — broad wave of AI-assisted attacks",
        "title": "Record Microsoft Patch Tuesday — 570 Vulnerabilities, Two Zero-Days Already Exploited",
        "lead": "**Buhnici ties this week's wave of cyber incidents directly to the spread of AI tools**, both for attacking and for finding vulnerabilities.",
        "bullets": [
            "Microsoft shipped its largest Patch Tuesday on record: 570 vulnerabilities fixed in a single month, including two zero-days already actively exploited.",
            "Accenture lost 35GB of code and access keys; the ransomware-as-a-service group \"Jade Puffer\" (mentioned in earlier episodes) now even sells \"education\" services for anyone wanting to learn the same.",
            "Buhnici's own story: an audit run with Fable on his server found an unpatched Grafana instance from 2023 with two zero-days, one of two SSDs dead after a failed restart, and an SSD \"fried\" (110% wear past the maker's threshold) by a backup script that kept hanging and rewriting for three years.",
            "Practical takeaway: he set up a Telegram bot (built with an AI model) that alerts him to any desync on the server, moving from occasional manual checks to proactive monitoring — and reused the freed server capacity for automatic video conversion.",
        ],
        "quote": {"text": "Mi se pare mult mai important in momentul de fata sa stai sa iti faci update de securitate la orice — la telefon, la aplicatii — decat sa amani update-urile.", "cite": "— George Buhnici"},
        "watch": None,
        "names": [
            {"name": "Microsoft (MSFT)", "blurb": "Shipped its largest Patch Tuesday on record: 570 vulnerabilities, two zero-days already exploited.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Accenture (ACN)", "blurb": "Lost 35GB of code and access keys in a recent cyberattack.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F9E0", "tag": "AI", "title": "Test Kimi K3 and Grok 4.5 alongside Fable/GPT — the gap to the US leaders has narrowed far more than most expected."},
    {"icon": "\U0001F512", "tag": "Privacy", "title": "Rely on zero data retention only on enterprise plans when handling sensitive data — on free and Pro plans, assume your data is kept."},
    {"icon": "⚡", "tag": "Energy", "title": "Track the Cernavoda reactor 1 refurbishment — another kWh price shock is a plausible scenario, not an isolated accident."},
    {"icon": "\U0001F4BE", "tag": "Hardware", "title": "Delay big RAM purchases if you can — the HBM shortage is expected to last into 2027."},
    {"icon": "\U0001F6E1️", "tag": "Cybersecurity", "title": "Audit your own servers (even with an AI model's help) — desyncs or abnormal wear can hide for years without active monitoring."},
]

CLAIMS = [
    {"who": "George Buhnici", "claim": "US tech stocks will open lower after the Kimi K3 launch.", "metric": "market direction at the open", "target": "US tech stocks down", "by": "2026-07-17", "condition": "his own call, explicitly flagged as risky", "entity": None},
    {"who": "Sam Altman (cited by George Buhnici)", "claim": "Proposal to Donald Trump that the US state become a shareholder in AI labs.", "metric": "stake via public fund", "target": "5% initially, up to 10%", "by": None, "condition": "proposal not officially confirmed", "entity": "OpenAI"},
    {"who": "George Buhnici, citing Tom's Hardware", "claim": "RAM prices will keep rising next quarter.", "metric": "quarterly RAM price increase", "target": "13-18% in Q3 2026 (after +60% in Q2)", "by": "2026-09", "condition": None, "entity": None},
    {"who": "Memory makers (cited by George Buhnici)", "claim": "The high bandwidth memory (HBM) shortage will persist.", "metric": "HBM availability", "target": None, "by": "2027", "condition": None, "entity": None},
    {"who": "SpaceX (cited by George Buhnici)", "claim": "The new Starlink V3 generation delivers far more capacity per satellite.", "metric": "capacity per satellite / theoretical latency", "target": "1 terabit per satellite (from 96GB), theoretical latency down to 5ms", "by": None, "condition": "theoretical maximum, reached only in tests so far", "entity": None},
]

RELATIONS = [
    {"from": "Apple (AAPL)", "rel": "criticizes", "to": "OpenAI", "note": "Lawsuit over trade-secret theft, including allegations tied to former Apple hardware VP Tang Tan"},
    {"from": "Nvidia (NVDA)", "rel": "invests_in", "to": "Romania", "note": "Advanced, unconfirmed talks on data-center investment tied to power generation"},
]

HOT_TAKES = [
    {"take": "Cred ca stirea asta o sa schimbe radical felul in care companiile americane fac pricing-ul si abonamentele la modelele de inteligenta artificiala.", "cite": "— George Buhnici", "why": "A concrete, checkable call on Kimi K3's impact on US labs' pricing, made on launch day."},
    {"take": "Cand vezi gratis, tu esti produsul de foarte multe ori.", "cite": "— George Buhnici", "why": "Direct critique of free AI platforms' business model, explicitly extended to paid Pro/business plans."},
    {"take": "Nu cred ca a fost un accident — eu cred ca se va repeta, pentru ca odata ce reactorul unu de la Cernavoda intra in revizie, vom ramane doar cu reactorul doi.", "cite": "— George Buhnici", "why": "Specific call on renewed power-price shocks, tied to a named structural cause."},
    {"take": "Ma intristeaza de fiecare data cand ma intalnesc cu oameni care nu pun mana pe inteligenta artificiala pentru afacerile lor sau munca lor — vad asta ca un risc foarte important pentru fiecare dintre noi.", "cite": "— George Buhnici", "why": "Firm personal stance on AI adoption, given as the reason he makes this content."},
    {"take": "Statul roman este un administrator foarte prost pe niste active foarte valoroase, mai ales in perioada asta.", "cite": "— George Buhnici", "why": "Blunt critique of the state's stewardship of Hidroelectrica/Nuclearelectrica."},
]

OTHER_NEWS = [
    {"icon": "\U0001F3D4️", "title": "Two Romanian climbers (Emil Gheorghe and Cornel Roman) died in the Italian Alps (Gran Paradiso), falling into a crevasse hidden by a snow bridge created by accelerated glacier melt — found at about 3,700m after three days of searching. Separately, a 36-year-old climber died in the Bucegi mountains after a 10m fall when a rope broke, with four people anchored to a single point, against safety guidance (at least two points).", "tag": "Mountain safety"},
    {"icon": "\U0001F52C", "title": "Nearly $4 billion invested over the past year in longevity solutions (peptides, treatments) — Buhnici doubts a \"miracle pill\" will appear, but notes sleep, weightlifting and sauna (up to 60% lower cardiovascular risk in men over 40) remain the most overlooked interventions with real impact.", "tag": "Science"},
    {"icon": "\U0001F3AC", "title": "Tribute to actor Sam Neill (Jurassic Park), recently deceased. Film pick: Christopher Nolan's 'The Odyssey' (Matt Damon, Tom Holland, Anne Hathaway, Robert Pattinson). Podcast pick: 'The Skeptics' Guide to the Universe', hosted by Steven Novella.", "tag": "Picks"},
]

GLOSSARY = [
    {"term": "Distillation (AI)", "def": "Training a newer model by comparing a rival model's answers to the same questions and copying the pattern — suspected (but unconfirmed) in some Chinese models."},
    {"term": "Zero Data Retention (ZDR)", "def": "A contractual commitment that the AI provider doesn't keep the user's data or prompts after processing — usually only on enterprise plans, not free or Pro."},
    {"term": "Patch Tuesday", "def": "The second Tuesday of each month, when Microsoft ships security updates — a record Patch Tuesday means an unusually large number of fixes at once."},
    {"term": "HBM (High Bandwidth Memory)", "def": "High-speed memory used in top-end graphics cards and AI accelerators — today's HBM shortage feeds directly into rising RAM prices."},
]
