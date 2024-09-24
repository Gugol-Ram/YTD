import yt_dlp

# Lista de enlaces de videos de YouTube
urls = [
    '',
    '',

    # Agrega más URLs según sea necesario
]

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/rami_/Downloads/Music Youtube/%(title)s.%(ext)s',  # Ruta de descarga, modificar a gusto.
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        print(f"Descargando y convirtiendo: {url}")
        ydl.download([url])

print("Musiquita lista✅.")
