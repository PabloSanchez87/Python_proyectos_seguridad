# Módulos para realizar peticiones con Python

## Objetivos

### Competencia
- Conocer los principales módulos disponibles tanto en la libería estándar como en forma de módulo para realizar peticiones a un sitio web y una APIREST.
- Protocolo HTTP y cómo podemos recuperar y manipular contenido web usando Python.
- Biblioteca `urllib` y paquete `requests` para realizar peticiones HTTP.
    - `requests`es una herramienta muy útil si queremos realizar solicitudes a los endpoins de la API con el objetivo de optimizar los flujos de trabajo HTTP.

### Resultados
- Comprender el protocolo HTTP y construir clientes HTTP en Python.
- Crear scripts en Python para consultar un sitio web con el módulo `urllib`.
- Crear scripts en Python para consultar una API REST con el módulo `requests`.
- Crear scripts en Python para obtener las cabeceras de la respuesta y la petición con el módulo `requests` de una API REST.

### Índice

1. Protocolo HTTP y creación de clientes HTTP en Python.
2. Contruyendo un cliente HTPP con urllib.request.
3. Crear un cliente HTTP con requests.
4. Resumen

---

## 1. Protocolo HTTP y creación de clientes HTTP en Python.

HTTP es un protocolo de capa de aplicación que básicamente consta de dos elementos: una solicitud realizada por el cliente, que solicita al servidor un recurso especifico especificado por una URL, y una respuesta, enviada por el servidor, que suministra el recurso que el cliente ha solicitado. 

- **Request**: es la petición que se envía al servidor.
- **Response**: es la respuesta que se recibe del servidor.

### Introducción al protocolo HTTP

- El protocolo HTTP es un protocolo de transferencia de hypertexto, **sin estado** que almacena la información que se intercambia entre cliente y servidor.

- Este protocolo define las reglas que deben de seguir clientes, proxies y servidores para el intercambio de información.

- Se trata de un protocolo sencillo, donde los clientes realizan peticiones y los servidores emiten las respuestas.

- Al ser un protocolo sin estado para poder almacern información relatica a una transaccion HTTP hay que recurrir a otras técnicas como:
    - cookies(valores almacenados en el lado del clientes) 
    - sesiones (espacios de memoria temporal reservada para almacernar información sobre una o varias transacciones HTTP en el lado del servidor)

#### RECUERDA
- `get`. Pide una representación del recurs especificado. Por seguridad no deberían ser usado por aplicaciones que causen efectos ya que transmite información a través de la URL agregando parámetros a la URL.

- `head`. Pide una respuesta idéntica a la que correspondería a una petición `get`, pero en la petición no devuelve el cuerpo de la respuesta. Esto es útil para poder recuperar los metadatos de los encabezados de repuesta, sin tener que transportar todo el contenido.

- `post`. Envía los datos para que sean procesados por el recurso identificado. Los datos se incluirán en el cuerpo de la petición. Esto puede resultar en la creación de un nuevo recurso o de las actualizaciones de los recursos existentes o ambas cosas.

### ´Módulo http.client´

- El protocolo HTTP emplea los sockets a nivel más bajo para establecer la conexión entre cliente y servidor.

- En Python tenemos la posibilidad de usar un módulo para crear un cliente HTTP. Los módulos que proporciona Python en biblioteca estándar son:
    - `http.client`: este módulo proporciona una clase `HTTPConnection` que se usa para realizar peticiones HTTP.
    - `http.request`: este módulo proporciona una función `urlopen` que se usa para realizar peticiones HTTP.

- También puedes encontrar paquetes como el de `requests` que proporciona una API para realizar peticiones HTTP.

