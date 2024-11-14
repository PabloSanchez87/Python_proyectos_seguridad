# Importa la biblioteca necesaria para analizar argumentos y para consultas de DNS.
import argparse
import dns.name
import dns.reversename

# Función principal que verifica si un dominio es subdominio o superdominio de otro.
def main(dominio1, dominio2):
    # Convierte los dominios dados en objetos `dns.name` para su procesamiento.
    dominio1 = dns.name.from_text(dominio1)
    dominio2 = dns.name.from_text(dominio2)
    
    # Verifica y muestra si `dominio1` es un subdominio de `dominio2`.
    print("dominio1 is subdomain of dominio2:", dominio1.is_subdomain(dominio2))
    
    # Verifica y muestra si `dominio1` es un superdominio de `dominio2`.
    print("dominio1 is superdomain of dominio2:", dominio1.is_superdomain(dominio2))

# Punto de entrada del programa.
if __name__ == '__main__':
    # Configura el analizador de argumentos para recibir dominios desde la línea de comandos.
    parser = argparse.ArgumentParser(description='Comprobar 2 dominios con dns Python')
    
    # Argumentos opcionales para `dominio1` y `dominio2` con valores predeterminados.
    parser.add_argument('--dominio1', action="store", dest="dominio1", default='www.python.org')
    parser.add_argument('--dominio2', action="store", dest="dominio2", default='python.org')
    
    # Parsea los argumentos ingresados.
    given_args = parser.parse_args()
    dominio1 = given_args.dominio1
    dominio2 = given_args.dominio2
    
    # Llama a la función `main` con los dominios proporcionados.
    main(dominio1, dominio2)
