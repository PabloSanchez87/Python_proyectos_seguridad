#!/usr/bin/env python3

# Importar módulos necesarios
import getpass  # Para manejar contraseñas de forma segura
import paramiko  # Para realizar conexiones SSH y transferencias SFTP

# Definimos valores predeterminados para el host, puerto y ruta de archivo
HOSTNAME = 'localhost'  # Host predeterminado
PORT = 22  # Puerto predeterminado para SSH
FILE_PATH = '/tmp/test_sftp.txt'  # Ruta de archivo predeterminada en el servidor remoto

def sftp_download(username, password, hostname=HOSTNAME, port=PORT):
    """
    Conecta a un servidor remoto usando SSH y descarga un archivo especificado mediante SFTP.

    Args:
        username (str): Nombre de usuario para la conexión SSH.
        password (str): Contraseña del usuario.
        hostname (str): Dirección del servidor remoto. Por defecto es 'localhost'.
        port (int): Puerto para la conexión SSH. Por defecto es 22.
    """
    # Establecer una conexión SSH Transport
    ssh_transport = paramiko.Transport(hostname, int(port))  # Crear un objeto Transport para SSH
    ssh_transport.connect(username=username, password=password)  # Autenticarse con el servidor

    # Crear una sesión SFTP a partir del transporte
    sftp_session = paramiko.SFTPClient.from_transport(ssh_transport)

    # Solicitar la ruta del archivo remoto o usar el valor predeterminado
    file_path = input("Enter filepath: ") or FILE_PATH  # Si no se ingresa, usa FILE_PATH por defecto

    # Extraer el nombre del archivo del camino completo
    target_file = file_path.split('/')[-1]  # Obtiene solo el nombre del archivo (sin el directorio)

    # Descargar el archivo remoto al directorio local
    sftp_session.get(file_path, target_file)
    print(f"Downloaded file from: {file_path} to local file: {target_file}")

    # Cerrar la sesión SFTP
    sftp_session.close()
    print("SFTP session closed.")

if __name__ == '__main__':
    """
    Solicita al usuario la información necesaria para conectarse al servidor remoto y 
    llama a la función sftp_download para descargar un archivo especificado.
    """
    # Solicitar al usuario los datos de conexión
    hostname = input("Enter the target hostname: ")  # Dirección del servidor remoto
    port = input("Enter the target port: ")  # Puerto del servidor remoto
    username = input("Enter your username: ")  # Nombre de usuario
    password = getpass.getpass(prompt="Enter your password: ")  # Contraseña (ocultada al escribir)

    # Llamar a la función para descargar un archivo usando SFTP
    sftp_download(username, password, hostname, port)
