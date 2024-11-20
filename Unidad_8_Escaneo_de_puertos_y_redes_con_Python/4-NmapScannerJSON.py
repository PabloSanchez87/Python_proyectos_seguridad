#!/usr/bin/env python3
# Especifica que este script debe ejecutarse con Python 3.

# Importa la librería nmap para realizar análisis de puertos desde Python.
import nmap

# Importa la librería json para trabajar con archivos JSON.
import json

# Define una clase para manejar el escaneo de puertos y guardar resultados en formato JSON.
class NmapScannerJSON:
    
    # Constructor de la clase.
    def __init__(self):
        # Inicializa un objeto PortScanner, que se usará para realizar escaneos.
        self.portScanner = nmap.PortScanner()
    
    # Método para realizar un escaneo y guardar los resultados en formato JSON.
    def nmapScanJSON(self, host, ports):
        try:
            # Imprime un mensaje indicando qué puertos se están escaneando en qué máquina.
            print("Comprobando puertos " + str(ports) + " en la máquina " + host)
            
            # Realiza el escaneo en el host y puertos especificados.
            self.portScanner.scan(host, ports)
            
            # Muestra el comando Nmap que se ejecutó internamente para realizar el análisis.
            print("[*] Ejecutando el comando: %s" % self.portScanner.command_line())
            
            # Imprime los resultados en formato CSV para facilitar el análisis.
            print(self.portScanner.csv())
            
            # Inicializa un diccionario para almacenar los resultados.
            results = {}
            
            # Procesa cada línea del resultado CSV (excepto la cabecera y la última línea vacía).
            for x in self.portScanner.csv().split("\n")[1:-1]:
                # Divide la línea CSV en columnas usando el separador `;`.
                splited_line = x.split(";")
                
                # Extrae información relevante de la línea procesada.
                host = splited_line[0]         # Dirección IP del host.
                dns = splited_line[1]          # Nombre DNS (si está disponible).
                protocolo = splited_line[3]    # Protocolo (TCP/UDP).
                puerto = splited_line[4]       # Número de puerto.
                estado = splited_line[6]       # Estado del puerto (abierto/cerrado/etc.).
                
                # Actualiza el diccionario de resultados con los datos extraídos.
                results.update({
                    'host': host,
                    'dns': dns,
                    'protocolo': protocolo,
                    'puerto': puerto,
                    'estado': estado
                })

            # Define el nombre del archivo JSON donde se almacenarán los resultados.
            file_info = "scan_%s.json" % host
            
            # Abre el archivo JSON en modo escritura y guarda los resultados.
            with open(file_info, "w") as file_json:
                json.dump(results, file_json)
            
            # Imprime un mensaje indicando que el archivo JSON se generó correctamente.
            print("[*] El fichero '%s' ha sido generado con los resultados del escaner" % file_info)
        
        # Captura cualquier excepción que ocurra durante el escaneo y la imprime.
        except Exception as exception:
            print("Error al conectar con " + host + " para escaneo de puertos: " + str(exception))

# Crea una instancia de la clase NmapScannerJSON.
nmapScannerJSON = NmapScannerJSON()

# Realiza un escaneo en los puertos 21, 22, 23 y 80 del host 45.33.32.156 (scanme.nmap.org).
nmapScannerJSON.nmapScanJSON("45.33.32.156", "21,22,23,80")


