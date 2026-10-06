# Transcriptor Whisper

Aplicación de escritorio (Tkinter) que transcribe a texto el audio de un vídeo de
YouTube o de un archivo local, usando el modelo Whisper en tu propio equipo.

## Estructura

```
transcriptor-whisper/
├── main.py                  # Punto de entrada
├── requirements.txt         # openai-whisper, yt-dlp
├── setup_mac.sh             # Instalación automática en macOS
├── setup_linux.sh           # Instalación automática en Linux (Ubuntu/Debian)
├── transcriptor/
│   ├── __init__.py
│   ├── app.py               # Interfaz gráfica
│   ├── config.py            # Modelos, idiomas, carpeta de salida
│   ├── descarga.py          # Descarga del audio con yt-dlp
│   └── transcripcion.py     # Whisper y guardado del .txt
└── .idea/runConfigurations/Transcriptor.xml   # Configuración de ejecución de PyCharm
```

## Instalación (macOS)

1. Descomprime el zip donde quieras.
2. Abre Terminal en esa carpeta y ejecuta: `bash setup_mac.sh`
   (instala ffmpeg, Python y Tkinter con Homebrew y crea el entorno `.venv`).
3. Ejecuta con: `source .venv/bin/activate && python main.py`

## Instalación (Linux - Ubuntu/Debian)

1. Abre Terminal en la carpeta del proyecto.
2. Ejecuta el script de instalación: `bash setup_linux.sh`
   (instala ffmpeg, python3-tk y crea el entorno `.venv`).
3. Ejecuta la aplicación con: `source .venv/bin/activate && python main.py`

## Uso

- Pega la URL del vídeo de YouTube **o** elige un archivo de audio/vídeo.
- Elige el modelo (`small` es buen equilibrio; `medium` más preciso pero más lento).
- Pulsa **Transcribir**. El texto aparece en la ventana y se guarda en
  `~/Downloads/Transcripciones/<título>.txt`.

La primera vez que uses cada modelo se descarga (small ≈ 460 MB, medium ≈ 1,5 GB).

## Problemas frecuentes

| Error | Solución |
|---|---|
| `No module named '_tkinter'` | **macOS:** Repite `setup_mac.sh`. **Linux:** `sudo apt install python3-tk`. |
| `ffmpeg not found` | **macOS:** `brew install ffmpeg`. **Linux:** `sudo apt install ffmpeg`. |
| `Sign in to confirm…` | YouTube ha cambiado algo: `pip install -U yt-dlp`. |

## Aviso

Las condiciones de uso de YouTube no permiten descargar contenido con herramientas
externas. Úsalo con tus propios vídeos o para consulta personal.
