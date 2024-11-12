#!/usr/bin/python
# -*- coding: utf-8 -*-

# Importamos los módulos necesarios
import socket  # Para crear y gestionar la conexión de red mediante sockets
import time    # Para implementar los retardos entre reintentos de conexión

# Configuración del host y puerto
# Aquí definimos el nombre de dominio y el puerto del servidor al que queremos conectarnos
target_host = "www.google.es"  # Nombre del dominio de Google España
target_port = 80               # Puerto HTTP estándar para conexión web

# Configuración de reintentos
# Definimos el número máximo de intentos de conexión y el tiempo de espera entre intentos
max_retries = 5          # Número máximo de intentos en caso de fallo de conexión
retry_delay = 2          # Tiempo (en segundos) entre cada intento fallido

# Contador de intentos
attempts = 0             # Inicializamos el contador de intentos

# Bucle de conexión con reintentos
while attempts < max_retries:
    try:
        # Intento de conexión
        print('Intento de conexión #{}'.format(attempts + 1))
        
        # Crear un objeto socket TCP
        # socket.AF_INET indica el uso de direcciones IPv4
        # socket.SOCK_STREAM indica el protocolo TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar al host y puerto especificados
        s.connect((target_host, target_port))
        print('Conexión establecida')
        
        # Preparar y enviar una solicitud HTTP GET
        # Usamos el método HTTP GET para solicitar el recurso raíz ("/")
        request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
        s.send(request.encode())  # Codificamos la solicitud en bytes antes de enviarla
        
        # Recibir datos de la respuesta del servidor
        data = s.recv(4096)  # Leemos hasta 4096 bytes de datos
        print("Datos:", repr(data))  # Imprimimos la respuesta recibida
        print("Longitud:", len(data))  # Imprimimos la longitud de los datos recibidos
        
        # Cerrar el socket tras recibir la respuesta
        s.close()
        
        # Salir del bucle, ya que la conexión fue exitosa
        break
        
    except socket.error as e:
        # Si ocurre un error de socket, mostramos el mensaje y aumentamos el contador de intentos
        print(f"Error de conexión: {e}")
        attempts += 1
        s.close()  # Aseguramos que el socket se cierre tras el fallo
        
        # Si aún no alcanzamos el máximo de reintentos, esperamos antes de reintentar
        if attempts < max_retries:
            print(f"Reintentando en {retry_delay} segundos...")
            time.sleep(retry_delay)
        else:
            # Mensaje final si no se logra la conexión tras el número máximo de intentos
            print("No se pudo establecer la conexión después de varios intentos.")
