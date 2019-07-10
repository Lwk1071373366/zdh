from socket import *
from threading import Thread
def client(ipport):
    c = socket(AF_INET,SOCK_STREAM)
    c.connect(ipport)
    while True:
        try:
            # res = input('>>').strip()
            # if not res:continue
            res = 'hello'
            c.send(res.encode('utf-8'))
            ree = c.recv(1024).decode('utf-8')
            print(ree)
        except Exception:break
    c.close()

if __name__ == '__main__':
        ipport = ('127.0.0.1',8080,)
        for i in range(500):
            t = Thread(target=client,args=(ipport,))
            t.start()

client