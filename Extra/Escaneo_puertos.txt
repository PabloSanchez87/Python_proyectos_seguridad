import socket

def escanear_puerto(ip, puerto):
    try:
        # Crear un socket para la conexión
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Tiempo de espera reducido
            resultado = s.connect_ex((ip, puerto))  # 0 = éxito
            if resultado == 0:
                print(f" - Puerto {puerto}: Abierto")
            else:
                print(f" - Puerto {puerto}: Cerrado")
    except Exception as e:
        print(f"Error al escanear el puerto {puerto}: {e}")

def main():
    while True:
        # Pedir al usuario la dirección IP o dominio
        direccion = input("\nIntroduce la dirección IP o dominio a escanear: ")
        try:
            ip = socket.gethostbyname(direccion)  # Convertir dominio en IP
            print(f"La dirección IP resuelta es: {ip}")
        except socket.gaierror:
            print("Error: Dirección o dominio no válido.")
            continue
        
        while True:
            try:
                # Pedir el puerto a escanear
                puerto = int(input("Introduce el puerto que quieres escanear: "))
                if puerto < 1 or puerto > 65535:
                    print("Error: El puerto debe estar entre 1 y 65535.")
                    continue
                
                # Escanear el puerto especificado
                escanear_puerto(ip, puerto)

                # Preguntar qué desea hacer a continuación
                print("\n¿Qué deseas hacer ahora?")
                print("1. Escanear otro puerto en la misma IP.")
                print("2. Introducir otra IP.")
                print("3. Salir.")
                opcion = input("Selecciona una opción (1, 2 o 3): ")

                if opcion == "1":
                    continue  # Repetir escaneo en la misma IP
                elif opcion == "2":
                    break  # Salir al bucle principal para nueva IP
                elif opcion == "3":
                    print("Saliendo del programa. ¡Hasta pronto!")
                    return
                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            except Exception as e:
                print("Error: Debes introducir un número para el puerto.")
                print(f"Error: {e}")
            

if __name__ == "__main__":
    main()