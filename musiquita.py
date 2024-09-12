# copiar enlace del video y ejecutar en la consola:

# python musiquita.py

import yt_dlp
from pydub import AudioSegment
import os

# Enlace del video de YouTube
url = ''

# Configuración de yt-dlp para descargar solo el audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/rami_/Downloads/Music Youtube/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("La descarga y conversión se completaron exitosamente.")
