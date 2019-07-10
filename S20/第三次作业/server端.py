import json
import struct
import socket
from urllib.request import urlopen
sk = socket.socket()
sk.bind(('127.0.0.1',9001))
sk.listen()

conn,addr = sk.accept()
num = conn.recv(4)
num = struct.unpack('i',num)[0]
str_dic = conn.recv(num).decode('utf-8')
dic = json.loads(str_dic)
with open(str_dic,'wb') as f :
    content = conn.recv(str_dic)
    f.write(content)
conn.close()
sk.close()