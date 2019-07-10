'''
1.列举Python2与Python3之间的区别（5条）？(4分)
'''
# python2中:
# 1.默认编码:ASCll
# 2.range返回的是列表,xrange返回的是可迭代对象
# 3.整数分为:int和lang
# 4.代码重复
# 5.语言不统一
# 6.不支持中文
# python3中:
# 1默认编码:Unicode
# 2.返回的是可迭代对象
# 3.整数统一是:int
# 4.代码重复
# 5.语言统一
# 6.支持中文
#更多python2和Python3的区别 see also:
# https://wiki.python.org/moin/Python2orPython3
# https://www.cnblogs.com/Neeo/p/8033520.html
'''
2.有整数3.14 如何去掉小数位？ 请一行代码实现不能使⽤切⽚ (1分)
'''
print(round(3.14))

print(int(3.14))

print('%.0f'%3.14)
'''
3.文件件操作有哪些模式？请简述各模式的作用 (3分)
'''
#Character Meaning
# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
#  'x' open for exclusive creation, failing if the file already exists
# 'a' open for writing, appending t
#'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)
# 'U' universal newlines mode (deprecated)
# see also: https://docs.python.org/3/library/functions.html#open
# 'r' 打开文件，以读的方式，默认的方式
# 'w' 打开文件，写入文件，如果原文件存在则会被覆盖，如果没有此文件就会创建，前提是
#该模式下必须保证文件目录的存在
# 'x' 创建一个新文件并打开以写入，如果文件已存在则抛出FileExistsError错误
# 'a' 以追加的方式打开文件，如果文件存在则从原文件的末尾写入，否则会创建文件
# 'b' 二进制模式，可以搭配其他的模式使用，如'rb',
#  't' 文本模式，默认
#  '+' 读/写模式，用于更新
# 'U' 通用的换行模式，现已弃用
# 'rt' 文本读模式，默认模式
# 'wt' 以文本写模式打开，打开前原文件会被清空
# 'rb' 打开文件，以二进制的形式读文件
# 'ab' 以二进制追加模式打开文件
# 'wb' 以二进制写模式打开，打开前原文件会被清空
#'r+' 以文本读写模式打开文件，可以控制写入到文件任何位置，默认写的指针开始指在文件
#开头，所以会复写文件
# 'w+' 以文本读写模式打开文件
# 'a+' 以文本读写模式打开文件，如果写那么指针将从文件末尾开始
# 'rb+' 以二进制读写模式打开文件
# 'wb+' 以二进制读写模式打开文件，原文件会被清空
#  'ab+' 以二进制读写模式打开文件

'''
4.字符串和列表如何互相转换？(2分)
'''
a='aaaa'
print(list(a))
l=['a','b']
s=''.join(l)
print(s)

'''
5. ... 及 pass在Python中是否是占位 ? (1分)
'''
# 表示为了程序的完成性，而又不能立即实现其功能或者不需要实
# 现其功能，故采用pass或者...语句
'''
6.a=10; b=20 用一行代码实现a,b数值交换：(1分)
'''
a=10
b=20
# def func(a,b):
#     print(a,b)    ##函数方法
# func(b,a)

a,b=b,a           #简单方法
print(a,b)

'''
7.读代码写结论为什么? (2分)
result = 1.2-1
while True:
if round(result,1) == 0.2:
print('hi guys!')
else:
print(False)

'''
# 结论是result的结果是0.19999999999999996，round保留一位小数四舍五入后是0.2，符
# 合while循环中的if条件，打印结果是死循环hi guys！
# result = 1.2-1
# print(result, round(result, 1)) # 0.19999999999999996 0.2
# while True:
# if round(result,1) == 0.2:
# print('hi guys!')
# else:
# print(False)
'''
8.递归的最大层数？(1分)
'''
# 网络上的递归最大层数:1000
# 自己测得:998
import sys
print(sys.getrecursionlimit())
'''
9.读代码写结果 如下代码输出的结果是？(2分)
def Generator():
value = yield 1
yield value
gen = Generator()
print(gen.send(1))
'''
#报错
#修改:
def Generator():
    value = yield 1
    yield value
gen = Generator()
# s=gen.__next__()
# print(s)

print(gen.send(None))
'''
10.列举你了解的5个模块并简述其作⽤。(2分)
'''
# import  time        时间模块
# import  random      数字模块
# import  sys          python解释器相关
# import  os            系统相关
# import   pickle       序列化相关
# import  json          序列化相关
# import   re           正则相关
#import  logging         日志
#import  hashlib         加密

