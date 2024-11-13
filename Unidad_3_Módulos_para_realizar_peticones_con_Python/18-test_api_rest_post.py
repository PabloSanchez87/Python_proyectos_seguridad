#!/usr/bin/env python3

# Importamos el módulo requests para manejar peticiones HTTP
import requests

# Definimos un diccionario con los datos que enviaremos en la petición POST
data_dictionary = {"id": "0123456789"}

# Establecemos las cabeceras de la petición para indicar que enviamos y recibimos JSON
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Realizamos una petición POST a la URL especificada, enviando el diccionario y las cabeceras
response = requests.post("http://httpbin.org/post", data=data_dictionary, headers=headers)

# Imprimimos el código de estado HTTP de la respuesta
print("HTTP Status Code: " + str(response.status_code))

# Si el código de estado es 200 (éxito), imprimimos el contenido de la respuesta
if response.status_code == 200:
    print(response.text)
