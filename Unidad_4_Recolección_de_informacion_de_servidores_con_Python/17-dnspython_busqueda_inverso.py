# Importa la biblioteca `dns.reversename` para realizar consultas de DNS inversas.
import dns.reversename

# Convierte una dirección IP en un nombre DNS inverso.
# En este caso, estamos usando la dirección IP "8.8.8.8".
nombre = dns.reversename.from_address("8.8.8.8")

# Imprime el nombre DNS inverso generado a partir de la dirección IP.
print(nombre)

# Convierte el nombre DNS inverso de vuelta a la dirección IP original.
print(dns.reversename.to_address(nombre))
