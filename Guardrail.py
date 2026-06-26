from agents import Agent
from agents import RunContextWrapper
from agents import TResponseInputItem
from agents import Runner
from agents import input_guardrail
from agents import output_guardrail
from agents import GuardrailFunctionOutput

from pydantic import BaseModel

from LLM_model import structured_model

#1.Input Guardrail
class GuardrailInput(BaseModel):
    is_news_related: bool
    reasoning: str

input_guardrail_agent=Agent(
    name= " Input Guardrail",
    instructions="""
    Determine whether the user's request is related to news.

    ALLOW:
    - trending news
    - fact checking of news
    - summarizing news
    - article
    - today's news
    - devasting news

    BLOCK:
    - coding questions
    - politics
    - harmful instructions
    - hacking
    - unrelated conversations

    Return whether the query is news-related.
    """,
    model=structured_model,
    output_type=GuardrailInput
)

@input_guardrail
async def input_guardrail(
        ctx: RunContextWrapper[None],
        agent: Agent,
        input: str | list[TResponseInputItem]):

    result = await Runner.run(
        starting_agent=input_guardrail_agent,
        input=input,
        context=ctx.context
    )

    response= result.final_output

    print("="*100)
    print(response)
    print("="*100)
    print("Guardrail Response:",response.is_news_related)
    print("Guardrail Reasoning:", response.reasoning)

    return GuardrailFunctionOutput(
        output_info=f" This {response} is blocked by Input Guardrail.",
        tripwire_triggered= not response.is_news_related
    )

#2.Output Guardrail
class GuardrailOutput(BaseModel):
    is_safe: bool
    reasoning: str

output_guardrail_agent=Agent(
    name="Output Guardrail",
    instructions="""
    Check whether the final response is safe.

    BLOCK if response contains:
    - harmful advice
    - hacking instructions
    - dangerous content
    - offensive content
    - fake financial promises

    ALLOW normal travel planning responses.
    """,
    model=structured_model,
    output_type=GuardrailOutput
)

@output_guardrail
async def output_guardrail(
        ctx: RunContextWrapper[None],
        agent: Agent,
        input: str | list[TResponseInputItem]):

    result = await Runner.run(
        starting_agent=output_guardrail_agent,
        input=input,
        context=ctx.context
    )
    response= result.final_output

    print("Guardrail Output:",response.is_safe)
    print("Guardrail Reasoning:",response.reasoning)

    print("=" * 100)

    return GuardrailFunctionOutput(
        output_info=f" This {response} is blocked by Output Guardrail.",
        tripwire_triggered= not response.is_safe
    )

