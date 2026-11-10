import argparse
from pathlib import Path

from src.load import load_pdf, load_csv
from src.chunk import split_documents
from src.index import index_documents, get_collection_count
from src.generate import responder
from config import TOP_K, MAX_CHUNKS

print("Máximo de fragmentos configurado:", MAX_CHUNKS)
print("TOP_K configurado:", TOP_K)


def index_corpus():

    #Carga, divide e indexa los documentos del corpus.

    pdf_path = Path("data/informacion_general_donana.pdf")
    csv_path = Path("data/faq_donana.csv")

    pdf_documents = load_pdf(pdf_path)
    csv_documents = load_csv(csv_path)

    documents = pdf_documents + csv_documents

    print("Documentos PDF:", len(pdf_documents))
    print("Documentos CSV:", len(csv_documents))
    print("Total de documentos:", len(documents))

    chunks = split_documents(documents)

    print("Fragmentos generados:", len(chunks))

    total_indexed = index_documents(chunks)

    print("Fragmentos indexados:", total_indexed)
    print("Fragmentos almacenados:", get_collection_count())


def ask_question(question):
    #Consulta el sistema RAG sin volver a indexar el corpus.

    result = responder(question)

    print("\nPREGUNTA:")
    print(result["pregunta"])

    print("\nRESPUESTA:")
    print(result["respuesta"])

    print("\nFUENTES:")
    for source in result["fuentes"]:
        print(source)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Sistema RAG sobre el Parque Nacional de Doñana"
    )

    parser.add_argument(
        "--index",
        action="store_true",
        help="Indexar el corpus documental"
    )

    parser.add_argument(
        "--ask",
        type=str,
        help="Realizar una pregunta al sistema RAG"
    )

    args = parser.parse_args()

    if args.index:
        index_corpus()

    elif args.ask:
        ask_question(args.ask)

    else:
        parser.print_help()