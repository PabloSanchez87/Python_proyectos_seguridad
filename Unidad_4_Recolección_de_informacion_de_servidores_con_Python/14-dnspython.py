# Importa el módulo `dns.resolver` que permite realizar consultas de DNS.
import dns.resolver

# Define la función principal que recibe un dominio como argumento.
def main(dominio):
    # Lista de tipos de registros DNS a consultar.
    registros = ['A', 'AAAA', 'NS', 'SOA', 'MX', 'MF', 'MD', 'TXT']
    
    # Itera sobre cada tipo de registro en la lista.
    for registro in registros:
        try:
            # Intenta resolver el registro DNS del dominio especificado.
            respuestas = dns.resolver.resolve(dominio, registro)
            
            # Muestra el tipo de registro que se está resolviendo.
            print("Respuestas del registro ", registro)
            print("-----------------------------------")
            
            # Itera sobre cada respuesta obtenida y la imprime.
            for respuesta in respuestas:
                print(respuesta)
        
        # Captura cualquier excepción que pueda ocurrir durante la resolución DNS.
        except:
            print("No pude resolver la consulta para el registro ", registro)

# Punto de entrada del programa.
if __name__ == '__main__':
    try:
        # Llama a la función `main` con el dominio 'google.com'.
        main('google.com')
    
    # Permite salir del programa con `Ctrl+C` sin mostrar un error.
    except KeyboardInterrupt:
        exit()
