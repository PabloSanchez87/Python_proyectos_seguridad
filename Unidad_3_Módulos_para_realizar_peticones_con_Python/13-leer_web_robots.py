import requests  # Importa la biblioteca requests para manejar solicitudes HTTP de manera sencilla
import sys  # Importa el módulo sys para trabajar con argumentos de línea de comandos

# Función principal que recibe una URL como parámetro
def main(url):
    # Construye la URL completa de robots.txt usando la URL base proporcionada
    robot_url = f'{url}/robots.txt'
    
    # Realiza una solicitud HTTP GET para obtener el contenido de robots.txt
    response = requests.get(robot_url)
    
    # Imprime el contenido de robots.txt en texto
    print(response.text)

# Bloque principal del script
if __name__ == "__main__":
    # Toma el primer argumento de línea de comandos como la URL base
    url = sys.argv[1]
    
    # Llama a la función main con la URL proporcionada
    main(url)
