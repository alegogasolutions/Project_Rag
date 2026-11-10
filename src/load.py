from pathlib import Path
from pypdf import PdfReader
from langchain_core.documents import Document

import pandas as pd
import re

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


#Limpiamos el pdf de espacios, saltos de linea etc
def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()

#Leer PDF
def load_pdf(file_path: Path) -> list[Document]:
    reader = PdfReader(str(file_path))
    documents = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        cleaned_text = clean_text(text)
        documents.append(
            Document(
                page_content=cleaned_text,
                metadata={"page": page_number, "source": str(file_path)},
            )
        )
    return documents

#Leer CSV
# Leer archivo CSV con preguntas frecuentes
def load_csv(file_path: Path) -> list[Document]:
    dataframe = pd.read_csv(file_path)

    documents = []

    for _, row in dataframe.iterrows():
        content = (
            f"Pregunta: {row['pregunta']}\n"
            f"Respuesta: {row['respuesta']}"
        )

        documents.append(
            Document(
                page_content=content,
                metadata={
                    "source": str(file_path),
                    "id": int(row["id"]),
                    "question": row["pregunta"],
                },
            )
        )

    return documents