import paramiko

def ssh_comando(ip, user, passwd, comando):
    """
    Función para ejecutar un comando en un servidor remoto utilizando SSH.
    
    Args:
        ip (str): Dirección IP o hostname del servidor remoto.
        user (str): Nombre de usuario para la autenticación SSH.
        passwd (str): Contraseña del usuario.
        comando (str): Comando que se desea ejecutar en el servidor remoto.
    """
    # Crear un objeto SSHClient para manejar la conexión SSH
    client = paramiko.SSHClient()
    
    # Registrar todas las conexiones y actividades en un fichero de log
    paramiko.util.log_to_file('paramiko.log')
    
    # Cargar las claves del sistema para la autenticación (host keys conocidas)
    client.load_system_host_keys()
    
    # Configurar la política de manejo de claves de hosts desconocidos.
    # AutoAddPolicy automáticamente acepta claves desconocidas sin requerir intervención.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Conectar al servidor remoto utilizando las credenciales proporcionadas
    client.connect(ip, username=user, password=passwd)
    
    # Abrir una sesión SSH para ejecutar comandos en el servidor remoto
    ssh_session = client.get_transport().open_session()
    
    if ssh_session.active:  # Verificar si la sesión SSH está activa
        # Ejecutar el comando proporcionado en el servidor remoto
        ssh_session.exec_command(comando)
        
        # Recibir y mostrar la salida del comando (hasta un máximo de 1024 bytes)
        print(ssh_session.recv(1024))
        
        # Cerrar la conexión SSH una vez que se termina la operación
        client.close()

# Ejemplo de uso: Ejecutar el comando 'ls -la' en el servidor localhost con credenciales
ssh_comando('localhost', 'usuario', 'password', 'ls -la')