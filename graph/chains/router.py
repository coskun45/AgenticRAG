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
Your are an expert at routing a user query to a vector store or web search.
The vectorstore contains documents that provide answers to people's questions about the Quran, Islam, being a Muslim, and contemporary issues in accordance with Islamic principles.
Use the vectorstore if the user query is about Islamic principles or the Quran.
"""
route_prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router
