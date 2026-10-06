#!/bin/bash
# Instalación automática de Transcriptor Whisper para Linux (Ubuntu/Debian)
set -e

echo "=========================================================="
echo "   Instalador de Transcriptor Whisper para Linux"
echo "=========================================================="

# 1. Arreglar posibles errores de dpkg/apt
echo "==> Limpiando gestor de paquetes y reparando dependencias..."
sudo apt-get install -f -y || true
sudo dpkg --configure -a || true
sudo apt update

# 2. Instalar dependencias del sistema
echo "==> Instalando ffmpeg y python3-tk (necesarios para audio y GUI)..."
sudo apt install -y ffmpeg python3-tk python3-pip python3-venv

# 3. Crear entorno virtual
echo "==> Creando entorno virtual en .venv..."
python3 -m venv .venv
source .venv/bin/activate

# 4. Instalar librerías de Python
echo "==> Instalando dependencias de Python (Whisper, yt-dlp)..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "=========================================================="
echo "¡Instalación completada con éxito!"
echo "Para ejecutar la aplicación, usa:"
echo "  source .venv/bin/activate"
echo "  python main.py"
echo "=========================================================="
