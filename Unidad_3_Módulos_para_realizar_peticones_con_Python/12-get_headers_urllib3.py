#!/usr/bin/env python3

import urllib3  # Importa la biblioteca urllib3 para manejar solicitudes HTTP

# Crea un pool de conexiones con un límite de 10 conexiones simultáneas
pool = urllib3.PoolManager(10)

# Realiza una solicitud HTTP GET a la URL especificada
response = pool.request('GET', 'http://www.python.org')

# Imprime el código de estado de la respuesta (por ejemplo, 200 para éxito)
print(response.status)

# Imprime una línea de separación y los nombres de las claves en los encabezados de respuesta
print("Keys\n-------------")
print(response.headers.keys())

# Imprime una línea de separación y los valores de los encabezados de respuesta
print("Values\n-------------")
print(response.headers.values())

# Itera a través de los encabezados de la respuesta y muestra cada uno en formato "clave: valor"
for header, value in response.headers.items():
    print(header + ":" + value)
