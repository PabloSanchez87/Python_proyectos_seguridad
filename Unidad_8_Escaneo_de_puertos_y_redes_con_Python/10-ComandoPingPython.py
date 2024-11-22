#!/usr/bin/env python3
from subprocess import Popen, PIPE  # Para ejecutar procesos del sistema y manejar su entrada/salida
import sys  # Para detectar el sistema operativo
import argparse  # Para manejar argumentos de línea de comandos

# Configuración del analizador de argumentos
parser = argparse.ArgumentParser(description='Ping Scan Network')  # Descripción del script

# Argumento principal: Dirección IP o nombre de host a escanear
parser.add_argument("--host", dest="host", help="Host o dirección IP", required=True)

# Parseo de los argumentos proporcionados por el usuario
parsed_args = parser.parse_args()
direccion_ip = parsed_args.host  # Almacena el host o dirección IP objetivo

print("Scanning %s " % (direccion_ip))  # Mensaje informando el inicio del escaneo

# Verifica el sistema operativo y ajusta el comando de ping en consecuencia
if sys.platform.startswith('linux'):
    # Si el sistema es Linux
    subprocess = Popen(
        ['/bin/ping', '-c 1', direccion_ip],  # Comando para realizar un solo ping
        stdin=PIPE, stdout=PIPE, stderr=PIPE  # Manejo de entrada/salida del proceso
    )
elif sys.platform.startswith('win'):
    # Si el sistema es Windows
    subprocess = Popen(
        ['ping', direccion_ip],  # Comando para ping en Windows
        stdin=PIPE, stdout=PIPE, stderr=PIPE  # Manejo de entrada/salida del proceso
    )

# Comunica con el proceso y captura la salida estándar y de error
stdout, stderr = subprocess.communicate(input=None)

# Imprime la salida del comando ping
print(stdout)

# Analiza la salida para determinar si el host está activo o no
if b"Destination Host Unreachable" in stdout or b"100% packet loss" in stdout or b"100% perdidos" in stdout or stdout == b"":
    # Condiciones que indican que el host no está activo
    print("La dirección IP %s no está activa!" % (direccion_ip))
else:
    # Si no se cumplen las condiciones anteriores, se asume que el host está activo
    print("La dirección IP %s está activa!" % (direccion_ip))
