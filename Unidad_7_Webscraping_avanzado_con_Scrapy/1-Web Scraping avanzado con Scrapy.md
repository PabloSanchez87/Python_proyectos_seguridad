# Web Scrapping Avanzado con `Scrapy`

## Objetivos

### Competencia
- Conocer `Scrapy`como framework para extraer información de sitios web de forma automática mediante la creación se spyders.
- Scrapy también permite exportar los datos extraidos en diferentes formatos como csv, xml y jsaon con el objetivo de analizar estos datos posteriormente.

### Resultados
- Comprender el framework `Scrapy` y su funcionalidad, para crear nuestros propios spiders con el objetivo de automatizar el proceso de extración de un sitio web.
- Crear spiders en Python con el objetivo de extraer enlaces a partir de una sitio web.
- Analizar las diferentes formas que ofrece Scrapy para exportar la información extraída en diferentes formatos (CSV, JSON, XML, sqlite, etc.).


### Contexto

`Scrapy` como framework incluye algunas características para el scraping eficiente en términos de concurrencia, peticiones y rendimiento. Revisaremos componentes, la arquitectura y la forma de crear un proyecto Scrapy que incluya spiders y pipelines de post-procesamiento.

- https://scrapy.org/


### Índice

1. Aprender sobre los componentes de `Scrapy` y su arquitectura.
2. Aprender sobre `Scrapy Shell` que puede ayudarnos a crear rápidamente prototipos para validar su metodología de scraping.
3. Aprender a crear y configurar un proyecto Scrapy con spiders y pipelines.
4. Proyecto Scrapy para extraer las conferencias europython
5. Resumen

---

## 1. Aprender sobre los componentes de `Scrapy` y su arquitectura.

Scrapy es un framework para Python que permite tareas de webscraping y procesos de web crawling y análisis de datos.

