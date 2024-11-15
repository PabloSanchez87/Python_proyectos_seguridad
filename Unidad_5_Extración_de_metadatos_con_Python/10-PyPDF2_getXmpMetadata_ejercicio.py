#!/usr/bin/env python

# Importa la clase PdfReader para trabajar con archivos PDF.
from PyPDF2 import PdfReader

# Ruta al archivo PDF que se analizará.
fichero = 'Unidad_5_Extración_de_metadatos_con_Python/XMPSpecificationPart3.pdf'

# Carga el archivo PDF utilizando PdfReader.
pdf = PdfReader(open(fichero, 'rb'))

# Muestra el número total de páginas en el PDF.
print("[+] Pages number:", len(pdf.pages))

# Obtiene los metadatos generales del archivo PDF.
info = pdf.metadata

# Verifica y muestra los metadatos estándar si están disponibles.
if hasattr(info, 'author'):
    print("[+] Author:", info.author)
if hasattr(info, 'creator'):
    print("[+] Creator:", info.creator)
if hasattr(info, 'producer'):
    print("[+] Producer:", info.producer)

# Obtiene los metadatos XMP (si están presentes en el PDF).
xmpinfo = pdf.xmp_metadata

# Verifica y muestra metadatos específicos de XMP si están disponibles.
if hasattr(xmpinfo, 'dc_contributor'):
    print('[+] Contributor:', xmpinfo.dc_contributor)
if hasattr(xmpinfo, 'dc_identifier'):
    print('[+] Identifier:', xmpinfo.dc_identifier)
if hasattr(xmpinfo, 'dc_date'):
    print('[+] Date:', xmpinfo.dc_date)
if hasattr(xmpinfo, 'dc_source'):
    print('[+] Source:', xmpinfo.dc_source)
if hasattr(xmpinfo, 'dc_subject'):
    print('[+] Subject:', xmpinfo.dc_subject)
if hasattr(xmpinfo, 'xmp_modify_date'):
    print('[+] ModifyDate:', xmpinfo.xmp_modify_date)
if hasattr(xmpinfo, 'xmp_metadata_date'):
    print('[+] MetadataDate:', xmpinfo.xmp_metadata_date)
if hasattr(xmpinfo, 'xmpmm_document_id'):
    print('[+] DocumentId:', xmpinfo.xmpmm_document_id)
if hasattr(xmpinfo, 'xmpmm_instance_id'):
    print('[+] InstanceId:', xmpinfo.xmpmm_instance_id)
if hasattr(xmpinfo, 'pdf_keywords'):
    print('[+] PDF-Keywords:', xmpinfo.pdf_keywords)
if hasattr(xmpinfo, 'pdf_pdfversion'):
    print('[+] PDF-Version:', xmpinfo.pdf_pdfversion)
