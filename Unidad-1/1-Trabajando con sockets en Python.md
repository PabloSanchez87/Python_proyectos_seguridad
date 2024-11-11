# Trabajando con sockets en Python

## Objetivos

### Competencia
Módulo sockets para realizar peticiones de red, resolver un dominio a partir de una dirección ip y viceversa, implementar un escáner de puertos y crear su propio servidor http apra atender peticiones.

### Resultados
- Conocer los principales métodos del módulo sockets para resolver un dominio a partir de una dirección ip y viceversa.
- Crear scripts en Python para automatizar un proceso escáner de puertos a partir de la dirección ip.
- Crear scripts en Python para crear tu propio servidor HTTP
- Crear scripts en Python para automatizar un proceso de escáner de puertos a partir de un dominio.

### Índice

1. Introducción a python para proyectos de seguridad.
2. Introducción a sockets.
3. Recopilación de información con sockets.
4. Implementar en Python un escáner de puertos con sockets.
5. Implementar en Python un servidor HTTP.

---

## 1. Introducción a python para proyectos de seguridad.

Características de Python:
- Lenguaje multiplataforma y de código abierto.
- Lenguaje sencillo, ráìdo, robusto y potente.
- Muchas de las liberías, módulos y proyectos enfocados a la seguridad informática se encuentran escritos en Python.
- Hay mucha documentación y una comunidad de usuarios.
- Es un lenguaje diseñado apra realizar programas robustos con pocas líneas de código.
- Ideal para realizar prototipos y pruebas de concepto (PoC) rápidas.

## 2. Introducción a sockets.

- Los sockets son el componente principal que nos permite aprovechar las capacidades del sistema operativo para interactuar con la red.
- Los sockets son como un canal de comunicación punto a punto entre un cliente y un servidor.
- Los sockets de red son una manera fácil de establecer una comunicación entre procesos que están en la misma máquina o en diferentes máquinas.
- El concepto de sockets es muy similar al de los descriptores de archivos UNIX.
- Los comando como `read()` y `write()` que nos permiten trabajar con el siste a de archivos, funcionan de manera simiar a los socets.
- Una dirección socket de red consta de una dirección IP y un número de puerto.
- **El objetivo de un socket es comunicar procesos a través de la red.**

    ### `Sockets de red en Python`

    - La comunicación entre distintas entidades en una red se basa en el clásico concepto de sockets.
    - Los sockets son un concepto abstracto con el que se designa el punto final de una conexión.
    - Los programas utilizan sockets para comunicarse con otros programas, que peuden estar situados en computadoras distintas.

    - **Un socket queda definido por la dirección IP de la máquina, el puerto en el que escucha y el protocolo que utiliza.**

    - Los tipos y funciones necesarios apra trabajar con sockets se encuetran en Python en el módulo `socket`.

    - Los sockets se clasifican en dos tipos::
        - Sockets de flijo TCP (`socket.SOCK_STREAM`)
        - Sockets de datagrama UDP (`socket.SOCK_DGRAM`)

      Dependiendo de si el servicio utilizado es TCP (que es orientado a conexión y fiable), o UDP (que es orientado a comunicación sin conexión), se utilizará el tipo adecuado.

      **Nota:** TCP cubren el 90% de las necesidades comunes.
    
    - Para crear un socket se utiliza el constructor `socket.socket()` que puede tomar como parámetros opcionales:
        - La familia: default: `AF_INET`
        - El tipo: default: `SOCK_STREAM`
        - El protocolo: default: `0`

    - **Sintaxis:**
        ```python
        socket.socket(socket_family, socket_type, socket_protocol=0)
        ```
        
    - Los sockets también se peuden clasificar según la familia.
        - Sockets UNIX (`socket.AF_UNIX`) que se crearon antes de la concepción de las redes y se basan en el sistema de archivos.
        - Sockets de Internet (`socket.AF_INET`) que se crearon para la comunicación de red y se basan en la arquitectura de la red IP.

            ![alt text](/Unidad-1/img/contructor_socket.png)

    ### `Módulo socket en Python`

    - Los tipos y funciones necesarios apra trabajar con los sockets se pueden encontrar en el módulo `socket`.
    
    - El módulo `socket`  expone todas las piezas necesarias para escribir rápidamente clientes y servidores TCP y UDP.

    - EL módulo de socket tiene todo lo que necesita para contruir un servidor o un cliente de socket.
    - En Python, el socket devuelve un objeto al que se peuden aplicar los métodos de la clase `socket` que viene instalado por defecto.

        ```python
        import socket

        dir(socket)
        ```

    - Para abrir un socket en un determinada máquina utilizamos el constructor de la clase socket que acepta por parámetros la familia, el tipo de socket y el protocolo. Una llamada típica para contruir un socket que funcione a nivel TCP es pasando como parámetros la familia y el tipo de socket.

        ```python
        # Method

        __init__(self, family=2, type=1, proto=0, _sock=None)

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ```

## 3. Recopilación de información con sockets.

- Los métodos útiles para recopiar más información son:
    - `gethostbyaddr(dirección):` nos permite obtener un nombre de dominio a partir de la dirección IP.
    - `gethostbyname(hostname)`: nos permite obtener una dirección IP a patir de un nombre de dominio.

- Podemos obtener más información sobre estos métodos con el comando `help(socket)`

    ### Ejemplos de métodos realacionado con el host, dirección IP y dominio

    - `socket.gethostbyname(hostname)`: este método convierte un nombre de host al formato de dirección IPv4. La dirección IPv4 se devuelve en forma de cadena de texto. Este método es equivalente al comando `nslookup`.
        ```python
        >>> import socket
        >>> socket.gethostbyname('www.google.com')
            '142.250.184.4'
        ```

    - `socket.gethostbyname_ex(nombre)`: este método devuelve muchas direcciones IP para un solo nombre de dominio. Significa que un dominio se ejecuta en múltiples IPs.

        ```python
        >>> import socket
        >>> socket.gethostbyname_ex('www.google.com')
        ('www.google.com', [], ['142.250.184.4'])
        ```

        - Otro de los métodos que disponemos en la clase sockets es el que permite obtener el nombre cualificado de un dominio:

            ```python
            >>> import socket
            >>> socket.getfqdn('www.google.com')
            'mad07s09-in-f4.1e100.net'
            ```

    - `socket.gethostbyaddr(ip_address)`: este método devielve una tupla (hostname, nombre, ip_address_list) donde hostaname es el nombdre del host que responde a la dirección IP especificia, el nombre es una lisda de nombres asociados con la misma dirección IP y ip_address_list es una lista de direcciones IP asociadas con el nombre de host especificado.

        ```python
        >>> import socket
        >>> socket.gethostbyaddr('8.8.8.8')
        ('dns.google', [], ['8.8.8.8'])
        ```

    - `socket.getservbyname(servicename, [protocolname])`: este método devuelve el número de puerto asociado con el servicio especificado.

        ```python
        >>> import socket
        >>> socket.getservbyname('http')
        80
        >>> socket.getservbyname('smtp', 'tcp')     
        25
        ```

    - `socket.getservbyport(port, [protocolname])`: este método realiza la operación inversa a la anterior, permite obtener el nombr del puerto a partir del número de puerto.

        ```python
        >>> import socket
        >>> socket.getservbyport(80)
        'http'
        >>> socket.getservbyport(23)
        'telnet'
        ```

    - [Ejemplo de script en jupytet notebook](/Unidad-1/2-sockets_metodos.ipynb)