#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

from urllib.request import urlopen  # Para realizar solicitudes HTTP y obtener contenido de la página
from urllib.error import HTTPError  # Para manejar errores HTTP específicos, como 404 o 500
from urllib.error import URLError  # Para manejar errores relacionados con el servidor o el dominio
from bs4 import BeautifulSoup  # Para analizar y extraer información del contenido HTML
import urllib.request  # Para realizar solicitudes HTTP con encabezados personalizados

# Configuramos un agente de usuario (User-Agent) para simular un navegador web y evitar bloqueos por parte del servidor
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}  # Encabezados de la solicitud

# URL de la página que queremos analizar
url = 'http://python.org'

try:
    # Preparamos la solicitud HTTP con los encabezados personalizados
    req = urllib.request.Request(url, headers=headers)
    # Realizamos la solicitud HTTP y obtenemos la respuesta usando `urlopen`
    with urlopen(req) as res:
        html = res.read()  # Leemos el contenido de la página en formato HTML

# Manejo de errores HTTP
except HTTPError as error:
    print("HTTPError ", error)  # Mostramos el error específico (como 404 o 500)

# Manejo de errores de conexión, como servidor caído o dominio incorrecto
except URLError as error:
    print("Server down or incorrect domain ", error)

# Si no hubo errores, procesamos el contenido de la página
else:
    # Analizamos el HTML usando BeautifulSoup con el analizador 'lxml'
    res = BeautifulSoup(html, "lxml")
    # Verificamos si la página tiene una etiqueta `<title>`
    if res.title is None:
        # Si no se encuentra la etiqueta `<title>`, lo indicamos
        print(f"Tag not found")
    else:
        # Si la etiqueta `<title>` existe, imprimimos su contenido (el texto del título)
        print(res.title.text)
