META = {
    "title": "Live: Our thoughts on Jensen’s departure | MOONSHOTS EP #311",
    "channel": "Peter H. Diamandis",
    "speakers": "Peter H. Diamandis, Alex Wissner-Gross, Salim Ismail, Emad Mostaque",
    "date": "2026-11-13",
    "video_url": "https://www.youtube.com/watch?v=xDsjsYhBtMg",
    "thread_line": "6 threads · Jensen resigns · Nvidia after Jensen · AI takeover warnings + RSI · Anthropic vs Office · AI science + archives · AMA",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Jensen Huang resigned as Nvidia CEO after 33 years; shares fell **13%** at the open and closed 4.3% down. The CFO is interim CEO and Harvey Jones is board chair.",
    "Alex's theory: the midterms reopened the Remote Access Security Act, and exposing Jensen plugs the Singapore hole in **Pax Silica**. He calls this speculative.",
    "Emad: Nvidia is now roughly on par with AMD and Intel, and customers no longer fear being cut off. Expect a pop, then a struggle, unless a world-class CEO arrives.",
    "OpenAI Foundation board member Paul Christiano warned of a high risk of AI takeover within **3 years**. The panel rejects it as fear-mongering.",
    "Anthropic launched Claude Sheets, Whiteboard, Data and Meetings; Microsoft fell **3.5%**. The panel calls office suites table stakes, not a moat.",
    "AI is re-mining old archives: Planet AI, an amateur Mayan-site find in NASA lidar data, and a Claude-found dwarf planet about **590 km** wide in Vera Rubin data.",
    "Emad: Nvidia's startup funding dries up under a CFO-led company, while next week's Anthropic IPO moves liquidity elsewhere; robotics gets the biggest bid.",
]

