#!/usr/bin/env python3

# Importa las clases necesarias de Scrapy.
from scrapy import Spider  # Clase base para definir un spider.
from scrapy.http import Request  # Clase para generar solicitudes HTTP adicionales.

# Define el spider para rastrear el sitio web de libros.
class BooksSpider(Spider):
    # Nombre del spider, se usará al ejecutarlo (`scrapy crawl BooksSpider`).
    name = 'BooksSpider'
    
    # Lista de dominios permitidos. El spider no rastreará fuera de estos dominios.
    allowed_domains = ['books.toscrape.com']
    
    # URLs iniciales para comenzar el rastreo.
    start_urls = ['http://books.toscrape.com']

    # Método principal que se ejecuta para procesar la respuesta de las URLs en `start_urls`.
    def parse(self, response):
        # Extrae los enlaces de los libros usando un selector XPath.
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            # Convierte el enlace relativo de cada libro en una URL absoluta.
            absolute_url = response.urljoin(book)
            
            # Genera una solicitud HTTP para cada libro y especifica que `parse_book` procesará la respuesta.
            yield Request(absolute_url, callback=self.parse_book)

        # Encuentra el enlace a la página siguiente usando un selector XPath.
        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        if next_page_url:  # Verifica si hay una página siguiente.
            # Convierte el enlace relativo de la página siguiente en una URL absoluta.
            absolute_next_page_url = response.urljoin(next_page_url)
            
            # Genera una solicitud HTTP para la página siguiente y vuelve a llamar a `parse`.
            yield Request(absolute_next_page_url)

    # Método para procesar los detalles de cada libro.
    def parse_book(self, response):
        # Devuelve un diccionario con la URL de la página del libro actual.
        yield {'book_url': response.url}
