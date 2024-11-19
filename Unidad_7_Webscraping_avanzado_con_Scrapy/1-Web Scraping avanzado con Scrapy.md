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

Vamos a contruir un proyecto de Scrapy que nos permite extraer los datos de las sessiones de la conferencia EuroPython siguiendo el patrón de la siguiente URL:

`https://ep{year}.europython.eu/en/events/sessiones`

- Podríamos probar con los años de 2016 a 2020.

    https://ep2016.europython.eu/en/events/sessions/
    https://ep2017.europython.eu/en/events/sessions/
    https://ep2018.europython.eu/en/events/sessions/
    https://ep2019.europython.eu/en/events/sessions/
    https://ep2020.europython.eu/en/events/sessions/

### Creación del proyecto

- La forma estandar de comenzar a trabajar con Scrapy es crear un proyecto, que se realiza con el comando `scrapy startproject <project_name>`.

    ```bash
    scrapy startproject europython
    ```
- De esta forma, se creará la carpeta del proyecto con la siguiente estructura:
    ```bash
    .
    ├── europython: módulo de Python de nuestro proyecto.
    │   ├── __init__.py
    │   ├── items.py: archivo donde definimos los campos que queremos extraer.
    │   ├── middlewares.py: 
    │   ├── pipelines.py: fichero de pipelenes del proyecto.
    │   ├── settings.py: fichero
    │   └── spiders: directorio donde se almacenarán los spiders.
    │       └── __init__.py
    └── scrapy.cfg : fichero de configuración principal de Scrapy.
    ```


### Ficheros proyecto Scrapy

- Los items son contenedores que cargaremos con los datos que queremos extraer.

- Como nuestros items contendrán los datos relacionados con el título y la descripción, definiremos estos atributos en el fichero `items.py`.

- En la clase `EuropythonItem`, que se crea de forma automática, definiremos los campos que queremos extraer, instanciando objetos de la clase `scrapy.Field`.

    ```python
    import scrapy
    from itemloaders.processors import Compose, MapCompose, Join

    clean_text = Compose(MapCompose(lambda v: v.strip()), Join())   

    def custom_field(text):
        text = clean_text(text)
        return text.strip()
        
    class EuropythonItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        title = scrapy.Field(output_processor=custom_field)
        author = scrapy.Field(output_processor=custom_field)
        description = scrapy.Field(output_processor=custom_field)
        date = scrapy.Field(output_processor=custom_field)
        tags = scrapy.Field(output_processor=custom_field)
    ```

    - La función `custom_field`está utilizando para el formato de las cadenas de texto donde el mñetodo strip() nos permite eliminar cualquier espacio al principio y al ginal para cada uno de los campos y se aplciará automáticamente a todos los elementos que indicamos cuando los instanciamos.


### Spider europython

- Los spiders son clases escritas por el usuario para extraer información de un dominio ( o un grupo de dominios).

- Se define como una lista inicial de URLs, para posteriormente definir la lógica necesaria para seguir los enlaces y analziar el contenido de esas páginas para extraer elementos.

- Este spider tendrá un método constructor init para inicializar el spider, la url de la que queremos extraer los datos y un parámetro adicional que indica el año del que queremos extraer información.

- En el archivo `europython_spider.py` definimos la clase `EuropythonSpider` que hereda de la clase `scrapy.Spider`.

