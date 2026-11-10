from src.gemini_client import get_gemini_client


client = get_gemini_client()


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    #Convierte textos en vectores numéricos por lotes usando Gemini.
    embeddings = []
    batch_size = 50

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=batch
        )

        embeddings.extend(
            embedding.values
            for embedding in response.embeddings
        )

    return embeddings