# Extracción de metadatos con Python

## Objetivos

### Competencia
- Conocer los principales módulos disponibles en Python con el objetivo de automatizar la extración de información del sitio web.
- Si queremos extraer el contenido de una página web automatizando la extracción de información, muchas veces nos encontramos con que la páguina web no ofrece ninguna API para obtener los datos que necesitas y es necesario recurrir a técnicas de scraping para recuperar datos de un web de forma automática.
- Algunas de la herramientas más pontentes las podemos encontrar en Python, entre las que podemos destacar:
    - `BeautifulSoup`: Permite extraer información de páginas web.
    - `Scrapy`: Permite automatizar el proceso de scraping de páginas web.

### Resultados
- Analizar los principales parsers que disponemos en Python para recuoerar informacion de contenidos HTML de un sitio web.
- Comprender las diferentes técnicas que permiten obtener información de forma programática con Python a partir del módulo `BeautifulSoup`.
- Crear scripts en Python para automotizar el proceso de extracción de enlaces, documentos e imágenes con BeutifulSoup.

- Conoceremos `Scrapy` como framework para extraer información de sitios web de forma automática mediante la creación de `spiders`
- `Scrapy` también permite exportar los datos extrídos en diferentes formatos como CSV, XML y Json con el objeto de analizar estos datos posteriormente.


### Contexto
Si queremos extraer el contenido de una páguina wuen automatizando la extración de infgormación, muchas veces nos encontramos con que la páquina web no ofrece una API para obtener los datos que necesitas es es necesario recurrir a técnicas de scraping para recuperar datos de una web de forma automática. Algunas de las herramientas más populares las podemos encontrar en Python, entre las que podemos destacar:
- `BeautifulSoup`: Permite extraer información de páginas web.
- `Scrapy`: Permite automatizar el proceso de scraping de páginas web.


### Índice

1. Extración de contenido web con Python
2. Extraer contenido y etiquetas con `BeautifulSoup`	
3. 

---

## 1. Extración de contenido web con Python

Entre las técnicas que disponemos para extraer contenido web podemos destacar:

- **`Screen scraping`**: Técnica que permite obtener información moviéndote por la pantalla, por ejemplo, registrando los click del usuario.

- **`Web scraping`**: Trata de obtener la información de un recurso como por ejemplo de una páguina web en HTML y procesa esa información para extraer datos relevantes.

- **`Report minging`**: Técnica que también pretende obtener información, pero en este caso a partide de un archivo (HTML, RDF, VSC, etc.). Con esta aproximacion de definición podemos crear un mecanismo simpple y rápido sin necesidad de escribir una API y como característica principal podemos indicar que el sistema no neceista una conexión ya que al trabajar a partir de un fichero es posible extraer la información de forma offline y sin necesidad de utilizar una API.

- **`Spider`**: Los spiders (crawlers/arañas) son scripts o programas que siguen unas reglas para moverse por un sitio web y tienen como objetivo recolectar información imitando la interacción que realizaría un usuario con la web. La idea es que sea solo necesario escribir las reglas para extraer los datos que nos interesen y dejar que el spyder rastree todo el sitio web en busca de enlaces..

Nos centraremos en la técnica de `web scraping`que permite la recolección o extracción de datos de páginas web de forma automática. Es un campo muy activo y en continuo desarrollo que comparte objetos con la web semántica, el procesamiento de texto automático, inteligencia artificial e interacción humano-computador.

El `web scraping` es una técnica que nos permite la extración de información de sitios webm transofmando datos no estructurados como los datos en formato HTML en daos estructurados.

![alt text](/resources/webscraping.png)

- En esta unidad revisaremos el módulo `lxml` con los parses `xml`, `html` y el módulo `BeautifulSoup`.

- Complementamos el uso de estos módulos con `requests` para realizar peticiones y descargar el código HTML.

    - Por ejemplo, **BeutifulSoup** recibirá el contenido de la respuesta con el objetivo de analizar el código HTML del sitio web y extrar información de interés.

### `Parsers XML y HTML` 

- Dentro del ecosistema de Python encontramos diferentes módulos que nos puedes ayudar a parsear un documento que se encuentra en formato xml y html-