'''
11.闭包函数有什么特点，应用场景？(2分)
'''
# 保证了数据的安全,只能内部访问外部,外部不能访问内部
#应用场景:
# 装饰器
# 缓存
'''
12.写出下⾯代码的输出结果，并解释为什么？(2分)
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)
'''
# 答案:[0,1]
# [3,2,1,0,1,4]
# [0,1,0,1,4]
'''
13.写出下⾯代码的输出结果，并解释为什么？(3分)
l = [1,2,3]
d = {"a":7,"b":8}
def f(arg1,arg2,*args,**kwargs):
print(arg1,arg2,args,kwargs)
f(1,2,3,"groovy")
f(arg1=1,arg2=2,c=3,zzz="h1"
f(1,2,3,a=1,b=2,c=3)
f(*l,**d)
f(1,2,*l,q="winning",**d)
'''
# 1 2 (3,'groovy') {}
# 1 2 () {'c':3,'zzz':'h1'}
# 1 2 (3,) {'a': 1, 'b': 2, 'c': 3}
# 1 2 (3,) {'a': 7, 'b': 8}
# 18 1 2 (1, 2, 3) {'q': 'winning', 'a': 7, 'b': 8}
'''
14.解释⼀下什么是迭代器，你在代码中如何获得⼀个迭代器？(2分)
'''
# 可迭代对象执行__iter__方法返回的结果称为迭代器
# 迭代器中必须包含:__iter__和__next__
'''
15.迭代器如何取值？迭代器的好处？(2分)
'''
# 迭代器的特点:
# 重复    下一次的重复是基于上一次结果
# 使用迭代器的优点:
# 1.提供一种不依赖索引的取值方式.迭代器通过__next__方法取值
# 2.惰性运算
# 缺点:
# 1.取值不如索引方便
# 2.迭代过程不可逆
'''
16.什么是⽣成器？你在代码中如何获得⼀个⽣成器？(2分)
'''
# 函数体内包含有yield关键字,该函数执行的结果(返回值generator_obj)为生成器,而该函数称为生成器函数
#  yield的功能：
# 1. yield与return一样可以终止函数执行、可以返回值(不指定返回值默认返回None)，
# 但不同之处yield可以在函数内多次使用，而return只能返回一次。
#  2. 为函数封装好了__iter__和__next__方法，把函数得执行结果转换为迭代器，也就是
# 说yield自动实现了迭代协议并遵循迭代器协议。
#  3. 触发函数的执行、暂停、再继续，包括状态都由yield保存。
#  4. 生成器本质就是迭代器。
#  5. 延迟计算，当你需要的时候，yield返回一次，不需要，就保留信息，等待下一次调
# 用。
#  生成器函数和普通的函数最大的不同之处在于，生成器每当yield一次，在返回值的时候，将
# 函数挂起，保存相关信息，在下一次函数执行的时候，从当前挂起的位置继续执行。

'''
17.请写出下⾯代码的执⾏结果(4分)
print([lambda: i for i in range(10)][0]())
'''
print([lambda: i for i in range(10)][0]())
# 结果:9
'''
二.简洁编程
'''
'''
1）有列表 a = ["7net ","www.7net ","www.septnet ","7net ","www"]现需要从中将包含字符
7net的元素给删掉，请以最少代码量实现。(2分
'''
a = ["7net ","www.7net ","www.septnet ","7net ","www"]
print([i for i in a  if '7net'not in i ])
'''
2）l = ['20','10','3','15','32']，按照数字的顺序从小到大排序，不改变原列表。（请⽤最简的
⽅式）(1分)
'''
l = ['20','10','3','15','32']
l1=[str(k)  for k in sorted([int(i) for i in l])]
print(l1)
'''
3）l = ['班级20','班级10','班级3','班级15','班级32']，按照数字的顺序从小到大排序，不改变
原列表。（请⽤最简的⽅式) (2分)
'''
l = ['班级20','班级10','班级3','班级15','班级32']
def bar(y):
    return '班级'+str(y)
def foo(n):
    return  int(n[2:])
