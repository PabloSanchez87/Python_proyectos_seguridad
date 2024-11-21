#!/usr/bin/env python3

# Importar las bibliotecas necesarias
import nmap  # Biblioteca para interactuar con Nmap desde Python
import argparse  # Biblioteca para manejar argumentos en la línea de comandos

# Función de callback para procesar los resultados del escaneo
def callbackResult(host, scan_result):
    """
    Procesa y muestra los resultados del escaneo para un host específico.

    :param host: El host que fue escaneado (IP o nombre de dominio).
    :param scan_result: Resultados del escaneo como un diccionario.
    """
    # Extraer información sobre los puertos y sus estados
    port_state = scan_result['scan'][host]['tcp']
    # Mostrar el comando que se utilizó para realizar el escaneo
    print("Command line:" + scan_result['nmap']['command_line'])
    # Mostrar el estado de cada puerto escaneado
    for key, value in port_state.items():
        print('Port {0} --> {1}'.format(key, value))

# Clase que encapsula la lógica del escaneo asíncrono con Nmap
class NmapScannerAsync:
    def __init__(self):
        """
        Inicializa un objeto PortScannerAsync para manejar escaneos de forma asíncrona.
        """
        self.portScannerAsync = nmap.PortScannerAsync()

    def scanning(self):
        """
        Monitorea el estado del escaneo asíncrono, imprimiendo un mensaje mientras está en progreso.
        """
        while self.portScannerAsync.still_scanning():
            print("Scanning >>>")  # Indica que el escaneo sigue en curso
            self.portScannerAsync.wait(5)  # Espera 5 segundos antes de verificar nuevamente

    def nmapScanAsync(self, hostname, port):
        """
        Ejecuta un escaneo asíncrono en un host y puerto específicos.

        :param hostname: El host objetivo (IP o dominio).
        :param port: El puerto a escanear.
        """
        try:
            # Indica qué puerto se está verificando
            print("Checking port " + port + " ..........")
            # Inicia el escaneo con los argumentos especificados
            self.portScannerAsync.scan(
                hostname, 
                arguments="-A -sV -p" + port,  # Escaneo avanzado con detección de servicios (-sV) y versiones (-A)
                callback=callbackResult  # Llama a la función callback cuando los resultados están disponibles
            )
            # Monitorea el estado del escaneo
            self.scanning()
        except Exception as exception:
            # Maneja errores en la conexión o durante el escaneo
            print("Error to connect with " + hostname + " for port scanning", str(exception))

# Punto de entrada del programa
if __name__ == "__main__":
    # Configurar el analizador de argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description='Asynchronous Nmap scanner')
    
    # Agregar el argumento obligatorio para el host
    parser.add_argument(
        "--host", 
        dest="host", 
        help="target IP / domain", 
        required=True  # Este argumento es obligatorio
    )
    
    # Agregar el argumento opcional para los puertos
    parser.add_argument(
        "--ports", 
        dest="ports", 
        help="Specify the target port(s) separated by comma [default: 80,8080]", 
        default="80,8080"  # Valor predeterminado
    )
    
    # Parsear los argumentos proporcionados por el usuario
    parsed_args = parser.parse_args()
    port_list = parsed_args.ports.split(',')  # Dividir los puertos en una lista
    host = parsed_args.host  # Obtener el host proporcionado por el usuario

    # Realizar un escaneo para cada puerto especificado
    for port in port_list:
        NmapScannerAsync().nmapScanAsync(host, port)
