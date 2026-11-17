META = {
    "title": "Yann LeCun's $1B Bet Against LLMs [Part 2]",
    "channel": "Welch Labs",
    "speakers": "Yann LeCun (AMI Labs), Welch Labs narrator",
    "date": "2026-05-30",
    "video_url": "https://www.youtube.com/watch?v=v_jDvpEGTIg",
    "thread_line": "4 threads · V-JEPA 2 vs CLIP · VL-JEPA efficiency · LeCun vs VLA robots · AMI Labs roadmap",
    "category": "market",
    "region": "",
}

SNAPSHOT = [
    "Part 2 climbs the stack (vision encoder → VLM → VLA) and puts a JEPA alternative at each level.",
    "**V-JEPA 2** (Meta, 2025, 1M hours of video, up to 1B parameters) is trained with no language yet beats CLIP-style encoders on video understanding.",
    "**VL-JEPA** reached 35% vs 20% accuracy after 5M examples and beat 7B models on GQA with just 1.6B parameters.",
    "LeCun: \"VLAs are doomed\": behavioral cloning doesn't scale and there's no explicit planning.",
    "Reality check: JEPA takes 60 seconds to move a cup, and Le World Model plans only ~5 steps ahead on Push-T (15 with two hierarchy levels).",
    "AMI Labs plan: industrial pilots within 1-2 years, then become \"the main supplier of intelligent systems\" in 3-5 years.",
]

