#!/usr/bin/env python3
# Indica que este script debe ejecutarse con Python 3.

import pygeoip  # Importa la biblioteca pygeoip para trabajar con datos de geolocalización.
import argparse  # Importa argparse para manejar argumentos desde la línea de comandos.

# Define una función para obtener la geolocalización (ciudad y región) de un dominio e IP.
def geoip_city(domain, ipaddress):
    path = 'GeoLiteCity.dat'  # Especifica el archivo de base de datos de geolocalización (debe estar en el directorio actual).
    geolitecity = pygeoip.GeoIP(path)  # Carga la base de datos GeoLiteCity.
    
    # Imprime información detallada de la dirección IP proporcionada (como país, ciudad, etc.).
    print(geolitecity.record_by_addr(ipaddress))
    
    # Imprime información de la región asociada al dominio proporcionado.
    print(geolitecity.region_by_name(domain))

# Bloque principal, ejecutado solo si el script se ejecuta directamente.
if __name__ == '__main__':
    # Configura un parser para manejar argumentos de línea de comandos.
    parser = argparse.ArgumentParser(description='Get geolocation from domain and IP address')
    
    # Argumento para el dominio (opcional, con valor predeterminado 'www.python.org').
    parser.add_argument('--domain', action="store", dest="domain", default='www.python.org')
    
    # Argumento para la dirección IP (opcional, con valor predeterminado '83.166.169.231').
    parser.add_argument('--ipaddress', action="store", dest="ipaddress", default='83.166.169.231')
    
    # Analiza los argumentos proporcionados por el usuario.
    given_args = parser.parse_args()
    domain = given_args.domain  # Asigna el dominio proporcionado al argumento 'domain'.
    ipaddress = given_args.ipaddress  # Asigna la IP proporcionada al argumento 'ipaddress'.
    
    # Llama a la función para procesar el dominio y la IP.
    geoip_city(domain, ipaddress)
