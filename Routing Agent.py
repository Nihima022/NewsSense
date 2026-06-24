from LLM_model import structured_model

from pydantic import BaseModel

from typing import List

from agents import Agent

from Fact_Checking_Agent import fact_checking_agent, checking_items
from Trending_News_Agent import trending_news_agent
from News_Summarizer_Agent import new_summarizer_agent

from Trending_News_Agent import trending_news_tool
from Fact_Checking_Agent import fact_checking
from News_Summarizer_Agent import summarize_news

class conversation(BaseModel):
    trending_news: List[str]
    fact_checking:str
    summarize: List[str]

Routing_Agent=Agent(
    names=" Controller Agent",
    instructions=""" 
    You are the controller agent of NewsSense.

    Your job:
    1. Read the user's message.
    2. Detect intent.
    3. Route to the correct specialist agent.

    Routing rules:
    - trending_news_tool → Trending News Agent
    - fact_checking → Fact Checker Agent
    - summarize_news → News Summarizer Agent

    Never answer directly.
    Always route.
    """,
    model=structured_model,
    handoff=[fact_checking_agent, new_summarizer_agent, trending_news_agent],
    output_type= conversation
)
