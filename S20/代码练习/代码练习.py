# import hashlib
# md5 = hashlib.md5('alex'.encode('utf-8'))    #加盐了
# md5.update('alex3714'.encode('utf-8'))
# print(md5.hexdigest())

# import  hashlib
# md5 = hashlib.md5('alex'.encode('utf-8'))
# md5.update('alex3717'.encode('utf-8'))
# print(md5.hexdigest())

#client端：

# import socket
# sk =socket.socket()
# sk.connect(('127.0.0.1',9000))
# while True:
#     msg = sk.recv(1024)
#     print(msg)
#     sk.send(b'byebye')
# sk.close()
#
# #server端：
#
import time
# import socketserver
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()



# import time
# import socketserver
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()
#
#
# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
#
# while True:
#     msg = sk.recv(1024)
#     print(msg)
#     sk.send(b'byebye')
# sk.close()

# import socketserver
# import time
#
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()

# import socketserver
# import time
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         for i in range(200):
#             conn.send(('hello%s'%i).encode('utf-8'))
#             print(conn.recv(1024))
#             time.sleep(1)
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()

#client端：
# import os
# import struct
# import socket
# import json
#
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# filepath = input('>>>')
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
#     while filesize > 2048:
#         content = f.read(2048)
#         sk.send(content)
#         filesize -= 2048
#     else:
#         content = f.read()
#         sk.send(content)
# sk.close()


#server端：
# import socket
# import struct
# import json
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# len_bytes = conn.recv(4)
# num = struct.unpack('i',len_bytes)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename'],'wb') as f :
#     while dic['filesize']:
#         content = conn.recv(2048)
#         f.write(content)
#         dic['filesize'] -=len(content)
#     conn.close()
# sk.close()

# import socket
# import struct
# import json
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# conn,addr = sk.accept()
# len_bytes = conn.recv(4)
# num = struct.unpack('i',len_bytes)[0]
# str_dic = conn.recv(num).decode('utf-8')
# dic = json.loads(str_dic)
# with open(dic['filename','wb']) as f :
#     while dic['dilesize']:
#         content = conn.recv(2048)
#         f.write(content)
#         dic['filesize'] -=len(content)
#         conn.close()
# sk.close()

