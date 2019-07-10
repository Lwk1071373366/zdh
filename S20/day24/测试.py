# ⼀.简答题:(36分)
# 1.列举Python2与Python3之间的区别（请写出5条）？ (4分)
#一个源码混乱一个简洁；input一个是特殊语句一个数函数；类：一个默认经典类一个默认新式类；一个默认ASCII码一个默认Unicode码；/：一个默认
#整型一个默认浮点型。
# 2.有整数3.14 如何去掉⼩数位？ 请⽤⼀⾏代码实现不能使⽤切⽚ (1分)
# print(int(3.14))
# 3.⽂件操作有哪些模式？请简述各模式的作⽤ (3分)
#r模式：读；w模式：写；r+模式：读写；w+模式：写读；a模式：追加
# 4.字符串和列表如何互相转换？ (2分)
#split和join
# 5. ... 及 pass在Python中是否是占位 ? (1分)
#  是
# 6.a=10; b=20 ⽤⼀⾏代码实现a,b数值交换： (1分)
# a = 10
# b = 20
# a,b =b,a
# print(b)  # 分别赋值
# 7.读代码写结论为什么? (2分)
# result = 1.2-1
# while True:
#     if round(result,1) == 0.2:
#         print('hi guys!')
#     else:
#         print(False)
# print(result)
# 8.递归的最⼤层数？ (1分)
# 9.读代码写结果 如下代码输出的结果是？ (2分)
# def Generator():
#     value = yield 1
#     yield value
# gen = Generator()
# print(gen.send(1))
# def Generator():
#     value = yield 1
#     yield value
# gen = Generator()
# # s=gen.__next__()
# # print(s)
#
# print(gen.send(None))
# 10.列举你了解的5个模块并简述其作⽤。 (2分)
import random  #随机数
import os #相关
import re #正则相关
import hashlib #加密
import time #时间模块
# 11.闭包函数有什么特点，应⽤场景？ (2分)
#内部可以访问外部，外部不能访问内部，安全；场景：装饰器，缓存
# 12.写出下⾯代码的输出结果，并解释为什么？ (2分)
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)    #[0,1]
# f(3,[3,2,1])  #[3,2,1,0,1,4]
# f(3)
# 13.写出下⾯代码的输出结果，并解释为什么？ (3分)
# l = [1,2,3]
# d = {"a":7,"b":8}
# def f(arg1,arg2,*args,**kwargs):
#     print(arg1,arg2,args,kwargs)
# f(1,2,3,"groovy")     # 1,2,(3,'groovy')，{}
# f(arg1=1,arg2=2,c=3,zzz="h1")  #  1,2,(),{c:3,zzz:'h1'}
# f(1,2,3,a=1,b=2,c=3)    # 1,2,(3,),{a：1，b：2，c:3}
# f(*l,**d)               #1,2,(3,),{'a':7,'b':8}
# f(1,2,*l,q="winning",**d)  # 1,2,(1,2,3),{q:'winning','a':7,'b':8}
# 14.解释⼀下什么是迭代器，你在代码中如何获得⼀个迭代器？ (2分)
#具有__iter__ __next__  ；可迭代对象执行iter方法返回的结果
# 15.迭代器如何取值？迭代器的好处？ (2分)
# 16.什么是⽣成器？你在代码中如何获得⼀个⽣成器？ (2分)
# 17.请写出下⾯代码的执⾏结果(4分)
# print([lambda: i for i in range(10)][0]())
# ⼆.简洁编程:(22分)
# 1）有列表 a = ["7net","www.7net","www.septnet","7net","www"]现需要从中将包
# 含字符7net的元素给删掉，请以最少代码量实现。 (2分)
# a = ["7net","www.7net","www.septnet","7net","www"]
# list = []
# for i in a:
#     if '7net' not in i:
#         list.append(i)
# print(list)
# 2） l = ['20','10','3','15','32']，按照数字的顺序从⼩到⼤排序，不改变原列表。
# （请⽤最简的⽅式） (2分)
# l = ['20', '10', '3', '15', '32']

# l1=[str(k)  for k in sorted([int(i) for i in l])]
# print(l1)
# 3） l = ['班级20','班级10','班级3','班级15','班级32']，按照数字的顺序从⼩到⼤排
# 序，不改变原列表。（请⽤最简的⽅式) (2分)
l = ['班级20','班级10','班级3','班级15','班级32']
for i in l:
    print(i[2:])
