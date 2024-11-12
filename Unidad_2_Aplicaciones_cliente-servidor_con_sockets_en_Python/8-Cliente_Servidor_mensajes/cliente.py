import socket
s = socket.socket()
s.connect(("localhost", 9999))
while True:
    mensaje = input("> ")
    s.send(bytes(mensaje.encode('utf-8')))
    if mensaje == "quit":
        break
print("cerrando socket cliente")
s.close()