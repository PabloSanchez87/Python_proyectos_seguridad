#!/usr/bin/env python

# Importa las librerías necesarias
from PyPDF2 import PdfReader  # Librería para trabajar con archivos PDF
import os  # Para manejar rutas de directorios y archivos

# Define una función para extraer metadatos de todos los archivos PDF en una carpeta específica
def get_metadatos_carpeta_pdf():
    # Usa os.walk para recorrer recursivamente los directorios dentro de "pdf"
    for dirpath, dirnames, files in os.walk("pdf"):
        for data in files:  # Itera sobre cada archivo en la carpeta
            ext = data.lower().rsplit('.', 1)[-1]  # Obtiene la extensión del archivo
            if ext in ['pdf']:  # Verifica si el archivo es un PDF
                # Construye la ruta completa del archivo PDF
                full_path = os.path.join(dirpath, data)
                print(f"[+] Metadatos: {full_path}")

                try:
                    # Lee el archivo PDF con PdfReader
                    pdf = PdfReader(full_path)
                    
                    # Obtiene los metadatos generales del documento PDF
                    info = pdf.metadata
                    if info:
                        for key, value in info.items():
                            print(f"[+] {key.strip('/')}: {value}")
                    else:
                        print("[+] No se encontraron metadatos estándar.")
                    
                    # Extrae información XMP si está disponible
                    # PyPDF2 actualmente no soporta XMP directamente; esta sección es opcional
                    xmpinfo = pdf.metadata  # Placeholder para futuras implementaciones
                    if xmpinfo:
                        # Ejemplo de posibles metadatos (esto puede variar según la implementación futura)
                        print("[+] XMP Metadata:")
                        if hasattr(xmpinfo, 'dc_contributor'):
                            print(f"[+] Contributor: {xmpinfo.dc_contributor}")
                        if hasattr(xmpinfo, 'dc_identifier'):
                            print(f"[+] Identifier: {xmpinfo.dc_identifier}")
                        if hasattr(xmpinfo, 'dc_date'):
                            print(f"[+] Date: {xmpinfo.dc_date}")
                        if hasattr(xmpinfo, 'dc_source'):
                            print(f"[+] Source: {xmpinfo.dc_source}")
                        if hasattr(xmpinfo, 'dc_subject'):
                            print(f"[+] Subject: {xmpinfo.dc_subject}")
                        if hasattr(xmpinfo, 'xmp_modifyDate'):
                            print(f"[+] ModifyDate: {xmpinfo.xmp_modifyDate}")
                        if hasattr(xmpinfo, 'xmp_metadataDate'):
                            print(f"[+] MetadataDate: {xmpinfo.xmp_metadataDate}")
                        if hasattr(xmpinfo, 'xmpmm_documentId'):
                            print(f"[+] DocumentId: {xmpinfo.xmpmm_documentId}")
                        if hasattr(xmpinfo, 'xmpmm_instanceId'):
                            print(f"[+] InstanceId: {xmpinfo.xmpmm_instanceId}")
                        if hasattr(xmpinfo, 'pdf_keywords'):
                            print(f"[+] PDF-Keywords: {xmpinfo.pdf_keywords}")
                        if hasattr(xmpinfo, 'pdf_pdfversion'):
                            print(f"[+] PDF-Version: {xmpinfo.pdf_pdfversion}")
                except Exception as e:
                    # Manejo de errores, como archivos corruptos o inaccesibles
                    print(f"[!] Error al procesar {full_path}: {e}")

# Llama a la función para ejecutarla
get_metadatos_carpeta_pdf()
