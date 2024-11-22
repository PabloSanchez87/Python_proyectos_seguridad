#!/usr/bin/env python3

import ftplib  # Importa la biblioteca `ftplib` para trabajar con servidores FTP

def ftpListDirectory(ftp):
    """
    Lista el contenido del directorio actual en el servidor FTP, buscando archivos con extensiones específicas.
    
    Args:
        ftp (ftplib.FTP): Objeto de conexión FTP ya autenticado.

    Returns:
        list: Lista de nombres de archivos encontrados con extensiones específicas (.php, .htm, .asp).
    """
    try:
        # Obtener la lista de archivos y directorios en el directorio actual del servidor FTP
        dirList = ftp.nlst()  # `nlst` devuelve una lista de nombres simples (no detalles como `dir`).
        print(dirList)  # Muestra la lista completa de archivos y directorios
    except:
        # Si no se puede listar el directorio, muestra un mensaje de error y devuelve una lista vacía
        dirList = []
        print('[-] Could not list directory contents.')
        return

    # Filtrar la lista de archivos para buscar extensiones específicas
    retList = []
    for fileName in dirList:
        fn = fileName.lower()  # Convierte el nombre del archivo a minúsculas para facilitar la búsqueda
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            # Si el archivo tiene una de las extensiones buscadas, lo añade a la lista de resultados
            print('[+] Found default page: ' + fileName)
            retList.append(fileName)
            
    return retList

def anonymousLogin(hostname):
    """
    Intenta realizar un inicio de sesión anónimo en el servidor FTP especificado.
    
    Args:
        hostname (str): Dirección o nombre del servidor FTP.

    Returns:
        ftplib.FTP or bool: Objeto FTP autenticado si el inicio de sesión es exitoso, o False si falla.
    """
    try:
        # Crear una instancia del cliente FTP y conectarse al servidor
        ftp = ftplib.FTP(hostname)
        
        # Intentar iniciar sesión con credenciales anónimas
        ftp.login('anonymous', 'anonymous')
        
        # Mostrar el mensaje de bienvenida del servidor
        print(ftp.getwelcome())
        
        # Activar el modo pasivo para transferencias de datos (común en servidores modernos)
        ftp.set_pasv(1)
        
        # Mostrar el contenido del directorio raíz del servidor
        print(ftp.dir())
        
        # Mensaje de éxito si la conexión y el inicio de sesión son exitosos
        print('\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.')
        return ftp  # Devuelve el objeto FTP autenticado
    except Exception as e:
        # Manejo de errores en caso de fallos en la conexión o autenticación
        print(str(e))
        print('\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.')
        return False  # Devuelve False si el inicio de sesión falla

# Dirección del servidor FTP al que queremos conectarnos
host = 'ftp.be.debian.org'

# Intentar realizar un inicio de sesión anónimo
ftp = anonymousLogin(host)

# Si el inicio de sesión fue exitoso, listar el contenido del directorio
if ftp:
    ftpListDirectory(ftp)
