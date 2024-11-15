#!/usr/bin/env python3

# Importamos las librerías necesarias
import socket  # Para trabajar con direcciones IP y resolver nombres de dominio.
from geoip import geolite2  # Proporciona acceso a la base de datos GeoIP para geolocalización.
import argparse  # Permite procesar argumentos desde la línea de comandos.
import json  # Para manejar datos en formato JSON, aunque aquí no se utiliza directamente.

# Configuración de los argumentos de línea de comandos
# Esto permite que el usuario especifique el nombre de dominio al ejecutar el script.
parser = argparse.ArgumentParser(description='Get IP Geolocation info')  # Descripción del script.
parser.add_argument('--hostname', action="store", dest="hostname", required=True)  
# El argumento `--hostname` es obligatorio (`required=True`) y especifica el dominio a consultar.

# Procesa los argumentos proporcionados por el usuario.
given_args = parser.parse_args()
hostname = given_args.hostname  # Obtiene el nombre de dominio del argumento.

# Resuelve el nombre de dominio a su dirección IP correspondiente.
ip_address = socket.gethostbyname(hostname)
print("IP address: {0}".format(ip_address))  # Muestra la dirección IP resuelta.

# Realiza la consulta de geolocalización para la dirección IP utilizando GeoLite2.
match = geolite2.lookup(ip_address)

# Si se encuentra información de geolocalización, se imprime en pantalla.
if match is not None:
    print('País: ', match.country)  # País asociado a la IP.
    print('Continente: ', match.continent)  # Continente asociado a la IP.
    print('Time zone: ', match.timezone)  # Zona horaria asociada a la IP.
    print('Location: ', match.location)  # Coordenadas geográficas (latitud, longitud).

# Si no se encuentra información, no se imprime nada adicional.
