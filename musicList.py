# Para descargar varios audios en secuencia. Copiar enlaces. Luego ejecutar en la consola:

# python musicList.py

#Esperar que termine 🙃

import yt_dlp

# Lista de enlaces de videos de YouTube
urls = [
    ''


    
    # Agrega más URLs según sea necesario
]

# Configuración de yt-dlp para descargar solo el audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/rami_/Downloads/Music Youtube/%(title)s.%(ext)s',  # Ajusta la ruta si es necesario
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Descargar y convertir los audios
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        print(f"Descargando y convirtiendo: {url}")
        ydl.download([url])

print("Descarga y conversión completadas para todas las URLs.")
