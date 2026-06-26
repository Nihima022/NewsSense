import streamlit as st
import asyncio
from agents import Runner
from Routing_Agent import Routing_Agent


# Page setup
st.set_page_config(
    page_title="NewsSense",
    page_icon="📰",
    layout="wide"
)


# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#Load Queries
def load_sample_queries():
    """
    Load sample queries from txt file.
    Each line = one query
    """
    with open("sample_query.txt", "r", encoding="utf-8") as file:
        queries = []

        for line in file:
            clean_line = line.strip()

            if clean_line:   # skip empty lines
                queries.append(clean_line)

    return queries


# Session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_started" not in st.session_state:
    st.session_state.chat_started = False


# Sidebar sample queries
with st.sidebar:
    st.title("📌 Sample Queries")

    sample_queries = load_sample_queries()

    for q in sample_queries:
        if st.button(q):
            st.session_state.selected_query = q


# Header
st.markdown("""
<div class="main-header">
    <div class="heading-title">NewsSense</div>
    <div class="subtitle">
        Stay ahead with AI-powered news intelligence. Track trending headlines,
        verify claims instantly, and summarize long articles into concise insights.
    </div>
</div>
""", unsafe_allow_html=True)


# Show trending cards only before first chat
if not st.session_state.chat_started:
    st.markdown(
        '<div class="trending-title">🔥 Trending Headlines</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="news-box">
            <h4>IBM unveils the world’s first sub-1 nanometer chip</h4>
            <p>IBM announced a breakthrough with its sub-1nm “Nanostack” chip architecture, potentially redefining the next decade of computing and AI hardware.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="news-box">
            <h4>🌍 Global Weather: Europe faces historic heatwave</h4>
            <p> A record-breaking heatwave is sweeping across Europe, with France, Spain, Italy, and the UK crossing extreme temperature thresholds.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="news-box">
            <h4>📉 Economy: Global growth outlook weakens amid energy shock</h4>
            <p>The Organisation for Economic Co-operation and Development and World Bank both warn that global economic growth is slowing due to rising oil prices, inflation pressure.</p>
        </div>
        """, unsafe_allow_html=True)


# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# Async agent function
async def run_agent(user_query):
    result = await Runner.run(Routing_Agent, user_query)
    return result.final_output


# Input source
if "selected_query" in st.session_state:
    prompt = st.session_state.selected_query
    del st.session_state.selected_query
else:
    prompt = st.chat_input("Ask anything about news...")


# Handle first query + rerun
if prompt:
    if not st.session_state.chat_started:
        st.session_state.chat_started = True
        st.rerun()

    # Save user input
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user input
    with st.chat_message("user"):
        st.markdown(prompt)

    # Run routing agent
    response = asyncio.run(run_agent(prompt))

    # Format output
    if hasattr(response, "title"):
        formatted_response = f"""
### 📰 {response.title}

**Source:** {response.source}  
**Category:** {response.category}
"""

    elif hasattr(response, "claims"):
        formatted_response = f"""
### ✅ Fact Check Result

**Claim:** {response.claims}  
**Verdict:** {response.verdict}  
**Evidence:** {response.evidence}  
**Source:** {response.source}
"""

    elif hasattr(response, "summary"):
        formatted_response = f"""
### ✍ Summary

{response.summary}
"""

    else:
        formatted_response = "No data found."

    # Save assistant output
    st.session_state.messages.append({
        "role": "assistant",
        "content": formatted_response
    })

    # Display assistant output
    with st.chat_message("assistant"):
        st.markdown(formatted_response)