from typing import Any, Dict
from graph.state import GraphState
from graph.chains.retrieval_grader import retrievel_grader

def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question. If any documents are not relevant, we will set a flag to run web search.
    
    Args:
        state(dict): The current state of the graph
    Returns:
        state(dict): Filtered out irrelevan documents and updated web_search state
    """
    print("----CHECK DOCUMENTS RELEVANT TO QUESTION----")
    question = state["question"]
    documents = state["documents"]
    web_search = False
    
    filtered_docs = []
    
    
    for document in documents:
        score = retrievel_grader.invoke(
            {
                "document": document.page_content,
                "question": question
            }
        )
        grade = score.binary_score
        
        if grade.lower() == "yes":
            print("----- GRADE: DOCUMENT RELEVANT TO QUESTION -----")
            filtered_docs.append(document)
        else:
            print("----- GRADE: DOCUMENT RELEVANT TO QUESTION -----")
            web_search = True
            continue
    return {"question": question, "documents": filtered_docs, "web_search": web_search}