#### Enlaces de interés
- [Documentación de http.client](https://docs.python.org/3/library/http.client.html)

#### La clase `HTTPConnection` es la que se usa para realizar peticiones HTTP. 

- Acepta un host y un puerto como parámetros.

- Una instancia de esta clase representa una transacción con un servidor HTTP. 

- Debe instanciarse pasando un identificador de servidor y un número de puerto adicional.

- Si no se especifica el número de puerto, el número de puerto de la cadena de identificación del servidor se extrae si tiene el formulario hosrt:puerto; de lo contrario, se utiliza el puerto predeterminado para el protocolo HTTP (80 para HTTP y 443 para HTTPS).

    ```python
    import http.client
    connection = http.client.HTTPConnection("www.google.com")
    connection.request("GET", "/")
    response = connection.getresponse()
    print('Respuesta:',response)
    print('Estado:', response.status, response.reason)
    datos = response.read()
    print(datos)
    ```

- [Código request-httplib.py](/Unidad_3_Módulos_para_realizar_peticones_con_Python/2-requet-httplib.py)

- [Código httplib_dominio.py](/Unidad_3_Módulos_para_realizar_peticones_con_Python/3-httplib_dominio.py)

    - Para ejecutar el script
        - python3 3-httplib_dominio.py -t www.google.com 
        - python3 3-httplib_dominio.py -t 142.250.200.100

        ```
        # Output

        301
        Location: http://www.google.com/
        Content-Type: text/html; charset=UTF-8
        Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-soYj_W8wJ_gbSWRzAPNScg' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
        Date: Wed, 13 Nov 2024 09:39:54 GMT
        Expires: Fri, 13 Dec 2024 09:39:54 GMT
        Cache-Control: public, max-age=2592000
        Server: gws
        Content-Length: 219
        X-XSS-Protection: 0
        X-Frame-Options: SAMEORIGIN


        [b'<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n', b'<TITLE>301 Moved</TITLE></HEAD><BODY>\n', b'<H1>301 Moved</H1>\n', b'The document has moved\n', b'<A HREF="http://www.google.com/">here</A>.\r\n', b'</BODY></HTML>\r\n']
        ``` 

## 2. Contruyendo un cliente HTPP con urllib.request.
En esta sección usaremos urllib para contruir clientes HTTP con este módulo.

- `urllib` puede leer datos de una URL usando varios protocolos, como HTTP, HTTPS, FTP o Gopher.

- Este módulo proporciona la funcion `urlpen` utilizada para cear un objeto similar a un archivo con el que puede leer desde la URL.

- Este objeto tiene métodos como:
    - `read()` se utiliza para leer el 'archivo' completo o la cantidad de bytes especificados como parámetros.
    - `readline()` permite leer un fichero para leer una línea.
    - `readlines()`permite leer todas las líneas y devuelve una lista con cada una de ellas.
    - `close()`
    
    que funcionan exactamente igual que en los objetos de un archivo, aunque en realidad estamos trabajando con un contenedor que nos abstrae del uso de un socket a bajo nivel.

- El `módulo urllib.request` permite el acceso a un recurso publico en Internet a través de su dirección
    - [Documentación oficial](https://docs.python.org/3/library/urllib.request.html#module-urllib.request)

- Ejemplos de funciones del `módulo urllib.request`:

    - Recuperar el contenido de una URL es un proceso sencillo cuando se hace usando `urllib`. 
        ```python
        >>> from urllib.request import urlopen
        >>> response = urlopen('http://www.python.org')
        >>> response
        <http.client.HTTPResponse object at 0x7fa3c53059b0>
        >>> response.readline()
        ```
        - Utilizamos urllib.request.urlopen() para enviar una petición y recicbir una respuesta para el recurso de 'http://www.python.org', en este caso una página HTML.
        - Luego imprimimos la primera línea HTML que recibimos con el método `readline()` del objete `response`.

    - [Ejemplo con el método urlopen()](/Unidad_3_Módulos_para_realizar_peticones_con_Python/4-url_basico.py)
        - Realizamos la petición a una página web usando el método `urlopen()`.
        - Cuando pasamos una URL al método, devolverá un objeto, podemos usar el atributo read() para obetener los datos de este objeto en un formato de cadena.
        - La función urlopen() tiene un parámetro de datos opcional con el cual enviar información de direcciones HTTP usando POST (los parámetros se envían en la solicitud misma), por ejemplo, para responder a un formulario.
        - Cuando trabajamos con el módulo `urllib`, tambien necesitamos administrar errores y el tipo de excepción `URLError`.
        - Si trabajamos con HTTP, también podemos encontrar errores en la subclase `HTTPError`, que se generan cuando el servidor devuelve un código de error HTTP, como el error 404 cuando no se encuentra un recurso.

---

- **`Objeto de respuesta`**
    - [Documentación](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse)
    - El objeto respuesta devuelve información sobre os datos de recursos solicitados y las propiedades y metadatos de la respuesta.
    - El siguiente código realiza una petición con urllib al dominio python.org:

        ```python
        >> response = urllib.request.urlopen('http://www.python.org')
        >>> response.read()
        b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">\n<html
        >>> response.read(100)
        ```	
    - En la salida vemos, que el método read() nos permite leer los datos de recursos solicitaos y devolver el número especificado de bytes.

---

- **`Códigos de estado HTTP`**
    - Las respuestas HTTP nos proporcionan una forma de verificar su estado de la respuesta a través de códigos de estado.
    - Podemos leer el código de estado de una respuesa usando su propiedad `status`.
    - Ejemplo: El valor **200** indica que la petición ha sido exitosa.
        ```python
        >>> response.status
        200
        ```
    - Los dódigos de estado se clasifican en categorías, como las siguientes:
        - 1xx: Información de protocolo
        - 2xx: Acción correcta
        - 3xx: Redirección
        - 4xx: Error del cliente
        - 5xx: Error del servidor

        Los códigos de estado nos ayudan a ver si nuestra respuesta fue exitosa o no. Cualquier código en el rango 200 indica un éxito, mientras que cualquier código en el rango 400 indica un error del cliente y el rango 500 indica un error del servidor.
        
    - LA IANA mantiene una lista oficial de códigos de estado HTTP: [https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml](https://www.iana.org/assignments/http-status-codes)

---

- **`Manejo de excepciones con urllib.request`**
    - Los códigos de estados siembre deben verificarse para que nuestro programa pueda responder de manera adecuada.
    - El paquete urllib nos ayuda a verificar los códigos de estado al generar un excepción si encuentra un problema.
    - Ejemplo:
        ```python
        #!/usr/bin/env python3

        import urllib.error

        from urllib.request import urlopen

        try:
            urlopen('https://www.ietf.org/rfc/rfc0.txt')
            
        except urllib.error.HTTPError as e:
            print('Exception', e)
            print('status', e.code)
            print('reason', e.reason)
            print('url', e.url)
        ```
        - Resultado:
            ```
            Exception HTTP Error 404: Not Found
            status 404
            reason Not Found
            url https://www.ietf.org/rfc/rfc0.txt
            ```
        - Hemos solicitado un documento rfc0.txt, que no existe. Entonces, el servidor devuelve un código 404, y urllib ha capturado esto y ha generado una excepcion del tipo **HTTPError**.
        - Puede ver que HTTPError proporciona atributos útiles con respecto a la petición realizada, como el código de estado, la razón, y la URL.

---

- **`Comprobación de cabeceras HTTP con urllib.request`**
    - Las peticiones HTTP constan de dor partes principales:
        - **Cabeceras**: Son las líneas de información que contienen metadatos específicos sobre la respuesta que devuelve el servidor y le dice al cliente cómo interpretar los datos. Con una simple llamada podemos verificar si las cabeceras de respuesta pueden propocionar información extra sobre el servidor web que está detras del dominio.
        - **Cuerpo**: Es el contenido de la respuesta que se encuentra después de las cabeceras.
    
    - La declaración `http_response.headers` proporciona la cabeceras de respuesta del servidor web. Antes de acceder a esta propiedad, es importante verificar si el código de respuesta es igual a 200.

    - Ejemplo:
        - [urllib_headers_basic.py](/Unidad_3_Módulos_para_realizar_peticones_con_Python/6-urllib_headers_basic.py)
            - Realizamos una petición a dominio que el usuario introduce y si el código de respuesta es 200 nostranos las cabeceras de la respuesta accediendo a la propiedad `http_response.headers`.

        - [urllib_headers_info.py](/Unidad_3_Módulos_para_realizar_peticones_con_Python/7-urllib_headers_info.py)
            - Otra forma de recuperar las cabeceras de la respuesta es mediante el uso del metodo `http_response.info()`, que devolverá un diccionario con todas las cabeceras de la respuesta.

        - [urllib_headers.py](/Unidad_3_Módulos_para_realizar_peticones_con_Python/8-urllib_headers.py)
            - Obtendremos las cabeceras del sitio a través de las cabeceras del objeto de respuesta. Usamos las propiedades:
                - `http_response.headers`: Para obtener todas las cabeceras de la respuesta.
                - `http_response.getheaders()`: Para obtener todas las cabeceras de la respuesta como pares clave-valor.

---                

- **` Personalización de cabeceras con urllib`**
    - Podemos personalizar las cabeceras que se envían para recuperar una versión específica de un sitio web.
    - Podemos usar la cabecera `Accept-Language` para especificar el idioma de la respuesta.
    - `User-Agent` es una cabecera que especifica el navegador y sistema operativo que realiza la petición.
    - Por defecto, **urllib** se identifica como `Python-urllib/<versión>` como podemos comprobaral ejecuatar en el interprete las siguientes instrucciones:
        ```python
        >>> from urllib.request import Request
        >>> from urllib.request import urlopen
        >>> request = Request('http://www.python.org')
        >>> urlopen(req)
        <http.client.HTTPResponse object at 0x034AEBF0>
        >>> request.get_header('User-agent')
        
        'Python-urllib/3.7'
        ```	
    - Si queremos identificarnos, por ejemplo, como un navegador Chrome, podríamos redifinir el parámetro de cabeceras al realizar la petición.
        - En este ejemplo, creamos la misma solicitud GET utilizando la clase `Request` pasando como parámetro una cabecera 'User-Agent' HTTP personalziada.
        - Para hacer uso de la funcionalidad que proporcionan las cabeceras, las añadimos antes de enviar la petición.
        - Pasos:
            1. Crear un objeto de solicitud (Request)
            2. Añadir cabeceras al objeto Request
            3. Llamar al método urlopen con el objeto Request

            ```python	
            import urllib.request
            url = "http://www.python.org"
            headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
            request = urllib.request.Request(url,headers=headers)
            response = urllib.request.urlopen(request)
            print('User-agent',request.get_header('User-agent'))
            if response.code == 200:
                print(response.headers)
            ```
            - En el código anterior, hemos usado user-agent correspondiente a un navegador Chrome para realizar la petición en un SO Linux.
                - [Obtener user agent de tu SO](https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome)

        - Con la clase Request, es posible crear cabeceras personalizadas para las peticiones HTTP. 
        - Para esto es necesario definir en el argumento de headers un diccionario con el formato clave-valor.
        - En el ejemplo anterior, creamos un diccionario con la cabecera 
            ```python	
            headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
            ```

---

- **`Obtener correos electrónicos de un URL con urllib.request`**
    - Podemos extraer correos electrónicos usando urllib y expresiones regulares.
        - [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/9-get_emails_from_url.py)

        ```python	
        import urllib.request
        import re
        web = input("Introduce una url(sin http://): ")
        #https://www.adrformacion.com/
        #obtener la respuesta
        response = urllib.request.Request('http://'+web)
        #obtener el contenido de la página a partir de la respuesta
        content = urllib.request.urlopen(response).read()
        # expression regular para detectar emails
        pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
        #obtener emails a partir de una expresión regular
        mails = re.findall(pattern,str(content))
        print(mails)
        ```

---

- **` Obtener URLs de un dominio con urllib.request`**
    - Podemos extraer URLs de un dominio usando urllib y expresiones regulares.
        - [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/10-get_urls_from_domain.py)

        ```python	
        #!/usr/bin/env python3

        from urllib.request import urlopen
        import re

        def download_page(url):
            return urlopen(url).read()

        def extract_links(page):
            link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
            return link_regex.findall(page)

        if __name__ == '__main__':
            target_url = 'http://www.adrformacion.com'
            content = download_page(target_url)
            links = extract_links(str(content))
            for link in links:
                print(link)
        ```

---

- **`Extraer imágenes usando urllin.request y re`**
    - Podemos extraer imágenes de un sitio web usando expresiones regulares encontrando las etiquetas `<img>` y extrayendo la URL de la imagen.
        - [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/11-get_images_from_url.py)

        ```python	
        #!/usr/bin/env python3

        from urllib.request import urlopen, urljoin
        import re

        def download_page(url):
            return urlopen(url).read()
            
        def extract_image_locations(page):
            img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']',
            re.IGNORECASE)
            return img_regex.findall(page)

        if __name__ == '__main__':
            target_url = 'http://www.adrformacion.com'
            content = download_page(target_url)
            image_locations = extract_image_locations(str(content))
            for src in image_locations:
                print(urljoin(target_url, src))
        ```

---

### `Módulo urllib3`
- Se trata de un módulo que extiende las funcionalidades de urllib permitiendo aprovechar algunas de las características más llamaticas del protocolo HTTP 1.1. de forma automática.

- Añade nuevas funcionalidades al método urllib, diferenciándose principalmente en su capacidad de soportar características avanzadas del protocolo HTTP 1.1, como la autenticación y la encriptación.

- [Documentación oficial](https://urllib3.readthedocs.io/en/latest/)

- Como característica más relevante, permite la reutilización de conexiones TCP para realziar múltiples peticiones y soporta la validación de certificados en conexiones HTTPS.

- Una características interesante es que le podemos indicar el número de conexiones que vamos a reservar para el pool de conexiones que estamos creando y utilizando la clase `PoolManager`.

    - Esta clase se encagar de gestionar las conexiones de forma persistente y reutilizar las coneziones HTTP que va creando gracias a un **pool de conexiones**.

- Para realizar una peticion con `urllib3` se emplea el método `request` de la clase `PoolManager` del objeto que hayamos creado.
    - El método `request`acepta por parámetro el tipo de petición (GET, POST) y la url del dominio.

        ```python
        >>> import urllib3
        >>> pool = urllib3.PoolManager(10)
        >>> response = pool.request('GET','url_dominio')
        ```	

    - La respuesta la obtenemos en el objeto `response` que nos devuelve y si accedemos a la prorpiedad `status` obtenemos el código de estado de la respuesta.
        ```python
        >>> response.status
        200
        ```
    
    - Ejemplo completo de petición con `urllib3`:
        - Realizamos una petición GET al dominio python.org.
        - Obtenemos las cabeceras de la respuesta en formato de diccionario.

            ```python
            import urllib3
            pool = urllib3.PoolManager(10)
            response = pool.request('GET','http://www.python.org')
            print(response.status)
            print("Keys\n-------------")
            print(response.headers.keys())
            print("Values\n-------------")
            print(response.headers.values())
            for header,value in response.headers.items():
                print(header + ":" + value)
            ```
            - Obtenemos como resultado el código de estado de la respuesta y las cabeceras de la respuesta.

- [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/12-get_headers_urllib3.py)

---

## 3. Crear un cliente HTTP con requests.
- Poder interactuar con una API RESTful basadas en HTTP es una tarea cada vez más común en proyectos en cualquier lenguaje de programación.

- En Python, también tenemos la opción de interactuar con una API REST de una manera simple con el módulo `requests`.

### Introducción al módulo requests
```bash
pip install requests
```
- [Documentación oficial](http://docs.python-requests.org/)

- Básicamente, `requests` es un contenedor de urllib junto con otros módulos de Python para proporcionarnos métodos con los cuales realizar peticiones a un sitio web o a una API REST. 

- Contamos con los métodos:
    - `get`: para realizar peticiones GET.
    - `post`: para realizar peticiones POST.
    - `put`: para realizar peticiones PUT.
    - `patch`: para realizar peticiones PATCH.
    - `delete`: para realizar peticiones DELETE.

    que son los métodos disponiblespara comunicarse con una API RESTful.

    ```python
    import requests
    response = requests.get('https://www.python.org')
    print(response.status_code)
    print(response.text)
    ```

### Comprobar una respuesta de una petición

- El método `requests.get` nos devuelve un objeto `response` que contiene la respuesta de la petición.

- En este objeto encontrará toda la información correspondiente a la respuesta.

- Principales propiedades y métodos que ofrece el objeto `response`:
    - `response.status_code`: código HTTP devuelto por el servidor.
    - `response.content`: contenido de la respuesta.
    - `response.json()`: devuelve el contenido de la respuesta como un objeto JSON.
        - Este método serializa la cadena y devuelve una estructura de diccionario que representa el objeto JSON.
        - En caso de no recibir un objeto JSON, el método devolvería una excepción que podríamos controlar.

    ```python
    >>> response.status_code
    200

    >>> response.reason
    'OK'
    >>> response.url
    'http://www.python.org'
    >>> response.headers['content-type']
    'text/html; charset=utf-8'
    ```	

    - También podemos acceder a las propiedades de las cabeceras a traves del objeto de respuesta donde podemos ver que el `user-agent` corresponde a la versión de la librería requests que estamos usando.

        ```python	
        >>> response.request.headers
        {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
        ```

### Obtener el fichero robots.txt de un dominio

- Podemos obtener el fichero robots.txt de un dominio con una simple petición HTTP GET.

- [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/13-leer_web_robots.py)

    - Para ejecutar el script
        ```bash
        python3 13-leer_web_robots.py http://www.python.org
        ```

        ```
        # Directions for robots.  See this URL:
        # http://www.robotstxt.org/robotstxt.html
        # for a description of the file format.


        User-agent: HTTrack
        User-agent: puf
        User-agent: MSIECrawler
        Disallow: /


        # The Krugle web crawler (though based on Nutch) is OK.
        User-agent: Krugle
        Allow: /
        Disallow: /~guido/orlijn/
        Disallow: /webstats/


        # No one should be crawling us with Nutch.
        User-agent: Nutch
        Disallow: /


        # Hide old versions of the documentation and various large sets of files.
        User-agent: *
        Disallow: /~guido/orlijn/
        Disallow: /webstats/
        ```

### Obtener número de palabras de un fichero con el módulo requests
1. Escribir una función que recibe por parámetro una URL de un fichero de texto y devuelve el número de palabras que contiene.
    - Parámetros:
        - url: Es una cadena con la URL del archivo de texto.
    - Devuelve:
        - El número de palabras que contiene el archivo de texto dado por la URL.
2. Pasos a seguir:
    - importar requests
    - definir función y realziar la peticón con el módulo requests, añadiendo también un try/except para manejar excepciones.
    - Obtener el número de palabras del contenido de la respuesta.

    - Ejemplo de url con un archivo de texto:
        - https://www.gutenberg.org/cache/epub/2000/pg2000.txt


- [Código de ejemplo solucionado](/Unidad_3_Módulos_para_realizar_peticones_con_Python/14-leer_url_resquests.py)


### Obtener cabeceras con el módulo requests
- Obtener cabeceras del dominio python.org

    - [Código](/Unidad_3_Módulos_para_realizar_peticones_con_Python/15-get_headers_requests.py)

    ```python	
    import requests

    response = requests.get("http://www.python.org")

    print(response.content)

    print("Status code: "+str(response.status_code))

    print("Cabeceras de respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
    
    print("Cabeceras de la peticion:")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
    ```	

- La instrucción `response.headers` proporciona las cabeceras de la respuesta del servidor. Básicamente es un diccionario con claves y valores, y con el método `items()` se puede iterar sobre ellos.

- Al ejecutar el script, podemos resaltar la presencia de python-resquest en la cabecera de respuesta.

    ```
    Cabeceras de la peticion:
    User-Agent --> python-requests/2.23.0
    Accept-Encoding --> gzip, deflate
    Accept --> */*
    Connection --> keep-alive
    ```

- De la misma forma, podríamos obtener solo las claves con el método `keys()`.

    - [Código](/Unidad_3_Módulos_para_realizar_peticones_con_Python/16-get_headers_keys.py)

    ```python
     import requests

    import requests
    if __name__ == "__main__":
        response = requests.get("http://www.python.org")
        for header in response.headers.keys():
            print(header + ":" + response.headers[header])
    ```

### Ventajas del módulo requests

- Facilita el uso de peticiones HTTP en Python en comparacion con urllib.

- A menos que tenga qun requisito especial, se recomienda usar requests.

- Ventajas más destacadas:

    - Biblioteca enfocada en la creacion de clientes HTTP completamente funcionales.

    - Soporta todos los métodos y características definidos en la especificación HTTP.
    - Es `Pythonic`, es decir, está completamente escrito en Python y todas las operaciones se realzian de manera simple y directa.
    - Tareas como la integración con sercicios web, la creación de un pool de coneciones HTTP, codificación de datos POST en formularios y el manejo de cookier se manejan automáticamente.
    - Se trata de una librería que implementa las funcionalidades de urllib3 y las extiende.

### Realizar peticiones GET a una API REST

- Para probar la realizar peticiones con este módulo podríamos usar el servcicio http://httpbin.org/, ejecutando cada tipo de petición por separado.

- En todos los casos, el código a ejecutar para obtener el resultado deseado será el mismo, lo único que cambiará será el topo e petición y los datos que se envían al servidor.

- https://httpbin.org ofrece un servicio que le permite probar las solicitudes REST a través de puntos finales (endpoints) predefinidos utilizando peticiones GET, POST, PATCH, PUT y DELETE.

    - [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/17-test_api_rest_get.py)

    ```python
    import requests,json

    response = requests.get("http://httpbin.org/get",timeout=5)

    print("Código de estado HTTP: " + str(response.status_code))

    print(response.headers)

    if response.status_code == 200:
        results = response.json()
        for result in results.items():
            print(result)
        print("Cabeceras de la respuesta: ")
        for header, value in response.headers.items():
            print(header, '-->', value)
        print("Cabeceras de la petición : ")
        for header, value in response.request.headers.items():
            print(header, '-->', value)
        print("Server:" + response.headers['server'])
    else:
        print("Error code %s" % response.status_code)
    ```


### Realizar peticiones POST a una API REST

- Cuando queremos realizar una peticion POST parte de la información que vamos a enviar al servidor se pasa a través del atributo de datos a través de una estructura de diccionario.

- El método de publicación POST requiere un campo adicional llamado `data`, en el que enviamos un diccionario con todos los elementos que enviaremos al servidor.

- Ejemplo, vamos a simular el envío de un formulario HTML a través de una solicitud POST, tal como lo hacen los navegadores web cuando enviamos un formulario.

    - Los datos del formulario siempre se envían en un formato de diccionario clave-valor
    - El método POST está disponible en el servicio REST de httpbin.org

- En el siguiente código, definimos un diccionario de datos que estamos utilizando con el método de publicación para pasar datos en el cuerpo de la petición.

    ```python	
     >>> data_dictionary = {"id": "0123456789"}
    >>> url = "http://httpbin.org/post"
    >>> response = requests.post(url, data=data_dictionary)
    ```

- Hay casos en los que el servidor requiere que la solicitud contenga cabeceras que indiquen que nos estamos comunicando con el formato JSON.
    - Para esos casos, podemos añadir nuestras propias cabeceras o modificar las existentes con el método `headers`.

    - [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/18-test_api_rest_post.py)
    ```python	
        #!/usr/bin/env python3

    import requests

    data_dictionary = {"id": "0123456789"}
    headers = {"Content-Type" :"application/json","Accept":"application/json"}
    response = requests.post("http://httpbin.org/post",data=data_dictionary,headers=headers)

    print("HTTP Status Code: " + str(response.status_code))

    if response.status_code == 200:
        print(response.text)
    ```	
    - En el script anterior, además de utilizar el método `post`, habría que pasar los datos que desea enviar al servidor como parámetro en el atributo `data`.
    - En la respuesta vemos cómo se envía el ID en el objeto del formulario.
    - Otras de las acciones que podemos hacer con el método POST con el módulo requests son:
        - Modificar las cabeceras (header) de la petición enviando información adicional.
        - En la respuesta podemos ver que la cabecera que hemos definido se añade jusnto con las definidas por defecto.
        
        ```python	
        >>> headers = {'user-agent': 'my-user-agent-header/v1.0'}
        >>> response = requests.post("http://httpbin.org/post",data=datos,headers=headers)
        ```
        - De esta forma, estamos cambiando la cabecera de user-agent dentro de las cabeceras de la petición.

### Ejercicio: Obtener cabeceras de la petición y de la respuesta de la llamada a una API REST

- [Código con la solución](/Unidad_3_Módulos_para_realizar_peticones_con_Python/19-test_api_rest_get_headers.py)

```python	
#!/usr/bin/env python3

# Importamos el módulo requests para realizar peticiones HTTP
import requests

# Definimos un diccionario con los datos que se enviarán en la petición POST
data_dictionary = {"id": "0123456789"}

# Especificamos las cabeceras para la petición: tipo de contenido y lo que aceptamos como respuesta
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Realizamos una petición POST a la URL especificada, enviando los datos y cabeceras definidas
response = requests.post("http://httpbin.org/post", data=data_dictionary, headers=headers)

# Imprimimos el código de estado HTTP de la respuesta
print("HTTP Status Code: " + str(response.status_code))

# Verificamos si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprimimos el cuerpo de la respuesta en formato de texto
    print(response.text)
    
    # Imprimimos nuevamente el código de estado
    print("Status code: " + str(response.status_code))

    # Imprimimos las cabeceras de la respuesta
    print("Cabeceras de respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
  
    # Imprimimos las cabeceras de la petición enviada
    print("Cabeceras de la peticion: ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
```	

### Realizar peticiones mediante un proxy

- Una caracterñistica interesante que ofrece el módulo de requests es la posiblidad de **realizar peticiones mediante un proxy** o máquina intermedia entre nuestra red interna y la red externa.

- Un proxy se define de la siguiente manera:
    ```python
    proxies = {
        'protocolo': 'direccion_ip:puerto',
        ...,
    }
    ```
    
    ```python
    proxies = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080'
    }
    ```

- Para realizar una petición a través del proxy, se utiliza el atributo proxies del método get:
    ```python
    response = requests.get(url, headers=headers, proxies=proxies)
    ```

- El objeto proxy debe pasarse en forma de diccionario, es decir, debe crear previamente un objeto de tipo diccionario donde especificamos el protocolo junto con la direccion IP y el puerto donde escuchará el proxy.

    ```python	
     import requests
    http_proxy = "http://<direccion_ip>:<puerto>"
    proxy_dictionary = { "http" : http_proxy}
    requests.get("http://dominio.org", proxies=proxy_dictionary)
    ```

### Gestionar excepciones con requests

- Los errores en el módulo requests se manejan de manera diferente a otros módulos.

- El siguiente ejemplo genera un error 404 que indica que no puede encontrar el recurso solicitado debido a que el dominio no existe.
    ```python
    >> response = requests.get('http://www.google.com/pagenotexists')
    >>> response.status_code
    404
    ```

- En este caso, el módulo devuelve un error 404. 
- Para ver la excepción generada internamente, podemos usar el método `raise_for_status()`.

    ```python
    >>> response.raise_for_status()
    requests.exceptions.HTTPError: 404 Client Error
    ```

- EN el caso de realizar una petición a un host que no existe, y una vez que se ha producido el tiempo de espera, obtenemos un excepción `ConnectionError`.

    ```python	
    >>> response = requests.get('http://url_not_exists')

    requests.exceptions.ConnectionError: HTTPConnectionPool(host='url_not_exists', port=80): Max retries exceeded with url: 
    / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f6ecaddd760>: Failed to establish a new connection: 
    [Errno -2] Name or service not known'))
    ```

#### Ejemplo script para tratar excepciones
- Usaremos el módulo `requests` para realizar 3 peticiones:
    - La primera es una url correcta
    - La segunda es un url incorrecta
    - La tercera provoca una excepción que podríamos controlar con un `try/except`.

- [Código de ejemplo](/Unidad_3_Módulos_para_realizar_peticones_con_Python/20-test_requests_exceptions.py)

```python	
import requests

url_ok = "http://www.python.org"
url_error  = "http://www.python.org/incorrecta"
url_exception  = "http://url_not_exists"

headers  = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

response = requests.get(url_ok,headers=headers)

if response.status_code == 200:
    print(response.content)
else:
    print("Error al conectar %s (%d)" % (url_ok,response.status_code))
    
response = requests.get(url_error,headers=headers)
if response.status_code == 200:
    print(response.content)
else:
    #print(response.raise_for_status())
    print("Error al conectar %s (%d)" % (url_error,response.status_code))
    
try:
    response = requests.get(url_exception,headers=headers)
except Exception as exception:
    print("Error al conectar %s (%s)" % (url_exception,exception))
```

- En la salida del script, vemos como en primera instancia obtenemos el contenido de la respuesta de la petición correcta y en segunda instancia vemos las 2 peticion que dan error de conexión.

    ```
    Error al conectar http://www.python.org/incorrecta (404)

    Error al conectar http://url_not_exists (HTTPConnectionPool(host='url_not_exists', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f80e6a33dc0>: Failed to establish a new connection: [Errno -2] Name or service not known')))
    ```


## 4. Resumen

- Establecer la conexión con un host con módulo `http.client` utilizando la clase `HTTPConnection`.

- Establecer la conexión con un host con módulo `requests` utilizando el método `urlopen()`, incluyendo la obtención del código de estado, cabeceras  de la respuesta y la petición a partir el objeto de respuestas `response`.

- Obtener información de las cabeceras de la respuesta y de la petición de diferentes formas como utilizando los métodos `info()` y `getheaders()` del objeto de respuesta.

- Personalizar las cabeceras que se envían en la petición a través del parámetro headers `urllib.request.Request(url, data=data_dictionary, headers=headers).`

- Extraer información de un página web como enlaces e imágenes utilizando el **módulo re para expresiones regulares.**

- Establecer la conexión con un host con el módulo `urllib3` utilizando la clase `PoolManager`.

- Establecer la conexión con un dominio con módulo `requests` utilizando el método `get()`, incluyendo la obtención del código de estado, cabeceras de la respuesta y la petición con el objeto de respuesta `response`.

- Realiziar una petición a una API Rest utilizando requests a través de los métodos `get()` y `post()`.

### FAQ

- `¿Que es el user-agent?`

    Es un encabezado que se utiliza para identificar el navegador y el sistema operativo que estamos utilizando para realizar peticiones a un determinado dominio. Por defecto, urllib se identifica como "Python-urllib / version"; si queremos identificarnos, por ejemplo, como un navegador Chrome, podríamos redifinir el parámetro de cabeceras al realizar la petición.

- `¿qué son las cabeceras de una petición?`

    Las cabeceras son las líneas de información que contienen metadatos específicos sobre la respuesta que devuelve el servidor y le dice al cliente cómo interpretarla. Con una simple llamada podemos verificar si las cabeceras de respuesta pueden proporcionar información extra sobre el servidor web que está detrás de un dominio.

### Enlaces de interés

- https://docs.python.org/3/library/urllib.request.html#module-urllib.request

- https://requests.readthedocs.io/en/latest/

- https://docs.python.org/3/library/http.client.html

- https://es.wikipedia.org/wiki/Anexo:Cabeceras_HTTP

- https://urllib3.readthedocs.io/en/latest/

- https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml

### Glosario

- `User-agent`

    Es un encabezado que se utiliza para identificar el navegador y el sistema operativo que estamos utilizando para realizar peticiones a un determinado dominio.