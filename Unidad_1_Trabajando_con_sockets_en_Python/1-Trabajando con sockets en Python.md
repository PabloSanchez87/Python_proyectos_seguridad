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
6. Resumen

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


## 4. Implementar en Python un escáner de puertos con sockets.
- Los sockets son el bloque de construcción fundamental para las comunicaciones de red y de manera fácil podemos verificar si un puerto específico está abierto, cerrado o filtrado al llamar al método `connect_ex()`

- `Método connect_ex()`
    - El método `socket.connect_ex(dirección, puerto)` se usa para implementar el escaneo de puertos con sockets.
    - Este script muestra que los puertos están abiertos en la máquina localhost con la interfaz de dirección IP loopback 127.0.0.1

        ```python
        import socket

        ip ='127.0.0.1'
        portlist = [22,23,80,912,135,445,20,631]
        for port in portlist:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((ip,port))
            print(port,":", result)
	        sock.close()
        ```
        ```
        # Output
        22 : 111
        23 : 111
        80 : 111
        912 : 111
        135 : 111
        445 : 111
        20 : 111
        631 : 111
        ```

- **`Escáner de puertos con sockets`**

    - Por ejemplo, podríamos tener una función que acepte por parámetros una IP y una listsa de puertos y devuelva para cada puerto si está abierto o cerrado.

    >[!NOTE]
    > En este caso, necesistamos importar el módulo socket y sys. El módulo sys lo utilizamos para salir del programa con la instruccion sys.exit() y devovler el control al intérprete de Python en caso de error de conexión. 
    > Si ejecutamos la función desde nuestro protrama principal vemos como comprueba cada uno de los puertos y nos devuelve si está abierto o cerrado para cada ip determinada.
    > El primer parámetro pude ser tanto una IP como un nombdre de dominio ya que el módulo es capaz de resolver un nombre a partir de una IP y viceversas.

    ```python
    import socket
    import sys

    def comprobarListaPuertos(ip,portlist):
        try:
            for port in portlist:
                sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip,port))
                if result == 0:
                    print ("Puerto {}: \t Abierto".format(port))
                else:
                    print ("Puerto {}: \t Cerrado".format(port))
                sock.close()
        except socket.error as error:
            print (str(error))
            print ("Error de conexion")
            sys.exit()

    comprobarListaPuertos('www.google.es',[80,8080,443,22])
    ```

    - **Nota:** Utilizamos `settimeout()` para indicarle un tiempo de intento de conexión en segundos.


- **`Escaner de puertos avanzado`**

    - En el siguiente código de Python le permitirá escanera un host local o remoto en busca de puertos abierto.
    - El programa busca puerto seleccionados a partir de una determinada dirección IP introducida por el usuario y refleja elo spuertos abierto de regreso al usuario.
    - Si el puerto está cerrrado, también muestra información sobre el motivo, por ejemplo, por tiemout de la conexión.


        ```python
        # Escaner de puertos con sockets

        # Importamos modulo socket
        from socket import * 

        # Preguntamos por la IP                 
        ip = input("Introduce IP : ")

        # Preguntamos por el puertos           
        puerto_inicio = input("Introduce puerto de inicio : ") 
        puerto_fin = input("Introduce puerto de fin : ")
            
        print ("Escaneando IP {} : ".format(ip))

        #recorrer cada uno de los puertos
        for port in range(int(puerto_inicio),int(puerto_fin)+1):
            print ("Probando puerto {} ...".format(port))
            # Crea el objeto socket
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(5)
            
            # Comprobar conexion e imprimimos si el puerto está abierto
            if(s.connect_ex((ip,port))==0):
                print("El puerto " , port, "está abierto")
            
            # Cierra el socket
            s.close()
            
        print("Escaneo finalizado!")
        ```

