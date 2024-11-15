#!/usr/bin/env python

#Caso base
'''
# Importamos la biblioteca PIL para trabajar con imágenes
from PIL import Image  # Para abrir y manipular imágenes
from PIL.ExifTags import TAGS  # Para traducir las claves EXIF a nombres legibles

# Abrimos la imagen ubicada en el directorio 'images' y obtenemos los metadatos EXIF
# Nota: Si no hay metadatos EXIF, _getexif() puede devolver None
print(Image.open('images/image.jpg')._getexif())

# Iteramos sobre los datos EXIF obtenidos para imprimirlos de manera legible
for (key, value) in Image.open('images/image.jpg')._getexif().items():
    # Usamos TAGS.get(key) para traducir el identificador EXIF a su nombre humano legible
    print('%s = %s' % (TAGS.get(key), value))


'''

# Caso avanzado

# Importamos los módulos necesarios de PIL para manejar imágenes y etiquetas EXIF
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

# Función para decodificar información GPS en formato RAW y mostrarla en formato legible
def decode_gps_info2(exif):
    gpsinfo = {}
    # Verifica si hay información GPS en los metadatos EXIF
    if 'GPSInfo' in exif:
        # Itera sobre las claves de GPSInfo y decodifica su significado
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key, key)  # Obtiene el nombre legible de la clave
            gpsinfo[decode] = exif['GPSInfo'][key]  # Asocia la clave decodificada al valor
        print(gpsinfo)  # Muestra la información GPS decodificada
        exif['GPSInfo'] = gpsinfo  # Actualiza el diccionario EXIF con la información GPS decodificada

# Función para calcular las coordenadas GPS en formato decimal
def decode_gps_info(exif):
    gpsinfo = {}
    # Verifica si hay información GPS en los metadatos EXIF
    if 'GPSInfo' in exif:
        # Calcula las coordenadas latitud y longitud en formato decimal
        Nsec = exif['GPSInfo'][2][2][0] / float(exif['GPSInfo'][2][2][1])
        Nmin = exif['GPSInfo'][2][1][0] / float(exif['GPSInfo'][2][1][1])
        Ndeg = exif['GPSInfo'][2][0][0] / float(exif['GPSInfo'][2][0][1])
        Wsec = exif['GPSInfo'][4][2][0] / float(exif['GPSInfo'][4][2][1])
        Wmin = exif['GPSInfo'][4][1][0] / float(exif['GPSInfo'][4][1][1])
        Wdeg = exif['GPSInfo'][4][0][0] / float(exif['GPSInfo'][4][0][1])
        # Determina el signo de las coordenadas según el hemisferio
        Nmult = 1 if exif['GPSInfo'][1] == 'N' else -1
        Wmult = 1 if exif['GPSInfo'][3] == 'E' else -1
        # Convierte las coordenadas a formato decimal
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        # Actualiza la información GPS con las coordenadas decimales
        exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}

# Función para obtener todos los metadatos EXIF de una imagen
def get_exif_metadata(image_path):
    exifData = {}
    image = Image.open(image_path)  # Abre la imagen
    # Verifica si la imagen tiene metadatos EXIF
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            # Decodifica todas las etiquetas EXIF en un diccionario
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)  # Traduce el identificador EXIF a su nombre legible
                exifData[decoded] = value
    decode_gps_info2(exifData)  # Decodifica información GPS en formato RAW
    return exifData  # Devuelve el diccionario con metadatos EXIF

# Función para recorrer el directorio "images" y mostrar los metadatos de cada imagen
def printMetadata():
    # Recorre los archivos en el directorio "images"
    for dirpath, dirnames, files in os.walk("images"):
        for name in files:
            print(f"[+] Metadata for file: {dirpath+os.path.sep+name}")
            try:
                # Extrae los metadatos EXIF
                exifData = {}
                exif = get_exif_metadata(dirpath+os.path.sep+name)
                # Imprime cada metadato encontrado
                for metadata in exif:
                    print(f"Metadata: {metadata} - Value: {exif[metadata]}")
                print("\n")
            except:
                # Maneja posibles errores al procesar una imagen
                import sys, traceback
                traceback.print_exc(file=sys.stdout)

# Llama a la función principal para procesar las imágenes
printMetadata()
