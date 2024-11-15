#!/usr/bin/env python
# Este script se ejecutará en un entorno Unix-like con Python.

from PIL import Image  # Importa la clase Image para abrir y manipular imágenes.
from PIL.ExifTags import TAGS  # Importa TAGS para traducir códigos EXIF a nombres legibles.

def get_exif_tags(path_image):
    """
    Extrae las etiquetas EXIF de una imagen y devuelve un diccionario
    con los nombres de las etiquetas como claves y sus valores como valores.

    :param path_image: Ruta de la imagen a analizar.
    :return: Diccionario con etiquetas EXIF y sus valores.
    """
    resultado = {}  # Inicializa un diccionario para almacenar las etiquetas EXIF.

    # Abre la imagen especificada.
    image = Image.open(path_image)

    # Obtiene los datos EXIF de la imagen.
    info = image._getexif()

    # Si hay datos EXIF, procesa cada etiqueta.
    for tag, value in info.items():
        # Traduce el código EXIF a un nombre más comprensible (si existe).
        decoded = TAGS.get(tag, tag)

        # Almacena el par clave-valor en el diccionario de resultados.
        resultado[decoded] = value

    # Devuelve el diccionario con los datos EXIF.
    return resultado


# Llama a la función get_exif_tags para extraer las etiquetas de una imagen específica.
tags = get_exif_tags('images/image.png')

# Itera sobre el diccionario de etiquetas y las imprime en un formato legible.
for key, value in tags.items():
    print('%s = %s' % (key, value))
