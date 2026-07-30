from state import AgentState

def research_node(state: AgentState):

    question = state["question"]

    answer = f"I received your question: {question}"

    return {
        "answer": answer
    }