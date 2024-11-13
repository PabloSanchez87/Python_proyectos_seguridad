#!/usr/bin/python3

import urllib.request           # Importa el módulo urllib.request para realizar solicitudes HTTP
from urllib.error import HTTPError, URLError  # Importa HTTPError y URLError para manejar errores específicos de HTTP y URL

# Petición GET
try:
    # Intenta abrir una conexión a la URL especificada (en este caso, http://www.python.org)
    response = urllib.request.urlopen("http://www.python.org")
    
    # Lee el contenido de la respuesta, lo decodifica en formato UTF-8, y lo imprime en la consola
    print(response.read().decode('utf-8'))
    
    # Cierra la conexión después de leer los datos
    response.close()

# Manejo de errores
except HTTPError as error:
    # Este bloque captura errores HTTP específicos, como códigos de error 404 o 500
    print("Ocurrió un error HTTP:", error)

except URLError as error:
    # Este bloque captura errores de URL, por ejemplo, si el dominio no es accesible
    print("Ocurrió un error de URL:", error)

except Exception as error:
    # Este bloque captura cualquier otro tipo de excepción que no sea HTTPError o URLError
    print("Ocurrió un error general:", error)