- **`Escáner de puerto a partir de un dominio`**
    - El siguiente script nos permitirá escaner una dirección IP con las funciones `portScanning` y `scocketScan`.
    - El programa busca puertos seleccionados en un dominio específico resuelto a partir de la dirección IP ingresada por el usuario por parámetro.

    - **Ejecución**
        - `.\socket_portScan.py -H www.google.es -P 80,21,22,23` 

        ```python
        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        import optparse
        from socket import *
        from threading import *

        def socketScan(host, port):
            try:
                socket_connect = socket(AF_INET, SOCK_STREAM)
                socket_connect.settimeout(10)
                socket_connect.connect((host, port))
                print('[+] %d/tcp open \n' % port)
            except Exception as error:
                print(error)
                print('[-] %d/tcp closed \n' % port)
            finally:
                socket_connect.close()	

        def portScanning(host, ports):
            try:
                ip = gethostbyname(host)
            except:
                print("[-] Cannot resolve '%s': Unknown host" %host)
                return

            try:
                name = gethostbyaddr(ip)
                print('\n[+] Scan Results for: ' + name[0])
            except:
                print('\n[+] Scan Results for: ' + ip)

            for port in ports:
                t = Thread(target=socketScan,args=(ip,int(port)))
                t.start()

        def main():
            parser = optparse.OptionParser('socket_portScan '+ '-H <Host> -P <Port>')
            parser.add_option('-H', dest='host', type='string', help='specify host')
            parser.add_option('-P', dest='port', type='string', help='specify port[s] separated by comma')

            (options, args) = parser.parse_args()

            host = options.host
            ports = str(options.port).split(',')

            if (host == None) | (ports[0] == None):
                print(parser.usage)
                exit(0)

            portScanning(host, ports)


        if __name__ == '__main__':
            main()
        ```

        - `optparse`: Proporciona una forma de analizar opciones de línea de comandos (parámetros que el usuario introduce al ejecutar el script).
        - `socket`: Proporciona las funcionalidades necesarias para crear conexiones de red.
        - `threading`: Permite crear hilos para ejecutar múltiples operaciones de escaneo en paralelo, acelerando el proceso.
        - `Función socketScan(host, port)`:
            - Esta función intenta establecer una conexión TCP con el host y el puerto especificados.
            - socket(AF_INET, SOCK_STREAM) crea un socket de tipo STREAM (TCP) que se conecta a una dirección IP (AF_INET).
            - settimeout(10) establece un tiempo de espera de 10 segundos para la conexión.
            - connect((host, port)) intenta conectar el socket al host y puerto especificados.
            - Si la conexión es exitosa, se imprime que el puerto está abierto.
            - Si ocurre un error, se muestra un mensaje indicando que el puerto está cerrado.
            - Finalmente, el socket se cierra en el bloque finally, asegurando que el recurso se libere.
        - `Función portScanning(host, ports)`:
            - Esta función se encarga de resolver el nombre de host a una dirección IP y luego iniciar el escaneo de los puertos proporcionados.
            - gethostbyname(host) intenta resolver el nombre de dominio en una dirección IP. Si no se puede resolver, se muestra un mensaje de error.
            - gethostbyaddr(ip) intenta obtener el nombre de host asociado con la IP. Si no se puede obtener, simplemente se usa la IP.
            - Luego, se recorre la lista de puertos proporcionados. Para cada puerto, se crea un hilo (Thread) que ejecuta la función socketScan en paralelo, lo que permite escanear varios puertos al mismo tiempo.
        - `Función main()`
            - Esta función utiliza optparse para analizar los argumentos de línea de comandos.
            - -H especifica el host (por ejemplo, un nombre de dominio o una dirección IP).
            - -P especifica los puertos, separados por comas (por ejemplo, 80,443,22).
            - Si el host o los puertos no se proporcionan, el script muestra la información de uso y termina.
            - Si se proporcionan ambos, llama a portScanning con el host y la lista de puertos.

    - - [Ejemplos de scripts en jupytet notebook](/Unidad-1/2-sockets_metodos.ipynb)

## 5. Implementar en Python un servidor HTTP.
- Podríamos crear un socket del tipo TCP y vincularlo a un puerto.
- Podríamos utilizar 'localhost', para aceptar conexiones desde la misma máquina.
- El puerto podría ser el 80, pero necesita privilegios de root, usaremos uno mayor o gual que 8080.

### `Métodos de socket del servdor`
- `socket.bind(direccion)`: permite conectar la dirección con el socket, con el requisito de que el socket debe estar abierto antes de establecer la conexción.
- `socket.listen(número_conexiones)`: acepta como parámetro el número máximo de conexiones de los clientes e inicia la escucha TCP para la conexiones entrantes.
- `socket.accept()`: permiete aceptar conexiones del cliente. Devuelve dos valores:
    - client_socket: socket conectado al cliente.
    - client_address: dirección del cliente.

  Antes de usar este método, debe lllamar a los métodos `bind` y `listen`.

