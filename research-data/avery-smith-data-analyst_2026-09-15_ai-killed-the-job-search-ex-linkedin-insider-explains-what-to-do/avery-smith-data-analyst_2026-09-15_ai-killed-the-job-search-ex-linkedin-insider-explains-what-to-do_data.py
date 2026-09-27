"""Jeremy Schifeling on the Data Career Podcast (w/ Avery Smith) — "AI Killed The Job Search:
Ex-LinkedIn Insider Explains What To Do" (2026-09-15)"""

META = {
    "title": "AI Killed The Job Search: Ex-LinkedIn Insider Explains What To Do",
    "channel": "Avery Smith | Data Analyst",
    "speakers": "Jeremy Schifeling (ex-LinkedIn executive, early OpenAI partner) interviewed by Avery Smith",
    "date": "2026-09-15",
    "video_url": "https://www.youtube.com/watch?v=yBpi_wzxrDk",
    "thread_line": "6 threads · the AI mass-apply arms race that's failing everyone, why a referral is now "
                    "worth ~20x a cold application, how to actually earn one, the two types of referral "
                    "that matter, where AI genuinely helps vs. hurts a job search, and why fewer/better "
                    "applications beat more",
    "category": "dev",
}

SNAPSHOT = [
    "Both job seekers and recruiters have weaponized AI, producing a mutual arms race — Jeremy Schifeling says the result is that purely mechanical, AI-driven mass-applying now converts at roughly **0%**, not 0.01%.",
    "AI's real-world reliability gap matters: he cites that AI solves about **66%** of a given task well, leaving a third needing manual correction — and that programmers who felt they were saving 20-30 hours/week with AI were actually measured as 20-30 hours/week *slower* than expected.",
    "A referral was worth **10x** a cold application in 2016; Jeremy now estimates it's worth roughly **20x** in 2026, because online applicant volume has exploded since.",
    "Employers benefit too — referred hires are more likely to accept the offer, stay longer, and perform better — which is why some companies (Google, per Jeremy) pay bonuses up to **$25,000** for a strong referral, and some firms now only accept referred candidates.",
    "The practical playbook: find shared affinity (alma mater, volunteer group, church, employer), get a warm introduction, then ask for *advice* rather than pitching yourself — a 'golden question' script does double duty as relationship-building and referral-generation.",
    "AI is genuinely useful for two narrow jobs — checking your target role/fit and diagnosing resume/JD keyword gaps — but crosses a line the moment it invents accomplishments you didn't actually do.",
    "Core recommendation: shrink your applicant list and raise your per-application acceptance rate (aim for 1-10%) instead of maximizing volume — quality over quantity, like a diversified portfolio instead of one big bet.",
]

