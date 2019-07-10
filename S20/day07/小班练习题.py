# 1.
# Python中str, list, tuple, dict列举5个常用的方法
#字符串拼接 ，列表的增删改查 ，元祖查询，字典的增删改查
# 2.
# 按升序合并如下两个list, 并去除重复的元素:
# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
# # list1.sort()
# # print(list1)
# # list2.sort()
# # print(list2)
# for i in list1:
#     list2.append(i)
# # print(list2)
# list2.sort()
# print(list2)
# s1=set(list2)
# print(s1)
# 3.
# 将以下内容进行反转
# L =‘hello
# world’
# 执行效果：L =‘dlrow
# olleh’
# l='hello world'
# l2=[]
# # l1=l.split(' ')
# # print(l1)
# for i in l:
#     # print(i)
#     l2.append(i)
# # print(l2)
# l2.reverse()
# # print(l2)
# l3=','.join(l2)
# print(l3,type(l3))
# l3.split('')
# print(l3)
# l='hello world'
# l1=l.split(' ')
# # print(l1)
# l1.reverse()
# print(l1)
# 读以下代码写出执行结果:
# a = 10
# b = 20
# c = b
# b = 25
# print(a)
# print(b)
# print(c)
#
# 5.
# 读以下代码写出执行效果：
#
# dic = {'k': 'v', '1': 5}
# dic['k'] = []
# dic['k'].append(567)
# print(dic)
#
# 6．有这样一段代码：
# a = 10
# b = 20
# c = [a]
# a = 15
# print(c)
# 会输出什么，为什么会输出这样的结果
#
# 7.
# 读以下代码写出执行效果：
# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
# a.append(5)
# a[4].append('c')
#
# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)
# 输出结果：
#
#
#
# 8.
# Python中的数据类型共有那些？那些是可变的？那些是不可变的？那些是有序的？那些是无序的？
#
#
#
#
# 9.
# 有如下列表：
# LIS = [‘1’，{‘k1’:’v1’, ’k2’:[33, 22, 44]}，1，[’alex’, ’egon’]，{(13, 14, 15): {‘key’:’value’}}]
# （8）
# a．    查找alex并修改成全部大写，
# b．    将33更改成字符串类型
# c．    将key对应的值用‘ * ’代替，长度由key对应的值决定
# d．    在[’alex’, ’egon’]列表元素之间添加‘ritian’
#
#
#
# 10.
# Python中，中文输出问题怎么解决，2
# 和3有什么区别？
#
#
#
#
# 11.
# Python中pass语句的用法是什么?
#
#
#
#
# 12.
# Python中，格式化输出有哪几种方式？都是什么？怎么运用？
#
#
#
#
#



# s='a' + 'b' + 1
# print(s)
# print(range(3))
# s = 'abcd'.replace('cb', 'dd')
# print(s)
# s='{0}|{2}|{1}'.format('a','b','c')
# print(s)
#
# l1 = [1,2,3]
# l2 = l1
# l1.append(666)
# print(l2)
# l1 = [22,33,44]
# l2 = l1[:]
# print(l2)
# print(l1 is l2)
#
# for i in range(5):
#     # pass
#     print(i)
# i=1
# j=1
# for i  in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}\t'.format(j,i,i*j),end='')
#     print()

# li = [1,2,3,4,5]
# def func(x,y):
#     return x*10 + y
# print(reduce(func,li))