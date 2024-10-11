import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import pgvector;
from langchain_community.embeddings import fastembed;

class ChunkVectorStore:

  def __init__(self) -> None:
    # Determine which .env file to load
    env_file = ".env.docker" if os.getenv("ENV") == "docker" else ".env.local"
    load_dotenv(env_file)

  def split_into_chunks(self, file_path: str):
    doc = PyPDFLoader(file_path).load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=20)
    chunks = text_splitter.split_documents(doc)
    chunks = filter_complex_metadata(chunks)

    return chunks

  def store_to_vector_database(self, chunks):
    connection_string = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return pgvector.PGVector.from_documents(
        documents=chunks,
        embedding=fastembed.FastEmbedEmbeddings(),
        connection_string=connection_string
    )

