from typing import Any, Dict
from graph.state import GraphState
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.schema import Document

web_search_tool = TavilySearchResults(k=1)

def web_search(state: GraphState) -> Dict[str, Any]:
    """
    Performs a web search to retrieve documents relevant to the question.
    
    Args:
        state(dict): The current state of the graph
    """
    print("----WEB SEARCH----")
    question = state["question"]
    documents = state["documents"]
    docs = web_search_tool.invoke({"query": question})
    web_results = "\n".join([d["content"] for d in docs])
    web_results = Document(page_content=web_results)
    
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    
    return {"question": question, "documents": documents}