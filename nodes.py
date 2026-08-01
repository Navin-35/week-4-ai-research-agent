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

    retry_count = state.get("retry_count", 0)

    retry = False

    if len(web_text.strip()) < 100:
        retry = True
        retry_count += 1

    return {
        "web_result": web_text,
        "wiki_result": wiki,
        "research": research,
        "retry": retry,
        "retry_count": retry_count,
    }


def summarize_node(state: AgentState):

    prompt = f"""
You are an AI Research Assistant.

Research Question:
{state["question"]}

Research Material:
{state["research"]}

Write a professional research summary in simple language.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }


def decision_node(state: AgentState):
    return {}