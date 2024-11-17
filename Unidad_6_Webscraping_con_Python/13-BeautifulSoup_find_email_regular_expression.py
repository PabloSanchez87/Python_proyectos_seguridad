#!/usr/bin/env python3
# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP y obtener el contenido de la página
import re  # Para trabajar con expresiones regulares
from bs4 import BeautifulSoup  # Para analizar y extraer información del HTML

# Encabezado de solicitud para evitar bloqueos por agentes de usuario
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# Solicitamos al usuario que proporcione la URL del sitio web
url = input("Introduzca la URL: ")

# Aseguramos que la URL tenga el prefijo adecuado
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url

try:
    # Realizamos una solicitud HTTP GET a la URL proporcionada por el usuario
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verificamos si la solicitud fue exitosa

    # Extraemos el contenido de la página en formato texto
    html_page = response.text

    # Analizamos el HTML de la página con BeautifulSoup utilizando el analizador 'lxml'
    soup = BeautifulSoup(html_page, 'lxml')

    # Definimos el patrón de búsqueda para direcciones de correo electrónico en formato `mailto:`
    email_pattern = re.compile(r'^mailto:([a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+)$', re.IGNORECASE)

    # Buscamos todas las etiquetas <a> que tengan un atributo 'href'
    emails = []
    for tag in soup.find_all('a', href=True):
        match = email_pattern.match(tag['href'])
        if match:
            # Extraemos y guardamos el correo limpio sin `mailto:`
            emails.append(match.group(1))

    # Imprimimos los correos encontrados
    if emails:
        print("Correos electrónicos encontrados:")
        for email in emails:
            print(email)
    else:
        print("No se encontraron correos electrónicos.")
except requests.exceptions.RequestException as e:
    print(f"Error al conectar con la URL: {e}")