# import hashlib
# import pickle
# import os
# import sys
#
# class Course:
#     def __init__(self,name,price,period,teacher):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.teacher = teacher
# class User(object):
#     def show_courses(self):
#         with open('course_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     course = pickle.load(f)
#                     print('%s %s,%s,%s,%s'%(count,course.name,course.price,course.period,course.teacher))
#                     count += 1
#                 except EOFError:
#                     print()
#                     break
# class Manager(User):
#     opt_lst = [('创建课程', 'create_course'), ('给学生创建账号', 'create_student'),
#                ('查看所有课程', 'show_courses'), ('查看所有学生', 'show_students'),
#                ('查看所有学生的选课情况', 'show_students_courses'), ('退出', 'quit')]
#     def __init__(self,name):
#         self.name = name
#     def create_course(self):
#         print('in Manager create_course')
#         course_name = input('课程名：')
#         price = input('课程价格：')
#         period = input('课程周期：')
#         teacher = input('授课老师：')
#         course = Course(course_name,price,period,teacher)
#         with open('course_info','ab') as f :
#             pickle.dump(course,f)
#         print('创建%s课程成功\n'%course_name)
#     def create_student(self):
#         print('in Manager create_student')
#         username = input('用户名 ')
#         password = input('密码')
#         with open('userinfo','a',encoding='utf-8') as f :
#             f.write('%s|%s|Student\n'%(username,get_md5(username,password)))
#         stu = Student(username)
#         with open('student_info','ab') as f :
#             pickle.dump(stu,f)
#         print('创建%s学生账号成功\n'%username)
#     def show_students(self):
#         print('in Manager show_student')
#         with open('student_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     student = pickle.load(f)
#                     print('%s %s'%(count,student.name))
#                     count += 1
#                 except EOFError:
#                     print()
#                     break
#     def show_students_courses(self):
#         print('in Manager show_students_courses')
#         with open('student_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     stu = pickle.load(f)
#                     name_lst = [course.name for course in stu.courses]
#                     print('%s %s:%s'%(count,stu.name,','.join(name_lst)))
#                     count +=1
#                 except EOFError:
#                     break
#     @classmethod
#     def init(cls,username):
#         managet = cls(username)
#         return managet
#     def quit(self):
#         exit()
# class Student(User):
#     opt_lst = [('查看所有课程', 'show_courses'), ('查看已选课程', 'show_selected_course'),
#                ('选择课程', 'choose_course'), ('退出', 'quit')]
#     def __init__(self,name):
#         self.name = name
#         self.course = []
#     def show_selected_course(self):
#         print('in Student show_selected_course' )
#         for index,course in enumerate(self.course,1):
#             print('%s %s,%s,%s,%s'%(index,course.name,course.price,course.period,course.teacher))
#     def choose_course(self):
#         print('in Student choose_course')
#         flag = False
#         self.show_courses()
#         num = int(input('请输入序号'))
#         with open('course_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     obj = pickle.load(f)
#                     if count == num :
#                         self.course.append(obj)
#                         flag = True
#                         break
#                     count +=1
#                 except EOFError:
#                     print('请输入课程编号：')
#                     break
#         if flag:
#             print('选择%s课程成功'% obj.name)
#             with open('student_info','rb') as f1,open('student_info.bak','wb') as f2:
#                 while True:
#                     try:
#                         obj = pickle.load(f1)
#                         if obj.name == self.name:
#                             pickle.dump(self,f2)
#                         else:
#                             pickle.dump(obj,f2)
#                     except EOFError:
#                         break
#             os.remove('student_info')
#             os.rename('student_info.bak','student_info')
#     @staticmethod
#     def init(name):
#         with open('student_info','rb') as f :
#             while True:
#                 try:
#                     stu = pickle.load(f)
#                     if stu.name == name:
#                         return stu
#                 except EOFError:
#                     break
#     def quit(self):
#         exit()
# def get_md5(usr,pwd):
#     md5 = hashlib.md5(usr.encode('utf-8'))
#     md5.update(pwd.encode('utf-8'))
#     return md5.hexdigest()
# def login(usr,pwd):
#     with open('userinfo',encoding='utf-8') as f :
#         for line in f :
#             username,password ,ident = line.strip().split('|')
#             if usr == username and get_md5(usr,pwd) == password:
#                 return {'result':True,'identify':ident,'username':usr}
#             else:
#                 return {'result':False}
# def auth():
#     opt_lst1 = ['登录','退出']
#     while True:
#         for index,opt in enumerate(opt_lst1,1):
#             print(index,opt)
#         num = int(input('请输入你要做的操作：'))
#         if num == 1:
#             usr = input('username:')
#             pwd = input('password:')
#             ret = login(usr,pwd)
#             if ret ['result']:
#                 print('登录成功')
#                 return ret
#             else:
#                 print('登录失败')
#         elif num ==2:
#             exit()
# ret = auth()
# print(ret)
# if ret['result']:
#     if hasattr(sys.modules[__name__],ret['identify']):
#         cls = getattr(sys.modules[__name__],ret['identify'])
#         obj = cls(ret['username'])
#         while True:
#             for index,opt in enumerate(cls.opt_lst,1):
#                 print(index,opt[0])
#             num = int(input('请输入你要操作的序号：'))
#             if hasattr(obj,cls.opt_lst[num-1][1]):
#                 getattr(obj,cls.opt_lst[num-1][1])()
# -----------------------------------------------------------------------------------
#server端：
# import json
# import socket
# import struct
# import hashlib
#
# def get_md5(usr,pwd):
#     md5 = hashlib.md5(usr.encode('utf-8'))
#     md5.update(pwd.encode('utf-8'))
#     return md5.hexdigest()
# def login(conn):
#     msg = conn.recv(1024).decode('utf-8')
#     dic = json.loads(msg)
#     with open('userinfo',encoding='utf-8') as f :
#         for line in f :
#             username,password = line.strip().split('|')
#             if username ==dic['user'] and password ==get_md5(dic['user'],dic['passwd']):
#                 res = json.dumps({'flag':True}).encode('utf-8')
#                 conn.send(res)
#                 return True
#         else:
#             res = json.dumps({'flag':False}).encode('utf-8')
#             conn.send(res)
#             return False
# def update(conn):
#     len_bytes = conn.recv(4)
#     num = struct.unpack('i',len_bytes)[0]
#     str_dic = conn.recv(num).decode('utf-8')
#     dic = json.loads(str_dic)
#     with open(dic['filename'],'wb') as f :
#         while dic ['filesize'] :
#             content = conn.recv(2048)
#             f.write(content)
#             dic['filesize'] -= len(content)
# sk = socket.socket()
# sk.bind(('127.0.0.1',9999))
# sk.listen()
# while True:
#     try:
#         conn,addr = sk.accept()
#         ret = login(conn)
#         if ret :
#             update(conn)
#     except Exception as e:
#         print(e)
#     finally:
#         conn.close()
# sk.close()
#client端：
# import os
# import struct
# import json
# def upload(sk):
#     filepath = input('>>>')
#     filename = os.path.basename(filepath)
#     filesize = os.path.getsize(filepath)
#     dic ={'filename':filename,'filesize':filesize}
#     bytes_dic =json.dumps(dic).encode('utf-8')
#
# ---------------------------------------------------------------------
# class Manager:   # 管理员用户
#     opt_lst = ['创建课程','给学生创建账号','查看所有课程','查看所有学生','查看所有学生的选课情况','退出']
#     def __init__(self,name):
#         self.name  = name
#     def create_course(self):  # 创建课程
#         print('in Manager create_course')
#
#     def create_student(self): # 给学生创建账号
#         print('in Manager create_student')
#
#     def show_courses(self): # 查看所有课程
#         print('in Manager show_courses')
#
#     def show_students(self): # 查看所有学生
#         print('in Manager show_students')
#
#     def show_students_courses(self): # 查看所有学生的选课情况
#         print('in Manager show_students_courses')
#
#     def quit(self):
#         exit()
#
# #
#
# class Student:
#     opt_lst = ['查看所有课程', '查看已选课程', '选择课程', '退出']
#     def __init__(self,name):
#         self.name  = name
#
#     def show_courses(self):  # 查看所有课程
#         print('in Student show_courses')
#
#     def show_selected_course(self):  # 查看已选课程
#         print('in Student show_selected_course')
#
#     def choose_course(self):         # 选择课程
#         print('in Student choose_course')
#
#     def quit(self):
#         exit()
#
# # 1.输入用户名和密码
# # 2.程序判断 用户名密码 是否正确   获知身份
# # 3.如果是学生
#     # 1,2,3,4学生能做的事情
#     # 让用户选择
# # 4.如果是管理员
#     # 1,2,3,4,5,6管理员能做的事
#     # 让管理员选择
# import hashlib
# def get_md5(usr,pwd):
#     md5 = hashlib.md5(usr.encode('utf-8'))
#     md5.update(pwd.encode('utf-8'))
#     return md5.hexdigest()
#
# def login(usr,pwd):
#     with open('userinfo',encoding='utf-8') as f:
#         for line in f:
#             username,password,ident = line.strip().split('|')
#             if usr == username and get_md5(usr,pwd) == password:
#                 return {'result':True,'identify':ident,'username':usr}
#         else: return {'result':False}
#
# def auth():
#     opt_lst1 = ['登录','退出']
#     while True:
#         for index,opt in enumerate(opt_lst1,1):
#             print(index,opt)
#         num = int(input('请输入你要做的操作 :'))
#         if num == 1:
#             usr = input('username :')
#             pwd = input('password :')
#             ret = login(usr,pwd)
#             if ret['result']:
#                 print('登录成功')
#                 return ret
#             else:
#                 print('登录失败')
#         elif num == 2:
#             exit()
#
#
# ret = auth()
# print(ret)
# if ret['result']:
#     if ret['identify'] == 'Manager':
#         manager = Manager(ret['username'])
#         while True:
#             for index,opt in enumerate(Manager.opt_lst,1):
#                 print(index,opt)
#             num = int(input('请选择您要操作的序号 :'))
#             if num == 1:
#                 manager.create_course()
#             elif num == 2:
#                 manager.create_student()
#             elif num == 3:
#                 manager.show_courses()
#             elif num == 4:
#                 manager.show_students()
#             elif num == 5:
#                 manager.show_students_courses()
#             elif num == 6:
#                 manager.quit()
#     elif ret['identify'] == 'Student':
#         student = Student(ret['username'])
#         while True:
#             for index,opt in enumerate(Student.opt_lst,1):
#                 print(index,opt)
#             num = int(input('请选择您要操作的序号 :'))
#             if num == 1:
#                 student.show_courses()
#             elif num == 2:
#                 student.show_selected_course()
#             elif num == 3:
#                 student.choose_course()
#             elif num == 4:
#                 student.quit()



