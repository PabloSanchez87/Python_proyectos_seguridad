import requests  # Importa la librería requests para realizar solicitudes HTTP

# Define el dominio que se va a analizar
domain = 'domaintools.com'

# Construye la URL de la API de DomainTools para la consulta de IP inversa en el dominio especificado
url = 'https://api.domaintools.com/v1/' + domain + '/reverse-ip/?format=json'

# Define las cabeceras de la solicitud, en este caso con un User-Agent personalizado
headers = {'User-Agent': 'wswp'}

# Realiza una solicitud GET a la API y convierte la respuesta en un diccionario JSON
response = requests.get(url, headers=headers).json()['response']

# Extrae la primera dirección IP de la respuesta JSON
ip_addresses = response['ip_addresses'][0]

# Imprime la dirección IP encontrada
print('IP address: ', ip_addresses['ip_address'])

# Imprime el número de dominios asociados a esta dirección IP
print('domain_count: ', ip_addresses['domain_count'])

# Imprime los nombres de dominio asociados a esta dirección IP
print('domain names: ', ip_addresses['domain_names'])
