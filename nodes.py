from state import AgentState
from tools import search_web, search_wikipedia
from chatbot import llm


def research_node(state: AgentState):

    question = state["question"]

    web = search_web(question)

    wiki = search_wikipedia(question)

    web_text = ""

    for result in web:

        web_text += result.get("body", "") + "\n"

    research = f"""
WEB SEARCH

{web_text}

WIKIPEDIA

{wiki}
"""

    return {

        "web_result": web_text,

        "wiki_result": wiki,

        "research": research

    }


def summarize_node(state: AgentState):

    question = state["question"]

    research = state["research"]

    prompt = f"""
You are an AI Research Assistant.

Research Question:

{question}

Research Material:

{research}

Write a professional summary.
"""

    response = llm.invoke(prompt)

    return {

        "answer": response.content

    }


def decision_node(state: AgentState):

    return {}