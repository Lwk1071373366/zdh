# # 大作业:
# # 1)，启动程序，首页面应该显示成如下格式：
# #     欢迎来到博客园首页
# #     1:请登录
# #     2:请注册
# #     3:文章页面
# #     4:日记页面
# #     5:评论页面
# #     6:收藏页面
# #     7:退出程序
# # 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# # 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
# #         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
# #         必须要在log文件中写入日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
# #         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# # 4)，如果用户没有注册，则可以选择注册，注册成功之后，完成登录，然后进入首页选择。
# def wrapper_login(func):
#     def inner(*args,**kwargs):
#         global login_flag
#         if login_flag:
#             res = func(*args,**kwargs)
#             return res
#         else:
#             print('请先登录===>')
#             login1()
#             return func(*args,**kwargs)
#     return inner
# #装饰器wrapper_log：功能：用于在页面程序访问时，记录用户的操作信息；
# def wrapper_log(func):
#     def inner(*args,**kwargs):
#         import time
#         local_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#         with open('log','a',encoding='utf-8') as f:
#             s = '用户：%s 在%s 执行了%s函数，访问页面时，页面内容为：' \
#                 '欢迎%s用户访问%s\n'%(login_name,local_time,func.__name__,login_name,menu_list[int(choice_num)-1].split(':')[1])
#             f.write(s)
#         res = func(*args,**kwargs)
#         return res
#     return inner
# #登录功能
# def login1():
#     print('登录页面'.center(16,'※'))
#     global login_name
#     count = 0
#     while 1:
#         login_name = input('请输入用户名：').strip()
#         login_pwd = input('请输入密码：').strip()
#         with open('regist','r',encoding='utf-8') as f:
#             for line in f:
#                 name,pwd = line.strip().split('|')
#                 if login_name == name and login_pwd == pwd:
#                     global login_flag
#                     login_flag = True
#                     break
#             if login_flag:
#                 print('登录成功！')
#                 return
#             else:
#                 count += 1
#                 if count < 3:
#                     print('用户名或密码错误，请重新登录。您已错误%s次，还有%s次机会'%(count,3-count))
#                 else:
#                     quit('登录失败，退出程序')
# #注册功能
# def regist2():
#     print('注册页面'.center(16, '※'))
#     while 1:
#         regist_flag = 0
#         regist_name = input('请输入注册用户名：').strip()
#         regist_pwd = input('请输入注册密码：').strip()
#         regist_re_pwd = input('请再次输入注册密码：').strip()
#         with open('regist','r+',encoding='utf-8') as f:
#             for line in f:
#                 if regist_name == line.strip().split('|')[0]:
#                     print('用户名重复，请重新注册===>')
#                     regist_flag = 1
#                     break
#             if regist_flag == 0:
#                 if regist_pwd == regist_re_pwd:
#                     f.write('\n%s|%s'%(regist_name,regist_pwd))
#                     print('注册成功')
#                     return
#                 else:
#                     print("两次输入的密码不一致，请重新注册===>")
#
# @wrapper_login
# @wrapper_log
# def article3():
#     print('文章页面'.center(16, '※'))
#
# @wrapper_login
# @wrapper_log
# def log4():
#     print('日志页面'.center(16, '※'))
#
# @wrapper_login
# @wrapper_log
# def comment5():
#     print('评论页面'.center(16, '※'))
#
# @wrapper_login
# @wrapper_log
# def collect6():
#     print('收藏页面'.center(16, '※'))
# #注销功能
# def cancel7():
#     global login_flag
#     if login_flag:
#         login_flag = False
#         print('===》已完成用户注销')
#     else:
#         print('用户正处于注销状态')
# #退出功能
# def q8():
#     quit('退出程序！')
# #起始函数
# def start():
#     print('欢迎来到博客园首页')
#     global choice_num
#     while 1:
#         for el in menu_list:
#             print(el)
#         choice_num = input('请输入选项编号：')
#         if choice_num.isdigit():
#             if int(choice_num) <= len(menu_list):
#                 for i in menu_dic.keys():
#                     if int(choice_num) == i:
#                         menu_dic[i]()
#                         print('\n请继续进行其他的选择===》')
#             else:
#                 print('您输入的选项不存在，请重新选择===》')
#         else:
#             print('录入信息不正确，请重新选择===》')
#
# if __name__ == '__main__':
#     login_flag = False  #登录状态的标识
#     login_name = ''    #存放登录的用户名信息
#     choice_num = ''   #存放用户选择的菜单编号
#     menu_dic = {1:login1,2:regist2,3:article3,4:log4,5:comment5,6:collect6,7:cancel7,8:q8}
#     menu_list = ['1:请登录','2:请注册','3:文章页面','4:日志页面','5:评论页面','6:收藏页面','7:注销','8:退出程序']
#     start()


'''
2.写一个函数完成三次登陆功能：
a.用户的用户名密码从一个文件register中取出。
b.register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
c.完成三次验证，三次验证不成功则登录失败，登录失败返回False。
d.登陆成功返回True。
'''
#
# def login():
#     for i in range(3):
#         username,password=input('输入用户名密码：').strip().split('|')
#         with open('register','r',encoding='utf-8') as f :
#             for j in f :
#                 u,p=j.strip().split('|')
#                 if username==u and password == p :
#                     return True
#             else:
#                 print('cuowu')
#     else:
#         return False
# print(login())

'''
3.再写一个函数完成注册功能：
(1)用户输入用户名密码注册。
(2)注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
(3)注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
(4)注册成功后，返回True,否则返回False。
'''

# def regsiter():
#     while 1:
#         username,password=input('输入用户名密码|：').strip().split('|')
#         with open('register','r+',encoding='utf-8') as f :
#             for i in f :
#                 u,p=i.strip().split('|')
#                 if username==u :
#                     print('用户名存在')
#                     break
#             else:
#                 f.write(f'\n{username}|{password}')
#                 print('注册成功')
#                 return True
# regsiter()
#
# def regsiter():
#     while 1 :
#         username,password = input('输入用户名及密码|：').strip().split()
#         with open('register','r+',encoding='utf-8') as f :
#             for i in f :
#                 u,p = i.strip().split('|')
#                 if username == u :
#                     print('已存在')
#                     break
#             else:
#                 f.write(f'\n{username}|{password}')
#                 print('成功')
#                 return True
# regsiter()


# def wenjian():
#     while 1 :
#         username,password = input('输入用户名密码|：').strip().split('|')
#         with open('register','r+',encoding='utf-8') as f :
#             for i in f:
#                 u,p = i.strip().split('|')
#                 if username==u:
#                     print('存在')
#                     break
#             else:
#                 f.write(f'\n{username}|{password}')
#                 print('成功')
#                 return True
# wenjian()