#!/usr/bin/env python

import shodan        # Importa la librería de Shodan para interactuar con su API
import re            # Importa re para trabajar con expresiones regulares si es necesario en el análisis
import os            # Importa os para acceder a variables de entorno

# Lista para almacenar las direcciones IP de los sitios encontrados
sitios = []

# Obtiene la clave de API de Shodan desde las variables de entorno
shodanKeyString = os.getenv("SHODAN_API_KEY")

# Inicializa el cliente de Shodan usando la clave de API
shodanApi = shodan.Shodan(shodanKeyString)

# account_info = shodanApi.info()
# print(account_info)

# Realiza una búsqueda en Shodan de hosts que permiten acceso anónimo en el puerto 21 (FTP)
resultados = shodanApi.search("port:21 Anonymous user logged in")

# Muestra el número de hosts encontrados que cumplen con el criterio de búsqueda
print("Número de hosts: " + str(len(resultados['matches'])))

# Recorre cada resultado de la búsqueda
for resultado in resultados['matches']:
    # Si existe una dirección IP en el resultado, la añade a la lista de sitios
    if resultado['ip_str'] is not None:
        sitios.append(resultado['ip_str'])
        
# Imprime cada dirección IP de la lista de sitios encontrados
for sitio in sitios:
    print(sitio)
