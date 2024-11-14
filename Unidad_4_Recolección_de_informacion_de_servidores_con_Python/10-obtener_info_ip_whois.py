#!/usr/bin/python

import sys          # Importa sys para acceder a los argumentos de la línea de comandos
import socket       # Importa socket para realizar la resolución de dominio a IP
from ipwhois import IPWhois  # Importa IPWhois para realizar consultas WHOIS a direcciones IP

# Verifica si el número de argumentos es distinto de 2 (script + dominio)
if len(sys.argv) != 2:
    print("[-] uso: python informacion_ip_whois.py <nombre_dominio>")
    sys.exit()  # Sale del programa si no se pasa el dominio como argumento

# Obtiene el dominio desde el argumento de la línea de comandos
dominio = sys.argv[1]

# Resuelve el dominio a su dirección IP
direccion_ip = socket.gethostbyname(dominio)
print('Dirección IP:', direccion_ip)

# Realiza una consulta WHOIS sobre la dirección IP obtenida
whois = IPWhois(direccion_ip).lookup_whois()

# Recorre cada clave y valor en el diccionario de información WHOIS e imprime
for key, value in whois.items():
    print(key, value)
