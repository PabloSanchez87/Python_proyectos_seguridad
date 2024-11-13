import urllib.request  # Importa el módulo urllib.request para realizar solicitudes HTTP
import re  # Importa el módulo re para trabajar con expresiones regulares

# Solicita al usuario que introduzca una URL (sin el prefijo "http://")
web = input("Introduce una url(sin http://): ")

# Ejemplo de URL: https://www.adrformacion.com/
# Crear una solicitud HTTP para obtener la respuesta de la URL ingresada
response = urllib.request.Request('http://' + web)

# Envía la solicitud y lee el contenido de la página web
content = urllib.request.urlopen(response).read()

# Define una expresión regular para detectar direcciones de correo electrónico
pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")

# Usa re.findall para encontrar todas las coincidencias de la expresión regular en el contenido de la página
# Convierte 'content' a cadena con str(content) antes de buscar coincidencias
mails = re.findall(pattern, str(content))

# Imprime la lista de correos electrónicos encontrados en la página
print(mails)
