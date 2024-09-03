import threading
import socket
host = '127.0.0.1'
port = 9872

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
clinets = []
aliass = []


def broudcast(message):
    for client in clinets:
        client.send(message)
def handle_client(client):
    while True:
        client.send(f'{input("")}'.encode("utf-8"))
        try:
            message = client.recv(1024)
            print(message)
            
        except:
            index = clinets.index(client)
            clinets.remove(client)
            client.close()
            alias = aliass[index]
            broudcast(f'{alias} has left the chat room!'.encode('utf-8'))

            

def resive():
    print('server is running and listening....')
    while True:
        client, address = server.accept()
        print(f' {str(address)}  has joind')
        client.send('alise? '.encode("utf-8"))
        alias = client.recv(1024)
        print(f'{alias}')
        thred = threading.Thread(target=handle_client, args=(client,))
        thred.start()
def all():
    resive()
if __name__ == "__main__":
    all()



        