# 登录 一个用户在一台电脑上只能登录三次,三次之后就锁住了
# 在函数里不能用print
    # 模块 写一个函数完成一个功能

# -------------------------------------------------------------------------------------------作业：选课系统
# import os
# import hashlib
# import pickle
# class Courser:
#     def __init__(self,name,price,period,teacher):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.teacher = teacher
# class Manager():
#     opt_lst = ['创建课程','创建学生账号','查看所有课程','查看所有学生','查看所有学生的选课情况','退出程序']
#     def __init__(self,name):
#         self.name = name
#     def cjkc(self):
#         print('创建课程')
#         name = input('课程名：')
#         price = input('课程价格:')
#         period = input('学习周期：')
#         teacheer = input('授课老师：')
#         course = Courser(name,price,period,teacheer)
#         with open('course_info','ab') as f :
#            pickle.dump(course,f)
#         print('创建%s课程成功\n'%name)
#     def cjxszh(self):
#         print('创建学生账号')
#         username = input('学生用户：')
#         password = input('密码：')
#         with open('userinfo','a',encoding='utf-8') as f :
#             f.write('%s|%s|Student\n'%(username,get_md5(username,password)))
#         stu = Student(username)
#         with open('student_info','ab') as f :
#             pickle.dump(stu,f)
#         print('创建%s学生账号成功\n'%username)
#     def cksykc(self):
#         print('查看所有课程')
#         with open('course_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     course = pickle.load(f)
#                     print('%s %s,%s,%s,%s'%(count,course.name,course.price,course.period,course.teacher))
#                     count += 1
#                 except EOFError:
#                     break
#     def cksyxs(self):
#         print('查看所有学生')
#         with open('student_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     student = pickle.load(f)
#                     print('%s %s'%(count,student.name))
#                     count += 1
#                 except EOFError:
#                     break
#     def ckxsxkqk(self):
#         print('查看学生选课情况')
#         with open('student_info','rb') as f :
#             count = 1
#             while True:
#                 try:
#                     stu = pickle.load(f)
#                     for course in stu:
#                         name_lis = [course.name]
#                         print('%s %s:%s'%(count,stu.name,','.join(name_lis)))
#                         count += 1
#                 except EOFError:
#                     break
#     def quit(self):
#         print('退出程序')
#         exit()
# while True:
#     class Student():
#         opt_lst = ['查看课程','选择课程','查看所选课程','退出程序','返回']
#         def __init__(self,name):
#             self.name = name
#             self.course = []    #课程列表
#         def ckkc(self):
#             print('查看课程')
#             with open('course_info','rb') as f :
#                 count = 1
#                 while True:
#                     try:
#                         course = pickle.load(f)
#                         print('%s %s,%s,%s,%s'%(count,course.name,course.price,course.period,course.teacher))
#                         count += 1
#                     except EOFError:
#                         break
#
#         def xzkc(self):
#             print('选择课程')
#             self.ckkc()
#             num = int(input('>>>'))
#             with open('course_info','rb') as f :
#                 count = 1
#                 while True:
#                     try:
#                         obj = pickle.load(f)
#                         if num == count:
#                             self.course.append(obj)
#                             print('选择%s课程成功'%obj.name)
#                             break
#                         count += 1
#                     except EOFError:
#                         print('请输入有效序号：')
#                         break
#             with open('student_info','rb') as f1,open('student_info.bak','wb')as f2:
#                 while True:
#                     try:
#                         obj = pickle.load(f1)
#                         if obj.name == self.name:
#                             pickle.dump(self,f2)
#                         else:
#                             pickle.dump(obj,f2)
#                     except EOFError:
#                         break
#             os.remove('student_info')
#             os.rename('student_info.bak','student_info')
#
#         def cksxkc(self):
#             print('查看所选课程')
#             for index,course in enumerate(self.course,1):
#                 print('%s %s,%s,%s,%s'%(index,course.name,course.price,course.period,course.teacher))
#
#         def quit(self):
#             print('退出程序')
#             exit()
#         def fanhui(self):
#             self.cksxkc()
#
#     def get_md5(user,pwd):
#         md5 = hashlib.md5(user.encode('utf-8'))
#         md5.update(pwd.encode('utf-8'))
#         return md5.hexdigest()
#     def login(user,pwd):
#         with open('userinfo',encoding='utf-8') as f :
#             for line in f :
#                 username,password,ident = line.strip().split('|')
#                 if user ==username and password == get_md5(user,pwd):
#                     return {'jieguo':True,'shenfen':ident,'username':user}
#             else:
#                 return {'jieguo':False}
#     def auth():
#         opt_lst1 = ['登陆','退出']
#         while True:
#             for index,opt in enumerate(opt_lst1,1):
#                 print(index,opt)
#             num = int(input('请输入你要选的操作：'))
#             if num == 1:
#                 user = input('username:')
#                 pwd = input('password:')
#                 ret = login(user,pwd)
#                 if ret['jieguo']:
#                     print('登陆成功')
#                     return ret
#                 else:
#                     print('登陆失败')
#             elif num == 2:
#                 exit()
#     ret = auth()
#     print(ret)
#
#
#     if ret['jieguo']:
#         if ret['shenfen'] == 'Manager':
#             manager =Manager(ret['username'])
#             while True:
#                 for index,opt in enumerate(Manager.opt_lst,1):
#                     print(index,opt)
#                 num = int(input('请输入要选择的序号：'))
#                 if num ==1:
#                     manager.cjkc()
#                 if num ==2:
#                     manager.cjxszh()
#                 if num ==3:
#                     manager.cksykc()
#                 if num ==4:
#                     manager.cksyxs()
#                 if num ==5:
#                     manager.ckxsxkqk()
#                 if num ==6:
#                     manager.quit()
#         elif ret['shenfen'] =='Student':
#             student = Student(ret['username'])
#             while True:
#                 for index,opt in enumerate(Student.opt_lst,1):
#                     print(index,opt)
#                 num = int(input('请输入你要选择的序号：'))
#                 if num == 1:
#                     student.ckkc()
#                 if num == 2:
#                     student.xzkc()
#                 if num == 3:
#                     student.cksxkc()
#                 if num == 4:
#                     student.quit()
#                 if num == 5:
#                     student.fanhui()



