import logging
from pathlib import Path

# Directorio donde se guardarán los registros
PROJECT_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "rag.log"


def setup_logger():
    """
    Configura el sistema de logging del proyecto.
    """

    logger = logging.getLogger("rag")
    logger.setLevel(logging.INFO)

    # Evitar añadir varios manejadores al mismo logger
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    # Guardar registros en un archivo
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Mostrar registros también en la terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


logger = setup_logger()