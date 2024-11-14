import dns.resolver  # Importa la biblioteca `dns.resolver` para realizar consultas DNS

# Realiza una consulta DNS para obtener los registros MX (Mail Exchange) del dominio 'google.com'
respuestas = dns.resolver.resolve('google.com', 'MX')

# Recorre cada respuesta en los registros MX obtenidos
for respuesta in respuestas:
    # Imprime el servidor de correo (exchange) y la preferencia de ese servidor (preference)
    print('Host', respuesta.exchange, 'tiene una preferencia de', respuesta.preference)
