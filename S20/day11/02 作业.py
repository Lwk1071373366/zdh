# day11作业及默写
# 1.
# 写函数，传入n个数，返回字典
# {‘max’:最大值,’min’:最小值}
# 例如: min_max(2, 5, 7, 8, 4)
# 返回: {‘max’:8,’min’:2}(此题用到max(), min()内置函数)
# def func(*args):
#     dic = {}
#     dic['max'] = max(args)
#     dic['min'] = min(args)
#     return dic
# ret = func(3,5,7,9)
# print(ret)
# def func(*args):
#     dic = {}
#     dic['max']=max(args)
#     dic['min']=min(args)
#     return dic
# ret=func(35,98,25,11)
# print(ret)
# def func(*args):
#     dic={}
#     dic['max']=max(args)
#     dic['min']=min(args)
#     return dic
# set=func(66,55,66,22,11)
# print(set)
# 2.
# 写函数，传入一个参数n，返回n的阶乘
# 例如: cal(7)
# 计算7 * 6 * 5 * 4 * 3 * 2 * 1
# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n-1)
# print(func(7))
# def func(n):
#     sum=1
#     for i in range(1,n+1):
#         sum=sum * i
#     print(sum)
# func(7)
# 3.
# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组
# 例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]
# def func():
#     li=['红心','草花','方片','黑桃']
#     l1=list(range(2,11))
#     l2=['J','Q','K','A']
#     l3=[]
#     for i in li:
#         for j in l1:
#             l3.append((i,j))
#         for k in l2:
#             l3.append((i,k))
#     print(l3)
# func()
# 4.
# 相关面试题（先从纸上写好答案，然后在运行）：
#
# def calc(a, b, c, d=1, e=2):
#     return (a + b) * (c - d) + e
#
#
# 请分别写出下列标号代码的输出结果，如果出错请写出Error。
# print(calc(1, 2, 3, 4, 5))
# ___2__
# print(calc(1, 2))
# ___Error_
# print(calc(e=4, c=5, a=2, b=3))
# ___24
# print(calc(1, 2, 3))
# ____8_
# print(calc(1, 2, 3, e=4))
# __10__
# print(calc(1, 2, 3, d=5, 4))
# ___Error_位置参数高于关键字参数_
#
# 下面代码打印的结果分别是_________, ________, ________.
#
#
# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
#
# print('list1=%s' % list1)
# print('list2=%s' % list2)
# print('list3=%s' % list3)

# 写代码完成99乘法表.(升级题)
# 1 * 1 = 1
# 2 * 1 = 2
# 2 * 2 = 4
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# ......
# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,j*i),end='')
    print()
# 作业写完了的同学继续完善昨天的作业。
#
# 明日默写内容:
# 1，什么是闭包。
# 2，迭代器的特性。
# 3，用while循环模拟for循环（写具体代码）。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(i,j,i*j),end='')
#     print()
