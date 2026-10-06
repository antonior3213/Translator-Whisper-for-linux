import whisper
import os
from .config import OUTPUT_FOLDER

def transcribir_audio(audio_path, model_name="small", language="es"):
    """
    Transcribe un archivo de audio usando el modelo Whisper.
    """
    # Cargar el modelo de Whisper
    model = whisper.load_model(model_name)

    # Realizar la transcripción
    result = model.transcribe(audio_path, language=language)

    text = result["text"].strip()

    # Generar nombre de archivo basado en el audio
    filename = os.path.basename(audio_path).replace(".mp3", ".txt").replace(".wav", ".txt")
    full_path = os.path.join(OUTPUT_FOLDER, filename)

    # Guardar el resultado en un archivo .txt
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(text)

    return text, full_path
