# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9001))
# sk.listen()
#
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
#
# conn.close()
# sk.close()


# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9002))
# sk.listen()
#
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import json
# import struct
# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# # print(conn)
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import socket
# import json
# import struct
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# num = sk.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.rece(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import json
# import struct
# import socket
#
# sk= socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# num = sk.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filesize'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import json
# import socket
# import struct
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filesize'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import socket
# import json
# import struct
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic =conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write()
# conn.close()
# sk.close()

# import socket
# import json
# import struct
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# num =conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()

# import json,socket,struct
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# conn,addr = sk.accept()
# num = conn.recv(4)
# num = struct.unpack('i',num)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     content = conn.recv(dic['filesize'])
#     f.write(content)
# conn.close()
# sk.close()
