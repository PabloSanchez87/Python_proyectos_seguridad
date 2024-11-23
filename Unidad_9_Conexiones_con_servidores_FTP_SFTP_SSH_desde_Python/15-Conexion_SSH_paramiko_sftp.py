#!/usr/bin/env python3

# Importar módulos necesarios
import getpass  # Para manejar contraseñas de forma segura
import paramiko  # Para realizar conexiones SSH y SFTP

# Definimos valores predeterminados para el host y el puerto
HOSTNAME = 'localhost'
PORT = 22

def sftp_list_files(username, password, hostname=HOSTNAME, port=PORT):
    """
    Conecta a un servidor remoto usando SSH y lista los archivos en el directorio remoto actual mediante SFTP.

    Args:
        username (str): Nombre de usuario para la conexión SSH.
        password (str): Contraseña del usuario.
        hostname (str): Dirección del servidor remoto. Por defecto es 'localhost'.
        port (int): Puerto para la conexión SSH. Por defecto es 22.
    """
    # Crear un cliente SSH
    ssh_client = paramiko.SSHClient()

    # Configurar el registro de depuración para diagnosticar problemas
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)

    # Configurar la política para aceptar automáticamente claves de host desconocidas
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Conectar al servidor remoto
    ssh_client.connect(hostname, port, username, password)
    print(f"SSH Client connected to {hostname}.")

    # Crear un objeto SFTP a partir de la conexión SSH
    sftp = ssh_client.open_sftp()
    print(f"SFTP session established with {hostname}.")

    # Listar los archivos en el directorio actual del servidor remoto
    dirlist = sftp.listdir('.')
    print(f"Files in the remote directory: {dirlist}")

    # Cerrar la conexión SSH
    ssh_client.close()
    print("SSH Client disconnected.")

if __name__ == '__main__':
    """
    Solicita al usuario la información necesaria para conectarse al servidor remoto y 
    llama a la función sftp_list_files para listar los archivos en el directorio remoto actual.
    """
    # Solicitar al usuario los datos de conexión
    hostname = input("Enter the target hostname: ")  # Dirección del servidor remoto
    port = int(input("Enter the target port: "))  # Puerto del servidor remoto
    username = input("Enter your username: ")  # Nombre de usuario
    password = getpass.getpass(prompt="Enter your password: ")  # Contraseña (ocultada al escribir)

    # Llamar a la función para listar archivos usando SFTP
    sftp_list_files(username, password, hostname, port)
