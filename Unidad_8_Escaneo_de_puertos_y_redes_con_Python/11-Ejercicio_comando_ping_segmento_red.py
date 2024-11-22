#!/usr/bin/env python3
from subprocess import Popen, PIPE  # Para ejecutar procesos del sistema y manejar entrada/salida
import sys  # Para detectar el sistema operativo
import argparse  # Para manejar argumentos de línea de comandos

# Configuración del analizador de argumentos
parser = argparse.ArgumentParser(description='Ping Scan Network')  # Descripción del script

# Argumento para especificar el segmento de red
parser.add_argument(
    "-network",
    dest="network",
    help="NetWork segment [For example 192.168.1]",
    required=True
)

# Argumento para especificar el número de máquinas (IPs) a escanear
parser.add_argument(
    "-machines",
    dest="machines",
    help="Number of machines in the network segment to scan",
    type=int,
    required=True
)

# Parseo de los argumentos proporcionados por el usuario
parsed_args = parser.parse_args()

# Bucle para escanear las direcciones IP dentro del rango especificado
for ip in range(0, parsed_args.machines):
    # Construye la dirección IP en base al segmento de red y al índice actual
    direccion_ip = parsed_args.network + '.' + str(ip)
    print("Scanning %s " % (direccion_ip))  # Informa al usuario de la IP que se está escaneando

    # Verifica el sistema operativo para ajustar el comando de `ping`
    if sys.platform.startswith('linux'):
        # Si el sistema es Linux
        subprocess = Popen(
            ['/bin/ping', '-c 1', direccion_ip],  # Comando para un solo paquete ICMP
            stdin=PIPE, stdout=PIPE, stderr=PIPE  # Manejo de entrada/salida del proceso
        )
    elif sys.platform.startswith('win'):
        # Si el sistema es Windows
        subprocess = Popen(
            ['ping', direccion_ip],  # Comando para `ping` en Windows
            stdin=PIPE, stdout=PIPE, stderr=PIPE  # Manejo de entrada/salida del proceso
        )

    # Captura la salida estándar y de error del comando `ping`
    stdout, stderr = subprocess.communicate(input=None)

    # Imprime la salida del comando `ping`
    print(stdout)

    # Analiza la salida para determinar si la IP está activa
    if b"Destination Host Unreachable" in stdout or stdout == b"":
        # Condiciones para IP inactiva
        print("La dirección IP %s no está activa!" % (direccion_ip))
    else:
        # Caso de IP activa
        print("La dirección IP %s está activa!" % (direccion_ip))
