import requests  # Importamos la biblioteca requests para realizar peticiones HTTP

# Definimos tres URLs para probar diferentes tipos de respuestas
url_ok = "http://www.python.org"               # URL correcta
url_error  = "http://www.python.org/incorrecta" # URL que da error (no existe)
url_exception  = "http://url_not_exists"        # URL inexistente para generar una excepción

# Definimos las cabeceras de la petición, especificando un agente de usuario
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

# Enviamos una petición GET a la URL correcta con las cabeceras especificadas
response = requests.get(url_ok, headers=headers)

# Verificamos si el código de estado es 200 (éxito)
if response.status_code == 200:
    # Imprimimos el contenido HTML de la respuesta
    print(response.content)
else:
    # Si el código de estado no es 200, mostramos un mensaje de error
    print("Error al conectar %s (%d)" % (url_ok, response.status_code))

# Enviamos una petición GET a la URL que genera un error
response = requests.get(url_error, headers=headers)

# Verificamos si el código de estado es 200
if response.status_code == 200:
    # Si es 200, imprimimos el contenido HTML de la respuesta
    print(response.content)
else:
    # Si hay error, imprimimos un mensaje de error con la URL y el código de estado
    print("Error al conectar %s (%d)" % (url_error, response.status_code))

# Intentamos hacer una petición a una URL inexistente para capturar la excepción
try:
    response = requests.get(url_exception, headers=headers)
except Exception as exception:
    # En caso de excepción, imprimimos un mensaje de error con la URL y la excepción generada
    print("Error al conectar %s (%s)" % (url_exception, exception))
