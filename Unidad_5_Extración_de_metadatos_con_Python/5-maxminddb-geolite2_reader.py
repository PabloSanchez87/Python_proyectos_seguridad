#!/usr/bin/env python3

# pip install maxminddb-geolite2
# La librería `maxminddb-geolite2` se utiliza para acceder a la base de datos de geolocalización GeoLite2.
# Documentación: https://github.com/rr2do2/maxminddb-geolite2

import socket  # Módulo para trabajar con direcciones IP y nombres de dominio.
from geolite2 import geolite2  # Librería para consultar la base de datos GeoLite2.
import argparse  # Permite procesar argumentos desde la línea de comandos.
import json  # Módulo para manejar datos en formato JSON.

# Configuración de argumentos de línea de comandos
# Esto permite que el usuario especifique el nombre de dominio desde la línea de comandos.
parser = argparse.ArgumentParser(description='Get IP Geolocation info')  # Descripción del script.
parser.add_argument('--hostname', action="store", dest="hostname", default='python.org')  
# El argumento `--hostname` acepta un dominio. Si no se proporciona, usa 'python.org' por defecto.

# Analiza los argumentos proporcionados por el usuario.
given_args = parser.parse_args()
hostname = given_args.hostname  # Obtiene el nombre de dominio del argumento.

# Resuelve el nombre de dominio a una dirección IP.
ip_address = socket.gethostbyname(hostname)
print("IP address: {0}".format(ip_address))  # Imprime la dirección IP resuelta.

# Inicializa el lector de la base de datos GeoLite2.
reader = geolite2.reader()

# Consulta la información de geolocalización para la dirección IP obtenida.
response = reader.get(ip_address)

# Muestra la respuesta completa en formato JSON con indentación para facilitar la lectura.
print(json.dumps(response, indent=4))

# Extrae y muestra información específica del resultado JSON.
# Se utilizan los campos disponibles en la base de datos GeoLite2.

# Continente
print("Continente:", json.dumps(response['continent']['names']['en'], indent=4))  
# Se accede al nombre del continente en inglés.

# País
print("País:", json.dumps(response['country']['names']['en'], indent=4))  
# Se accede al nombre del país en inglés.

# Latitud
print("Latitud:", json.dumps(response['location']['latitude'], indent=4))  
# Coordenada de latitud.

# Longitud
print("Longitud:", json.dumps(response['location']['longitude'], indent=4))  
# Coordenada de longitud.

# Zona horaria
print("Zona horaria:", json.dumps(response['location']['time_zone'], indent=4))  
# Se obtiene la zona horaria.
