import os
import sys
import json
import struct
import socket
import hashlib

upload_path = r'地址'
def get_md5(usr,pwd):
    md5 = hashlib.md5(usr.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()
def pro_recv(conn):
    num = conn.recv(4)
    num = struct.unpack('i',num)[0]
    str_dic = conn.recv(num).decode('utf-8')
    dic = json.loads(str_dic)
    return dic
def pro_send(conn,dic,pro = True):
    bytes_dic = json.dumps(dic).encode('utf-8')
    if pro:
        len_bytes = struct.pack('i',len(bytes_dic))
        conn.send(len_bytes)
    conn.send(bytes_dic)
def login(conn):
    dic = pro_recv(conn)
    with open('userinfo',encoding='utf-8') as f :
        for line in f :
            user,pwd = line.strip().split('|')
            if user == dic['user'] and pwd == get_md5(dic['user'],dic['passwd']):
                return {'opt':'login','flag':True}
        else:
            return {'opt':'login','flag':False}
def upload(dic,conn):
    file_path = os.path.join(upload_path,dic['filename'])
    with open(file_path,'wb') as f :
        while dic['filesize']:
            content = conn.recv(2048)
            f.write(content)
            dic['filesize'] -= len(content)
def download(dic,conn):
    path = os.path.join(upload_path,dic['filename'])
    if os.path.isfile(path):
        filesize = os.path.getsize(path)
        dic = {'filename':filesize,'exist':True}
        pro_send(conn,dic)
        with open(path,'rb') as f :
            while filesize >2048:
                content = f.read(2048)
                conn.send(content)
                filesize -= len(content)
            else:
                content = f.read()
                conn.send(content)
    else:
        dic = {'exist':False}
        pro_send(conn,dic)
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
conn,_ = sk.accept()
ret = login(conn)
bytes_ret = json.dumps(ret).encode('utf-8')
conn.send(bytes_ret)
if ret['flag']:
    while True:
        dic = pro_recv(conn)
        if hasattr(sys.modules[__name__],dic['operate']):
            getattr(sys.modules[__name__],dic['operate'])(dic,conn)
else:
    conn.close()