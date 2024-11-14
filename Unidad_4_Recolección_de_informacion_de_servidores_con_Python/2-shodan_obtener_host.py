#!/usr/bin/env python

import requests  # Importa la biblioteca requests para realizar solicitudes HTTP

# Variable para almacenar la clave de la API de Shodan. Se debería completar con el valor correspondiente.
SHODAN_API_KEY = ""

# Dirección IP a consultar en Shodan
ip = '8.8.8.8'

# Función que consulta información sobre una IP utilizando la API de Shodan
def ShodanInfo(ip):
    try:
        # Realiza una solicitud GET a la API de Shodan para obtener información sobre la IP proporcionada
        # La URL de la API incluye el IP y la clave de la API (SHODAN_API_KEY) como parámetros
        result = requests.get(
            'https://api.shodan.io/shodan/host/' + ip + '?key=' + SHODAN_API_KEY + '&minify=True'
        ).json()
    except Exception as exception:
        # Si ocurre algún error en la solicitud, devuelve un diccionario con un mensaje de error
        result = {"error": "Informacion no disponible."}
    return result  # Retorna el resultado de la consulta

# Imprime la información obtenida sobre la IP
print(ShodanInfo(ip))
