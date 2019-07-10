import socket
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))
msg,addr = sk.recvfrom(1024)
msg = msg.decode('utf-8')
dic = {addr:[msg]}
print(dic)
sk.close()


import socket
sk =socket.socket(type=socket.SOCK_DGRAM)
server_addr = ('127.0.0.1',9000)
msg = input('>>>')
sk.sendto(msg.encode('utf-8'),server_addr)
sk.close()



