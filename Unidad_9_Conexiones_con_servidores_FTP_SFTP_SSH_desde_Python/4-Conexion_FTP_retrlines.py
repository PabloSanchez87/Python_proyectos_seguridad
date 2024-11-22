#!/usr/bin/env python3

from ftplib import FTP

def writeData(data):
    """
    Callback que escribe líneas de datos recibidas desde el servidor FTP en un archivo local.
    Args:
        data (str): Línea de texto recibida del servidor FTP.
    """
    file_descriptor.write(data + "\n")  # Escribe cada línea en el archivo con un salto de línea

# Crear una instancia del cliente FTP y conectarse al servidor
ftp_client = FTP('ftp.be.debian.org')

# Iniciar sesión en el servidor FTP (modo anónimo por defecto)
ftp_client.login()

# Cambiar al directorio donde se encuentra el archivo en el servidor FTP
ftp_client.cwd('/www.kernel.org/pub/linux/kernel/v5.x/')

# Abrir un archivo local en modo escritura de texto para guardar los datos descargados
file_descriptor = open('ChangeLog-5.0', 'wt')

# Descargar el archivo línea por línea, usando 'writeData' como callback para escribir cada línea
ftp_client.retrlines('RETR ChangeLog-5.0', writeData)

# Cerrar el archivo local después de completar la descarga
file_descriptor.close()

# Cerrar la conexión FTP de forma limpia
ftp_client.quit()
