import asyncio

from agents import (Runner, set_tracing_disabled, InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered)

from Routing_Agent import Routing_Agent

from Trending_News_Agent import news_item, trending_news_tool, trending_news_agent
from News_Summarizer_Agent import summarize_item, summarize_news, new_summarizer_agent
from Fact_Checking_Agent import checking_items, fact_checking, fact_checking_agent

def load_queries():
    """
    Load queries from sample_query.txt
    Each line in txt file = one query
    """

    queries = []

    with open("sample_query.txt", "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()

            # Skip empty lines
            if cleaned_line:
                queries.append(cleaned_line)

    return queries


async def main():
    queries= load_queries()

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
