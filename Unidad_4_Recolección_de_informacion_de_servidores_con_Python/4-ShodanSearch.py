#!/usr/bin/env python

import shodan   # Importa la biblioteca de Shodan para interactuar con su API
import re       # Importa la biblioteca de expresiones regulares (aunque no se usa en el código)

# Clase principal para realizar búsquedas en Shodan
class ShodanSearch:
    """Clase para buscar en Shodan"""

    def __init__(self, API_KEY):
        # Inicializa el cliente de la API de Shodan con la API key proporcionada
        self.api = shodan.Shodan(API_KEY)

    def buscar(self, cadena):
        """Realiza una búsqueda en Shodan según la cadena dada"""
        try:
            # Ejecuta la búsqueda con el término pasado como parámetro
            resultado = self.api.search(str(cadena))
            return resultado
        except Exception as exception:
            # Si ocurre un error, imprime el mensaje de error y devuelve una lista vacía
            print('Ha ocurrido un error: %s' % exception)
            resultado = []
        return resultado

    def obtener_info_host(self, IP):
        """Obtiene la información sobre una IP específica en Shodan"""
        try:
            # Realiza la consulta de información sobre el host dado (IP)
            resultados = self.api.host(IP)
            return resultados
        except Exception as exception:
            # Si ocurre un error, imprime el mensaje de error y devuelve una lista vacía
            print('Ha ocurrido un error: %s' % exception)
            resultados = []
        return resultados

# Función que muestra cómo usar el script
def uso():
    print(r"""Uso: ShodanSearch.py {OPTION} {CADENA | HOST}
     OPCIONES:
      -s, --search: Para buscar segun una determinada cadena
      -h, --host: Para obtener la informacion de un host segun su IP
     EJEMPLOS
      ShodanSearch.py --search apache
      ShodanSearch.py --host 8.8.8.8""")

# Función que imprime un banner decorativo
def banner():
    print(r"""
         ____  _               _             _____      
                / ___|| |__   ___   __| | __ _ _ __
                \___ \| '_ \ / _ \ / _` |/ _` | '_ \  
                 ___) | | | | (_) | (_| | (_| | | | |  
                |____/|_| |_|\___/ \__,_|\__,_|_| |_|
                                               Search
    """)

# Función principal que ejecuta el programa según los argumentos pasados
def main():
    import sys   # Importa sys para manejar argumentos de línea de comandos
    import time  # Importa time para pausar antes de mostrar resultados
    import os    # Importa os para acceder a variables de entorno

    # Obtiene la clave de API de Shodan desde las variables de entorno
    SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
    shodan = ShodanSearch(SHODAN_API_KEY)  # Crea una instancia de ShodanSearch con la API key

    # Verifica que se hayan pasado suficientes argumentos
    if len(sys.argv) < 3:
        uso()  # Muestra el mensaje de uso si hay menos de 3 argumentos
        sys.exit(2)
    else:
        # Opción para realizar una búsqueda
        if sys.argv[1] == '--search':
            banner()  # Muestra el banner decorativo
            time.sleep(3)  # Pausa de 3 segundos antes de ejecutar la búsqueda
            resultados = shodan.buscar(sys.argv[2])  # Realiza la búsqueda

            # Si hay resultados, los muestra
            if len(resultados) != 0:
                print('Cantidad de resultados encontrados: %s' % resultados['total'])
                for resultado in resultados['matches']:
                    # Imprime la información de cada resultado
                    print('Ciudad: %s' % resultado['location']['city'])
                    print('Pais: %s' % resultado['location']['country_name'])
                    print('IP: %s' % resultado.get('ip_str'))
                    print('O.S: %s' % resultado.get('os', 'Unknown'))
                    print('Puerto: %s' % resultado.get('port'))
                    print('Hostnames: %s' % resultado.get('hostnames'))
                    print('Latitude: %s' % resultado['location']['latitude'])
                    print('Longitude: %s' % resultado['location']['longitude'])
                    print('Actualizado en: %s' % resultado.get('timestamp'))
                    print(resultado['data'])

                # Muestra información adicional, si está disponible
                if 'organizations' in resultados.keys():
                    for key, value in resultados['organizations'].items():
                        print(key + ":" + value)
                if 'countries' in resultados.keys():
                    for key, value in resultados['countries'].items():
                        print(key + ":" + value)
                if 'cities' in resultado.keys():
                    for key, value in resultados['cities'].items():
                        print(key + ":" + value)

        # Opción para obtener información de un host específico
        elif sys.argv[1] == '--host':
            banner()  # Muestra el banner decorativo
            time.sleep(3)  # Pausa de 3 segundos antes de ejecutar la búsqueda
            host = shodan.obtener_info_host(sys.argv[2])  # Obtiene información sobre el host

            # Si hay información sobre el host, la muestra
            if len(host) != 0:
                print("keys", host.keys())
                # Imprime detalles del host
                print("IP: %s Organization: %s Operating System: %s " % (
                    host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
                if 'ip' in host.keys():
                    print('IP: %s' % host.get('ip_str'))
                if 'country_name' in host.keys():
                    print('Pais: %s' % host.get('country_name', 'Unknown'))
                if 'country_code' in host.keys():
                    print('Codigo pais: %s' % host.get('country_code', 'Unknown'))
                if 'city' in host.keys():
                    print('City: %s' % host.get('city', 'Unknown'))
                if 'latitude' in host.keys():
                    print('Latitude: %s' % host.get('latitude'))
                if 'longitude' in host.keys():
                    print('Longitude: %s' % host.get('longitude'))
                if 'hostnames' in host.keys():
                    print('Hostnames: %s' % host.get('hostnames'))
                
                # Imprime los banners de los servidores
                try:
                    for i in host['data']:
                        print('Puerto: %s' % i['port'])
                        print('Banner: %s' % i['banner'])
                except Exception as exception:
                    print(exception)
                    pass
        else:
            # Si no se pasa una opción válida, muestra el uso y sale del programa
            uso()
            sys.exit(2)

# Punto de entrada principal
if __name__ == '__main__':
    main()
