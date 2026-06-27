<h3>NewsSense — Multi-Agent News Intelligence System</h3>

NewsSense is an AI-powered multi-agent news assistant built to retrieve trending news, verify claims, and summarize content through a modular agent architecture. The system is designed using specialized agents coordinated by a central controller, making the workflow structured.

<h4>Core Architecture</h4>

At the center of the system is the Routing Agent, which acts as the entry point for all user queries. It analyzes user intent and routes the request to the appropriate specialized agent. It supports only single-intent workflows.

Example:

---“What’s trending in AI?” → Trending Agent <br>
---“Did Apple acquire OpenAI?” → Fact Checker Agent<br>
---“Summarize this article…” → Summarizer Agent<br>

<h4>Specialized Agents</h4>

<h5>Trending News Agent</h5>
This agent retrieves category-based trending news using a dummy database that simulates real-world news retrieval.

It uses:<br>
---keyword matching
---topic detection
---category mapping
---title-based matching

Output:<br>
---------title:<br>
---------source:<br>
---------category:<br>

This acts as the retrieval layer for the system.

<h5>Fact Checking Agent</h5>

This agent performs claim verification using a simulated RAG (Retrieval-Augmented Generation) pipeline.

Workflow:<br>
1.accepts a user claim<br>
2.searches the fact-check database<br>
3.matches claim keywords<br>
4.retrieves evidence<br>
5.returns verdict<br>

Possible verdicts:
TRUE
FALSE
UNCERTAIN

Each fact-check record is directly linked to the trending news database, creating data continuity between retrieval and verification.

Output:<br>
----claim<br>
----verdict<br>
----evidence<br>
----source<br>

This makes NewsSense capable of misinformation detection.

<h5>News Summarizer Agent</h5>

This agent summarizes long articles or trending news into short bullet points.

It supports
direct pasted articles,
topic-based summaries,
retrieved news summaries

Workflow:<br>
1.takes raw article text OR topic<br>
2.if topic → fetches related news first<br>
3.extracts important points<br>
4.returns concise summary<br>

Output: summary

This allows fast content digestion.

<h4>Dummy Data Layer</h4>
NewsSense uses two connected datasets:

TRENDING_NEWS_DB :Stores categorized news articles.(
title
source
category)<br>

FACT_CHECK_DB : Stores verification knowledge.(
claims
verdict
evidence
source)<br>

The fact-check database is intentionally built from trending news topics so agents share contextual consistency.

<h4>Guardrail System</h4>

NewsSense includes input and output guardrails for safety and relevance control.

<h5>Input guardrails</h5>detect unrelated queries ,block off-topic content

Example:“Suggest me travel places” → blocked

<h5>Output guardrails</h5>

prevent invalid structured output,
maintain schema consistency

This keeps the system focused only on news-related tasks.

User Interface (Streamlit)

<h4>NewsSense includes a custom Streamlit UI with:</h4>

orange-white gradient theme<br>
responsive layout<br>
left-aligned branding<br>
dynamic trending news cards<br>
collapsible sidebar sample queries<br>
interactive chatbox<br>

Behavior:

On initial load → shows 3 trending news cards
After user query → cards disappear for focus
Results render dynamically based on agent type
Technical Stack

<h4>Built with</h4>

Python
Streamlit
Pydantic
OpenAI Agents SDK
Asyncio

<h4>Concepts used</h4>

Multi-agent systems
Function tools
Handoffs
Structured outputs
RAG simulation
Guardrails
Agent routing

