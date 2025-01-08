from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma 
from langchain_openai import OpenAIEmbeddings
from pathlib import Path
from chromadb.utils import embedding_functions
import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import SentenceTransformerEmbeddings

sentence_transformer_model="multi-qa-distilbert-cos-v1"#distiluse-base-multilingual-cased-v1"
embedding_function = SentenceTransformerEmbeddings(model_name=sentence_transformer_model, model_kwargs={"trust_remote_code":True}) 

vectorstore = Chroma( 
embedding_function=embedding_function,collection_name="asrin-getirdigi-tereddutler", persist_directory=".chromadb",
collection_metadata={"embeeding_model":"multi-qa-distilbert-cos-v1",
"chunk_size":512,
"chunk_overlap":50})

retriever = vectorstore.as_retriever()