l2=sorted(list(map(foo,l)))
print(l2)
print(list(map(bar,l2)))
'''
4）有⼀个列表l1 = ['alex', 'WuSir', '⽼男孩', '太⽩']⽤列表推导式将其构造成这种列表
['alex0', 'WuSir1', '⽼男孩2', '太⽩3'] (2分)
'''
l1 = ['alex', 'WuSir', '老男孩', '太白']
print([i+str(l1.index(i)) for i in l1])
'''
5）现在有两元祖(('a'),('b'))，(('c'),('d'))，请使⽤python中的匿名函数和内置函数⽣成列表
[{'a':'c'},{'b':'d'}] (2分)
'''
t1=(('a'),('b'))
t2=(('c'),('d'))
print([{k:v} for k,v in zip(t1,t2)])
#第二种,用lambda
ret=lambda t1,t2:[{k:v} for k,v in zip(t1,t2)]
print(ret(t1,t2))
'''
6）alist = [{“a”:5,”b”:2},{“a”:2,”b”:8},{“a”:8,”b”:2}]请写出以键a的值对alist进⾏排序的表达
式（3分）
'''
alist = [{'a':5,'b':2},{'a':2,'b':8},{'a':8,'b':2}]
ret=sorted([i['a'] for i in alist])
print([i for k in ret for i in alist if i['a']==k])
'''
7）现有列表alist = [3,1,-4,-2],按照元素的绝对值⼤⼩进⾏排序并将得到列表的每个元素求
平⽅形成⼀个新的列表 (2分
'''
alist = [3,1,-4,-2]
print(list(sorted(map(lambda  x:abs(x)**2,alist))))
'''
8).写函数(lambda)实现字符串翻转，如：V = ‘oldboy’ (请⽤最简的⽅式) (2分)
'''
print((lambda x:x[::-1])('oldboy'))
##第二种
ret =  ''.join(reversed('oldboy'))
print(ret)
'''
9)请构建⼀个⽣成器，⾥⾯的元素是1,4,9,16,25,36,49
'''
def func():
    for i in range(1,8):
        ret=i**2
        yield  ret
for i  in func():
    print(i)
'''
10).写个⽣成器，⾥⾯的元素是20以内所有奇数的平⽅减⼀
'''
print(list(i*i-1 for i in range(20) if i %2==1))
'''
1.写函数传入一个列表[11,22,33,44,55,[66,77,88,‘99’]] 将列表的所有的元素相加
得到总和495 (3分
'''
list=[11,22,33,44,55,[66,77,88,'99']]
def func(list):
    sum=0
    sum1=0
    for i in list[0:5]:
        sum+=i
    for k in list[-1]:
        sum1+=int(k)
    print(sum+sum1)
func(list)

#第二种
def func(l):
    num=0
    for i in l:
        if isinstance(i ,list):  #判断是否是列表类型
            for k in i:
                num+=int(k)
        else:
            num+=int(i)
    return num
print(func([11,22,33,44,55,[66,77,88,'99']]))
'''
2.写函数，接收两个列表类型的参数，返回⼀个规定的字典：假设有列表
a = ['name', 'age', 'sex']和b = ['alex', 35, 'Male']，
此函数最终的返回结果为{'name': 'alex', 'age': 35, 'sex': 'Male'} (3分)
'''
a = ['name', 'age', 'sex']
b = ['alex', 35, 'Male']
ret=zip(a,b)
print(dict(ret))

print(dict(zip(a,b)))    #一条代码输出

def func(a,b):
    dict={}                       ##函数输出
    for i in zip(a,b):
        dict[i[0]]=i[1]
    print(dict)
func(a,b)

'''
3.有字符串 “AlexLi_PageWu_BossJin” 写函数传⼊该字符串 将该字符串结果处
理成”AlexPageWuBossJin”(2分)
'''
a='AlexLi_PageWu_BossJin'
s=a.replace('_','')
print(s)

print(a.replace("_",""))

'''
4.写函数，接收两个字典类型的参数，此函数完成的功能是实现两个字典的相
加，不同的key对应的值保留，相同的key对应的值相加后保留，如果是字符串
就拼接。⽐如：
dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
如上⽰例得到结果为： dictc = {“a":1,"b":5,"c":3,"d":9,"e":7,"m":
9,"f":"hello","k":"world"}(4分)
'''
dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}
def func(a,b):
    dictc={}
    for i in a:
        if i in b:
            dictc[i]=b[i]+a[i]
        else:
            dictc[i]=a[i]
    for k in b:
        if k not in dictc:
            dictc[k]=b[k]
    print(dictc)
func(dicta,dictb)
'''
5.写函数，完成给下个列表去重的功能。（不能使⽤set集合）(3分)
'''
a=[1,2,3,5,2,4,1]
b=[1,5,6]
def func():
    for i in a:
        if i in b:
            b.remove(i)
    print(a+b)
func()

#第二种
def func(args):
    list=[]
    for i  in args:
        if i not in list:
          list.append(i)
        else:
            continue
    print(list)
func(a)

'''
6. 将当前时间戳打印成 "2017-10-01 18:08:15" 的格式 , 将 "2017-11-18 17:43:43"
转换为结构化时间(2分)
'''
import  time
s=time.strptime("2017-10-01 18:08:15","%Y-%m-%d %H:%M:%S")
print(s)
s1=time.mktime(s)
print(s1)


ret=time.strptime('2017-11-18 17:43:43','%Y-%m-%d %H:%M:%S' )
print(ret)

import time
s=time.gmtime(time.time())
s1=time.mktime(s)
print(time.strftime('%Y-%m-%d %H:%M:%S',s))

