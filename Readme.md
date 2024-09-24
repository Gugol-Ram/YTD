# 1.PYTHON

Descargar Python `https://www.python.org/downloads/` marcar la casilla "Add Python to PATH" y luego la casilla "Disable path length limit"(probablemente hay que reiniciar el equipo)<br>

## 2.FFMPEG (por el momento omitirlo)

Descargar el ejecutable(EXE) FFMPEG de la pagina `https://ffmpeg.org/download.html` por ejemplo "Windows Build from gyan.dev" y descomprimirlo.<br>
Buscar la ubicacion del archivo "ffmpeg.exe" normalmente `C:\Users\"nombre usuario"\Downloads\ffmpeg\bin\`. y agregarlo al PATH.

Agregar al PATH:

    Haz clic derecho en Este PC o Mi PC O Equipo y selecciona Propiedades.

    Haz clic en Configuración avanzada del sistema.

    En la ventana de Propiedades del sistema, haz clic en Variables de entorno.

    En Variables del sistema, busca la variable Path y selecciona Editar.

    Agrega una nueva entrada con la ruta a la carpeta bin donde se encuentra ffmpeg.exe. Solo necesitas la ruta a la carpeta, no el nombre del archivo.

### 3.DEPENEDENCIA

Instalar yt-dlp

`python -m pip install yt-dlp`

#### 4.EJECUCIÓN

Copiar enlaces y colocar en `URLS` los que querramos.

```
'https://www.youtube.com/watch?v=qJUz1yit8Us&ab_channel=PLACEBO',
'https://www.youtube.com/watch?v=n7mQWy7pDE0&ab_channel=JoanJettVEVO',
```

Ejecutar en la consola/terminal:

`python musicList.py`

# Esperar que termine 🙃

## En caso de error entonces si realizar el paso 2(FFMPEG)
