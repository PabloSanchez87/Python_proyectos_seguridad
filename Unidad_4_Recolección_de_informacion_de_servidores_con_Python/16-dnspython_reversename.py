# Importa la biblioteca `dns.resolver` para realizar consultas DNS.
import dns.resolver

# Lista de dominios para los que se quieren obtener las direcciones IP.
dominios = ["google.com", "microsoft.com", "python.org"]

# Itera sobre cada dominio en la lista.
for dominio in dominios:
    # Imprime el dominio que se está consultando.
    print('Direcciones IP del dominio', dominio)
    
    # Realiza una consulta DNS para el registro A del dominio,
    # que nos proporciona las direcciones IP asociadas.
    direcciones = dns.resolver.resolve(dominio, "A")
    
    # Itera sobre cada dirección IP obtenida y la imprime.
    for direccion_ip in direcciones:
        print(direccion_ip)
