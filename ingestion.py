from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma 
from langchain_openai import OpenAIEmbeddings
from pathlib import Path
from chromadb.utils import embedding_functions

load_dotenv()
knowledge_base_paths = Path("KnowledgeBase")
files_path = [f for f in knowledge_base_paths.iterdir() if f.is_file()]

docs = [PyPDFLoader(path).load() for path in files_path]
docs_list = [item for sublist in docs for item in sublist]
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
chunks = splitter.split_documents(docs_list)

sentence_transformer_model="multi-qa-distilbert-cos-v1"#distiluse-base-multilingual-cased-v1"
tokens_per_chunk=512
embedding_function= embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=sentence_transformer_model)
vector_store = Chroma(
    documents=chunks,
    collection_name="asrin_getirdigi_tereddutler1-4",
    embedding_function = embedding_function,
    persist_directory="./.chroma"
)

if __name__ == '__main__':
    print(len(docs_list))