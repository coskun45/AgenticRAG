import sys
sys.path.append('/home/ecoskun/repos/AgenticRAG')
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Literal 
from dotenv import load_dotenv
from ingestion import retriever

load_dotenv()


llm = ChatOpenAI(temperature=0)

class GradeDocuments(BaseModel):
    """
    Binary score for relevance check on retrieved documents
    """
    
    binary_score: str =Field(description="Documents are relevant to the question, 'yes' or 'no'")
    
structured_llm_grader = llm.with_structured_output(GradeDocuments) # llm artik belgelerin soruyla ilgili olup olmadigini kontrol edebilir

system_prompt = """
You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\n
If the document contains keyword or semantic meaning related to question, grade it as relevant.\n
Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts.
"""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Retrieved Document: {document} \n\n User question: {question}"),
    ]
)

retrievel_grader = grade_prompt | structured_llm_grader 

# if __name__ == '__main__':
#     user_question = "What is the coverage of Hannoversche Versicherung car insurance?"
#     docs = retriever.get_relevant_documents(user_question)
#     retrieved_document=docs[0].page_content
#     print(retrievel_grader.invoke(
#         {"question": user_question, "document": retrieved_document}
#     ))