#!/usr/bin/env python3

# Importamos el módulo requests para realizar peticiones HTTP
import requests

# Definimos un diccionario con los datos que se enviarán en la petición POST
data_dictionary = {"id": "0123456789"}

# Especificamos las cabeceras para la petición: tipo de contenido y lo que aceptamos como respuesta
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Realizamos una petición POST a la URL especificada, enviando los datos y cabeceras definidas
response = requests.post("http://httpbin.org/post", data=data_dictionary, headers=headers)

# Imprimimos el código de estado HTTP de la respuesta
print("HTTP Status Code: " + str(response.status_code))

# Verificamos si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprimimos el cuerpo de la respuesta en formato de texto
    print(response.text)
    
    # Imprimimos nuevamente el código de estado
    print("Status code: " + str(response.status_code))

    # Imprimimos las cabeceras de la respuesta
    print("Cabeceras de respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
  
    # Imprimimos las cabeceras de la petición enviada
    print("Cabeceras de la peticion: ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
