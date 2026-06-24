from LLM_model import structured_model

from dummy_dataset import FACT_CHECK_DB

from pydantic import BaseModel

from agents import function_tool
from agents import Agent

class checking_items(BaseModel):
    claims: str
    verdict: str
    evidence: str
    source: str

@function_tool()
def fact_checking(claim:str):
    """
    Verify a user claim using a dummy fact-check database (RAG simulation).

    How it works:
    - Matches keywords from the user claim with stored claims
    - Searches for related evidence
    - Returns supporting or refuting information

    Args:
        claim (str): User-provided statement to verify

    Returns:
        dict: Matched fact-check results with verdict and evidence
    """
    claim= claim.lower().strip()  #lowercase the input string
    matched_results=[]            # create a dict of list for matching claims

    for news in FACT_CHECK_DB:
        claim_found=news['claim'].lower()   #Extract the {claim} and make it lowercase from database

        words_in_claim_found=claim_found.split()  #split the database claim in list of words
        match_found= False  # assume no match initially

        for word in words_in_claim_found:
            if word in claim.split():
                match_found=True
                break

        if match_found:
            matched_results.append(news)

    if not matched_results:
        return {
            "query" : claim,
            "status" : "failure",
            "results" : [],
            "message" : "No matches found"
        }

    if matched_results:
        return {
            "query" : claim,
            "status" : "success",
            "results" : matched_results
        }


fact_checking_agent= Agent(
    name="Fact Checking Agent",
    instructions="""
    You are a Fact Checker Agent.

    Your job is to verify user claims using a knowledge base.

    Workflow:
    1. Receive a claim from the user.
    2. Use fact_check_claim tool to search for evidence.
    3. Analyze retrieved results.
    4. Decide whether the claim is:
       - TRUE
       - FALSE
       - UNCERTAIN

    Rules:
    - Always use tool results only.
    - Never generate fake verification.
    - Always include evidence and source.
    - Be neutral and factual.
    - If no data is found, return "UNCERTAIN"
    """,
    model= structured_model,
    tools=[fact_checking],
    output_type= checking_items,
    handoff_description= """ Handles verification of claims, misinformation detection,and factual validation of news statements. """
)



