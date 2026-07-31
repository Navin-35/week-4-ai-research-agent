from state import AgentState
from tools import search_web
from tools import search_wikipedia
from chatbot import llm


def research_node(state: AgentState):

    question = state["question"]

    web = search_web(question)

    wiki = search_wikipedia(question)

    web_text = ""

    for result in web:

        web_text += result["body"] + "\n"

    prompt = f"""
You are an AI Research Assistant.

Research Question:

{question}

Web Search Results:

{web_text}

Wikipedia:

{wiki}

Write a concise research summary.
"""

    response = llm.invoke(prompt)

    return {

        "web_result": web_text,

        "wiki_result": wiki,

        "answer": response.content

    }