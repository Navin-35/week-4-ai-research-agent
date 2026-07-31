from tools import search_web
from tools import search_wikipedia

print("WEB SEARCH\n")

web = search_web("LangGraph")

if len(web) == 0:
    print("No web results found.")
else:
    for i, result in enumerate(web, start=1):
        print("=" * 60)
        print(f"Result {i}")
        print("Title:", result.get("title"))
        print("Body:", result.get("body"))
        print("URL:", result.get("href"))
        print()

print("\nWIKIPEDIA\n")

print(search_wikipedia("Artificial Intelligence"))