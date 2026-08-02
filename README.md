# 🔍 AI Research Agent

An AI-powered Research Assistant built using **LangGraph**, **Google Gemini**, **Flask**, and external research tools. The application performs web-based research, retrieves information from multiple sources, and generates concise summaries through a multi-node LangGraph workflow.

---

## 🚀 Features

- AI-powered research assistant
- LangGraph multi-node workflow
- Google Gemini integration
- Web search support
- Wikipedia search
- Conditional routing
- Retry mechanism
- Flask web interface
- Chat history
- Responsive UI

---

## 🛠 Tech Stack

- Python
- Flask
- LangGraph
- LangChain
- Google Gemini
- DDGS
- Wikipedia API

---

## 📂 Project Structure

```
app.py
graph.py
nodes.py
tools.py
chatbot.py
state.py
templates/
static/
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd week-4-ai-research-agent

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key
```

Run:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

Add project screenshots here.

---

## 📌 Future Improvements

- Tavily integration
- Multiple research tools
- PDF export
- Streaming responses
- Memory across sessions
- Multi-agent workflow

---

## 👨‍💻 Author

Navin Kumar