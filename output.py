import asyncio

from agents import Runner, set_tracing_disabled
from pandas.core.computation.common import result_type_many

from Routing_Agent import Routing_Agent

from Trending_News_Agent import news_item, trending_news_tool, trending_news_agent
from News_Summarizer_Agent import summarize_item, summarize_news, new_summarizer_agent
from Fact_Checking_Agent import checking_items, fact_checking, fact_checking_agent

async def main():
    queries=["Summarize this article: Apple launched iOS 19 with new AI-powered features, stronger privacy tools, and better Siri integration. The update will roll out next month."]

    for query in queries:
        print("="*100)
        print("Query:",query)
        print("="*100)

        result = await Runner.run(Routing_Agent, query)
        response=result.final_output

        print(response)

        print("="*100)
        print("Final Output:")
        print("-"*100)

        if hasattr(response,"title"):
            print("Title:",response.title)
            print("Source:",response.source)
            print("Category:",response.category)

        elif hasattr(response, "claims"):
            print("Claim:",response.claims)
            print("Verdict:",response.verdict)
            print("Evidence:",response.evidence)
            print("Source:",response.source)

        elif hasattr(response, "summary"):
            print("Summary:",response.summary)

        else:
            print("No data found")

set_tracing_disabled(True)

if __name__=="__main__":
    asyncio.run(main())
