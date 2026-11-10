
import streamlit as st

from src.generate import responder
from src.index import get_collection_count
from config import TOP_K, MAX_CHUNKS


# Configuración de la página
st.set_page_config(
    page_title="Chatbot RAG - Doñana",
    page_icon="🌿",
    layout="wide"
)

# Título y presentación
st.title("🌿 Chatbot RAG - Parque Nacional de Doñana")

st.write(
    "Pregunta sobre el Parque Nacional de Doñana. "
    "El chatbot responderá utilizando la información "
    "disponible en su corpus documental."
)

# Panel lateral con información del sistema
st.sidebar.header("Configuración del sistema")

st.sidebar.metric("Fragmentos almacenados", get_collection_count())
st.sidebar.metric("TOP_K", TOP_K)
st.sidebar.metric("Máximo de fragmentos", MAX_CHUNKS)

st.sidebar.info(
    "Las respuestas se generan utilizando "
    "los documentos indexados en la base de datos."
)

# Inicializar el historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and "sources" in message:
            with st.expander("Consultar fuentes y fragmentos"):
                st.write("Fuentes utilizadas:")
                st.json(message["sources"])

                st.write("Fragmentos recuperados:")
                for i, chunk in enumerate(message["context"], start=1):
                    st.markdown(f"**Fragmento {i}**")
                    st.text(chunk)

# Entrada de preguntas
question = st.chat_input("Escribe tu pregunta sobre Doñana...")

if question:
    # Mostrar y guardar la pregunta
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generar respuesta
    with st.chat_message("assistant"):
        with st.spinner("Consultando los documentos..."):
            try:
                result = responder(question)
                answer = result["respuesta"]

                st.markdown(answer)

                with st.expander("Consultar fuentes y fragmentos"):
                    st.write("Fuentes utilizadas:")
                    st.json(result["fuentes"])

                    st.write("Fragmentos recuperados:")
                    for i, chunk in enumerate(result["contexto"], start=1):
                        st.markdown(f"**Fragmento {i}**")
                        st.text(chunk)

                # Guardar respuesta y evidencias
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": result["fuentes"],
                    "context": result["contexto"]
                })

            except Exception as error:
                st.error(f"Se ha producido un error: {error}")
