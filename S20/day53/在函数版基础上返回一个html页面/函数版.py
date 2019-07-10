import socket    #进阶版
import time
from threading import Thread
server = socket.socket()
server.bind(('127.0.0.1',9091))
server.listen()


def html(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('01进阶版.html', 'rb') as f:
        date = f.read()
    conn.send(date)
    conn.close()
def css(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('index.css', 'rb') as f:
        date = f.read()
    conn.send(date)
    conn.close()
def js(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('index.js', 'rb') as f:
        date = f.read()
    conn.send(date)
    conn.close()
def ico(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('favicon.ico', 'rb') as f:
        date = f.read()
    conn.send(date)
    conn.close()
def png(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    with open('2.png', 'rb') as f:
        date = f.read()
    conn.send(date)
    conn.close()
def home(conn):
    conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
    current_time = str(time.time())                #动态效果，用时间模拟
    with open('home.html', 'r',encoding='utf-8') as f:
        data = f.read()
        data = data.replace('双击666',current_time)
    conn.send(data.encode('utf-8'))
    conn.close()
urlpatterns=[
    ('/',html),
    ('/index.css',css),
    ('/index.js',js),
    ('/favicon.ico',ico),
    ('/2.png',png),
    ('/home.html',home)
]

def func(conn):
    client_msg = conn.recv(1024).decode('utf-8')
    path = client_msg.split('\r\n')[0].split(' ')[1]
    for urlpattern in urlpatterns:
        if urlpattern[0] == path:
            # urlpattern[1](conn)
            t = Thread(target=urlpattern[1],args=(conn,))   #多线程提高每个请求的并发效果
            t.start()
while 1:   # 多线程接收请求
    conn, addr = server.accept()
    t = Thread(target=func, args=(conn,))
    t.start()