- En esta clase se define el spider que a partir de la url de inicio rastreará los enlaces que va encontrando en función del patrón indicado, y para cada entrada obtendrá los datos correspondientes a cada sesión(título, autos, descripción, fecha, etc.).

    ```bash
    scrapy genspider europython_spider ep2016.europython.eu
    ```	

    ```python
    #!/usr/bin/env python3

    import scrapy
    from scrapy.spiders import CrawlSpider, Rule
    from scrapy.linkextractors import LinkExtractor
    from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
    from scrapy.loader import ItemLoader

    from europython.items import EuropythonItem

    class EuropythonSpider(CrawlSpider):
        def __init__(self, year='', *args, **kwargs):
            super(EuropythonSpider, self).__init__(*args, **kwargs)
            self.year = year
            self.start_urls = ['http://ep'+str(self.year)+".europython.eu/en/events/sessions"]
            print('start url: '+str(self.start_urls[0]))
        
        name = "europython_spider"
        allowed_domains = ["ep2016.europython.eu", "ep2017.europython.eu","ep2018.europython.eu","ep2019.europython.eu","ep2020.europython.eu"]
        
        # Pattern for entries that match the conference/talks and /talks format
        rules = [Rule(LxmlLinkExtractor(allow=['conference/talks']),callback='process_response2016_17_18'),
        Rule(LxmlLinkExtractor(allow=['talks']),callback='process_response_europython2019_20')]

        def process_response2016_17_18(self, response):
            itemLoader = ItemLoader(item=EuropythonItem(), response=response)
            itemLoader.add_xpath('title', "//div[contains(@class, 'grid-100')]//h1/text()")
            itemLoader.add_xpath('author', "//div[contains(@class, 'talk-speakers')]//a[1]/text()")
            itemLoader.add_xpath('description', "//div[contains(@class, 'cms')]//p//text()")
            itemLoader.add_xpath('date', "//section[contains(@class, 'talk when')]/strong/text()")
            itemLoader.add_xpath('tags', "//div[contains(@class, 'all-tags')]/span/text()")
            item = itemLoader.load_item()
            return item
            
        def process_response_europython2019_20(self, response):
            item = EuropythonItem()
            item['title'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/h1/text()").extract()
            item['author'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/h5/a/text()").extract()
            item['description'] = response.xpath("//*[@id='talk_page']/div/div/div[1]/p[3]/text()").extract()
            item['date'] = "July "+self.year
            item['tags'] = response.xpath("//span[contains(@class, 'badge badge-secondary')]/text()").extract()

            return item
    ```

### Funcionamiento del spider

- Las variables más significativas de nuestro spider son:

    - `name`: nombre del spider.
    - `allowed_domains`: array con los dominios permitidos.
    - `start_urls`: array con las URLs de inicio.
    - `rules`: reglas para la extración de enlaces (estos enlaces también serán visitados por la spider) de esta manera podemos hacer una búsqueda recursiva.
    - `process_response`: método que se ejecuta cada vez que se realiza una petición a una url. (La regla de extración de enlaces se pasa como parámetro).


- Las reglas definidas por objetos del tipo Rule, que reciben como parámetros un objeto extractor de enlaces LinkExtracto donde allow es una expresión regular con la que los enlaces deben coincidir, y una función callback que se pasa como parámetro que se ejecutará cada vez que se extraiga un enlace y se realiza una solicitud a la URL de este enlace.

- Para obtener más información sobre las reglas puedes visitar la documentación oficial: https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.contrib.spiders.Rule

- En la spider definimos también los métodos `process_response2016_17_18` y `process_response_europython2019_20` para extraer cada uno de los campos.

- Si en la web la vista detallada de cualquiera de las charlas, podemos identificar la expresion XPath necearia para extraer el título, autor, descripción y etiquetas de cada una de las conferencias.

### Obtener Expresion XPath

- Para extraer la información que nos interesa a partir del código HTML utilizaremos expresiones XPath, que podemos obtener haciendo clocl derecho en el navegador y seleccionando la opcion de inspeccionar.

- En este caso, estamos interesados en extraer el título, autor, descripción y etiquetas de cada una de las conferencias.

