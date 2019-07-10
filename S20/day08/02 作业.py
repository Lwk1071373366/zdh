# Day09作业及默写
# 1.整理函数相关知识点,写博客。
#
# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(a):
#     list=[]
#     for i in range(len(a)):
#         if i % 2 ==1:
#             list.append(a[i])
#     print(list)
# func([1,2,3])
# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func(a):
#     for i in range(len(a)):
#         if len(a)>5:
#             print('大了')
#         else:
#             print('正好')
#         return
# func('a,j')

# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(a):
#     list=[]
#     for i in range(len(a)):
#         if len(a) > 2 :
#             list.append(a[0:2])
#         return list
# f=func([1,2,3,4,5])
# print(f)
# 5.写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返回结果。
# def func(a):
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for i in a:
#         if i.isdigit():
#             shuzi+=1
#         elif i.isalpha():
#             zimu+=1
#         elif i.isspace():
#             kongge+=1
#         else:
#             qita+=1
#             return (shuzi,zimu,kongge,qita)
# f=func('22ll !')
# print(f)


# 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# f=func(5,2)
# print(f)

# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
#  PS:字典中的value只能是字符串或列表
# def func(a):
#     for k,v in dic.items():
#         if len(v) > 2:
#           a[k]=v[0:2]
#     return a
# f=func(dic)
# print(f)
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def func(a):
#     dic={}
#     for i in range(len(a)):
#         dic[i]=a[i]
#     print(dic)
# func([11,22,33])

# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
# 然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def func(name,sex,age,education):
#     with open('student_msg',encoding='utf-8',mode='a') as f1:
#         f1.write('\t{}|{}|{}|{}'.format(name,sex,age,education))
# name,sex,age,education=input('依次输入，以逗号隔开').replace('，',',').split(',')
# func(name,sex,age,education)
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
#
# 11.	写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（升级题）。
#
# 明日默写内容。
# ①return的作用。

# ②传参的几种方法，每个都简单写一个代码。
# 如，实参，按位置传参。
# def func(x,y):
# pass
# func(‘a’,’b’)
# ---------------------------------------------------------------以下答案
# day09作业及默写
# 1 # 1.整理函数相关知识点,写博客。
# 2 #
# # 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返
# 回给调用者。
# 3
# def func(argv):
#     l1 = []
#     for i in range(len(argv)):
#         if i % 2 == 1:
#             l1.append(argv[i])
#         return l1
# print(func(['a','b','c','d']))

# def func(a):
#     l2=[]
#     for i in range(len(a)):
#         if i % 2 == 1:
#             l2.append(a[i])
#     return l2
# print(func(['a','b','c','d']))

