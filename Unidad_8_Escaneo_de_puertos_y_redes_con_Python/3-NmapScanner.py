#!/usr/bin/env python3
# Especifica que este script debe ejecutarse con Python 3.

# Importa la librería nmap para realizar análisis de puertos desde Python.
import nmap

# Define una clase para manejar el escaneo de puertos utilizando la librería nmap.
class NmapScanner:
    # Constructor de la clase
    def __init__(self):
        # Inicializa un objeto PortScanner, que se usará para realizar escaneos.
        self.portScanner = nmap.PortScanner()

    # Método para realizar un escaneo en un puerto específico de un host.
    def nmapScan(self, host, port):
        try:
            # Imprime un mensaje indicando qué puerto se está escaneando en qué máquina.
            print("Comprobando el puerto " + port + " en la máquina " + host)
            
            # Realiza el escaneo en el host y puerto especificados.
            self.portScanner.scan(host, port)
            
            # Muestra el comando Nmap que se ejecutó internamente para realizar el análisis.
            print("[*] Ejecutando el comando: %s" % self.portScanner.command_line())
            
            # Obtiene el estado del puerto (por ejemplo, 'open', 'closed', etc.).
            self.state = self.portScanner[host]['tcp'][int(port)]['state']
            
            # Imprime el estado del puerto (abierto, cerrado, etc.) en el host.
            print(" [+] " + host + " tcp/" + port + " " + self.state)
            
            # Imprime información completa del puerto analizado (nombre del servicio, etc.).
            print(self.portScanner[host].tcp(int(port)))
            
            # Obtiene el nombre del servicio y la versión ejecutándose en el puerto (si está disponible).
            self.server = self.portScanner[host].tcp(int(port))['product']
            self.version = self.portScanner[host].tcp(int(port))['version']
            
            # Imprime el nombre del servicio y la versión.
            print(" [+] " + self.server + " " + self.version + " tcp/" + port)

        except Exception as exception:
            # Captura cualquier excepción que ocurra durante el escaneo y la imprime.
            print("Error al conectar con " + host + " para escaneo de puertos: " + str(exception))


# Instancia un objeto de la clase NmapScanner.
NmapScanner = NmapScanner()

# Realiza un escaneo en el puerto 80 del host 45.33.32.156 (scanme.nmap.org).
NmapScanner.nmapScan("45.33.32.156", "80")
