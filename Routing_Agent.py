from LLM_model import structured_model

from pydantic import BaseModel

from typing import List

from agents import Agent
from agents import function_tool

from Fact_Checking_Agent import fact_checking_agent, checking_items
from Trending_News_Agent import trending_news_agent
from News_Summarizer_Agent import new_summarizer_agent

class conversation(BaseModel):
    output: List[str]

@function_tool()
def get_actual_agent(user_query:str):
    """
    Detect user intent and route to the proper specialist agent.Supports multiple intents.
    """
    query=user_query.lower().strip()
    get_output=[]

    trending_news_list=["trending", "latest", "news", "happening", "update"]
    fact_checking_list=["verify", "fact check", "is it true", "did", "claim"]
    summarizer_list=["summarize", "summary", "shorten"]

    for word in trending_news_list:
        if word in query:
            get_output.append(word)
            break

    for word in fact_checking_list:
        if word in query:
            get_output.append(word)
            break

    for word in summarizer_list:
        if word in query:
            get_output.append(word)

    if not get_output:
        return {
            "output": "Not Found in this agent function",
        }

    return {
        "output": get_output,
    }
Routing_Agent=Agent(
    name="Controller Agent",
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
    tools=[get_actual_agent],
    handoffs=[fact_checking_agent, new_summarizer_agent, trending_news_agent],
    output_type= conversation
)
