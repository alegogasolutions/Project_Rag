from pathlib import Path
from src.embed import generate_embeddings
import chromadb

PROJECT_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = PROJECT_DIR / "chroma"

client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)

collection = client.get_or_create_collection(
    name="donana"
)

def index_documents(chunks):
    #Guarda los fragmentos, sus embeddings y metadatos en ChromaDB.
    texts = [chunk.page_content for chunk in chunks]
    metadatas = [chunk.metadata for chunk in chunks]

    embeddings = generate_embeddings(texts)

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return len(chunks)

def get_collection_count():
    #Devuelve el número de fragmentos almacenados en ChromaDB.
    return collection.count()