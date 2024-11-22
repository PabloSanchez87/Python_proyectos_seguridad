#!/usr/bin/env python3

import ftplib  # Importa el módulo para trabajar con servidores FTP

def anonymousLogin(hostname):
    """
    Intenta realizar un inicio de sesión anónimo en un servidor FTP y lista su contenido si es exitoso.

    Args:
        hostname (str): Nombre o dirección del servidor FTP.
    """
    try:
        # Crear una instancia del cliente FTP y conectarse al servidor
        ftp = ftplib.FTP(hostname)
        
        # Intentar iniciar sesión de forma anónima
        response = ftp.login('anonymous', 'anonymous')  # Usa 'anonymous' como usuario y contraseña
        print(response)  # Imprime la respuesta del servidor al comando LOGIN
        
        # Verificar si el inicio de sesión fue exitoso
        if "230 Anonymous access granted" in response:
            print('\n[*] ' + str(hostname) + ' FTP Anonymous Login Succeeded.')
            
            # Mostrar el mensaje de bienvenida del servidor
            print(ftp.getwelcome())
            
            # Listar los archivos y directorios disponibles en el directorio raíz
            ftp.dir()
        else:
            print('\n[-] ' + str(hostname) + ' FTP Anonymous Login Failed.')
    
    except Exception as e:
        # Manejo de errores en caso de fallo al conectarse o iniciar sesión
        print(str(e))
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Login Failed.')

# Dirección del servidor FTP al que queremos conectarnos
hostname = 'ftp.be.debian.org'

# Llama a la función para intentar un inicio de sesión anónimo en el servidor FTP
anonymousLogin(hostname)
