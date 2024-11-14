#!/usr/bin/python

import shodan   # Importa el módulo de Shodan para trabajar con su API
import os       # Importa el módulo os para acceder a las variables de entorno

# Obtiene la clave de la API de Shodan desde la variable de entorno
SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

# Crea un objeto cliente de Shodan usando la API key obtenida
shodan_client = shodan.Shodan("SHODAN_API_KEY")

try:
    # Realiza una búsqueda en Shodan con el término 'apache'
    resultados = shodan_client.search('apache')
    
    # Muestra el número de resultados encontrados
    print("Número de resultados:", resultados['total'])
except Exception as exception:
    # Muestra un mensaje de error en caso de que ocurra una excepción
    print("Error:", str(exception))


