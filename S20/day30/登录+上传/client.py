import os
import json
import socket
import struct

def upload(sk):
    file_path = input('>>>')
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)
    dic = {'filename':filename,'filesize':filesize}
    bytes_dic = json.dumps(dic).encode('utf-8')
    len_bytes = struct.pack('i',len(bytes_dic))
    sk.send(len_bytes)
    sk.send(bytes_dic)

    with open(file_path,'rb') as f :
        while filesize > 2048:
            content = f.read(2048)
            sk.send(content)
            filesize -= 2048
        else:
            content = f.read()
            sk.send(content)
# def download(sk):
#     file_path = input('>>>')
#     filename = os.path.basename(file_path)
#     filesize = os.path.getsize(file_path)
#     dic = {'filename':filename,'filesize':filesize}
#     bytes_dic = json.dumps(dic).encode('utf-8')
#     len_bytes = struct.pack('i',len(bytes_dic))
#     sk.recv(len_bytes)
#     sk.recv(bytes_dic)
#
#     with open(file_path,'wb') as f :
#         while filesize > 2048:
#             content = f.read(2048)
#             sk.recv(content)
#             filesize -= 2048
#         else:
#             content = f.read()
#             sk.recv(content)
usr = input('username')
pwd = input('password')
dic = {'operate':'login','user':usr,'passwd':pwd}
bytes_dic =json.dumps(dic).encode('utf-8')
sk = socket.socket()
sk.connect(('127.0.0.1',9999))
sk.send(bytes_dic)

res = sk.recv(1024).decode('utf-8')
dic =json.loads(res)
if dic['flag']:
    print('登录成功')
    upload(sk)
else:
    print('登录失败')
sk.close()