- El `módulo lxml` es un módulo que uno las librerías `libxml2` para análisis de documentos XML y `libxslt`. Características de este módulo son:

    - Soporte para documentos XML y HTML.
    - Dispone de una API basada en **`ElementTree`** que permite crear, leer, modificar y borrar elementos XML.
    - Soporte para seleccionar elemento del documento mediantes expresiones XPath.
    - https://lxml.de/

    - La instalación de este módulo se realiza mediante el siguiente comando:
        ```bash
        pip install lxml
        ```

- En este ejemplo vamos a hacer uso del módulo `lxml.etree` que se trta de un submódulo dentro de la librería `lxml` , que proporciona métodos como XPath(), que soporta expresiones utilizando sintaxis selectores de XPath.
    - Vemos el uso del parser lxml para leer un fichero html y extraer el texto de la etiqueta title del documento html a través de una expresión XPath.

        - [Código de ejemplo](/Unidad_6_Webscraping_con_Python/2-obtener_texto_xpath.py)

        ```python
        #!/usr/bin/env python3

        import re
        import requests

        from lxml import etree

        respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

        parser = etree.HTML(respuesta.text)

        resultado = etree.tostring(parser,pretty_print=True, method="html")
        #print(resultado)

        obtener_texto_xpath = etree.XPath("//title/text()", smart_strings=False)
        texto = obtener_texto_xpath(parser)[0]
        print(texto)
        ```

#### `Submódulo lxml.html`
- https://lxml.de/lxmlhtml.html

- Ejemplo realizando una extracción de datos de un documento HTML.

    - [Código de ejemplo](/Unidad_6_Webscraping_con_Python/3-lxml_html.py)

    ```python
    #!/usr/bin/env python3

    import re
    import requests

    from lxml import etree

    respuesta = requests.get('https://www.debian.org/releases/stable/index.en.html')

    parser = etree.HTML(respuesta.text)

    resultado = etree.tostring(parser, pretty_print=True, method="html")
    #print(resultado)

    obtener_texto_xpath = etree.XPath("//title/text()", smart_strings=False)
    ```

#### Extraer etiquetas de un sitio web con el módulo `lxml`

- Antes de comenzar a analizar el código HTML, necesitamos extraer el contenido para analizarlo.

