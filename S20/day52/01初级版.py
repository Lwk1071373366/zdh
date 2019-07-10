# # import socket                            #基础版
# #
# # server = socket.socket()
# # server.bind(('127.0.0.1',9000))
# # server.listen()
# #
# # conn,addr = server.accept()
# #
# # client_msg = conn.recv(1024)
# # print(client_msg.decode('utf-8'))
# # conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
# # conn.send(b'hello world')
#
#
# # import socket                               #并发版
# # from threading import Thread
# #
# # server = socket.socket()
# # server.bind(('127.0.0.1',9000))
# # server.listen()
# #
# #
# # def func(conn):
# #     client_msg = conn.recv(1024)
# #     print(client_msg.decode('utf-8'))
# #     conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
# #     conn.send(b'hello world!!')
# # while 1:
# #     conn, addr = server.accept()
# #     t = Thread(target=func,args=(conn,))
# #     t.start()
#
#
#
# import socket                            #进阶版
# from threading import Thread
# server = socket.socket()
# server.bind(('192.168.16.29',9091))
# server.listen()
#
#
# def func(conn):
#     client_msg = conn.recv(1024).decode('utf-8')
#     path = client_msg.split('\r\n')[0].split(' ')[1]
#     if path == '/':
#         conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#         with open('01进阶版.html','rb') as f :
#             date = f.read()
#         conn.send(date)
#         conn.close()
#     elif path == '/index.css':
#         conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#         with open('index.css','rb') as f :
#             date = f.read()
#         conn.send(date)
#         conn.close()
#     elif path == '/index.js':
#         conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#         with open('index.js','rb') as f :
#             date = f.read()
#         conn.send(date)
#         conn.close()
#     elif path == '/2.png':
#         conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#         with open('2.png','rb') as f :
#             date = f.read()
#         conn.send(date)
#         conn.close()
#     elif path == '/favicon.ico':
#         conn.send(b'HTTP/1.1 200 ok \r\n\r\n')
#         with open('favicon.ico','rb') as f :
#             date = f.read()
#         conn.send(date)
#         conn.close()
# while 1:
#     conn, addr = server.accept()
#     t = Thread(target=func, args=(conn,))
#     t.start()
def num():
    return [lambda x:i * x for i in range(4)]
print([(2)for m in num()])