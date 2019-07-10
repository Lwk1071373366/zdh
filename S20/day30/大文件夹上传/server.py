import json
import socket
import struct

sk = socket.socket()
sk.bind(('127.0.0.1',9005))
sk.listen()

conn,addr = sk.accept()
len_bytes = conn.recv(4)

num = struct.unpack('i',len_bytes)[0]
str_dic = conn.recv(num).decode('utf-8')
dic = json.loads(str_dic)

with open(dic['filename'],'wb') as f :
    while dic['filesize']:
        content = conn.recv(2048)
        f.write(content)
        dic['filesize'] -= len(content)
    conn.close()
sk.close()





#
# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9003))
# sk.listen()
#
# conn,addr = sk.accept()
# len_bytes = conn.recv(4)
# num = struct.unpack('i',len_bytes)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
#
# with open(dic['filename'],'wb') as f:
#     while dic['filesize']:
#         content = conn.recv(2048)
#         f.write(content)
#         dic['filesize'] -= len(content)