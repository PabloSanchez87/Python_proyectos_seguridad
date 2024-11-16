#!/usr/bin/env python3
# Indica que el script debe ejecutarse utilizando Python 3.

import os
import requests
from lxml import html
# Importamos las bibliotecas necesarias:
# - `os`: para operaciones relacionadas con el sistema operativo (aunque no se utiliza aquí).
# - `requests`: para realizar solicitudes HTTP.
# - `lxml.html`: para analizar HTML y navegar por el DOM.

class Scraping:
    # Definimos una clase llamada `Scraping` para encapsular métodos relacionados con web scraping.
    
    def scrapingLinks(self, url):
        # Método para obtener y listar los enlaces (`<a href>`) de una URL específica.
        print("Obtener links de la url:" + url)
        
        try:
            # Realizamos una solicitud HTTP GET a la URL proporcionada.
            response = requests.get(url)
            
            # Convertimos el contenido HTML de la respuesta en un árbol DOM.
            parsed_body = html.fromstring(response.text)
    
            # Usamos un XPath para obtener todos los atributos `href` de los elementos `<a>`.
            links = parsed_body.xpath('//a/@href')
    
            # Imprimimos el número total de enlaces encontrados.
            print('Links encontrados %s' % len(links))
    
            # Iteramos sobre los enlaces encontrados.
            for link in links:
                # Si el enlace comienza con "http", lo consideramos un enlace absoluto y lo imprimimos directamente.
                if link.startswith("http"):
                    print(link)
                else:
                    # Si el enlace es relativo, lo combinamos con la URL base.
                    print(url + link)
                    
        except Exception as e:
            # Manejamos cualquier error durante la conexión y mostramos un mensaje informativo.
            print("Error de conexión en:  " + url)
            pass

# Punto de entrada del script.
if __name__ == "__main__":
    # URL objetivo para realizar el scraping.
    target = "https://www.python.org"
    
    # Instancia de la clase `Scraping`.
    scraping = Scraping()
    
    # Llamamos al método `scrapingLinks` con la URL objetivo.
    scraping.scrapingLinks(target)
