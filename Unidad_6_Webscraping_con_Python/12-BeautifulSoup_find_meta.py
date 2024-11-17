#!/usr/bin/env python3
# Esta línea shebang especifica que el script debe ejecutarse con Python 3

# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Para analizar y extraer datos del HTML

# Definimos la función que obtendrá las etiquetas `<meta>` de una página web
def obtener_etiquetas_meta(url):
    # Cabecera para la solicitud HTTP, simulando un navegador (User-Agent)
    cabecera = {'User-Agent': 'Firefox'}
    
    # Realizamos la solicitud GET a la URL proporcionada
    peticion = requests.get(url=url, headers=cabecera)
    
    # Creamos un objeto BeautifulSoup para analizar el contenido HTML
    # Usamos 'lxml' como el parser para analizar el HTML
    soup = BeautifulSoup(peticion.text, 'lxml')
    
    # Recorremos todas las etiquetas `<meta>` encontradas en el HTML
    for v in soup.find_all('meta'):
        # Imprimimos la etiqueta completa para inspección
        print(v)
        
        # Si la etiqueta `<meta>` tiene un atributo `name` con el valor 'msapplication-tooltip'
        if v.get('name') == 'msapplication-tooltip':
            # Obtenemos el contenido del atributo `content` de esa etiqueta
            version = v.get('content')
            # Imprimimos el contenido del atributo `content`
            print(version)

# Punto de entrada principal del script
if __name__ == '__main__':
    # Solicitamos al usuario que introduzca la URL de un sitio web
    url = input("Introduzca url:")
    
    # Llamamos a la función con la URL proporcionada, añadiendo "http://" al inicio
    obtener_etiquetas_meta("http://" + url)
