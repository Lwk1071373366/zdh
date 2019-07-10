# import socketserver
# import time
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf8'))
#             print(conn.recv(1024).decode('utf-8'))
#             time.sleep(0.5)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
# server.serve_forever()

# import socketserver
# import time
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello$s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
# server.serve_forever()

# import  socketserver
# import time
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
#
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9001),Myserver)
# server.serve_forever()



import json
# import socket
# import struct
# import socketserver
#
# sk = socket.socket()
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn =self.request
#         len_bytes = conn.recv(4)
#         num = struct.unpack('i',len_bytes)[0]
#         str_dic = conn.recv(num).decode('utf-8')
#         dic = json.loads(str_dic)
#
#         with open(dic['filename'], 'wb') as f:
#             while dic['filesize']:
#                 content = conn.recv(2048)
#                 f.write(content)
#                 dic['filesize'] -= len(content)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9005),Myserver)
# server.serve_forever()

import time
for i in range(0,101,2):
     time.sleep(0.1)
     char_num = i//2      #打印多少个'*'
     per_str = '\r%s%% : %s\n' % (i, '*' * char_num) if i == 100 else '\r%s%% : %s'%(i,'*'*char_num)
     print(per_str,end='', flush=True)


















