#!/usr/bin/env python3

from ftplib import FTP, error_perm

def list_directory(ftp, path):
    """Intenta listar un directorio usando nlst() y manejar errores."""
    try:
        ftp.cwd(path)
        print(f"\nContenido del directorio '{path}':")
        files = ftp.nlst()  # Obtener la lista de archivos y directorios
        if files:
            for file in files:
                print(file)
        else:
            print("El directorio está vacío.")
    except error_perm as e:
        print(f"Error al acceder al directorio '{path}': {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Crear cliente FTP y conectarse al servidor
ftp_client = FTP('ftp.be.debian.org')

# Mostrar el mensaje de bienvenida del servidor
print("Server: ", ftp_client.getwelcome())

# Iniciar sesión en el servidor FTP
print(ftp_client.login())

# Listar los directorios disponibles en la raíz
print("\nFicheros y directorios en el directorio raíz:")
try:
    root_files = ftp_client.nlst()
    for file in root_files:
        print(file)
except error_perm as e:
    print(f"Error al listar el directorio raíz: {e}")

# Intentar acceder a diferentes directorios disponibles
list_directory(ftp_client, '/debian')
list_directory(ftp_client, '/debian-security')
list_directory(ftp_client, '/www.kernel.org')  # Intentar ruta del kernel

# Cerrar la conexión FTP
ftp_client.quit()
