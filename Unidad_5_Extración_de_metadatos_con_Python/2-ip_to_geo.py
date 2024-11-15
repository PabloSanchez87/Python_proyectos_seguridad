import requests

# Definimos una clase llamada IPtoGeo que se utiliza para obtener información geográfica 
# basada en una dirección IP proporcionada.
class IPtoGeo(object):

    # Método inicializador (__init__) que se ejecuta al crear una instancia de la clase.
    # Recibe una dirección IP como argumento y define atributos predeterminados para almacenar
    # la información geográfica que se obtendrá posteriormente.
    def __init__(self, ip_address):
        self.latitude = ''       # Latitud de la ubicación
        self.longitude = ''      # Longitud de la ubicación
        self.country = ''        # Nombre del país
        self.city = ''           # Nombre de la ciudad
        self.time_zone = ''      # Zona horaria
        self.ip_address = ip_address  # Dirección IP proporcionada por el usuario
        self._get_location()     # Llama al método privado para obtener la información geográfica

    # Método privado (_get_location) que realiza una solicitud HTTP a la API de geolocalización
    # para obtener información geográfica basada en la dirección IP.
    def _get_location(self):
        # Realiza una solicitud GET a la API FreeGeoIP con la dirección IP proporcionada
        json_request = requests.get('https://freegeoip.app/json/%s' % self.ip_address).json()

        # Verifica si la clave 'country_name' existe en la respuesta JSON y la asigna al atributo 'country'
        if 'country_name' in json_request.keys():        
            self.country = json_request['country_name']
        
        # Verifica si la clave 'country_code' existe en la respuesta JSON y la asigna al atributo 'country_code'
        if 'country_code' in json_request.keys():
            self.country_code = json_request['country_code']
        
        # Verifica si la clave 'time_zone' existe en la respuesta JSON y la asigna al atributo 'time_zone'
        if 'time_zone' in json_request.keys():
            self.time_zone = json_request['time_zone']
        
        # Verifica si la clave 'city' existe en la respuesta JSON y la asigna al atributo 'city'
        if 'city' in json_request.keys():        
            self.city = json_request['city']
        
        # Verifica si la clave 'latitude' existe en la respuesta JSON y la asigna al atributo 'latitude'
        if 'latitude' in json_request.keys():
            self.latitude = json_request['latitude']
        
        # Verifica si la clave 'longitude' existe en la respuesta JSON y la asigna al atributo 'longitude'
        if 'longitude' in json_request.keys():
            self.longitude = json_request['longitude']

# Bloque principal: se ejecuta si el archivo se ejecuta como un script principal.
if __name__ == '__main__':
    # Crea una instancia de la clase IPtoGeo con la dirección IP '8.8.8.8' (servidor DNS público de Google).
    ip = IPtoGeo('8.8.8.8')
    
    # Imprime el diccionario de atributos del objeto creado, mostrando la información geográfica obtenida.
    print(ip.__dict__)
