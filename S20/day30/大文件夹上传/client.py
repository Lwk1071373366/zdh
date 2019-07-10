import os
import struct
import socket
import json

sk = socket.socket()
sk.connect(('127.0.0.1',9005))
filepath = input('>>>')
filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic)
bytes_dic = str_dic.encode('utf-8')
len_dic = len(bytes_dic)
bytes_len = struct.pack('i',len_dic)
sk.send(bytes_len)
sk.send(bytes_dic)
with open(filepath,'rb') as f :
    while filesize >2048:
        content = f.read(2048)
        sk.send(content)
        filesize -= 2048
    else:
        content = f.read()
        sk.send(content)
sk.close()




import os
import json
import struct
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9003))

# file_path = input('>>>')
# filename = os.path.basename(file_path)
# filesize = os.path.getsize(file_path)
# dic = {'filename':filename,'filesize':filesize}
# bytes_dic = json.dumps(dic).encode('utf-8')
#
# len_bytes = struct.pack('i',len(bytes_dic))
# sk.send(len_bytes)
# sk.send(bytes_dic)
#
# with open(file_path,'rb') as f:
#     while filesize > 2048:
#         content = f.read(2048)
#         sk.send(content)
#         filesize -= 2048
#     else:
#         content = f.read()
#         sk.send(content)
#
# sk.close()
# 175,060,348
# 152,117,248