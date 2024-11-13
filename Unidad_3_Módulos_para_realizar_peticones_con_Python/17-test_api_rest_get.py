import requests  # Importamos la biblioteca requests para manejar peticiones HTTP
import json  # Importamos json para manejar datos en formato JSON

# Realizamos una petición GET a la URL especificada con un tiempo de espera de 5 segundos
response = requests.get("http://httpbin.org/get", timeout=5)

# Imprimimos el código de estado HTTP de la respuesta
print("Código de estado HTTP: " + str(response.status_code))

# Imprimimos las cabeceras de la respuesta
print(response.headers)

# Verificamos si la petición fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertimos el contenido de la respuesta a formato JSON y lo guardamos en results
    results = response.json()
    
    # Recorremos los elementos de results y los imprimimos como pares clave-valor
    for result in results.items():
        print(result)
    
    # Imprimimos las cabeceras de la respuesta
    print("Cabeceras de la respuesta: ")
    for header, value in response.headers.items():
        print(header, '-->', value)
    
    # Imprimimos las cabeceras de la petición enviada
    print("Cabeceras de la petición: ")
    for header, value in response.request.headers.items():
        print(header, '-->', value)
    
    # Accedemos al valor de la cabecera 'server' en la respuesta y lo imprimimos
    print("Server: " + response.headers['server'])
else:
    # En caso de error, imprimimos el código de estado correspondiente
    print("Error code %s" % response.status_code)
