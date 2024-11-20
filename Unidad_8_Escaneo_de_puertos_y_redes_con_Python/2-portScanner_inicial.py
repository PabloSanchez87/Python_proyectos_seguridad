# Importa la librería nmap, que proporciona herramientas para interactuar con Nmap desde Python.
import nmap

# Crea una instancia del objeto PortScanner, que se utiliza para realizar análisis de puertos.
portScanner = nmap.PortScanner()

# Realiza un escaneo a la dirección 'scanme.nmap.org' en los puertos 21, 22, 23 y 80.
# Se utiliza la opción '-sV' para detectar las versiones de los servicios que están ejecutándose en esos puertos.
resultados = portScanner.scan('scanme.nmap.org', '21,22,23,80', '-sV')

# Imprime los resultados del escaneo en forma de diccionario. Este diccionario contiene información detallada 
# como puertos abiertos, servicios en ejecución y sus versiones.
print(resultados)

# Muestra la línea de comando que Nmap ejecutó internamente para realizar el escaneo.
# Esto es útil para depuración y para comprender exactamente cómo se realizó el análisis.
print(portScanner.command_line())

# Genera una representación en formato CSV de los resultados del escaneo.
# Este formato es útil para exportar los datos a hojas de cálculo o sistemas de análisis.
print(portScanner.csv())

# Lista todas las direcciones IP encontradas durante el escaneo.
# En este caso, solo debería devolver la dirección IP de 'scanme.nmap.org'.
print(portScanner.all_hosts())

# Proporciona información sobre el tipo de escaneo realizado.
# Esto incluye detalles sobre las opciones utilizadas en el escaneo.
print(portScanner.scaninfo())
