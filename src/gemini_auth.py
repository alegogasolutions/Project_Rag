import os
from dotenv import load_dotenv


def get_gemini_api_key() -> str:
    #Carga y obtiene la API Key de Gemini desde el archivo .env.
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "No se ha encontrado GEMINI_API_KEY en el archivo .env"
        )

    return api_key