THEMES = [
    {
        "id": "vjepa-vlm",
        "tags": ["ai-infra"],
        "color": "green",
        "badge": "Strong evidence",
        "status": "META · V-JEPA 2 / VL-JEPA",
        "title": "Language-free vision and embedding-space targets beat their generative counterparts",
        "lead": "JEPA already competes in the vision half of VLMs and learns faster when the whole VLM predicts embeddings instead of text.",
        "bullets": [
            "OpenAI's 2021 CLIP matches image-caption pairs and underpins most multimodal LLM vision encoders. Natively it handles images only.",
            "**V-JEPA 2** learns by predicting embeddings of masked video patches. Swapped into a VLM, it set state-of-the-art video-understanding results \"contrary to conventional wisdom\".",
            "TempCompass reversed-pineapple test: ChatGPT 5.5 fails forwards and backwards in Welch Labs' testing, and only some Claude and Gemini versions get it right.",
            "AMI Labs' landing page: \"Real intelligence does not start in language. It starts in the world.\"",
            "Mushroom example: a generative VLM is penalized for a correct paraphrase. **VL-JEPA** maps both phrasings to nearby embeddings.",
            "VL-JEPA (Meta, late 2025): 35% vs 20% video classification after 5M examples, and on GQA it beats 7B models with 1.6B parameters.",
            "Being non-generative, it answers by nearest embedding among candidate answers, or through a trained text decoder.",
        ],
        "quote": None,
        "watch": "Still hybrid: V-JEPA 2 alignment uses a standard next-token LLM on the language side.",
        "names": [
            {"name": "Meta (META)", "blurb": "Trained V-JEPA 2 and VL-JEPA", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
            {"name": "OpenAI", "blurb": "CLIP, the language-supervised encoder JEPA competes with", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "vla-doomed",
        "tags": ["robotics", "ai-infra"],
        "color": "red",
        "badge": "Contested",
        "status": "PHYSICAL INTELLIGENCE PI0.7 VS JEPA",
        "title": "LeCun says VLAs are doomed, while VLAs keep generalizing in demos",
        "lead": "LeCun's critique is that VLAs rely on behavioral cloning and don't plan explicitly. The narrator shows VLAs are far ahead in real capability today.",
        "bullets": [
            "Physical Intelligence's PI0.7 VLA peels zucchini, folds pinwheels, takes out trash, and shuffles a key between grippers to open a lock.",
            "VLAs = VLM + action expert, trained end-to-end on human demonstrations captured with teleoperation controllers.",
            "LeCun: collecting demonstrations for every variation is \"only practical for a very small number of applications\". Faced with new situations, VLAs are brittle.",
            "Counter-evidence: Google's RT-2 (2023) moved a Coke can to a picture of Taylor Swift with no such demo. PI robots handle unseen microwave, paper-towel and air-fryer tasks.",
            "Second critique: no visibility into planning. The VLA is a black box from camera + text to joint positions.",
        ],
        "quote": {"text": "VLAs are doomed. I mean, they they basically don't work really well.", "cite": "— Yann LeCun"},
        "watch": "LeCun's company competes with the VLA approach he dismisses. The video's own comparison shows JEPA robotics far behind for now.",
        "names": [
            {"name": "Physical Intelligence", "blurb": "Builds the PI VLA robot models LeCun calls doomed", "stance": "NEGATIVE VIEW", "conviction": "High", "horizon": None},
            {"name": "Google (GOOGL)", "blurb": "RT-2 was the 2023 VLA generalization breakthrough", "stance": "CASUAL MENTION", "conviction": "None", "horizon": None},
        ],
    },
    {
        "id": "le-world-model",
        "tags": ["robotics"],
        "color": "amber",
        "badge": "Early",
        "status": "PUSH-T · 5 → 15 STEP HORIZON",
        "title": "Le World Model plans in embedding space, but only a few steps ahead",
        "lead": "A JEPA world model trained from pixels and actions learns Push-T physics well enough to plan, though horizon limits keep it to simple tasks.",
        "bullets": [
            "Learns from human Push-T trajectories but predicts *outcomes*, not human actions. A decoder shows a \"learned video game\" matching reality over 18 steps, with some drift.",
            "Planning uses the **cross-entropy method**: 500 random trajectories rolled out 5 actions per batch and scored by Euclidean distance to the goal embedding. A top-30 elite set resamples until it converges.",
            "Reliable only ~5 prediction loops ahead. Two-level hierarchical world models extend that to 15.",
            "LeCun's hierarchy analogy: NYU office to Paris means airport → taxi → stand up. \"Your cat can do hierarchical planning\" without language.",
            "Hope: the hierarchy emerges from training like CNN features, but it needs semi-expert trajectories, not random actions.",
        ],
        "quote": None,
        "watch": "The narrator compares it to LeCun's 30-year-old handwritten-digit nets: limited then, scaled later. Whether JEPA follows is open.",
        "names": None,
    },
    {
        "id": "ami-roadmap",
        "tags": ["ai-infra", "energy", "biotech"],
        "color": "green",
        "badge": "Speculative",
        "status": "1-2 YEARS INDUSTRIAL · 3-5 YEARS SCALE",
        "title": "AMI Labs targets complex systems you can't write equations for",
        "lead": "LeCun plans first to apply JEPA planning to industrial control problems, not consumer robots, aiming to gain experience rather than revenue.",
        "bullets": [
            "Targets: jet engines, whole airplanes, chemical plants, power plants, and diabetes patients' blood-sugar control.",
            "Also: steering stem cells into insulin-producing pancreas cells, and designing materials, catalysts and batteries.",
            "Excluded: robot arms, humanoids or NASA moon rockets, where dynamical equations can be written down.",
        ],
        "quote": {"text": "the hope is that, you know, we might become the main supplier of intelligence systems, whatever the application is", "cite": "— Yann LeCun"},
        "watch": None,
        "names": [
            {"name": "AMI Labs", "blurb": "Industrial pilots in 1-2 years, broad supplier ambition in 3-5", "stance": "POSITIVE VIEW", "conviction": "High", "horizon": "3-5 years"},
        ],
    },
]

TAKEAWAYS = [
    {"icon": "\U0001F441️", "tag": "AI research", "title": "Test language-free video encoders like V-JEPA 2 where temporal understanding matters"},
    {"icon": "\U0001F916", "tag": "Robotics", "title": "Weigh VLA generalization demos against LeCun's brittleness critique before betting on either camp"},
    {"icon": "\U0001F3ED", "tag": "Markets", "title": "Watch AMI Labs' first industrial pilots in 1-2 years as the real JEPA proof point"},
    {"icon": "\U0001F9ED", "tag": "Agents", "title": "Prefer agents that can predict consequences and plan explicitly when safety matters"},
]

HOT_TAKES = [
    {"take": "VLAs are doomed. I mean, they they basically don't work really well.", "cite": "— Yann LeCun", "why": "dismisses the leading robotics approach"},
    {"take": "your cat can do hierarchical planning. So, you know, they don't have language", "cite": "— Yann LeCun", "why": "planning needs no language"},
    {"take": "within a year or two uh we'll we'll try to apply the the whole JEPPA world model planning, etc., to a number of uh industrial applications", "cite": "— Yann LeCun", "why": "dated plan"},
    {"take": "we might become the main supplier of intelligence systems, whatever the application is", "cite": "— Yann LeCun", "why": "3-5 year ambition"},
]

CLAIMS = [
    {"who": "Yann LeCun", "claim": "JEPA-based approaches will overtake VLA approaches in robotics", "metric": "JEPA overtakes VLA", "target": "overtake", "by": None, "condition": None, "entity": "Physical Intelligence"},
    {"who": "Yann LeCun", "claim": "AMI Labs applies JEPA world-model planning to industrial applications", "metric": "industrial pilots", "target": "several", "by": "1-2 years", "condition": None, "entity": "AMI Labs"},
    {"who": "Yann LeCun", "claim": "AMI Labs becomes the main supplier of intelligent systems", "metric": "market position", "target": "main supplier", "by": "3-5 years", "condition": None, "entity": "AMI Labs"},
]

RELATIONS = [
    {"from": "AMI Labs", "rel": "competes_with", "to": "Physical Intelligence", "note": "JEPA world models vs VLA robot brains"},
    {"from": "AMI Labs", "rel": "criticizes", "to": "Physical Intelligence", "note": "LeCun calls VLAs doomed"},
]

OTHER_NEWS = []

GLOSSARY = [
    {"term": "CLIP", "def": "OpenAI's 2021 contrastive image-caption encoder used as the vision front-end of many VLMs."},
    {"term": "VLM / VLA", "def": "Vision-language model / vision-language-action model, the latter outputting robot controls."},
    {"term": "Behavioral cloning", "def": "Training a policy to imitate human demonstration actions."},
    {"term": "Cross-entropy method (CEM)", "def": "Sample trajectories, keep an elite set, refit and resample until the plan converges."},
    {"term": "Hierarchical world model", "def": "Stacked predictors: detailed short-term at the bottom, abstract long-term subgoals above."},
]
