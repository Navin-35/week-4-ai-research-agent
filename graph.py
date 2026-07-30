from langgraph.graph import StateGraph, START, END

from state import AgentState
from nodes import research_node

builder = StateGraph(AgentState)

builder.add_node("research", research_node)

builder.add_edge(START, "research")

builder.add_edge("research", END)

graph = builder.compile()