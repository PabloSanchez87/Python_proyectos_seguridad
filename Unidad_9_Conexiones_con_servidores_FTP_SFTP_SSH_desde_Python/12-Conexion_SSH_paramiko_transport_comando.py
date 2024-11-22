import paramiko

# Configuración de la conexión y del comando a ejecutar
host = 'localhost'         # Dirección IP o hostname del servidor SSH
username = 'linux'         # Nombre de usuario para la autenticación SSH
password = 'linux'         # Contraseña para el usuario
comando = "uname -a"       # Comando que se ejecutará en el servidor remoto

# Crear un objeto Transport para gestionar la conexión
sshTransport = paramiko.Transport(host)

try:
    print("Creando conexión con la clase Transport")
    
    # Iniciar el cliente SSH sobre la instancia de Transport
    sshTransport.start_client()
    
    # Autenticación utilizando usuario y contraseña
    sshTransport.auth_password(username=username, password=password)
    
    # Comprobar si la autenticación fue exitosa
    if sshTransport.is_authenticated():
        print("Conectado y autenticado al servidor SSH en el host", host)
        print("Detalles del host remoto conectado:", sshTransport.getpeername())  # Información del servidor remoto
        
        # Abrir una sesión para ejecutar comandos en el servidor remoto
        channel = sshTransport.open_session()
        
        # Ejecutar el comando especificado en el servidor remoto
        channel.exec_command(comando)
        
        # Recibir la salida del comando ejecutado
        respuesta = channel.recv(1024)  # Leer un máximo de 1024 bytes
        print('Comando %r/(%r) --> %s' % (comando, username, respuesta.decode('utf-8')))
except Exception as exception:
    # Capturar y mostrar errores en caso de que ocurra algún problema
    print("Error al conectar: ", exception)
finally:
    # Cerrar la conexión y liberar los recursos
    print("Cerrando conexión")
    sshTransport.close()