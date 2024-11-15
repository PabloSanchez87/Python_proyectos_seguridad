from peepdf.PDFCore import PDFParser
import os

def analyze_pdf(relative_path):
    # Resolver la ruta completa a partir de la ruta relativa
    file_path = os.path.abspath(relative_path)

    # Verificar si el archivo existe
    if not os.path.exists(file_path):
        print(f"El archivo '{relative_path}' no existe.")
        return

    # Crear una instancia del parser de peepdf
    pdf_parser = PDFParser()
    pdf, stats = pdf_parser.parse(file_path)

    if not pdf:
        print(f"Error al analizar el archivo: {file_path}")
        return

    # Imprimir los resultados
    print(f"File: {relative_path}")
    print(f"MD5: {pdf.hashes['MD5']}")
    print(f"SHA1: {pdf.hashes['SHA1']}")
    print(f"Size: {pdf.file_size} bytes")
    print(f"Version: {pdf.version}")

    print(f"\nBinary: {pdf.is_binary}")
    print(f"Linearized: {pdf.is_linearized}")
    print(f"Encrypted: {pdf.is_encrypted}")
    print(f"Updates: {pdf.num_updates}")
    print(f"Objects: {pdf.num_objects}")
    print(f"Streams: {pdf.num_streams}")
    print(f"Comments: {pdf.num_comments}")
    print(f"Errors: {len(stats.errors)}")

# Ruta relativa del archivo PDF a analizar
relative_pdf_path = "Unidad_5_Extración_de_metadatos_con_Python/example_test_pdf.pdf"
analyze_pdf(relative_pdf_path)
