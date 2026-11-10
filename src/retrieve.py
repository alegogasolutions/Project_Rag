from src.embed import generate_embeddings
from src.index import collection

def retrieve_documents(question: str, k: int = 4):
    #Recupera los fragmentos más relevantes para una pregunta.
    question_embeddings = generate_embeddings([question])[0]

    results = collection.query(
        query_embeddings=[question_embeddings],
        n_results=k
    )

    return results