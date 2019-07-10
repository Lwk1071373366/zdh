# 1.	day10作业及默写
# 1.继续整理函数相关知识点，写博客。
#
# 2.写函数，接收n个数字，求这些参数数字的和。（动态传参）
# def func(*args):
#     sum = 0
#     for n in args:
#         sum=sum+int(n)
#     return (sum)
# print(func(1,2,3,4,5,6,7,8,9))

# 3.读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#     print(a,b)
# c=test5(b,a)
# print(c)
# 4.读代码，回答：代码中,打印出来的值a,b,c分别是什么？为什么？
# a=10
# b=20
# def test5(a,b):
#   a=3
#   b=5
# print(a,b)
# c = test5(b,a)
# print(c)
# 5.传入函数中多个列表和字典,如何将每个列表的每个元素依次添加到函数的动态参数args里面？
# 如何将每个字典的所有键值对依次添加到kwargs里面？
#
# 6.下面代码成立么?如果不成立为什么报错?怎么解决?
# 6.1
# a = 2
# def wrapper():
#          print(a)
# wrapper()            #a=2
#
#     6.2
# a = 2
# def wrapper():
#
# a += 1
# print(a)
# wrapper()     #局内变量没有值
# 6.3
# def wrapper():
#      a = 1
#      def inner():
#         print(a)
#         inner()
# wrapper()      #局内变量没有值
# 6.4
# def wrapper():
#      a = 1
#      def inner():
#          a += 1
#         print(a)
#      inner()
# wrapper()           #语法错误没有global
# 7.写函数,接收两个数字参数,将较小的数字返回.
# def func(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# c=func(8,2)
# print(c)
# 8.写函数,接收一个参数(此参数类型必须是可迭代对象),将可迭代对象的每个元素以’_’相连接,形成新的字符串,并返回.
# 例如 传入的可迭代对象为[1,'老男孩','武sir']返回的结果为’1_老男孩_武sir’
# def func(list):
#     s=''
#     for i in list:
#         s=s+str(i)+'_'
#     print(s.strip('_'))
# func([1,'老男孩','武sir'])
# def func(*args):
#     for i in args:
#         print(i,end='_')
# func(*[1,'老男孩','武sir'])
# ['1','老男孩','武sir']
# s=['1','老男孩','武sir']
# print('_'.join(s))
# 9.有如下函数:
# def wrapper():
#      def inner():
#         print(666)
#      inner()
# wrapper()
# 你可以任意添加代码,执行inner函数.
# 明日默写内容:
#  1.形参的接收顺序。
#  2.什么是全局名称空间，什么是局部名称空间，什么是内置名称空间。
#  3.名称空间的加载顺序，取值顺序。
#  4.解释一下什么是global，什么是nonlocal。

