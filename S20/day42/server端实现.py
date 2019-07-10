# import socket
# server = socket.socket()
# server.bind(('127.0.0.1',9002))
# server.listen()
# conn,addr = server.accept()
# msg = conn.recv(1024)
# print(msg.decode('utf-8'))
# conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
# with open('html初识.html','rb') as f :
#     data = f.read()
# conn.send(data)
# conn.close()
# server.close()


# import socket
# server = socket.socket()
# server.bind(('127.0.0.1',9001))
# server.listen()
# conn,addr = server.accept()
# msg = conn.recv(1024)
# print(msg.decode('utf-8'))
# conn.send(b'HTTP/1.1 200 ok\r\n\r\n')
# with open('html初识.html','rb') as f :
#     data = f.read()
# conn.send(data)
# conn.close()
# server.close()


# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9003))
# sk.listen()
# conn,addr =sk.accept()
# msg=conn.recv(1024)
# print(msg.decode('utf-8'))
# conn.send(b'HTTP/1. 1 200 ok\r\n\r\n')
# with open('html初识.html','rb') as f :
#     data = f.read()
# conn.send(data)
# conn.close()
# sk.close()