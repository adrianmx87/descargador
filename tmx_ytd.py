#!/usr/bin/env python3
import os
import sys
import subprocess

# Configuración personalizable
fpath = '/data/data/com.termux/files/home/storage/shared/Youtube/%(title)s.%(ext)s'

def clear():
    os.system('clear')

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def download(url, format_code):
    cmd = [
        "yt-dlp",
        "-f", format_code,
        "-o", fpath,
        url
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print_colored("❗ Error durante la descarga.", "31")

def main():
    if len(sys.argv) < 2:
        print_colored("❗ Error: No se ingresó ninguna URL.", "31")
        print_colored("👉 Uso correcto: python3 script.py <URL>", "33")
        sys.exit(1)

    url = sys.argv[1]

    # Descarga inmediata si es shorts
    if "shorts" in url:
        download(url, "best")
        sys.exit(0)

    clear()
    print_colored(" ▄ █   ▄▀▀▀▀▀▄   █ ▄   == Termux-YTD 2.0 =", "31")
    print_colored("▄▄▀▄   █─▀─▀─█  ▄▀▄▄   With Enhanced Speed", "31")
    print_colored("     ▀▄▒▒▒▒▒▒▒▒▒▄▀    --------------------", "31")
    print_colored("     █────▀────█       Check out my Github", "31")
    print_colored("     █────▀────█       For More info...   ", "31")
    print_colored("╔════════════════════════════════════════╗", "36")
    print_colored("║ ♚ Proyecto : 🆃🅴🆁🅼🆄🆇-🆈🆃🅳 (crrcn)        ║", "32")
    print_colored("║ ♚ Autor : KhanSaad1275                 ║", "32")
    print_colored("║ ♚ GitHub : github.com/adrianmx87       ║", "32")
    print_colored("║ ♚ Web    : FRIENDS SCHOOL              ║", "32")
    print_colored("╠════════════════════════════════════════╝", "36")
    print_colored("╠═▶ [𝗦𝗲𝗹𝗲𝗰𝗰𝗶𝗼𝗻𝗮 𝗨𝗻 𝗙𝗼𝗿𝗺𝗮𝘁𝗼]  ➳", "36")
    print_colored("╠═▶ 1. Música MP3♫", "32")
    print_colored("╠═▶ 2. Video 360p", "32")
    print_colored("╠═▶ 3. Video 480p", "32")
    print_colored("╠═▶ 4. Video 720p", "32")
    print_colored("╠═▶ 5. Video 1080p", "32")
    print_colored("╠═▶ 6. Video 2160p (4K)", "32")
    print_colored("╠═▶ 7. Salir", "32")
    print_colored("╠═▶ A. Acerca de", "32")
    choice = input(" ╚═:➤ ").strip().lower()

    formats = {
        '1': 'bestaudio[ext=m4a]',
        '2': 'best[height<=360]',
        '3': 'best[height<=480]',
        '4': 'best[height<=720]',
        '5': 'best[height<=1080]',
        '6': 'best[height<=2160]',
    }

    if choice == '7':
        print_colored("👋 ¡Adiós!", "33")
        sys.exit(0)
    elif choice == 'a':
        print_colored("📣 Termux-YTD  - Herramienta ligera para descargar videos, música y shorts desde YouTube usando Termux.", "36")
        print("🔗 GitHub: https://github.com/adrianmx87/Termux-YTD2.0")
        print("🌐 Website: FRIENDS SCHOOL")
    elif choice in formats:
        download(url, formats[choice])
    else:
        print_colored("❗ Opción inválida. Ejecutando descarga por defecto (2160p)...", "31")
        download(url, 'best[height<=2160]')

if __name__ == "__main__":
    main()
