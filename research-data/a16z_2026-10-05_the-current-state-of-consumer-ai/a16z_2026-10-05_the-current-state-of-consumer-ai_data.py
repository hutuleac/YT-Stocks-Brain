META = {
    "title": "The Current State of Consumer AI",
    "channel": "a16z",
    "speakers": "Olivia Moore, Josh Elman",
    "date": "2026-10-05",
    "video_url": "https://www.youtube.com/watch?v=aCvrzhwUxg0",
    "thread_line": "5 threads · who pays for AI · personal agents · ads and OpenAI · labs vs specialists · startups vs incumbents and white space",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "a16z's 7th Top 100 Consumer AI Apps report added consumer card-spend data for the first time: only 11 new products, but 29 of the 50 top spenders weren't on either traffic list.",
    "About half of Americans use AI, but only ~**4.5%** pay; spend is a power-user game (top 10% of payers = more than half of revenue).",
    "The big new trend is personal agents/assistants (Muse, Instinct, Town) after OpenClaw's spark; growth is fast but still not mainstream.",
    "OpenAI's ad business hit a **$1B annualized run rate** by August on ~1.2B weekly users; Anthropic says no ads.",
    "ChatGPT still leads, but Claude passed Gemini in US paid subscribers in the panel data.",
    "Specialists (Suno, ElevenLabs, Midjourney) keep winning where labs don't focus; incumbents struggle to cannibalize their own interfaces.",
    "White space is largest in network categories (dating, recruiting, social, shopping, entertainment) and in \"spend time\" rather than \"save time\" products.",
]

