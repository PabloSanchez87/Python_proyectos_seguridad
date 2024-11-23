#!/usr/bin/env python3

# Importar las bibliotecas necesarias
import pysftp  # Para realizar conexiones SFTP
import getpass  # Para ocultar la entrada de contraseñas en la terminal

# Constantes por defecto para el servidor SFTP
HOSTNAME = 'localhost'  # Nombre del host del servidor (por defecto localhost)
PORT = 22  # Puerto estándar para conexiones SFTP/SSH

# Definición de la función para obtener archivos desde un servidor SFTP
def sftp_getfiles(username, password, hostname=HOSTNAME, port=PORT):
    """
    Establece una conexión SFTP con un servidor remoto y muestra
    la lista de archivos y directorios en el directorio raíz del servidor.
    
    Args:
        username (str): Nombre de usuario para la conexión SFTP.
        password (str): Contraseña del usuario.
        hostname (str): Nombre del host o dirección IP del servidor remoto.
        port (int): Número de puerto para la conexión SFTP.

    Returns:
        None
    """
    
    
    # Establecer la conexión SFTP usando las credenciales proporcionadas
    with pysftp.Connection(host=hostname, username=username, password=password, port=int(port)) as sftp:
        print("Conexión establecida con el servidor ... ")

        # Cambiar al directorio raíz del servidor remoto
        sftp.cwd('/')

        # Obtener la estructura del directorio raíz
        list_directory = sftp.listdir_attr()  # Devuelve información detallada de cada archivo/directorio

        # Imprimir la información de cada archivo/directorio
        for directory in list_directory:
            print(
                directory.filename,  # Nombre del archivo/directorio
                directory.longname,  # Representación detallada del archivo/directorio (permisos, tamaño, etc.)
                directory  # Objeto completo que contiene los atributos del archivo/directorio
            )

    # La conexión se cierra automáticamente al salir del bloque "with"

# Bloque principal del programa
if __name__ == '__main__':
    # Solicitar al usuario la información de conexión
    hostname = input("Introduce el nombre del host: ")  # Nombre o IP del servidor remoto
    port = input("Introduce el puerto: ")  # Puerto para la conexión SFTP
    username = input("Introduce usuario: ")  # Usuario SFTP
    password = getpass.getpass(prompt="Introduce password: ")  # Contraseña del usuario, oculta en la terminal

    # Llamar a la función para establecer conexión y listar archivos
    sftp_getfiles(username, password, hostname, port)


'''
import pysftp
import getpass

HOSTNAME = 'localhost'
PORT = 22

def sftp_getfiles(username, password, hostname=HOSTNAME, port=PORT):
    # Deshabilitar la validación del host
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None  # Permitir la conexión sin verificar las claves del host

    # Conectarse al servidor SFTP
    with pysftp.Connection(host=hostname, username=username, password=password, port=int(port), cnopts=cnopts) as sftp:
        print("Conexión establecida con el servidor ... ")
        # Cambiar al directorio raíz
        sftp.cwd('/')
        # Listar los archivos/directorios del directorio raíz
        list_directory = sftp.listdir_attr()
        for directory in list_directory:
            print(directory.filename, directory.longname, directory)

if __name__ == '__main__':
    hostname = input("Introduce el nombre del host: ")
    port = input("Introduce el puerto: ")
    username = input("Introduce usuario: ")
    password = getpass.getpass(prompt="Introduce password: ")
    sftp_getfiles(username, password, hostname, port)
'''