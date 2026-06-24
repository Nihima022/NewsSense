from turtledemo.sorting_animate import instructions1

from numpy.lib.recfunctions import join_by

from Fact_Checking_Agent import checking_items
from LLM_model import structured_model

from agents import function_tool
from agents import Agent

from pydantic import BaseModel

class summarize_item(BaseModel):
    summary:str

@function_tool
def summarize_news(news_article:str):
    """
    Summarize a given news article or combined news content into 3–5 concise bullet points.

    This tool is used after:
    - a user directly provides an article
    OR
    - the Trending_News_Agent provides fetched news content

    Args:
        news_article (str): Full article text or combined news headlines.

    Returns:
        dict: Summarized bullet-point output.
    """
    sentences = news_article.split(".")         #Split the whole paragraph in sentences

    matched_news=[]

    for sentence in sentences:
        sentence=sentence.strip()      #Remove Extra space from sentences

        if sentence:
            matched_news.append(sentence)

        if len(matched_news)==5:
            break

    if not matched_news:
        return {
            "summary":"No matched news article"
        }

    summary=[]
    for points in matched_news:
        bullet_point= f"-{points}"
        summary.append(bullet_point)

    return {
        "summary":summary
    }

new_summarizer_agent=Agent(
    name="News Summarizer Agent",
    instructions="""
    You are a News Summarizer Agent.

    Your job is to summarize long news articles or multiple news headlines into 3–5 bullet points.

    Workflow:
    1. Accept article text or combined news content.
    2. Use summarize_news tool.
    3. Extract key points.
    4. Return concise bullet summaries.

    Rules:
    - Always summarize only the given content.
    - Never invent extra details.
    - Keep summaries short and factual.
    - Limit to 3–5 bullets.
    """,
    tools=[summarize_item],
    output_type= checking_items,
    handoff_description= """Handles summarization of long news articles ,multiple trending headlines, pasted news reports"""
)
