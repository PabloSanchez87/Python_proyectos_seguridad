#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Implementación de un cliente TCP que se conecte a un host y un puerto introducido por el usuario.
'''

import socket  # Importamos el módulo socket para manejar la comunicación en red

print('creando socket ...')
# Creamos un socket TCP (SOCK_STREAM) con IPv4 (AF_INET)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket creado')

# Solicitamos al usuario la dirección del host y el puerto
target_host = input("Introduce la dirección del host remoto:")  # Dirección del host a conectar
target_port = int(input("Introduce el puerto:"))  # Puerto al que se desea conectar

print("conexion con el host remoto")
# Establecemos la conexión con el host y el puerto especificados
my_socket.connect((target_host, target_port))
print('connection ok')  # Confirmación de que la conexión fue exitosa

# Preparamos la solicitud HTTP GET para obtener la página de inicio "/"
# Incluimos el encabezado "Host" necesario para solicitudes HTTP/1.1
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
# Enviamos la solicitud codificada en bytes
my_socket.send(request.encode())

# Recibimos datos del servidor con un tamaño de búfer de hasta 4096 bytes
data = my_socket.recv(4096)
# Imprimimos los datos recibidos en formato `repr` para mostrar caracteres especiales
print("Datos", repr(data))
# Mostramos la longitud de los datos recibidos
print("Longitud", len(data))

print('cerrando el socket')
# Cerramos el socket para liberar los recursos de la conexión
my_socket.close()
