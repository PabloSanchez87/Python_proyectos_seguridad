#!/usr/bin/env python3

# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
import re  # Para trabajar con expresiones regulares
from bs4 import BeautifulSoup  # Para analizar y extraer contenido del HTML
import sys  # Para manejar argumentos de línea de comandos

# Verificamos que el usuario pase exactamente un argumento (el dominio)
if len(sys.argv) != 2:
    # Mostramos un mensaje de uso correcto y salimos si no se cumple
    print("uso: %s dominio" % (sys.argv[0]))
    sys.exit(0)

# Lista para almacenar las URLs encontradas
urls = []

# Asignamos el dominio proporcionado por el usuario
dominio = sys.argv[1]

# Realizamos una solicitud GET al dominio principal para obtener su HTML
respuesta = requests.get(dominio)

# Usamos una expresión regular para buscar todos los comentarios HTML en el código fuente del dominio
comentarios = re.findall('<!--(.*)-->', respuesta.text)

# Mostramos los comentarios HTML encontrados en el dominio principal
print("Comentarios en el dominio: " + dominio)

for comentario in comentarios:
    print(comentario)

# Analizamos el contenido HTML usando BeautifulSoup para encontrar todos los enlaces (<a>)
soup = BeautifulSoup(respuesta.text, "lxml")

# Iteramos sobre todas las etiquetas <a> encontradas para extraer sus enlaces (href)
for link in soup.find_all('a'):
    enlace = link.get('href')  # Obtenemos el atributo 'href'
    try:
        # Verificamos si el enlace es absoluto y pertenece al dominio proporcionado
        if enlace[:4] == "http" and dominio in enlace:
            urls.append(str(enlace))
        # Verificamos si el enlace es relativo (comienza con '/')
        elif enlace[:1] == "/":
            urls.append(str(dominio + enlace))
    except Exception as exception:
        # Si ocurre algún error al procesar un enlace, lo ignoramos y seguimos
        pass
        print("Exception", exception)

# Para cada enlace recopilado, realizamos solicitudes para buscar comentarios HTML en esas páginas
for url in urls:
    print("Comentarios en la página: " + url)
    # Realizamos una solicitud GET al enlace actual
    respuesta = requests.get(url)
    # Buscamos todos los comentarios HTML en el código fuente de la página
    comentarios = re.findall('<!--(.*)-->', respuesta.text)
    # Imprimimos los comentarios encontrados
    for comentario in comentarios:
        print(comentario)
