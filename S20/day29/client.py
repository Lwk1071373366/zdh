# import os
# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9001))
#
# filepath = input('请输入文件路径：')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
# dic = {'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len = struct.pack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filepath,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()


# import os
# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9002))
#
# filepath = input('请输入路径:')      # 文件路径
# filename = os.path.basename(filepath)     #文件名
# filesize = os.path.getsize(filepath)            #文件大小
# dic = {'filename':filename,'filesize':filesize}      #文件名 文件大小  字典的形式
# str_dic = json.dumps(dic)                             #将字典转为字符串形式
# bytes_dic = str_dic.encode('utf-8')                   #将字符串转为字节
# len_dic = len(bytes_dic)                              #得到字典的长度
# bytes_len = struct.pack('i',len_dic)                  #得到字节的长度
# sk.send(bytes_len)                                    #传字节的长度
# sk.send(bytes_dic)                                    #传字典的长度
# with open(filesize,'rb') as f :                       #以rb形式打开这个文件
#     content = f.read()                                #读这个文件的大小
#     sk.send(content)
# sk.close()

# import os
# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9003))
# filepath = input('请输入文件路径：')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
# dic = {'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len = struct.pack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filesize,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()

# import os
# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
#
# filepath = input('请输入文件路径：')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
#
# dic ={'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len = struct.pack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filesize,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()
# import os
# import socket
# import json
# import struct
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# filepath = input('请输入文件路径')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
# dic = {'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len = struct.pack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filesize,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()
# import os,struct,json,socket
# sk= socket.socket()
# sk.connect(('127.0.0.1',9000))
# filepath = input('请输入文件路径：')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
# dic = {'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len =struct.unpack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filesize,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()
# import os,socket,json,struct
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# filepath = input('>>>')
# filename = os.path.basename(filepath)
# filesize = os.path.getsize(filepath)
# dic = {'filename':filename,'filesize':filesize}
# str_dic = json.dumps(dic)
# bytes_dic = str_dic.encode('utf-8')
# len_dic = len(bytes_dic)
# bytes_len = struct.unpack('i',len_dic)
# sk.send(bytes_len)
# sk.send(bytes_dic)
# with open(filesize,'rb') as f :
#     content = f.read()
#     sk.send(content)
# sk.close()