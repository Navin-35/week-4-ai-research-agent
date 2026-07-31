from state import AgentState
from chatbot import llm


def research_node(state: AgentState):

    question = state["question"]

    response = llm.invoke(question)

    return {
        "answer": response.content
    }