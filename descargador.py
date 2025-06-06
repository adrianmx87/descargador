import os
import subprocess

lineas = "=" * 40
version = "3.0"

# Colores ANSI
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
cyan = "\033[1;36m"
reset = "\033[0m"

# Selección de carpeta de descarga
print(f"{yellow}{lineas}")
carpeta = input("📁 Ingresa la carpeta donde se guardarán las descargas (ENTER para usar la actual): ").strip()
if not carpeta:
    carpeta = os.getcwd()

# Crear la carpeta si no existe
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

print(f"📥 Descargando en: {carpeta}")
print(f"{lineas}{reset}")

# Título
print(f"{red}╻ ╻┏━┓╻ ╻╺┳┓┏━┓╻ ╻┏┓╻╻  ┏━┓┏━┓╺┳┓")
print("┗┳┛┃ ┃┃ ┃ ┃┃┃ ┃┃╻┃┃┗┫┃  ┃ ┃┣━┫ ┃┃")
print(" ╹ ┗━┛┗━┛╺┻┛┗━┛┗┻┛╹ ╹┗━╸┗━┛╹ ╹╺┻┛")
print(version)
print(lineas)

# Menú principal
print(f"{green}¿Qué deseas descargar?")
print(" [1] Música")
print(" [2] Video")
print(" [3] Salir")
opcion = input("> ").strip()
print(reset)

def ejecutar(cmd):
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"❌ Error: {e}")

if opcion == "1":
    print(f"{red}¿Qué deseas descargar?\n [1] Canción\n [2] Playlist\n [3] Salir")
    tipo = input("> ").strip()

    if tipo == "1":
        url = input("🎵 Pega la URL de la canción _> ").strip()
        if not url:
            print("❌ URL vacía")
            exit(1)
        print("🔽 Iniciando descarga...")
        comando = f'yt-dlp -P "{carpeta}" -f bestaudio --embed-thumbnail --extract-audio --audio-format mp3 --audio-quality 0 "{url}"'
        ejecutar(comando)
        print(f"✅ Archivo descargado en: {carpeta}")

    elif tipo == "2":
        url = input("🎵 Pega la URL de la playlist _> ").strip()
        if not url:
            print("❌ URL vacía")
            exit(1)
        print("🔄 Descargando playlist...")
        comando = f'yt-dlp -P "{carpeta}" --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output "%(title)s.%(ext)s" --yes-playlist "{url}"'
        ejecutar(comando)
        print(f"✅ Playlist descargada en: {carpeta}")

    else:
        print(f"{lineas}\n👋 Adiós\n{lineas}")

elif opcion == "2":
    print(f"{cyan}¿Qué deseas descargar?\n [1] Vídeo\n [2] Playlist\n [3] Salir")
    tipo = input("> ").strip()

    if tipo == "1":
        url = input("📹 Pega la URL del vídeo _> ").strip()
        if not url:
            print("❌ URL vacía")
            exit(1)
        print("🔽 Iniciando descarga...")
        comando = f'yt-dlp -P "{carpeta}" -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio" --merge-output-format mp4 "{url}"'
        ejecutar(comando)
        print(f"✅ Vídeo descargado en: {carpeta}")

    elif tipo == "2":
        url = input("📹 Pega la URL de la playlist _> ").strip()
        if not url:
            print("❌ URL vacía")
            exit(1)
        print("🔄 Descargando playlist...")
        comando = f'yt-dlp -P "{carpeta}" -f "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "{url}"'
        ejecutar(comando)
        print(f"✅ Playlist descargada en: {carpeta}")

    else:
        print(f"{lineas}\n👋 Adiós\n{lineas}")

else:
    print(f"{lineas}\n👋 Adiós\n{lineas}")
