import requests

# Solicita al usuario que introduzca una dirección IP. La dirección IP se almacena en la variable 'ip'.
ip = input("Introduce direccion ip:")

# Construye la URL de la API de FreeGeoIP, agregando la dirección IP proporcionada por el usuario.
url = "https://freegeoip.app/json/" + ip

# Define los encabezados que se enviarán junto con la solicitud HTTP.
# 'accept': Indica que se aceptan respuestas en formato JSON.
# 'content-type': Especifica que el contenido de la solicitud (si lo hubiera) también está en formato JSON.
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

# Realiza una solicitud GET a la API usando la URL construida y los encabezados definidos.
# requests.request("GET", ...) realiza la solicitud al servidor y devuelve una respuesta.
respuesta = requests.request("GET", url, headers=headers)

# Imprime la respuesta de la API en formato JSON. Este método convierte la respuesta en un diccionario de Python.
print(respuesta.json())
