#!/usr/bin/env python3

from urllib.request import urlopen  # Importa urlopen para realizar solicitudes HTTP
import re  # Importa el módulo re para trabajar con expresiones regulares

# Función para descargar el contenido de una página
def download_page(url):
    # Abre la URL y lee el contenido de la página
    return urlopen(url).read()

# Función para extraer todos los enlaces de una página HTML
def extract_links(page):
    # Define una expresión regular para encontrar enlaces en el contenido HTML
    # El patrón busca etiquetas <a> con atributos href que contienen un enlace
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    
    # Usa findall para encontrar todos los enlaces que coinciden con el patrón en la página
    return link_regex.findall(page)

# Bloque principal del script
if __name__ == '__main__':
    # Define la URL objetivo de la que se va a extraer el contenido y los enlaces
    target_url = 'http://www.adrformacion.com'
    
    # Llama a download_page para descargar el contenido de la página
    content = download_page(target_url)
    
    # Convierte el contenido a cadena de texto y extrae los enlaces con extract_links
    links = extract_links(str(content))
    
    # Imprime cada enlace encontrado en la página
    for link in links:
        print(link)
