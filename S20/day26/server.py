# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9990))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'shaungji666')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()


# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()

# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()

# import socket
# sk= socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()
# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# conn.send(b'hello')
# msg = conn.recv(1024)
# print(msg.decode('utf-8'),addr)
# conn.close()
# sk.close()
# import socket
# sk = socket.socket()
# sk.bind(('192.168.16.59',9000))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     while True:
#         msg = input('>>>')
#         conn.send(msg.encode('utf-8'))
#         if msg.upper() == 'Q':
#             break
#         content = conn.recv(1024).decode('utf-8')
#         if content.upper() == 'Q':break
#         print(content)
#     conn.close()
# sk.close()
# ---------------------------------------------------------------------------------------UDP


# import socket
#
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1',9988))
# while True:
#     msg,client_addr = sk.recvfrom(1024)
#     print(msg.decode('utf-8'))
#     msg = input('>>>')
#     sk.sendto(msg.encode('utf-8'),client_addr)
# sk.close()

# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1',9000))
# while True:
#     msg,client_addr = sk.recvfrom(1024)
#     print(msg.decode('utf-8'))
#     msg = input('>>>')
#     sk.sendto(msg.encode('utf-8'),client_addr)
# sk.close()
# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1',9000))
# while True:
#     msg,client_addr = sk.recvfrom(1024)
#     print(msg.decode('utf-8'))
#     msg = input('>>>')
#     sk.sendto(msg.encode('utf-8'),client_addr)
# sk.close()

# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# sk.bind(('127.0.0.1',9000))
# while True:
#     msg ,client_addr = sk.recvfrom(1024)
#     print(msg.decode('utf-8'))
#     msg = input('>>>')
#     sk.sendto(msg.encode('utf-8'),client_addr)
# sk.close()
# -------------------------------------------------------------------------------------TCP登录
# import socket
# # import hashlib
# # def md5(pwd):
# #     md5 = hashlib.md5()
# #     md5.update(pwd.encode('utf-8'))
# #     pwd= md5.hexdigest()
# #     return pwd
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     while True:
#         username = conn.recv(1024).decode('utf-8')
#         password = conn.recv(1024).decode('utf-8')
#         with open('info','r',encoding='utf-8') as f :
#             for line in f:
#                 user,pwd = line.strip().split('|')
#                 if user == username and pwd == password:
#                     conn.send('登录成功'.encode('utf-8'))
#                 else:
#                     conn.send('登录失败'.encode('utf-8'))
#     conn.close()
# sk.close()












# import socket
# import hashlib
# def md5(user,pwd):
#     md5 = hashlib.md5(user.encode('utf-8'))
#     md5.update(pwd.encode('utf-8'))
#     pwd= md5.hexdigest()
#     return pwd
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     while True:
#         username = conn.recv(1024).decode('utf-8')
#         password = conn.recv(1024).decode('utf-8')
#         with open('info','r',encoding='utf-8') as f :
#             for line in f:
#                 user,pwd = line.strip().split('|')
#                 if user == username and md5(user,pwd)== password:
#                     conn.send('登录成功'.encode('utf-8'))
#                 else:
#                     conn.send('登录失败'.encode('utf-8'))
#     conn.close()
# sk.close()












