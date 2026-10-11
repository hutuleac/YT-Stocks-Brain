META = {
    "title": "Vitalik in Singapore: What Will Blockchain Look Like in the AI Era?",
    "channel": "WuBlockchain Podcast",
    "speakers": "Vitalik Buterin",
    "date": "2026-10-07",
    "video_url": "https://www.youtube.com/watch?v=9HHpDMBa_Ds",
    "thread_line": "3 threads · ZK and programmable privacy · AI as attacker, auditor and new UI · Ethereum in two years and full-stack security",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Short keynote (~15 min): Vitalik Buterin argues crypto tech **has not matured** and AI is now both its biggest opportunity and biggest risk.",
    "Zero-knowledge proofs turn blockchains from programmable assets into **programmable data** — prove a property without revealing the data.",
    "Prediction: within two years the majority of people will have used a ZK/privacy tech without knowing it.",
    "AI is already finding exploits everywhere; Ethereum and Bitcoin haven't gone down, and AI-driven formal verification will make much stronger security possible — and mandatory.",
    "He updated his ENS record with a locally run model writing a script in ~5 minutes — **AI is becoming the new UI**, killing the front-end attack layer behind the ~$1.4B Safe hack but adding prompt-injection risk.",
    "Ethereum in two years: many more, cheaper, more private transactions; apps where bots trade with bots, and possibly no apps at all — just agents reading on-chain offers.",
    "The blockchain world gets the internet's problems first because it holds a lot of money; today's hardware wallet becomes tomorrow's universal secure device.",
]