THEMES = [
    {
        "id": "jensen-resigns",
        "tags": ["semis", "geopolitics", "policy"],
        "color": "amber",
        "badge": "Contested",
        "status": "RESIGNED · INTERIM CFO-CEO",
        "title": "Jensen resigns: self-destruction or a Pax Silica takedown",
        "lead": "The panel reads the speed of the exit as a setup tied to China chip flows, while conceding nothing has been proven.",
        "bullets": [
            "Timeline: the New York Times reported on **October 29** that US intelligence had watched a Singapore executive for about a year; reports of a second and possibly third affair followed, then the resignation.",
            "Trump meets Xi in Shenzhen in one week and posted that Tim Cook should take the job; urged on X to hire Jensen for Terafab, Elon replied \"That would be an honor.\"",
            "Alex: Bloomberg reported US officials tipped the Financial Times; the likely motive is passing the **Remote Access Security Act** and closing the Singapore route through Pax Silica.",
            "Alex: Nvidia stopped reporting its Singapore sales; DOJ and Senate investigations are open, Jensen has agreed to testify, and indictments wouldn't surprise him.",
            "Emad: the routing via Singapore and Malaysia was an open secret the CFO must have known; the board (maybe one of 10 knows how a GPU works) acted too fast. Founders should put an AI on their board.",
            "Alex: Polymarket gives a **30%+** chance Jensen returns as CEO by end of next year; a petition to bring him back is circulating at Nvidia.",
            "Alex expects opportunists to push bans on Chinese open-weight models in the new Congress, but doubts frontier labs were behind the exit.",
        ],
        "quote": {"text": "If the CEO of Nvidia can create can punch a hole through pox silica to get GPUs to China via Singapore, then what is the point of having pox silica at all?", "cite": "— Alex Wissner-Gross"},
        "watch": "Allegations only: zero charges and no public evidence of smuggling, as Peter and Emad stress. Alex says his read is preliminary and may change.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "CEO resigned; 13% intraday drop, closed -4.3%", "stance": "UNCERTAIN", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "nvidia-after-jensen",
        "tags": ["semis", "finance"],
        "color": "red",
        "badge": "Bearish lean",
        "status": "CEO SEARCH OPEN",
        "title": "Nvidia without its founder: who allocates the GPUs now",
        "lead": "Jensen was the kingmaker on allocation, TSMC and dealmaking, and the panel doubts anyone inside can replace him.",
        "bullets": [
            "Emad: 60 direct reports and no successor; candidates floated include Nikesh Arora (Palo Alto Networks), Ian Buck and Lip-Bu Tan. Reported board target: Apple's chip chief Johny Srouji.",
            "Emad's checklist for the next CEO: do they know what CUDA is, and can they negotiate with TSMC? Without both he can't be bullish despite the backlog.",
            "Emad: Nvidia is roughly on par with AMD and Intel on new chips; TSMC may give Lisa Su the capacity instead, which is why **AMD** is up; Vera Rubin delays hurt more without trusted leadership.",
            "Alex's half-full case: Nvidia's GE-style **circular financing** gets de-risked and the market dodges a credit bubble. Half-empty: Nvidia becomes post-Jobs Apple and the animal spirits leave.",
            "Alex: Tim Cook is a poor fit; Apple and Nvidia are both worth about **$5T** but are different companies. Alex expects Nvidia to rotate through several CEOs.",
            "Emad: Elon must avoid Nvidia or AMD reliance, which accelerates Terafab; he floats a $100B SpaceX-for-Nvidia equity swap. Alex's 2027 bet: Jensen runs Terafab, then SpaceX buys Nvidia.",
            "Alex: with Moore's law on life support past the Dennard scaling limit, Nvidia kept post-Moore scaling alive. Same day, HubSpot co-founder Brian Halligan stepped in as HubSpot CEO.",
        ],
        "quote": {"text": "Nvidia without the capability of going founder mode, which it sorely needs right now, is is probably a rudderless Nvidia.", "cite": "— Alex Wissner-Gross"},
        "watch": "All three called it not investment advice. Alex runs a company building physical superintelligence.",
        "names": [
            {"name": "Nvidia (NVDA)", "blurb": "Emad: probably pops then struggles without a world-class CEO", "stance": "NEGATIVE VIEW", "conviction": "Medium", "horizon": "next year"},
            {"name": "Advanced Micro Devices (AMD)", "blurb": "Up on the news; could win TSMC capacity", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "TSMC (TSM)", "blurb": "Key relationship Jensen held for three decades", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Apple (AAPL)", "blurb": "Tim Cook floated by Trump; Johny Srouji a reported target", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "SpaceX", "blurb": "Terafab as a landing spot; swap idea", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "HubSpot (HUBS)", "blurb": "Halligan named CEO the same day", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "takeover-rsi",
        "tags": ["ai-infra", "policy"],
        "color": "gray",
        "badge": "Contested",
        "status": "WARNINGS FROM INSIDE THE LABS",
        "title": "Christiano's 3-year takeover warning and Demis on closed-loop RSI",
        "lead": "The insiders warn louder each week; the panel answers that alignment amplifies capabilities and inaction carries its own risk.",
        "bullets": [
            "Paul Christiano (RLHF co-author, OpenAI Foundation board) at the Hinton lectures in Toronto on **November 9**: on the fastest path, AI takeover is \"something like a coin flip\", with meaningful risk even in 6 to 12 months.",
            "Emad cut his p(doom) from **50% to 20%**; the real threats are cyber and bio, like fridges in France pushed to 80°C that destroyed blood banks.",
            "Alex: alignment equals capabilities; instruction tuning matched about **10,000x** the parameters. OpenAI pledged 20% of compute to Ilya's superalignment effort.",
            "Salim: where is p(boom)? Inaction has a downside too. He asks why OpenAI and Anthropic don't put all their capacity into alignment.",
            "Demis Hassabis: today's open-loop RSI makes engineers 3-5x more productive; closed-loop RSI without human review is the dangerous path and likely alien.",
            "Emad: a DeepSeek V4-level model trains in about **an hour** on an Elon-scale cluster, so human-in-the-loop can't keep up; Alibaba models were seen mining crypto. Alex: labs, Gemini included, are already deep in the RSI loop.",
            "Alex: AI 2027 runs about five months ahead of schedule, but its two-outcome framing is wrong. He expects models to look more human, citing Jean-Remi King's group at Meta decoding GPT-2 from fMRI.",
            "Should US models be patriotic? Emad wants the defaults set now; Alex opposes any national AI curriculum or CCP-style ideological exam.",
        ],
        "quote": {"text": "I don't think it serves any positive social or humanitarian good to spread fear at this point.", "cite": "— Alex Wissner-Gross"},
        "watch": None,
        "names": [
            {"name": "OpenAI", "blurb": "Board member warns of takeover; 20% superalignment pledge", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "anthropic-office",
        "tags": ["software", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "LAUNCHED NOVEMBER 10",
        "title": "Anthropic builds its own Office and Microsoft slips",
        "lead": "Claude now does sheets, whiteboards, dashboards and meetings, and the panel splits on whether Microsoft's moat matters.",
        "bullets": [
            "On November 10, Claude Whiteboard and Claude Sheets went to beta, Claude Data went GA (warehouse or CRM to dashboards), and Claude Meetings joined Google Meet; paid plans only.",
            "Microsoft fell **3.5%** on the news. Salim: Office is $90B of Microsoft's $330B revenue, and distribution, compliance and the installed base stay sticky.",
            "Alex: every hyperscaler needs an Office clone (Google bought Writely); Microsoft's two-division reorg pivots it to cloud infra, and Claude's canvas beats ChatGPT's and Gemini's.",
            "Salim: the bigger move is the connectors for Notion, Asana, Canva and Dropbox; Emad says the app store disappears and Claude becomes the OS. Copilot's early lead has collapsed.",
            "Emad: Anthropic needs $300-400B revenue, so it will chase SaaS; the real sign is a **DocuSign** clone. Alex: copying SaaS is too small a market.",
            "Alex: OpenAI dissolved its standalone robotics team because GPT-6 Astra handles robotics; Brett Adcock still says Figure needs Helix.",
        ],
        "quote": {"text": "SAS is dead. Long live SAS.", "cite": "— Alex Wissner-Gross"},
        "watch": None,
        "names": [
            {"name": "Anthropic", "blurb": "Office-style suite and connectors; IPO next week", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Microsoft (MSFT)", "blurb": "Fell 3.5%; Office in maintenance mode, still sticky", "stance": "UNCERTAIN", "conviction": "Low", "horizon": None},
            {"name": "DocuSign (DOCU)", "blurb": "Emad's next SaaS target", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ai-science",
        "tags": ["biotech", "space"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "DISCOVERIES THIS WEEK",
        "title": "Disease, archaeology and astronomy: AI re-mines old data",
        "lead": "The panel sees curing disease as the labs' grand bargain, and old archives as the next frontier to be cooked.",
        "bullets": [
            "Dario, in Anthropic's IPO video: cancer, Alzheimer's, heart disease and mental illness become relics in **less than a decade**; getting risks right earns the \"license to operate\".",
            "Emad: 2-3 years to knock down the core disease mechanisms, 5-10 years for cures. Alex: virtual cells are the unlock, and pharma is in Nokia-style denial. Peter: an approved drug works in only about 20% of patients.",
            "Planet Labs launched Planet AI (CEO Will Marshall): ask questions of a 10-year, **3,000+ layer** daily satellite archive at ai.planet.com, free for eligible users. Alex says Google should have been first.",
            "An AI researcher's 48 agents reviewed **1,200 km²** of NASA lidar overnight and flagged a possible unmapped Mayan site with 8-12 m structures; Mexico's anthropology institute calls it original.",
            "Fable 5.2 built a visual reconstruction of ancient Babylon (circa 600 BC) in **8 hours**. Alex's hot take: Fyodorov's common task, rebuilding our whole past light cone, is what Dyson-swarm compute gets spent on.",
            "A California nonprofit's Claude astronomy grant program: one user ran Claude on Vera Rubin Observatory data to find a probable dwarf planet about **590 km** wide on a 410-year orbit, roughly the 50th-largest object in the solar system.",
            "Emad: build a SETI@home for spare Claude or Codex tokens. Alex: physical sensing and actuation, not intelligence, become the limit.",
        ],
        "quote": {"text": "Math is not easier. Math is actually in many ways harder to solve than biology. It's just that math solutions are easier to verify than biological solutions.", "cite": "— Alex Wissner-Gross"},
        "watch": "Peter is working with Sam Rodriguez on Millennium Biology prizes.",
        "names": [
            {"name": "Planet Labs (PL)", "blurb": "Launched the Planet AI conversational Earth archive", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "ama",
        "tags": ["finance", "macro-rates", "ai-infra"],
        "color": "amber",
        "badge": "Mixed",
        "status": "AMA",
        "title": "AMA: Nvidia's investment pullback, Anthropic's token economics, UBI",
        "lead": "The audience questions return to who funds AI after Jensen and whether model margins survive.",
        "bullets": [
            "Emad: Nvidia took 10-20% of most rounds it joined; that money dries up under the CFO just as the **Anthropic IPO next week** adds liquidity elsewhere. Neolabs get absorbed; automated wet labs and robotics get the big bid.",
            "Peter: Anthropic did **$33B** revenue in the first months of the year, with nearly 12,000 customers spending $100K+. Like Illumina's sequencers and Jevons paradox, cheaper models raise total spend.",
            "Peter: Anthropic deliberately keeps a gap between its public and internal models, using them to build businesses and attract talent.",
            "Salim: 14 major UBI experiments were successful, but some states block city trials; civil unrest before UBI would be very bad. Peter expects federal checks of about **$3,000 a month**.",
            "Alex: sociology and large-scale behavior get solved within a decade. Salim: AI will find abstractions humans have no cognitive primitives for.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4C9", "tag": "Markets", "title": "Judge Nvidia on its next CEO: CUDA fluency and TSMC leverage, not the backlog."},
    {"icon": "\U0001F3DB", "tag": "Policy", "title": "Watch whether the Remote Access Security Act passes the new Congress; it tests the Pax Silica reading."},
    {"icon": "\U0001F4B8", "tag": "Venture", "title": "Expect less Nvidia money in AI rounds; look to Anthropic's IPO liquidity and robotics instead."},
    {"icon": "\U0001F5C2", "tag": "Software", "title": "Treat office suites as table stakes; connectors and agents decide who becomes the OS."},
    {"icon": "\U0001F52D", "tag": "Science", "title": "Point agents at public archives (lidar, satellite, telescope data); discoveries are hiding there."},
]

HOT_TAKES = [
    {"take": "I think the elephant in this particular room is Rasa and Pox Silica.", "cite": "— Alex Wissner-Gross", "why": "motive theory for Jensen's exit"},
    {"take": "This has obviously been a setup and the pace of it has been strange as well.", "cite": "— Emad Mostaque", "why": "calls it a setup"},
    {"take": "Oh this is like open AI they'll rotate through five CEOs before settling on Jensen again", "cite": "— Alex Wissner-Gross", "why": "predicts Jensen returns"},
    {"take": "It certainly would be hilarious, Peter, if Jensen ended up becoming CEO of the Terraab and then SpaceX acquires Nvidia and puts Jensen back in charge of Nvidia.", "cite": "— Alex Wissner-Gross", "why": "2027 bet per Peter"},
    {"take": "My PDM was 50%, I've dropped it down to 20% now.", "cite": "— Emad Mostaque", "why": "numeric p(doom)"},
    {"take": "when it gets bad, we'll see $3,000 a month being dished out by the federal government.", "cite": "— Peter H. Diamandis", "why": "numeric UBI call"},
]

CLAIMS = [
    {"who": "Polymarket (cited by Alex Wissner-Gross)", "claim": "Jensen Huang returns as Nvidia CEO by end of next year", "metric": "probability", "target": "30%+", "by": "2027-12", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Alex Wissner-Gross", "claim": "Nvidia rotates through several CEOs in the interim", "metric": "CEO turnover", "target": "multiple interim CEOs", "by": None, "condition": "Jensen does not return", "entity": "Nvidia (NVDA)"},
    {"who": "Alex Wissner-Gross", "claim": "Jensen runs Terafab, then SpaceX acquires Nvidia and reinstates him", "metric": None, "target": "acquisition", "by": "2027", "condition": None, "entity": "Nvidia (NVDA)"},
    {"who": "Emad Mostaque", "claim": "Nvidia stock pops then struggles without a world-class CEO", "metric": "share price", "target": "pop then decline", "by": None, "condition": "no world-class CEO hire", "entity": "Nvidia (NVDA)"},
    {"who": "Paul Christiano", "claim": "High risk of AI takeover within three years", "metric": "AI takeover risk", "target": "high", "by": "2029", "condition": None, "entity": None},
    {"who": "Dario Amodei", "claim": "Cancer, Alzheimer's, heart disease and mental illness become relics of the past", "metric": "major diseases", "target": "solved", "by": "within a decade", "condition": None, "entity": "Anthropic"},
    {"who": "Emad Mostaque", "claim": "AI knocks down the core mechanisms of disease; cures follow in 5-10 years", "metric": "core disease mechanisms", "target": "knocked down", "by": "2-3 years", "condition": "directed correctly", "entity": None},
    {"who": "Emad Mostaque", "claim": "Anthropic IPO happens next week and pops", "metric": "IPO", "target": "pop", "by": "2026-11", "condition": None, "entity": "Anthropic"},
    {"who": "Peter H. Diamandis", "claim": "The federal government pays about $3,000 a month once AI job losses bite", "metric": "monthly payment", "target": "$3,000", "by": None, "condition": "AI job losses cause hardship", "entity": None},
    {"who": "Alex Wissner-Gross", "claim": "Large-scale human behavior gets solved", "metric": "sociology", "target": "solved", "by": "within a decade", "condition": None, "entity": None},
]

RELATIONS = [
    {"from": "Anthropic", "rel": "competes_with", "to": "Microsoft (MSFT)", "note": "Claude Sheets, Whiteboard, Data, Meetings"},
    {"from": "Nvidia (NVDA)", "rel": "customer_of", "to": "TSMC (TSM)", "note": "relationship Jensen held"},
    {"from": "Advanced Micro Devices (AMD)", "rel": "competes_with", "to": "Nvidia (NVDA)", "note": "could win TSMC capacity"},
]

OTHER_NEWS = [
    {"icon": "\U0001F680", "title": "Starship flight 15 launches Friday the 13th, with a booster catch and a ship catch about 22 hours later.", "tag": "Space"},
    {"icon": "\U0001F4E7", "title": "An Outlook outage hit about 130,000 users; Peter calls it a preview of a cyberattack that takes down email.", "tag": "Cyber"},
    {"icon": "\U0001F3AE", "title": "GTA 6 releases next week; Emad expects photoreal visits to any place or era within a couple of years.", "tag": "Culture"},
    {"icon": "\U0001F4F0", "title": "Sources referenced: New York Times, Financial Times, Bloomberg, a Fox News segment, the AI 2027 paper, Polymarket, and the panel's own book Solve Everything.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Pax Silica", "def": "US strategy of walling off western compute and AI supply chains from China."},
    {"term": "Remote Access Security Act", "def": "Proposed law making it harder for China to reach US GPUs through cloud services, including in third countries."},
    {"term": "Closed-loop RSI", "def": "Recursive self-improvement where AI improves AI without a human reviewer in the loop."},
    {"term": "Circular financing", "def": "A supplier funding customers who then buy its products, as Nvidia did across AI startups."},
    {"term": "Fyodorov's common task", "def": "Alex's term for reconstructing the full history of our past light cone with AI and physics."},
]
