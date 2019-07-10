# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9990))
# msg = sk.recv(1024)
# print(msg)
# # sk.send(b'666')
# sk.send(b'666')
# sk.close()


# import socket
# sk =socket.socket()
# sk.connect(('127.0.0.1',9000))
# msg = sk.recv(1024)
# print(msg)
# sk.send(b'666')
# sk.close()

# import socket
# sk = socket.socket()
# sk.connect(('192.168.16.59',9000))
# while True:
#     ret = sk.recv(1024).decode('utf-8')
#     if ret.upper() == 'Q':break
#     print(ret)
#     msg = input('>>>')
#     sk.send(msg.encode('utf-8'))
#     if msg.upper()=='Q':break
# sk.close()

# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# msg = sk.recv(1024)
# print(msg)
# sk.send(b'666')
# sk.close()

# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# msg = sk.recv(1024)
# print(msg)
# sk.send(b'666')
# sk.close()
# -----------------------------------------------------------  UDP

# import socket
# sk=socket.socket(type=socket.SOCK_DGRAM)
# server_addr =('127.0.0.1',9988)
# while True:
#     count = input('>>>')
#     if count.upper() == 'Q':break
#     sk.sendto(count.encode('utf-8'),server_addr)
#     msg= sk.recv(1024).decode('utf-8')
#     if msg.upper() =='Q':break
#     print(msg)
# sk.close()
# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# server_addr = ('127.0.0.1',9000)
# while True:
#     count = input('>>>')
#     if count.upper()=='Q':break
#     sk.sendto(count.encode('utf-8'),server_addr)
#     msg = sk.recv(1024).decode('utf-8')
#     if msg.upper()=='Q':break
#     print(msg)
# sk.close()

# import socket
# sk= socket.socket(type=socket.SOCK_DGRAM)
# server_addr = ('127.0.0.1',9000)
# while True:
#     count = input('>>>')
#     if count.upper() =='Q':break
#     sk.sendto(count.encode('utf-8'),server_addr)
#     msg = sk.recv(1024).decode('utf-8')
#     if msg.upper() == 'Q':break
#     print(msg)
# sk.close()

# import socket
# sk = socket.socket(type=socket.SOCK_DGRAM)
# server_addr = ('127.0.0.1',9000)
# while True:
#     count = input('>>>')
#     if count.upper() =='Q':break
#     sk.sendto(count.encode('utf-8'),server_addr)
#     msg = sk.recv(1024).decode('utf-8')
#     if msg.upper()=='Q':break
#     print(msg)
# sk.close()
# ---------------------------------------------------------------------------------------TCP登录
# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# while True:
#     username = input('请输入用户名：').strip().encode('utf-8')
#     password = input('请输入密码：').strip().encode('utf-8')
#     sk.send(username)
#     sk.send(password)
#     ret = sk.recv(1024).decode('utf-8')
#     print(ret)
# sk.close()














# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# while True:
#     username = input('请输入用户名：').strip().encode('utf-8')
#     password = input('请输入密码：').strip().encode('utf-8')
#     sk.send(username)
#     sk.send(password)
#     ret = sk.recv(1024).decode('utf-8')
#     print(ret)
# sk.close()