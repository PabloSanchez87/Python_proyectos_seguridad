#!/usr/bin/python
#-*- coding: utf-8 -*-

# Cliente básico con el módulo sockets
'''
Ejemplo para probar cómo enviar y recibir datos de un sitio web.

- Una vez establece la conexión, podemos enviar y recibir datos.
- La comunicación con el socket se puede hacer muy fácilmente gracias a dos funciones del módulo sockets: 
    - Comunicación TCP:
        - send()
        - recv()
    - Comunicación UDP:
        - sendto()
        - recvfrom()

- En el script de abajo,  creamos un objeto socket con los parámetros AF_INET y SOCK_STREAM para establecer una conexión TCP.
- Luego, establecemos la dirección del servidor remoto y le enviamos algunos datos.
- El último paso es recibir algunos datos e imprimir la respuesta.
'''


import socket  # Importamos el módulo socket para la comunicación en red

print('creando socket ...')
# Creamos un socket TCP/IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket creado')

# Definimos el host de destino, que puede ser una URL o una dirección IP
# target_host = "www.google.com" 
target_host = "142.250.200.100"  # Dirección IP de Google

# Definimos el puerto de destino, en este caso el puerto 80 para HTTP
target_port = 80

print("conexion con el host remoto")
# Establecemos la conexión con el servidor en el host y puerto especificados
s.connect((target_host, target_port))
print('connection ok')  # Confirmamos que la conexión se ha realizado correctamente

# Construimos la solicitud HTTP GET para obtener la página de inicio "/"
# La solicitud incluye el encabezado "Host" necesario para HTTP/1.1
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
# Enviamos la solicitud codificada en bytes al servidor
s.send(request.encode())

# Recibimos datos del servidor, con un máximo de 4096 bytes
data = s.recv(4096)
# Imprimimos los datos recibidos del servidor en formato "repr" para mostrar caracteres especiales
print("Datos", repr(data))
# Mostramos la longitud de los datos recibidos
print("Longitud", len(data))

print('cerrando el socket')
# Cerramos la conexión del socket para liberar los recursos
s.close()
