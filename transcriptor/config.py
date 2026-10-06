import os

# Modelos disponibles de Whisper
# tiny, base, small, medium, large
MODELS = {
    "Tiny": "tiny",
    "Base": "base",
    "Small": "small",
    "Medium": "medium",
    "Large": "large"
}

DEFAULT_MODEL = "small"
DEFAULT_LANGUAGE = "es"

# Carpeta de salida para las transcripciones
OUTPUT_FOLDER = os.path.expanduser("~/Downloads/Transcripciones")

# Asegurar que la carpeta de salida exista
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