'''
7.生成器题，有空⽂件“userinfo.txt” 请往⾥填写任意内容,你往”userinfo.txt”所写⼊的内
容实时返回到控制台(也就是电脑的屏幕)⽤⽣成器函数实现 请列出具体代码(4
分)
'''
# with open ('userinfo.tst',mode='w',encoding='utf-8')as f:
#     f.write('kaowanle')
# def tail(filename):
#     f=open(filename,mode='r',encoding='utf-8')
#     f.seek(0,2)
#     while True:
#         line =f.read()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield  line
# tail_g=tail('userinfo.txt')

# for line in tail_g:
#     print(line)
'''
8.请基于random模块 写⼀个随机生成6位验证码包含大小写a-z 数字0-9 例如：
Kn7s1F 请列出具体代码(4分)
'''
#纯数字的
import random
def func(n=6):
    s=''
    for i in range(n):
        num=random.randint(0,9)
        s+=str(num)
    return s
print(func())
#数字和字母的
import  random
def func():
    s=''
    for i in range(6):
        num =random.randint(0,9)
        alf_big=chr(random.randint(65,90))
        alf_small=chr(random.randint(97,123))
        add=random.choice([num,alf_big,alf_small])
        s = ''.join([s,str(add)])
    print(s)
func()

'''
9.⽤内置函数过滤出单价大于100的股票。(3分)
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
'''
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
ret=filter(lambda dic:dic['price']>100,portfolio)
print(list(ret))

#一条代码
print(list(filter(lambda x:x['price']>100,portfolio)))

'''
10.’asjdgf1.23sjdhf2.56ahsfgf2.34’请⽤python代码从字符串中找到所有数字并求
和。
最后计算1.23+2.56+2.34(3分)
'''
s='asjdgf1.23sjdhf2.56ahsfgf2.34'
import  re
print(sum([float(i) for i  in re.findall('\d+\.\d+',s)]))  #取用这个方法

'''
11.请从⽂件中读取内容，并且⽤内置函数和匿名函数找到年纪最⼩的⼈的字典
⽂件中的内容如下：(5分)
[{“name”:“yuan”,”age”:18},{“name”:“nezha”,”age”:19},{“name”:“baoyuan”,”age”:
17}]
 '''

with open('userinfo',encoding='utf-8')as  f:
    l1=[]
    title=f.readline().strip().split(',')
    for i in f:
        name,age=i.strip().split(',')
        l1.append({title[0]:name,title[1]:age})
        print([i for i in l1 if str(min(list(map(lambda d:int(d['age']),l1))))==i['age']])

'''
12.请写函数，接收参数⽂件夹路径，获取这个⽂件夹中所有的⽂件(不包括⽂件
夹)的⼤⼩，并根据⽂件的size从⼤到⼩进⾏排序。(6分)
最终结果：[{‘file’:’file1’,’size’：10000},{‘file’:’file2’,’size’：9000}，…]

'''
import os
def sort_file(path):
    l=[]
    name_lst=os.listdir(path)
    for name in name_lst:
        w = os.path.join(path,name)
        w1=os.path.getsize(w)
        l.append({'file':name,'size':w1})
    l.sort(key=lambda dic: dic['size'],reverse=True)
    return l
ret=sort_file('/Users/jingliyang/PycharmProjects/MyFlask')
print(ret)
'''
13.有一个数据结构如下所示，请编写一个函数从该结构数据中返回由指定的字段和对应的值
组成的字典。如果指定字段不存在，则跳过该字段。（字典还有可能有n层）
(实现可扩展10分 实现当前功能5分)
data:{"time":"2016-08-05T13:13:05",
"some_id":"ID1234",
"grp1":{ "fld1":1,
"fld2":2},
"xxx2":{ "fld3":0,
“test”:{‘fld5’:0.4}},
"fld6":11,
"fld7":7,
“fld46":8
}
fields:由"|"连接的以"fld"开头的字符串,如:fld2|fld3|fld7|fld19
def select(data,fields):
# TODO:implementation
return resul
'''
data = {'time': '2016-08-05T13:13:05', 'some_id': 'ID1234', 'grp1':
{'fld1': 1, 'fld2': 2},
'xxx2': {'fld3': 0, 'test': {'fld5': 0.4}}, 'fld6': 11, 'fld7': 7,
'fld46': 8}
def foo(data,fields):
    d=[]
    for k,v in data.items():
        if isinstance(v,dict):
            d+=foo(v,fields)
        elif k in fields:
            d.append({k:v})
    return d
def core():
    while True:
        fields=input('输入你的field:').strip().split('|')
        if fields[0].upper()=='Q':
            break
        print(foo(data,fields))
core()