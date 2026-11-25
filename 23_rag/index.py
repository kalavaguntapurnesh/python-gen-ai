from pathlib import Path

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_openai import OpenAIEmbeddings

from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path(__file__).parent / "nodejs.pdf"

# Load this file into our python program

loader = PyPDFLoader(file_path=pdf_path)

docs = loader.load()

print(docs[0])


# Split the docs into smaller CHUNKS

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 400
)

chunks = text_splitter.split_documents(documents=docs)

print("TExt Splitting into Chunks Done....")
print(f"Our Chunks are : {chunks}")


# Vector Embeddings

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# in the above line "6333" means we have the docker file right, there we are running the QDRANT container.

print("Indexing of documents done...")