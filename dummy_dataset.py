#Data for Trending_News_Agent
TRENDING_NEWS_DB = {
    "ai": [
        {
            "title": "Meta releases Llama 3.2 with breakthrough reasoning abilities",
            "source": "Reuters",
            "category": "AI"
        },
        {
            "title": "OpenAI enhances GPT-4 Turbo with faster inference and lower cost",
            "source": "TechCrunch",
            "category": "AI"
        },
        {
            "title": "Google Gemini 2.0 rumors spark excitement in developer community",
            "source": "The Verge",
            "category": "AI"},
        {
            "title": "Anthropic Claude 3.5 sets new benchmark in safety alignment",
            "source": "Nature AI",
            "category": "AI"},
        {
            "title": "AI agents now outperform humans in coding competitions",
            "source": "MIT Tech Review",
            "category": "AI"}
    ],

    "technology": [
        {
            "title": "Apple unveils AI-powered iOS 19 with on-device intelligence",
            "source": "Apple Newsroom",
            "category": "Tech"
        },
        {
            "title": "Samsung launches foldable AI smartphone with real-time translation",
            "source": "Samsung Press",
            "category": "Tech"
        },
        {
            "title": "NVIDIA announces next-gen AI chip for trillion-parameter models",
            "source": "NVIDIA Blog",
            "category": "Tech"},
        {
            "title": "Microsoft integrates Copilot into Windows system level",
            "source": "Microsoft News",
            "category": "Tech"},
        {
            "title": "Tesla improves self-driving using neural network upgrade",
            "source": "Reuters",
            "category": "Tech"}
    ],

    "finance": [
        {
            "title": "Bitcoin reaches new all-time high amid global adoption surge",
            "source": "CoinDesk",
            "category": "Crypto"
        },
        {
            "title": "Global stock markets rise due to AI-driven tech boom",
            "source": "Bloomberg",
            "category": "Finance"
        },
        {
            "title": "Tesla shares jump 18% after AI announcement",
            "source": "CNBC",
            "category": "Finance"
        },
        {
            "title": "Gold prices fall as investors shift to tech equities",
            "source": "WSJ",
            "category": "Finance"
        },
        {
            "title": "US Federal Reserve signals stable interest rate policy",
            "source": "Reuters",
            "category": "Finance"
        }
    ],

    "world": [
        {
            "title": "UN proposes global AI regulation framework for safety",
            "source": "UN News",
            "category": "World"
        },
        {
            "title": "US-China semiconductor tensions escalate again",
            "source": "BBC",
            "category": "World"
        },
        {
            "title": "EU passes strict digital privacy laws for AI systems",
            "source": "EU News",
            "category": "World"
        },
        {
            "title": "India launches national AI education initiative",
            "source": "India Today",
            "category": "World"
        },
        {
            "title": "Climate summit highlights AI role in climate prediction",
            "source": "Reuters",
            "category": "World"}
    ],

    "war": [
        {
            "title": "Border conflict escalates between two neighboring countries",
            "source": "Al Jazeera",
            "category": "War"
        },
        {
            "title": "Ceasefire talks collapse after overnight airstrikes",
            "source": "Reuters",
            "category": "War"
        },
        {
            "title": "Military drones deployed in ongoing regional conflict",
            "source": "BBC",
            "category": "War"
        },
        {
            "title": "UN calls emergency meeting over escalating war tensions",
            "source": "UN News",
            "category": "War"
        },
        {
            "title": "Cyber warfare attacks reported on critical infrastructure",
            "source": "CyberNews",
            "category": "War"
        }
    ],

    "politics": [
        {
            "title": "Major election results shock political analysts worldwide",
            "source": "BBC Politics",
            "category": "Politics"
        },
        {
            "title": "New policy reforms announced in US government",
            "source": "Washington Post",
            "category": "Politics"
        },
        {
            "title": "EU leaders debate AI regulation and digital rights",
            "source": "Politico",
            "category": "Politics"
        },
        {
            "title": "Parliament passes controversial surveillance law",
            "source": "Reuters",
            "category": "Politics"
        },
        {
            "title": "Diplomatic tensions rise between global superpowers",
            "source": "Al Jazeera",
            "category": "Politics"
        }
    ],

    "cricket": [
        {
            "title": "India wins thrilling match against Pakistan in final over",
            "source": "ESPN Cricinfo",
            "category": "Sports"
        },
        {
            "title": "ICC announces new T20 rules for upcoming world cup",
            "source": "ICC",
            "category": "Sports"
        },
        {
            "title": "Virat Kohli scores record century in international match",
            "source": "Cricbuzz",
            "category": "Sports"
        },
        {
            "title": "Australia dominates Ashes series with strong performance",
            "source": "BBC Sport",
            "category": "Sports"},
        {
            "title": "IPL sees record-breaking auction bids for young players",
            "source": "ESPN",
            "category": "Sports"
        }
    ],

    "fifa": [
        {
            "title": "FIFA World Cup qualifiers begin with shocking upsets",
            "source": "FIFA",
            "category": "Sports"
        },
        {
            "title": "Messi scores hat-trick in final international appearance",
            "source": "ESPN",
            "category": "Sports"
        },
        {
            "title": "VAR technology updated for upcoming FIFA tournaments",
            "source": "FIFA Tech",
            "category": "Sports"
        },
        {
            "title": "Underdog team reaches World Cup semi-finals unexpectedly",
            "source": "BBC Sport",
            "category": "Sports"
        },
        {
            "title": "FIFA announces new stadium technology standards",
            "source": "FIFA",
            "category": "Sports"
        }
    ],

    "travel": [
        {
            "title": "Tourism surges as global travel restrictions ease",
            "source": "CNN Travel",
            "category": "Travel"
        },
        {
            "title": "Top 10 safest travel destinations in 2026 revealed",
            "source": "Lonely Planet",
            "category": "Travel"
        },
        {
            "title": "Airlines adopt AI-based passenger experience systems",
            "source": "Skift",
            "category": "Travel"
        },
        {
            "title": "New visa policies simplify international travel",
            "source": "IATA",
            "category": "Travel"
        },
        {
            "title": "Luxury travel trends shift toward eco-tourism",
            "source": "National Geographic",
            "category": "Travel"
        }
    ]
}

