import socket
s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
print("servidor escuchando en el puerto 9999...")
sc, addr = s.accept()

while True:
    recibido = sc.recv(1024)
    print("Recibido:", recibido)
    sc.send(recibido)
    if recibido == "quit":
        break
print("cerrando el socket servidor")
sc.close()
s.close()