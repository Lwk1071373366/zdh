# Day13作业及默写
# 1.
# 整理今天的博客，写课上代码，整理流程图。
# 2.
# 写一个函数完成三次登陆功能：
# a.用户的用户名密码从一个文件register中取出。
# b.register文件包含多个用户名，密码，用户名密码通过 | 隔开，每个人的用户名密码占用文件中一行。
# c.完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# d.登陆成功返回True。
# def func():
#     count=0
#     while count < 3:
#         username=input('请输入用户名：a/b/c').strip()
#         password=input('请输入密码：').strip()
#         with open('register','r',encoding='utf-8') as f:
#             for line in f:
#                 line=line.strip()
#                 x,y = line.split('|')
#                 if username == x and password== y:
#                     return True
#             count+=1
#             print('登录失败')
#     return False
# ret=func()
# if ret :
#     print('ok')
# else:
#     print('no')
# def func():
#     count = 0
#     while count < 3:
#         username=input('请输入用户名：').strip()
#         password=input('请输入密码：').strip()
#         with open('register','r',encoding='utf-8') as f:
#             for line in f:
#                 line=line.strip()
#                 x,y=line.split('|')
#                 if username==x and password == y:
#                     return True
#             count+=1
#             print('登录失败')
#     return False
# ret=func()
# if ret:
#     print('ok')
# else:
#     print('no')
# def func():
#     count = 0
#     while count < 3:
#         username=input('请输入用户名：').strip()
#         password=input('请输入密码：').strip()
#         with open('register','r',encoding='utf-8') as f:
#             for line in f :
#                 line = line .strip()
#                 x,y=line.split('|')
#                 if username==x and password==y:
#                     return True
#             count+=1
#             print('登录失败')
#     return False
# ret=func()
# if ret:
#     print('ok')
# else:
#     print('no')
# 再写一个函数完成注册功能：
# (1)
# 用户输入用户名密码注册。
# (2)
# 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# (3)
# 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# (4)
# 注册成功后，返回True, 否则返回False。
# def register():
#     username=input('请输入用户名：').strip()
#     password=input('请输入密码：').strip()
#     with open('register','r+',encoding='utf-8') as f:
#         for line in f :
#             line=line.strip()
#             x,y=line.split('|')
#             if username==x:
#                 print('用户名已存在，请重新注册')
#                 break
#         else:
#             f.write('')



# 明日默写:
# 写一个装饰器, 求运行时间
# 写一个匿名函数
import time

# def func():
#     strat_time=time.time()
#     print('666')
#     time.sleep(3)
#     print(time.time()-strat_time)
# func()
# def func():
#     strat_time=time.time()
#     print('6666')
#     time.sleep(4)
#     print(time.time()-strat_time)
# func()
# l1=[1,2,3,4,5]
# def func(i):
#     return i*i
# print(list(map(func,l1)))

# print(list(map(lambda x:x+10,l1)))

# def my_abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x
# print(my_abs(-99))