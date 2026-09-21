"""Data file for Peter H. Diamandis (Moonshots, EP #275) — Dario vs Jensen on Open Weights, OpenAI & Anthropic in DC, Xi Exports AI to Global South."""

META = {
    "title": "Dario vs Jensen on Open Weights, OpenAI & Anthropic in DC, Xi Exports AI to Global South | EP #275",
    "channel": "Peter H. Diamandis",
    "speakers": "Peter Diamandis (host), Dave Blundin, Alex (AWG), and Salim/\"Seem\" (co-hosts)",
    "date": "2026-07-29",
    "video_url": "https://www.youtube.com/watch?v=O70Ff5xBnYo",
    "thread_line": "6 threads · Jensen Huang's Open Secure AI Alliance versus Dario Amodei's biosafety-focused rebuttal, OpenAI and Anthropic's joint DC lobbying push and the four-layer business model for surviving free open-weight models, Kimi K3's architecture and the Claude Opus 5 release, China's 'Pax Silica' AI diplomacy strategy, Starship flight 13's successful splashdown plus two brain-computer interface breakthroughs, and Elon Musk's 'money won't matter by 2036' post-capitalist prediction.",
    "category": "market",
}

SNAPSHOT = [
    "Nvidia CEO Jensen Huang posted his first-ever tweet (signed by 77 companies) launching an 'Open Secure AI Alliance,' arguing open models strengthen safety, cybersecurity, and sovereignty — Anthropic's Dario Amodei responded after three days of silence, denying he wants a ban on open weights but arguing the real risk is authoritarian states reaching the AI frontier, particularly around bioweapons; the panel is broadly skeptical of the biosafety argument and reads the fight as partly a business-strategy battle over where profit accrues in the AI stack.",
    "OpenAI and Anthropic are reportedly teaming up in Washington DC to lobby for a federal review process for the most powerful models ahead of an August 1st deadline — the panel debates whether this is genuine safety concern or regulatory capture, and lays out a 'four-layer cake' business model (unreleased frontier models for internal breakthroughs, near-frontier paid models, commoditized open-source models, and application-layer ecosystems) for how closed labs can still make money even as open models get free; Anthropic's implied valuation reportedly dropped roughly $230B (~13%) on secondary markets after Kimi K3's release.",
    "Kimi K3 went fully open-weight on Hugging Face with no API gate, drawing roughly 100,000 downloads in 24 hours — its architecture removes standard positional embeddings entirely (a technique called 'NoPE') in favor of a recurrent-style attention mechanism, which the panel reads as a genuinely novel, quickly-adoptable innovation; Anthropic separately released Claude Opus 5, which the panel finds strong on coding/visual benchmarks but suspects of some benchmark-specific tuning ('benchmaxing') after it underperformed on Frontier Math versus Fable 5.",
    "The Financial Times reports China's Xi Jinping is using AI as a tool of statecraft ('Pax Silica'), exporting models and infrastructure across the developing world as leverage — the panel warns that if the US over-restricts open model exports, it risks ceding the entire global-south AI ecosystem to China by default, comparing the dynamic to historical fighter-jet and infrastructure-loan diplomacy.",
    "SpaceX's Starship flight 13 achieved a historic soft ocean splashdown (the vehicle remained intact), deployed 20 live Starlink V3 satellites, and successfully relit a Raptor engine in orbit — panel discusses plunging launch costs (Space Shuttle ~$54,000/kg to orbit, Falcon 9 ~$2-3,000/kg, Starship targeting $10-100/kg) alongside two BCI stories: Science Corporation's Prima implant earned EU approval for restoring central vision in macular degeneration, and Neuralink demonstrated a paralyzed patient controlling a powered wheelchair purely through thought.",
    "Elon Musk told The Economist that money will become largely irrelevant by 2036 as AI/robotics-driven abundance outpaces demand, predicting deflation rather than inflation — the panel pushes back that money still functions as a means of exchange even in abundance, floats UBI ('COVID checks' at higher purchasing power) as a bridge, and flags a structural conflict with debt-based fiat currency systems (citing Jeff Booth's observation that GDP growth has required roughly $4 of new debt per $1 of GDP growth for 50 years).",
]

