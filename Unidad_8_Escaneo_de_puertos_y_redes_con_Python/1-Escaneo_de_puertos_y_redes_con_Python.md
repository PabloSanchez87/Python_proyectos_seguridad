# Escaneo de puertos y redes con Python

## Objetivos

### Competencia
- Conocer los módulos disponibles en Python con el objetivo de automatizar los procesos de escáner de puertos y redes.
- ALgunas de las herramientas que permiten realizar un escáner de puertos y automatizar la detección de servicios y puertos abiertos, ente las que podemos destacar `Python-nmap`.
- También usaremos `nmap` para detectar vulnerabilidades en servicios específicos gracias a los scripts de nmap.

### Resultados
- Comprener cómo detectar los puertos aberto de un sistema o segmento de red, así como realizar operaciones avanzadas para recolectar información sobre su objetivo y detectar vulnerabilidades.
- Entender la herramienta `namp` como escáner de puertos que nos permite analizar los puertos y servicios que se ejecutan en una máquina.
- Crear scripts en Python con el objetivo de optimizar y automatizar las tareas de descubrimiento y análisi de un determinado objetivo con el módulo Python-namp.
- Comprender el uso de los scripts de nmap para detectar serviciso y vulnerabilidades en servidores.
- Obtener las máquinas activas de un segmento de red.


### Contexto

`Nmap`  es un potente escáner de puertos que permite identificar puertos abiertos, cerrados o filtrados. También permite la programación de rutinas para encontrar posibles vulnerabilidades en un host determinado. 


### Objetivos

1. Dar a conocer nmap cómo escáner de puertos que nos permite analizar los puertos y servicios que se ejecutan en una máquina.
2. Dar a conocer el módulo Python-nmap que utiliza nmap por debajo y es una herramienta útil para optimizar tareas de descibrimiento y análisis de objetivos.
3. Enseñar cómo detectar los puertos abiertos de un sistema o segmentos de red, así como realizar operaciones avanzadas para recolectar información sobre su objetivo y detectar vulnerabilidades.
4. Obtener las máquinas activas de un segmento de red.

---

## Namp como herramienta de escáner de puertos

