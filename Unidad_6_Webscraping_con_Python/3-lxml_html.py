#!/usr/bin/env python3
# Indica que el script debe ejecutarse utilizando Python 3.

import re
import requests
# Importamos los módulos necesarios:
# `re` (aunque no se utiliza en este script, está importado por si necesitas trabajar con expresiones regulares más adelante)
# y `requests` para realizar solicitudes HTTP y obtener contenido de páginas web.

from lxml import html
# Importamos el módulo `html` de `lxml`, que facilita el trabajo con estructuras HTML.

# Realizamos una solicitud HTTP GET para obtener el contenido de la página web de Debian estable.
respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

# Analizamos el contenido de la respuesta HTTP y convertimos el texto HTML en un árbol DOM.
elementos = html.fromstring(respuesta.text)

# Utilizamos XPath para buscar el texto del elemento `<title>` en el árbol DOM.
# El método `xpath` devuelve una lista con los resultados encontrados.
# El argumento `smart_strings=False` asegura que los valores devueltos sean cadenas de texto estándar.
obtener_texto_xpath = elementos.xpath("//title/text()", smart_strings=False)

# Accedemos al primer elemento de la lista (el texto del `<title>`) y lo almacenamos en la variable `texto`.
texto = obtener_texto_xpath[0]

# Imprimimos el texto del `<title>` extraído.
print(texto)
