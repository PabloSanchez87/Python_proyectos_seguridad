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

1.

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