THEMES = [
    {
        "id": "programmable-privacy",
        "tags": ["crypto", "policy"],
        "color": "green",
        "badge": "High conviction",
        "status": "MAINSTREAM WITHIN ~2 YEARS",
        "title": "Zero-knowledge proofs make every disclosure an intentional choice",
        "lead": "ZK proofs let you prove something about yourself or an asset without revealing it, and Vitalik expects most people to be using them unknowingly within two years.",
        "bullets": [
            "Shift from programmable assets to **programmable data** — a line of work that started with ZK proofs about 10 years ago.",
            "Room poll: only a few had used Zcash, an Ethereum privacy protocol, or a ZK rollup.",
            "Privacy is what tech progress usually costs: if you think with Claude, the model now has access to your thoughts.",
            "Attorney-client privilege and NDA material: not clear it is even **legal** to put that into many mainstream AI products.",
            "Data capture is exploding — phones went from one camera to three, likely 1,000+ cameras in the room; in ~10 years, five or 10 drones flying around.",
        ],
        "quote": {"text": "every bit of information that you reveal can be an intentional choice", "cite": "— Vitalik Buterin"},
        "watch": "Vitalik co-founded Ethereum and its privacy roadmap is his own agenda — the adoption timeline is an advocate's forecast.",
        "names": [
            {"name": "Zcash (ZEC)", "blurb": "Cited as the early privacy protocol few in the room had used.", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "ai-attacker-and-ui",
        "tags": ["crypto", "software"],
        "color": "amber",
        "badge": "Contested",
        "status": "AI FIXES ONE ATTACK LAYER, OPENS ANOTHER",
        "title": "AI hacks everything, audits everything, and replaces the wallet front end",
        "lead": "Any exploit will be found by AI, so formal-verification-grade security becomes mandatory — and AI as the new UI removes the front-end attack surface while adding its own.",
        "bullets": [
            "This year AI has broken out of sandboxes, taken down websites and found bugs and exploits across software — yet **Ethereum** and Bitcoin have not gone down.",
            "AI is already helping the Ethereum protocol find bugs and implement complex cryptography with formal proofs, at both protocol and application layer.",
            "About a month ago he updated his **ENS** record with no interface — a locally run Qwen model wrote the script in about 5 minutes.",
            "The Safe hack (~$1.4B lost last year) hit the layer between chain and user, not the contract — the layer that disappears if agents transact for you.",
            "New risks: is the AI itself safe, can it be prompt-injected, does it actually understand what it's doing on-chain.",
        ],
        "quote": {"text": "anything that has any um any exploit in it AI is going to find it", "cite": "— Vitalik Buterin"},
        "watch": "Vitalik frames AI-as-UI as a net trade, not a win: one class of front-end attacks shrinks while prompt injection and agent misunderstanding grow.",
        "names": [
            {"name": "Ethereum (ETH)", "blurb": "Has not gone down despite AI-driven hacking; AI already used for protocol bug-finding and formal verification.", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "2 years"},
            {"name": "Bitcoin (BTC)", "blurb": "Also has not gone down under the wave of AI-found exploits.", "stance": "POSITIVE VIEW", "conviction": "Low", "horizon": None},
        ],
    },
    {
        "id": "ethereum-two-years",
        "tags": ["crypto", "ai-infra", "semis"],
        "color": "green",
        "badge": "Forward view",
        "status": "ETHEREUM IN TWO YEARS",
        "title": "Bots trading with bots, and the hardware wallet as the universal secure device",
        "lead": "In two years Ethereum gives you more, cheaper and more private transactions, with AIs as both counterparty and app author — so security has to cover the full stack down to silicon.",
        "bullets": [
            "Already live: apps that make it easier to pay for AI inference and keep that payment private.",
            "Your average trading counterparty is probably already a bot; in two years the app may be bot-written too, or there may be **no apps** — just agents posting and interpreting on-chain offers.",
            "Digital capabilities improving at roughly **10x** the historical rate; the physical world is lagging but becoming digital.",
            "Blockchain gets the internet's problems first because it holds a lot of money — it is the front line for computing as a whole.",
            "Security is full stack — user, chain, internet and hardware: the other 'Si' that matters is silicon, element 14.",
        ],
        "quote": {"text": "what is a hardware wallet today is going to become the universal secure device of tomorrow", "cite": "— Vitalik Buterin"},
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F510", "tag": "Crypto", "title": "Track ZK rollups and privacy layers as the next mainstream crypto rail, not a niche"},
    {"icon": "\U0001F916", "tag": "Security", "title": "Assume any exploitable code gets found by AI — favor protocols investing in formal verification"},
    {"icon": "\U0001F9E0", "tag": "AI privacy", "title": "Keep privileged or NDA material out of mainstream AI tools; prefer local models for sensitive work"},
    {"icon": "\U0001F4B3", "tag": "Crypto", "title": "Watch agent-driven on-chain activity and AI-inference payments as Ethereum's next demand driver"},
    {"icon": "\U0001F6E1️", "tag": "Hardware", "title": "Treat hardware wallets and secure silicon as core infrastructure, not an accessory"},
]

HOT_TAKES = [
    {"take": "within two years quite possibly the majority of people will have used one of those things without even knowing it", "cite": "— Vitalik Buterin", "why": "dated adoption call on ZK/privacy tech"},
    {"take": "GPT7 is going to find it quad 7 is going to find it deepse 7 is going to find it they're all going to find it", "cite": "— Vitalik Buterin", "why": "any exploit will be found; security becomes mandatory"},
    {"take": "I think AI is going to become the new UI", "cite": "— Vitalik Buterin", "why": "wallet/dapp front ends replaced by agents"},
    {"take": "Possibly in two years there will be no applications. There will just be bots making onchain offers", "cite": "— Vitalik Buterin", "why": "dated, radical call on app layer"},
    {"take": "The blockchain world gets them first", "cite": "— Vitalik Buterin", "why": "crypto as the internet's front line for AI-era problems"},
]

CLAIMS = [
    {"who": "Vitalik Buterin", "claim": "The majority of people will have used a ZK proof, privacy protocol or ZK rollup without knowing it.", "metric": "share of people using ZK/privacy tech", "target": "majority", "by": "2028", "condition": None, "entity": None},
    {"who": "Vitalik Buterin", "claim": "Ethereum will offer many more, much cheaper and more private transactions than today.", "metric": "transaction volume, cost, privacy", "target": "higher / cheaper / more private", "by": "2028", "condition": None, "entity": "Ethereum (ETH)"},
    {"who": "Vitalik Buterin", "claim": "On-chain applications may themselves be written by bots, or replaced by agents posting and reading on-chain offers.", "metric": "bot-written apps", "target": "possibly no apps, just agents", "by": "2028", "condition": None, "entity": "Ethereum (ETH)"},
    {"who": "Vitalik Buterin", "claim": "Five or 10 drones will be flying around in a room like this one.", "metric": "drones per room", "target": "5-10", "by": "~2036", "condition": None, "entity": None},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F4DA", "title": "Sources referenced: none named — a solo keynote built on Vitalik's own experience and a live room poll.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "Zero-knowledge proof", "def": "Cryptography that proves a statement about data is true without revealing the data itself."},
    {"term": "ZK rollup", "def": "An Ethereum scaling layer that batches transactions off-chain and posts a validity proof on-chain."},
    {"term": "Formal verification", "def": "Mathematically proving code has the properties it is supposed to have, rather than only testing it."},
    {"term": "ENS", "def": "Ethereum Name Service — human-readable names mapped to on-chain addresses and records."},
    {"term": "Prompt injection", "def": "Hidden instructions in content an AI reads that hijack what the AI does."},
]
