#!/usr/bin/env python

# Importación de las bibliotecas necesarias
from urllib.request import urlopen  # Para abrir URLs y descargar contenido
from urllib.parse import urlparse, urlsplit  # Para analizar y dividir URLs
import requests  # Para realizar solicitudes HTTP
import optparse  # Para procesar argumentos de línea de comandos
from os.path import basename  # Para extraer el nombre base de un archivo desde su ruta
from bs4 import BeautifulSoup  # Para analizar y extraer datos de HTML
from PIL import Image  # Para trabajar con imágenes
from PIL.ExifTags import TAGS  # Para decodificar etiquetas EXIF de imágenes
import os  # Para manejar rutas y directorios

# Función para encontrar todas las etiquetas <img> en una página web
def findImages(url):
    print('[+] Finding images on ' + url)
    # Descarga el contenido de la URL
    urlContent = requests.get(url).text
    # Muestra el contenido descargado (puede generar mucho texto si la página es grande)
    print(urlContent)
    # Analiza el contenido HTML usando BeautifulSoup con el parser 'lxml'
    soup = BeautifulSoup(urlContent, 'lxml')
    # Encuentra todas las etiquetas <img> en la página
    imgTags = soup.findAll('img')
    return imgTags

# Función para descargar una imagen a partir de una etiqueta <img>
def downloadImage(imgTag, url):
    try:
        print('[+] Downloading in images directory...' + imgTag['src'])
        # Construye la URL completa de la imagen
        imgSrc = url + imgTag['src']
        # Descarga el contenido de la imagen
        imgContent = urlopen(imgSrc).read()
        # Obtiene el nombre base del archivo desde la URL
        imgFileName = basename(urlsplit(imgSrc)[2])
        # Guarda la imagen en el directorio 'images'
        imgFile = open('images/' + imgFileName, 'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except Exception as e:
        # Si hay un error, lo imprime y retorna una cadena vacía
        print(e)
        return ''

# Función para decodificar información GPS de los datos EXIF
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        # Obtiene las coordenadas geográficas del EXIF y las transforma a formato decimal
        Nsec = exif['GPSInfo'][2][2][0] / float(exif['GPSInfo'][2][2][1])
        Nmin = exif['GPSInfo'][2][1][0] / float(exif['GPSInfo'][2][1][1])
        Ndeg = exif['GPSInfo'][2][0][0] / float(exif['GPSInfo'][2][0][1])
        Wsec = exif['GPSInfo'][4][2][0] / float(exif['GPSInfo'][4][2][1])
        Wmin = exif['GPSInfo'][4][1][0] / float(exif['GPSInfo'][4][1][1])
        Wdeg = exif['GPSInfo'][4][0][0] / float(exif['GPSInfo'][4][0][1])
        # Determina si las coordenadas son norte/sur o este/oeste
        Nmult = 1 if exif['GPSInfo'][1] == 'N' else -1
        Wmult = 1 if exif['GPSInfo'][1] == 'E' else -1
        # Calcula la latitud y longitud en formato decimal
        Lat = Nmult * (Ndeg + (Nmin + Nsec / 60.0) / 60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec / 60.0) / 60.0)
        # Almacena la información GPS en el EXIF
        exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}

# Función para extraer metadatos EXIF de una imagen
def get_exif_metadata(image_path):
    print(image_path)
    exifData = {}
    # Abre la imagen
    image = Image.open(image_path)
    # Verifica si la imagen tiene datos EXIF
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            # Decodifica las etiquetas EXIF
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                exifData[decoded] = value
    # Decodifica información GPS si está presente
    decode_gps_info(exifData)
    return exifData

# Función para imprimir metadatos de todas las imágenes en el directorio 'images'
def printMetadata():
    print("Extracting metadata from images in images directory.........")
    # Recorre los archivos en el directorio 'images'
    for dirpath, dirnames, files in os.walk("images"):
        for name in files:
            print("[+] Metadata for file: %s " % (dirpath + os.path.sep + name))
            try:
                # Extrae y muestra los metadatos de cada imagen
                exif = get_exif_metadata(dirpath + os.path.sep + name)
                for metadata in exif:
                    print("Metadata: %s - Value: %s " % (metadata, exif[metadata]))
                print("\n")
            except:
                # Manejo de errores en caso de fallo al leer metadatos
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

# Función principal
def main():
    # Configura y parsea los argumentos de línea de comandos
    parser = optparse.OptionParser('--url <target url>')
    parser.add_option('--url', dest='url', type='string', help='specify url address')
    (options, args) = parser.parse_args()
    url = options.url
    if url is None:
        # Muestra el uso si no se proporciona la URL
        print(parser.usage)
        exit(0)
    else:
        # Encuentra las imágenes en la URL proporcionada
        imgTags = findImages(url)
        print(imgTags)
        # Descarga cada imagen encontrada
        for imgTag in imgTags:
            imgFileName = downloadImage(imgTag, url)
        # Extrae e imprime los metadatos de las imágenes descargadas
        printMetadata()

# Punto de entrada del programa
if __name__ == '__main__':
    main()
