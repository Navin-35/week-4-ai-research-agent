from typing import TypedDict

class AgentState(TypedDict):

    question: str

    web_result: str

    wiki_result: str

    answer: str