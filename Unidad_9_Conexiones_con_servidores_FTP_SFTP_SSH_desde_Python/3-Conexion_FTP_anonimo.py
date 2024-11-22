#!/usr/bin/env python3

import ftplib

# URL del servidor FTP al que queremos conectarnos
FTP_SERVER_URL = 'ftp.be.debian.org'

# Ruta actualizada del directorio en el servidor FTP donde se encuentra el archivo que deseamos descargar
DOWNLOAD_DIR_PATH = '/www.kernel.org/pub/linux/kernel/v5.x/'

# Nombre del archivo que deseamos descargar desde el servidor FTP
DOWNLOAD_FILE_NAME = 'ChangeLog-5.0'

def ftp_descarga_fichero(server, username):
    """
    Descarga un archivo desde un servidor FTP.
    
    Args:
        server (str): URL del servidor FTP.
        username (str): Nombre de usuario para autenticarse en el servidor FTP.
    """
    try:
        # Crear una instancia del cliente FTP y conectarse al servidor
        ftp_client = ftplib.FTP(server, username)
        
        # Cambiar al directorio especificado
        ftp_client.cwd(DOWNLOAD_DIR_PATH)
        
        # Abrir un archivo en modo escritura binaria para guardar el contenido descargado
        file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
        
        # Preparar el comando FTP para descargar el archivo
        ftp_cmd = 'RETR %s' % DOWNLOAD_FILE_NAME
        
        # Descargar el archivo de forma binaria, escribiendo directamente en `file_handler`
        ftp_client.retrbinary(ftp_cmd, file_handler.write)
        
        # Cerrar el archivo local después de completar la descarga
        file_handler.close()
        
        # Cerrar la conexión FTP de forma limpia
        ftp_client.quit()
        
        print(f"Archivo '{DOWNLOAD_FILE_NAME}' descargado correctamente.")
    except Exception as exception:
        # Capturar cualquier excepción durante el proceso de descarga y mostrar un mensaje de error
        print('No se ha podido descargar el fichero:', exception)

# Punto de entrada principal del script
if __name__ == '__main__':
    # Llama a la función para descargar el archivo desde el servidor FTP
    ftp_descarga_fichero(server=FTP_SERVER_URL, username='anonymous')
