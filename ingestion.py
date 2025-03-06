from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma 
from langchain_openai import AzureOpenAIEmbeddings
from pathlib import Path
from chromadb.utils import embedding_functions
import bs4
from langchain import hub
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.schema import Document
import os
import json
load_dotenv()

def split_pdf(path=Path("KnowledgeBase")):
    knowledge_base_paths = path
    files_path = [f for f in knowledge_base_paths.iterdir() if f.is_file()]
    print(files_path)

    docs = [PyPDFLoader(path).load() for path in files_path]
    docs_list = [item for sublist in docs for item in sublist]
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs_list)
    return chunks
chunks=split_pdf()


def split_json(file_path = './KnowledgeBase/json/HannoverscheVerscicherung.json', chunks=chunks):
    # JSON dosyasını okuma
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    def create_Doc(page_content, source =file_path, page=0 ):
        doc = Document(
        metadata={'source': source, 'page': page},
        page_content=page_content
    )
        return doc


    for d in data:
        content = ''
        content += d['frage']
        content += d['ref_antwort']
        Doc = create_Doc(content)
        chunks.append(Doc)
    return chunks
chunks=split_json()

def get_embeddings_model():
    deployment = os.getenv("EMBEDDING_DEPLOYMENT")  
    embedding_function = AzureOpenAIEmbeddings(
        model="text-embedding-ada-002",
        deployment=deployment)
    return embedding_function
embedding_function = get_embeddings_model()
    


import time

def create_vector_store(chunks=chunks, embedding_function=embedding_function):
    requests_per_minute = 600
    sleep_time = 60 / requests_per_minute  # İstekler arasına bekleme süresi ekle

    for chunk in chunks:
        vectorstore = Chroma.from_documents(
            documents=[chunk],  # Tek tek ekleyerek limiti aşmayı önle
            embedding=embedding_function,
            collection_name="hannoversche-versicherung",
            persist_directory="./.chromadb",
            collection_metadata={"embeding_model": "azure-openai-ada-002",
                                "chunk_size": 1000,
                                "chunk_overlap": 200}
        )
        time.sleep(sleep_time)  # Rate limit aşımını önlemek için bekleme süresi ekle

vectorstore = Chroma( 
    collection_name="hannoversche-versicherung", 
    persist_directory="./.chromadb",
    embedding_function=embedding_function,
    collection_metadata={"embeding_model":"azure-openai-ada-002",
"chunk_size":1000,
"chunk_overlap":200})

retriever = vectorstore.as_retriever()