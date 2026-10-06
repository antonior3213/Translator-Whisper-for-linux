import yt_dlp
import os

def descargar_audio(url, output_path="audio_temp.mp3"):
    """
    Descarga el audio de un vídeo de YouTube usando yt-dlp con máxima compatibilidad y bypass de bot.
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp_audio',
        'quiet': False,
        'no_warnings': False,
        # Añadimos User-Agent para evitar el error 400 y el bloqueo de bot de YouTube
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.google.com/',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        if os.path.exists("temp_audio.mp3"):
            if os.path.exists(output_path):
                os.remove(output_path)
            os.rename("temp_audio.mp3", output_path)
            return output_path

    except Exception as e:
        print(f"Error detallado de yt-dlp: {str(e)}")
        raise e

    raise FileNotFoundError("No se pudo encontrar el archivo de audio resultante.")
