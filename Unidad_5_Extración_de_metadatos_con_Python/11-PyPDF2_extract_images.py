import subprocess

# Define las rutas del archivo PDF y el directorio de salida
pdf_path = 'Unidad_5_Extración_de_metadatos_con_Python/XMPSpecificationPart3.pdf'
output_dir = 'Unidad_5_Extración_de_metadatos_con_Python/imagenes'

# Usa el comando `pdfimages` para extraer las imágenes del PDF
# `pdfimages` es una herramienta de la suite Poppler que extrae imágenes directamente de archivos PDF.
# Aquí usamos `subprocess.run` para ejecutar el comando desde Python.
subprocess.run(f'pdfimages {pdf_path} {output_dir}', shell=True)