- `Namp` es una herramienta para la exploración de la red y la auditoría de seguridad.
- Permite realizar escaneados con `ping`(determinando que máquinas esstán activas), utilizando diferentes técnicas de escaneado de puertos, detección de versiones (determinando los protocolos de los servicios y las versiones de las aplicaciones que estsán escuchando en los puertos), e identificación mediante TCP/IP (identificando el SO de la máquina).
- La herramienta `nmap` se utiliza principalmente para reconocimiento y escaneo de puertos en un determinado segmento de red.
- [Página oficial Nmap](https://nmap.org/)

### Principales opciones de los comandos de nmap

- **`sT (TCP Connect Scan)`**: 

    - Es la opción que se suele utilizar para detectar si un puerto está abierto o cerrado, pero también suele ser el mecanismo más auditado y vigilado por sistemas de detección de intrusos. 
    
    - Con esta opción, un puerto se encuentra abierto si el servidor responde con un paquete que contenga la `flag ACK` al enviar un paquete con el `flag SYN`.

- **`sS (TCP Stealth Scan)`**:

    - Tipo de escaneo basado en TCP Connect Scan con la diferencia de que la conexión en el puerto indicado no se realiza de forma completa.

    - Consiste en comprobar el paquete de respuesta del obetivo con un paquete con el `flag SYN` habilitado.

    - Si el objetivo responde con un pquete que tiene el `flag RST`, entonces se puede comprobar si el puerto está abierto o cerrado.

- **`sU (UDP Scan)`**:

    - Tipo de escaneo basado en el procotolo UDP donde no se lleva a cabo un proceso de conexión, sino que simplemente se envía un paquete para determinar si el puerto está abierto.

    - Si la respuesta es otro paquete UDP, significa que el puerto está abierto.

    - En el caso de que el puerto no esté abierto se recibirá un paquete ICMP del tipo 3 (tipo inalcanzable).

- **`sA (TCP ACK Scan)`**:

    - Tipo de escaneo que permite saber si una máquina objetivo tiene algún tipo de firewall en ejecución.

    - Lo que hace este escaneo es enviar un paquete con el `flag ACK` activado y se envía a la máquina objetivo.

    - En el caso de que la máquina remota responda con un paquete que tenga la `flag RST` activada, se puede determinar que el puerno no se encuentra filtrado por ningún firewall.

    - En caso de que el no responda o lo haga con un paquete ICMP del tipo se puede determinar que hay un firewall filtrando los paquetes enviados en el puerto indicado.

- `sN (TCP Null Scan)`:

    - ipo de escaneo que envía un paquete TCP a la máquina objetivo sin ningún flag.

    - Si la máquina remota no emite ninguna respuesta, se puede determinar que el puerto está abierto.

    - Si la máquina remota devuelvee un `flag RST`, se puede determinar que el puerto está cerrado.

- **`sF (TCP FIN Scan)`**:

    - Tipo de escaneo que envía un paquete TCP con el `flag FIN` activado.

    - Si la máquina remota no emite ninguna respuesta, se puede determinar que el puerto está abierto.

    - Si la máquina remota devuelvee un `flag RST`, se puede determinar que el puerto está cerrado.

- **`sX (TCP Xmas Scan)`**:

    - Tipo de escaneo que envía un paquete TCP a la máquina objetivo con los `flags PSH, FIN y URG activados`.

    - Si la máquina remota no emite ninguna respuesta, se puede determinar que el puerto está abierto.

    - Si la máquina remota devuelvee un `flag RST`, se puede determinar que el puerto está cerrado.

    - Si en el paquete de respuesta obtenemos uno del tipo ICMP del tipo3, entonces el puerto se encuentra filtrado.
    
>[!NOTE]
> El tipo de scan por defecto puede variar en función del usuario que lo esté ejecutando, por aquello de los permisos de enviar paquetes durante el scan. La diferencia entre unos y otros  radica en el `ruido` generado, y en su capacidad de evitar ser detectados por sistemas de seguridad como pueden ser los firewalss o los sistemas de detección de intrusos.

- Si queremos crear un escáner de puertos, tendríamos que crear un hilo por cada socket que abriese una conexión en un puerto y gestionar el uso compartido de la pantalla mediante un semáforo. Con esto tendríamos un código largo y además solo haríamos un scanning simple TCP, pero no ACK, SYN-ACK, RST o FIN proporcionados por el toolkit Nmap.

### Ejercicio: Escaneo de puertos con nmap

- Realizar un escaneo en un máquina y lista los puertos con el objetivo de detectar puertos y servidores abiertos.

- Determinar los puerto abiertos y filtrados para los siguientes dominios:
    - adrformacion.com
    - python.org
    - ftp.be.debian.org 

    ```bash	
    nmap adrformacion.com
    
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-20 11:55 CET
    Nmap scan report for adrformacion.com (52.208.64.192)
    Host is up (0.052s latency).
    Other addresses for adrformacion.com (not scanned): 54.77.229.117 34.241.72.197
    rDNS record for 52.208.64.192: ec2-52-208-64-192.eu-west-1.compute.amazonaws.com
    Not shown: 998 filtered ports
    PORT    STATE SERVICE
    80/tcp  open  http
    443/tcp open  https
    ```

    ```bash		
    nmap python.org

    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-20 11:56 CET
    Nmap scan report for python.org (151.101.0.223)
    Host is up (0.015s latency).
    Other addresses for python.org (not scanned): 151.101.192.223 151.101.128.223 151.101.64.223 2a04:4e42:400::223 2a04:4e42:600::223 2a04:4e42::223 2a04:4e42:200::223
    Not shown: 998 filtered ports
    PORT    STATE SERVICE
    80/tcp  open  http
    443/tcp open  https
    ```

    ```bash		
    nmap ftp.be.debian.org

    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-20 11:57 CET
    Nmap scan report for ftp.be.debian.org (195.234.45.114)
    Host is up (0.050s latency).
    Other addresses for ftp.be.debian.org (not scanned): 2a05:7300:0:100:195:234:45:114
    rDNS record for 195.234.45.114: mirror.as35701.net
    Not shown: 995 closed ports
    PORT    STATE SERVICE
    21/tcp  open  ftp
    22/tcp  open  ssh
    80/tcp  open  http
    443/tcp open  https
    873/tcp open  rsync
    ```	

## Escaneo de puertos con `Python-nmap`

- En Python podemos hacer uso de nmap a travcés de la libería `python-nmap`, la cual nos permite manipular fácilmente los resultados de un escaneo, además, puede ser una herramienta perfecta para administradores de sistemas o consultores de seguirdad informática a la hora de automatizar procesos de penetración testing.

- `Python-nmap` es una herramienta que se utiliza dentro del ámbito de las auditorías de seguridad o pruebas de intrusión y su principal funcionalidad es descubrir qué puertos o servicios tienen en escucha un determinado host.

- [Python nmap](https://xael.org/pages/python-nmap-en.html)

- Instalación de `python-nmap`:

    ```bash
    sudo apt-get install python-pip nmap
    sudo pip install python-nmap
    ```

- Una vez instalado, podemos realizar escaneos sobre un determinado host, para ello tenemos que instanciar un objeto de la clase `PortScanner()`, así podremos acceder al método más importante `scan()`.

    - Una buena práctica para entender cómo trabaja una función, método u objeto es usar la función help() o dir() para saber las funciones/métodos disponibles en una clase u objeto.

        ```python
        >>> import nmap
        >>> portScanner = nmap.PortScanner()

        >>> dir(portScanner)
        ['_PortScanner__process', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_nmap_last_output', '_nmap_path', '_nmap_subversion_number', '_nmap_version_number', '_scan_result', 'all_hosts', 'analyse_nmap_xml_scan', 'command_line', 'csv', 'get_nmap_last_output', 'has_host', 'listscan', 'nmap_version', 'scan', 'scaninfo', 'scanstats']
        ```

- Si ejeceutamos el comando `help(PortScanner.scan)` vemos que el método `scan()` de la clase PortScanner recibe tres argumentos:

    - host: es el host que queremos escanear.
    - ports: es el rango de puertos que queremos escanear.
    - arguments: es un diccionario con los argumentos que queremos pasar al comando nmap.

        ```python
        >>> help(PortScanner.scan)
        Help on method scan in module nmap:
        
        scan(self, host, ports='1-65535', arguments=None)
            Scan host on given ports.
        ```

- Lo primero que tenemos que hacer importar la librería de nmap y crear nuestro objeto para empezar a interactuar con PortScanner().

- Lanzaremos nuestro primer escaneo con el método `scan("ip/rango", "puertos", "argumentos")`, donde solo el primer argumento es obligatorio.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/portScanner_inicial.py)

    - Resultado:
        ```bash
        {'nmap': {'command_line': 'nmap -oX - -p 21,22,23,80 -sV scanme.nmap.org', 'scaninfo': {'tcp': {'method': 'connect', 'services': '21-23,80'}}, 'scanstats': {'timestr': 'Wed Nov 20 12:15:17 2024', 'elapsed': '53.05', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'45.33.32.156': {'hostnames': [{'name': 'scanme.nmap.org', 'type': 'user'}, {'name': 'scanme.nmap.org', 'type': 'PTR'}], 'addresses': {'ipv4': '45.33.32.156'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'conn-refused'}, 'tcp': {21: {'state': 'closed', 'reason': 'conn-refused', 'name': 'ftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 'OpenSSH', 'version': '6.6.1p1 Ubuntu 2ubuntu2.13', 'extrainfo': 'Ubuntu Linux; protocol 2.0', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel'}, 23: {'state': 'closed', 'reason': 'conn-refused', 'name': 'telnet', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}}
        nmap -oX - -p 21,22,23,80 -sV scanme.nmap.org
        host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe
        45.33.32.156;scanme.nmap.org;user;tcp;21;ftp;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;21;ftp;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;user;tcp;22;ssh;open;OpenSSH;"Ubuntu Linux; protocol 2.0";syn-ack;6.6.1p1 Ubuntu 2ubuntu2.13;10;cpe:/o:linux:linux_kernel
        45.33.32.156;scanme.nmap.org;PTR;tcp;22;ssh;open;OpenSSH;"Ubuntu Linux; protocol 2.0";syn-ack;6.6.1p1 Ubuntu 2ubuntu2.13;10;cpe:/o:linux:linux_kernel
        45.33.32.156;scanme.nmap.org;user;tcp;23;telnet;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;23;telnet;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;user;tcp;80;http;open;;;syn-ack;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;80;http;open;;;syn-ack;;3;

        ['45.33.32.156']
        {'tcp': {'method': 'connect', 'services': '21-23,80'}}
        ```

    - En el script anterior está realizando un escaneo sobre el dominio scanme.nmap.org, en los puertos 21, 22, 23 y 80.

    - Lo primero que hacemos es instanciár un objeto de la clase `PortScanner()`, y a través de los métodos `scan()` y  `command_line()` para ver el comando que nmap está ejecutando por debajo.

    - Con el argumento `-sV` le estamos indicando que detecte las versiones cuando se realiza el escaneo. El resultado es un diccionario que contiene la misma información que devolvería un escaneo echo con Namp.

    - En la salida del script vemos como los puerto 22 y 80 son los que están abiert, además muestra información sobre la versión del servicio que se está ejecutando en esos puertos.

    - El método `all_host()` nos devuelve información acerca de los hosts o direcciones ip que están activos.

        ```python	
        portScanner.all_hosts()
        ['45.33.32.156']
        ```

    - Con el método scaninfo() podemos ver los servicios que han dado algún tipo de respuesta en el proceso del escaneo, así como el método de escaneo.

        ```python
        portScanner.scaninfo()
        {'tcp': {'method': 'connect', 'services': '21-23,80'}}
        ```
    
    - Si queremos visualizar de una manera fácil el resultado del escanep, disponemos de la función `csv()`, el cual nos dvolverá la información en formato CSV que lo separa por punto y coma.

        ```bash
        host;hostname;hostname_type;protocol;port;name;state;product;extrainfo;reason;version;conf;cpe
        45.33.32.156;scanme.nmap.org;user;tcp;21;ftp;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;21;ftp;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;user;tcp;22;ssh;open;OpenSSH;"Ubuntu Linux; protocol 2.0";syn-ack;6.6.1p1 Ubuntu 2ubuntu2.13;10;cpe:/o:linux:linux_kernel
        45.33.32.156;scanme.nmap.org;PTR;tcp;22;ssh;open;OpenSSH;"Ubuntu Linux; protocol 2.0";syn-ack;6.6.1p1 Ubuntu 2ubuntu2.13;10;cpe:/o:linux:linux_kernel
        45.33.32.156;scanme.nmap.org;user;tcp;23;telnet;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;23;telnet;closed;;;conn-refused;;3;
        45.33.32.156;scanme.nmap.org;user;tcp;80;http;open;;;syn-ack;;3;
        45.33.32.156;scanme.nmap.org;PTR;tcp;80;http;open;;;syn-ack;;3;
        ```


## `Escaneo síncrono`

- En el siguiente script  vamos a implementar una clase llamada `NmapScanner`  que permite realizar un ecaneo de una dirección IP y un puerto específico que se pasan por parámetro a la función `nmapScan(ip,port)` de la clase NampScanner.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/3-NmapScanner.py)

    - Resultado:

        ```bash
        Comprobando el puerto 80 en la máquina 45.33.32.156
        [*] Ejecutando el comando: nmap -oX - -p 80 -sV 45.33.32.156
        [+] 45.33.32.156 tcp/80 open
        {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.7', 'extrainfo': '(Ubuntu)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.7'}
        [+] Apache httpd 2.4.7 tcp/80
        ```

        - Vemos como ha detectado que el puerto 80 está abierto en la dirección IP 45.33.32.156., mostrando información adicional sobre el comando ejecutado y la versión del Sistema Operativo.

