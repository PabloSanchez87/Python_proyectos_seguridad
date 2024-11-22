# Conexiones con servidores FTP, SFTP y SSH desde Python

## Objetivos

### Competencia
- Conocer los principales módulos disponibles en Python para realizar conexiones con servidores FTP, SFTP y SSH.
- Alguna de las herramientas que permiten conectarnos con estos servidores las podemos encontrar en Python, entre las que podemos destacar `Paramiko` y `ftplib`.

### Resultados
- Crear scripts en Python con el objetivo de conectarnos con servidores FTP con el objetivo de listar y obtener ficheros con el módulo `FTPlib`.
- Crear scripts en Python con el objetivo de conectarnos con servidores SFTP con el objetivo de ejecutar comandos de forma remota con el módulo `Paramiko`.
- Crear scripts en Python con el objetivo de conectarnos con servidores SSH mediante un proceso de fuerza bruta mediante ficheros de usuario y contraseña con el módulo `Paramiko`.

---

## Conexiones con servidores FTP utilizando el módulo `ftplib`

- `FTP` es un protocolo que emplea el puerto 21 y permite a clientes y servidores conectados en la misma red, intercambiar ficheros.

- El diseño del protocolo está definido de tal forma que no es necesario que cliente y servidor se ejecuten en la misma plataforma, cualquier cliente y cualquier servidor FTP pueden utilizar un SO distinto y utilizar las primitivas y comandos definidos en el protocolo para transferir ficheros.

- EL protocolo está enfocado en ofrecer a clientes y servidores una velocidad aceptable en la transferencia de ficheros, pero no se tiene en cuenta conceptos más importantes como seguridad.

- La desventaja de este protocolo es que la información viaja en texto plano, incluso las credenciales de acceso cuando un cliente se autentica en el servidor FTP.

### `Módulo ftplib`

- `ftplib` es una librería nativa de Python que permite la conexión con servidores FTP y la ejecución de comandos en dichos servidores.

- Está diseñada para crear clientes FTP con pocas líneas de código y para realizar rutinas de admin/server.

