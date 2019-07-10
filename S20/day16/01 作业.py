# 1、匹配整数或者小数（包括正数和负数）
# \-(\d+\.\d+|([1-9]\d*|0))|(\d+\.\d+|([1-9]\d*|0))
# 2、匹配年月日日期 格式2018-12-6
# 2\d{3}\-[1-2][1-2]\-\d[\d]?
# 3、匹配qq号
# [1-9]\d{8}\d?\d?      [1-9]\d{4-11}
#  4、长度为8-10位的用户密码 ： 包含数字字母下划线
# \w{8,10}
# 5、匹配验证码：4位数字字母组成的
# [0-9a-zA-Z]{4}
# 6、匹配邮箱地址
# \w*@\w*\.com


# ----------------------------------------------------------------------------------
# 2.hashlib做一个密文存储密码的注册 登录程序
# import hashlib
# def md5(username,password):
#     md5 = hashlib.md5(username[::-1].encode('utf-8'))
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()
# def get_line():
#     with open('userinfo',encoding='utf-8') as f:
#         for line in f :
#             user,pwd = line.strip().split(',')
#             yield user,pwd
# def register():
#     flag = True
#     while flag:
#         username = input('user:')
#         password = input('pwd:')
#         for user,pwd in get_line():
#             if user == username:
#                 print('用户名已存在')
#                 break
#         else:
#             flag = False
#     password = md5(username,password)
#     with open('userinfo',mode='a',encoding='utf-8') as f :
#         f.write('%s,%s\n'%(username,password))
# def login():
#     username = input('user:')
#     password = input('pwd:')
#     for user,pwd in get_line():
#         if username == user and pwd == md5(username,password):
#             return  True
# ret = login()
# if ret:
#     print('登录成功')
# register()

# import hashlib
# def md5(username,password):
#     md5 = hashlib.md5(username[::-1].encode('utf-8'))
#     md5.update(password.encode('utf-8'))
#     return md5.hexdigest()
# def get_line():
#     with open('userinfo', encoding='utf-8') as f:
#         for line in f:
#             user, pwd = line.strip().split(',')
#             yield user,pwd
# def register():
#     flag = True
#     while flag:
#         username = input('user :')
#         password = input('passwd :')
#         for user,pwd in get_line():
#             if user == username:
#                 print('您输入的用户名已经存在')
#                 break
#         else:
#             flag = False
#     password = md5(username,password)
#     with open('userinfo',encoding='utf-8',mode='a') as f:
#         f.write('%s,%s\n'%(username,password))
# def login():
#     username = input('user :')
#     password = input('passwd :')
#     for user,pwd in get_line():
#         if username == user and pwd == md5(username,password):
#             return True
# ret = login()
# if ret:
#     print('登陆成功')
# register()   # 注册
# ----------------------------------------------------------------------------------------------
# 3.拼手气发红包 函数
# 怎么能第一个人和最后一个人能取到多少钱是平均概率
# import random
# def red_pac(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(money*100)
#     for i in range(len(ret)-1):
#         value = ret[i+1] - ret[i]
#         yield value/100
#
# g = red_pac(200,10)
# for i in g:
#     print(i)
# import random
# def red_pac(money,num):
#     ret = random.sample(range(1,money*100),num-1)
#     ret.sort()
#     ret.insert(0,0)
#     ret.append(money*100)
#     for i in range(len(ret)-1):
#         value = ret[i+1] - ret[i]
#         yield value/100
# g = red_pac(200,10)
# for i in g:
#     print(i)
# -----------------------------------------------------------------------------------------------
# 用hashlib 写函数 校验两个文件夹是否相同
# import os
# import hashlib
#
# def file_md5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f:
#         while filesize >= 4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
#
# def cmp_file(path1,path2):
#     return file_md5(path1) == file_md5(path2)
# path1 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\作业题讲解.mp4'
# path2 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\4.面向对象整理.mp4'
# ret = cmp_file(path1,path2)
# print(ret)

