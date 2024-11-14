# Recolección de información de servidores con Python

## Objetivos

### Competencia
- Conocer los principales módulos disponibles en Python con el objetvo de extraer información de servidores y servicios que están ejecutando, así como nombres de dominio y banners.
- Sacar información que nos puede resultar útil para fases posteriores en nuestro proceso de pentesting o auditoría.

### Resultados
- Extraer información de los banners de un servidor utilizando el API de Shodan.
- Extraer información de los servicios de Shodan como herramienta para extrar información de los servidores.
- Crear scriots en Python para automatizar el proceso de extracción de información de servidores web con el registro WHOIS.
- Crear scripts en Python para automatizar el proceso de extraccón de información de servidores DNS con el módulo DNSPython.

El proceso de recolección de informaciónse puede automatizar utilizando tanto módulos que vienen instalados por defecto como módulos de terceros. 

Uno de los objetivos es conocer los módulos que permiten extraer información que los servidores exponen de forma pública.


### Índice

1. Utilizando Shodan para obtener información de un servidor.
2. Utilizando Python para realizar búsquedas en Shodan.
3. Utilizando el módulo de Python-whois para obtener información de un servidor.
4. Introducción al módulo DNSPython para obtener información de servidores DNS.
5. Resumen

---

## 1. Utilizando Shodan para obtener información de un servidor.

- **Shodan** es un motor de búsqueda que se encarga de rastrear servidores y diversos tipos de dispositivos en la red., extrayendo información útil sobre servicios que se encuentran en ejecución en dichos servidores.

- A diferencia de otros buscadores, Shodan no busca contenido web, lo que hace es buscar entre las cabeceras de las peticiones HTTP información sobre el servidor, tales como SO, banners, tipo de servidor y versiones.

- Shodan funciona de forma similar a los buscadores de internet, con la diferencia de que no indexa los contenidos de los servidores encontrados, sino las cabeceras y los banners devueltos por los servidores.

- Es conocido como el 'google de los hackers' ya que permite realziar búsquedas aplicando diferentes tipos de filtros para recuperar información de servivios que utilicen el protocolo HTTP concreto.

### Diferencias entre Shodan y otros buscadores

- Shodan es un proyecto que escane el direccionamiento público de internet en más de 200 puertos y si encuentra puertos abierto, guarda la respuesta (banner) que dan estas ips por estos puertos.

- Esta información almacenada por Shodan es accesible vía Web, por línea de comando y mediante una APIs de diferentes lenguajes.

- La principal diferencia entre Shodan y otros buscadores es que Shodan recorre internet escaneando cada dirección IP, obeteniendo los servicios en ejecución y los puestos que tiene abiertos, capturando el banner que le devuelve en cada servicio.

- Esto nos permite hacer búsquedas en  la información retornadas para los servicios, de tal forma que permite encontrar, por ejemplo, todos los servidores apache de una versión en concreto.

- La mayoria de los buscadores trabajan a través de sus spiders, crawlers y robots recolectando información que va indexando, para luego organizarla y mostrarnos la misma en el momento que queremos.

- Shodan, en cambio, recolecta la información de los puertos que los dispositivos conectados a internet exponen y organiza tanto la información que estos otorgan a través de sus banners, así como tambiñen metadatos que los mismos offrecen en forma de ubicación geográfica, nombre de dominio, SO, ...

#### Ejemplo `port:53`

![alt text](/resources/shodan-1.png)

#### Extensión de Google Chrome