- [Página oficial](https://docs.python.org/3/library/ftplib.html)

- Este módulo puede ser utilizado para crear scripts que permiten automatizar determinadas tareas o realizar ataques por diccionario conta un servidor FTP.

- Además, soporta conexiones cifradas con TLS, para ello se utiliza las utilidades definidas en la clase `FTP_TLS`.

- El módulo `ftplib` , nos provee de los métodos necesarios para crear clientes FTP de forma rápida y sencilla. Para conectarse a un servidor FTP, el móduglo `ftplib` nos provee de la clase `FTP`.

### Coneción con un servidor FTP

- El método constructor de la clase `FTP` (método `__init__()`), recibe como parámetros el host, usuario y clave, de forma que pasando estos parámetros durante la instanciación de un objeto de la clase FTP, se ahorra el uso de los métodos `connect(host, port, timeout)` y `login(user, passwd)`.

- Para conectarnos con un servidor lo podemos hacer de varias formas:

    1. Utilizar el constructor de la clase `FTP`.
    2. Utilizar los métodos:
        - `connect(host, port, timeout)` : que acepta como parámetros el host, el puerto y el tiempo de espera.
        - `login(user, passwd)`: que acepta como parámetros el usuario y la contraseña.

### Métodos de la clase `FTP`


| Método                          | Descripción                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| `FTP.connect(host)`             | Conecta al servidor FTP especificado por `host`.                                            |
| `FTP.login(user, passwd)`       | Inicia sesión en el servidor FTP con el usuario y contraseña proporcionados.                |
| `FTP.cwd(path)`                 | Cambia el directorio de trabajo actual en el servidor FTP al especificado por `path`.       |
| `FTP.dir()`                     | Lista el contenido del directorio actual en el servidor FTP.                                |
| `FTP.retrbinary(cmd, callback)` | Descarga un archivo en modo binario y ejecuta `callback` con cada bloque de datos recibido. |
| `FTP.storbinary(cmd, fp)`       | Sube un archivo al servidor en modo binario desde un archivo abierto `fp`.                  |
| `FTP.quit()`                    | Cierra la conexión con el servidor FTP de forma ordenada.                                   |
| `FTP.delete(filename)`          | Elimina el archivo especificado en el servidor FTP.                                         |
| `FTP.mkd(path)`                 | Crea un nuevo directorio en el servidor FTP con la ruta especificada.                       |
| `FTP.rmd(path)`                 | Elimina el directorio especificado del servidor FTP.                                        |
| `FTP.rename(fromname, toname)`  | Cambia el nombre de un archivo o directorio en el servidor FTP.                             |
| `FTP.size(filename)`            | Obtiene el tamaño del archivo especificado en bytes.                                        |
| `FTP.pwd()`                     | Devuelve el directorio de trabajo actual en el servidor FTP.                                |
| `FTP.nlst()`                    | Devuelve una lista de los nombres de archivos y directorios en el directorio actual.        |


- En este ejemplo, nos conectamos a un servidor FTP y realizamos diferentes operaciones relacionadas con la obtención de archivos.
    
    - Vamos a enumerar los achivos disponibles en el servidor ftp del kernel de linux usando los métodos `FTP.dir()` y `FTP.nlst()`.

    - [Código de ejemplo](/Unidad_9_Conexiones_con_servidores_FTP_SFTP_SSH_desde_Python/2-Conexion_FTP.py)

    - Resultado:

        ```
        Server:  220 ProFTPD Server (mirror.as35701.net) [::ffff:195.234.45.114]
        230-Welcome to mirror.as35701.net.
        
        The server is located in Brussels, Belgium.
        
        Server connected with gigabit ethernet to the internet.
        
        The server maintains software archive accessible via ftp, http, https and rsync.
        
        ftp.be.debian.org is an alias for this host, but https will not work with that
        alias. If you want to use https use mirror.as35701.net.
        
        Contact: mirror-admin at as35701.net
        
        230 Anonymous access granted, restrictions apply

        Ficheros y directorios en el directorio raíz:
        ubuntu-cloudimages
        debian
        mint-iso
        debian-cd
        ubuntu
        welcome.msg
        ...

        Contenido del directorio '/debian':
        ls-lR.gz
        tools
        indices
        doc
        README.html
        extrafiles
        ...

        Contenido del directorio '/debian-security':
        ls-lR.gz
        indices
        README.security
        ...

        Contenido del directorio '/www.kernel.org':
        pub
        lost+found
        ```

        - Usando el método `getwelcome()` obtenemos el mensaje de bienvenida del servidor FTP.

        - Con el método `dir()` enumeramos archivos y directorios en el directorio raíz.

        - Con el método `nlst()` obtenemos una lista de los archivos y directorios en el directorio actual.

### Descarga de ficheros de servidores FTP (Parte 1)

- En el siguiente scripts, nos estamos conectando a un servidor FTP para descargar un archivo binario del servidor `ftp.be.debian.org`.

- **Nos conectamos con un servidor FTP anónimo** y descargamos archivos bianrios sin autenticación.

- [Código de ejemplo](/Unidad_9_Conexiones_con_servidores_FTP_SFTP_SSH_desde_Python/3-Conexion_FTP_anonimo.py)

### Descarga de ficheros de servidores FTP (Parte 2)

- Otra forma de descargar un archivo desde un servidor FTP es mediante el método `retrlines()`, que acepta como parámetro el comando ftp a ejecutar.

- Por ejemplo, `LIST` es un comando definido por el protocolo, así como otros que también se pueden aplicar como RETR, NLST o MLSD. Puedes obtener más informacion sobre los comandos admitidos en el documento [RFC 959](https://datatracker.ietf.org/doc/html/rfc959.html).

- El segundo parámetro del método `retrlines()` es una función de devolución de llamada, que se llama para cada línea de datos recibidos.

- [Código de ejemplo](/Unidad_9_Conexiones_con_servidores_FTP_SFTP_SSH_desde_Python/4-Conexion_FTP_retrlines.py)


### Comprobar conexión FTP anónima

- Podemos utilizar el módulo `ftplib` para construir un script para detemrinar si un servidor ofrece inicios de sesiones anónimas.

- Este mecanismo consiste en suministrar al servidor FTP la palabra clave `anonymous` como usuario y contraseña.

- De esta forma, podemos realizar consultas al servidor FTP si conocer los datos de un usuario específico.

- [Código de ejemplo](/Unidad_9_Conexiones_con_servidores_FTP_SFTP_SSH_desde_Python/5-Conexion_FTP_anonima.py)

    - La función anonymousLogin(hostname) toma un nombre de host como parámetro y verifica la conexión con el servidor FTP con un usuario y contraseña anónimos.

    - La función intenta crear una conexión FTP con credenciales anónimas y muestra información realacionada con el servidor y la lista de archivos en el directorio raíz.

    - Resultado:

        ```
        230-Welcome to mirror.as35701.net.
 
        The server is located in Brussels, Belgium.
        
        Server connected with gigabit ethernet to the internet.
        
        The server maintains software archive accessible via ftp, http, https and rsync.
        
        ftp.be.debian.org is an alias for this host, but https will not work with that
        alias. If you want to use https use mirror.as35701.net.
        
        Contact: mirror-admin at as35701.net
        
        230 Anonymous access granted, restrictions apply

        [*] ftp.be.debian.org FTP Anonymous Login Succeeded.
        220 ProFTPD Server (mirror.as35701.net) [::ffff:195.234.45.114]
        drwxr-xr-x   9 ftp      ftp          4096 Nov 22 08:36 debian
        drwxr-xr-x   5 ftp      ftp           105 Nov 10 06:39 debian-cd
        drwxr-xr-x   7 ftp      ftp          4096 Nov 21 23:27 debian-security
        drwxr-xr-x   5 ftp      ftp          4096 Oct 13  2006 ftp.irc.org
        -rw-r--r--   1 ftp      ftp           432 Jul  9  2021 HEADER.html
        drwxr-xr-x   5 ftp      ftp          4096 Nov 22 08:23 mint
        drwxr-xr-x   5 ftp      ftp            49 Nov 30  2015 mint-iso
        lrwxrwxrwx   1 ftp      ftp            33 Apr 29  2021 pub -> /var/www/html/www.kernel.org/pub/
        drwxr-xr-x   7 ftp      ftp          4096 Nov 22 09:50 ubuntu
        drwxr-xr-x  36 ftp      ftp          4096 Nov 22 05:47 ubuntu-cdimage
        drwxr-xr-x  30 ftp      ftp          4096 Nov 22 09:16 ubuntu-cloudimages
        drwxr-xr-x   7 ftp      ftp          4096 Nov 22 07:17 ubuntu-ports
        drwxr-xr-x  15 ftp      ftp          4096 Nov 22 02:24 ubuntu-releases
        drwxr-xr-x  24 ftp      ftp           291 Nov 22 08:01 video.fosdem.org
        -rw-r--r--   1 ftp      ftp           390 Jul  9  2021 welcome.msg
        drwxr-xr-x   4 ftp      ftp          4096 Jun 14  2023 www.kernel.org
        ```

#### Ejercicio: Comprobar si un servidor FTP soporta autenticación anónima.

- [Código del ejercicio](/Unidad_9_Conexiones_con_servidores_FTP_SFTP_SSH_desde_Python/6-Comprobar_conexion_FTP_anonima.py)

    ```bash	
    220 ProFTPD Server (mirror.as35701.net) [::ffff:195.234.45.114]
    drwxr-xr-x   9 ftp      ftp          4096 Nov 22 08:36 debian
    drwxr-xr-x   5 ftp      ftp           105 Nov 10 06:39 debian-cd
    drwxr-xr-x   7 ftp      ftp          4096 Nov 21 23:27 debian-security
    drwxr-xr-x   5 ftp      ftp          4096 Oct 13  2006 ftp.irc.org
    -rw-r--r--   1 ftp      ftp           432 Jul  9  2021 HEADER.html
    drwxr-xr-x   5 ftp      ftp          4096 Nov 22 08:23 mint
    drwxr-xr-x   5 ftp      ftp            49 Nov 30  2015 mint-iso
    lrwxrwxrwx   1 ftp      ftp            33 Apr 29  2021 pub -> /var/www/html/www.kernel.org/pub/
    drwxr-xr-x   7 ftp      ftp          4096 Nov 22 09:50 ubuntu
    drwxr-xr-x  36 ftp      ftp          4096 Nov 22 05:47 ubuntu-cdimage
    drwxr-xr-x  30 ftp      ftp          4096 Nov 22 09:16 ubuntu-cloudimages
    drwxr-xr-x   7 ftp      ftp          4096 Nov 22 07:17 ubuntu-ports
    drwxr-xr-x  15 ftp      ftp          4096 Nov 22 02:24 ubuntu-releases
    drwxr-xr-x  24 ftp      ftp           291 Nov 22 08:01 video.fosdem.org
    -rw-r--r--   1 ftp      ftp           390 Jul  9  2021 welcome.msg
    drwxr-xr-x   4 ftp      ftp          4096 Jun 14  2023 www.kernel.org
    None

    [*] ftp.be.debian.org FTP Anonymous Logon Succeeded.
    ['ubuntu-cloudimages', 'debian', 'mint-iso', 'debian-cd', 'ubuntu', 'welcome.msg', 'debian-security', 'mint', 'video.fosdem.org', 'ubuntu-releases', 'www.kernel.org', 'ubuntu-ports', 'ftp.irc.org', 'ubuntu-cdimage', 'HEADER.html']
    [+] Found default page: HEADER.html
    ```	

### Proceso de fuerza bruta para conectarnos a un servidor FTP

