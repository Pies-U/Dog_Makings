import socket
import threading

PORT = 32222
SERVER = "100.64.6.11"
ADDR = (SERVER, PORT)

client = socket.socket()
client.connect(ADDR)

while True:
    message = input("> ")
    if message == "!q":
        break
    else:
        client.send(message.encode())