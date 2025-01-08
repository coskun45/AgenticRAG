from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(temperature=0)

class GradeDocuments(BaseModel):
    """
    Binary score for hallucination present in generated answer
    """
    
    binary_score: bool =Field(description="Anser is grounded in the facts, 'yer' or 'no'")
    
structured_llm_grader = llm.with_structured_output(GradeDocuments)

system_prompt = """
You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.\n
Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts.
"""

hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
    ]
)

hallucination_grader: RunnableSequence = hallucination_prompt | structured_llm_grader