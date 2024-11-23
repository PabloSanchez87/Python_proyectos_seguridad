#!/usr/bin/env python3

# Importamos las bibliotecas necesarias
import pysftp  # Biblioteca para trabajar con SFTP (Secure File Transfer Protocol)
import getpass  # Biblioteca para ocultar la entrada del usuario al pedir contraseñas

# Constantes predeterminadas para el nombre del host y puerto
HOSTNAME = 'localhost'  # Host predeterminado (puede ser cambiado por el usuario)
PORT = 22  # Puerto predeterminado para SFTP

def sftp_getfiles(username, password, hostname=HOSTNAME, port=PORT):
    """
    Establece una conexión SFTP y descarga un archivo desde el servidor.

    Args:
        username (str): Nombre de usuario para autenticar en el servidor SFTP.
        password (str): Contraseña para autenticar en el servidor SFTP.
        hostname (str): Nombre del host o dirección IP del servidor SFTP. Por defecto es 'localhost'.
        port (int): Puerto del servidor SFTP. Por defecto es 22.

    Returns:
        None. (El archivo se descarga en el directorio local indicado.)
    """
    # Establecemos una conexión SFTP con las credenciales proporcionadas
    with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
        print("Conexión establecida con el servidor ... ")
        
        # Ruta del archivo remoto que queremos descargar
        remoteFilePath = '/tmp/test_sftp.txt'
        
        # Ruta local donde se guardará el archivo descargado
        localFilePath = 'test_sftp.txt'
        
        # Descargamos el archivo desde el servidor SFTP
        sftp.get(remoteFilePath, localFilePath)
        print(f"Archivo descargado exitosamente desde {remoteFilePath} a {localFilePath}")

    # La conexión SFTP se cierra automáticamente al salir del bloque `with`

if __name__ == '__main__':
    # Solicita al usuario el nombre del host
    hostname = input("Introduce el nombre del host: ")
    
    # Solicita al usuario el puerto
    port = input("Introduce el puerto: ")
    
    # Solicita al usuario el nombre de usuario
    username = input("Introduce usuario: ")
    
    # Solicita al usuario la contraseña de forma segura (oculta la entrada)
    password = getpass.getpass(prompt="Introduce password: ")
    
    # Llama a la función para descargar el archivo mediante SFTP
    sftp_getfiles(username, password, hostname, port)
