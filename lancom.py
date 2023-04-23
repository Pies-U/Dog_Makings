import socket

PORT = 32222
SERVER = input("Server's IP > ")
ADDR = (SERVER, PORT)

client = socket.socket()
client.connect(ADDR)

while True:
    message = input("> ")
    if message == "!q":
        break
    else:
        client.send(message.encode())