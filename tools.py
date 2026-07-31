from ddgs import DDGS
import wikipedia


def search_web(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        return results

    except Exception as e:
        print("Web Search Error:", e)
        return []


def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=3)

    except Exception:
        return "No Wikipedia information found."