#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

import os  # Para trabajar con el sistema de archivos (crear directorios, manejar rutas)
import requests  # Para realizar solicitudes HTTP y descargar contenido
from bs4 import BeautifulSoup  # Para analizar y extraer información del HTML

# Definimos una clase llamada `Scraping` que contendrá métodos para tareas de scraping
class Scraping:
    # Método para extraer y descargar imágenes de una URL dada
    def scrapingImages(self, url):
        print("Obtener imágenes de la url con bs4: " + url)  # Mensaje informativo
        
        try:
            # Realizamos una solicitud HTTP GET a la URL proporcionada
            response = requests.get(url)
            # Analizamos el contenido de la respuesta con BeautifulSoup y el analizador `lxml`
            bs = BeautifulSoup(response.text, 'lxml')
            
            # Buscamos todas las etiquetas <img> en el HTML
            images = bs.find_all("img")

            # Mostramos cuántas imágenes se encontraron
            print('Imágenes encontradas %s' % len(images))
    
            # Creamos un directorio llamado "imagenes" para guardar las imágenes descargadas
            os.system("mkdir imagenes")
    
            # Iteramos sobre todas las etiquetas <img> encontradas
            for tagImage in images:
                # Verificamos si el atributo `src` de la imagen es un enlace absoluto o relativo
                if tagImage['src'].startswith("http") == False:
                    # Si es relativo, concatenamos la URL base con el atributo `src`
                    download = url + tagImage['src']
                else:
                    # Si es absoluto, usamos directamente el atributo `src`
                    download = tagImage['src']
                
                # Mostramos la URL de la imagen que vamos a descargar
                print(download)
                
                # Descargamos la imagen
                r = requests.get(download)
                # Guardamos la imagen en el directorio "imagenes", usando el nombre del archivo extraído de la URL
                f = open('imagenes/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)  # Escribimos el contenido de la imagen
                f.close()  # Cerramos el archivo después de guardar
    
        except Exception as e:
            # Si ocurre un error, mostramos un mensaje indicando que hubo un problema con la conexión
            print("Error de conexión en: " + url)
            pass
                
# Punto de entrada del script
if __name__ == "__main__":
    # URL objetivo para realizar el scraping
    target = "https://www.python.org"
    # Creamos una instancia de la clase `Scraping`
    scraping = Scraping()
    # Llamamos al método `scrapingImages` con la URL objetivo
    scraping.scrapingImages(target)
