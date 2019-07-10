# Day14作业及默写
# 1.整理今天所学内容，整理知识点，整理博客。
#
# 2.画好流程图。
#
# 3.都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
#
# 4.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# name=[‘oldboy’,'alex','wusir']
# name=['oldboy','alex','wusir']
# def func(i):
#     return i+'_sb'
# print(list(map(func,name)))
# 5.用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
l=[{'name':'alex'},{'name':'y'}]
# for i in l:
#     print(list(map(lambda i:i['name']+'sb',l)))
# 6.用filter来处理,得到股票价格大于20的股票名字
# shares={
#     'IBM':36.6,
#     'Lenovo':23.2,
#    'oldboy':21.2,
#     'ocean':10.2,
#  }
# print(list(filter(lambda x: shares[x] > 20,shares)))
# 7.有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
# 结果：list一下[9110.0, 27161.0,......]
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# l1=[]
# for i in portfolio:
    # print(list(map(lambda x:i['shares']*i['price'],portfolio)))
#     l1.append(i['shares']*i['price'])
# print(l1)
# 8.还是上面的字典，用filter过滤出单价大于100的股票。
# for i in portfolio:
#     print(list(filter(lambda i:i['price']>100,portfolio)))
# 9.有下列三种数据类型，
l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
#  [(3, 'wusir', '****'), (4, '太白', '*******')]这样的数据。
# l3=list(zip(l1,l2,tu))
# print(l3[2:4])
# 10.有如下数据类型：
# l1 = [ {'sales_volumn': 0},
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
# print(sorted(l1,key=lambda x:x['sales_volumn']))
# 11.	求结果
# v = [lambda :x for x in range(10)]
# print(v)
# print(v[0])
# print(v[0]())

# 12.	求结果
# v = (lambda :x for x in range(10))
# print(v)
# print(v[0])
# print(v[0]())
# print(next(v))
# print(next(v)())
#
# 13.有两个字符串列表,a和b,每个字符是由逗号分隔的一些字符,(升级题)尽量做得支持扩展
a = [
'a,1',
'b,3,22',
'c,3,4',
'f,5'
]
b=[
'a,2',
'b,4',
'd,2',
'e,12'
]
data={i[0]: i for i  in a}    #首先将a这个列表转换成字典，字典的键就是元素的第一个，值就是元素
for em in b :
    if data.get(em[0]):        #判断b的每一个元素的第一个位置在不在字典中
        data[em[0]]+=[em[1:]] #通过键找到值，然后将值与b相加
    else:
        data[em[0]]=em          #键不在data这个字典中，就直接添加一个键值对
print(list(data.values()))        #将字典中的值求出

data={i[0]:i for i in a }
for en in b :
    if data.get(en[0]):
        data[en[0]]+=[en[1:]]
    else:
        data[en[0]]=en
print(list(data.values()))
# for i in l1:
#     print(i)
# for i in a :
#     l1=i.split(',')
#     print(l1)
# for j in b :
#     l2=j.split(',')
#     print(l2)
# 按每个字符串的第一个值,合并a和b到c
# c = [
# 'a,1,2',
# 'b,3,22,4',
# 'c,3,4',
# 'd,2',
# 'e,12',
# 'f,5'
# ]
#
