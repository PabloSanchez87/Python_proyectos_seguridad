#!/usr/bin/env python3
# Indica que el script debe ser ejecutado usando Python 3.

import re
import requests
# Importamos los módulos necesarios: `re` para trabajar con expresiones regulares (aunque no se usa en este script)
# y `requests` para realizar solicitudes HTTP.

from lxml import etree
# Importamos `etree` del módulo `lxml` para analizar y trabajar con documentos HTML/XML.

# Realizamos una solicitud HTTP GET a la URL de la página de Debian stable.
respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

# Parseamos el contenido HTML de la respuesta para convertirlo en un árbol DOM que pueda ser analizado.
parser = etree.HTML(respuesta.text)

# Convierte el árbol DOM nuevamente en una cadena HTML bien formateada y con saltos de línea.
resultado = etree.tostring(parser, pretty_print=True, method="html")
# Aunque la variable `resultado` se define, actualmente no se utiliza más adelante. 
# Podrías descomentar el `print(resultado)` para ver el HTML procesado.

# Define una función XPath para extraer el texto del elemento `<title>` del documento.
# `smart_strings=False` asegura que el resultado sea una cadena estándar y no un objeto especial de lxml.
obtener_texto_xpath = etree.XPath("//title/text()", smart_strings=False)

# Utilizamos la función XPath definida para obtener el texto del elemento `<title>` del árbol DOM.
texto = obtener_texto_xpath(parser)[0]

# Imprimimos el texto del `<title>` que se ha extraído.
print(texto)
