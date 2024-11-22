#!/usr/bin/env python3

import paramiko
import getpass

def run_ssh_command(hostname, user, passwd, command):
    """
    Ejecuta un comando en un servidor remoto utilizando el protocolo SSH.
    
    Args:
        hostname (str): Dirección IP o hostname del servidor remoto.
        user (str): Nombre de usuario para autenticarse en el servidor.
        passwd (str): Contraseña del usuario para autenticarse.
        command (str): Comando que se ejecutará en el servidor remoto.
    """
    # Crear una instancia del objeto Transport
    transport = paramiko.Transport((hostname, 22))  # Puerto predeterminado 22
    try:
        # Iniciar el cliente SSH
        transport.start_client()
    except Exception as exception:
        # Manejar errores durante la inicialización del cliente
        print("Error al iniciar el cliente SSH:", exception)
        return  # Terminar la ejecución si no se puede iniciar el cliente

    try:
        # Autenticarse con usuario y contraseña
        transport.auth_password(username=user, password=passwd)
    except Exception as e:
        # Manejar errores de autenticación
        print("Error en la autenticación:", e)
        return  # Terminar la ejecución si falla la autenticación

    # Verificar si la autenticación fue exitosa
    if transport.is_authenticated():
        print("Conectado al servidor:", transport.getpeername())
        
        # Abrir un canal de sesión para ejecutar el comando
        channel = transport.open_session()
        
        # Enviar el comando al servidor remoto
        channel.exec_command(command)
        
        # Recibir y mostrar la respuesta del comando
        response = channel.recv(1024)  # Leer un máximo de 1024 bytes de salida
        print('Comando %r(%r) --> %s' % (command, user, response.decode('utf-8')))
    else:
        print("No se pudo autenticar al usuario.")
    
    # Cerrar la conexión al servidor
    transport.close()

if __name__ == '__main__':
    # Solicitar los detalles de la conexión al usuario
    hostname = input("Introduce el hostname: ")  # Dirección IP o nombre del host
    username = input("Introduce usuario: ")     # Usuario SSH
    password = getpass.getpass(prompt="Introduce password: ")  # Contraseña (oculta)
    comando = input("Introduce comando: ")     # Comando a ejecutar

    # Llamar a la función para ejecutar el comando
    run_ssh_command(hostname, username, password, comando)