# 11
# 12 # 方法二
# 13 # def func(argv):
# 14 # return argv[1::2]
# 15 # func([11,2,23,3,5,4])
# 16
# 17 # 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# 18 # def func2(argv):
# 19 # if len(argv) > 5:
# 20 # return '大于5'
# 21 # else:return '不大于5'
# 22 # print(func2('dfdsafdsafa'))
# 23
# 24 # 方法二：
# 25 # def func2(argv):
# 26 # return '大于5' if len(argv) > 5 else '不大于5'
# 27
# # 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返
# 回给调用者。
# 28
# 29 # def func3(argv):
# 30 # if len(argv) > 2:
# 31 # new_list = argv[:2]
# 32 # return new_list
# 33 # print(func3([1,2,3,4]))
# 34
# 35 # 方法二
# 36 def func(li):
# 37 return li[:2] if len(li) > 2 else None
# 38 print(func([1,2]))
# 39# 5.写函数，计算传入函数的字符串中,[数字]、[字母]、[空格] 以及 [其他]的个数，并返
# 回结果。
# 40
# 41 def func4(str):
# dic =
# {'num_of_digit':0,'num_of_char':0,'num_of_space':0,'num_of_other':0,}
# 42
# 43 for i in str:
# 44 if i.isdigit():
# 45 dic['num_of_digit'] += 1
# 46 elif i.isalpha():
# 47 if 66 < ord(i) < 123:
# 48 dic['num_of_other'] +=1
# 49 else:
# 50 dic['num_of_char'] += 1
# 51 elif i.isspace():
# 52 dic['num_of_space'] += 1
# 53 else:
# 54 dic['num_of_other'] += 1
# 55 return '数字个数为%s,字母个数为%s,空格个数为%s,其他个数为%s,'\
# %
# (dic['num_of_digit'],dic['num_of_char'],dic['num_of_space'],dic['num_of_ot
# her'])
# 56
# 57
# 58 input_str = input('请输入任意字符串:')
# 59 print(func4(input_str))
# 6.写函数，接收两个数字参数，返回比较大的那个数字。
# 方法一：
# def max_num(argv1,argv2):
# if argv1 > argv2:
# return argv1
# else:
# return argv2
# 方法二
# def max_num(argv1,argv2):
# return argv1 if argv1 > argv2 else argv2
# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表
# def func6(argv):
# for key in argv:
# if len(argv[key]) > 2:
# argv[key] = argv[key][0:2]
# return argv
# print(func6({"k1": "v1v1", "k2": [11,22,33,44]}))
# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给
# 调用者一个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：
# [11,22,33] 返回的字典为 {0:11,1:22,2:33}。
# def func(argv):
# dic = {}
# for i in range(len(argv)):
# dic[i] = argv[i]
# return dic
# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
# 然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容追加到一个student_msg文件中。
# def func(name,sex,age,xueli):
#     with open('student_msg','a',encoding='utf-8') as f:
#         f.write('\t{},{},{},{}'.format(name,sex,age,xueli))
# name,sex,age,xueli=input('请依次输入姓名，性别，年龄，学历').replace('，',',').split(',')
# func(name,sex,age,xueli)
# 10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把
# 性别输入女。
# def register1(name,age,education,sex='男'):
#     sex = '男' if sex == '' else sex
#     with open('register2','a+' ,encoding='utf-8') as f1:
#         f1.write('{},{},{},{}\n'.format(name,age,sex,education))
# while 1:
#     name = input('请输入名字(q或者Q退出):').strip()
#     if name.upper() == 'Q': break
#     age = input('请输入年龄:').strip()
#     sex = input('请输入性别(性别为男则直接回车):').strip()
#     education = input('请输入学历:').strip()
#     register1(name,age,education,sex)
# def xinxi(name,age,xueli,sex='男'):
#         sex='男' if sex=='' else sex
#         with open('xinxibiao2','a+',encoding='utf-8') as f2:
#             f2.write('{},{},{},{}\n'.format(name,age,xueli,sex))
# while 1:
#     name=input('请输入姓名（按q或者Q退出）：').strip()
#     if name.upper()=='Q': break
#     age=input('请输入年龄：').strip()
#     xueli =input('请输入学历：').strip()
#     sex = input('请输入性别：为男直接回车').strip()
#     xinxi(name,age,xueli,sex)
# 11.写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改
# 操作（升级题）。
# import os
# def func(file_name,old,new):
#     with open(file_name,'r',encoding='utf-8')as f,\
#         open(f'new_{file_name}','w',encoding='utf-8')as f1:
#         for line in f:
#             line = line.replace(old,new)
#             f1.write(line)
#     os.remove(file_name)
#     os.rename(f'new_{file_name}',file_name,)
# func('student_msg','sb','alex')

import os
# def func(file_name,old,new):
#     with open(file_name,'r',encoding='utf-8') as f,\
#         open(f'new_{file_name}','w',encoding='utf-8') as f1:
#         for line in f:
#             line=line.replace(old,new)
#             f1.write(line)
#     os.remove(file_name)
#     os.rename(f'new_{file_name}',file_name)
# func('student_msg','sb','taibai')

import os
def func(file_name,old,new):
    with open(file_name,'r',encoding='utf-8') as f ,\
        open(f'new_{file_name}','w',encoding='utf-8') as f2:
        for line in f:
            line=line.replace(old,new)
            f2.write(line)
    os.remove(file_name)
    os.rename(f'new_{file_name}',file_name)
func('student_msg','taibai','nbnb')