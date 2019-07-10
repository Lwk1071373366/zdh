import os
import json
import struct
import socket
download_path =r'地址'

def pro_send(sk,dic,pro = True):
    bytes_dic = json.dumps(dic).encode('utf-8')
    if pro:
        len_bytes = struct.pack('i',len(bytes_dic))
        sk.send(len_bytes)
    sk.send(bytes_dic)
def pro_recv(sk,pro = True,num = 1024):
    if pro :
        num = sk.recv(4)
        num = struct.unpack('i',num)[0]
    str_dic =sk.recv(num).docode('utf-8')
    dic = json.loads(str_dic)
    return dic
def upload(sk):
    file_path = input('路径')
    if os.path.isfile(file_path):
        filename = os.path.basename(file_path)
        filesize = os.path.getsize(file_path)
        dic = {'filename':filename,'filesize':filesize,'operate':'upload'}
        pro_send(dic)
        with open(file_path,'rb') as f :
            while filesize >2048:
                content = f.read(2048)
                sk.send(content)
                filesize -= len(content)
            else:
                content = f.read()
                sk.send(content)
        print('上传成功')
    else:
        print('文件路径不存在')
def download(sk):
    filename = input('文件名')
    dic = {'filename':filename,'operate':'download'}
    pro_send(sk,dic)
    ret = pro_recv(sk)
    if ret['exist']:
        file_path = os.path.join(download_path,filename)
        with open(file_path,'rb') as f :
            while ret['filesize']:
                content = sk.recv(2048)
                f.write(content)
                ret['filesize'] -=len(content)
        print('下载成功')
    else:
        print('你 要下载的文件不存在')
def login2():
    username = input('user')
    password = input('pwd')
    dic = {'user':username,'pwd':password,'operate':'login'}
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    pro_send(sk,dic)
    dic_ret = pro_recv(sk,pro = False)
    if dic_ret['opt'] == 'login' and dic_ret['flag']:
        print('登录成功')
    else:
        print('登录失败')
        sk.close()
    return sk,dic_ret['flag']
sk,flag = login2()
while flag:
    operate = [('上传',upload),('下载',download)]
    for ind,opt in enumerate(operate,1):
        print(ind,opt[0])
    num = int(input('请输入你的操作'))
    operate[num-1][1](sk)