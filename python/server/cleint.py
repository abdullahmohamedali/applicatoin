import socket

HEADER = 64
PORT = 5678
SERVER = '127.0.1.1'
FORMAT = 'utf-8'
DISSCONECTE = "!Dissconect"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_lenth = str(msg_length).encode(FORMAT)
    send_lenth += b' ' * (HEADER - len(send_lenth))
    client.send(send_lenth)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
