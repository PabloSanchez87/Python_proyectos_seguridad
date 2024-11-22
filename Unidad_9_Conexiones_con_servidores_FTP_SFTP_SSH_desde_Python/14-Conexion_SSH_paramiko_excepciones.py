import paramiko
import socket

# Configuración de la conexión SSH
host = 'localhost'       # Dirección IP o hostname del servidor SSH
usuario = 'usuario'       # Usuario SSH
password = 'password'     # Contraseña del usuario

try:
    # Crear una instancia del cliente SSH
    ssh_client = paramiko.SSHClient()
    
    # Configurar el nivel de logs para mostrar información de depuración
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    
    # Cargar las claves conocidas del sistema (archivo known_hosts)
    ssh_client.load_system_host_keys()
    
    # Configurar la política para aceptar automáticamente claves de hosts desconocidos
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Establecer la conexión SSH al host remoto
    response = ssh_client.connect(host, port=22, username=usuario, password=password)
    print('Conectado con el host en el puerto 22')
    
    # Obtener el objeto de transporte (Transport) asociado a la conexión
    transport = ssh_client.get_transport()
    
    # Obtener las opciones de seguridad utilizadas en la conexión
    security_options = transport.get_security_options()
    
    # Mostrar las opciones de intercambio de claves (kex) y cifrados disponibles
    print("Opciones de intercambio de claves (kex):", security_options.kex)
    print("Cifrados disponibles:", security_options.ciphers)
except paramiko.BadAuthenticationType as exception:
    # Captura y manejo de errores de autenticación
    print("BadAuthenticationException:", exception)
except paramiko.SSHException as sshException:
    # Captura y manejo de errores generales de SSH
    print("SSHException:", sshException)
except socket.error as socketError:
    # Captura y manejo de errores de socket (por ejemplo, problemas de red)
    print("socketError:", socketError)
finally:
    # Cerrar la conexión SSH y liberar recursos
    print("Cerrando conexión")
    ssh_client.close()