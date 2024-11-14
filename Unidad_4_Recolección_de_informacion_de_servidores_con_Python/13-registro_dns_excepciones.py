#!/usr/bin/env python

import argparse        # Importa argparse para analizar los argumentos de la línea de comandos
import dns.zone        # Importa dns.zone para manipular zonas DNS (no se usa en este código pero podría ser útil)
import dns.resolver    # Importa dns.resolver para realizar consultas DNS
import socket          # Importa socket para trabajar con conexiones y manipular direcciones IP

# Función principal que realiza consultas DNS para diferentes tipos de registros
def main(dominio):
    # Registros DNS de tipo A (IPv4)
    try:
        respuestaIPV4 = dns.resolver.resolve(dominio, 'A')  # Realiza la consulta para registros A (IPv4)
        for i in range(0, len(respuestaIPV4)):
            print("IPv4:", respuestaIPV4[i])  # Imprime cada registro IPv4
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros IPv4:", error)  # Muestra un mensaje si no hay respuesta para registros A

    # Registros DNS de tipo AAAA (IPv6)
    try:
        respuestaIPV6 = dns.resolver.resolve(dominio, 'AAAA')  # Realiza la consulta para registros AAAA (IPv6)
        for i in range(0, len(respuestaIPV6)):
            print("IPv6:", respuestaIPV6[i])  # Imprime cada registro IPv6
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros IPv6:", error)  # Muestra un mensaje si no hay respuesta para registros AAAA

    # Registros de correo (MX)
    try:
        mx = dns.resolver.resolve(dominio, 'MX')  # Realiza la consulta para registros MX (servidores de correo)
        for i in range(0, len(mx)):
            print("MX:", mx[i])  # Imprime cada registro MX
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros MX:", error)  # Muestra un mensaje si no hay respuesta para registros MX

    # Registros de alias (CNAME)
    try:
        cname_answer = dns.resolver.resolve(dominio, 'CNAME')  # Realiza la consulta para registros CNAME (alias)
        print("CNAME:", cname_answer)  # Imprime el registro CNAME
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros CNAME:", error)  # Muestra un mensaje si no hay respuesta para registros CNAME

    # Registros de servidores de nombres (NS)
    try:
        ns_answer = dns.resolver.resolve(dominio, 'NS')  # Realiza la consulta para registros NS (servidores de nombres)
        print(ns_answer)  # Imprime los registros NS
    except dns.resolver.NoAnswer as error:
        print("Error al obtener los registros NS:", error)  # Muestra un mensaje si no hay respuesta para registros NS

# Punto de entrada principal del script
if __name__ == '__main__':
    # Configuración del parser de argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='DNS Python')
    parser.add_argument('-dominio', action="store", dest="dominio", default='python.org')  # Argumento para el dominio
    given_args = parser.parse_args()  # Analiza los argumentos de línea de comandos
    dominio = given_args.dominio  # Obtiene el valor del dominio pasado por el usuario o el valor por defecto
    main(dominio)  # Llama a la función principal con el dominio proporcionado
