
import json
from pathlib import Path

from src.generate import responder
from src.logging_utils import logger


PROJECT_DIR = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = PROJECT_DIR / "queries" / "preguntas_evaluacion.json"


def load_evaluation_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def evaluate_system():
    questions = load_evaluation_questions()

    print("\n===== EVALUACIÓN DEL SISTEMA RAG =====")
    print("Número de preguntas:", len(questions))

    correct = 0
    abstentions = 0

    for i, item in enumerate(questions, start=1):
        question = item["pregunta"]
        expected = item["esperado"]

        print(f"\n--- Pregunta {i} ---")
        print("Pregunta:", question)

        try:
            result = responder(question)
            answer = result["respuesta"]

            print("Respuesta esperada:", expected)
            print("Respuesta obtenida:", answer)

            if "no dispongo de información suficiente" in answer.lower():
                abstentions += 1

            if answer.strip().lower() == expected.strip().lower():
                correct += 1

        except Exception:
            logger.exception("Error en la evaluación de la pregunta: %s", question)
            print("Se ha producido un error al procesar esta pregunta.")

    print("\n===== RESUMEN DE EVALUACIÓN =====")
    print("Total de preguntas:", len(questions))
    print("Coincidencias exactas:", correct)
    print("Abstenciones:", abstentions)


if __name__ == "__main__":
    evaluate_system()
