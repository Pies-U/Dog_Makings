#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import socket
import threading
import time

#Defines
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Control Variables 
server_online = True
close_connections = False


#Console Config


#Net Config
PORT = 32222
LOCAL_HOST = "192.168.1.10"
ADDR = (LOCAL_HOST, PORT)

#Console Code

#Net Code

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]} connected")
    while True:
        recived_data = conn.recv(1024).decode()
        print(f'[RECIVED DATA] "{recived_data}" from {addr[0]}')
        if close_connections == True:
            conn.close()


def listener():
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server listening on {LOCAL_HOST} and port {PORT} ...")
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()


# Startup

listener()