### Guardar resultado del escaneo en un archivo JSON

- Además de realizar el escaneo de puertos y devolver el resultado por consola, podríamos generar un documento JSON donde almacenar el resultado con los puertos abierto para un determinado host o direcciones IP.

- EN este caso utilizamos la funcion `csv()` que devuelve el resultado del escaneo en un formato fácil de tratar para recoger la información en un archivo JSON.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/4-NmapScannerJSON.py)

    - Resultado:
        ```json
        {
            "host": "45.33.32.156",
            "dns": "scanme.nmap.org",
            "protocolo": "tcp",
            "puerto": "80",
            "estado": "filtered"
        }
        ```

    - Al final del script vemos cómo se instancia un objeto de la clase NmapScannerJSON y se realiza la llamada al método nmapScanJSON() pasando por parámetro la ip y la lista de puertos que queremos analizar.

### Usando `PortScannerYield`

- Si necesitamos mostrar los resultados conforme los vayamos obteniendo podemos utilozar su clase `PortScannerYield` que nos permite obtener los resultados de manera iterativa observando el progreso del escaneo.

- Esta clase es útil cuando tenemos que escaner un segmento de red y necesitamos hacer operaciones cn cada host que vayamos descubriendo.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/5-PortScannerYield.py)

    - Resultado:
        ```bash
        1
        Host ==> 45.33.32.156
        {'45.33.32.156': {'hostnames': [{'name': 'scanme.nmap.org', 'type': 'PTR'}], 'addresses': {'ipv4': '45.33.32.156'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'conn-refused'}, 'tcp': {21: {'state': 'closed', 'reason': 'conn-refused', 'name': 'ftp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 22: {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 'OpenSSH', 'version': '6.6.1p1 Ubuntu 2ubuntu2.13', 'extrainfo': 'Ubuntu Linux; protocol 2.0', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel'}, 23: {'state': 'closed', 'reason': 'conn-refused', 'name': 'telnet', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 25: {'state': 'closed', 'reason': 'conn-refused', 'name': 'smtp', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 80: {'state': 'filtered', 'reason': 'no-response', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}
        ```

- Tambien podríamos realizar estos escaneos con nmap desde python y también tendríamos la opción de realizarlos los módulos `os` y `subprocess`.

### Usando `nmap` con el módulo `os`

- Para usar nmap con el módulo `os` podemos utilizar el comando `os.system()` que permite ejecutar comandos en la terminal.

    ```python
    import os

    nmap_command="nmap -sT 127.0.0.1"

    os.system(nmap_command)
    ```

    - Resultado (ejemplo):
        ```bash
        Nmap scan report for 127.0.0.1
        Host is up (0.00012s latency).
        Not shown: 998 closed ports
        PORT     STATE SERVICE
        22/tcp   open  ssh
        80/tcp   open  http
        ```

### Usando `nmap` con el módulo `subprocess`

- Con el módulo `subprocess` podemos proceder de la misma forma que hacíamos con el módulo `os`, pero en este caso podemos trabajar con las alidas STDOUT y STDERR de la consola, cosa que nos facilita el posterior tratamiento del resultado.

    ```python
    from subprocess import Popen, PIPE

    process = Popen(['nmap','-O','127.0.0.1'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode())
    ```

    - Necesitamos permisos de administrador.

    - Resultado:
        ```bash
        Nmap scan report for localhost (127.0.0.1)
        Host is up (0.000042s latency).
        Not shown: 998 closed ports
        PORT STATE SERVICE
        22/tcp open ssh
        631/tcp open ipp
        Device type: general purpose
        Running: Linux 2.6.X
        OS CPE: cpe:/o:linux:linux_kernel:2.6.32
        OS details: Linux 2.6.32
        Network Distance: 0 hops
        ```