THEMES = [
    {
        "id": "open-vs-closed-weights-war",
        "tags": ["ai-infra", "geopolitics"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — Nvidia positioned to win regardless of outcome",
        "title": "Jensen's Open Secure AI Alliance vs. Dario's Biosafety Rebuttal",
        "lead": "**Nvidia CEO Jensen Huang's first-ever tweet launched an industry alliance arguing open models make the world safer**, directly challenging Anthropic's historically cautious stance on open weights — Dario Amodei's response reframes the debate around China, not openness itself.",
        "bullets": [
            "Huang's letter (signed by 77 companies) argues open models strengthen safety/cybersecurity, accelerate innovation, and enable sovereignty — cites last week's Hugging Face breach, where closed models (GPT 5.6, Claude Fable) refused to help forensically analyze the attack, forcing defenders to use the open-weight GLM 2.5 instead.",
            "Dario Amodei's rebuttal: Anthropic has never advocated banning open-weight models; his real concern is whether authoritarian states can reach the AI frontier, centered specifically on biosecurity risk (sufficiently capable models weaponizing pandemic-scale pathogens) — proposes blocking advanced chips/equipment to China, cracking down on industrial-scale distillation, and mandatory safety testing for all powerful models, open or closed.",
            "The panel is largely unconvinced by the biosafety framing specifically: dangerous biological knowledge is already findable without frontier AI, existing models already have substantial biological knowledge, and the argument echoes Microsoft's late-1990s fear-uncertainty-doubt campaign against open-source software, which turned out to be largely wrong (open source proved safer than closed, not less safe, over time).",
            "Frames the deeper dynamic as a fight over where profit accumulates in the AI stack: Nvidia's incentive (as the 'aggregator') is to commoditize the model layer above it, just as IBM once benefited from commoditizing software by backing open source in the 1990s-2000s — the panel notes it's unclear why Nvidia isn't similarly working to commoditize the chip-fabrication layer beneath it (e.g. financing TSMC/Samsung competitors), speculating this may be too politically risky to pursue openly.",
            "One panelist relays a story from a former intelligence-agency innovation chief: rather than restricting distributed dangerous capabilities, agencies have found it more effective to actively fund and open up those ecosystems, since open visibility makes bad actors easier to spot than forcing everything underground.",
        ],
        "quote": {"text": "I don't buy biosafety as an argument... you can just go out on the internet and find things.", "cite": "— Alex, Moonshots with Peter Diamandis"},
        "watch": "One panelist explicitly states he believes Dario's stated motivations are sincere (not purely self-interested), while acknowledging the safety argument and Anthropic's economic self-interest are hard to fully separate given the competitive pressure cheaper open models are putting on closed labs.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Launched the Open Secure AI Alliance; positioned to benefit from commoditization of the model layer regardless of whether open or closed models win.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Anthropic", "blurb": "Reportedly saw its implied valuation drop roughly $230B (~13%) on secondary markets after Kimi K3's release; publicly disputes wanting to ban open weights.", "stance": "UNCERTAIN", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "openai-anthropic-dc-lobbying",
        "tags": ["ai-infra", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — August 1 regulatory deadline",
        "title": "OpenAI and Anthropic Team Up in DC — and the Four-Layer Business Model for Surviving Free Models",
        "lead": "**Two historical rivals are reportedly aligned on lobbying for a federal review process for powerful models ahead of an August 1 deadline** — the panel debates whether this is genuine safety concern or regulatory capture, while sketching how closed labs still make money in a world of free open models.",
        "bullets": [
            "The reported ask: a voluntary 30-day government review before releasing anything with serious cyber/national-security capability, applied to Meta, xAI, and startups too — one panelist calls this a textbook regulatory-capture pattern (comparing it to how railroads, banks, and telecom historically used regulation to entrench incumbents), while another argues Sam Altman (who isn't even an OpenAI shareholder) is genuinely trying to prevent things 'getting out of hand,' not protecting his own economic upside.",
            "Proposes a four-layer business model for how frontier labs stay profitable even as open models commoditize: (1) unreleased, most-advanced internal models used for the lab's own breakthroughs in biology/materials/energy; (2) near-frontier paid models (e.g. GPT 5.6, Fable 5) still worth paying a premium for; (3) fully commoditized open-source models powering everything else; (4) application-layer ecosystems (Meta's 3.5B users, Google's 2B Gemini users, OpenAI's ~1B ChatGPT users) monetized through product distribution rather than raw model access.",
            "A counter-argument raised: business outcomes tend to follow power laws, so it's more likely one layer captures the vast majority of total profit rather than value splitting evenly across all four — with infrastructure/compute (chips, fabs, memory) suggested as an under-discussed fifth layer that could ultimately accrue disproportionate value.",
            "Draws a historical parallel to the 1990s browser wars: Netscape tried to own the whole stack, Mozilla/Firefox made browsers free, and value shifted to the application layer (Google, Amazon) — suggesting a similar fate may await today's frontier labs regardless of their lobbying efforts.",
            "One panelist argues enforcement should target actions/outcomes rather than model capability itself ('aiming enforcement at intelligence is like thought policing... police what the AIs are doing, not what they're thinking'), and separately proposes 'defensive co-scaling' — deploying the strongest available AI specifically to police/monitor other powerful AI — as a more targeted alternative to broad capability restrictions.",
        ],
        "quote": {"text": "This is regulatory capture in real time. Every major industry has tried this — the railroads did it, the banks did it, telco did it, big tech did it.", "cite": "— Peter Diamandis, Moonshots with Peter Diamandis"},
        "watch": "The panel is split on motive (regulatory capture vs. sincere concern) without reaching consensus — both readings are presented as plausible.",
        "names": [
            {"name": "Palantir (PLTR)", "blurb": "CEO Alex Karp reportedly working with Nvidia's Jensen Huang on an open enterprise model plus application layer for enterprises to control their own AI.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Meta (META)", "blurb": "Cited as an application-layer business (3.5B active users) that monetizes AI through product distribution rather than direct model sales.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "Cited with roughly 2B active users on Gemini as another application-layer AI business.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "kimi-k3-opus-5",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "High conviction",
        "status": "WATCHING — architecture innovations expected to be rapidly copied",
        "title": "Kimi K3's Architecture Breaks the Rules — and Claude Opus 5 Draws Benchmaxing Suspicion",
        "lead": "**Kimi K3's fully free release removed a core piece of the original Transformer architecture entirely**, while Anthropic's new Opus 5 release shows strong benchmark gains that the panel suspects are partly narrow optimization rather than broad capability improvement.",
        "bullets": [
            "Kimi K3 went live on Hugging Face with no API key or gatekeeper, drawing roughly 2,500 downloads in the first two hours and an estimated 100,000 within 24 hours; one panelist had it running on dedicated cloud GPUs within an hour of release for about $55/hour.",
            "Architecturally, K3 removes standard positional embeddings entirely (dubbed 'NoPE') in favor of a recurrent-network-style attention mechanism ('Kimi Delta Attention') that gives recent tokens more weight than distant ones — described as an obvious-in-hindsight improvement over the standard rotational position encoding used elsewhere, and one the panel expects other labs to adopt quickly given it's now openly documented.",
            "Claude Opus 5 launched at the same price as its predecessor ($5/$25 per million input/output tokens) and posted a striking jump on the ARC-AGI-3 visual-reasoning benchmark (1.5% to 30.2%), reportedly solving problems by reasoning about visual objects algebraically — but the panel flags this specific benchmark spike as possibly narrow 'benchmaxing,' since a third-party evaluation on a similar-genre game found a much smaller real capability gain, and Opus 5 actually underperformed Fable 5 on Frontier Math.",
            "Panel's practical verdict: despite Opus 5's benchmark gains, panelists report still preferring Fable 5 for day-to-day work, citing better general reasoning and fewer unwarranted refusals — Opus 5's strengths appear concentrated at the intersection of code generation and visual/front-end tasks specifically.",
            "Separately flagged: a significant number of shared Claude chats were found publicly indexable on Google (via a site-specific search operator), exposing personal health records and other private information — read as a reminder that any 'sharing' feature on a hosted AI product carries real privacy exposure, reinforcing the case for locally-run, on-premises models for sensitive data.",
        ],
        "quote": {"text": "The other labs are going to adopt that immediately. It's just flat-out better.", "cite": "— Dave Blundin, Moonshots with Peter Diamandis"},
        "watch": "Panel explicitly flags Opus 5's ARC-AGI-3 jump as possibly not representative of general capability given a third-party benchmark showed a much smaller gain on a similar task.",
        "names": None,
    },
    {
        "id": "pax-silica",
        "tags": ["geopolitics", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "WATCHING — no current US open-source model to compete globally",
        "title": "China's 'Pax Silica': Xi Jinping Exports AI as a Tool of Statecraft",
        "lead": "**The Financial Times reports China is exporting AI models and infrastructure across the developing world as diplomatic leverage** — the panel warns that if the US restricts its own open models too aggressively, it risks handing the entire global-south AI ecosystem to China by default.",
        "bullets": [
            "Frames the dynamic as a new form of soft power: whichever country supplies AI models and infrastructure to the developing world shapes alignment for decades to come, similar to how China's Belt and Road Initiative used infrastructure loans for geopolitical leverage.",
            "One panelist argues over-restricting US open models is a strategic 'self-own' — protecting a small number of domestic labs while ceding an entire global ecosystem's usage habits, developer base, and alignment to Chinese alternatives.",
            "Draws an explicit escalation comparison: a foreign-funded telecom deployment lets a rival government potentially monitor or shut off communications; embedding a foreign AI model into a country's core decision-making infrastructure is a deeper form of dependency — 'thinking for you' rather than just listening to or lending money to you.",
            "Notes the US currently has no fully open-source frontier-adjacent model to compete globally with options like Kimi K3, comparing the dilemma to whether to sell F-16 fighter jets to a given country: refusing doesn't prevent proliferation, it just cedes the sale (and the relationship) to Russia or China instead.",
            "Cites a personal anecdote about a small Asian country taking a $500M Chinese loan for port infrastructure that may be technologically bypassed within a few years by falling drone costs — used to argue exponential technology awareness itself is a form of national sovereignty protection against this kind of infrastructure-debt trap.",
        ],
        "quote": {"text": "The whole power of the US is its open and very broad innovation ecosystem. If you create a restrictive open model policy, it's a self-own of epic level.", "cite": "— Salim, Moonshots with Peter Diamandis"},
        "watch": None,
        "names": None,
    },
    {
        "id": "starship-and-bci",
        "tags": ["space", "biotech"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "WATCHING — flight 14 expected to attempt a tower catch",
        "title": "Starship Flight 13's Historic Splashdown, Plus Two Brain-Computer Interface Breakthroughs",
        "lead": "**A strong week for physical-world technology**: SpaceX's Starship survived a soft ocean landing intact for the first time, while two separate BCI companies demonstrated real restoration of human capability.",
        "bullets": [
            "Starship flight 13 deployed 20 live, operational Starlink V3 satellites (targeting 0.5-1 gigabit connectivity anywhere on Earth), successfully relit a Raptor engine in orbit (needed for Artemis missions), and achieved a soft, intact ocean splashdown — a first, since prior flights had ended in expected detonation from residual fuel; Elon Musk indicated flight 14 may attempt catching the ship with the tower's mechanical arms given how precise this landing was.",
            "Panel cites plunging launch costs as the underlying abundance story: Space Shuttle cost roughly $54,000/kg to orbit, Falcon 9 brought that to $2,000-3,000/kg, and Starship's target is $10-100/kg.",
            "Science Corporation (a Diamandis portfolio company, run by former Neuralink president Max Hodak) earned EU approval (CE mark) for Prima, a retinal implant restoring central vision in age-related macular degeneration — patients showed a five-line improvement on a standard eye chart after 12 months; the device uses external glasses that beam images via infrared to an implant behind the retina, distinct from Neuralink's more direct brain-stimulation approach.",
            "Neuralink released video of a paralyzed patient controlling a powered wheelchair purely through imagined cursor movements translated into wheelchair motion, with a built-in safety fail-safe (the cursor drifts back to center if the user becomes incapacitated) — panel extrapolates this toward eventual full-body exoskeleton control and, longer-term, partial motor-cortex uploading.",
        ],
        "quote": {"text": "Nobody else [treats failure the way SpaceX does] — he views any kind of failure as information, and you don't get embarrassed by it. You take the data, you learn, and you do it way better next time.", "cite": "— Peter Diamandis, Moonshots with Peter Diamandis"},
        "watch": None,
        "names": None,
    },
    {
        "id": "post-capitalist-prediction",
        "tags": ["macro-rates", "policy"],
        "color": "gray",
        "badge": "Speculative framework",
        "status": "WATCHING — Musk reportedly considering a wealth pledge in response to a public challenge",
        "title": "Elon's 'Money Won't Matter by 2036' — and the Debt-Based Currency Problem It Raises",
        "lead": "**Elon Musk told The Economist money will become largely irrelevant within a decade as AI/robotics-driven abundance of goods and services outpaces demand** — the panel pushes back on the framing while flagging a real structural currency problem underneath it.",
        "bullets": [
            "Musk's specific claim: as AI/robotics-driven output of goods and services grows faster than the money supply, the result will be deflation, not inflation — panelists interpret this as shorthand for most daily-living costs (food, shelter, healthcare, utilities, education, entertainment) becoming radically cheaper within a decade, not the literal end of exchange, unit-of-account, or store-of-value functions of money.",
            "One panelist floats a bridge scenario: a higher-purchasing-power universal basic income (using the analogy of pandemic-era stimulus checks) combined with AI-driven collapses in the cost of healthcare, construction, and transportation could make a fixed monthly amount go dramatically further than it does today.",
            "Flags a structural currency risk underneath the abundance thesis: citing investor Jeff Booth's observation that global GDP growth has required roughly $4 of new debt for every $1 of GDP growth over the past 50 years — argues this debt-fueled growth model breaks down if deflation from technological abundance takes hold, since debts denominated in a currency become harder to service as prices for the goods that generate revenue keep falling.",
            "Economist and Nobel laureate Daron Acemoglu publicly challenged Musk to pledge his roughly $1 trillion net worth to charity by 2036 if he's serious that money won't matter by then — Musk reportedly responded that he's considering something along those lines, which one panelist speculates could take the form of distributing SpaceX/Tesla stock broadly rather than a traditional charitable pledge.",
            "Panel's closing framing: they're comfortable with continued wealth concentration at the very top ('trillionaires living on Mars') as long as the floor for ordinary people keeps rising — citing that the share of humanity in extreme poverty (under $2/day, 2011 parity) has fallen from roughly 94% in 1820 to under 9% today as the underlying long-term trend they expect AI abundance to accelerate.",
        ],
        "quote": {"text": "The biggest challenge here is not that abundance is impossible — it's that abundance will get captured by a few big companies, which is where wealth inequality has been coming from.", "cite": "— Salim, Moonshots with Peter Diamandis"},
        "watch": "Musk's response to the Acemoglu challenge is explicitly described as tentative ('I'm actually going to do something along those lines') — no concrete commitment had been made as of this recording.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F310", "tag": "AI ethics", "title": "Weigh biosafety arguments for restricting open-weight AI against how easily the same information is already findable without frontier models."},
    {"icon": "\U0001F4B0", "tag": "AI infra", "title": "Map which of the four AI business-model layers (unreleased frontier, near-frontier paid, commoditized open-source, application layer) a given company actually occupies before assuming it's threatened by free models."},
    {"icon": "\U0001F510", "tag": "AI infra", "title": "Default to locally-run or on-premises models for sensitive data — any hosted 'sharing' feature carries real privacy exposure, as the Claude chat indexing incident showed."},
    {"icon": "\U0001F30D", "tag": "Geopolitics", "title": "Track which country's open AI models and infrastructure the global south adopts as a genuine soft-power indicator, not just a technical curiosity."},
    {"icon": "\U0001F680", "tag": "Space", "title": "Watch launch cost-per-kilogram trends as the leading indicator for which space-dependent business models become viable next."},
]

CLAIMS = [
    {"who": "Moonshots panel (citing secondary-market pricing)", "claim": "Anthropic's implied valuation dropped after Kimi K3's release", "metric": "valuation change", "target": "roughly $230 billion decline (~13%)", "by": None, "condition": "based on secondary market trading, not a public valuation event", "entity": "Anthropic"},
    {"who": "Dave Blundin (citing SpaceX targets)", "claim": "Starship's target launch cost per kilogram to orbit", "metric": "cost per kilogram", "target": "$10-100/kg (vs. Space Shuttle's ~$54,000/kg and Falcon 9's ~$2,000-3,000/kg)", "by": None, "condition": None, "entity": "SpaceX"},
    {"who": "Elon Musk (cited)", "claim": "money becomes largely irrelevant due to AI/robotics-driven abundance", "metric": "timing", "target": "by 2036", "by": "2036", "condition": "his own stated post-capitalist prediction, made in an Economist interview", "entity": None},
    {"who": "Alex, citing broader consensus (Moonshots with Peter Diamandis)", "claim": "longevity escape velocity timing", "metric": "timing", "target": "2030-2033 consensus range ('LEV by 2033')", "by": "2033", "condition": None, "entity": None},
    {"who": "Science Corporation (cited)", "claim": "Prima implant vision-restoration outcome in human trials", "metric": "vision improvement", "target": "5 lines of improvement on a standard eye chart after 12 months", "by": None, "condition": "human trial results, cited as basis for EU CE mark approval", "entity": None},
]

RELATIONS = [
    {"from": "Nvidia (NVDA)", "rel": "partners_with", "to": "Palantir (PLTR)", "note": "Alex Karp reportedly working with Jensen Huang on an open enterprise-grade model plus application layer"},
    {"from": "Anthropic", "rel": "criticizes", "to": "Nvidia (NVDA)", "note": "Dario Amodei publicly disputed the framing of Nvidia's Open Secure AI Alliance, centering the debate on China/biosafety risk instead"},
]

HOT_TAKES = [
    {"take": "I'm not shedding tears for the profit margins of a couple of frontier labs. This is what intelligence too cheap to meter is supposed to look like.", "cite": "— Alex, Moonshots with Peter Diamandis", "why": "A direct pushback against sympathy for Anthropic/OpenAI's competitive pressure from free open models."},
    {"take": "Aiming enforcement at intelligence is like thought policing, but for the AIs. I'd much rather see enforcement leveled at the action layer.", "cite": "— Alex, Moonshots with Peter Diamandis", "why": "A specific, checkable policy position on where AI regulation should target, made against the grain of most current proposals."},
    {"take": "This is regulatory capture in real time. Every major industry has tried this — the railroads did it, the banks did it, telco did it, big tech did it.", "cite": "— Peter Diamandis, Moonshots with Peter Diamandis", "why": "A direct accusation against two specific, named companies (OpenAI and Anthropic) regarding their DC lobbying push."},
    {"take": "Money won't matter in 2036.", "cite": "— Elon Musk, cited by Moonshots with Peter Diamandis", "why": "A sweeping, dated, checkable macroeconomic prediction made directly to The Economist."},
    {"take": "The whole power of the US is its open and very broad innovation ecosystem. If you create a restrictive open model policy, it's a self-own of epic level.", "cite": "— Salim, Moonshots with Peter Diamandis", "why": "A blunt warning against a specific US policy direction, framed as strategically self-defeating."},
]

OTHER_NEWS = [
    {"icon": "\U0001F513", "title": "A significant number of shared Claude chats (via the site's share-link feature) were found to be publicly indexable on Google, exposing personal health records, private documents, and phone numbers — reinforces the case for on-premises/local model deployment for sensitive data.", "tag": "Privacy/security"},
]

GLOSSARY = [
    {"term": "NoPE (No Positional Embeddings)", "def": "An architectural choice (used in Kimi K3) that removes standard position-encoding mechanisms from a transformer model entirely, instead relying on a recurrent-style attention mechanism to implicitly track token order and recency."},
    {"term": "Benchmaxing", "def": "Optimizing a model specifically to score well on a particular benchmark rather than improving general capability — suspected by the panel in some of Claude Opus 5's most dramatic benchmark jumps."},
    {"term": "Defensive co-scaling", "def": "The strategy of ensuring defenders (the 'good guys') have access to AI capability at least as strong as, and ideally slightly ahead of, potential attackers, on the theory that a time advantage compounds enormously under recursive self-improvement."},
    {"term": "Pax Silica", "def": "The Financial Times' term for China's strategy of exporting AI models and infrastructure to developing nations as a tool of geopolitical influence, echoing the historical 'Pax' framing of dominant global powers exporting their systems abroad."},
]
