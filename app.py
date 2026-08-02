from flask import Flask, render_template, request, jsonify
from graph import graph

app = Flask(__name__)

chat_history = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        question = data["message"]

        result = graph.invoke({
            "question": question,
            "retry_count": 0
        })

        return jsonify({
            "answer": result["answer"]
        })

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "answer": str(e)
        }), 500


@app.route("/clear", methods=["POST"])
def clear():

    global chat_history

    chat_history.clear()

    return jsonify(
        {
            "status": "success"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)