### `Implementación del servidor HTTP`
- De los métodos comentados anteriormente podríamos utilizar el método `bind` que acepta como parámetro la dirección del servidor, y el puerto.
- El módulo socket proporciona el método `listen()` que permite poner en cola hasta un máximo de n solicitudes de conexión.
    - Por ejemplo, podríamos establer en 5 el número máximo de peticiones con la instrucción `socket.listen(5)`.
- Posteriormente, podríamos establecer la lógica de nuestro servidor cada vez que recibe la petición de un cliente.
- Utilizmaos el método `accept()` para aceptar las conexiones de los clientes, leer datos entrantes con el método `recv()` y enviar datos con el método `send()`.

    ```python	
    import socket

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind(('localhost', 8080)
    mySocket.listen(5)

    while True:
        print('Esperando conexiones...')
        (recvSocket, address) = mySocket.accept()
        print('Petición HTTP recibida:')
        print(recvSocket.recv(1024))
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n",'utf-8'))
        recvSocket.close()
    ```

- [Servidor_http.py](/Unidad-1/3-Servidor_http.py)
- [Test_servidor_http.py](/Unidad-1/4-test_servidor_http.py)
    - En otra terminal podemos ejecutar el código del test con el servidor levantado.

## 6. Resumen
- Crear un socket utilizando el constructor `s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, protocolo=0)` donde inidicamos la familia, el tipo y el protocolo.
- Obtener información con los métodos `gethostbyaddr(ip)` que nos permite obtener un nombre de dominio a partir de una dirección IP y `gethostbyname(hostname)` que nos permite obtener una dirección IP a partir de un nombre de dominio.
- Gracias al uso del método `socket.connect_ex(dirección, puerto)` podemos verificar si un puerto está abierto o cerrado.
- Implementar nuestro propio servidor HTTP qu tiene la capacidad de atender peticiones por parte de n clientes de forma simultánea. Con el uso del método `socket.bind(dirección)` nos permite conectar la direccion con el sockert, con el requisito de que el socket debe estar abierto antes de llamar a este método.
- El método `socket.listen(n)` nos permite establecer un número máximo de conexiones que se pueden establecer en cola.
- Implementamos un cliente HTTP para realizar peteiciones al servidor creado.

### FAQ
- ¿cuántas familias de direcciones para sockets encontramos en el módulo socket de Python?

    - AF_INET: son las direcciones IPv4. Se representa con el host y el puerto.
    - AF_INET6: son las direcciones IPv6. Se representa con el host y el puerto (así como la etiqueta de flujo “Flow Label” con la documentación en https://tools.ietf.org/html/rfc6437, y el alcance de la id “scope id” que indica el interfaz qué usar)
    - AF_UNIX o AF_LOCAL: son las direcciones locales de Unix. Se representa como un string que apunta a un fichero del sistema.

- ¿Cuál es la utilidad de los sockets?

    - Los sockets mantienen la conexión en tiempo real entre un cliente y un servidor con el objetivo de enviar y recibir datos de un lado a otro. Por ejemplo, podremos crear nuestro propio chat; es decir, una aplicación de escritorio en nuestro ordenador recibiendo y enviando mensajes, para que el lado del servidor reciba y envíe los mensajes en tiempo real.

### Enlaces
- [HOWTO de programación de sockets](https://wiki.python.org/moin/HowTo/Sockets)

- [Documentación del módulo sockets](https://docs.python.org/3/library/socket.html)

### Glosario
- `API`

    Una API o Application Programming Interface, es un conjunto de clases, métodos y procedimientos que se ofrecen como una biblioteca para ser utilizados por otro software sin la necesidad de saber como esta implementada internamente, sirve como una capa de abstracción.

- `Dominio`
    
    Sistema de denominación servidores en Internet el cual está formado por un conjunto de caracteres que identifica un sitio de la red accesible por un usuario. Cada dominio es administrado por un servidor de dominios (DNS). Los más comunes son .com, .edu, .net, .org y .es

- `HTTP`
    
    Hyper Text Transfer Protocol. Protocolo base de la web y que ofrece un conjunto de instrucciones para que los servidores y navegadores funcionen

- `Protocolo`

    Formato o conjunto definido de reglas, procedimientos que permiten inter-operar a dos dispositivos. Un protocolo sirve para la comunicación en red o entre aplicaciones

- `Proxy`
    
    Mecanismo que permite compartir una única conexión desde una red local a una red externa.`

- `Puerto`

    Abstracción empleada por los protocolos de transporte a fin de distinguir entre múltiples conexiones simultáneas en un solo nodo de la red.

