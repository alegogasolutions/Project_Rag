from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from config import MAX_CHUNKS


def split_documents(documents: list[Document]) -> list[Document]:
    
    #Divide los documentos en fragmentos y limita su cantidad.

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    # Limitar el número máximo de fragmentos
    chunks = chunks[:MAX_CHUNKS]

    return chunks