- Podríamos utilizar `scrapy shell` para obtener las expresions XPath necesarias para extraer dicha información.

    ```bash
    scrapy shell

    In [1]: fetch('https://ep2019.europython.eu/talks/KNhQYeQ-downloading-a-billion-files-in-python/')
    2024-11-19 10:13:37 [scrapy. core. engine] INFO: Spider opened
    2024-11-19 10:13:39 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://ep2019.europython.eu/talks/KNhQYeQ-downloadin
    g-a-billion-files-in-python/> (referer: None)

    2024-11-19 10:13:39 [asyncio] DEBUG: Using selector: EpollSelector
    ```	

    ```bash
    In [2]: response.xpath('//*[@id="talk_page"]/div/div/div[1]/h1').extract()
    Out[2]: ['<h1>Downloading a Billion Files in Python</h1>']

    2024-11-19 10:18:24 [asyncio] DEBUG: Using selector: EpollSelector
    ```


    ```bash
    In [3]: response.xpath('//*[@id="talk_page"]/div/div/div[1]/h5/a').extract()
    Out[3]: ['<a href="../../conference/p/-332.html">James Saryerwinnie</a>']

    2024-11-19 10:19:20 [asyncio] DEBUG: Using selector: EpollSelector
    ```

    ```bash
    In [4]: response.xpath('//*[@id="talk_page"]/div/div/div[1]/p[3]').extract()
    Out[4]: ["<p>You've been given a task.  You need to download some files from a server to your local machine.   The files are fairly small, and you can list and access these files from the remote server through a REST API.  You'd like to download them as fast as possible.  The catch?  There's a billion of them.  Yes, one billion files.</p>"]

    2024-11-19 10:20:18 [asyncio] DEBUG: Using selector: EpollSelector
    ```

    ```bash
    In [5]: response.xpath("//span[contains(@class,'badge badge-secondary')]/text()").extract()
    Out[5]:
    ['ASYNC / Concurreny',
    'Case Study',
    'Multi-Processing',
    'Multi-Threading',
    'Performance']
    ```	

### Ejecutando el spider Europython

- Podemos ejecutar nuestro spider con el siguiente comando:

    ```bash 
    scrapy crawl europython_spider -o europython.json -t json
    ``` 

- Donde los últimos parámetros indican que los datos extraídos se almacenan en un fichero llamado `europython_items.json` y que se exportará en formato json.

- Otra opción interesantes es que los spiders pueden administrar los argumentos que se pasan en el comando de rastreo utilizando la opción `-a` de Scrapy. Por ejemplo, podemos ejecutar el spider con el siguiente comando:


    ```bash 
    scrapy crawl europython_spider -a year=2026 -o europython.json -t json
    ```


### Pipelines proyecto europython

- De esta forma los archivos europython_items.json, europython_items.xml y europython_items.csv se generan automáticamente.

- ¿Qué sucede si queremos separar la información o validar algunos campos antes de guardar los registros?

    - Para esos casos podemos hacer uso de los pipelines. 
    - Permiten tratar la información extraída, como por ejemplo, almacenar la información en otro recurso como por ejemplo un archivo csv o un archivo sqlite.

- Para ellos, primero necesitamos **habilitar el uso de pipelines en el fichero `settings.py`** de nuestro proyecto.

- Este paso consiste en añadir una linea que indique la clase donde se definián las reglas para el pipeline definido, en este caso, estamos definiendo 4 pipelines:

    ```python
    ITEM_PIPELINES = {
        'europython.pipelines.EuropythonJsonExport': 100,
        'europython.pipelines.EuropythonXmlExport': 200,
        'europython.pipelines.EuropythonCSVExport': 300,
        #'europython.pipelines.EuropythonSQLitePipeline': 400
    }
    ``` 

#### Fichero `pipelines.py`
- La clase `EuropythonJsonExport` se encarga de guardar los datos extraídos en un fichero json.

```python
class EuropythonJsonExport(object):    
    def __init__(self):
        self.file = codecs.open('europython_items.json', 'w+b', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
```

- La clase `EuropythonXmlExport` se encarga de guardar los datos extraídos en un fichero xml.

```python
class EuropythonXmlExport(object):
    
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('europython_items.xml', 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
```

- De la misma forma, la clase `EuropythonCSVExport` se encarga de guardar los datos extraídos en un fichero csv.

- Al finalizar el proceso, obtenemos como ficheros de salida:

    - europython_items.json
    - europython_items.xml
    - europython_items.csv

#### Ejercicio: Implementar pipelines para guardar los datos en una base de datos sqlite

