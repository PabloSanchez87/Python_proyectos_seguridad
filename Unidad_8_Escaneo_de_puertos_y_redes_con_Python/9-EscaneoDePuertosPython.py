#!/usr/bin/env python3

import nmap  # Librería para interactuar con Nmap
import argparse  # Librería para manejar argumentos de línea de comandos

# Función de callback para procesar los resultados de los scripts de Nmap sobre FTP
def callbackFTP(host, result):
    """
    Procesa los resultados del escaneo asíncrono de Nmap para servicios FTP.
    Args:
        host (str): Dirección IP o nombre de host objetivo.
        result (dict): Resultados del escaneo Nmap.
    """
    try:
        # Obtiene los resultados del script ejecutado en el puerto 21
        script = result['scan'][host]['tcp'][21]['script']
        print("Command line: " + result['nmap']['command_line'])
        # Itera sobre los resultados de los scripts y los imprime
        for key, value in script.items():
            print('Script {0} --> {1}'.format(key, value))
    except KeyError:
        # Maneja casos donde no haya resultados de script disponibles
        pass

# Clase para manejar escaneos asíncronos de Nmap, enfocada en FTP
class NmapScannerAsyncFTP:
    def __init__(self):
        """
        Inicializa las instancias de PortScanner y PortScannerAsync de la librería nmap.
        """
        self.portScanner = nmap.PortScanner()  # Sincronización
        self.portScannerAsync = nmap.PortScannerAsync()  # Asincronización

    def scanning(self):
        """
        Controla la espera mientras los escaneos asíncronos siguen ejecutándose.
        """
        while self.portScannerAsync.still_scanning():
            print("Scanning >>>")
            self.portScannerAsync.wait(10)  # Espera 10 segundos antes de verificar nuevamente

    def nmapScanAsync(self, hostname, port):
        """
        Realiza un escaneo sobre un puerto específico en el host objetivo.
        Args:
            hostname (str): Dirección IP o nombre de host.
            port (str): Puerto a escanear.
        """
        try:
            print("Checking port " + port + " ..........")
            # Escaneo del puerto especificado en el host
            self.portScanner.scan(hostname, port)
            self.state = self.portScanner[hostname]['tcp'][int(port)]['state']
            print(" [+] " + hostname + " tcp/" + port + " " + self.state)

            # Verifica si el puerto 21 (FTP) está abierto y realiza escaneos con scripts de Nmap
            if (port == '21') and self.portScanner[hostname]['tcp'][int(port)]['state'] == 'open':
                print('Checking FTP port with Nmap scripts...')
                
                # Lista de scripts a ejecutar para el puerto FTP
                scripts = [
                    "ftp-anon.nse", "ftp-bounce.nse", "ftp-libopie.nse",
                    "ftp-proftpd-backdoor.nse", "ftp-vsftpd-backdoor.nse"
                ]

                for script in scripts:
                    print(f'Checking {script} .....')
                    self.portScannerAsync.scan(
                        hostname, arguments=f"-A -sV -p21 --script {script}", callback=callbackFTP
                    )
                    self.scanning()

        except Exception as exception:
            # Manejo de errores durante el escaneo
            print(f"Error connecting to {hostname} for port scanning: {str(exception)}")

# Bloque principal para ejecución directa del script
if __name__ == "__main__":
    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Nmap scanner async')
    parser.add_argument(
        "--host", dest="host", help="Target IP / domain", required=True
    )
    parser.add_argument(
        "--ports", dest="ports", help="Specify target port(s) separated by comma [80,8080 by default]", default="80,8080"
    )
    parsed_args = parser.parse_args()

    # Obtiene los valores de los argumentos
    port_list = parsed_args.ports.split(',')
    ip_address = parsed_args.host

    # Realiza el escaneo para cada puerto especificado
    for port in port_list:
        NmapScannerAsyncFTP().nmapScanAsync(ip_address, port)