- [Documentación oficial](https://docs.scrapy.org/en/latest/)

- Este framework también nos permite expandir su funcionalidad y al estar desarrollado en Python puede ejecutarse en los sistemas operativos Windows, Linux y MacOS.

- Aunque el objetivo principal de `Scrapy` es la extración de datos de un sitio web, también se puede utilizar apra extraer datos mediante el uso de APIs, obtener la estructura de un sitio web o actuar como extractor de información de propósito general.

- `Scrapy` tiene las siguientes características:

    - **Rápudo y robusto**: podemos escribir las reglas para extraer losd atos y Scrapy hace el trabajo por nosotros.

    - **Fácilmente extendible**: dada su configuración, podemos generar una nueva funcionalidad sin tener que modificar el código fuente.

    - **Multiplataforma**: está escrito en Python y puede ejecutarse en Windows, Linux y MacOS.

- `Scrapy` tiene una serie de herramientas con el objetivo de scrapear o extraer información de un sitio web de manera fácil y eficiente. Estas herramientas incluyen:

    - Soporte para extraer y seleccionar datos de fuentes HTMl/XML usando **selectores CSS y expresiones XPath**, con mñetodos para extraer usando expresiones regulares.

    - Una consola interactica en IPython para probar expresiones CSS y XPath para extraer datos, lo cual es muy útil al crear sus propios métodos.

    - Soporte para exportar registros en múltiples formatos, como CSV, JSON, XML, etc.

    - Gran extensibilidad, ya que le permite conectar su propia funcionalidad utilizando señales, extensiones y pipelenes.

- **`Recuerda`**

    - `Scrapy` se puede decir que es una unión de Crawler y Scraper.

        - Los web crawlers son robots que recorren sitios web, partiendo de una lista de urls y van siguiendo los links encontrados y descargando las páginas para su posterior procesamiento.

        - Los web scrapers son utilizados para extraer datos estructurados (ej. diccionarios) a partir de contenido no estructurado o semistructurado (ej. HTML).

---

### `Arquitectura de Scrapy`

Scrapy permite **escanear de forma recursiva los contenidos de un sitio web** y aplicar un conjunto de reglas sobre dichos contenidos para extraer información que nos pueda ser útil.

Estos son los principales elementos de una arquitectura de Scrapy:

- **`Motor de scrapy(engine)`**
    
    El motor gestiona las peticiones y el flujo de datos entre todos los demás componentes.

- **`Planificador(Scheduler)`**

    El planificador recibe las peticiones enviadas por el motor y las  pone en cola.

- **`Downloader`**

    El propósito del downloader es buscar todas las páginas wveb y enviarlas al motor. El motor posteriormente envías las páginas a los spiders.

- **`Spiders`**

    Rutinas de código que se encargan de realizar peticiones HTTP a un listado de dominios dados por el cliente y de aplicar reglas en forma de expresiones regulares o XPath sobre el contenido retornado por la petición HTTP.

- **`Expresiones XPath`**

    Con las expresiones XPath podemos llegar a un nivel bastante detallado de la información que queremos extraer.

    Por ejemplo, si queremos sacar los links de descarga de una página bastsa con obtener la expresion XPath del elemento y acceder añ atributo `href`.

    Scrapy utiliza un mecanismo basado en expresiones XPath llamado Xpath Selectos. Se encargan de aplicar reglas XPath definidas por el desarrollador y de componer objetos Python que contienen la información extraída.

- **`Items`**

    Son los objetos que generan los XPath Selectors .

    Los items son como contenedores de información ya que permiten alamacenar la información que retornan las reglas XPath que aplicamos sobre los contenidos que vamos obteniendo.

    Básicamente, contienen los campos de la información que queremos extraer.


- **`Items Pipelines`**

    Son elementos que procesan los items una vez estos han sido analizados por los spiders.

---

![alt text](/resources/scrapy.png)

- En esta imagen podemos ver una descripción general de la acrquitectura de Scrapy.

- La figura muestra en detalles cómo los componentes de la arquitectura de Scrapy funcionan juntos donde el motor no se comunica directamente con los downloadres, sino que primero pasa la solicitud HTTP al Scheduler o planificador.

- Los spiders usan los items para pasar los datos al pipeline.

- Los spiders le hacen los requests, estos quedan planificados en el sheduler, y estos son los que realizan las peticiones al server, finalmente, cuando responde el server, esta respuesta es enviada de nuevo al spider, de forma que el spider se va retroalimentando con cada petición que realiza.

- [Data Flow- Arquitectura de Scrapy](https://doc.scrapy.org/en/latest/topics/architecture.html#topics-architecture)

### `Instalación de Scrapy`

- Existen diversas herramietnas y técnicas que permiten a un desarrollador o analista acceder, consumir y extraer contenido basado en el web.

    - [Instalación de Scrapy](https://doc.scrapy.org/en/latest/intro/install.html#intro-install)

    - [Documentación oficial](https://docs.scrapy.org/en/latest/)

- `Scrapy` se creó a partir de [Twisted](https://twisted.org/), por lo que es capaz de realizar diversas peticiones de forma simultanea.

- Comando instalación:
    ```bash
    pip install scrapy  
    ```

## 2. Aprender sobre `Scrapy Shell` que puede ayudarnos a crear rápidamente prototipos para validar su metodología de scraping.

### Extrayendo información mediante Scrapy Shell

- `Scrapy Shell` es una herramienta de línea de comando que permite a los desarrolladores realizar pruebas de extracción de datos sobre una determinada URL.

- `Scrapy` facilita este proceso al proporcionar una shell de línea de comandos, que toma una URL y crea un contexto de respuesta en el que probar las expresions XPath y CSS.

- Llamar a Scrapy por línea de comandos de shell le mostraá los comandos básicos de scrapy.

    - https://docs.scrapy.org/en/latest/topics/shell.html

- Para comenzar, podemos abrir una sesión interactica en `scrapy shell`.
- Posteriormente podemos utilizar el comando `fetch`para realizar una petición HTTP a una URL pasada por parámetro y transferir los resultados con el objeto `response`.

- Por ejemplo, si queremos extraer el texto correspondiente al título de la página, podemos hacer con la expresión XPath `//title/text()`.

    ```bash
    >>> scrapy shell "http://www.scrapy.org"
    >>> response.xpath('//title/text()').extract()
    [u'Scrapy: A Fast and Powerful Crawler']
    ```

    - La expresión XPath `//title/text()` nos devuelve el texto correspondiente al título de la página.

    - El comando `extract()` nos devuelve el resultado de la expresión XPath.

### Uso de selectores

- Para utilizar `Scrapy` es necesario definir aquellas reglas que Scrapy utilizará para la extración de información.

- Dichas reglas pueden ser expresiones XPath. 

- Podemos usar los selectores para seleccionar algunas partes de los datos HTML obtenidos.

- Los selectores permiten seleccionar datos HTML usando expresiones XPath, CSS a través de response.xpath() y response.css() respectivamente.

- En el siguiente ejemplo, declaramos una cadena con etiquetas HTML y usamos a la Clase `Selector` àra extraer los datos en la etiqueta h1 usando el método `Selecto.xpath()`.

    ```python
    >> from scrapy.selector import Selector
    >>> body = '<html><body><h1>Extract data with selectorh1></body></html>'
    >>> Selector(text = body).xpath('//h1/text()').get()
    "Extract data with selector'
    ```

- [Selectores en Scrapy](https://docs.scrapy.org/en/latest/topics/selectors.html)

#### Ejercicio: Obtener las expresiones xpath que podríamos usuar para extraer información de una url

- URL objetivohttps://www.python.org/jobs/

    ```bash
    scrapy shell https://www.python.org/jobs/
    ```

- información a extraer:

    - Localización del trabajo

    - Empresa

    - Título del trabajo

    - Descripción

```python
 response.xpath('//span[@class="listing-location"]/a/text()').getall()
['Remote, Remote, USA', 'Hyderabad, Telangana, India', 'Chennai, Tamil Nadu, India', 'Remote, Worldwide, Remote, Worldwide, Remote, Worldwide', 'Cape Town, Western Cape, South Africa', 'Waterford, Ireland', 'Remote, Remote, Remote', 'Cascina, Pisa, Tuscany, Italy', 'Richmond, BC, Canada', 'Munich, Bayern, Germany', 'Nottingham, United Kingdom', 'Remote, Remote', 'remote, Switzerland, Switzerland', 'Warsaw (fully remote), Poland', 'Warsaw (fully remote), Poland', 'remote, MD, United States', 'remote, MD, United States', 'London, United Kingdom', 'Remote, North Carolina, United States', 'Leuven, Belgium', 'remote, Europe', 'Remote, Pennsylvania, United States', 'Remote, Pennsylvania, United States', 'Hybrid (United States), Los Angeles, United States', 'Remote (United States), United States']
```

```python
>>> response.xpath('//span[@class="listing-company-name"]/text()[2]').getall()
['\n                    \n                    ', '\n                    \n                    ', '\n\t\t    TeraLumen Solutions Pvt Ltd\n                ', '\n\t\t    ActivePrime, Inc.\n                ', '\n\t\t    Kazang a company part of the Lesaka Technologies Group\n                ', '\n\t\t    Red Hat, Inc.\n                ', '\n\t\t    NJB Brands LLC\n                ', '\n\t\t    European Gravitational Observatory (EGO)\n                ', '\n\t\t    Pepper Wireless\n                ', '\n\t\t    Entrix GmbH\n                ', '\n\t\t    Axion Recruitment\n                ', '\n\t\t    Baserow\n                ', '\n\t\t    Windsor.ai\n                ', '\n\t\t    Reef Technologies\n                ', '\n\t\t    Reef Technologies\n                ', '\n\t\t    eSImplicity\n                ', '\n\t\t    eSImplicity\n                ', '\n\t\t    EDITED\n                ', '\n\t\t    Aidentified, LLC\n                ', '\n\t\t    Twipe\n                ', '\n\t\t    Windsor.ai\n                ', '\n\t\t    Powerlytics\n                ', '\n\t\t    Powerlytics\n                ', '\n\t\t    Multi Media LLC\n                ', '\n\t\t    Multi Media LLC\n                ']
```

```python
>>> response.xpath('//span[@class="listing-job-type"]/a/text()').getall()

['Back end', 'Big Data', 'Machine Learning', 'Systems', 'Testing', 'Back end', 'Back end', 'Front end', 'Image Processing', 'Integration', 'Operations', 'Testing', 'Back end', 'Cloud', 'Database', 'Back end', 'Front end', 'Back end', 'Cloud', 'Systems', 'Back end', 'Machine Learning', 'Numeric processing', 'Integration', 'Lead', 'Operations', 'Systems', 'Database', 'Back end', 'Cloud', 'Systems', 'Back end', 'Cloud', 'Database', 'Front end', 'Web', 'Back end', 'Back end', 'Back end', 'Big Data', 'Big Data', 'Back end', 'Big Data', 'Database', 'Back end', 'Cloud', 'Database', 'Web', 'Cloud', 'Database', 'Machine Learning', 'Web', 'Back end', 'Back end', 'Big Data', 'Cloud', 'Database', 'Front end', 'Integration', 'Machine Learning', 'Systems', 'Testing', 'Web', 'Back end', 'Big Data', 'Cloud', 'Database', 'Front end', 'Integration', 'Machine Learning', 'Systems', 'Testing', 'Back end', 'Lead', 'Management', 'Web', 'Back end', 'Web']
```

## 3. Aprender a crear y configurar un proyecto Scrapy con spiders y pipelines.

### Scrapy como framework de desarrollo de spyders.

- Exploraremos Scrapy como un framework de desarrollo para Python que nos permite realizar tareas de web scraping y procesos de rastreo web y análisis de datos.

- Exploraremos la estructura de un proyecto `Scrapy` y cómo crar nuestro propio proyecto, y crearemos un spyder para rastrear una página web y extraer los datos que nos interesan.

- Revisaremos los componentes de `Scrapy` creando una proyecto para configurar diferentes pipelines.

- Una de las principales ventajas de `Scrapy` es que está construido en `Twisted`, un framework de red asíncrono y sin bloqueo para tareas de concurrencia.

    - `Sin bloqueo` significa que no tiene que esperar a que finalice una solicitud antes de hacer otra, incluso que puede lograrlo con un alto nivel de rendimiento
    - Esta característica mejora los crawlers y spiders desarrollados con `Scrapy` en comparación con otros sistemas de scraping.

- Entre las principales ventajas de `Scrapy` se encuentran:

    - Menos uso de CPU y menos consumo de memoria
    - Muy eficiente en comparación con otros frameworks y librerías.
    - La arquitectura diseñada le ofrece robustez y flexibilidad.
    - Puede desarrollar fácilmente middleware personalizado para añadir funcionalidad personalizadas.


### Creación de un nuevo proyecto Scrapy

- Para crear un nuevo proyecto Scrapy, podemos utilizar el comando `scrapy startproject`.

    ```bash
    scrapy startproject scrapy-project
    ```

- Cuando crea un proyecto con el comando anterior, genera la siguiente escrutura de carpetas y ficheros donde podemos ver los principales componentes de un proyecto `Scrapy`.

    ```
    .
    └── scrapy_project
        ├── scrapy.cfg
        └── scrapy_project
            ├── __init__.py
            ├── items.py
            ├── middlewares.py
            ├── pipelines.py
            ├── settings.py
            └── spiders
                └── __init__.py
    ```

- Cada proyecto se compone de los siguientes ficheros:

    - items.py: Definimos los elementos a extraer y creamos los campos de la información que queremos extraer.

    - spiders: Es el corazón del proyecto, aquí definimos el procedimiento de extración. Scrapy internamente lo que hace es buscar clases del tipo Spider ubicadas en la carpeta de spiders y usará la configuración que encontramos en el archivo settings.py

    - pipelines.py: Son los elementos para analizar lo obtenido: validación de datos, limpieza del código HTML, etc. Se usa para recibir un elemento y realizar una acción sobre él.

    - settings.py: Aquí se definen las configuraciones del proyecto, como las URLs a scrapear, las cookies que se utilizarán, etc.

    - middlewares.py: Son elementos que procesan los items una vez estos han sido analizados por los spiders.

- Una vez que se crea el proyecto, tenemos que definir los elementos que queremos extraer, o más bien la clase donde se almacenarán los datos extraídos por scrapy.

- El siguiente código sería un ejemplo de fichero `items.py` donde definimos una clase que hereda de la clase `scrapy.Item`:

    - Básicamente tenemos que definir los campos(fields) de la información que queremos extraer(título, descripción, url, precio, ...).

    ```python
    from scrapy.item import Item, Field
    class MyItem(Item):
    name = Field()
    ...
    ```

- Scrapy proporciona la clase Item para definir el formato de datos de salida.

- Los objetos Item son contendores que se utilizan para recopilar los daos extraídos y especifican metadatos para el campo utilizado para caracterizar esos datos.

- **Estos objetos proporcionan una sintaxis para declarar campos donde el objeto Field especifica los metadatos para cada campo.**

- [Documentación Clase Items de Scrapy](https://doc.scrapy.org/en/latest/topics/items.html)


### Spiders

- Scrapy usa los **spiders** para definir cómo se debe scrapear un sitio para obtener los datos que se desea extraer.

- Scrapy nos permite determinar qué información queremos extraer y cómo podemos extraerla.

- Específicamente, las spiders son clases de Python donde pondremos toda nuestra lógica y comportamiento personalizados.

    - https://docs.scrapy.org/en/latest/topics/spiders.html

- Las spiders son clases que definen la forma de navegar por un determinado sitio o dominio y como extraer los datos de esas páginas, es decir, definimos de forma personalziada el comportamiento para analziar las páginas de un sitio particular.

- El ciclo que sigue una spider es el siguiente:

    1. Primero empezamos generando la peticion inicial (requests) para navegar por la priemra URL y especificamos la funcion `parse_item()` que será llamada con la respuesta de la petición (response).
    2. La primera petición a hacer es obtenida llamando al método `start_requests()` de la spider, que por defecto genera la petición para la URL específica en las direcciones de incio `start_urls` y la función `parse_item()` para las peticiones.

        - EN la función `parse_item()` analizamos la respuesta y se uede devolver:
            - Objetos tipo Item.
            - Obejetos tipo Request.
            - Una unión de ambos sobre la que se puede iterar.

        - Estas peticiones serán realizadas descargánose por `Scrapy` y sus respuestas manipuladas por la función `parse_item()`.
        - En estsa función analizamos el contenido usando los selectores (XPath Selectos) y generamos los Items con el contenido analizado.
        - Por último, los Items devueltos por la spider se podrán pasar a algún Item Pipeline para ser procesados.

#### Estructura de una Spider

- Esta podría ser la **la estructura base de nuestra spider** donde definimos el nombdre de la spider y el domino del cual queremos extraer información.

    ```python
    from scrapy.contrib.spiders import CrawlSpider

    class MySpider(CrawlSpider):
        name = 'myspider'
        allowed_domains = ['dominio.com']
    ```

- En esta primera instancia realizamos los imports de las clases necesarias para llvar a cabo el proceso de crawling.

- Entre estas clases podems destacar:

    - `Rule`: Nos permite establecer las reglas por las cuales el crawler se va a basar para navegar por los diferentes enlaces.

    - `LxmlLinkExtractor`: Nos permite definir una función de callback y expresiones regulares para indicarle al crawler por los enlaces que debe pasar. Permite definir las reglas de navegaación entre los enlaces que queremos obtener.

    - `HtmlPathSelector`: Permite aplicar expresions XPath.

    - `CrawlSpider`: provee un mecanismo que permite seguir los enlaces que siguen un determinado patrón. Además de los atributos inherentes a la clase BaseSpider, esta clase disponde un nuevo atributo `rules` con el cual podemos indicarle al Spider el/los comportamiento/s que queremos que realice.

#### Creando el esquelo de nuestro Spider.

- Este es el código de nuestro spider que podemos guardar en un archivo llamado MySpider.py bajo el directorio de spiders del proyecto de Scrapy.

    ```python	
    from scrapy.contrib.spiders import CrawlSpider, Rule
    from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
    from scrapy.selector import Selector
    from scrapy.item import Item

    class MySpider(CrawlSpider):

        name = 'dominio.com'
        allowed_domains = ['dominio.com']
        start_urls = ['http://www.example.com']
        rules = (Rule(LxmlLinkExtractor(allow=())))

        def parse_item(self, response):
            hxs = Selector(response)
            elemento = Item()
            return elemento
    ```

#### Extración de enlaces con Scrapy

- EL primer paso es crear el spider. Scrapy proporciona el comando genspider para generar la plantilla básica de nuestro spyder.

- Para crear un spider, ejecutamos el siguiente comando:

    ```bash
    scrapy genspider <spidername> <website>
    ```

- URL utilizada en el ejemplo.[Scraping de Libros](https://books.toscrape.com/)

    ```bash
    scrapy genspider BooksSpider https://books.toscrape.com/
    ```

    ```bash	
    .
    ├── scrapy.cfg                        # Archivo de configuración principal de Scrapy.
    └── scrapy_project
        ├── __init__.py                   # Marca el directorio como un paquete de Python.
        ├── __pycache__                   # Archivos de caché de Python (pueden ignorarse).
        │   ├── __init__.cpython-312.pyc  # Bytecode compilado de __init__.py.
        │   └── settings.cpython-312.pyc  # Bytecode compilado de settings.py.
        ├── items.py                      # Definición de estructuras para datos extraídos.
        ├── middlewares.py                # Middleware personalizado de Scrapy.
        ├── pipelines.py                  # Procesamiento de datos extraídos.
        ├── settings.py                   # Configuración del proyecto Scrapy.
        └── spiders                       # Contiene todos los spiders.
            ├── BooksSpider.py            # Tu spider para https://books.toscrape.com/.
            ├── __init__.py               # Marca spiders como un paquete de Python.
            └── __pycache__               # Caché de Python para spiders.
                └── __init__.cpython-312.pyc
    ```	

- Recorrerá la páguina principal y añadirá posteriormente nuestro comportamiento.

    ```python
    # BooksSpider.py
    import scrapy


    class BooksspiderSpider(scrapy.Spider):
        name = "BooksSpider"
        allowed_domains = ["books.toscrape.com"]
        start_urls = ["https://books.toscrape.com/"]

        def parse(self, response):
            pass
    ```

- La clase `BooksSpider` hereda de la clase `scrapy.Spider`. Al heradar de scrapy.Spider se proporcionan los siguientes métodos:
    - `start_requests:` PAra cada url definida se crea un objeto request de Scrapy, asignando los parámetros necesarios para que el motor use la conexión correcta. Como manejador de respuestas, se asigna el método `parse`.

    - `parse(response):` Scrapy llama a este método cuando obtiene un objeto de respuesta HTTP al completar con éxito una descarga de contenido. Recibe el mismo objeto de tipo `response`. El objetico principal sería extrar los datos apropiados de esta respuesta.

- Más info: https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.parse

    - `name`: es el nombre de la spider que se dio en el comando de generación. Usaremos este nombre para iniciar la spider desde línea de comandos.
    - `allowed_domains`: lista de los dominios pemritidos que la araña puede rastrear.
    - `start_urls`: la URS desde donde comenzará el proceso de scraping. Luego tenemos el método de análisis que chequea el contenido de la páguina.
    - `parse(response):` es la función que permite analizar la respuesta, extraer los datos y obtener nuevas URLs para seguir creando nuevas peticiones a partir de ellas.

- [Fichero con lógica BooksSpider](/scrapy-project/scrapy_project/scrapy_project/spiders/BooksSpider.py)

- Ejecución del spider:

    ```bash
    scrapy runspider BooksSpider.py -o books_links.json -t json
    ```

    - [Archivo de salida books_links.json](/Scrapy/scrapy_project/books_links.json)


- EN la salida del comando anterior vemos la sección de estadísticas (Dumping Scrapy stats) con informaicón como **request_count** y **response_count** que representa la cantidad de elementos extraídos.

    ```json
    2024-11-18 13:39:29 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 354604,
    'downloader/request_count': 1051,
    'downloader/request_method_count/GET': 1051,
    'downloader/response_bytes': 22126017,
    'downloader/response_count': 1051,
    'downloader/response_status_count/200': 1050,
    'downloader/response_status_count/404': 1,
    'elapsed_time_seconds': 18.153778,
    'feedexport/success_count/FileFeedStorage': 1,
    'finish_reason': 'finished',
    'finish_time': datetime.datetime(2024, 11, 18, 12, 39, 29, 389193, tzinfo=datetime.timezone.utc),
    'item_scraped_count': 1000,
    'items_per_minute': None,
    'log_count/DEBUG': 2056,
    'log_count/INFO': 11,
    'memusage/max': 67178496,
    'memusage/startup': 67178496,
    'request_depth_max': 50,
    'response_received_count': 1051,
    'responses_per_minute': None,
    'robotstxt/request_count': 1,
    'robotstxt/response_count': 1,
    'robotstxt/response_status_count/404': 1,
    'scheduler/dequeued': 1050,
    'scheduler/dequeued/memory': 1050,
    'scheduler/enqueued': 1050,
    'scheduler/enqueued/memory': 1050,
    'start_time': datetime.datetime(2024, 11, 18, 12, 39, 11, 235415, tzinfo=datetime.timezone.utc)}
    ```

- La salida del spider nos permite ver la cantidad de peticiones realizadas, la cantidad de respuestas recibidas y la cantidad de elementos extraídos.

- También vemos la línea `download/request_status_count/200`, donde 200 significa que recibimos con éxito una respuesta del servidor. Podemos obtene rotros código como 500 y 400, lo que significa que el servidor rechazó la solicitud o no es capaz de obtener la respuesta.

#### Ejercicio: Obtener enlaces de una url con scrapy

- Ejemplo de una url: https://news.ycombinator.com/

- [Código de ejemplo](/Scrapy/scrapy_project/spiders/HackerNewsItem.py)

- Resultado: [HackerNews_links.json](/Scrapy/scrapy_project/HackerNews_links.json)

---

### `Scrapy pipelines`

- Los `pipelines` son elementos de Scrapy a los que la información que les llega son Items que han salido previamente obtenidos y procesados por alguna spider.

- Son clases en sí, que tienen un simple objetivo: volver a procesar el Item que les llega pudiendo rechazarlo o dejar que pase por ese pipeline.

- Los usos típicos son:

    - Limpieza de datos en HTML
    - Validación de datos scrapeados comprobando que los items contienen ciertos campos
    - Comprobación de items duplicados
    - Almacenamiento de los datos extraídos en una base de datos

- Para cada elemento que se obtiene, se envía al pipeline correspondiente, que lo procesará para guardarlo en la base de datos o para enviarlo a otra pipeline si fuera necesario.

- [Documentacion item-pipeline](https://doc.scrapy.org/en/latest/topics/item-pipeline.html)

- Un pipeline de elementos es una clase de Python que sobre escribe algunos métodos específicos y debe activarse en la configuración del proyecto Scrapy.

- Al crear un proyecto Scrapy, encontrará un archivo `pipeline.py` ya disponible para crear sus propios pipelines.

- Estos objetos son clases Python que deben implementar el método `process_item(item,spider)` y deben devolver un objeto tipo `item` (o una subclase) o bien, si no lo devuelve, debe lanzar una expceción del tipo DropItem para indicar que ese Item no seguirá siendo procesado.

- Un ejemplo de pipeline:

    ```python
    #!/usr/bin/python

    from scrapy.exceptions import DropItem

    class MyPipeline(object):
        def process_item(self, item, spider):
            if item['key']:
                return item
            else:
                raise DropItem("No existe el elemento: %s" % item['key'])
    ```	

- Un punto más a tener en cuenta es que cuando creamos un objeto de este tipo debemos introducir en el fichero `settings.py` la siguiente línea para **activar el pipeline** en la variable `ITEM_PIPELINES`:

    ```python
     ITEM_PIPELINES = [ 'proyecto.pipeline.MyPipeline':300,]
    ```
---

### Fichero de configuración `settings.py`

- El fichero de configuración lo podemos encontrar en el directorio raíz del proyecto para que el spider se pueda ejecutar.

- Este archivo alamacela la configuración del spider y le permite modificar el comportamiento de los spiders cuando sea necesario, por ejemplo, modificando las cabeceras de petición, el agente de usuario y el tiempo de retardo entre peticiones con el objetivo de que nuestro spider tenga mejor rendimiento.

- Entre las principales características en forma de variables que podemos modificar podemos destacar:

    - `DEFAULT_REQUEST_HEADERS`: que son parte de cualquier solicitud que su navegador envía al servidor web. Esta característica es similar al USER_AGENT y se puede usar con algunos sitios que no le permiten ver sus datos sin usar cabeceras en las peticiones.

    - `USER_AGENT` que en realidad es parte de lo encabezados, pero también se puede configurar por separado. Con respecto al agente de usuario, puede configurarlo de forma personalizada.

    - `DOWNLOAD_DELAY` que permite establecer un tiempo de retardo entre solicitudes concurrentes a diferentes págines del mismo sitio web. Cada solicitud se retrasa el tiempo en segundos especificado en esta variable. Por ejemplo, si lo configura como 5, esto retrasa cada petición por 5 segundos. Antes de iniciar Scrapy, se recomienda modificar la configuración y limitar la velocidad a la que se accede a los datos y **evitar los ataques DOS(Denial of Service)**.

    - `ROBOTSTXT_OBEY` ofrece una opción para seguir o ignorar el archivo robots.txt. El archivo robots.txt, almacenado en la raíz del sitio web, describe el comportamiento de los bots en el sitio web.

- Ejemplo de configuración de Scrapy:

    ```python
    # Configuración de Scrapy

    # Identificar el agente de usuario:
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

    # Respetar las reglas definidas en el fichero de robots.txt:
    ROBOTSTXT_OBEY = True

    # Sobrescribe las cabeceras de la petición predeterminadas:
    DEFAULT_REQUEST_HEADERS = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "DNT": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "x-requested-with": "XMLHttpRequest",
    }

    # Configurar un tiempo de retardo para las solicitudes en el mismo sitio web:
    # (predeterminado: 0)
    # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
    # See also autothrottle settings and docs
    DOWNLOAD_DELAY = 3

---

### Exportación de resultados en formatos json, csv, xml, etc.

- Con Scrapy podemos recopilar la información y guardarla en un archivo en uno de los formatos compatibles (json, csv o xml), o incluso directamente en una base de datos usando un pipeline.

- En este caso, estamos ejecutando el comando scrapy pasando como argumento el formato JSON:

    ```bash
    scrapy crawl <crawler_name> -o <output_file>.json -t json
    ```	

- Los últimos parámetros indican que los datos extrados se alamacenan en un archivo llamado `<output_file>.json` y que el exportador utiliza para el formato JSON. 
    - Se puede hacer de la misma manera para exportar a formatos CSV o XML.

    - La opcion `-o <output_file>` proporciona como parámetro del archivo de salida que contendrá los datos que ha extraído.

    - Con la opción `-t <format>` podemos indicar el formato de salida (json, csv, xml, etc.).

---

### `CONSEJOS Y TRUCOS DE EJECUCIÓN DE SCRAPY`

- Al ejecutar Scrapy, podemos seguir estas reglas para administrar la ejecución del rastreador:

    - Si el proceso de scraping falla, puede buscar en el registro de la consola las líneas que incluyen `[Scrapy] DEBUG` y `[scrapy.core.engine] DEBUG.`

    - Si desea parar el proceso de scraping, podemos usar la tecla `Ctrl + C` en la consola de comandos.

    - Cuando Scrapy haya terminado de procesar los datos, mostrará la siguiente información en la consola: `[scrapy] INFO: Closing spider (finished).`

    - Por defecto, Scrapy añade nuevos datos al final del achivo de salida si ya existe. Si el archivo no existe, creará uno nuevo. Por lo tanto, si solo desea obtener datos nuevos y descartar los anteriores, es recomendable eleiminar el archivo anterior.


## 4. Proyecto Scrapy para extraer las conferencias europython

## 5. Resumen





