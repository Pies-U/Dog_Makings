import socket
import threading

PORT = 32222
LOCAL_HOST = socket.gethostbyname(socket.gethostname())
ADDR = (LOCAL_HOST, PORT)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    while True:
        recived_data = conn.recv(1024).decode()
        print(f'[RECIVED DATA] "{recived_data}" from {addr}')

def startup():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server listening on {LOCAL_HOST} and port {PORT} ...")
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()

startup()