#
# import datetime
# def wrapper(func):
#     def inner(count):
#         if count<3:return func(count)
#         else:return {'result':False,'msg':'用户已冻结！'}
#     return inner
#
# @wrapper
# def index_(count):
#     user = input('输入用户名')
#     pwd = input('输入密码')
#     v=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     with open('log.txt', mode='w', encoding='utf-8')as file:
#         file.write('%s %s %s'%(user,pwd,v))
#     return {'result':True,'msg':'用户已注册！'}
#
# count=0
# while True:
#     ret=index_(count)
#     print(ret['msg'])
#     if  not ret['result']:break
#     count+=1



#
# def file_read():
#     """
#     获取用户文件内的信息
#     :return: 字典，用户名：密码
#     """
#     with open('log.txt', mode='r', encoding='utf-8') as  f:
#         dic = {}
#         for i in f:
#             user, pwd, time, data = i.split()
#             dic[user] = pwd
#     return dic
#
#
# def login():
#     """
#     登录验证
#     :return:
#     """
#     con = 0  # 用来判断用户名是否是连续输错三次
#     dic = file_read()  # 获取文件中的消息
#     ua = ''  # 判断量词输入的用户名是否相同
#     while True:
#         us = input('请输入用户名 >>')
#         pw = input('请输入密码 >>')
#         if us in dic:
#             if con == 1:
#                 print('连续输错三次，账号已被冻结')
#                 continue
#             if pw == dic[us]:
#                 print('登录成功')
#                 break
#             else:
#                 print('密码输入错误，请重新输入！！！')
#                 if ua == us:
#                     con += 1
#                 else:
#                     con = 0
#                 ua = us
#         else:
#             ua = us
#             con = 0
#             print('用户不存在')
#
#
# login()  # 调用登录验证函数



