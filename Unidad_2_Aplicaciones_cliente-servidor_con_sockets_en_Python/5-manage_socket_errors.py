#!/usr/bin/env python
#--*-- coding:UTF-8 --*--

#!/usr/bin/env python
# --*-- coding:UTF-8 --*--

import socket  # Importamos el módulo socket para manejar la comunicación en red
import sys  # Importamos el módulo sys para gestionar la salida del programa en caso de errores


host = "domain/ip_address"  
port = 9999  

# Definimos el host y puerto finales a utilizar para la conexión
host = "www.bing.com"  # Host de destino (en este caso, Bing)
port = 111  # Puerto de destino para la conexión

try:
    # Creamos un socket TCP (SOCK_STREAM) usando IPv4 (AF_INET)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Establecemos un tiempo de espera de 5 segundos para la conexión
    s.settimeout(5)
except socket.error as e:
    # En caso de error al crear el socket, mostramos un mensaje y salimos del programa
    print("socket create error: %s" % e)
    sys.exit(1)  # Terminamos el programa con un código de error

try:
    # Intentamos establecer la conexión con el host y puerto especificados
    s.connect((host, port))
    print(s)  # Imprimimos el objeto socket si la conexión es exitosa
except socket.timeout as e:
    # Si ocurre un tiempo de espera (timeout), mostramos un mensaje y salimos del programa
    print("Timeout %s" % e)
    sys.exit(1)
except socket.gaierror as e:
    # Si hay un error en la resolución de la dirección del host (gaierror), lo indicamos y salimos
    print("connection error to the server: %s" % e)
    sys.exit(1)
except socket.error as e:
    # Capturamos cualquier otro error de conexión, lo mostramos y salimos del programa
    print("Connection error: %s" % e)
    sys.exit(1)