### Ejercicio: Escaneo con `python-nmap` dada una lista de puertos y una dirección IP.

- Realizar un escaneo con nmap con las siguientes condiciones en forma de argumentos:
    - Puertos a escanear: 21,22,23,80,8080
    - -n para no hacer resolución DNS
    - Una vez obteniedos, guardarlos en un fichero scan.txt
    - IP: 45.33.32.156 que corresponde a scanme.nmap.org

- [Código del ejercicio](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/6-Ejercicio_nmap.py
)

    - Resultado:
        ```
        45.33.32.156
        Port:21 State:closed
        Port:22 State:open
        Port:23 State:closed
        Port:25 State:closed
        Port:80 State:filtered
        Port:8080 State:closed
        ```


## `Escaneo asíncrono`

- Podemos realizar escaneos asíncronos haciendo uso de la clase `PortScannerAsync()`.

- En este caso, al realizar el escaneo le podemos indicar un parámetro adicional de función callback donde definimos la función de retorno, que se ejecutaría al final del proceso.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/7-PortScannerAsync.py)

    - Resultado:
        ```bash
        Scanning >>>
        5.33.32.156 {'nmap': {'command_line': 'nmap -oX - -sP 45.33.32.156', 'scaninfo': {}, 'scanstats': {'timestr': 'Thu Nov 21 10:09:35 2024', 'elapsed': '0.53', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'45.33.32.156': {'hostnames': [{'name': 'scanme.nmap.org', 'type': 'PTR'}], 'addresses': {'ipv4': '45.33.32.156'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'conn-refused'}}}}
        ```

    - De esta forma, podemos definir una función de callback que se ejecute cada vez que nmap disponga de un resultado para la máquina que estemos analizando. 

### Escaneo asíncrono con `python-nmap`

- En el siguiente ejemplo lo que hacemos es implementar una clase que realiza el escaneo asíncrono a partir de la información introducida por el usuario en forma de argumento en el script.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/8-NmapScannerAsync.py.py)

    - Resultado: `python3 8-NmapScannerAsync.py --host scanme.nmap.org` 
        ```bash
        Checking port 80 ..........
        Scanning >>>
        Scanning >>>
        Scanning >>>
        Command line:nmap -oX - -A -sV -p80 45.33.32.156
        Port 80 --> {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.7', 'extrainfo': '(Ubuntu)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.7', 'script': {'http-server-header': 'Apache/2.4.7 (Ubuntu)', 'http-title': 'Go ahead and ScanMe!'}}
        Checking port 8080 ..........
        Scanning >>>
        Command line:nmap -oX - -A -sV -p8080 45.33.32.156
        Port 8080 --> {'state': 'closed', 'reason': 'conn-refused', 'name': 'http-proxy', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}
        ```	

    - Si lo ejecutamos con los parámetros --host y --ports podemos ver como realiza el escaneo en los puertos especificados.
        - La función callbackResult() será la encargada de mostrar el estado del escaneo para cada puerto.

    - Resultado: `python3 8-NmapScannerAsync.py --host scanme.nmap.org --ports 80,443,22,8080`

        ```bash
        Checking port 80 ..........
        Scanning >>>
        Scanning >>>
        Scanning >>>
        Command line:nmap -oX - -A -sV -p80 45.33.32.156
        Port 80 --> {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.7', 'extrainfo': '(Ubuntu)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.7', 'script': {'http-server-header': 'Apache/2.4.7 (Ubuntu)', 'http-title': 'Go ahead and ScanMe!'}}
        Checking port 443 ..........
        Scanning >>>
        Command line:nmap -oX - -A -sV -p443 45.33.32.156
        Port 443 --> {'state': 'closed', 'reason': 'conn-refused', 'name': 'https', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}
        Checking port 22 ..........
        Scanning >>>
        Scanning >>>
        Command line:nmap -oX - -A -sV -p22 45.33.32.156
        Port 22 --> {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh', 'product': 'OpenSSH', 'version': '6.6.1p1 Ubuntu 2ubuntu2.13', 'extrainfo': 'Ubuntu Linux; protocol 2.0', 'conf': '10', 'cpe': 'cpe:/o:linux:linux_kernel', 'script': {'ssh-hostkey': '\n  1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)\n  2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)\n  256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)\n  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)'}}
        Checking port 8080 ..........
        Scanning >>>
        Command line:nmap -oX - -A -sV -p8080 45.33.32.156
        Port 8080 --> {'state': 'closed', 'reason': 'conn-refused', 'name': 'http-proxy', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}
        ```

## Ejecutar script de nmap para detectar servicios y vulnerabilidades

- `Nmap` es una herramienta muy conocida en el mundo de la seguridad informática por su funcionalidad de escaneo de redes, puertos y servicios.

- Una de las características más interesantes que tiene nmap es la posibilidad de ejecutar scripts que siguen la especificación `NSE(Nmap Scripting Engine)`

- `NSE` es una herramienta que permite extender los tipos de escaneos que se pueden realizar e incluso realizar tareas de detección de vulnerabilidades en los servicios.

- De esta forma, a parte de detectar si un determinado puerto está abierto o cerrado, también podemos ejecutar turinas más compleajas que permiten filtrar información sobre un determinado objetivo.

- Actualmente incorpora el uso de scripts para comprobar algunas de las vulnerabilidades más conocidas. Estos scripts están ordenados por categorías de la siguiente manera:

    - `Auth:` scripts disponibles de autenticación.
    - `Default:` ejecuta los scripts básicos por defecto.
    - `Discovery:` scripts disponibles para recuperar información sobre el objetivo.
    - `External:` script que contactan con fuentes externas.
    - `Intrusive:` scripts que son considerados intrusivos por el objetivo.
    - `Malware:` scripts que comprueban la presencia de conexiones abiertas por códigos maliciosos o backdoors (puertas traseras).
    - `Safe:` ejecuta scripts que no son considerados intrusivos.
    - `Vuln:` scripts que comprueban vulnerabilidades más conocidas y comunmente explotadas.
    - `All:` ejecuta absolitamente todos los scritps con extension NSE disponibles.

- Por lo general, el motor de scipts de NMAP puede ejecutar diferentes funcionalidades entre las que podemos destacar:

    - `Descubrumiento de redes`: Es la función básica de Nmap. Los ejemplos incluyen encontrar la información whois del nombre de dominio destino, encontrar puertos abiertos, consultas SNMP y enumerar los recursos y servicios NFS / SMB / RPC disponibles.

    - `Detección de vulnerabilidades`: Cuando se descubre una nueva vulnerabilidad, sería impotante escanear la red para identificar los sistemas vulnerables antes que los atacantes los encuentren. En este aspecto, NSE nos podría ayudar a realizar comprobaciones de vulnerabilidades que podemos encontrar en los diferentes servicios que exponen los servidores.

