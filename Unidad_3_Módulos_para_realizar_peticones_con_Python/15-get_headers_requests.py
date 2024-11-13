import requests  # Importamos la biblioteca requests para hacer peticiones HTTP

# Realizamos una petición GET a la URL de Python.org
response = requests.get("http://www.python.org")

# Imprimimos el contenido de la respuesta, que incluye el HTML de la página solicitada
print(response.content)

# Imprimimos el código de estado HTTP de la respuesta para verificar si fue exitosa (por ejemplo, 200)
print("Status code: " + str(response.status_code))

# Imprimimos las cabeceras de la respuesta, que contienen información del servidor y el contenido
print("Cabeceras de respuesta: ")
for header, value in response.headers.items():
    print(header, '-->', value)
  
# Imprimimos las cabeceras de la petición enviada, que describen detalles como el agente de usuario y otras configuraciones
print("Cabeceras de la peticion: ")
for header, value in response.request.headers.items():
    print(header, '-->', value)
