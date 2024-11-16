#!/usr/bin/env python3
# Indica que este script debe ejecutarse utilizando Python 3.

import re
import requests
# Importamos las bibliotecas necesarias:
# - `re` para trabajar con expresiones regulares.
# - `requests` para realizar solicitudes HTTP.

from lxml.etree import HTML
# Importamos `HTML` de `lxml.etree` para analizar el contenido HTML como un árbol DOM.

# Realizamos una solicitud HTTP GET a la página de Debian.
response = requests.get('https://www.debian.org/releases/stable/index.en.html')

# Convertimos el contenido HTML de la respuesta en un árbol DOM.
root = HTML(response.content)

# Accedemos al título de la página:
# 1. Navegamos al elemento `<head>`.
# 2. Buscamos el elemento `<title>` dentro de `<head>`.
# 3. Obtenemos el texto contenido en el elemento `<title>`.
title_text = root.find('head').find('title').text
print(title_text)  # Imprime el texto del título para verificar el contenido.

# Extraemos el "codename" de la versión de Debian:
# - Utilizamos una expresión regular para buscar el texto entre comillas tipográficas (“ y ”).
release = re.search('\u201c(.*)\u201d', title_text).group(1)

# Utilizamos un XPath para localizar el primer párrafo dentro del div con `id="content"`.
# - `//div[@id="content"]/p[1]`: Encuentra el primer `<p>` dentro del div con id="content".
p_text = root.xpath('//div[@id="content"]/p[1]')[0].text

# Dividimos el texto del párrafo en palabras y obtenemos la segunda palabra como la versión.
version = p_text.split()[1]

# Imprimimos el "codename" y la versión obtenida.
print('Codename: {}\nVersion: {}'.format(release, version))
