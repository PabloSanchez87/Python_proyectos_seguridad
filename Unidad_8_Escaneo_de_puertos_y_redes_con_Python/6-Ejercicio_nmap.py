#!/usr/bin/python3

# Importar la librería nmap e inicializar el objeto PortScanner
import nmap                       
nm = nmap.PortScanner()

# Pedir al usuario que introduzca el host que se va a escanear
host_scan = input('Host scan: ')

# Definir una lista de puertos a escanear y ejecutar el escaneo con nmap
portlist = "21,22,23,25,80,8080"  # Lista de puertos separados por comas
# Ejecutar el escaneo en el host especificado con los puertos definidos
# La opción '-n' evita la resolución de nombres DNS
nm.scan(hosts=host_scan, arguments='-n -p' + portlist)

# Mostrar el comando que nmap está ejecutando internamente
print(nm.command_line())

# Crear una lista de tuplas con los hosts encontrados y sus estados
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

# Abrir un archivo para escribir los resultados del escaneo
archivo = open('scan.txt', 'w')

# Iterar sobre los hosts encontrados, mostrando y escribiendo en el archivo su estado
for host, status in hosts_list:
    print(host, status)  # Mostrar por consola
    archivo.write(host + '\n')  # Escribir el host en el archivo

# Dividir la lista de puertos en un array y mostrar el estado de cada uno
array_portlist = portlist.split(',')  # Dividir los puertos por comas
for port in array_portlist:
    # Obtener el estado del puerto desde el escaneo realizado
    state = nm[host_scan]['tcp'][int(port)]['state']
    # Mostrar el puerto y su estado por consola
    print("Port:" + str(port) + " " + "State:" + state)
    # Escribir el puerto y su estado en el archivo
    archivo.write("Port:" + str(port) + " " + "State:" + state + '\n')

# Cerrar el archivo una vez que se hayan escrito todos los resultados
archivo.close()
