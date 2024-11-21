# Importar la librería nmap para realizar escaneos con Nmap
import nmap

# Inicializar el objeto PortScannerAsync para realizar escaneos de forma asíncrona
portScannerAsync = nmap.PortScannerAsync()

# Definir una función de callback que se ejecutará cuando los resultados del escaneo estén disponibles
def callback_result(host, scan_result):
    """
    Función de callback que maneja los resultados del escaneo.

    :param host: El host que fue escaneado (nombre o dirección IP).
    :param scan_result: Los resultados del escaneo para ese host, en forma de diccionario.
    """
    print(host, scan_result)  # Imprime el host y los resultados del escaneo en la consola

# Iniciar un escaneo asíncrono
portScannerAsync.scan(
    hosts='scanme.nmap.org',  # Host que se desea escanear (en este caso, un host público de prueba)
    arguments='-sP',         # Argumentos para Nmap. '-sP' realiza un escaneo de ping para determinar si el host está activo.
    callback=callback_result  # Función de callback que se ejecutará cuando haya resultados disponibles
)

# Mientras el escaneo esté en progreso, el programa seguirá verificando el estado
while portScannerAsync.still_scanning():
    print("Scanning >>>")  # Mensaje que indica que el escaneo sigue en curso
    portScannerAsync.wait(5)  # Pausa de 5 segundos antes de volver a verificar si el escaneo terminó
