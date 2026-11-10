from src.gemini_client import get_gemini_client
from src.retrieve import retrieve_documents
from config import TOP_K
from src.logging_utils import logger

# Modelo que utilizaremos para generar respuestas
MODEL_NAME = "gemini-3.5-flash-lite"

client = get_gemini_client()


def generate_text(prompt: str) -> str:
    """
    Envía un prompt a Gemini y devuelve la respuesta generada.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    if not response.text:
        raise ValueError("Gemini no ha generado ninguna respuesta.")

    return response.text.strip()

def answer_question(question: str, k: int = 2) -> dict:
    
    #Recupera información de ChromaDB y genera una respuesta
    #utilizando únicamente los fragmentos recuperados.

    results = retrieve_documents(question, k=k)

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    # Construir el contexto con los fragmentos recuperados
    context_parts = []

    for i, document in enumerate(documents):
        metadata = metadatas[i]

        context_parts.append(
            f"Fuente: {metadata['source']}\n"
            f"Página o identificador: "
            f"{metadata.get('page', metadata.get('id', 'No disponible'))}\n"
            f"Contenido: {document}"
        )

    context = "\n\n".join(context_parts)

    # Crear las instrucciones para Gemini
    prompt = f"""
Eres un asistente especializado en el Parque Nacional de Doñana.

Responde a la pregunta utilizando exclusivamente la información
proporcionada en el contexto.

INSTRUCCIONES:
- No inventes información.
- No utilices conocimientos externos.
- Si el contexto no contiene información suficiente,
  responde: "No dispongo de información suficiente en el corpus
  para responder a esta pregunta."
- Distingue entre Parque Nacional y Parque Natural cuando sea necesario.
- Responde de forma clara y directa.

CONTEXTO:
{context}

PREGUNTA:
{question}

RESPUESTA:
"""

    answer = generate_text(prompt)

    return {
        "answer": answer,
        "sources": metadatas,
        "context": documents
    }

def responder(pregunta: str) -> dict:
    
    #Función principal del sistema RAG.
    #Registra las preguntas, respuestas y fuentes utilizadas.

    logger.info("Nueva pregunta recibida: %s", pregunta)

    try:
        result = answer_question(pregunta, k=TOP_K)

        respuesta = result["answer"]
        fuentes = result["sources"]

        logger.info("Fragmentos recuperados: %s", len(fuentes))

        for fuente in fuentes:
            logger.info("Fuente utilizada: %s", fuente)

        logger.info("Respuesta generada correctamente")

        return {
            "pregunta": pregunta,
            "respuesta": respuesta,
            "fuentes": fuentes,
            "contexto": result["context"]
        }

    except Exception:
        logger.exception("Error al procesar la pregunta")
        raise