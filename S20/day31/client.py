from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',9005))


while True:
    msg=input('>>: ').strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    msg=client.recv(1024)
    print(msg.decode('utf-8'))
#
# import socket
# sk =socket.socket()
# sk.connect(('127.0.0.1',9000))
# msg = sk.recv(1024)
# print(msg)
# sk.send(b'666')
# sk.close()