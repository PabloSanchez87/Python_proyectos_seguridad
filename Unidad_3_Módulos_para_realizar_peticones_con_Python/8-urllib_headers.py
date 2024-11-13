#!/usr/bin/env python3

import urllib.request  # Importa el módulo urllib.request para realizar solicitudes HTTP

# Solicita al usuario que introduzca una URL
url = input("Enter the URL:")

# Realiza una solicitud HTTP GET a la URL proporcionada por el usuario y guarda la respuesta en 'http_response'
http_response = urllib.request.urlopen(url)

# Verifica si el código de estado es 200 (lo que indica una respuesta exitosa)
if http_response.code == 200:
    # Si el código es 200, imprime todos los encabezados de la respuesta HTTP en formato de diccionario
    print(http_response.headers)
    
    # Itera a través de los encabezados de la respuesta como pares clave-valor
    for key, value in http_response.getheaders():
        # Imprime cada encabezado en formato "clave: valor"
        print(key, value)