# 4）有⼀个列表l1 = ['alex', 'WuSir', '⽼男孩', '太⽩']⽤列表推导式将其构造成这种
# 列表['alex0', 'WuSir1', '⽼男孩2', '太⽩3'] (2分)
# l1 = ['alex', 'WuSir', '⽼男孩', '太⽩']
# print([i+str(l1.index(i)) for i in l1])
# 5）现在有两元祖(('a'),('b'))， (('c'),('d'))，请使⽤python中的匿名函数和内置函数
# ⽣成列表[{'a':'c'},{'b':'d'}] (2分)
# 6） alist = [{“a”:5,”b”:2},{“a”:2,”b”:8},{“a”:8,”b”:2}]请写出以键a的值对alist进⾏
# 排序的表达式（2分）

# 7）现有列表alist = [3,1,-4,-2],按照元素的绝对值⼤⼩进⾏排序并将得到列表的每
# 个元素求平⽅形成⼀个新的列表 (2分)
# alist = [3,1,-4,-2]
# print(list(sorted(map(lambda  x:abs(x)**2,alist))))
# 8).写函数(lambda)实现字符串翻转，如： V = ‘oldboy’ (请⽤最简的⽅式) (2分)
# print((lambda x:x[::-1])('oldboy'))
# 9).请构建⼀个⽣成器，⾥⾯的元素是1,4,9,16,25,36,49。 (3分)
# def func():
#     for i in range(1,8):
#         ret = i **2
#         yield ret
# for i in func():
#     print(i)

# 10).写⼀个⽣成器，⾥⾯的元素是20以内所有奇数的平⽅减⼀ (3分)
# 三.编程题:(42分)
# 1.写函数传⼊⼀个列表[11,22,33,44,55,[66,77,88,‘99’]] 将列表的所有的元素相加
# 得到总和495 (3分)
# 2.写函数，接收两个列表类型的参数，返回⼀个规定的字典：假设有列表
# a = ['name', 'age', 'sex']和b = ['alex', 35, 'Male']，此函数最终的返回结果为{'name': 'alex', 'age': 35, 'sex': 'Male'} (3分)
a = ['name', 'age', 'sex']
b = ['alex', 35, 'Male']
print(dict(zip(a,b)))
# 3.有字符串 “AlexLi_PageWu_BossJin” 写函数传⼊该字符串 将该字符串结果处
# 理成”AlexPageWuBossJin”(2分)
# 4.写函数，接收两个字典类型的参数，此函数完成的功能是实现两个字典的相
# 加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串
# 就拼接。⽐如：
# dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
# dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
# 如上⽰例得到结果为： dictc = {“a":1,"b":5,"c":3,"d":9,"e":7,"m":
# 9,"f":"hello","k":"world"}(4分)
# 5.写函数，完成给⼀个列表去重的功能。（不能使⽤set集合） (3分)
# 6. 将当前时间戳打印成 "2017-10-01 18:08:15" 的格式 , 将 "2017-11-18 17:43:43"
# 转换为结构化时间(2分)
# 7.⽣成器题，有空⽂件“userinfo.txt” 请往⾥填写任意内容,你往”userinfo.txt”所写⼊的内
# 容实时返回到控制台(也就是电脑的屏幕)⽤⽣成器函数实现 请列出具体代码(4
# 分)
# 8.请基于random模块 写⼀个随机⽣成6位验证码包含⼤⼩写a-z 数字0-9 例如：
# Kn7s1F 请列出具体代码(4分)
# 9.⽤内置函数过滤出单价⼤于100的股票。 (3分)
# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# 10.’asjdgf1.23sjdhf2.56ahsfgf2.34’请⽤python代码从字符串中找到所有数字并求
# 和。
# 最后计算1.23+2.56+2.34(3分)
# 11.请从⽂件中读取内容，并且⽤内置函数和匿名函数找到年纪最⼩的⼈的字典
# ⽂件中的内容如下： (5分)
# [{“name”:“yuan”,”age”:18},{“name”:“nezha”,”age”:19},{“name”:“baoyuan”,”age”:
# 17}]
# 12.请写函数，接收参数⽂件夹路径，获取这个⽂件夹中所有的⽂件(不包括⽂件
# 夹)的⼤⼩，并根据⽂件的size从⼤到⼩进⾏排序。 (6分)最终结果： [{‘file’:’file1’,’size’： 10000},{‘file’:’file2’,’size’： 9000}， …]
# 附加题（15分）
# 13.有⼀个数据结构如下所⽰，请编写⼀个函数从该结构数据中返回由指定的字
# 段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。（字典还有
# 可能有n层）
# (实现可扩展10分 实现当前功能5分)
# data:{"time":"2016-08-05T13:13:05",
# "some_id":"ID1234",
# "grp1":{ "fld1":1,
# "fld2":2},
# "xxx2":{ "fld3":0,
# “test”:{‘fld5’:0.4}},
# "fld6":11,
# "fld7":7,
# “fld46":8
# }
# fields:由"|"连接的以"fld"开头的字符串,如:fld2|fld3|fld7|fld19
# def select(data,fields):
# # TODO:implementation
# return result