- [Código pipeline-sqlite](/Unidad_7_Webscraping_avanzado_con_Scrapy/pipelines-sqlite.py)


### Settings proyecto Europython

- `settings.py`: Definimos el nombre del módulo `europython.spiders` y los pipelines definidos entre los que destacamos uno que permite exportar los datos en formato xml(EuropythonXmlExport), json(EuropythonJsonExport) y csv(EuropythonCSVExport).

- También tenemos un pipeline que permite guardar los datos en una base de datos sqlite.

```python
 # Scrapy settings for europython project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#
http://doc.scrapy.org/en/latest/topics/settings.html
#
BOT_NAME = 'europython'

SPIDER_MODULES = ['europython.spiders']
NEWSPIDER_MODULE = 'europython.spiders'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
 'europython.pipelines.EuropythonJsonExport': 100,
 'europython.pipelines.EuropythonXmlExport': 200,
 'europython.pipelines.EuropythonCSVExport': 300,
 'europython.pipelines.EuropythonSQLitePipeline': 400
}

DOWNLOADER_MIDDLEWARES = {
"scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 110,
#"europython.middlewares.ProxyMiddleware": 100,
}
```	

- De esta forma ya tenemos un proyecto funcional, si lo ejecutamos, extraerá la información deseada y la guardará en los archivos correspondientes.

- Sin embrago, todavía hay aspectos por mejorar.

- Una de las más importantes es evitar el bloqueo de nuestro spider debido a un número elevado de peticiones.

- El primer paso para evitar este caso es limitar la velocidad de nuestro spider. En scrapy esto se puede hacer modificando la variable `DOWNLOAD_DELAY` en el fichero `settings.py`.

    ```python	
    DOWNLOAD_DELAY = 3
    ```

## 5. Resumen


#### Conceptos principales
- **Arquitectura**: Comprender los diferentes elementos que forman Scrapy. Entre los principales elementos de la arquitectura se destacan:
  - **Spiders**
  - **Items**
  - **Pipelines**

#### Extracción de información
- Uso de la **Shell de Scrapy** para acceder a elementos HTML y extraer información con **expresiones XPath**.
  - Ejemplo:
    ```python
    fetch('url_dominio')
    response.xpath('//title/text()').extract()
    ```

#### Herramientas útiles
- Utilización del método **`Selector.xpath()`** para extraer información específica.

#### Creación de proyectos en Scrapy
- Comando inicial:
  ```bash
  scrapy startproject <nombre_proyecto>
  ```

#### Organización del proyecto
- Identificar la estructura de ficheros y carpetas del proyecto Scrapy:
  - `items.py`
  - `spiders/`
  - `pipelines.py`

## Definición de spiders
- Crear un nuevo **spider** basado en la clase `CrawlSpider`.
- Asignar un nombre al spider y el dominio que se desea rastrear.

#### Definir comportamiento de extracción
- Implementar el método **`parse()`** para:
  - Analizar la respuesta.
  - Extraer datos.
  - Obtener nuevas URLs para crear nuevas solicitudes.

#### Configuración avanzada
- Definir un **pipeline** para procesar los **items** extraídos.
- Modificar y analizar el archivo de configuración principal: **`settings.py`**.

#### Exportar resultados
- Guardar los datos extraídos en formatos como **JSON**, **CSV** o **XML**.


### FAQ

- `¿Cuáles son los principales componentes de la arquitectura de scrapy?`

    La arquitectura de Scrapy contiene cinco componentes principales:

    - El motor de Scrapy
    - Planificador
    - Descargador
    - Arañas
    - Tuberías de elementos

### Enlaces de interés

- https://docs.scrapy.org/en/latest/
- https://doc.scrapy.org/en/latest/topics/commands.html
- https://scrapy.org/
- https://github.com/DanMcInerney/xsscrapy

### Glosario

- `Crawler (Rastreador)`
    
    Programa de software que visita virtualmente todas las páginas de Internet con el objetivo de crear índices para los motores de búsqueda. Por lo general, los rastreadores se centran más en los archivos de texto que en los gráficos.