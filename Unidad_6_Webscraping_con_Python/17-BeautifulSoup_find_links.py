#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

from bs4 import BeautifulSoup  # Para analizar y extraer información del contenido HTML
import requests  # Para realizar solicitudes HTTP

# Solicita al usuario que introduzca un sitio web para extraer los enlaces
url = input("Ingrese a un sitio web para extraer los links: ")

# Encabezados personalizados para la solicitud HTTP (simula un navegador para evitar bloqueos)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Realiza una solicitud HTTP GET al sitio ingresado por el usuario
# El prefijo "http://" se añade al inicio del sitio proporcionado
response = requests.get("http://" + url, headers=headers)

# Extrae el contenido de la respuesta en formato texto
data = response.text

# Analiza el contenido HTML utilizando BeautifulSoup con el analizador `lxml`
soup = BeautifulSoup(data, 'lxml')

# Busca todas las etiquetas <a> (enlaces) en el contenido HTML
for link in soup.find_all('a'):
    # Extrae el atributo 'href' de cada etiqueta <a>
    link = link.get('href')
    
    # Verifica si el enlace es absoluto (comienza con "http")
    if link.startswith("http"):
        # Si es absoluto, lo imprime directamente
        print(link)
    else:
        # Si es relativo, concatena el enlace relativo con la URL base y lo imprime
        print(url + link)