- En este ejemplo vamos a obtener la version y el nombre en clave de la última versión estable de Debian del sitio web de Debian.

    - Link: https://www.debian.org/releases/stable/index.en.html

    - La información que queremos se muesta en el título de la página y en el primer párrafo.

    - Primero lo que tenemos que hacer es descargar la página con el módulo `requests`:

        ```python
        import requests
        response = requests.get('https://www.debian.org/releases/stable/index.en.html')
        ```

    - Posteriormente, analizamos el xódigo fuente en un árbol ElementTree. Esto es lo mismo que analziar el XML con ElementTree de la biblioteca estándar, excepto que aquí usaremos el parser HTML disponible en lxml.
        ```python
        from lxml import html
        root = HTML(response.content)
        ```

    - La función HTML() es un acceso directo que lee el código HTML que se le pasa y produce un árbol XML. Tenga en cuenta que estamos pasando `response.content` y no `response.text` El módulo lxml produce mejores resultados cuando utiliza la respuesta sin procesar.

    - La implementación de ElementTree de la bibliteca lxml ha sido diseñada para ser 100% compatible con la biblioteca estándar, por lo que podemos comenzar a explotar el documento de la misma manera que lo hicimos con XML. Por ejemplo, podemos obtener las etiquetas raíz que se encuentran en un documento HTML.

        ```python
        >>> [e.tag for e in root]
        ['head', 'body']
        ```

    - Si nos interesa el contenido del texto del elemento `<title&gt;` del documento html, podríamos hacerlo de la siguiente manera:

        ```python
        >>> root.find('head').find('title').text
        'Debian --Debian "stretch" Release Information'


#### Obtener formularios de un sitio web

- En este ejemplo realizamos una petición al sitio https://www.w3schools.com/html/html_forms.asp y obtenemos el primer formulario que se utiliza en la página.

Para ello, realizamos una solicitud HTTP con requests y luego analizamos el contenido HTML usando lxml. Accedemos al objeto forms que se encuentra dentro del árbol DOM de la página.

    - [Código de ejemplo](/Unidad_6_Webscraping_con_Python/4-lxml_forms.py)

    ```python
    #!/usr/bin/env python3

    from lxml.html import fromstring, tostring
    import requests

    # Descargar el contenido de la página con requests
    url = 'https://www.w3schools.com/html/html_forms.asp'
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Analizar el contenido HTML
        page = fromstring(response.text)

        # Obtener el primer formulario de la página
        form = page.forms[0]
        print("Primer formulario encontrado:")
        print(tostring(form, pretty_print=True).decode('utf-8'))
    else:
        print(f"Error al acceder a {url}: Código {response.status_code}")

    ```

- Descripción del proceso:
    - Realizamos la solicitud HTTP: Usamos la biblioteca requests para descargar el contenido de la página web.
    - Analizamos el HTML: Convertimos el contenido en un árbol DOM utilizando fromstring de lxml.
    - Accedemos al formulario: Usamos la propiedad forms del árbol DOM para obtener el primer formulario de la página.
    - Mostramos el formulario: Imprimimos el HTML del formulario con formato legible usando tostring.

### `Expresiones XPath`

- Con el objetivo de optimizar la comprobación de los elementos, necesitamos usar XPath, que es un lenguaje de consulta que se desarrolló espcíficamente para XML y es compatible con el módulo `lxml`.

- Para comenzar con XPath, use el shell de Python de la última seccción y hago lo siguiente:

    ```python
    >>> root.xpath('body')
    [<Element body at 0x4477530>]
    ```

- Esto es la forma más simple de una expresion XPath; lo que hace es buscar hijos del elemento actual que tienen nombres de etiquetas que conincden con la etiqueta especificada.

- El elemento actual es el que llamamos xpath(), en este caso, root.

- El elemento raíz es el elemento `<html>` de nivel superior en el que el documento HTML, por lo que el elemento devuelto es el elemento `<body>`.

- Las expresiones XPath pueden contener múltiples niveles de elementos donde las búsquedas comienzan desde el nodo en el que se realiza la llamad xpath().

- Por ejemplo, podemos usar expresiones XPath para encontrar solo los elementos secundarios `<div>` densot del elemento `<body>`:

    ```python
    >>> root.xpath('//body//div')
    [<Element div at 0x4477530>, <Element div at 0x4477530>, <Element div at 0x4477530>, <Element div at 0x4477530>]
    ```

- La verdadera potencia de XPath está en que podemos aplicar condiciones adicionales a los elementos en el expresión:

    ```python
    >>> root.xpath('//body//div[@id="content"]')
    [<Element div at 0x4477530>]
    ```

- Los corchetes después del div, [@id="content"], forman una condición que colocamos en elos elementos `<div>`.

- Antes de mostrar un ejemplo completo, vamos a analizar algunos ***casos de uso***.

    - Podemos especificar solo un nombre de etiqueta:
        ```python
        >>> root.xpath('//div[h1]')
        [<Element div at 0x3d6d800>]    
        ```
        - Esto devuelve todos los elementos `<div>` que contienen un elemento `<h1>`.
    
    - Podemos acceder al segundo elemento hijo `div` del elemento `body`

        ```python
         >>> root.xpath('body/div[2]')
        [<Element div at 0x3d6d800>]
        ```
        - Poner un número como condición devolverá el elemento en esa posición en la lista. Hay que tener que estos indices comienzan en 1, a diferencia de la indexación de Python que comienza en 0.

- La especificación completa de XPath es un estándar del W3C(World Wide Web Consortium):

    - https://www.w3.org/TR/xpath-3/

#### Ejemplo de script utilizando expresiones XPath

- [Código de ejemplo](/Unidad_6_Webscraping_con_Python/5-lxml_xpath.py)

    ```python
    #!/usr/bin/env python3

    import re
    import requests

    from lxml.etree import HTML
    response = requests.get('https://www.debian.org/releases/stable/index.en.html')
    root = HTML(response.content)

    title_text = root.find('head').find('title').text
    print(title_text)

    release = re.search('\u201c(.*)\u201d', title_text).group(1)
    p_text = root.xpath('//div[@id="content"]/p[1]')[0].text
    version = p_text.split()[1]
    print('Codename: {}\nVersion: {}'.format(release, version))
    ```
    - Analizamos la páguina web extrayendo el texto que queremos con la ayuda de expresiones XPath. 

        - La expresión XPath `//div[@id="content"]/p[1]` nos permite obtener el primer párrafo dentro del div con id="content".

    
