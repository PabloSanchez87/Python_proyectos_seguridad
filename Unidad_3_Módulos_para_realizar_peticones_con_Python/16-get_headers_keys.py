import requests  # Importa la biblioteca requests para realizar solicitudes HTTP

# Bloque principal del script
if __name__ == "__main__":
    # Realiza una solicitud HTTP GET a la URL especificada y guarda la respuesta en 'response'
    response = requests.get("http://www.python.org")
    
    # Itera a través de las claves en los encabezados de la respuesta
    for header in response.headers.keys():
        # Imprime cada encabezado en formato "clave: valor" accediendo al valor con response.headers[header]
        print(header + ":" + response.headers[header])
