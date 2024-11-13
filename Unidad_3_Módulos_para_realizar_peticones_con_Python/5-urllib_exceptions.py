#!/usr/bin/env python3

import urllib.error  # Importa el módulo urllib.error para manejar errores HTTP específicos
from urllib.request import urlopen  # Importa urlopen para realizar solicitudes HTTP

# Intenta abrir una URL específica
try:
    # Realiza una solicitud GET a la URL 'https://www.ietf.org/rfc/rfc0.txt'
    # Esta URL es un ejemplo y puede devolver un error 404 si el archivo no existe
    urlopen('https://www.ietf.org/rfc/rfc0.txt')

# Manejo de errores HTTP
except urllib.error.HTTPError as e:
    # Captura errores HTTP específicos (como 404, 500, etc.)
    print('Exception', e)         # Imprime la excepción completa
    print('status', e.code)        # Imprime el código de estado HTTP (por ejemplo, 404 para "Not Found")
    print('reason', e.reason)      # Imprime la razón del error (una breve descripción)
    print('url', e.url)            # Imprime la URL que causó el error
