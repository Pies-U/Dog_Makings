import socket
import time
from colorist import Color

#Defines

connected = False
PORT = 32222
SERVER = "192.168.1.10" #input("Server's IP > ")
if SERVER == "quit":
    quit()
ADDR = (SERVER, PORT)
commands = ["disconnect","connect","quit","cls"]

#Setup

client = socket.socket()
try:
    client.connect(ADDR)
    print(f"Succesfully connected to {SERVER}")
    connected = True
except OSError:
    print(f"{Color.RED}[ERROR]{Color.OFF} Didnt found that adress")

def is_socket_connected(sock):
    try:
        sock.setblocking(False)
        sock.send(b"")
        return True
    except (BlockingIOError, ConnectionAbortedError):
        return True
    except OSError:
        return False


#Main loop

while True:
    try:
        message = input("> ").split()
    
        if len(message) > 1: 
        
            if message [0] == "connect":
                if connected == False:
                    try:
                        client.connect(ADDR)
                        print(f"Succesfully connected to {SERVER}")
                        connected = True
                    except OSError:
                        print(f"{Color.RED}[ERROR]{Color.OFF} Didnt found that adress")
                else:
                    print(f"{Color.YELLOW}[Warning]{Color.OFF} Youre already connected dumbass")

            elif message[0] == "send":
                if connected == True:
                    if message [1] == "-s":
                        print("Youre in series send mode - to quit type !q")
                        while True: 
                            message = input("Send > ").split()
                            try:
                                if message[0] == "!q":
                                    break
                            except IndexError:
                                print(f"{Color.YELLOW}[Warning]{Color.OFF} You need to incert a message")
                            else:
                                client.send((" ".join(message)).encode())
                    elif message[1] in commands:
                        print(f"{Color.YELLOW}[Warning]{Color.OFF} - User is a dumb bitch - you don't use control commands in send you stupid dumb fuck - go stir some gel using a wooden spatula")
                    else:    
                        to_send = []
                        for word in message:
                            to_send.append(word)
                        to_send.remove(message[0])
                        client.send((" ").join(to_send).encode())
                else:
                    print(f"{Color.YELLOW}[Warning]{Color.OFF} Youre not connected anywhere - use connect [ip]")

        elif message[0] == "disconnect":
            if connected == True:
                client.send((" ".join(message)).encode())
                print(f"Succesfully disconnected from {SERVER}")
                connected = False
            else:
                print(f"{Color.YELLOW}[Warning]{Color.OFF} Youre not connected anywhere - use connect [ip]")

        elif message[0] == "quit":
            if connected:
                client.send(str("disconnect").encode())
            print(f"{Color.RED}Task Failed Succesfully{Color.OFF}")
            break

        elif message[0] == "cls":
            print('\x1bc')

        elif message[0] == "help":
            print("")
            print("Usage:")
            print("connect [ip]      : Connects to the server with the given IP.")
            print("send [message]    : Sends the given message to the connected server.")
            print("                    Use -s option for sending messages in series.")
            print("disconnect        : Disconnects from the currently connected server.")
            print("quit              : Quits the program after disconnecting (if connected).")
            print("cls               : Clears the screen.")
            print("")
        
        #Command not found
        else:
            print(f"{Color.YELLOW}[Warning]{Color.OFF} - User is a dumb bitch")

    except (ConnectionResetError, ConnectionAbortedError, socket.timeout):
        print(f"{Color.RED}[ERROR]{Color.OFF} Lost connection to server. Reconnecting...")
        time.sleep(5)
        client.connect(ADDR)
        if is_socket_connected(client) == True:
            print(f"Successfully reconnected to {SERVER}")
        else:
            print(f"{Color.RED}[ERROR]{Color.OFF} Lost connection to server. Reconnecting Failed")
            time.sleep(5)