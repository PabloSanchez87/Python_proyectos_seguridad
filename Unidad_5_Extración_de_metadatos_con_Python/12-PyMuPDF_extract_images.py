#!/usr/bin/env python

# Importamos la librería `fitz`, que es parte de PyMuPDF, para trabajar con archivos PDF.
import fitz

# Ruta al archivo PDF desde el cual se extraerán las imágenes.
pdf_path = "Unidad_5_Extración_de_metadatos_con_Python/XMPSpecificationPart3.pdf"

# Abrimos el documento PDF.
doc = fitz.open(pdf_path)

# Iteramos sobre cada página del documento.
for i in range(len(doc)):
    # Obtenemos la lista de imágenes incrustadas en la página actual.
    for img in doc.get_page_images(i):
        xref = img[0]  # Referencia cruzada de la imagen dentro del PDF.
        pix = fitz.Pixmap(doc, xref)  # Creamos un objeto Pixmap para manipular la imagen.

        # Comprobamos el tipo de imagen.
        if pix.n < 5:  # Si es una imagen en escala de grises (GRAY) o en RGB.
            output_path = f"Unidad_5_Extración_de_metadatos_con_Python/imagenes/p{i + 1}-{xref}.png"
            pix.save(output_path)  # Guardamos la imagen en formato PNG.
        else:  # Si es una imagen en CMYK, la convertimos a RGB antes de guardarla.
            pix1 = fitz.Pixmap(fitz.csRGB, pix)  # Convertimos a RGB.
            output_path = f"Unidad_5_Extración_de_metadatos_con_Python/imagenes/p{i + 1}-{xref}.png"
            pix1.save(output_path)  # Guardamos la imagen convertida en formato PNG.
            pix1 = None  # Liberamos la memoria asociada al objeto Pixmap de la imagen convertida.

        pix = None  # Liberamos la memoria asociada al objeto Pixmap de la imagen original.
