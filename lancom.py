import socket

#Defines

connected = False
PORT = 32222
SERVER = input("Server's IP > ")
if SERVER == "!q":
    quit()
ADDR = (SERVER, PORT)


#Setup

client = socket.socket()
try:
    client.connect(ADDR)
    print(f"Succesfully connected to {SERVER}")
    connected = True
except OSError:
    print("Didnt fount that adress")

#Main loop

while True:
    message = input("> ").split()
    
    if len(message) > 1: 
        
        if message [0] == "connect":
            if connected == False:
                try:
                    client.connect(ADDR)
                    print(f"Succesfully connected to {SERVER}")
                    connected = True
                except OSError:
                    print("Didnt fount that adress")
            else:
                print("Youre already connected dumbass")

        elif message[0] == "send":
            if connected == True:
                if message [1] == "-s":
                    print("Youre in series send mode - to quit type !q")
                    while True: 
                        message = input("Send > ").split()
                        if message[0] == "!q":
                            break
                        else:
                            client.send((" ".join(message)).encode())
                else:    
                    to_send = []
                    for word in message:
                        to_send.append(word)
                    to_send.remove(message[0])
                    client.send((" ").join(to_send).encode())
            else:
                print("Youre not connected anywhere - use connect [ip]")

    elif message[0] == "disconnect":
        if connected == True:
            client.send((" ".join(message)).encode())
        else:
            print("Youre not connected anywhere - use connect [ip]")

    elif message[0] == "quit":
        if connected:
            client.send(str("disconnect").encode())
        break

    else:
        print("ERROR - User is a dumb bitch")