- Podríamos usar también Shodan desde un pligin disponible para Google Chrome.

    - [Plugin Shodan](https://chromewebstore.google.com/detail/shodan/jjalcfnidlmpjhdfepjhjbhnhkbgleap?utm_source=chrome-ntp-icon&pli=1)


### Filtros de Shodan

- Shodan incorpora diferentes tipos de filtros que nos pueden ayudar a realiza una búsqueda con más detalle valiéndose para ello de los metadatos que los dispositivos o servicios otorgan.

- Al igual que con cualquier motor de búsqueda, la potencia real viene con las consultas personalizadas. 

- Podemos destacar los siguientes filtros:
    - `after/before`: Filtra por fechas.
    - `country`: Filtra por país, por código de país o por nombre de país.
    - `city`: Filtra por ciudad.
    - `geo`: Filtra por latitud y longitud.
    - `hostname`: Filtra por nombre de dominio.
    - `net`: Filtra por subred, por un rango específico de ips o segmentod de red
    - `os`: Filtra por SO, por nombre de SO o por versión de SO.
    - `port`: Filtra por puerto.
    - `protocol`: Filtra por protocolo.

- **Ejemplo de búsqueda**

    - Servidores apache en London
        - apache city:"London"
    - Servidores ssha de uk:
        - ssh country:uk

- En este repositorio de Github puedes encontrar diferentes cadenas de búsqueda:
    - [Cadenas de búsqueda de Shodan](https://github.com/jakejarvis/awesome-shodan-queries)


### Servicios de Shodan

#### Servicio de mapas
- https://maps.shodan.io/

- Shodan dispone de un dashboard https://exposure.shodan.io/ donde podemos ver un resumen de los puertos y servicios expuestos para un país en concreto.

#### HoneyScore

- https://honeyscore.shodan.io/ 

- Permite comprobar si una determinada dirección IP es un honeypot, es decir, tiene un mecanismo configurado para detectar los intentos de uso y acceso no autorizado a los sistemas.

#### Shodan CLI "Command Line Interface"

- https://cli.shodan.io/

- Proporciona una manera de realizar búsquedas en Shodan desde líea de comandos. También se necesita iniciar el programa con la API KEY que se obtiene al registrarse en el sitio web de Shodan.

#### Servicio de exploits

- https://exploits.shodan.io/

- Shodan ofrece buscar exploits desde distintas bases de datos de vulnerabilidades.

#### Servicio de imágenes

- Shodan ofrece imágenes para proporciona un contexto más amplio en torno a los resultados encontrados por el motor.

- La página de imágenes es útil para realizar un explotación a tracés de las imágenes obtenidas de las búsquedas de Shodan, mostrar con qué frecuencia las pantallas de inicio se sesión están disponibles

- Los investigadores también pueden ver ejemplos de las pantallas de inicio de sesión y administración de los dispositivos que se acaban de encontrar y no se mostraban inicialmente.

#### Shodan Monitor

- https://monitor.shodan.io/

- Es una herramienta diseñada para permitir a los usuariso llevar un seguimiento directo y sencillo de sus dispositivos, recibiendo recomendaciones de seguridad y notificaciones en tiempo real cuando uno de sus dispositicos se exponga en la red.

- Shodan Monitos actúa a grandes ragos como un escáner de puertos masivo que podemos intefrar fáciulmente con las conocidas herramientas Nmap, MetasSploit, Maltego y Foca, así como usarlo directamente desde Google Chrome y Firefox.

- Debemos tener en cuenta que para poder sacar todo el partido a esta herrramienta es recomendable estar registrado con un plan de suscripción de Shodan Developer. El plan gratuito solo nos permite resgistar hasta 16 IPs.


### Registro en Shodan

- https://account.shodan.io/login

- Una vez registrado podemos obtener nuestra API KEY, que nos permite realizar búsquedas en Shodan desde línea de comandos.


## 2. Utilizando Python para realizar búsquedas en Shodan.

- Si nos registramos como desarrolladores obtenemos una `SHODRAN_API_KEY`, que nos permite realizar búsquedas en Shodan desde línea de comandos.

- [Developers SHODAN](https://developer.shodan.io/api/clients)

> [!NOTE]
> Se recomienda utilizar un environment virtual para instalar las dependencias y para guardar la API KEY de manera segura.

> [!WARNING]
> La API KEY de Shodan es privada, no debemos publicarla en un repositorio público.

> [!IMPORTANT]
> Cabe resaltar que Shodan recoge la información que le devuelve la máquina, y nada le impide a esa máquina falase esta informacaión. Podría ser que un apache server nos engañe con la versión, etc. Todo esto nos puede hacer caer en falsos positivos y en honeypots, por tanto, hay que ir con cuidado y utilizar información que nos da Shodan como una primera búsqueda que despueés debemos analizar y verificar.

- [API REST SHODAN](https://developer.shodan.io/api)

    - Podemos utilizar el API utilizando los endpoins que aparecen en la documentación y concatenando como parámetros el API KEY y la consulta a realizar

    - Uno de los endpoints permite realizar una consulta de búsqueda en Shodan a través del parámetro `query`.

    - La cadena proporcionada se utiliza para buscar en la base de datos de Shodan, con la opción de proporcionar filtros dentro de la consulta de búsqueda utilizand un formato de `nombre filtro:valor`.

        - Por ejemplo, si queremos realizar una búsqueda, podemos utilizar el endopoint `/shodan/host/search` 

            ```
            https://api.shodan.io/shodan/host/search?key=SHODAN_API_KEY&query={query}
            ```
    
    - En el siguiente script, lo que hacemos e sobtener la información de un servidor a partir de su IP.

        - [Código del script](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/2-shodan_obtener_host.py)

        ```python
        import requests

        SHODAN_API_KEY = "API_KEY"
        ip = '8.8.8.8'

        def ShodanInfo(ip):
            try:
                result = requests.get('https://api.shodan.io/shodan/host/'+ip+'?key='+SHODAN_API_KEY+'&minify=True').json()
            except Exception as exception:
                result = {"error":"Informacion no disponible."}
        ```	

        ```	
        # Output
        {'region_code': 'CA', 'tags': [], 'ip': 134744072, 'area_code': None, 'domains': ['dns.google'], 'hostnames': ['dns.google'], 'country_code': 'US', 'org': 'Google LLC', 'data': [], 'asn': 'AS15169', 'city': 'Mountain View', 'latitude': 37.4056, 'isp': 'Google LLC', 'longitude': -122.0775, 'last_update': '2024-11-14T04:01:21.956842', 'country_name': 'United States', 'ip_str': '8.8.8.8', 'os': None, 'ports': [443, 53]}
        ```


### Acceso a Shodan desde Python
- [Librería oficial se Shodan en Python - Repositorio Github](https://github.com/achillean/shodan-python)

- Comando para instalar shodan-python
    ```bash
    pip install shodan
    ```

- La interfaz de línea de comandos (CLI) de Shodan está empaquetada con la librería oficial de Python para Shodan, lo que significa que si estás ejecutando la última version de la libería, deberias tener acceso a la consola.

- Debemos inicializar la API de Shodan para que podamos utilizar las funciones de la librería.
    ```bash
    shodan init $SHODAN_API_KEY
    ```

- El comando `shodan host` permite visualizar información sobre un host, conocer su geolocalización, puertos que están abiertos, y qué organización es propietaria de esa dirección IP.

- El comando `shodan search` permite realizar una búsqueda en Shodan y visualizar la información de los resultados en la terminal de forma amigable.

- Por defecto muestra la dirección IP, puerto, nombres del host y otros datos. Se puede utilizar el parámetro `--fields` para imprimir campos de banners en los cuales se está interesado.

    ```bash
    shodan search "port:80 banner:apache" --fields=ip,port,hostnames
    ```

#### `Shodanploit`
- Esta herramienta se trata de un script en python que contiene todas las llamadas API de Shodan desde línea de comandos

- [Enlace documentación](https://github.com/shodansploit/shodansploit)

- Con esta herramienta se puede tener todas las llamadas que hacemos a Shodan desde nuestra terminal, también nos permite hacer búsquedas detalladas sobre lo que queremos buscar.

### Búsquedas de Shodan en Python

- Shodan tiene sercidores que escanean internet, catalgon los resultados de los escaneos y luego permiten que las personas busquen y visualicen esos resultados.

- Por ejemplo, cuando un usuario le pide a Shodan que le muestre todos los seridores Microsft IIS versión 8 que se ejecuten en el puerto 8080 TCP en china, le mostraría los que el sistema tiene registrado, pero desde el punto de vista de **privacidad** del usuario ninguno de esos servidores sabe qué usuarios es el que buscó esta información.

- Con la función `search` que ofrece la API se pueden realizar búsquedas de la misma forma que se pueden hacer con la interfaz web.

    - [Código busqueda de Shodan](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/3-busqueda_shodan.py)

    ```python
     import shodan

    SHODAN_API_KEY = "API_KEY"
    shodan = shodan.Shodan(SHODAN_API_KEY)

    try:
        resultados = shodan.search('apache')
        print("Numero de resultados:",resultados.items())
    except Exception as exception:
        print(str(exception))
    ```

    - Si ejecutamos el script desde la terminal, vemos que si buscamos la cadena `apache` obtenemos xxx resultados.

- También podemos crear nuestra propia clase llamada `ShodanSearch` que tenga como métodos  `__init__` para inicializar el objeto de Shodan a apartir de nuestra API_KEY.

- Podemos tener un m,étodo buscar que se le pase por parámetro la cadena de búsqueda y llame al método `search` del api de Shodan.

    ```python
     class ShodanSearch:
    """ Clase para buscar en Shodan """
    def __init__(self,API_KEY):
        self.api = shodan.Shodan(API_KEY)
    
    def buscar(self,cadena):
        """ Busca en funcion la cadena pasada por parametro """
        try:
            # Buscamos lo de la cadena pasada como parametro
            resultado = self.api.search(str(cadena))
            return resultado
        except Exception as exception:
            print("Ha ocurrido un error: %s" % exception)
            resultado = []
            
        return resultado
    ```	

### Realizar búsquedas por un host determinado.

- En este ejemplo vemos que con el método `shodan.host()` es posible obtener información de una determinada ip como país, ciudad, proveedor de servicios, versiones de software, etc.

- En la clase que hemos utilizado anteriormente `ShodanSearch`, podríamos definir un método que se le pase por parámetro la IP del Host y llame al método host() de la API de Shodan.

    ```python
     def obtener_info_host(self,IP):
        """ Obtiene la info que pueda tener shodan sobre una IP """
        try:
            resultados = self.api.host(IP)
            return resultados
        except Exception as exception:
            print("Ha ocurrido un error: %s" % exception)
            resultados = []
        
        return resultados
    ```		
- La llamada a este método se podría hacer de esta manera:
    ```python
    resultados = shodan.obtener_info_host("8.8.8.8")
    for key, value in results.items():
        print(key, "-->", value)
    ```

- [Código completo clase ShodanSearch](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/4-ShodanSearch.py)

    - Buscar en Shodan por la cadena `apache`
        ```bash
        python3 4-ShodanSearch.py --search apache
        ```
    - Buscar en Shodan por la IP `8.8.8.8`
        ```bash
        python3 4-ShodanSearch.py --host 8.8.8.8    
        ```

    - El código anterior solicita información sobre la resolcuion de la IP `8.8.8.8` y almacena en la variable info.

    - El resultado de api.host() devuelve información sobre los servicios que ejecuta así como el proveedor de alojamiento.

    - Entre las propiedades que decuelce la llamada destacamos:
        - `data`: una lista de banners que proporcionan detalles sobre los servicios que tenían un puerto abierto en dicho servidor.
        - `ports`: una lista de puertos abiertos en el servidor.
        - `tags`: Shodan hace validación extra para algunos servicios/dispositivos y tiene etiquetas especiales para facilitar la identificación de ciertos tipos de dispositivos (por ejemplo, la etiqueta `ics` para identificar sistemas de constrol industrial).


### Obtener banners e información del servicio de shodan

- Objetivo: Obetener banners e información del servicio de shodan a partir de la información que devielve el APIREST y el método que obtiene información a partir de una IP.

- [Código para www.google.com](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/5-shodan_info_api_rest.py)

    ```
    # OUTPUT
    IP: 142.251.40.228
    Organization: Google LLC
    Operating System: None
    Port: 80
    Banner: HTTP/1.1 301 Moved Permanently
    Location: http://www.google.com/
    Content-Type: text/html; charset=UTF-8
    Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-UB563lK-eiPgYIIXw1aLiw' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
    Permissions-Policy: unload=()
    Date: Tue, 12 Nov 2024 14:40:47 GMT
    Expires: Thu, 12 Dec 2024 14:40:47 GMT
    Cache-Control: public, max-age=2592000
    Server: gws
    Content-Length: 219
    X-XSS-Protection: 0
    X-Frame-Options: SAMEORIGIN


    Port: 443
    Banner: HTTP/1.1 301 Moved Permanently
    Location: http://www.google.com/
    Content-Type: text/html; charset=UTF-8
    Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-up1XMSB4OaQaTmRquxKdUw' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
    Cross-Origin-Opener-Policy: same-origin-allow-popups; report-to="gws"
    Report-To: {"group":"gws","max_age":2592000,"endpoints":[{"url":"https://csp.withgoogle.com/csp/report-to/gws/other"}]}
    Permissions-Policy: unload=()
    Date: Tue, 12 Nov 2024 21:03:36 GMT
    Expires: Thu, 12 Dec 2024 21:03:36 GMT
    Cache-Control: public, max-age=2592000
    Server: gws
    Content-Length: 219
    X-XSS-Protection: 0
    X-Frame-Options: SAMEORIGIN
    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
    ```

    Los datos obtenidos de Shodan describen aspectos técnicos y públicos del servidor de Google, como:

    - `Dirección IP:` Pública y conocida, pertenece a Google LLC.
    - `Organización:` Google LLC, el propietario registrado de esa IP.
    - `Sistema operativo:` Información pública y básica del sistema operativo, en este caso "None".
    - `Puertos y banners:` Información sobre los servicios públicos que corren en el servidor, como los puertos 80 y 443 (HTTP y HTTPS), y sus cabeceras HTTP, incluyendo Location, Content-Type, Date, Cache-Control, Server, etc. Estas cabeceras no contienen datos privados; son configuraciones de red y seguridad accesibles para cualquier usuario de Internet que haga una solicitud al servidor.

### Utilizando Shodan para la obtención de información de un servidor FTP

- Shodan permite realizar una búsqueda de servidores que tengan un acceso FTP con usuario anónimo y se pueda acceder sin usuario y contraseña.

- Si realizamos la búsqueda con la cadena `port:21 Anonymous user logged in`, obtenemos aquellos servidores ftp que son vulnerable por permitir el acceso anónimo.

    - https://www.shodan.io/search?query=port%3A21+Anonymous+user+logged+in

- EL siguiente script permite obtener quellas direcciones IP de servidores que permiten el **acceso FTP de forma anónima**.

    - [Código](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/6-ftp_anonymous.py)

    ```python
    #!/usr/bin/env python

    import shodan
    import re

    sitios =[]
    shodanKeyString = '<API_KEY>'
    shodanApi = shodan.Shodan(shodanKeyString)

    resultados = shodanApi.search("port: 21 Anonymous user logged in")
    print("numero de hosts: " + str(len( resultados['matches'])))
    for resultado in resultados['matches']:
        if resultado['ip_str'] is not None:
            sitios.append(resultado['ip_str'])
            
    for sitio in sitios:
        print(sitio)
    ```


### Shodan eye

- Esta herramienta recopila toda la informaación sobre todos los dispositivos que están directamente conectados a Internet con las palabras clave especificadas. 

- Para su instalación y ejecución necesitamos bajarnos el código del siguiente repositorio: https://github.com/BullsEye0/shodan-eye

    ```bash
     pip3 install shodan
    git clone https://github.com/BullsEye0/shodan-eye shodaneye
    cd shodaneye
    python3 shodan-eye.py
    ```

## 3. Utilizando el módulo de Python-whois para obtener información de un servidor.

- Empezamos introducciendo el protocolo **`Whois`** que es el nombre del protocolo que se utiliza para preguntar a los servidores operados por registros regionales de internet y contienen información sobre cada recuros (dirección IP, nombre de dominio, etc.).

- Podemos utilizar el protocolo `Whois` para ver quién es el propietario registrado del nombre del dominio.

- El comando `whois` permite obtener información sobre un dominio específico o dirección IP.

    ```bash	
    whois google.com
    ```
    - Resultado:
        ```bash
        Domain Name: google.com
        Registrar: MarkMonitor Inc.
        Sponsoring Registrar IANA ID: 292
        Whois Server: whois.markmonitor.com
        ...
        ```

- La informacion `whois` de un nombre de dominio proporcona diversos detalles como registrador, propietario, fecha de registro, fecha de expiración, etc.

- Eñ comando whois soporta la búsqueda tando por dirección ip como por nombre de dominio.

- La información devuelta incluye direcciones físicas, direcciones de correo electrónico, nombres de dominio, nombre y número de teléfono, etc.

- También se muestran los servidores de nombres DNS de un dominio.

### Servicios `whois`

- Un analista podría usar esta herramienta para descubrir el proppietario del nombre de dominio y la información de contacto del proveedor de sercicios donde se aloja el dominio.

- Las consultas de whois pueden devolver información de historial de IP, fechas de caducidad del domino e incluso números de tetéfono que podrían utilizarse para ataques de inteligencía social.

- En internet podemos encontrar difrentes servicios de registro de dominios para obtener el detall de un dominio:

    - https://hackertarget.com/whois-lookup/
    - https://whois.domaintools.com/

- Entre los principales **casos de uso para un búsqueda de whois** son:
    - **Respuesta a incidentes e inteligencia de amenazas**: las ventajas de una búsqueda whois para aquellos que responden a un incidente de seguridad es identificar el ISP que posee una dirección IP particular. A partir de estas información, se puede contactar al propietario de dominio y avisar al rpoveedor de la presencia de cierto tráfico anómalo.

    - **Registros históricos de Whois que permiten que un analista busque detalles en los datos**: Por ejemplo, se pueden buscar datos de whois para encontrar una dirección de correo electrónico en varios dominios y determinar cuándo apareció por primera vez la dirección de correo electrónico en un determinado registro.

    - **Solución de problemas de red con Whois**: Especialistas de seguridad de redes que investigan una ruta a través de Internet puede ver si una red en particular está intoduciendo una latencia significativa. Mediante una búsqueda en un registro de whois, se puede determinar quién es el propeitario de la red en cuestión y ponerse en contacto con los responsables de la red.

### Obtener información de un dominio con el servicio `domaintools`

- Podemos utilizar el módulo `requests` y el servicio `domaintools` para obtener información de un dominio que estamos analizando, como la dirección IP, nombre de dominio, etc.

    ```python
    import requests
 
    domain = 'domaintools.com'
    url = 'https://api.domaintools.com/v1/'+domain+'/reverse-ip/?format=json'
    
    headers = {'User-Agent': 'wswp'}
    response = requests.get(url, headers=headers).json()['response']
    ```	

    ```python
    ip_addresses = response['ip_addresses'][0]
    print('IP address: ',ip_addresses['ip_address'])
    ```

    ```python	
    print('domain_count: ',ip_addresses['domain_count'])
    print('domain names: ',ip_addresses['domain_names'])
    ```

    - [Documentación oficial](https://www.domaintools.com/resources/api-documentation/)


### Extracción de información de un servidor web mediante la consulta de `whois`

- Extración de información de un servidor web mediante la consulta de registry de dominios `whois`.

- Para ello hacemos uso del módulo reques para realizar la petición a la API de whoapi.com utilizando para ellos el parámetro domain de consulta y personalizando las cabeceras que se envían al servidor.

- Para realizar la consulta es necesario obtener el apikey al registrarse en el servicio de whois.

    - https://whoapi.com/

    ```
    http://api.whoapi.com/?domain=<dominio>&r=whois&apikey=<mi_key>
    ```

    - [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/8-obtener_info_web.py)


### `Módulo python-whois`
- Enlaces de interés:
    - https://github.com/richardpenman/whois 
    - https://pypi.org/project/python-whois/

- Este módulo permite obtener información de un dominio o IP utilizando el protocolo Whois.

- Para utilizar el módulo se debe instalar el paquete `python-whois` con el siguiente comando:
    ```bash
    pip install python-whois
    ```

- Este método devuelve una estructura del tipo diccionario (clave-valor) que contiene la información de un dominio o IP.

    ```python
    >>> import whois
    >>> dominio = "www.python.org"
    >>> whois = whois.whois(dominio)
    >>> for key in whois.keys():
    >>>     print ("%s : %s \n" %(key, whois[key])
    ```

- En el siguiente script vemos un ejemplo completo donde pasamos por parámetroel dominio del cual queremos extraer información.

    - [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/9-informacion_dominio_whois.py)

        ```python
         #!/usr/bin/python

        import whois
        import sys

        if len(sys.argv) != 2:
            print("[-] uso python inforamcion_dominio.py <nombre_dominio>")
            sys.exit()

        whois = whois.whois(sys.argv[1])
        print(whois)
        for key,value in whois.items():
            print ("%s : %s \n" %(key,value))
        ```	

        ```bash
        python3 informacion_dominio_whois.py google.com
        ```

### `Modulo ipwhois`

- [Documentación oficial](https://ipwhois.readthedocs.io/en/latest/index.html)

- Otro de los módulos que podemos usar para obtener esta información es el módulo llamado `ipwhois`.

- La instalación de este módulo es muy sencilla, solo se debe instalar el paquete `ipwhois` con el siguiente comando:
    ```bash
    pip install ipwhois
    ```

- Por ejemplo, si queremos consultar la información de un determinado dominio, tenemos que convertir el nombre del dominio en dirección IP y posteriomente reealizar la consulta a través del método `lookup_whois()`.

- En el siguiente script vemos un ejemplo completo donde pasamos por parámtro el dominio del cual queremos extraer información.

    - [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/10-obtener_info_ip_whois.py)

        ```python
        #!/usr/bin/python

        import sys
        import socket

        from ipwhois import IPWhois

        if len(sys.argv) != 2:
            print("[-] uso python informacion_ip_whois.py <nombre_dominio>")
            sys.exit()

        dominio = sys.argv[1]
        direccion_ip = socket.gethostbyname(dominio)
        print('Direccion ip:',direccion_ip)

        whois = IPWhois(direccion_ip).lookup_whois()
        for key,value in whois.items():
            print(key,value)
        ```

        ```bash
        python3 informacion_ip_whois.py google.com
        ```


## 4. Introducción al módulo DNSPython para obtener información de servidores DNS.

### Extracción de información de servidores DNS

- La dirección IP s puede traducir en cadenas legibles por humanos llamadas nombres de dominio.

- DNS son las siglas de **Domain Name System**, es decir, el sistema de nombres de dominio.

- El protocolo DNS se utiliza para distintos propósitos, como:	
    
    - **Se emplea para asignar un rango de IPs a un único dominio**.
    - **Resolución de nombres**: Dado el nombre completo de un host, obtener su dominio IP.
    - **Resolución inversa de direcciones**: Es el mecanismo inverso al anterior. Consiste en, dada una dirección IP, obtener el dominio que la contiene.
    - **Resolución de servidores de correo**: Dado un nombre de dominio (por ejemplo gmail.com), obtener e servidor a través del cual debe realizarse la entrga del correo electrónico (por ejemplo, **gmail-smtp-in.l.google.com**).

- DNS también es un protocolo que los dispositivos usan para calcular a los servidores DNS con el objetivo de resolver nombres de host en direcciones IP(y viceversa).

- La herramienta `nslookup` viene con la mayoría de los sistemas Linux y Windows y nos permite realizar consulstas DNS desde la línea de comandos.

- Ejemplo:
    ```bash
    nslookup python.org
    ```
    ```
    nslookup python.org
    Server:         10.255.255.254
    Address:        10.255.255.254#53

    Non-authoritative answer:
    Name:   python.org
    Address: 151.101.0.223
    Name:   python.org
    Address: 151.101.64.223
    Name:   python.org
    Address: 151.101.192.223
    Name:   python.org
    Address: 151.101.128.223
    Name:   python.org
    Address: 2a04:4e42:400::223
    Name:   python.org
    Address: 2a04:4e42:600::223
    Name:   python.org
    Address: 2a04:4e42::223
    Name:   python.org
    Address: 2a04:4e42:200::223
    ```	

### Servicios DNS

- Los seres humanos recordamos mucho mejor lo snombres para relacionar objetos que secuencias largas de números.

- Para cualquiera es mucho más sencillo recordar el dominio google.com que la dirección IP 142.250.200.100.

- Además la dirección IP puede cambiar por movimientos en la infraestructura de red, mientras que el nombre de dominio no.

- Su funcionamiento se basa en el uso de un base de datos distribuida y jerarquizada en la que se almacenan nombres de dominio y direcciones IP, así como la capacidad de prestar servicios de localización de srvidores de correo.

- Los servidores DNS permiten la consulta de diferentes tipos de registros en los que se ingluyen servidores de correo, direciones IP, nombres de dominio, etc.

- Los servidores DNS se ubican en la capa de aplicación y se suelen utilizar en el puerto 53(UDP).

- Cuando un cliente envía un paquete DNS para realizar algún tipo de consulta, debe enviar el tpo de registro que desea consultar. Los más comunes son:
    - A: Dirección IPv4
    - AAAA: Dirección IPv6
    - MX: Servidor de correo
    - NS: Servidor de nombres
    - CNAME: Alias de dominio
    - TXT: Texto
    - PTR: Dirección IP inversa

### `Módulo dnspython`

- Python disponde del módulo `dnspython` que permite realizar consultas DNS desde Python.

- https://www.dnspython.org/
- https://github.com/rthalley/dnspython

- Este módulo permite el acceso tanto a alto nivel por medio de sonsultar a registros DNS como a nivel bajo permitiendo la manipulacion directa de zonas, mensajes, nombres y registros.

- Para instalar el módulo se debe ejecutar el siguiente comando:
    ```bash
    pip install dnspython
    ```

- La principal utilizad de `dnspython` con respecto a otras herramientas de consulta DNS, como `nslookup`, es que puede controlar el resultado de las consultas desde Python y luego esa información puede usarse para otros fines en el script.

- A la hora de hacer uso de este módulo los paquetes necesarios son:
    ```python
    import dns
    import dns.resolver
    ```

- La información que podemos obtener de un determinado dominio es:
    - Registros para servidores de correo
        - `ansMX = dns.resolver.query('dominio', 'MX')`
    - Registros para servidores de nombres
        - `ansNS = dns.resolver.query('dominio', 'NS')`
    - Registros para direcciones IPv4
        - `ansA = dns.resolver.query('dominio', 'A')`
    - Registros para direcciones IPv6
        - `ansAAAA = dns.resolver.query('dominio', 'AAAA')`
    - Registros para alias de dominio
        - `ansCNAME = dns.resolver.query('dominio', 'CNAME')`
    - Registros para texto
        - `ansTXT = dns.resolver.query('dominio', 'TXT')`
    - Registros para direcciones IP inversas
        - `ansPTR = dns.resolver.query('dominio', 'PTR')`

- En este ejemplo, estamos haciendo una consulta con respecto a la direccion IPv4 del dominio `python.org` con el submódulo `dns.resolver`.
    ```python
    import dns
    import dns.resolver
    
    respuestas = dns.resolver.query('python.org', 'A')
    for respuesta in respuestas:
        print('IP', respuesta.to_text())
    ```

    - [Más ejemplos de uso de `dnspython`](https://www.dnspython.org/examples.html)

### Determinar el destino de un registro MC y su preferencia

- Con el submódulo `dns.resolver` podemos acceder a la información almacenada en los registros de intercambio de correo de ExChange para ver qué host tienen prioridad al intercambiar correos electrónicos a través de internet.
    
    - [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/11-obtener_info_destino_mx.py)
    ```python
     import dns.resolver
    respuestas = dns.resolver.query('google.com', 'MX')
    for respuesta in respuestas:
        print('Host', respuesta.exchange, 'tiene una preferencia de ', respuesta.preference)
    ```
    ```	
    Host smtp.google.com. tiene una preferencia de 10
    ```

### Implementar un cliente consulta de registros DNS

- En este ejemplo práctico utilizaremos dnspython para ejeceutar consultar en varios tipos de registros DNS como IPv4, IPv6, servidores de nombres(NS) e intercambio de correo(MX).

- [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/12-registros_dns.py)

    ```bash
    # Ejecutar el script
    python registros_dns.py python.org
    ```


### Añadiendo tratamiento de expcepciones a la consulta DNS

- En este ejemplo práctico utilizamos dnspython para ejecutar las consultas del ejemplo anterior, con la direncia de que en este caso estamos realizando un tratamiento y en caso de que no se pueda obtener información para un tipo de registro concreto, informar al usuario que se ha producido un error.

- [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/13-registro_dns_excepciones.py)


### Extracción de información de un servidor DNS mediante el móduloDNSPython

- [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/14-dnspython.py)

### Otras operaciones con el módulo dnspython

- Con el módulo `dnspython` podemos comprobar si un dominio es subdominio de otro a través del metodo `dns.name.is_subdomain()`.
    ```python
    >>> import dns.resolver
    >>> dominio1 = dns.name.from_text('dominio1')
    >>> dominio2 = dns.name.from_text('dominio2')
    >>> dominio1.is_subdomain(dominio2)
    ```

- En el siguiente script utilizamos el método anterior para comprobar si un dominio es subdominio o superdominio de otros.

    - [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/15-dnspython_subdominio_superdominio.py)	

    ```python
     #!/usr/bin/env python

    import argparse
    import dns.name

    def main(dominio1, dominio2):
        dominio1 = dns.name.from_text(dominio1)
        dominio2 = dns.name.from_text(dominio2)
        print("dominio1 is subdomain of dominio2: ", dominio1.is_subdomain(dominio2))
        print("dominio1 is superdomain of dominio2: ", dominio1.is_superdomain(dominio2))

    if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Comprobar 2 dominios con dns Python')
        parser.add_argument('--dominio1', action="store", dest="dominio1",  default='www.python.org')
        parser.add_argument('--dominio2', action="store", dest="dominio2",  default='python.org')
        given_args = parser.parse_args()
        dominio1 = given_args.dominio1
        dominio2 = given_args.dominio2
        main (dominio1, dominio2)
    ```

    ```bash
     # Ejecutar el script
     python3 15-dnspython_subdominio_superdominio.py --dominio1 www.python.org --dominio2 python.org
     ```

    ```
    dominio1 is subdomain of dominio2: True
    dominio1 is superdomain of dominio2: False
    ```

- Obtener un nombre de dominio a partir de su dirección IP.
    ```python
    >>> import dns.reversename
    >>> dominio = dns.reversename.from_address('direccion_ip')
    ```	

- Obtener una dirección IP a partir de un nombre de dominio.
    ```python	
    >>> import dns.resolver
    >>> ip = dns.reversename.to_address('dominio')
    ```	

### Obtención de las direcciones IP a partir de una lista de nombres de dominio

- [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/16-dnspython_reversename.py)

    ```python
    # Importa la biblioteca `dns.resolver` para realizar consultas DNS.
    import dns.resolver

    # Lista de dominios para los que se quieren obtener las direcciones IP.
    dominios = ["google.com", "microsoft.com", "python.org"]

    # Itera sobre cada dominio en la lista.
    for dominio in dominios:
        # Imprime el dominio que se está consultando.
        print('Direcciones IP del dominio', dominio)
        
        # Realiza una consulta DNS para el registro A del dominio,
        # que nos proporciona las direcciones IP asociadas.
        direcciones = dns.resolver.resolve(dominio, "A")
        
        # Itera sobre cada dirección IP obtenida y la imprime.
        for direccion_ip in direcciones:
            print(direccion_ip)
    ```	

    ``` 
    # Output
    Direcciones IP del dominio google.com
    142.250.201.78
    Direcciones IP del dominio microsoft.com
    20.236.44.162
    20.112.250.133
    20.231.239.246
    20.76.201.171
    20.70.246.20
    Direcciones IP del dominio python.org
    151.101.192.223
    151.101.128.223
    151.101.0.223
    151.101.64.223
    ```


### Búsqueda inversa

- Si desea realizar una búsqueda inversa, debe usar el submódulo `dns.reversename` de la biblioteca `dnspython`.
    ```python
    >>> import dns.reversename
    >>> name = dns.reversename.from_address("ip_address")
    >>> print(dns.reversename.to_address(name))
    ```

- [Código de ejemplo](/Unidad_4_Recolección_de_informacion_de_servidores_con_Python/17-dnspython_busqueda_inverso.py)

    ```python
    # Importa la biblioteca `dns.reversename` para realizar consultas de DNS inversas.
    import dns.reversename

    # Convierte una dirección IP en un nombre DNS inverso.
    # En este caso, estamos usando la dirección IP "8.8.8.8".
    nombre = dns.reversename.from_address("8.8.8.8")

    # Imprime el nombre DNS inverso generado a partir de la dirección IP.
    print(nombre)

    # Convierte el nombre DNS inverso de vuelta a la dirección IP original.
    print(dns.reversename.to_address(nombre))
    ```

    ```
    # Output
    8.8.8.8.in-addr.arpa.
    8.8.8.8
    ```

### Servicios DNS - `Robtex`

- `Robtex` se trata de un servicio considerado la navaja suiza de internet.

- Permite obtener, sin dejar rastro alguno en el objetivo, consultas sobre dominios, subdominios, servidores DNS.

- Este tipo de consultas suelen categorizarse como footprinting activo, aunque, al realizarlo a através de este servicio, en realidad se lleva a cabo de manera pasiva.

- `Robtex` utiliza varias fuentes para recopilar información pública sobre números de IP, nombres de dominio, nombres de host, etc. Posteriormente indeza los datos en un BD y proporciona acceso gratuito a los mismos.

- El objetivo es conseguir la herramienta de búsqueda de DNS gratuita más rápida y completa en internet.

- Robtex proprociona una gran cantidad de información sobre el dominio. Por ejemplo, puedes ver aquellos dominios realacionas.

- Disponemos tambien de un API que devuelve los datos de geolocalización y de red de un direccion IP.

    ```
    Example query: https://freeapi.robtex.com/ipquery/199.19.54.1
    ```

- Podríamos utilizar el servicio dns-lookup para obtener más información sobre un dominio:
    - https://www.robtex.com/dns-lookup/

#### ¿Qué tipo de información porporciona Robtex?   

- **Búsqueda de DNS inversa**. Permite buscar un número de IP para averiguar qué nombres de host lo apuntan. Los registros DNS inversos funcionan no solo para la dirección IP, sino también para los registros MX (servidor de correo) y los registros NS (servidor de nombres).

- **Buscar un número de IP y obtener qué nombres de host lo apuntan**. Los registros DNS inversos funcionan no solo para la dirección IP, sino también para los registros MX (servidor de correo) y los registros NS (servidor de nombres).

- **Información Whois**. Permite realizar búsquedas para un dominio registrado en varias bases de datos de whois. En esta base de datos es posible encontrar información de contacto del registro de dominio junto con la fecha de registro y la fecha de vencimiento. Se trata de un protocolo TCP que permite realizar consultas a bases de datos. Entre los principales datos que se pueden obtener podemos destacar el propietario del dominio, la dirección IP, direcciones de correo, fechas de creación y actualización de dominios.

### `DNS-Lookup`

Un dominio tiene una cantidad de registros asociados, se puede consultar un servidor DNS para determinar la dirección IP del dominio principal (registro A), servidores de correo (registros MX), servidores DNS (servidores de nombres NS) y otros elementos como registros TXT.

El comando más común que se utiliza es `nslookup` que está disponible en muchos sistemas operativos, incluidos Windows y la mayoría de las distribuciones de Linux. Otra herramienta que se encuentra en sistemas basados en Linux es la herramienta `dig`. En general, esta es una herramienta más avanzada que tiene una serie de características que `nslookup` no posee.

Los siguientes **servicios web** permiten realizar una consulta del tipo dns-lookup:

#### Enlaces
- [Servicio DNS de hacker target](https://hackertarget.com/dns-lookup/)
- [API de hacker target](https://api.hackertarget.com/dnslookup/?q=google.com)



## 5. Resumen

### En esta unidad hemos aprendido:

- Utilizar **Shodan** para la obtención de información de un servidor así como los filtros que podemos usar para realizar consultas avanzadas.
- Obtener nuestra **API KEY** y usar los principales servicios de Shodan para realizar búsquedas específicas.
- Utilizar **Python** para realizar búsquedas en Shodan tanto a través de la API REST que proporciona como de forma programática utilizando el módulo de Shodan en Python. En el caso del acceso programático hemos aprendido a utilizar el método `shodan.search()` para realizar búsquedas por una determinada cadena.
- Utilizar el cliente de **Shodan** desde línea de comandos.
- Crear nuestro script **ShodanSearch** con el objetivo de realizar búsquedas por dirección IP utilizando el método `host()` y por cadena de búsqueda utilizando el método `search()`.
- Realizar búsquedas en Shodan para obtener servidores **FTP** que permiten el **acceso anónimo** a partir de la cadena de búsqueda `"port: 21 Anonymous user logged in"`.
- Utilizar el comando **whois** y el módulo **Python-whois** para obtener información de un servidor con el método `whois.whois(dominio)`.
- Obtener información de un dominio con el servicio **domaintools** utilizando el módulo **requests** y el parser **lxml.html**.
- Utilizar el comando **nslookup** y el módulo **DNSPython** para obtener información de **servidores DNS** a través de los diferentes registros para consultar direcciones IP, servidores de correo y servidores de nombres utilizando el método `dns.resolver.query('dominio', 'tipo_registro')`.
- Por último, hemos utilizado el módulo **dnspython** para realizar diferentes operaciones como validar un dominio, obtener nombre de dominio a partir de la dirección IP y viceversa utilizando el submódulo **dns.reversename**.

### FAQ

- `¿Qué es Shodan?`

    Shodan corresponde al acrónimo de Sentient Hyper Optimized Data Access Network. A diferencia de los motores de búsqueda tradicionales que rastrean el sitio web para mostrar los resultados, Shodan ayuda a encontrar los servicios vulnerables en un servidor web.

    Shodan es un motor de búsqueda para encontrar dispositivos específicos que funciona escaneando todo Internet y analizando los banners que devuelven los dispositivos. Con esa información, Shodan puede decirle cosas como qué servidor web es más popular, o cuántos servidores FTP anónimos existen en una ubicación determinada.

    Funciona escaneando todo Internet y analizando los banners que devuelven los dispositivos. Utilizando esa información, Shodan puede devolver datos como qué servidor web (y versión) es más popular, o cuántos servidores FTP anónimos existen en una ubicación determinada.

    Es de particular utilidad para la investigación de seguridad en Internet de las cosas, ya que actualmente podemos encontrar miles de millones de dispositivos conectados a Internet que tienen vulnerabilidades específicas que deben corregirse, y pueden identificarse rápidamente mediante su información de banner.


### Enlaces de interés

- https://shodan.readthedocs.io/en/latest/
- https://developer.shodan.io/
- https://pypi.org/project/python-whois/
- https://github.com/rthalley/dnspython
- https://chromewebstore.google.com/detail/shodan/jjalcfnidlmpjhdfepjhjbhnhkbgleap?utm_source=chrome-ntp-icon
- https://github.com/BullsEye0/shodan-eye
- https://ipwhois.readthedocs.io/en/latest/index.html
- https://www.dnspython.org/examples.html
- https://github.com/achillean/shodan-python
- https://account.shodan.io/

### Glosario

- `DNS: Domain Name Server`

    Servidor de nombre de dominios. Base de datos distribuida a través de Internet que permite resolver una IP a partir de un nombre dominio y viceversa. Sistema que almacena información relacionada con nombres de dominio en una base de datos distribuida en redes, como Internet.
- `FTP: File Transfer Protocol`

    Protocolo de transferencia de archivos. Por medio de programas que usan este protocolo, se permite la conexión entre dos computadoras y se pueden cargar y descargar archivos entre el cliente y el servidor.
- `Host`

    Servidor que nos provee de la información que requerimos para realizar algún procedimiento desde una aplicación cliente a la que tenemos acceso de diversas formas (SSH, FTP, www). Al igual que cualquier computadora conectada a Internet, debe tener una dirección o número IP y un nombre.
- `Servidor Web`

    Un servidor web es el programa y la computadora que lo ejecuta, que maneja los dominios y páginas web, interpretando lenguajes como html y php, entre otros. Computadora con un programa capaz de aceptar peticiones HTTP de clientes web y devolver respuestas HTTP (en general, páginas web). Ejemplos: Apache Tomcaty Microsoft IIS.
- `URL(Uniform Resource Locator)`

    Sistema de direccionamiento estándar de archivos y funciones en Internet, especialmente en la WWW. Una URL está formada por el protocolo de servicio, el nombre del servidor que contiene el recurso, la ruta de acceso al recurso y el recurso buscado.

