THEMES = [
    {
        "id": "ai-arms-race",
        "tags": ["career", "dev-workflow"],
        "color": "red",
        "badge": "Structural critique",
        "status": "ONGOING — both sides now using AI",
        "title": "The AI arms race between job seekers and recruiters is a lose-lose",
        "lead": "Job seekers and recruiters have both armed themselves with AI, and the result is more noise, more fake data, and a mass-apply success rate of effectively zero.",
        "bullets": [
            "Job seekers now use resume/cover-letter chatbots (GPT, Claude) to mass-apply; recruiters have countered with AI-driven application screening — both sides are trying to out-scale the other, and Jeremy says \"I don't think anyone is winning.\"",
            "Recruiters report the job has gotten worse, not better, because the volume of applications to process has exploded and a large share of it is AI-generated fake or low-signal data.",
            "The reliability gap is real: AI solves roughly **66%** of a given task well but leaves a third needing manual correction — and in a cited early-AI-coding study, programmers who reported \"saving 20-30 hours a week\" were actually measured making progress 20-30 hours/week *slower* than expected.",
            "Purely mechanical, randomized mass-applying (\"apply to 1,000 jobs, don't stop until done\") converts at effectively **0%**, not the 0.01% people assume — throwing more darts doesn't help when the dartboard is thousands of feet away.",
            "Why people keep doing it anyway: mass-applying (or asking an AI agent to do it) delivers an immediate dopamine hit — \"I did something today\" — while real networking (sending messages that may get no reply) doesn't feel good even though it works better.",
        ],
        "quote": {"text": "Applying for jobs randomly in a completely mechanical way results in a success rate of not 0.01%, but 0%.", "cite": "— Jeremy Schifeling"},
        "watch": None,
        "names": None,
    },
    {
        "id": "referral-multiplier",
        "tags": ["career"],
        "color": "green",
        "badge": "Confirmed data point",
        "status": "UPDATED ESTIMATE — 2016 vs. 2026",
        "title": "A referral is worth roughly 20x a cold application today, up from 10x in 2016",
        "lead": "The hiring-probability gap between a referred candidate and an online applicant has roughly doubled over the past decade as applicant volume exploded.",
        "bullets": [
            "In 2016, a referred candidate was about **10x** more likely to be hired than an online applicant for the same role (Jeremy's figure, discussed relative to Adobe as an example).",
            "By 2026, Jeremy estimates that advantage has grown to roughly **20x**, because AI-assisted mass-applying has pushed online applicant volume far higher than in 2016.",
            "Employers have a rational reason to favor referrals: referred hires are more likely to accept the offer, more likely to stay long-term, and tend to perform better because they were vetted by someone inside.",
            "Some companies pay real money for this — the highest referral bonus Jeremy saw at Google was **$25,000**; more typical bonuses run **$500-$1,000**, and Avery cites a **$5,000** referral bonus example from his own network.",
            "The value is strong enough that some hiring managers now refuse open applications entirely — one company told Avery, when he offered to post a role publicly, \"No, that's fine. We are only looking for recommended candidates.\"",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
    {
        "id": "building-trust",
        "tags": ["career", "mindset"],
        "color": "green",
        "badge": "Recommendation",
        "status": "ACTIONABLE",
        "title": "How to actually earn a referral: shared affinity, not cold outreach",
        "lead": "Trust is the real currency once resumes, cover letters, and LinkedIn profiles are all AI-polished and indistinguishable — and trust is built through concrete shared context, not credentials.",
        "bullets": [
            "AI has made every resume, cover letter, and LinkedIn profile look equally polished, which destroys their differentiating power — a warm relationship with an insider is now the stronger signal.",
            "Concrete affinity groups that work: shared alma mater, shared employer alumni, volunteer organizations (searching \"Google employees volunteering at Habitat for Humanity\" on LinkedIn surfaces 1,000+ current Google employees), and even shared religious community — Jeremy says he replies faster to messages from his own alma mater or church.",
            "The psychology behind why this works is a form of generativity — an instinct (possibly evolutionary) to want to help the next generation succeed; Jeremy frames it as \"giving is just as important as receiving,\" and says he's more willing to help someone who frames a message as seeking his mentorship, not asking for a favor.",
            "Even without shared credentials, persistence in adding value works: Jeremy hired someone based in Africa who had commented on his LinkedIn posts every day for six months before he reached out to ask who they were — though he notes that person had to repeat outreach roughly **89** times without payoff before it worked.",
            "You don't need a privileged background for this to work — Avery's own example: he skipped a midterm to attend a STEM job fair and got hired, while a higher-performing classmate who studied instead did not; the intermediate goal (grades, perfect resume) isn't the actual goal (getting noticed by a person).",
            "Self-doubt is the main blocker Jeremy sees in the students he works with — people assume they \"don't deserve\" a referral or that someone else is more qualified, when in reality most organizations badly need the value a motivated new hire can add.",
        ],
        "quote": {"text": "I am giving a gift to others... don't forget that giving is just as important as receiving.", "cite": "— Jeremy Schifeling"},
        "watch": None,
        "names": None,
    },
    {
        "id": "two-types-of-referrals",
        "tags": ["career"],
        "color": "green",
        "badge": "Recommendation",
        "status": "ACTIONABLE",
        "title": "There are two kinds of referrals — and the checkbox kind is the weak one",
        "lead": "A referral logged into the Applicant Tracking System is a small checkbox; a referral that comes from a recruiter or hiring manager who knows you personally is what actually moves the needle.",
        "bullets": [
            "The basic/mechanical referral is someone entering your name into the company's ATS — recruiters and hiring managers can see it, but Jeremy calls it \"just a small checkbox.\"",
            "The stronger method is contacting the recruiter or hiring manager directly and explaining your specific strengths — this works because recruiters are the one person in the org whose own career success is tied to finding genuinely good talent, unlike a hiring manager juggling dozens of open roles.",
            "Never cold-DM or cold-email a stranger — Jeremy says most people aren't active on LinkedIn and a cold message can sit unread indefinitely. Find a common connection for a warm introduction instead.",
            "Once introduced, don't lead with an elevator pitch about yourself — ask about *their* journey instead (\"How did you get from X to Y? What surprised you along the way?\"). Jeremy's 'golden question' script: ask what they'd do differently if they were job-hunting today, and why — people who share advice often volunteer a referral unprompted.",
            "Avery demonstrated a related tool built for this exact problem: his site findajob.com / Premium Data Jobs lists recruiters currently hiring (with name, title, company, LinkedIn profile) and flags job postings by how few public comments they have, so a thoughtful direct message stands out against the crowd.",
        ],
        "quote": {"text": "If you ask for a recommendation, you get advice, and if you receive advice, you get recommendations.", "cite": "— a headhunter, quoted by Jeremy Schifeling"},
        "watch": None,
        "names": None,
    },
    {
        "id": "where-ai-helps-and-hurts",
        "tags": ["career", "dev-workflow"],
        "color": "amber",
        "badge": "Mixed verdict",
        "status": "CONTESTED — useful for two jobs, risky beyond them",
        "title": "Where AI genuinely helps a job search — and exactly where it crosses the line",
        "lead": "AI is a legitimately good fit-checker and gap-analyzer, but the moment it starts inventing your accomplishments, it becomes a liability you'll have to answer for in the interview.",
        "bullets": [
            "Good use #1 — career-fit check: feed AI your strengths and passions and ask it to recommend roles, similar to the Japanese concept of *ikigai*; because AI has training data on nearly every job that's ever existed, it might surface a better fit (e.g. a healthcare BI role) than the obvious path (e.g. data scientist).",
            "Good use #2 — gap analysis: paste a job description and your resume into ChatGPT/Claude/Perplexity and ask what important keywords are missing — this is exactly what an ATS is doing anyway, so it's a legitimate way to reverse-engineer it.",
            "The line gets crossed when someone says \"acknowledge all the skills in my experience section and apply right away\" — that produces a fabricated accomplishment story that falls apart the moment a future boss asks about it in person.",
            "On AI tutoring: tools with a Socratic/learning mode (present in Gemini, GPT, and likely Claude) can guide rather than hand over answers, but Jeremy compares using it well to Odysseus tying himself to the mast — you have to deliberately resist the pull toward instant answers to get real learning value.",
            "His mental model for over-trusting fluent AI output: AI is like a sophisticated British accent — precise, assertive, sounds 20 IQ points smarter — while still making intern-level mistakes underneath.",
        ],
        "quote": {"text": "I think AI is similar to a British accent... despite that sophisticated accent, he makes mistakes at an intern level.", "cite": "— Jeremy Schifeling"},
        "watch": None,
        "names": None,
    },
    {
        "id": "focus-over-volume",
        "tags": ["career"],
        "color": "green",
        "badge": "Recommendation",
        "status": "ACTIONABLE",
        "title": "Buy fewer, better lottery tickets: shrink your list, raise your acceptance rate",
        "lead": "Jeremy's closing first principle is to deliberately cut the number of companies you apply to and invest that saved time into raising your odds at each one.",
        "bullets": [
            "His core advice: reduce the number of companies you target, and push your personal acceptance rate up toward 1-10% rather than accepting a 0.01% (or effectively 0%) mass-apply rate — quality over quantity is \"a basic mathematical principle,\" not just a platitude.",
            "He frames it like portfolio diversification: don't put every egg in one basket (obsessing over a single dream company), but also don't scatter effort across a thousand low-probability bets.",
            "For skeptics of the 20x referral-multiplier claim, his suggested compromise is a middle path — cut mass applications from 100 to 80, and add just a couple of genuine relationship-building messages, rather than an all-or-nothing switch.",
        ],
        "quote": None,
        "watch": None,
        "names": None,
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F3AF", "tag": "Careers", "title": "Cut your target-company list and aim to raise your per-application acceptance rate toward 1-10%, instead of maximizing how many applications you send."},
    {"icon": "\U0001F91D", "tag": "Careers", "title": "Find one real point of shared affinity (alma mater, employer alumni, volunteer group) before you message anyone about a job."},
    {"icon": "\U0001F4AC", "tag": "Careers", "title": "Lead with a question about their journey, not an elevator pitch about yourself, when you get a warm introduction."},
    {"icon": "\U0001F916", "tag": "AI ethics", "title": "Use AI to check your target role and diagnose resume/JD keyword gaps — never to write accomplishments you didn't actually have."},
    {"icon": "\U0001F4E7", "tag": "Careers", "title": "Contact the recruiter or hiring manager directly instead of relying on the ATS checkbox referral — that's the version that actually moves your odds."},
]

HOT_TAKES = [
    {"take": "Applying for jobs randomly in a completely mechanical way results in a success rate of not 0.01%, but 0%.", "cite": "— Jeremy Schifeling", "why": "specific, checkable dismissal of the dominant AI-mass-apply strategy"},
    {"take": "I don't think anyone is winning [the AI arms race between recruiters and job seekers].", "cite": "— Jeremy Schifeling", "why": "blunt claim that a widely-hyped AI use case is net-negative for both sides"},
    {"take": "Think about what a recruiter's job entails. Their job is not to find the world's best talent, but to hire the right people as quickly as possible.", "cite": "— Jeremy Schifeling", "why": "unflattering, specific characterization of an entire profession"},
    {"take": "I think AI is similar to a British accent... despite that sophisticated accent, he makes mistakes at an intern level.", "cite": "— Jeremy Schifeling", "why": "memorable, pointed claim about over-trusting fluent AI output"},
    {"take": "A referral increases your chances of getting a job by 20 times.", "cite": "— Jeremy Schifeling", "why": "specific, checkable multiplier a listener could hold him to"},
    {"take": "The highest referral bonus when I worked at Google was $25,000.", "cite": "— Jeremy Schifeling", "why": "specific dollar figure from firsthand experience"},
]

CLAIMS = [
    {"who": "Jeremy Schifeling", "claim": "A referred candidate was about 10x more likely to be hired than an online applicant in 2016", "metric": "referral hiring-probability multiplier", "target": "10x", "by": "2016", "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "A referred candidate is now roughly 20x more likely to be hired than an online applicant", "metric": "referral hiring-probability multiplier", "target": "20x", "by": "2026", "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "The highest employee-referral bonus he saw while at Google was $25,000", "metric": "referral bonus", "target": "$25,000", "by": None, "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "AI solves about two-thirds of a given task well, leaving the remainder needing manual correction", "metric": "AI task-completion rate", "target": "66%", "by": None, "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "Programmers who reported saving 20-30 hours/week using AI were measured making progress 20-30 hours/week slower than expected", "metric": "measured vs. perceived AI productivity gain", "target": "20-30 hours/week slower than perceived", "by": None, "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "Mechanical, randomized mass-applying to jobs converts at effectively 0%", "metric": "application conversion rate", "target": "0%", "by": None, "condition": None, "entity": None},
    {"who": "Jeremy Schifeling", "claim": "LinkedIn now hosts 1.3 billion profiles", "metric": "platform profile count", "target": "1.3 billion", "by": None, "condition": None, "entity": "LinkedIn"},
]

RELATIONS = []

OTHER_NEWS = [
    {"icon": "\U0001F5C2️", "title": "Avery demoed his own platform, findajob.com (Premium Data Jobs), which lists recruiters actively hiring (55 listed at time of recording, with name/title/company/LinkedIn) and 121 premium job postings, ranked partly by which have the fewest public comments so a direct message stands out.", "tag": "Tool"},
    {"icon": "\U0001F4DA", "title": "Sources referenced this episode: Jeremy Schifeling's own books and podcast on the data job market; an unnamed headhunter's line about advice-and-referrals being reciprocal; a psychology concept (locus of control) and a second concept describing the instinct to help the next generation succeed, both cited without a specific named source.", "tag": "Sources"},
]

GLOSSARY = [
    {"term": "ATS (Applicant Tracking System)", "def": "The database companies use to log and screen applicants — a 'referral' logged only in the ATS is the weak, checkbox version Jeremy contrasts with a direct human referral."},
    {"term": "Locus of control", "def": "A psychology concept for whether someone attributes outcomes to forces outside themselves (external) or to their own actions (internal) — Jeremy frames focusing on the one small action you can control today as the antidote to feeling powerless in a bad job market."},
    {"term": "Generativity", "def": "A concept (Erikson) describing the human drive, especially later in a career, to help the next generation succeed and leave a legacy — Jeremy cites it as the psychological reason senior people are often glad to help a stranger who reaches out respectfully."},
    {"term": "Ikigai", "def": "A Japanese concept for the intersection of what you're good at, what you love, and what the world needs — used here as a model for using AI to sanity-check whether your target job is actually the right fit before you invest in applying."},
]
