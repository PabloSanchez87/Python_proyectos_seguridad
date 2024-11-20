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

## Usando `nmap` con el módulo `os`

