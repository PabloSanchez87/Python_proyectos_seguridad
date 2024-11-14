#!/usr/bin/env python

import dns               # Importa la biblioteca DNS completa
import dns.resolver      # Importa el módulo para resolver consultas DNS
import dns.query         # Importa el módulo para realizar consultas DNS
import dns.zone          # Importa el módulo para manipular zonas DNS
import dns.name          # Importa el módulo para manejar nombres de dominio
import dns.reversename   # Importa el módulo para obtener el nombre de dominio inverso
import sys               # Importa sys para acceder a los argumentos de la línea de comandos

# Verifica si el número de argumentos es distinto de 2 (script + dominio)
if len(sys.argv) != 2:
    print("[-] uso: python DNSPythonExample.py <nombre_dominio>")
    sys.exit()  # Sale del programa si no se pasa el dominio como argumento

# Asigna el dominio pasado como argumento a la variable `dominio`
dominio = sys.argv[1]

# Realiza consultas DNS para el dominio en registros de tipo A, MX, NS y TXT
# Cada consulta devuelve diferentes tipos de registros:
#   - A: Direcciones IPv4 del dominio.
#   - MX: Servidores de correo responsables del dominio.
#   - NS: Servidores de nombres del dominio.
#   - TXT: Registros de texto del dominio (usados para propósitos variados, como verificación de dominio o políticas SPF).
respuestaRegistroA, respuestaRegistroMX, respuestaRegistroNS, respuestaRegistroTXT = (
    dns.resolver.resolve(dominio, 'A'),
    dns.resolver.resolve(dominio, 'MX'),
    dns.resolver.resolve(dominio, 'NS'),
    dns.resolver.resolve(dominio, 'TXT')
)

# Muestra los servidores de correo (registros MX)
print("Servidores de correo")
print("--------------------")
print(respuestaRegistroMX.response.to_text())

# Muestra los servidores de nombre (registros NS)
print("\nServidores de nombre")
print("--------------------")
print(respuestaRegistroNS.response.to_text())

# Muestra las direcciones IPv4 (registros A)
print("\nDirecciones IPV4")
print("--------------------")
print(respuestaRegistroA.response.to_text())

# Muestra los registros TXT del dominio
print("\nRegistros DNS")
print("--------------------")
print(respuestaRegistroTXT.response.to_text())
