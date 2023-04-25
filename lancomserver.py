#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import socket
import threading
from colorist import Color

#Defines
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127."):
        print(f"{Color.RED}[ERROR]{Color.OFF} Machine's IP cannot be automatically pulled. Please provide the ip of the machine")
        ip = input("IP > ")
    return ip




#Config
PORT = 32222
LOCAL_HOST = "192.168.1.10" #get_ip()
ADDR = (LOCAL_HOST, PORT)
DISCONNECT_MESSAGE = "disconnect"


#Console Code

#Net Code

def handle_client(conn, addr):
    conected = True
    print(f"{Color.YELLOW}[NEW CONNECTION]{Color.OFF} {addr[0]} connected")
    while conected:
        try:  
            recived_data = conn.recv(1024).decode()
            if recived_data == DISCONNECT_MESSAGE:
                conected = False 
                print(f"{Color.YELLOW}[CONNECTION TERMINATED]{Color.OFF} {addr[0]} disconnected")
            else:
                print(f'[RECIVED DATA] "{recived_data}" from {addr[0]}')
        except ConnectionError:
            conected = False
            print(f"{Color.RED}[CONNECTION FORCEFULLY TERMINATED]{Color.OFF} {addr[0]} disconnected forcefully")
            


def listener():
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server listening on {LOCAL_HOST} and port {PORT} ...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


# Startup

listener()