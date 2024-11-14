#!/usr/bin/env python

import shodan      # Importa la librería de Shodan para interactuar con su API
import requests    # Importa requests para hacer solicitudes HTTP
import os          # Importa os para acceder a las variables de entorno del sistema

# Obtiene la clave de API de Shodan desde las variables de entorno
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

# Inicializa el cliente de Shodan usando la clave de API
api = shodan.Shodan(SHODAN_API_KEY)

# Define el dominio que queremos analizar
dominio = 'www.google.com'

# URL para resolver el dominio a una IP usando la API de Shodan
dnsResolve = f'https://api.shodan.io/dns/resolve?hostnames={dominio}&key={SHODAN_API_KEY}'

try:
    # Envía una solicitud a la API de Shodan para resolver el dominio a su IP
    resolved = requests.get(dnsResolve)
    # Extrae la IP resuelta del JSON devuelto usando el nombre de dominio como clave
    hostIP = resolved.json()[dominio]
   
    # Realiza una búsqueda en Shodan utilizando la IP obtenida
    host = api.host(hostIP)
    # Muestra la IP del host
    print("IP: %s" % host['ip_str'])
    # Muestra la organización a la que pertenece la IP
    print("Organization: %s" % host.get('org', 'n/a'))
    # Muestra el sistema operativo (si está disponible)
    print("Operating System: %s" % host.get('os', 'n/a'))

    # Recorre todos los banners de los servicios encontrados en el host
    for item in host['data']:
        # Muestra el puerto en el que el servicio está activo
        print("Port: %s" % item['port'])
        # Muestra el banner del servicio, que contiene detalles sobre el servicio
        print("Banner: %s" % item['data'])
        
except shodan.APIError as exception:
    # Muestra un mensaje de error si ocurre un problema con la API de Shodan
    print('Error: %s' % exception)
