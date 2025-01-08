from typing import List, TypedDict

class GraphState(TypedDict):
    """
    Represent the state of a graph.
    
    Attributes:
        question: question to be asked
        generation: LLM generation
        web_search: whether to search or not
        documents: list of documents
    
    
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]