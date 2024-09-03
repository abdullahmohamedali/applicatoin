import threading
import socket

alies = input('who do you want to chat with: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9872))

def client_resive():
    while True:
        try:
            message = client.recv(1024)
            if message == "alies?":
                client.send(alies.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            client.close()
            break
def client_send():
    while True:
        message = f'{alies}: {input("")}'
        client.send(message.encode('utf-8'))
resive_thrade = threading.Thread(target=client_resive)
resive_thrade.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()
