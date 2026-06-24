from pydantic import BaseModel
from agents import function_tool, Agent

from dummy_dataset import TRENDING_NEWS_DB

from LLM_model import structured_model

class news_item(BaseModel):
    title: str
    source: str
    category: str

category_keywords={
    "ai":["ai","openai","chatgpt","robot","llm"],
    "technology": ["tech", "iphone", "apple", "samsung", "nvidia", "microsoft"],
    "finance": ["bitcoin", "crypto", "stock", "market", "gold", "finance"],
    "world": ["un", "global", "world", "international", "climate"],
    "war": ["war", "conflict", "airstrike", "military", "ceasefire"],
    "politics": ["election", "government", "parliament", "policy", "law"],
    "fifa": ["football", "fifa", "messi", "ronaldo", "world cup"],
    "cricket": ["cricket", "icc", "kohli", "ipl", "ashes"],
    "travel": ["travel", "tourism", "visa", "airline", "destination"],
    "accident": ["accident", "crash", "earthquake", "flood", "explosion"]
}

@function_tool()
def trending_news_tool(topic:str):
    """ Fetch trending news based on user-provided topic"""
    topic=topic.lower().strip()     #lowercase the input topic
    matched_news=[]                 #an empty list of dict for matching news

    for category_search, news_list in TRENDING_NEWS_DB.items():
        # Case-1: if the topic is matched with the categories of database
        if topic == category_search:
            matched_news.extend(news_list)     #use extend because it unpacks list and adds one by one
            continue

        #Case-2: if the topic is in category_keywords,not in direct category
        category= category_keywords.get(category_search,[])   #it returns list
        if topic in category:
            matched_news.extend(news_list)
            continue

        #Case-3: if topic is in title
        for news in news_list:
            news_title=news["title"].lower().strip()  #extract the title from the news_list dict

            if topic in news_title:
                matched_news.append(news)

    if not matched_news:
        return []

    return {
        "Topic": topic,
        "Result": matched_news
    }

trending_news_agent= Agent(
    name= "Trending_News_Searching_Agent",
    instructions= """
    You are a Trending News Agent.

    Your job is to find relevant trending news using the tool.

    Rules:
    - Always use trending_news_tool.
    - Use tool results only.
    - Return structured response with query and results.
    - Do not invent news.
    """,
    tools=[trending_news_tool],
    model=structured_model(),
    output_type=news_item,
    handoff_description="""
     Handles trending news, breaking news, and topic-based news queries.
    """
)



