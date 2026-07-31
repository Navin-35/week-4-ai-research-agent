from graph import graph

question = input("Ask your research question: ")

result = graph.invoke(
    {
        "question": question
    }
)

print("\nAnswer:\n")

print(result["answer"])