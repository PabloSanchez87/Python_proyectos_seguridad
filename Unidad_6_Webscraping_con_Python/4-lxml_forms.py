#!/usr/bin/env python3

from lxml.html import fromstring, tostring
import requests

# Descargar el contenido de la página con requests
url = 'https://www.w3schools.com/html/html_forms.asp'
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML
    page = fromstring(response.text)

    # Obtener el primer formulario de la página
    form = page.forms[0]
    print("Primer formulario encontrado:")
    print(tostring(form, pretty_print=True).decode('utf-8'))
else:
    print(f"Error al acceder a {url}: Código {response.status_code}")
