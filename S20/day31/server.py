from socket import *
from multiprocessing import Process

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',9005))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if  __name__ == '__main__': #windows下start进程一定要写到这下面
    while True:
        conn,client_addr=server.accept()
        p = Process(target=talk,args=(conn,client_addr))
        p.start()
# import socket
# sk =socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()