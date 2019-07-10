goods = [{"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}, ]

# for i in goods:
#      # print(i['name'], i['price'])
#     print(i,type(i))
#
#      ShopMoney = 0
#      goods = list()
#      items_dic = dict()
#      with open(ShopMenu, encoding='utf-8', mode='r') as f:
#          menu = f.readline()
#          name, price = menu.split()
#          for line in f:
#              dic = dict()
#              dic[name] = dic.get(name, line.split()[0])
#              dic[price] = dic.get(price, line.split()[1])
#              goods.append(dic)
#              items_dic[line.split()[0]] = items_dic.get(line.split()[0], line.split()[1])
#
#      ShopCar = dict.fromkeys(items_dic, 0)


# 请用户输入一个数n, 判断用户输入的数字是否是质数.
# num = int(input('>>>'))
# if num >1:
#     for i in range(2,num):
#         if num % i == 0:
#             print('不是质数')
#             break
#     else:
#         print('是质数')
# else:
#     print('不是质数')

# num=int(input('请输入一个数：'))
# if num>1:
#     for i in range(2,num):
#         if num % i == 0:
#             print('bu是质数')
#             break
#     else:
#         print('是')
# else:
#     print('不是')
#
# num=int(input('输入一个数：'))
# if num >1:
#     for i in range(2,num):
#         if num % i == 0:
#             print('不是质素')
#             break
#     else:
#         print('是')

# 有如下演员和出场费的字典,
# dic = { '周杰伦':8000,'林俊杰':5000, '太白':5, 'alex':5},
# 请删除掉出场费低于平均值的演员(5分)

dic = { '周杰伦':8000,'林俊杰':5000, '太白':5, 'alex':5}
# money=0
# l1=[]
# for i in dic.values():
#     money+=i
# mean_number=money/len(dic)
# print(mean_number)
# for k,v in dic.items():
#     if v < mean_number:
#         l1.append(k)
# for em in l1:
#     dic.pop(em)
# print(dic)
# money=0
# l1=[]
# for i in dic.values():
#     money+=i
# pjs=money/len(dic)
# for k,v in dic.items():
#     if v < pjs:
#         l1.append(k)
# for em in l1:
#     dic.pop(em)
# print(dic)
# 4、敲七游戏.从1开始数数.遇到7或者7的倍数要在桌上敲⼀下.编程来完成敲七.
# # 给出⼀个任意的数字n. 从1开始数. 数到n结束.
# # 把每个数字都放在列表中, 在数的过程中出现7或者7的倍数，
# 含有7的数（包含类似于17,27，这种数).则向列表中添加⼀个'咣(5分)
# l1=[]
# num=int(input('输入一个数：'))
# for i in range(1,num):
#     if i % 7 ==0 or '7' in str(i):
#         i='咣'
#     l1.append(i)
# print(l1)

cars = ['鲁L32444', '鲁B12333', '京B8989M', '黑C49678', '黑C46555', '沪B25041', '黑C34567']
locations = {'沪': '上海', '京': '北京', '黑': '黑龙江', '鲁': '山东', '鄂': '湖北', '湘': '湖南'}
# ret={}
# for car in cars:
#     # print(car,type(car))
#     ret[locations[car[0]]]=ret.get(locations[car[0]],0)+1
# print(ret)
ret ={}
# for i in cars:
#     ret[locations[i[0]]]=ret.get(locations[i[0]],0)+1
# print(ret)

# for i in cars:
#     if locations[i[0]] not in ret:
#         ret[locations[i[0]]]=1
#     else:
#         ret[locations[i[0]]]+=1
# print(ret)


for i in cars:
    if locations[i[0]] not in ret:
        ret[locations[i[0]]]=1
    else:
        ret[locations[i[0]]]+=1
print(ret)