# import os
# import hashlib
# def file_md5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while filesize >= 4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def cmp_file(path1,path2):
#     return file_md5(path1) == file_md5(path2)
# path1 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\作业题讲解.mp4'
# path2 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\4.面向对象整理.mp4'
# ret = cmp_file(path1,path2)
# print(ret)
import os
import hashlib
def file_md5(path):
    filesize = os.path.getsize(path)
    md5 = hashlib.md5()
    with open(path,'rb') as f :
        while filesize >= 4096:
            content = f.read(4096)
            md5.update(content)
            filesize -= 4096
        else:
            content = f.read(filesize)
            if content:
                md5.update(content)
    return md5.hexdigest()
def cmp_file(path1,path2):
    return file_md5(path1) == file_md5(path2)
path1 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\作业题讲解.mp4'
path2 = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\4.面向对象整理.mp4'
ret = cmp_file(path1,path2)
print(ret)
# ----------------------------------------------------------------------------------------------------
# 4.os模块 计算文件夹的总大小
#     1、这个文件夹里面都是文件 D:\飞秋资料（讲师每天的视频及大纲）\day19\视频
#     2、这个文件夹里面还有文件
# import os
# def file_size(path):
#     size = 0
#     l = [path]
#     while l:
#         path = l.pop()
#         lst = os.listdir(path)
#         for name in lst:
#             son_path = os.path.join(path,name)
#             if os.path.isfile(son_path):
#                 size+= os.path.getsize(son_path)
#             else:
#                 l.append(son_path)
#     return size
# size=file_size('D:\飞秋资料（讲师每天的视频及大纲）')
# print(size)
# import os
# def file_size(path):
#     size = 0
#     l = [path]
#     while 1:
#         path = l.pop()
#         lst = os.listdir(path)
#         for name in lst:
#             son_path = os.path.join(path,name)
#             if os.path.isfile(son_path):
#                 size += os.path.getsize(son_path)
#             else:
#                 l.append(son_path)
#     return size
# size = file_size('D:\飞秋资料（讲师每天的视频及大纲）')
# print(size)
# import os
# def file_size(path):
#     size = 0
#     l = [path]
#     while l :
#         path = l.pop()
#         lst = os.listdir(path)
#         for name in lst:
#             son_path = os.path.join(path,name)
#             if os.path.isfile(son_path):
#                 size += os.path.getsize(son_path)
#             else:
#                 l.append(son_path)
#     return size
# size = file_size('D:\飞秋资料（讲师每天的视频及大纲）')
# print(size)
# # -------------------------------------------------------------------------------------------------------
# 5、计算当前月的1号的时间戳时间
# import time
# t2 = time.strftime('%Y-%m-1')
# t3 = time.strptime(t2,'%Y-%m-1')
# print(time.mktime(t3))


# import time
# from datetime import datetime , timedelta
# frist_num=datetime.now()-timedelta(20)
# print(frist_num)
# s1=time.strptime('2019-03-01 14:02:02','%Y-%m-%d %X')
# print(time.mktime(s1))

# 6、三级菜单
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
# 方法一：for循环
# for k in menu:
#     print(k)
# key1 = input('>>>')
# for k in menu[key1]:
#     print(k)
# key2 = input('>>>')
# for k in menu[key1][key2]:
#     print(k)
# key3 = input('>>>')
# for k in menu[key1][key2][key3]:
#     print(k)
# l = [menu]
# while l:
#     for k in l[-1]:
#         print(k)
#     key = input('>>>')
#     if key.upper() == 'B':
#         l.pop()
#     elif key.upper() == 'Q':
#         l.clear()
#     elif l[-1].get(key):
#         l.append(l[-1][key])
# l = [menu]
# while l:
#     for k in l[-1]:
#         key = input('>>>')
#     if key.upper() == 'B':
#         l.pop()
#     elif key.upper() =='Q':
#         l.pop()
#     elif l[-1].get(key):
#         l.append(l[-1][key])
