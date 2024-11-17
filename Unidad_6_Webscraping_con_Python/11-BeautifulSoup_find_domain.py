# Importamos las bibliotecas necesarias
import requests  # Para realizar solicitudes HTTP
from bs4 import BeautifulSoup  # Para analizar y extraer datos del contenido HTML

# URL del servicio utilizado:
# https://viewdns.info/reverseip/?host=python.org&t=1
# Este servicio permite obtener otros dominios alojados en el mismo servidor que el dominio que se está analizando.

def main():
    # Dominio que queremos analizar
    sitio = "python.org"

    # Definimos un User-Agent para que la solicitud HTTP se identifique como proveniente de un navegador
    # Esto es útil para evitar restricciones de algunos servidores.
    agent = {'User-Agent': 'Firefox'}

    # Realizamos una solicitud GET a la página con el dominio que queremos analizar
    response = requests.get(
        "https://viewdns.info/reverseip/?host={}&t=1".format(sitio), 
        headers=agent
    )

    # Analizamos el contenido HTML de la respuesta utilizando BeautifulSoup
    html = BeautifulSoup(response.text, 'html.parser')

    # Buscamos la tabla que contiene los resultados.
    # La tabla tiene un atributo `border="1"` que utilizamos para identificarla.
    tabla = html.find('table', attrs={'border': '1'})

    # Iteramos sobre todas las filas (`<tr>`) de la tabla
    for fila in tabla.find_all("tr"):
        # Imprimimos el dominio alojado en el mismo servidor.
        # Accedemos al primer elemento `<td>` de cada fila y obtenemos su texto (string).
        print("Dominio alojado en el mismo servidor: " + fila.td.string)

# Punto de entrada del programa
if __name__ == '__main__':
    main()
