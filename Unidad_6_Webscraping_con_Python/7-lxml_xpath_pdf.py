#!/usr/bin/env python3
# Indica que el script debe ejecutarse utilizando Python 3.

import os
import requests
from lxml import html
# Importamos las bibliotecas necesarias:
# - `os`: para trabajar con el sistema de archivos.
# - `requests`: para realizar solicitudes HTTP.
# - `lxml.html`: para analizar HTML y navegar por el DOM.

class Scraping:
    # Definimos una clase llamada `Scraping` para encapsular métodos relacionados con web scraping.

    def scrapingPDFs(self, url):
        # Método para obtener y descargar los enlaces de archivos PDF de una URL específica.
        print("Obtener pdfs de la url:" + url)
    
        try:
            # Realizamos una solicitud HTTP GET a la URL proporcionada.
            response = requests.get(url)
            
            # Convertimos el contenido HTML de la respuesta en un árbol DOM.
            parsed_body = html.fromstring(response.text)

            # Usamos un XPath para obtener todos los enlaces (`href`) que contienen ".pdf".
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')

            # Imprimimos el número total de PDFs encontrados.
            print('Pdfs encontrados %s' % len(pdfs))
    
            # Creamos un directorio llamado "pdfs" para guardar los documentos descargados.
            os.system("mkdir -p pdfs")
    
            # Iteramos sobre los enlaces de los PDFs encontrados.
            for pdf in pdfs:
                # Si el enlace no es absoluto, lo convertimos en un enlace completo.
                if not pdf.startswith("http"):
                    download = url + "/" + pdf
                else:
                    download = pdf
                
                # Imprimimos el enlace del archivo PDF.
                print(download)
                
                # Descargamos el archivo PDF.
                r = requests.get(download)
                
                # Guardamos el archivo en el directorio "pdfs".
                with open('pdfs/%s' % download.split('/')[-1], 'wb') as f:
                    f.write(r.content)
                
        except Exception as e:
            # Manejamos cualquier error durante la conexión o el procesamiento.
            print("Error de conexión en: " + url)
            print("Detalles del error:", e)
            pass

# Punto de entrada del script.
if __name__ == "__main__":
    # URL objetivo para realizar el scraping.
    target = "https://docs.python-guide.org"
   
    # Instancia de la clase `Scraping`.
    scraping = Scraping()
    
    # Llamamos al método `scrapingPDFs` con la URL objetivo.
    scraping.scrapingPDFs(target)