- Para detectar posibles vulnerabilidades en los servicios de los puertos que están abiertos podemos hacer usp de los scripts de namp que están disponibles cuando se instala el módulo.

    - En el caso de distribuciones basadas en Debian:
        - /usr/share/nmap/scripts

- Los scrips permiten la programación de rutinas para encontrar posibles vulnerabilidades de determinado host.

- [Scripts de nmap](https://nmap.org/nsedoc/scripts/)

### Ejecución scripts de nmap

- Hay una gran cantidad de scripts para cada tipo de servicio del cual queremos concocer más.

- Hay incluso algunos que permiten realizar ataques de diccionario o fuerza bruta y explotar determinadas vulnerabilidades en algunos de los servicios y puertos que exponen las máquinas.

- Para ejecutar estos scripts es necesario pasar la opción `--script` dentro del comando nmap.

- La sintaxis para ejecutar scripts es la siguiente:

    ```bash
    nmap --script <script> <host>
    nmap --script <categoria>/<script> <host>
    ```

    - Ejemplo:
        ```bash
        nmap --script default scanme.nmap.org

        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-21 10:56 CET
        Nmap scan report for scanme.nmap.org (45.33.32.156)
        Host is up (0.19s latency).
        Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
        Not shown: 996 closed ports
        PORT      STATE SERVICE
        22/tcp    open  ssh
        | ssh-hostkey: 
        |   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
        |   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
        |   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
        |_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
        80/tcp    open  http
        |_http-title: Go ahead and ScanMe!
        9929/tcp  open  nping-echo
        31337/tcp open  Elite

        Nmap done: 1 IP address (1 host up) scanned in 23.94 seconds
        ```

#### Ejemplo:

- Si quisieras ejecutar todos los scripts de la categoria `discovery` podríamos ejecutar el siguiente comando:

    ```bash
    nmap --script discovery scanme.nmap.org
    ```

#### Ejemplo: Lanzar script obtener cabeceras HTTP

- Con la opción `--script-help` podríamos ver una descripción de un script específico.

- Ejemplo:

    ```bash
    nmap --script-help http-headers
    ```

    - Resultado:
        ```bash
        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-21 10:59 CET

        http-headers
        Categories: discovery safe
        https://nmap.org/nsedoc/scripts/http-headers.html
        Performs a HEAD request for the root folder ("/") of a web server and displays the HTTP headers returned.
        ```

- Si queremos ejecutar el script `http-headers` podemos hacerlo de la siguiente manera, obteniendo las **cabeceras HTTP configuradas en el servidor web**.

    ```bash
    nmap --script http-headers scanme.nmap.org
    ```

    - Resultado:
        ```bash
        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-21 11:00 CET
        Nmap scan report for scanme.nmap.org (45.33.32.156)
        Host is up (0.19s latency).
        Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
        Not shown: 996 closed ports
        PORT      STATE SERVICE
        22/tcp    open  ssh
        80/tcp    open  http
        | http-headers: 
        |   Date: Thu, 21 Nov 2024 10:00:50 GMT
        |   Server: Apache/2.4.7 (Ubuntu)
        |   Accept-Ranges: bytes
        |   Vary: Accept-Encoding
        |   Connection: close
        |   Content-Type: text/html
        |   
        |_  (Request type: HEAD)
        9929/tcp  open  nping-echo
        31337/tcp open  Elite

        Nmap done: 1 IP address (1 host up) scanned in 12.78 seconds
        ```

### Obtener subdominios con script de nmap

- Los subdominios normalmente se utilizan para alojar sitios web adicionales para un subconjunto específico de usuarios.

- El script `dns-brute` que podemos encontrar dentro los scripts de Nmap permite obtener subdominios y las direcciones IP asociadas a ellos.

    - [Script dns-brute](https://nmap.org/nsedoc/scripts/dns-brute.html)

    - Ejemplo:
        ```bash
        nmap -p 80,443 --script dns-brute scanme.nmap.org

        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-21 11:03 CET
        Nmap scan report for scanme.nmap.org (45.33.32.156)
        Host is up (0.18s latency).
        Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

        PORT    STATE  SERVICE
        80/tcp  open   http
        443/tcp closed https

        Host script results:
        | dns-brute: 
        |   DNS Brute-force hostnames: 
        |     chat.nmap.org - 45.33.32.156
        |     chat.nmap.org - 2600:3c01::f03c:91ff:fe18:bb2f
        |     *AAAA: 2600:3c01:e000:3e6::6d4e:7061
        |_    *A: 50.116.1.184

        Nmap done: 1 IP address (1 host up) scanned in 6.74 seconds
        ```
    
    - En ese punto, un pentester o analista de seguridad podría utilizar esta información para analizar de forma recursiva los diferentes subdominios encontrados.
  
### Lanzar scripts para un determinado servicio
        
- Podríamos ejecutar los scripts correspondientes al servicio ssh para el caso de que el puerto 22 esté abierto.

- De esta forma estamos ejecutando todos los scripts con nombre que comiencen por ssh:

    ```bash
    nmap --script ssh-* <ip_domain>
    ```

- Los scripts que podríamos utilizar para testear el servicio ssh serían los siguientes localizados dentro del directorio de scripts de nmap:

    ```
    /usr/share/nmap/scripts/ssh-brute.nse
    /usr/share/nmap/scripts/ssh-auth-methods.nse
    /usr/share/nmap/scripts/ssh-scan.nse
    /usr/share/nmap/scripts/ssh2-enum-algos.nse
    /usr/share/nmap/scripts/ssh-hostkey.nse
    /usr/share/nmap/scripts/ssh-publickey-acceptance.nse
    /usr/share/nmap/scripts/ssh2-missing-host-key.nse
    /usr/share/nmap/scripts/sshv1.nse
    ```

- Ejemplo de ejecución del script `ssh-hostkey` en el puerto 22 que obtiene información de la clave pública del servidor:

    ```bash
    nmap -sV --script ssh-hostkey scanme.nmap.org

    - Resultado:
        ```bash
        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-22 09:26 CET
        Nmap scan report for scanme.nmap.org (45.33.32.156)
        Host is up (0.19s latency).
        Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f
        Not shown: 996 closed ports
        PORT      STATE SERVICE    VERSION
        22/tcp    open  ssh        OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
        | ssh-hostkey: 
        |   1024 ac:00:a0:1a:82:ff:cc:55:99:dc:67:2b:34:97:6b:75 (DSA)
        |   2048 20:3d:2d:44:62:2a:b0:5a:9d:b5:b3:05:14:c2:a6:b2 (RSA)
        |   256 96:02:bb:5e:57:54:1c:4e:45:2f:56:4c:4a:24:b2:57 (ECDSA)
        |_  256 33:fa:91:0f:e0:e1:7b:1f:6d:05:a2:b0:f1:54:41:56 (ED25519)
        80/tcp    open  http       Apache httpd 2.4.7 ((Ubuntu))
        |_http-server-header: Apache/2.4.7 (Ubuntu)
        9929/tcp  open  nping-echo Nping echo
        31337/tcp open  tcpwrapped
        Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

        Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
        Nmap done: 1 IP address (1 host up) scanned in 25.80 seconds

        ```

    - Al pasarle el parámetro `-sV` le estamos indicando que también muestre información relacionada con la versión del SO.

- También podríamos obtener más información acerca de los **algoritmos de cifrado soportados por el servidor usando el script ssh2-enum-algos** sobre el puerto:

    ```bash
    nmap -sV -p22 --script ssh2-enum-algos scanme.nmap.org
    ```
    
    - Resultado:
        ```bash
        Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-22 09:31 CET
        Nmap scan report for scanme.nmap.org (45.33.32.156)
        Host is up (0.19s latency).
        Other addresses for scanme.nmap.org (not scanned): 2600:3c01::f03c:91ff:fe18:bb2f

        PORT   STATE SERVICE VERSION
        22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
        | ssh2-enum-algos: 
        |   kex_algorithms: (8)
        |       curve25519-sha256@libssh.org
        |       ecdh-sha2-nistp256
        |       ecdh-sha2-nistp384
        |       ecdh-sha2-nistp521
        |       diffie-hellman-group-exchange-sha256
        |       diffie-hellman-group-exchange-sha1
        |       diffie-hellman-group14-sha1
        |       diffie-hellman-group1-sha1
        |   server_host_key_algorithms: (4)
        |       ssh-rsa
        |       ssh-dss
        |       ecdsa-sha2-nistp256
        |       ssh-ed25519
        |   encryption_algorithms: (16)
        |       aes128-ctr
        |       aes192-ctr
        |       aes256-ctr
        |       arcfour256
        |       arcfour128
        |       aes128-gcm@openssh.com
        |       aes256-gcm@openssh.com
        |       chacha20-poly1305@openssh.com
        |       aes128-cbc
        |       3des-cbc
        |       blowfish-cbc
        |       cast128-cbc
        |       aes192-cbc
        |       aes256-cbc
        |       arcfour
        |       rijndael-cbc@lysator.liu.se
        |   mac_algorithms: (19)
        |       hmac-md5-etm@openssh.com
        |       hmac-sha1-etm@openssh.com
        |       umac-64-etm@openssh.com
        |       umac-128-etm@openssh.com
        |       hmac-sha2-256-etm@openssh.com
        |       hmac-sha2-512-etm@openssh.com
        |       hmac-ripemd160-etm@openssh.com
        |       hmac-sha1-96-etm@openssh.com
        |       hmac-md5-96-etm@openssh.com
        |       hmac-md5
        |       hmac-sha1
        |       umac-64@openssh.com
        |       umac-128@openssh.com
        |       hmac-sha2-256
        |       hmac-sha2-512
        |       hmac-ripemd160
        |       hmac-ripemd160@openssh.com
        |       hmac-sha1-96
        |       hmac-md5-96
        |   compression_algorithms: (2)
        |       none
        |_      zlib@openssh.com
        Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

        Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
        Nmap done: 1 IP address (1 host up) scanned in 1.63 seconds
        ```	

### Analizar el servicio FTP con Scripts de Nmap

- Nmap proporciona una serie de scripts que podríamos utilizar para analizar posibles vulnerabilidades que tenga abierto el puerto 21.

- Por ejemplo, el script `ftp-anon`, si lo ejecutamos sobre la máquina objetivo en el puerto 21 podemos saber si el servicio FTP permite la autenticación sin tener que introducir un nombre de usuario y contraseña.

- Podríamos ejecutar dicho script para comprobar si el servidor FTP que estamos analizando soporta autenticación sin usuario y contraseña.

    ```bash
    nmap -sV -p21 --script ftp-anon ftp.be.debian.org
    ```

    - Resultado:
        ```bash
        Nmap scan report for ftp.be.debian.org (195.234.45.114)
        Host is up (0.046s latency).
        Other addresses for ftp.be.debian.org (not scanned): 2a05:7300:0:100:195:234:45:114
        rDNS record for 195.234.45.114: mirror.as35701.net

        PORT   STATE SERVICE VERSION
        21/tcp open  ftp     ProFTPD
        | ftp-anon: Anonymous FTP login allowed (FTP code 230)
        | drwxr-xr-x   9 ftp      ftp          4096 Nov 22 08:36 debian
        | drwxr-xr-x   5 ftp      ftp           105 Nov 10 06:39 debian-cd
        | drwxr-xr-x   7 ftp      ftp          4096 Nov 21 23:27 debian-security
        | drwxr-xr-x   5 ftp      ftp          4096 Oct 13  2006 ftp.irc.org
        | -rw-r--r--   1 ftp      ftp           432 Jul  9  2021 HEADER.html
        | drwxr-xr-x   5 ftp      ftp          4096 Nov 22 08:23 mint
        | drwxr-xr-x   5 ftp      ftp            49 Nov 30  2015 mint-iso
        | lrwxrwxrwx   1 ftp      ftp            33 Apr 29  2021 pub -> /var/www/html/www.kernel.org/pub/
        | drwxr-xr-x   7 ftp      ftp          4096 Nov 22 06:58 ubuntu
        | drwxr-xr-x  36 ftp      ftp          4096 Nov 22 05:47 ubuntu-cdimage
        | drwxr-xr-x  30 ftp      ftp          4096 Nov 22 01:18 ubuntu-cloudimages
        | drwxr-xr-x   7 ftp      ftp          4096 Nov 22 07:17 ubuntu-ports
        | drwxr-xr-x  15 ftp      ftp          4096 Nov 22 02:24 ubuntu-releases
        | drwxr-xr-x  24 ftp      ftp           291 Nov 22 08:01 video.fosdem.org
        | -rw-r--r--   1 ftp      ftp           390 Jul  9  2021 welcome.msg
        |_drwxr-xr-x   4 ftp      ftp          4096 Jun 14  2023 www.kernel.org

        Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
        Nmap done: 1 IP address (1 host up) scanned in 12.48 seconds
        ```

#### Ejercicio: Escaneo con python-nmap con el objetivo de lanzar diferentes scripts de nmap y detectar servicios vulnerables.

- [Código del ejercicio](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/9-EscaneoDePuertosPython.py)

- Ejecución del script:

    ```bash
    python3 9-EscaneoDePuertosPython.py --host 195.234.45.114 --ports 21
    ```

    - Resultado:
        ```bash
        Checking port 21 ..........
        [+] 195.234.45.114 tcp/21 open
        Checking FTP port with Nmap scripts...
        Checking ftp-anon.nse .....
        Scanning >>>
        Scanning >>>
        Command line: nmap -oX - -A -sV -p21 --script ftp-anon.nse 195.234.45.114
        Script ftp-anon --> Anonymous FTP login allowed (FTP code 230)
        drwxr-xr-x   9 ftp      ftp          4096 Nov 22 08:36 debian
        drwxr-xr-x   5 ftp      ftp           105 Nov 10 06:39 debian-cd
        drwxr-xr-x   7 ftp      ftp          4096 Nov 21 23:27 debian-security
        drwxr-xr-x   5 ftp      ftp          4096 Oct 13  2006 ftp.irc.org
        -rw-r--r--   1 ftp      ftp           432 Jul  9  2021 HEADER.html
        drwxr-xr-x   5 ftp      ftp          4096 Nov 22 08:23 mint
        drwxr-xr-x   5 ftp      ftp            49 Nov 30  2015 mint-iso
        lrwxrwxrwx   1 ftp      ftp            33 Apr 29  2021 pub -> /var/www/html/www.kernel.org/pub/
        drwxr-xr-x   7 ftp      ftp          4096 Nov 22 06:58 ubuntu
        drwxr-xr-x  36 ftp      ftp          4096 Nov 22 05:47 ubuntu-cdimage
        drwxr-xr-x  30 ftp      ftp          4096 Nov 22 01:18 ubuntu-cloudimages
        drwxr-xr-x   7 ftp      ftp          4096 Nov 22 07:17 ubuntu-ports
        drwxr-xr-x  15 ftp      ftp          4096 Nov 22 02:24 ubuntu-releases
        drwxr-xr-x  24 ftp      ftp           291 Nov 22 08:01 video.fosdem.org
        -rw-r--r--   1 ftp      ftp           390 Jul  9  2021 welcome.msg
        drwxr-xr-x   4 ftp      ftp          4096 Jun 14  2023 www.kernel.org
        Checking ftp-bounce.nse .....
        Scanning >>>
        Scanning >>>
        Checking ftp-libopie.nse .....
        Scanning >>>
        Scanning >>>
        Checking ftp-proftpd-backdoor.nse .....
        Scanning >>>
        Scanning >>>
        Checking ftp-vsftpd-backdoor.nse .....
        Scanning >>>
        Scanning >>>     
        ```   


## Obtener las máquinas acticas de un segmento de red

- `ICMP` se trata de un protocolo muy útil para diagnóstico de errores en la capa de red y se utiliza en herramientas tales como `TRACEROUTE` para el análisis del tráfico de un paquete por los diferentes routers por los que pasa.

- El protocolo `ICMP` es un protocolo de mensajes que permite saber si una máquina determinada está disponible o no. 

- Para ello deine una lista de mensajes de control para diferentes propósitos, en el caso de comando PING se utilizan los mensajes `Echo Request` y `Echo Reply`.

### Ejecutar comando ping en Python

- El comando `ping` utiliza un mensaje `ICMP` del tipo `Echo Request` para consultar si una máquina se encuentra activa y en el caso de que dicha máquina conteste con un `ICMP Echo Reply` dentro del tiempo fijado antes de que se obtenga el timeoyt, se entiende que la máquina está activa.

- Si se obtiene un timeout durante la petición de ping se entiende que la máquina está caida o bien existe algún mecanismo de protección como un proxy que esté filtrando este tipo de mensajes.

- En este caso, utilizamos el módulo `subprocess` que permite ejecutar el comando ping propio del sistema operativo.

- [Código de ejemplo](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/10-ComandoPingPython.py)

- Resultado:
    ```bash
    Scanning 195.234.45.114 
    b'PING 195.234.45.114 (195.234.45.114) 56(84) bytes of data.\n64 bytes from 195.234.45.114: icmp_seq=1 ttl=50 time=45.2 ms\n\n--- 195.234.45.114 ping statistics ---\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\nrtt min/avg/max/mdev = 45.166/45.166/45.166/0.000 ms\n'
    La dirección IP 195.234.45.114 está activa!
    ```

    ```bash
    Scanning 33.22.11.00 
    b'PING 33.22.11.00 (33.22.11.0) 56(84) bytes of data.\n\n--- 33.22.11.00 ping statistics ---\n1 packets transmitted, 0 received, 100% packet loss, time 0ms\n\n'
    La dirección IP 33.22.11.00 no está activa!
    ```

### Ejercicio: Utilizar el comando ping para determinar las máquinas acticas en un segmento de red.

- [Código del ejercicio](/Unidad_8_Escaneo_de_puertos_y_redes_con_Python/11-Ejercicio_comando_ping_segmento_red.py)

    ```bash
    python3 11-Ejercicio_comando_ping_segmento_red.py --network 192.168.1 --machines 3

    b'PING 192.168.1.0 (192.168.1.0) 56(84) bytes of data.\nFrom 192.168.1.36 icmp_seq=1 Destination Host Unreachable\n\n--- 192.168.1.0 ping statistics ---\n1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms\n\n'
    La dirección IP 192.168.1.0 no está activa!
    Scanning 192.168.1.1 
    b'PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.\n64 bytes from 192.168.1.1: icmp_seq=1 ttl=63 time=2.17 ms\n\n--- 192.168.1.1 ping statistics ---\n1 packets transmitted, 1 received, 0% packet loss, time 0ms\nrtt min/avg/max/mdev = 2.174/2.174/2.174/0.000 ms\n'
    La dirección IP 192.168.1.1 está activa!
    Scanning 192.168.1.2 
    b'PING 192.168.1.2 (192.168.1.2) 56(84) bytes of data.\nFrom 192.168.1.36 icmp_seq=1 Destination Host Unreachable\n\n--- 192.168.1.2 ping statistics ---\n1 packets transmitted, 0 received, +1 errors, 100% packet loss, time 0ms\n\n'
    La dirección IP 192.168.1.2 no está activa!
    ```

    ```bash
    python3 11-Ejercicio_comando_ping_segmento_red.py --network 192.168.18 --machines 3

    Scanning 192.168.18.0 
    b'PING 192.168.18.0 (192.168.18.0) 56(84) bytes of data.\n\n--- 192.168.18.0 ping statistics ---\n1 packets transmitted, 0 received, 100% packet loss, time 0ms\n\n'
    La dirección IP 192.168.18.0 está activa!
    Scanning 192.168.18.1 
    b'PING 192.168.18.1 (192.168.18.1) 56(84) bytes of data.\n\n--- 192.168.18.1 ping statistics ---\n1 packets transmitted, 0 received, 100% packet loss, time 0ms\n\n'
    La dirección IP 192.168.18.1 está activa!
    Scanning 192.168.18.2 
    b'PING 192.168.18.2 (192.168.18.2) 56(84) bytes of data.\n\n--- 192.168.18.2 ping statistics ---\n1 packets transmitted, 0 received, 100% packet loss, time 0ms\n\n'
    La dirección IP 192.168.18.2 está activa!
    ```

## Resumen

- **Nmap** como herramienta para obtener los **puertos abiertos de una determinada máquina** con el objetivo de realizar auditorías de seguridad.

- Instalar y utilizar el módulo **python-nmap** con el objetivo de tener un mayor control sobre los resultados de escaneo sobre un servidor.

- Utilizar la clase **PortScanner()** que contiene el método **scan()**, el cual permite lanzar un escaneo de un servidor para una determinada lista de puertos.

- Lanzar el proceso de escaneo con el método **scan('ip/rango', 'puertos', 'argumentos')**, donde solo el primer parámetro es obligatorio y los demás son opcionales.

- A través del método **command_line()** podemos ver el **comando que Nmap está ejecutando** por debajo.

- El método **all_hosts()** nos devuelve información acerca de los **hosts o direcciones IP que están activos**.

- Con el método **scaninfo()** podemos ver los servicios que han dado algún tipo de respuesta en el proceso de escaneo, así como el método de escaneo.

- Utilizar la función **csv()** con el objetivo de **obtener el resultado del escaneo en un formato fácil** de tratar para recoger la información que necesitemos.

- Utilizar la clase **PortScannerYield**, con la cual podemos ir obteniendo el progreso de nuestro escaneo.

- Utilizar el comando Nmap con el módulo **os** (operating system) con la llamada **os.system(comando_nmap)**.

- Ejecutar el comando Nmap con el módulo **subprocess** con la llamada **Popen(['nmap', '-O', 'direccion_ip'], stdin=PIPE, stdout=PIPE, stderr=PIPE)**.

- **Realizar escaneos asíncronos** utilizando la clase **PortScannerAsync()**. Además, podemos definir una **función de callback** que se ejecute cada vez que Nmap disponga de un resultado para la máquina que estemos analizando.

- Utilizar **NSE (Nmap Scripting Engine)** como herramienta que permite extender los tipos de escaneos que se pueden realizar e incluso realizar tareas de **detección de vulnerabilidades en los servicios**.

- Lanzar los scripts de Nmap localizados en la ruta **/usr/share/nmap/scripts** utilizando el comando:
  ```
  $ nmap --script (categoría) (target)
  ```

- Lanzar los scripts de Nmap para un determinado objetivo utilizando el comando:
  ```
  $ nmap --script "ssh-*" <ip_dominio>
  ```

- **Analizar posibles vulnerabilidades sobre un servidor FTP** utilizando los scripts de Nmap relacionados con el servicio FTP. Por ejemplo, podemos comprobar si un servidor FTP permite el acceso anónimo con el comando:
  ```
  $ nmap -sV -p21 --script ftp-anon <dominio>
  ```

- **Obtener las máquinas activas** de un segmento de red utilizando el módulo **subprocess** ejecutando el comando **ping** para determinar si una máquina está activa, utilizando el método:
  ```
  Popen(['ping', direccion_ip], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  ```



### FAQ

- `¿Para qué sirve nmap?`

    Nmap es una herramienta para la exploración de la red y la auditoría de seguridad. Permite realizar escaneados con ping (determinando que máquinas están activas), muchas técnicas de escaneado de puertos, detección de versiones (determinando los protocolos de los servicios y las versiones de las aplicaciones que están escuchando en los puertos), e identificación mediante TCP/IP (identificando el sistema operativo de la máquina o el dispositivo)

### Enlaces de interés

- [Nmap](https://nmap.org/)

### Bibliografía

**Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Security Scanning**


    Nmap Network Scanning is the official guide to the Nmap Security Scanner, a free and open source utility used by millions of people for network discovery, administration, and security auditing. From explaining port scanning basics for novices to detailing low-level packet crafting methods used by advanced hackers, this book by Nmap's original author suits all levels of security and networking professionals. The reference guide documents every Nmap feature and option, while the remainder demonstrates how to apply them to quickly solve real-world tasks. Examples and diagrams show actual communication on the wire. Topics include subverting firewalls and intrusion detection systems, optimizing Nmap performance, and automating common networking tasks with the Nmap Scripting Engine. Visit http://nmap.org/book for more information and sample chapters.

### Glosario

- `ICMP (Internet Control Message Protocol)`
    
    Este protocolo se emplea para el manejo de eventos como detección de errores en la red, detección de nodos o enrutadores no operativos, congestión en la red, etc., así como también para mensajes de control como “echo request”. Un ejemplo típico del uso de este protocolo es la aplicación PING.

- `Nmap (Network Mapper)`
    
    Es un escáner de puertos de la misma manera que el clásico comando netstat, con el cual podremos comprobar los puertos abiertos de un determinado equipo. Nmap sirve para determinar la accesibilidad del equipo, pero sin configurar el cortafuegos.
- `Ping`
    
    Comando que permite mandar paquetes a una máquina para comprobar si está accesible.

- `Sniffer`
    
    Analizador de paquetes (también conocido como analizador de red o analizador de protocolos) que se encarga de interceptar y registrar tráfico que pasa por un determinado segmento de red.

- `Target`
    
    Un target es el objetivo de “algo”, en el contexto de este curso se ha referenciado a la palabra target como aquella aplicación, servidor o dominio que se quiere analizar.

- `Time To Live (TTL)`
    
    El tiempo de vida de un paquete es un concepto usado en redes de computadores para indicar por cuántos nodos puede pasar un paquete antes de ser descartado por la red o devuelto a su origen.

- `Traceroute`
    
    Comando que traza el recorrido entre routers, ofreciendo información acerca de las direcciones IPs hasta llegar en un máximo de saltos a la máquina destino.