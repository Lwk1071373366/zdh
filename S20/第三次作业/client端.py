import json
import struct
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))

path = input('请输入网址：')
str_dic = json.dumps(path)
bytes_dic = str_dic.encode('utf-8')
len_dic = len(bytes_dic)
bytes_len = struct.pack('i',len_dic)
sk.send(bytes_len)
sk.send(bytes_dic)
with open(path,'rb') as f :
    content = f.read()
    sk.send(content)
sk.close()