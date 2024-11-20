# Importamos la biblioteca nmap, que se utiliza para realizar escaneos de red.
import nmap

# Creamos una instancia de PortScannerYield, que permite realizar escaneos
# de forma asíncrona y devolver los resultados en tiempo real.
portScannerYield = nmap.PortScannerYield()

# Iteramos sobre los resultados de un escaneo asíncrono realizado sobre el host 'scanme.nmap.org'.
# Los puertos especificados para el escaneo son: 21, 22, 23, 25 y 80.
for scan_yield in portScannerYield.scan('scanme.nmap.org', '21,22,23,25,80'):
    # 'scan_yield' es una tupla que contiene dos elementos:
    # - scan_yield[0]: La dirección IP o el host escaneado.
    # - scan_yield[1]: Un diccionario con los resultados del escaneo.

    # Extraemos y mostramos el número de hosts que están "arriba" o accesibles.
    # Este valor se encuentra en el campo 'nmap > scanstats > uphosts'.
    print(scan_yield[1]['nmap']['scanstats']['uphosts'])

    # Verificamos si el número de hosts accesibles es igual a 1.
    if scan_yield[1]['nmap']['scanstats']['uphosts'] == "1":
        # Si es así, imprimimos el nombre del host objetivo.
        print("Host ==> " + scan_yield[0])

        # También mostramos el detalle del escaneo relacionado con el host.
        # Esta información incluye detalles sobre los puertos, servicios y estado.
        print(scan_yield[1]['scan'])