#Data for fact_checking_agent
FACT_CHECK_DB = [

    # ================= AI =================
    {
        "claim": "Meta released Llama 3.2 with breakthrough reasoning abilities",
        "verdict": "true",
        "evidence": "Reuters confirms Meta has released Llama 3.2 with improved reasoning capabilities.",
        "source": "Reuters"
    },
    {
        "claim": "OpenAI shut down GPT-4 Turbo due to safety issues",
        "verdict": "false",
        "evidence": "No credible reports confirm shutdown. In fact, GPT-4 Turbo is actively maintained.",
        "source": "TechCrunch"
    },
    {
        "claim": "Google is secretly testing Gemini 2.0 internally",
        "verdict": "uncertain",
        "evidence": "Rumors exist in developer communities, but no official confirmation from Google.",
        "source": "The Verge"
    },

    # ================= TECHNOLOGY =================
    {
        "claim": "Apple launched AI-powered iOS 19 with on-device intelligence",
        "verdict": "true",
        "evidence": "Apple Newsroom officially announced AI features in iOS 19.",
        "source": "Apple Newsroom"
    },
    {
        "claim": "Samsung banned foldable smartphones globally",
        "verdict": "false",
        "evidence": "Samsung has instead expanded foldable smartphone production.",
        "source": "Samsung Press"
    },
    {
        "claim": "NVIDIA is working on trillion-parameter AI chips",
        "verdict": "true",
        "evidence": "NVIDIA Blog confirms development of next-generation AI chips.",
        "source": "NVIDIA Blog"
    },

    # ================= FINANCE =================
    {
        "claim": "Bitcoin reached a new all-time high due to global adoption",
        "verdict": "true",
        "evidence": "CoinDesk reports Bitcoin hitting a record high amid adoption surge.",
        "source": "CoinDesk"
    },
    {
        "claim": "Tesla stock crashed after AI announcement",
        "verdict": "false",
        "evidence": "Tesla shares actually jumped 18% after the AI announcement.",
        "source": "CNBC"
    },
    {
        "claim": "Gold prices dropped as investors moved to tech stocks",
        "verdict": "true",
        "evidence": "WSJ confirms gold decline due to tech equity shift.",
        "source": "WSJ"
    },

    # ================= WORLD =================
    {
        "claim": "UN proposed a global AI regulation framework for safety",
        "verdict": "true",
        "evidence": "UN News confirmed proposal of global AI governance framework.",
        "source": "UN News"
    },
    {
        "claim": "US and China signed a full semiconductor peace agreement",
        "verdict": "false",
        "evidence": "No such agreement has been signed; tensions remain high.",
        "source": "BBC"
    },
    {
        "claim": "India launched a national AI education initiative",
        "verdict": "true",
        "evidence": "India Today reports national-level AI education program launch.",
        "source": "India Today"
    },

    # ================= WAR =================
    {
        "claim": "Ceasefire talks collapsed after overnight airstrikes",
        "verdict": "true",
        "evidence": "Reuters confirms collapse of ceasefire negotiations.",
        "source": "Reuters"
    },
    {
        "claim": "UN declared end of all global conflicts",
        "verdict": "false",
        "evidence": "No such declaration has been made by the UN.",
        "source": "UN News"
    },

    # ================= POLITICS =================
    {
        "claim": "EU passed strict AI surveillance and digital rights law",
        "verdict": "true",
        "evidence": "Reuters and EU News confirm new AI regulation policies.",
        "source": "EU News"
    },
    {
        "claim": "US government banned all AI systems nationwide",
        "verdict": "false",
        "evidence": "No such ban exists; AI regulation is ongoing but not a full ban.",
        "source": "Washington Post"
    },

    # ================= CRICKET =================
    {
        "claim": "India defeated Pakistan in a last-over thriller match",
        "verdict": "true",
        "evidence": "ESPN Cricinfo confirms India’s victory in final over.",
        "source": "ESPN Cricinfo"
    },
    {
        "claim": "ICC canceled all T20 world cup events",
        "verdict": "false",
        "evidence": "ICC actually introduced new T20 rules instead of canceling events.",
        "source": "ICC"
    },

    # ================= FIFA =================
    {
        "claim": "Messi scored a hat-trick in his final international match",
        "verdict": "true",
        "evidence": "ESPN reports Messi’s final match performance with hat-trick.",
        "source": "ESPN"
    },
    {
        "claim": "FIFA banned VAR technology globally",
        "verdict": "false",
        "evidence": "FIFA actually upgraded VAR systems for upcoming tournaments.",
        "source": "FIFA Tech"
    },

    # ================= TRAVEL =================
    {
        "claim": "Global tourism surged after travel restrictions were lifted",
        "verdict": "true",
        "evidence": "CNN Travel reports increase in global tourism.",
        "source": "CNN Travel"
    },
    {
        "claim": "Airlines stopped using AI systems for passenger services",
        "verdict": "false",
        "evidence": "Airlines are actually increasing AI-based systems for better experience.",
        "source": "Skift"
    }
]