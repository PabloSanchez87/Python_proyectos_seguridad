#!/usr/bin/env python3

import urllib.request  # Importa el módulo urllib.request para realizar solicitudes HTTP

# Solicita al usuario que introduzca una URL
url = input("Introduce la URL:")

# Realiza una solicitud HTTP GET a la URL proporcionada por el usuario
http_response = urllib.request.urlopen(url)

# Imprime el código de estado de la respuesta HTTP (por ejemplo, 200 para éxito)
print('Código de estado: ' + str(http_response.code))

# Verifica si el código de estado es 200 (lo que indica una respuesta exitosa)
if http_response.code == 200:
    # Si el código es 200, imprime la información de los encabezados de la respuesta HTTP
    print(http_response.info())
