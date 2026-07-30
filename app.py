from graph import graph

result = graph.invoke(
    {
        "question": "What is LangGraph?"
    }
)

print(result["answer"])