#!/usr/bin/python3
'''
Script para obtener el contenido y las cabeceras de la respuesta correspondiente a la petición de un dominio. Será obligatorio pedir al usuario el target correspondiente al dominio a analizar.

usage: httplib_dominio.py -t <target>
httplib_dominio.py: error: the following arguments are required: -t/--target
'''

import http.client  # Importa el módulo http.client para manejar conexiones HTTP
import argparse     # Importa el módulo argparse para manejar argumentos de línea de comandos

# Crea un objeto ArgumentParser con una descripción del script
parser = argparse.ArgumentParser(description='obtener respuesta de un dominio')
    
# Agrega un argumento requerido llamado -target para especificar la IP o dominio
parser.add_argument("-target", dest="target", help="IP /dominio", required=True)

# Analiza los argumentos proporcionados en la línea de comandos y los guarda en parsed_args
parsed_args = parser.parse_args()

# Establece una conexión HTTP con el dominio o IP especificado en el argumento -target
connection = http.client.HTTPConnection(parsed_args.target)

# Envía una solicitud HTTP GET a la raíz ("/") del dominio o IP objetivo
connection.request("GET", "/")

# Obtiene la respuesta del servidor y la guarda en la variable 'data'
data = connection.getresponse()

# Imprime el código de estado de la respuesta (por ejemplo, 200 para éxito)
print(data.code)

# Imprime los encabezados de la respuesta recibida del servidor
print(data.headers)

# Lee el contenido de la respuesta línea por línea y lo guarda en 'texto'
texto = data.readlines()

# Imprime el contenido de la respuesta en formato de lista de líneas
print(texto)


## Para ejecutar el script
## python3 3-httplib_dominio.py -t www.google.com (o ip)