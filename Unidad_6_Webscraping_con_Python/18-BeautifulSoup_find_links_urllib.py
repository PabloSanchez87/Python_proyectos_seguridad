#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

import urllib.request  # Para realizar solicitudes HTTP y manejar URLs
from bs4 import BeautifulSoup  # Para analizar y extraer información del contenido HTML

# Definimos una función para obtener enlaces de videos desde una URL dada
def get_video_links(archive_url):
    # Crear un objeto de respuesta enviando una solicitud HTTP GET a la URL proporcionada
    response = urllib.request.urlopen(archive_url)
    
    # Leer el contenido de la respuesta y crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(response.read(), 'lxml')
    
    # Lista para almacenar los enlaces extraídos
    links = []
    
    # Iterar sobre todas las etiquetas <a> (enlaces) en el contenido HTML
    for link in soup.find_all('a'):
        # Extraer el atributo 'href' de cada etiqueta <a>
        file_link = link.get('href')
        # Agregar el enlace extraído a la lista
        links.append(file_link)
    
    # Retornar la lista de enlaces
    return links

# Llamamos a la función con la URL de pyvideo.org
links = get_video_links('https://pyvideo.org')

# Imprimimos todos los enlaces obtenidos
print(links)

