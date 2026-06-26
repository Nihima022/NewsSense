import asyncio

from agents import (Runner, set_tracing_disabled, InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered)

from Routing_Agent import Routing_Agent

from Trending_News_Agent import news_item, trending_news_tool, trending_news_agent
from News_Summarizer_Agent import summarize_item, summarize_news, new_summarizer_agent
from Fact_Checking_Agent import checking_items, fact_checking, fact_checking_agent

async def main():
    queries=["What’s trending in AI today?",
    "Show me the latest finance news.",
    "What’s happening in cricket right now?",
    "Give me trending technology updates.",
    "Did Apple acquire OpenAI?",
    "Is it true that Bitcoin hit a new all-time high?",
    "Fact check this: Meta released Llama 3.2.",
    "Summarize this article: Apple launched iOS 19 with new AI-powered features, stronger privacy tools, and better Siri integration. The update will roll out next month.",
    "What’s trending in AI? Verify if Apple and OpenAI are partnering, then summarize the results.",
    "Show me the latest tech news, fact check whether Tesla improved self-driving with AI, and summarize everything.",
    "I want to travel.suggest me some places.",]

    try:
        for query in queries:
            print("=" * 100)
            print("Query:", query)
            print("=" * 100)

            result = await Runner.run(Routing_Agent, query)
            response = result.final_output

            print(response)

            print("=" * 100)
            print("Final Output:")
            print("-" * 100)

            if hasattr(response, "title"):
                print("Title:", response.title)
                print("Source:", response.source)
                print("Category:", response.category)

            elif hasattr(response, "claims"):
                print("Claim:", response.claims)
                print("Verdict:", response.verdict)
                print("Evidence:", response.evidence)
                print("Source:", response.source)

            elif hasattr(response, "summary"):
                print("Summary:", response.summary)

            else:
                print("No data found")

    except InputGuardrailTripwireTriggered as e:
        print("Input Guardrail Triggered:",e)

    except OutputGuardrailTripwireTriggered as e:
        print("Output Guardrail Triggered:",e)

    except Exception as e:
        print("An error occurred:",e)

set_tracing_disabled(True)

if __name__=="__main__":
    asyncio.run(main())
