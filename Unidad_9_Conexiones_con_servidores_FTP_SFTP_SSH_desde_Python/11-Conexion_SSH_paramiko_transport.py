import paramiko

# Configuración de la conexión
host = 'localhost'  # Hostname o dirección IP del servidor SSH
username = 'linux'  # Usuario para la autenticación SSH
password = 'linux'  # Contraseña para el usuario

# Crear un objeto Transport para gestionar la conexión
sshTransport = paramiko.Transport(host)

try:
    print("Creando conexión con la clase Transport")
    
    # Iniciar el cliente SSH en el objeto Transport
    sshTransport.start_client()
    
    # Autenticación utilizando el método auth_password con usuario y contraseña
    sshTransport.auth_password(username=username, password=password)
    
    # Comprobar si la autenticación fue exitosa
    if sshTransport.is_authenticated():
        print("Conectado y autenticado en el servidor SSH en el host", host)
    else:
        print("No se pudo autenticar al usuario.")
except Exception as exception:
    # Capturar y mostrar errores ocurridos durante la conexión o autenticación
    print("Error al conectar: ", exception)
finally:
    # Finalizar la conexión y liberar los recursos
    print("Cerrando conexión")
    sshTransport.close()
