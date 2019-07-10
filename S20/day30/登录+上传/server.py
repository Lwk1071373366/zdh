import json
import socket
import struct
import hashlib
def get_md5(usr,pwd):
    md5 = hashlib.md5(usr.encode('utf-8'))
    md5.update(pwd.encode('utf-8'))
    return md5.hexdigest()
def login(conn):
    msg = conn.recv(1024).decode('utf-8')
    dic = json.loads(msg)
    with open('userinfo',encoding='utf-8') as f :
        for line in f :
            username,password = line.strip().split('|')
            if username == dic['user'] and password ==get_md5(dic['user'],dic['passwd']):
                res = json.dumps({'flag':True}).encode('utf-8')
                conn.send(res)
                return True
        else:
            res = json.dumps({'flag':False}).encode('utf-8')
            conn.send(res)
            return False
def upload(conn):
    len_bytes = conn.recv(4)
    num = struct.unpack('i',len_bytes)[0]
    str_dic = conn.recv(num).decode('utf-8')
    dic = json.loads(str_dic)
    with open(dic['filename'],'wb') as f :
        while dic['filesize'] :
            content = conn.recv(2048)
            f.write(content)
            dic['filesize'] -=len(content)
sk =socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen()
while True:
    try:
        conn,addr = sk.accept()
        ret = login(conn)
        if ret:
            upload(conn)
    except Exception as e :
        print(e)
    finally:
        conn.close()
sk.close()