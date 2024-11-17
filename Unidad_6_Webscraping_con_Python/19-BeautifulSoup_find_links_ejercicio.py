#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

import os  # Importado, aunque no se usa en este script
import requests  # Para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Para analizar y extraer información del contenido HTML

# Definimos una clase llamada `Scraping`
class Scraping:
    
    # Método para obtener y mostrar todos los enlaces de una URL dada
    def scrapingLinks(self, url):
        print("Obtener links de la url: " + url)  # Mensaje informativo
        
        try:
            # Realizamos una solicitud HTTP GET a la URL proporcionada
            response = requests.get(url)
            # Analizamos el contenido HTML de la respuesta usando BeautifulSoup
            bs = BeautifulSoup(response.text, 'lxml')
            
            # Buscamos todas las etiquetas <a> (enlaces) en el HTML
            links = bs.find_all("a")
            
            # Mostramos cuántos enlaces se encontraron
            print('Links encontrados %s' % len(links))
    
            # Iteramos sobre cada enlace encontrado
            for link in links:
                try:
                    # Verificamos si el enlace es absoluto (comienza con "http")
                    if link['href'].startswith("http") == False:
                        # Si es relativo, concatenamos la URL base con el enlace relativo
                        print(url + link['href'])
                    else:
                        # Si es absoluto, lo imprimimos directamente
                        print(link['href'])
                except KeyError:
                    # Algunos enlaces pueden no tener el atributo `href`, lo ignoramos
                    continue
                    
        except Exception as e:
            # Si ocurre algún error, mostramos un mensaje indicando que no se pudo conectar
            print("Error de conexión en:  " + url)
            pass

# Punto de entrada del script
if __name__ == "__main__":
    # URL objetivo para realizar el scraping
    target = "https://www.python.org"
    # Creamos una instancia de la clase `Scraping`
    scraping = Scraping()
    # Llamamos al método `scrapingLinks` con la URL objetivo
    scraping.scrapingLinks(target)
