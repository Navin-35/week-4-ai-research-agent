from graph import graph

while True:

    question = input("\nAsk Research Question: ")

    if question.lower() == "exit":
        break

    result = graph.invoke(
        {
            "question": question,
            "retry_count": 0
        }
    )

    print("\nResearch Summary\n")

    print(result["answer"])