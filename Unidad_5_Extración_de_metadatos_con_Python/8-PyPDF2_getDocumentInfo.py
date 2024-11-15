#!/usr/bin/env python

# Importa la librería PyPDF2, utilizada para trabajar con archivos PDF.
from PyPDF2 import PdfReader

# Define una función para extraer metadatos de un archivo PDF ubicado en una ruta específica.
def get_metadatos_ruta_pdf():
    # Imprime un mensaje indicando que se están obteniendo los metadatos del archivo PDF.
    print("[+] Metadatos de Unidad_5_Extración_de_metadatos_con_Python/TutorialPython3.pdf")

    # Abre el archivo PDF en modo lectura binaria ('rb') y crea un objeto PdfReader.
    pdf = PdfReader("Unidad_5_Extración_de_metadatos_con_Python/TutorialPython3.pdf")

    # Obtiene los metadatos del documento PDF usando la propiedad `metadata`.
    # Este método devuelve un diccionario con información como título, autor, creador, etc.
    info = pdf.metadata

    # Imprime los metadatos extraídos.
    print("Metadatos del PDF:")
    for key, value in info.items():
        print(f"{key}: {value}")

# Llama a la función para ejecutarla.
get_metadatos_ruta_pdf()
