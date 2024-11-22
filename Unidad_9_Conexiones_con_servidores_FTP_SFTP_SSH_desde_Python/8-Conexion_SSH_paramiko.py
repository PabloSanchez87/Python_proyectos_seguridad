import paramiko  # Biblioteca para manejar conexiones SSH en Python

# Configuración del servidor SSH al que queremos conectarnos
host = 'localhost'  # Dirección del servidor (localhost en este caso)
username = 'username'  # Nombre de usuario para la conexión SSH
password = 'password'  # Contraseña del usuario

# Crear una instancia del cliente SSH
sshCliente = paramiko.SSHClient()

# Configurar el cliente SSH para aceptar automáticamente claves de host no conocidas
# Esto evita que el programa falle si el host no está en el archivo known_hosts
sshCliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print("Creando conexión")
    
    # Conectar al servidor SSH con las credenciales proporcionadas
    sshCliente.connect(host, username=username, password=password)
    
    # Mensaje de éxito si la conexión es establecida
    print("Conectado")
except Exception as exception:
    # Manejar errores en caso de que la conexión falle
    print("Error al conectar: ", exception)
finally:
    # Cerrar la conexión SSH, independientemente de si tuvo éxito o no
    print("Cerrando conexión")
    sshCliente.close()