import socket
import threading
#youtube lin vidio https://www.youtube.com/watch?v=3QiPPX-KeSc


HEADER = 64
PORT = 5678
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISSCONECTE = "!Dissconect"

#starting server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handele_client(conn, addr):
    print(f"[new connection] {addr} connected")

    connected = True
    while connected:            
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISSCONECTE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handele_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

print("starting...")
start()