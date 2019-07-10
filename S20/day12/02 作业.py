# Day12作业及默写
# 1.	整理今天的博客，写课上代码，整理流程图。
# 2.	用列表推导式做下列小题
# li=['alex','wusir','abds','meet','ab']
# a.	过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
# l1=[]
# for i in li:
#     # print(i,type(i))
#     if len(i) < 3:
#         l1.append(i.upper())
#         print(l1)

# b.	求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表#
# for i in range(6):
#     if i % 2 == 0:
#         x=i
#         for j in range(6):
#             if j % 2 == 1:
#                 y=j
#                 print([(x,y)])
# c.	M = [[1,2,3],[4,5,6],[7,8,9]] 求M中3,6,9组成的列表
# m = [[1,2,3],[4,5,6],[7,8,9]]
# l1=[]
# for i in m:
#     for j in i:
#         if j % 3 ==0:
#             l1.append(j)
# print(l1)
# print([j for i in m for j in i if j % 3 ==0])
# d.	求出50以内能被3整除的数的平方，并放入到一个列表中。
# l1=[]
# for i in range(50):
#     if i % 3 ==0:
#         l1.append(i*i)
# print(l1)
# print([i*i for i in range(50) if i % 3 ==0])
# e.	构建一个列表：['python1期', 'python2期', 'python3期', 'python4期',
#        'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
# l1=[]
# for i in range(1,11):
#     if i !=5:
#         l1.append('python{}期'.format(i))
# print(l1)
# print(['python{}期'.format(i) for i in range(1,11)  if i !=5 ])
# f.	构建一个列表：[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# g.	构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# l1=[]
# for i in range(20):
#     if i % 2 ==0:
#         l1.append(i)
# print(l1)
# lst=[i for i in range(20) if i % 2 ==0]
# print(lst)
# print([i for i in range(20) if i % 2 ==0])
# h.	有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']
# 将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
# l1 = ['alex', 'WuSir', '老男孩', '太白']
# l2=[]
# for i in range(len(l1)):
#     l2.append(l1[i]+str(i))
# print(l2)
# print([l1[i]+str(i) for i in range(len(l1))])
# (9)有以下数据类型：
# x = {'name':'alex',
#     'Values':[{'timestamp':1517991992.94,
#          'values':100,},
#         {'timestamp': 1517992000.94,
#         'values': 200,},
#         {'timestamp': 1517992014.94,
#          'values': 300,},
#         {'timestamp': 1517992744.94,
#          'values': 350},
#         {'timestamp': 1517992800.94,
#          'values': 280}],}
# 将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100],
# [1517992000.94, 200],
#  [1517992014.94, 300],
# [1517992744.94, 350],
# [1517992800.94, 280]]
# l1=[]
# ret=x['Values']
# for i in ret:
#     j=list(i.values())
#     l1.append(j)
# print(l1)
# print([l1.append(j) j=list(i.values()) for i in ret ])
# 3.求结果：
# v = [i % 2 for i in range(10)]
# print(v)
#
#
# 4.求结果:
# v = (i % 2 for i in range(10))
# print(v)
#
# 5.求结果：
#
# for i in range(5):
#     print(i)
# print(i)
#
#
# 大作业:
# 1)，启动程序，首页面应该显示成如下格式：
#     欢迎来到博客园首页
#     1:请登录
#     2:请注册
#     3:文章页面
#     4:日记页面
#     5:评论页面
#     6:收藏页面
#     7:退出程序
# 2)，用户输入选项，3~6选项必须在用户登录成功之后，才能访问成功。
# 3)，用户选择登录，用户名密码从register文件中读取验证，三次机会，
#         没成功则结束整个程序运行，成功之后，可以选择访问3~6项，访问页面之前，
#         必须要在log文件中写入日志，日志格式为-->用户:xx 在xx年xx月xx日 执行了 %s函数，
#         访问页面时，页面内容为：欢迎xx用户访问评论（文章，日记，收藏）页面
# 4)，如果用户没有注册，则可以选择注册，注册成功之后，完成登录，然后进入首页选择。
# username='aaa'
# password=666
# while 1:
#     print('欢迎来到博客园首页\n1:请登录\n2:请注册\n3:文章页面\n4:日记页面\n5:评论页面\n6:收藏页面\n7:退出程序')
#     option=input('请输入序号：（1-7）').strip().isdigit()
#     if 0 < option < 8:
#         if option == 1:
#             print('请登录')
#     with open('register','r',encoding='utf-8') as f:
#         if