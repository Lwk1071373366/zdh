# day15作业
# 1.
# 整理今天内容
# 2.
# 现有列表alist = [3, 1, -4, 2, -6]
# 按照元素的绝对值大小进行排序
# alist = [3, 1, -4, 2, -6]
# alist.sort(key=abs)
# print(alist)
# print(sorted(alist,key=abs))
# 3.已知ip = '192.168.156.254'
# 提取各部分并写入列表中
# ip = '192.168.156.254'
# print(ip.split('.'))
# 4.
# 在以上题基础上实现写一个函数, 完成功能, 然后将列表返回
# def func(ip):
#     list=ip.split('.')
#     return list
# ret=func('192.168.156.254')
# print(ret)
# 5.
# 输入某年某月某日, 判断是这一年中的第几天?(用内置模块实现)
# '2019年3月20日'
# import time
# t=input('>>>>')
# t1=time.strptime(t,'%Y-%m-%d')
# print(t1.tm_yday)
import random
# 一行代码实现[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# l1=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print(list(filter(lambda x:x*x,l1)))
# 7.
# 从0 - 99
# 这个100个数中随机取出10个不重复的数
# l1=[]
# for i in range(100):
#     l1.append(i)
# print(random.sample(l1,k=10))
# 8.
# 一行代码, 通过filter和lambda函数输出以下列表索引为基数对应的元素
# lis = [12, 13, 14, 151, 5, 16, 17, 117, 133, 144, 177]
# def func(num):
#     ind=lis.index(num)
#     if ind%2==1:
#         return True
# ret=filter(func,lis)
# print(list(ret))
#
# def func(num):
#     ind=lis.index(num)
#     if ind % 2==1:
#         return True
# ret=filter(func,lis)
# print(list(ret))
#
#
# ret=filter(lambda num:lis.index(num) % 2==1,lis)
# print(list(ret))
# 9.
# 将下列数据转成想要的结果, 尽量用简洁的方式实现:
# 原数据lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 转换后
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l1=[]
# for i in lst:
#     # l1=lst[0]+lst[1]+lst[2]
#     for j in i :
#         l1.append(j)
# print(l1)
# 10.
# 实现一个装饰器, 通过调用一次装饰器使被装饰的函数调用5次
# def wrapper(func):
#     def inner(*args,**kwargs):
#         for i in range(5):
#             ret=func(*args,**kwargs)
#         return ret
#     return inner
# @wrapper
# def func():
#     print('12356')
# func()
# 11.
# 将列表内的元素, 根据位数被合并成字典(升级题)
# lst = [1, 2, 3, 4, 12, 13, 14, 123, 124, 125, 1234, 1235, 1236, 1237, 12345, 12346, 12347]
# 变成
# {
#     1: [1, 2, 3, 4],
#     2: [12, 13, 14],
#     3: [123, 124, 125],
#     4: [1234, 1235, 1236, 1237],
#     5: [12345, 12346, 12347]
# }
# lst = [1, 2, 3, 4, 12, 13, 14, 123, 124, 125, 1234, 1235, 1236, 1237, 12345, 12346, 12347]
# from collections import defaultdict
# d=defaultdict(list)
# for i in lst:
#     d[len(str(i))].append(i)
# print(dict(d))
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
#     length=len(s)
#     for i in range(1,length//2+1):
#         num=length//i
#         if s[:i]*num==s:
#             return True
#     else:
#         return False
# while True:
#     s=input('>>>')
#     ret=func(s)
#     print(ret)

# def func(s):
#     length=len(s)
#     for i in range(1,length//2+1):
#         num=length//i
#         if s [:i]*num==s:
#             return True
#     else:
#         return False
# while True:
#     s=input('>>>')
#     ret=func(s)
#     print(ret)
