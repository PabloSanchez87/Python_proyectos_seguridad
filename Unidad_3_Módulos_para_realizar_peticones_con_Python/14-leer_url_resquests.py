import requests  # Importa la biblioteca requests para manejar solicitudes HTTP

# Función que cuenta el número de palabras en un archivo de texto accesible desde una URL
def palabras_url(url):
    '''
    Función que recibe una URL que contiene un archivo de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la URL del archivo de texto.
    Devuelve:
        El número de palabras que contiene el archivo de texto dado por la URL.
    '''
    try:
        # Realiza una solicitud HTTP GET para acceder al contenido de la URL
        response = requests.get(url)
    except Exception:
        # Si ocurre una excepción (como una URL inválida), devuelve un mensaje de error
        return '¡La url ' + url + ' no existe!'
    else:
        # Obtiene el contenido de la respuesta en formato de texto
        contenido = response.text
        
        # Divide el contenido en palabras usando split() y cuenta el número de palabras
        return len(contenido.split())

# Llama a la función palabras_url con una URL válida y muestra el número de palabras
print(palabras_url('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))

# Llama a la función palabras_url con una URL inválida y muestra el mensaje de error
print(palabras_url('https://no-existe.txt'))
