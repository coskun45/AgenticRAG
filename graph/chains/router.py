from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Literal 
from dotenv import load_dotenv
load_dotenv()


class RouteQuery(BaseModel):
    """
    Route a user query to the most relevant datasource
    """
    datasource: Literal["vectorstore", "websearch"] = Field(..., description="Given a user question choose to route it to web search or vector store")

llm = ChatOpenAI(temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery) # llm artik ya vectorstore ya da websearch'e yonlendirilebilir

system_prompt = """
You are an expert at routing user queries to a vector store or web search.

The vector store contains documents related to Hannoversche Versicherung – Consumer Information, specifically about car insurance.
This database provides details on coverage, payments, cancellations, and policyholder responsibilities.
It includes sections on:
General Information
Insurance Conditions
Notice on Obligation to Provide Information
Data Protection Notices
Product Information Sheet – Motor Vehicle Insurance
General Contract Information – Motor Vehicle Insurance
Additional Notes on Premium Calculation
General Terms and Conditions for Motor Vehicle Insurance (AKB 2015)
Consumer Information for Legal Protection Insurance
Product Information Sheet – Legal Protection Insurance
General Contract Information – Legal Protection Insurance
Special Terms and Conditions for Legal Protection Insurance (NRV 2011 PLUS)
Data Protection Notices (Legal Protection Insurance Only)
Query Routing Rules:
If the user query is about motor vehicle insurance from Hannoversche Versicherung, use the vector store.
For all other queries, perform a web search.
"""
route_prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router


# if __name__ == "__main__":
#     response = question_router.invoke("What is the coverage of Hannoversche Versicherung car insurance?")
#     print(response)
#     response = question_router.invoke("What is the capital of Germany?")
#     print(response)