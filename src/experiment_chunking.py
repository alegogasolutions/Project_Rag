
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.load import load_pdf, load_csv


PROJECT_DIR = Path(__file__).resolve().parent.parent

pdf_path = PROJECT_DIR / "data" / "informacion_general_donana.pdf"
csv_path = PROJECT_DIR / "data" / "faq_donana.csv"


def experiment_chunking():
    # Cargar el corpus documental
    documents = load_pdf(pdf_path) + load_csv(csv_path)

    configurations = [
        {"name": "Configuración A", "chunk_size": 800, "overlap": 150},
        {"name": "Configuración B", "chunk_size": 500, "overlap": 100}
    ]

    print("\n===== EXPERIMENTO DE CHUNKING =====")
    print("Documentos originales:", len(documents))

    for config in configurations:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config["chunk_size"],
            chunk_overlap=config["overlap"],
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

        chunks = splitter.split_documents(documents)

        average_length = (
            sum(len(chunk.page_content) for chunk in chunks) / len(chunks)
            if chunks else 0
        )

        print(f"\n{config['name']}")
        print("Chunk size:", config["chunk_size"])
        print("Chunk overlap:", config["overlap"])
        print("Número de fragmentos:", len(chunks))
        print("Longitud media:", round(average_length, 2))


if __name__ == "__main__":
    experiment_chunking()
