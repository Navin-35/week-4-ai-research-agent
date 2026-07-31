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

builder.add_edge(

    START,

    "research"

)

builder.add_edge(

    "research",

    "summary"

)

builder.add_edge(

    "summary",

    "decision"

)

builder.add_edge(

    "decision",

    END

)

graph = builder.compile()