# 正则表达式练习
# 1、匹配一篇英文文章的标题 类似 The Voice Of China
# 2、匹配一个网址
    # 类似 https://www.baidu.com http://www.cnblogs.com
# 3、匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# 4、匹配15位或者18位身份证号

# 5、从lianjia.html中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]


# 6、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式


# 7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法

# 8、完成三级菜单

# 9、大作业：计算器

#10、继续完成day16的五个功能题
# ------------------------------------------------------------------------------------------------
# day15作业
#
# 1.
# 整理今天内容
#
# 2.
# 现有列表alist = [3, 1, -4, 2, -6]
# 按照元素的绝对值大小进行排序
#
# 3.
# 已知ip = '192.168.156.254'
# 提取各部分并写入列表中
#
# 4.
# 在以上题基础上实现写一个函数, 完成功能, 然后将列表返回
#
# 5.
# 输入某年某月某日, 判断是这一年中的第几天?(用内置模块实现)
#
# 6.
# 一行代码实现[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# 7.
# 从0 - 99
# 这个100个数中随机取出10个不重复的数
#
# 8.
# 一行代码, 通过filter和lambda函数输出以下列表索引为基数对应的元素
#
# lis = [12, 13, 14, 151, 5, 16, 17, 117, 133, 144, 177]
#
# 9.
# 将下列数据转成想要的结果, 尽量用简洁的方式实现:
#
# 原数据lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# 转换后
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 10.
# 实现一个装饰器, 通过调用一次装饰器使被装饰的函数调用5次
# def warpper(func):
#     def inner(*args,**kwargs):
#         for i in range(5):
#             ret=func(*args,**kwargs)
#         return ret
#     return inner()
# @warpper
# def func():
#     print('123')
# 11.
# 将列表内的元素, 根据位数被合并成字典(升级题)
#
# lst = [1, 2, 3, 4, 12, 13, 14, 123, 124, 125, 1234, 1235, 1236, 1237, 12345, 12346, 12347]
#
# 变成
#
# {
#
#     1: [1, 2, 3, 4],
#
#     2: [12, 13, 14],
#
#     3: [123, 124, 125],
#
#     4: [1234, 1235, 1236, 1237],
#
#     5: [12345, 12346, 12347]
#
# }
lst = [1, 2, 3, 4, 12, 13, 14, 123, 124, 125, 1234, 1235, 1236, 1237, 12345, 12346, 12347]
from collections import defaultdict
d = defaultdict(list)
for i in lst:
    d[len(str(i))].append(i)
print(dict(d))
# 12.
# 输入一个不是空的字符串, 判断这个字符串是不是由一个子字符重复多次组成, 字符只包含小写字母, 且长度不超过1000
# (升级题)
# 示例一:
# 输入: "abab"
# 这种就输出True, 因为输入的是ab重复组成的字符串
# 示例二:
# 输入: "abcabcabc"
# 这种就输出True, 因为输入的是abc重复组成的字符串
# 示例三:
# 输入: "abcdabcd"
# 这种就输出True, 因为输入的是abcd重复组成的字符串
# 示例四:
# 输入: 'abc"
# 这种就输出False, 因为输入的没有重复组成字符串
# def func(s):
#     length =len(s)
#     for i in range(1,length//2+1):
#         num = length//i
#         if s[:i] * num == s:
#             return True
#     else:
#         return False
# while True:
#     s = input('>>>')
#     ret = func(s)
#     print(ret)
# def func(s):
#     length = len(s)
#     for i in range(1,length//2+1):
#         num = length//i
#         if s[:i]*num == s :
#             return True
#     else:
#         return False
# while True:
#     s = input('>>')
#     ret = func(s)
#     print(ret)

# def func(lst):
#     lst.append(888)
#     return lst
# lst = [1,2,3]
# lst =func(lst)
# print(lst)
# def f(lst):
#     lst.append(888)
#
# lst = [1,2,3]
# f(lst)
# print(lst)
# def new_str(name):
#     return '---{}---'.format(name)
#
# s = 'andy'
# ss = new_str(s)
# print(ss)

#------------------------------------------------------------------------------------------
# Day14作业及默写
# 1.整理今天所学内容，整理知识点，整理博客。
#
# 2.画好流程图。
#
# 3.都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
#
# 4.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=['oldboy','alex','wusir']
# print(list(map(lambda i :i+'_sb',name)))
# 5.用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
# l=[{'name':'alex'},{'name':'y'}]
# print(list(map(lambda i : i['name']+'sb',l)))
# 6.用filter来处理,得到股票价格大于20的股票名字
# shares={
#     'IBM':36.6,
#     'Lenovo':23.2,
#    'oldboy':21.2,
#     'ocean':10.2,
#  }
# print(list(filter(lambda i :shares[i]>20,shares)))
# 7.有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
# 结果：list一下[9110.0, 27161.0,......]
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# l1 = []
# for i in portfolio:
#     s1=i['shares']*i['price']
#     l1.append(s1)
# print(l1)
# 8.还是上面的字典，用filter过滤出单价大于100的股票。
# print(list(filter(lambda i:i['price']>100,portfolio)))
# 9.有下列三种数据类型，
# l1 = [1,2,3,4,5,6]
# l2 = ['oldboy','alex','wusir','太白','日天']
# tu = ('**','***','****','*******')
# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
#  [(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。
# print(list(zip(l1,l2,tu)))
# print(list(filter(lambda i :i[0]>2,list(zip(l1,l2,tu)))))    #filter 和zip的混用
#
# 10.有如下数据类型：
# l1 = [{'sales_volumn': 0},
#        {'sales_volumn': 108},
#        {'sales_volumn': 337},
#        {'sales_volumn': 475},
#        {'sales_volumn': 396},
#        {'sales_volumn': 172},
#        {'sales_volumn': 9},
#        {'sales_volumn': 58},
#        {'sales_volumn': 272},
#        {'sales_volumn': 456},
#        {'sales_volumn': 440},
#        {'sales_volumn': 239}]
# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。

