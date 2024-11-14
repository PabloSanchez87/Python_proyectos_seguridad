#!/usr/bin/python

import whois  # Importa la biblioteca whois para realizar consultas WHOIS sobre dominios
import sys    # Importa sys para acceder a los argumentos de la línea de comandos

# Verifica si el número de argumentos es distinto de 2 (script + dominio)
if len(sys.argv) != 2:
    print("[-] uso: python informacion_dominio.py <nombre_dominio>")
    sys.exit()  # Sale del programa si no se pasa el dominio como argumento

# Realiza una consulta WHOIS para el dominio proporcionado como argumento
whois_data = whois.whois(sys.argv[1])

# Imprime la información WHOIS completa del dominio
print(whois_data)

# Recorre cada clave y valor en el diccionario de información WHOIS e imprime
for key, value in whois_data.items():
    print("%s : %s \n" % (key, value))
