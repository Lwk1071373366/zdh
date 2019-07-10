# from collections import defaultdict
# dic = defaultdict(int)
# flag = True
# while flag:
#     username = input('user :')
#     password = input('pwd :')
#     f = open('locked')
#     for line in f:
#         if username == line.strip():
#             print('%s账号已经被锁定' % username)
#             f.close()
#             flag = False
#             break
#     else:
#         f.close()
#         if dic[username]  < 2:
#             with open('userinfo',encoding='utf-8') as f:
#                 for line in f:
#                     user,pwd = line.strip().split(',')
#                     if user == username and pwd==password:
#                         print('登录成功')
#                         break
#                 else:
#                     print('登录失败')
#                     dic[username] += 1
#         else:
#             print('%s账号已经被锁定'%username)
#             with open('locked',mode='a',encoding='utf-8') as f:
#                 f.write(username+'\n')
#             break
# a = 0.01
# count = 0
# while a <= 8848:
#     count +=1
#     a = a *2
#     print(a,count)
# print(count)
# for x in range(5):
#     pass
# print(x)
# def f():
#     x = 0
#     for i in range(5):
#         x += i
#     print(x)
# f()
import random
#点sample :
# l1=[1,2,3,4,5,6]
# print(random.sample(l1,k=2))
#点random 默认0-1之间的随机小数
# print(random.random())

#点randint  （起始位，终止位）随机一位整数
# print(random.randint(1,110))

#点randrange  （起始位，终止位，可以加步长）
# print(random.randrange(1,10,3))

#点choice  从有序的数据结构中，随机产生一位整数
# l1=[1,2,3,4,5,6]
# l2=(1,2,3,4,5,6)
# print(random.choice(l2))

#点choices  从有序的数据结构中，随机产生k=n位整数,有重复
# l1=[1,2,3,4,5,6]
# l2=(1,2,3,4,5,6)
# print(random.choices(l2,k=2))

#点shuffle 打乱对象顺序   打印源数据
# l1=[1,2,3,4,5,6]
# random.shuffle(l1)
# print(l1)


