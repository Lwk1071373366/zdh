# l1=[1,2,3,4,5,6,7,8,9,0]
# l1[1:4]='abcd'
# print(l1)
# s='胡辣汤'.split('汤')
# print(s)
# a =('alex')
# print(a,type(a))
# l1=[1,2,3,4,5,6,7,8,9,0]
# len(l1)
# print(len(l1))
# l1.insert()
# tu=(1,2,3)
# list(tu)
# print(list(tu))
# list = [1,2,3,4,5]
# print(list[3:1:-1])
# l = [1,1,2,2,3,4,5,5,6,6,7,8]
# print(set(l))
# s1 = '老男孩'
# # a=s1.encode('utf-8')
# # print(a)
# b=s1.encode('gbk')
# print(b)
# s='1,2,3'
# s1=s.split(',')
# print(s1)
# s1=['1','2','3']
# s2=','.join(s1)
# print(s2)
# dic={}
# s2=dic.fromkeys('abc',666)
# print(s2)
# lis = [['哇',['how',{'good':['am',100,'99']},'太白金星'],'I']]
# lis[0][1][1]['good'][0]='AM'
# print(lis)
# lis[0][1][1]['good'][1]=lis[0][1][1]['good'][1]+9910
# print(lis)
# lis[0][1][1]['good'][1]='10010'
# print(lis)
# lis[0][1][1]['good'][2]='6666'
# print(lis)
# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}
# 1)将'k3'对应的值的最后面添加一个元素'23'。(1分)
# 2)将'k2'对应的值的第0个位置插入元素'a'。(1分)
# 3)将(1,2,3,)对应的值添加一个键值对'k4','v4'。(1分)
# dic = {'k1':'v1','k2':['alex','sb'],(1,2,3,):{'k3':['2',100,'wer']}}
# dic[(1,2,3)]['k3'].append('23')
# print(dic)
# dic['k2'].insert(0,'a')
# print(dic)
# dic[(1,2,3)]['k4']='v4'
# print(dic)
# 使用range打印100,99,98，....1,0
# for i in range(100,-1,-1):
#     print(i)
# 1、请用户输入一个数n, 判断用户输入的数字是否是质数.	（5分）
# 质数解释：质数又称素数。一个大于1的自然数，除了1和它自身外，不能整除其他自然数的数叫做质数；否则称为合数。
# n=input('请输入一个数:').strip()
# for i in range(2,n):
#     i=i.isdigit()
#     if i % 1 ==0 and i % i == 0:
#         print('是质数')
#     else:
#         print('是合数')
#答案：
# num=int(input('请输入一个数字：'))
# for i in range(1,num):
#     if num % i ==0:
#         print('不是质数')
#     else:
#         print(' 是质数')
# # 2、有如下演员和出场费的字典, dic = { '周杰伦':8000,'林俊杰':5000, '太白':5, 'alex':5}, 请删除掉出场费低于平均值的演员(5分)
# dic = { '周杰伦':8000,'林俊杰':5000, '太白':5, 'alex':5}
# # sum=0
# # s=dic.values()
# # # print(s)
# # for i in s:
# #     print(i,type(i))
# dic.pop('太白')
# dic.pop('alex')
# print(dic)

# 5、有如下值li= [11,22,33,44,55,77,88,99,90]，将所有大于 66 的值保
# 存至字典的第一个key中，将小于 66 的值保存至第二个key的值中(在原	有代码基础上补充,不得改变原有代码)。(6分)
#
# li = [11,22,33,44,55,77,88,99,90]
# dic={}
# l1=[]
# l2=[]
# for i in li :
#     if i > 66:
#         l1.append(i)
#     if i < 66:
#         l2.append(i)
# dic['k1']=l1
# dic['k2']=l2
# print(dic)
# 4、敲七游戏.从1开始数数.遇到7或者7的倍数要在桌上敲⼀下.编程来完成敲七.
# 给出⼀个任意的数字n. 从1开始数. 数到n结束.
# 把每个数字都放在列表中, 在数的过程中出现7或者7的倍数，含有7的数（包含类似于17,27，这种数).则向列表中添加⼀个'咣(5分)
# l1=[]
# n=input('请输入数字：').strip()
# for i in range(1,int(n)):
#     if i % 7 == 0:
#         i='咣'
#     l1.append(i)
# print(l1)
# 3、有文件t1.txt里面的内容为：（5分）
#     id,name,age,phone,job
#   1,alex,22,13651054608,IT
# 	2,wusir,23,13304320533,Tearcher
# 	3,taibai,18,1333235322,IT
#
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},......]
# l1=[]
# dic={}
# with open('t1.txt',encoding='utf-8',mode='r') as f:
#     for i in f :
#         print(i)
#         id,name,age,phone,job=i.split()
#         dic= {'id':int(id),'name':name,'age':int(age),'phone':int(phone),'job':job}
#         l1.append(dic)
# print(l1)
#
# 6、车牌区域划分，给出一下车牌和地点信息对照，请根据车牌信息，分析出各省的车牌持有数量。
# 	cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
# 	locations = {'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}(6分)
# 	最终形成这样的数据：{'山东': 2, '黑龙江': 3, '北京': 1, '上海':
cars = ['鲁A32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
locations = {'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}

result = {}
for car in cars:
    print(car)
    result[locations[car[0]]] = result.get(locations[car[0]], 0) + 1
print(result)

