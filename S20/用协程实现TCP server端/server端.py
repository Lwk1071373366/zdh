# from gevent import monkey;monkey.patch_all()
# from socket import *
# import gevent
# def sever(ipport):
#     s = socket(AF_INET,SOCK_STREAM)
#     s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#     s.bind(ipport)
#     s.listen(5)
#     while True:
#         cnn, addr = s.accept()
#         print('%s is from %s'%(cnn, addr))
#         gevent.spawn(talk, cnn,addr)
#     s.close()
# def talk(cnn,addr):
#     while True:
#         try:
#             res = cnn.recv(1024).decode('utf-8')
#             cnn.send(res.upper().encode('utf-8'))
#         except Exception:break
#     cnn.close()
#
# if __name__ == '__main__':
#     ipport = ('127.0.0.1', 8080,)
#     sever(ipport)
#
# sever