### Extracción de enlaces con el módulo `lxml` con expresiones XPath

- Una de las principales funcionalidades que podríamos desarrollar es la extracción de diferentes elementos html.

- Podríamos definir una clase llamada `Scraping` y definir un método para cada tipo de recursos a extraer.

- Es este caso estamos utilizando el parser xml y expresiones regulares del tipo xpath para obtener cada uno de los recursos a extraer.

- Para el caso de **extraer enlaces** a partir de una url podemos hacer uso de la expresión XPath `//a[@href]`.

- Esto nos devolverá el valor del atributo href para todos aquellos elementos correspondientes a un enlace html.

- [Código de ejemplo](/Unidad_6_Webscraping_con_Python/6-lxml_xpath_links.py)

    - Resultado:
        ```
        Obtener links de la url:https://www.python.org
        Links encontrados 207
        https://www.python.org#content
        https://www.python.org#python-network
        https://www.python.org/
        https://www.python.org/psf/
        https://docs.python.org
        https://pypi.org/
        https://www.python.org/jobs/
        https://www.python.org/community/
        https://www.python.org#top
        https://www.python.org/
        https://psfmember.org/civicrm/contribute/transact?reset=1&id=2
        https://www.python.org#site-map
        https://www.python.org#
        https://www.python.orgjavascript:;
        https://www.python.orgjavascript:;
        https://www.python.orgjavascript:;
        https://www.python.org#
        https://www.linkedin.com/company/python-software-foundation/
        https://fosstodon.org/@ThePSF
        https://www.python.org/community/irc/
        ...
        ```

### Extracción de documentos pdf con el modulo `lxml` con expresiones XPath

- Para el caso de **extraer documentos pdf** a partir de una url podemos hacer uso de la expresión XPath `//a[@href[contains(.,'.pdf')]]/@href`.

- Esto nos dvolverá el valor de atributo href para todos aquellos elementos correspondientes a un documento pdf.

- [Código de ejemplo](/Unidad_6_Webscraping_con_Python/7-lxml_xpath_pdf.py)

    - Resultado:
        ```
        Obtener pdfs de la url:https://docs.python-guide.org
        Pdfs encontrados 1
        https://media.readthedocs.org/pdf/python-guide/latest/python-guide.pdf
        ```

    
### Ejercicio: Extracción de imágenes con el módulo `lxml` con expresiones XPath

- En este ejercicio vamos a utilizar la misma idea de la anterior, pero esta vez vamos a extraer las imágenes de una página web.

- [Código de ejemplo](/Unidad_6_Webscraping_con_Python/8-lxml_xpath_images.py)

    - Resultado:
        ```
        Obtener imágenes de la url:https://www.python.org
        Imágenes encontradas 1
        https://www.python.org//static/img/python-logo.png
        ```
    
## 2. Extraer contenido y etiquetas con `BeautifulSoup`	

- `BeutifulSoup` es una libería utilizada para realizar operaciones de WebScraping desde Python, enfocada en el parseo de contenidos web como XML, HTML, JSON, etc.

- Esta herramienta no está pensada directamente para scraping web. En su ligar, el objetico de esta herramienta es oferecer una interfaz que permita acceder de una manera sencilla al contenido de una página web, lo cual la hace ideal para extraer información de la web.

- Entre las principales características podemos destacar:

    - Parsea y permite extraer información de documentos HTML.
    - Soporta múltiples parsers para tratar documentos XML, HTML(lxml, html5lib)
    - Genera una estructura de árbol con todos los elementos del documentos parseado.
    - Permite buscar de una forma sencilla elementos HTML, tales como enlaces, formularios o cualquier etiqueta HTML.

    - Para poder utilizarla hay que instalar el módulo específico que lo podemos encontrar en el repositorio ofical.
        - https://www.crummy.com/software/BeautifulSoup/
        - https://pypi.org/project/beautifulsoup4/

        ```bash
        pip install beautifulsoup4
        ```
