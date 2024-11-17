#!/usr/bin/env python3
# Línea shebang que indica que el script debe ejecutarse con Python 3.

import requests  # Para realizar solicitudes HTTP y manejar las respuestas
import sys  # Para manejar argumentos pasados por la línea de comandos

from bs4 import BeautifulSoup  # Para analizar y extraer información del contenido HTML

# Creamos listas para almacenar los enlaces de nivel 1 y nivel 2
urls_nivel1 = []  # Almacenará los enlaces encontrados en el nivel 1 (enlaces directos de la página objetivo)
urls_nivel2 = []  # Almacenará los enlaces encontrados dentro de las páginas enlazadas en el nivel 1

# Recibimos la URL objetivo como argumento desde la línea de comandos
target_url = sys.argv[1]

# Realizamos una conexión HTTP GET a la URL objetivo y obtenemos el contenido del código fuente de la página
url = requests.get(target_url).content

# Usamos BeautifulSoup para analizar el contenido HTML de la página
soup = BeautifulSoup(url, 'lxml')

# Usamos un bucle para encontrar todas las etiquetas `<a>` con el atributo `href` en el HTML
for line in soup.find_all('a'):
    new_line = line.get('href')  # Extraemos el valor del atributo `href` (el enlace)
    try: 
        # Verificamos si el enlace es absoluto (comienza con "http")
        if new_line[:4] == "http": 
            # Si pertenece al dominio de la URL objetivo, lo añadimos a la lista `urls_nivel1`
            if target_url in new_line: 
               urls_nivel1.append(str(new_line)) 
        # Si el enlace es relativo (comienza con "/"), lo combinamos con la URL base
        elif new_line[:1] == "/": 
            try:
                comb_line = target_url + new_line  # Combinamos la URL base con el enlace relativo
                urls_nivel1.append(str(comb_line))  
            except: 
                pass
        
        # Imprimimos los enlaces encontrados en nivel 1
        print(urls_nivel1)
        
        # Recorremos todos los enlaces guardados en `urls_nivel1` para buscar enlaces de nivel 2
        for get_this in urls_nivel1: 
            # Realizamos una conexión HTTP GET a cada enlace de nivel 1
            url = requests.get(get_this).content 
            # Usamos BeautifulSoup para analizar el contenido HTML de las páginas enlazadas
            soup = BeautifulSoup(url, 'lxml') 
            for line in soup.find_all('a'): 
                new_line = line.get('href')  # Extraemos el valor del atributo `href`
                try: 
                    # Verificamos si el enlace es absoluto (comienza con "http")
                    if new_line[:4] == "http": 
                        # Si pertenece al dominio de la URL objetivo, lo añadimos a la lista `urls_nivel2`
                        if target_url in new_line:
                            urls_nivel2.append(str(new_line)) 
                    # Si el enlace es relativo, lo combinamos con la URL base
                    elif new_line[:1] == "/": 
                        comb_line = target_url + new_line 
                        urls_nivel2.append(str(comb_line)) 
                except: 
                    pass
                
    except:
        # Manejo de excepciones genéricas; ignoramos errores en la extracción de enlaces
        pass

# Imprimimos los enlaces encontrados en nivel 2
print(urls_nivel2)
