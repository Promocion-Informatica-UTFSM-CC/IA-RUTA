import subprocess
import sys

def install_requirements():
    try:
        # Ejecuta el comando para instalar los paquetes desde requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación de los paquetes: {e}")

# Llama a la función antes de ejecutar el resto del código
install_requirements()