THEMES = [
    {
        "id": "who-pays",
        "tags": ["software", "consumer"],
        "color": "amber",
        "badge": "Contested",
        "status": "7TH EDITION, NEW SPEND DATA",
        "title": "Consumer AI is a power-user game: 4.5% pay, and the top 1% spend $93 a month",
        "lead": "Usage is broad but revenue is narrow, and the data now shows who the spenders are and what they buy.",
        "bullets": [
            "Report method: added revenue ranking for the first time using card-spend data (consumers only, no enterprise or SMB); only **11 new products** this edition, the fewest ever.",
            "Of the 50 products ranked on spend, **29** were on neither traffic list.",
            "About half of Americans report using AI and ~25% think they interact with it near-daily, but only ~**4.5%** of US consumers pay (some sources say 2-2.5%), roughly doubled in a year.",
            "Inside that 4.5%, the top 10% of payers generate more than half of revenue, the top 1% about 20%, and the bottom 50% about 16%.",
            "The top 1% spend $93/month on personal cards; the median payer spends $25.",
            "Top spenders over-index on builder tools: n8n, Granola, Higgsfield, Manus; a host frames $900/month as a sign of \"making\", not just productivity.",
            "Olivia Moore (consumer AI maximalist) says she does *not* want the 4.5% to simply expand: ~85% of the web list monetizes via subscriptions, ~62% via credits or extra usage, only ~13% via ads or other models.",
        ],
        "quote": {"text": "Most people aren't looking to save time. They're looking for ways to spend their time.", "cite": "— Eugenia Kuyda (quoted by Olivia Moore)"},
        "watch": "a16z invests in consumer AI companies, and the hosts cite portfolio-company founders and products as examples; the paying-user share comes from a panel plus other sources with a wide range.",
        "names": None,
    },
    {
        "id": "personal-agents",
        "tags": ["software", "consumer"],
        "color": "green",
        "badge": "Emerging",
        "status": "LAST 3-4 WEEKS OF LAUNCHES",
        "title": "Personal agents are the biggest new trend, but not yet mainstream",
        "lead": "OpenClaw sparked the category; Muse and Instinct are the headline consumer assistants, and growth is fast but far from Threads-scale.",
        "bullets": [
            "OpenClaw (Mac Mini DIY agent) would have ranked high last edition but is absent now as traffic declined; its team was acquired by OpenAI, and it has been overtaken by Grokbot, Town, and others.",
            "Instinct announced ~**100,000 users** growing ~10% day over day, 40% connecting a credit card in the first three weeks, and >$1,000 average spend in the first month.",
            "Muse (Meta): ~500,000 downloads and 250,000 active users in 12 days; over the same period it sits near **5M** US/Canada downloads versus ~16M for Threads.",
            "Muse is paced slowly partly because cost to serve is high; Amazon blocks Muse from browsing and buying on its site, while Muse has hundreds of partnerships such as Shopify.",
            "Cost reality: assistant founders post serving costs of hundreds or thousands of dollars per user per month, but Assistant Benchmark data (170-200+ agents, 1,500+ early adopters) shows coding and technical automation is the top use case; mainstream-aimed assistants see tens of dollars.",
            "Blockers: no person-to-person network effects yet, the tension of an AI that knows you intimately, and trust/privacy fears about giving agents email and credit cards.",
            "Josh Elman: platform capability is improving faster than consumers' willingness to use agents; the hard part is that a blank box gives users no ideas on what to do.",
        ],
        "quote": None,
        "watch": "Instinct's figures are company-announced; the 10%-per-day growth and card-connect rates are not independently shown here.",
        "names": [
            {"name": "Meta (META)", "blurb": "Muse assistant: strong tech-community launch, ~5M US/Canada downloads vs ~16M for Threads in the same window.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Instinct AI", "blurb": "iMessage personal assistant; ~100K users, 10% day-over-day growth, >$1,000 average first-month spend.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
            {"name": "Amazon (AMZN)", "blurb": "Does not allow Muse to browse and purchase on its site.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "Shopify (SHOP)", "blurb": "One of Muse's purchasing partnerships.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ads-openai",
        "tags": ["software", "consumer"],
        "color": "green",
        "badge": "Confirmed event",
        "status": "$1B RUN RATE AS OF AUGUST",
        "title": "OpenAI's ad business reached a $1B annualized run rate within months",
        "lead": "Density plus intent data lets OpenAI skip the years it normally takes to scale ads, while Anthropic stays subscription-only.",
        "bullets": [
            "OpenAI is at ~**$1B annualized** ad revenue (August figure, likely higher now), rolled out slowly through a partner network.",
            "Last reported ~1.2B weekly active users; login with ChatGPT is live and a wallet is expected to follow.",
            "Josh Elman found the ads clearly labeled and natural; he used ChatGPT to find a valet-key keychain made in America and an NYC travel ad he found useful.",
            "Olivia Moore expects targeting that could beat Meta because the system knows so much and is in a live conversation; unit economics (margins on ads vs coding or image gen) are an open question.",
            "OpenEvidence (AI for doctors) shows early ad success with an estimated 50-60% of US physicians on it, an example of a targeted vertical audience.",
            "Historical contrast: consumer internet giants earn most revenue from ads or transaction fees; in the top 20 global consumer subscription products ChatGPT sits beside media and platforms like Amazon and Uber.",
            "Josh Elman expects falling inference costs to let ads and transaction models finally work; he warns that intrusive, off-topic ads would break trust in a personal AI.",
        ],
        "quote": None,
        "watch": None,
        "names": [
            {"name": "OpenAI", "blurb": "~$1B ad run rate (August), ~1.2B weekly users, login and wallet products.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "OpenEvidence", "blurb": "AI product for physicians, ~50-60% US physician density, early ads success.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
        ],
    },
    {
        "id": "labs-vs-specialists",
        "tags": ["software", "ai-infra"],
        "color": "amber",
        "badge": "Contested",
        "status": "CHATGPT LEADS, CLAUDE PASSES GEMINI ON PAID",
        "title": "ChatGPT leads, Claude passed Gemini in paid subscribers, and specialists hold niches",
        "lead": "Below ChatGPT, rankings keep shifting; specialists survive where labs lack focus, and agent-friendly creative tools get a tailwind.",
        "bullets": [
            "ChatGPT is ~6x Claude and ~2x Gemini on web traffic and has ~3x the US paid consumer subscribers of Gemini or Claude.",
            "Surprise from the US spender panel: **Claude passed Gemini** in paid subscribers despite Gemini's larger install base and Google distribution.",
            "Anthropic's no-ads stance shows up in mix: ~7.5% of its subscribers are on the $100+/month Max plan versus ~1% for ChatGPT and Gemini.",
            "Drivers cited for Claude: recent launches (Claude Design), press from the Department of War episode back in February; Anthropic skipped an image/video model yet users generate images and video via coding.",
            "Audio is where labs under-invest: ElevenLabs and Suno rank near the top of traffic and spend; Suno ran away with music partly because labs avoid its IP headaches.",
            "Images/video: OpenAI Images 2.0 and Google's Nano Banana/Veo took mainstream traffic from standalone generators; Midjourney fell off the traffic list but is back on revenue for power users; Chinese video models have a training-data advantage.",
            "Agent-friendly creative tools should see tailwinds as agents tool-call out to them; bespoke interfaces (Figma-style) hold value beyond the model.",
        ],
        "quote": None,
        "watch": "a16z is a stated investor in several named companies; Claude-over-Gemini is from a US spender panel only, not global data.",
        "names": [
            {"name": "Anthropic", "blurb": "Claude passed Gemini in US paid subscribers; no-ads, 7.5% of subscribers on $100+ plans.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Alphabet (GOOGL)", "blurb": "Gemini trails ChatGPT ~2x on web and now Claude on paid subscribers; Nano Banana and Veo lead image/video traffic.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "ElevenLabs", "blurb": "Voice/audio specialist near the top of traffic and spend.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Suno", "blurb": "Music generation leader running away from the labs.", "stance": "POSITIVE VIEW", "conviction": "Medium", "horizon": None},
            {"name": "Midjourney", "blurb": "Fell off traffic rankings but ranks on revenue for power users who want taste.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "startups-whitespace",
        "tags": ["software", "consumer"],
        "color": "green",
        "badge": "Framework",
        "status": "VALUE MOVING TO THE SOFTWARE LAYER",
        "title": "Startups can still beat labs and incumbents, and the white space is in network categories",
        "lead": "The value is moving to the product layer (context, community, playbooks), and the biggest open categories need multiplayer networks.",
        "bullets": [
            "\"Great expansion\": prosumer AI products (Replit, ElevenLabs, Gamma, Whisper Flow, Granola) pick up team and enterprise revenue through low-cost PLG, years faster than Canva's six-plus.",
            "Incumbents struggle to cannibalize interfaces: Google has not reinvented Docs, Gmail or Calendar, and OpenAI and Anthropic succeed mostly inside their own chat/coding surfaces.",
            "Big-lab agility limit: Plaud (AI note-taker device, on the revenue list) shows startups getting in before OpenAI's hardware, since big companies move slower.",
            "Compounding personal context as a moat: Town builds playbooks of how Olivia writes, and the gap between 99.9% and 85% voice match is 10 seconds versus 10+ minutes of fixing.",
            "Josh Elman, who joined a16z a couple of months ago, says value is moving back to the software layer; \"harness\" and \"wrapper\" undersell rich products where the model is one piece.",
            "Open categories: dating, recruiting and social AI (no AI-native app on the list), shopping, home buying and retail, gaming and entertainment (AI micro-dramas are the exception).",
            "Entertainment closing thought: the biggest consumer companies are \"spend time\" products, while almost all consumer AI so far is \"save time\".",
        ],
        "quote": {"text": "Almost everything we've seen in consumer AI is save time, and that spend time, those end up often actually being amongst the biggest companies if not the biggest ones.", "cite": "— Olivia Moore"},
        "watch": "Both speakers work at an investor in consumer AI startups (a16z); the thesis favors startups.",
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F4CA", "tag": "Markets", "title": "Judge consumer AI by revenue and concentration, not traffic: 4.5% payers and a top-10% that funds most of it."},
    {"icon": "\U0001F4B0", "tag": "Ads", "title": "Watch OpenAI's ad run rate and Anthropic's no-ads stance as the diverging business-model test."},
    {"icon": "\U0001F916", "tag": "Agents", "title": "Track Muse and Instinct for trust, cost-to-serve and person-to-person network effects before calling them mainstream."},
    {"icon": "\U0001F3A8", "tag": "Creative", "title": "Back specialist creative tools (audio, video, taste-driven image) that agents can call."},
    {"icon": "\U0001F9ED", "tag": "Startups", "title": "Build in network categories (dating, recruiting, shopping) and in time-spending products rather than time-saving ones."},
    {"icon": "\U0001F6E1", "tag": "Trust", "title": "Make privacy and security a design feature before granting an agent email or card access."},
]

HOT_TAKES = [
    {"take": "I actually don't necessarily want to see that 4.5% of people paying for AI products directly expand.", "cite": "— Olivia Moore", "why": "Contrarian from a self-described consumer AI maximalist"},
    {"take": "We have transcended the need for everyone to buy a subscription to AI and we need to see these other business models come back.", "cite": "— Olivia Moore", "why": "Calls for ads/transactions over subscriptions"},
    {"take": "OpenAI being able to do crazy good targeting, even better than I think Meta, which previously was best in class.", "cite": "— Olivia Moore", "why": "Ranking prediction"},
    {"take": "I assume when we do this again next time we're going to see massive adoption.", "cite": "— Josh Elman", "why": "Dated adoption prediction (8th edition)"},
]

CLAIMS = [
    {"who": "Josh Elman", "claim": "Personal assistant products reach massive adoption by the next edition of the report.", "metric": "personal agent adoption", "target": "massive adoption", "by": "8th edition", "condition": None, "entity": None},
    {"who": "Olivia Moore", "claim": "OpenAI's ad targeting will beat Meta's, the prior best in class.", "metric": "ad targeting quality", "target": "better than Meta", "by": None, "condition": "As OpenAI leans into ads", "entity": "OpenAI"},
    {"who": "Olivia Moore", "claim": "Gaming and entertainment AI content good enough for average viewers is coming soon.", "metric": "AI-generated entertainment quality", "target": "mainstream-watchable", "by": "soon", "condition": None, "entity": None},
    {"who": "Josh Elman", "claim": "Falling inference costs let ad and transaction business models start working for consumer AI.", "metric": "inference cost", "target": "ads and transaction fees viable", "by": None, "condition": "Inference costs keep coming down", "entity": None},
]

RELATIONS = [
    {"from": "OpenAI", "rel": "acquires", "to": "OpenClaw", "note": "OpenClaw's team was acquired by OpenAI"},
    {"from": "Meta (META)", "rel": "partners_with", "to": "Shopify (SHOP)", "note": "Muse can buy on Shopify among hundreds of partnerships"},
]

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: a16z Top 100 Consumer AI Apps report (7th edition) using Yipit card-spend data; a16z's State of Markets (Sarah Wang's \"power law\" comment); Assistant Benchmark and its founder David Pollon (recent podcast); Eugenia Kuyda's quote; Olivia Moore's \"The Great Expansion\" piece.", "tag": "Sources"},
    {"icon": "\U0001F3AC", "title": "AI micro-dramas are named as the one entertainment format already blowing up; no AI-native dating, recruiting or social product is on the list.", "tag": "Media"},
]

GLOSSARY = [
    {"term": "PLG", "def": "Product-led growth: users adopt a product individually, and teams or enterprises follow."},
    {"term": "Harness", "def": "The newer, less derogatory word for a wrapper: the product layer that brings context and tools to a model."},
    {"term": "OpenClaw", "def": "The DIY personal-agent project that sparked the personal-agent wave and a run on Mac Minis."},
    {"term": "Network category", "def": "A product type that only works with multiple users matching or interacting, such as dating or recruiting."},
    {"term": "Cost to serve", "def": "The inference cost of running each user's AI usage, far higher than for classic consumer internet apps."},
]
