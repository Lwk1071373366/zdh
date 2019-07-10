import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9001))
while True:
    msg = sk.recv(1024)
    print(msg)
    sk.send('我是一号'.encode('utf-8'))
sk.close()





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
