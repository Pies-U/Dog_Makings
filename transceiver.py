import socket
import cv2
from colorist import Color

#Defines
cap = cv2.VideoCapture(0)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127."):
        print(f"{Color.RED}[ERROR]{Color.OFF} Machine's IP cannot be automatically pulled. Please provide the ip of the machine")
        ip = input("IP > ")
    return ip


#Config
PORT = 32222
DISCONNECT_MESSAGE = "disconnect"

mode = input("Recieve (r) or Send (s) data? > ")
if mode == "r" or "R":
    LOCAL_HOST = "192.168.1.10" #get_ip()
    ADDR = (LOCAL_HOST, PORT)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server listening on {LOCAL_HOST} and port {PORT} ...")
    while True:
        conn, addr = server.accept()
        conected = True
        print(f"{Color.YELLOW}[NEW CONNECTION]{Color.OFF} {addr[0]} connected")
        while conected:
            try:  
                recived_data = conn.recv(1024).decode()
                if recived_data == DISCONNECT_MESSAGE:
                    conected = False 
                    print(f"{Color.YELLOW}[CONNECTION TERMINATED]{Color.OFF} {addr[0]} disconnected")
                else:
                    frame = recived_data
                    cv2.imshow("Camera", frame)
            except ConnectionError:
                conected = False
                print(f"{Color.RED}[CONNECTION FORCEFULLY TERMINATED]{Color.OFF} {addr[0]} disconnected forcefully")

elif mode == "s" or "S":
    connected = False
    PORT = 32222
    SERVER = "192.168.1.20" #input("Server's IP > ")
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

    while connected:
        _, frame = cv2.read()
        client.send(frame)

else:
    print(f"{Color.YELLOW}[Warning]{Color.OFF} - User is a dumb bitch")