# import datetime
# v = datetime.datetime.now().strftime('%Y-%m-%d %X')
# print(datetime.datetime.now().strftime('%Y-%m-%d %X'))
# with open('log.txt','w',encoding='utf-8') as f :
#     f.write(v)
#     f.close()

#
# import datetime
# def warpper(func):
#     def inner(count):
#         if count < 3:
#             return func(count)
#         else:return {'result':False,'msg':'用户已冻结'}
#     return inner
# @warpper
# def index(count):
#     user = input('>>>')
#     pwd  = int(input('>>>'))
#     v =datetime.datetime.now().strftime('%Y-%m-%d %X')
#     with open('log.txt','w',encoding='utf-8') as f:
#         f.write('%s %s %s'%(user,pwd,v))
#     return {'result':True,'msg':'用户已注册'}
# count = 0
# while True:
#     ret = index(count)
#     print(ret['msg'])
#     if not ret['result']:
#         break
# count += 1

# def func():
#     return 1
# ret = func()
# print(ret)


# import time
#
# def deco(func):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     execution_time = (end_time - start_time)*1000
#     print("time is %d ms" %execution_time)
#
# def f():
#     print("hello")
#     time.sleep(1)
#     print("world")
#
# if __name__ == '__main__':
#
#     deco(f)
#     print("f.__name__ is",f.__name__)
#     print()
#


import threading
import time

#
# def _wait():
#     time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait, daemon=False)
# t.start()
# flag b

# def _wait():
#     time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait, daemon=True)
# t.start()
# # flag b



# import threading
# loop = int(1E7)
# def _add(loop:int = 1):
#  global number
#  for _ in range(loop):
#   number += 1
# def _sub(loop:int = 1):
#  global number
#  for _ in range(loop):
#   number -= 1
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()


# import threading
# # from threading import local
# import time
#
# # obj = local()
#
# def task(i):
#     # obj.xxxxx = i
#     a = i
#     time.sleep(2)
#     # print(obj.xxxxx, i)
#     print(a,i)
# for i in range(10):  # 开启了10个线程
#     t = threading.Thread(target=task, args=(i,))
#     t.start()



import random

# for i in range(25):
#     print(random.sample(range(1,34),k=6))
#     print(random.sample(range(1,17),k=1))
# print(i)
for i in range(25):
    print(random.sample(range(1,35),k=5))
    print(random.sample(range(1,12),k=2))
print(i)






















