#!/usr/bin/env python3

from urllib.request import urlopen, urljoin  # Importa urlopen para realizar solicitudes HTTP y urljoin para construir URLs completas
import re  # Importa el módulo re para trabajar con expresiones regulares

# Función para descargar el contenido de una página web
def download_page(url):
    # Abre la URL y lee el contenido de la página
    return urlopen(url).read()

# Función para extraer ubicaciones de imágenes en una página HTML
def extract_image_locations(page):
    # Define una expresión regular para encontrar etiquetas <img> con atributos src en el contenido HTML
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    
    # Usa findall para encontrar todos los valores src de las etiquetas <img> en la página
    return img_regex.findall(page)

# Bloque principal del script
if __name__ == '__main__':
    # Define la URL objetivo de la que se va a extraer el contenido y las ubicaciones de las imágenes
    target_url = 'http://www.adrformacion.com'
    
    # Llama a download_page para descargar el contenido de la página
    content = download_page(target_url)
    
    # Convierte el contenido a cadena de texto y extrae las ubicaciones de las imágenes con extract_image_locations
    image_locations = extract_image_locations(str(content))
    
    # Imprime cada ubicación de imagen encontrada en la página, completando la URL relativa a la URL base
    for src in image_locations:
        # Usa urljoin para construir una URL completa en caso de que src sea una URL relativa
        print(urljoin(target_url, src))
