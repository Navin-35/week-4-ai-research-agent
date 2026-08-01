from langgraph.graph import StateGraph, START, END

from state import AgentState

from nodes import (
    research_node,
    summarize_node,
    decision_node
)

builder = StateGraph(AgentState)

builder.add_node("research", research_node)
builder.add_node("summary", summarize_node)
builder.add_node("decision", decision_node)

builder.add_edge(START, "research")
builder.add_edge("research", "decision")


def should_retry(state: AgentState):

    if state["retry"] and state["retry_count"] < 2:
        return "research"

    return "summary"


builder.add_conditional_edges(
    "decision",
    should_retry,
    {
        "research": "research",
        "summary": "summary",
    },
)

builder.add_edge("summary", END)

graph = builder.compile()