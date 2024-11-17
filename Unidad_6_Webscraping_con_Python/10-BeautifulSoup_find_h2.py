# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP y obtener el contenido de la página
from bs4 import BeautifulSoup  # Para analizar y extraer información del HTML

# Realizamos una solicitud GET a la página principal de Python.org
html = requests.get("https://www.python.org/")

# Creamos un objeto BeautifulSoup para analizar el contenido HTML de la página
# Usamos "html.parser" como analizador para procesar el HTML de manera eficiente
res = BeautifulSoup(html.text, "html.parser")

# Buscamos todas las etiquetas <h2> que tienen la clase "widget-title"
# Esto devuelve una lista de etiquetas que coinciden con los criterios
tags = res.findAll("h2", {"class": "widget-title"})

# Iteramos sobre cada etiqueta encontrada
for tag in tags:
    # Obtenemos el texto contenido dentro de la etiqueta <h2> y lo imprimimos
    print(tag.getText())