# print(sorted(l1,key=lambda i:i['sales_volumn'],reverse=True))  #（先是可迭代对象，key=指定规则--函数）

# 11.	求结果
# v = [lambda :x for x in range(10)]
# print(v)
# print(v[0])
# print(v[0]())
#
# 12.	求结果
# v = (lambda :x for x in range(10))
# print(v)
# print(v[0])
# print(v[0]())
# print(next(v))
# print(next(v)())
#
# 13.有两个字符串列表,a和b,每个字符是由逗号分隔的一些字符,(升级题)尽量做得支持扩展
# a = [
# 'a,1',
# 'b,3,22',
# 'c,3,4'
# 'f,5'
# ]
# b=[
# 'a,2',
# 'b,4',
# 'd,2',
# 'e,12'
# ]
#
# 按每个字符串的第一个值,合并a和b到c
# c = [
# 'a,1,2',
# 'b,3,22,4',
# 'c,3,4',
# 'd,2',
# 'e,12',
# 'f,5'
# ]
# data = {i[0]:i for i in a}
# # print(data)
# # 首先将a这个列表转换字典,字典的键就是元素中的第一个,值就是元素
# for em in b:
#     if data.get(em[0]):
#         # 判断b的每一个元素的第一个位置在不在字典中
#         data[em[0]] += em[1:]
#         # 通过键找到值 然后将值和b相加(自己理解)
#     else:
#         data[em[0]] = em
#         # 键不在data这个字典中,就直接添加一个键值对
# print(list(data.values()))
# 将字典中的值求出
# data = {i[0]:i for i in a }
# for em in b:
#     if data.get(em[0]):
#         data[em[0]] +=em[1:]
#     else:
#         data[em[0]] = em
# print(list(data.values()))
# data = {i[0]:i for i in a }
# for em in b :
    # print(em[0])
    # if data.get(em[0]):
    #     data[em[0]] += em[1:]
#     else:
#         data[em[0]] = em
# print(list(data.values()))
# data = {i[0]:i for i in a}
# for em in b :
#     if data.get(em[0]):
#         data[em[0]]+=em[1:]
#     else:
#         data[em[0]] = em
# print(list(data.values()))
#---------------------------------------------------------------------------------------------
# 2.写一个函数完成三次登陆功能：
# a.	用户的用户名密码从一个文件register中取出。
# b.	register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# c.	完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# d.	登陆成功返回True。
# def login():
#     for em in range(3):
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         with open('register',encoding='utf-8') as f :
#             for line in f :
#                 i,j = line.strip().split('|')
#                 if i == username and j ==password:
#                     return  True
#             else:
#                 print('用户名或密码错误')
#
#     else:
#         return False
# print(login())

# def login():
#     for em in range(3):
#         my_user,my_pwd = input('user|pwd:').strip().split('|')
#         with open('register','r',encoding='utf-8')as f:
#             for i in f:
#                 user,pwd = i.strip().split('|')
#                 if my_user == user and my_pwd == pwd:
#                     return True
#             else:
#                 print('用户名或密码错误!')
#     else:
#         return False
# print(login())
#
# 3.再写一个函数完成注册功能：
# (1)用户输入用户名密码注册。
# (2)注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# (3)注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# (4)注册成功后，返回True,否则返回False。
# def register():
#     while True:
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         with open('register','r+',encoding='utf-8',) as f :  #  注意r+的使用 先读后写 换a+就不好使
#             for em in f :
#                 i,j = em.strip().split('|')
#                 if i == username:
#                     # return False
#                     print('用户名已存在')
#                     break
#             else:
#                 f.write('%s,%s\n'%(username,password))
#                 print('注册成功')
#                 return True
#     else:
#         return False
# print(register())
# def register():
#     while True:
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         with open('register','r+',encoding='utf-8') as f:
#             for em in f :
#                 i,j = em.strip().split('|')
#                 if i == username:
#                     print('用户名已存在')
#                     break
#             else:
#                 f.write('%s|%s\n'%(username,password))
#                 print('注册成功')
#                 return True
#     else:
#         return False
# print(register())
# def register():
#     while 1:
#         my_user,my_pwd = input('user|pwd:').strip().split('|')
#         with open('register','r+',encoding='utf-8')as f:
#             for i in f:
#                 user,pwd = i.strip().split('|')
#                 if my_user == user:
#                     print('用户名已存在,请重新输入用户名')
#                     break
#             else:
#                 f.write(f'{my_user}|{my_pwd}\n')
#                 print('注册成功!')
#                 return True
# register()
# k = 3
# def func():
#     global k
#     k =k + 1
#     return k
# ret = func()
# print(ret)