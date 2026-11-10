from google import genai
from src.gemini_auth import get_gemini_api_key


def get_gemini_client():
    #Crea y devuelve el cliente de Gemini.
    api_key = get_gemini_api_key()

    client = genai.Client(
        api_key=api_key
    )

    return client