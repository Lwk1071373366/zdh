# def wrapper():
#     money=10
#     def inner(num):
#         nonlocal money
#         money=money+num
#         print(money)
#     return inner
# wrapper()(100)
# li=[1,1,23,4,5,6,7,7,7,7]
# em=li.__iter__()
# while 1:
#     try:
#         print(em.__next__())
#     except StopIteration:
#         break
# def func():
#     print(1)
#     func()
# func()
#1,1,2,3,5,8,13,21,34,55
# def func(n):
#          n+=1
#          print(n)
#          if n == 5:
#              return
#          func(n)
# func(2)
# count = 1
# def search():
#     # global count
#     count = 100
# search()
# print(count)
# li = [1,2,3]
# dic = {'a':'b'}
#
# def change():
#     li.append('a')
#     dic['q'] = 'g'
#     print(dic)
#     print(li)
# change()
# print(li)
# print(dic)

# def add_b():
#     b = 42
#     def do_global():
#         b = 10
#         print(b)
#         def dd_nonlocal():
#             nonlocal b
#             b = b + 20
#             print(b)
#         dd_nonlocal()
#         print(b)
#     do_global()
#     print(b)
# add_b()
# def max2(x,y):
#     m  = x if x>y else y
#     return m
# def max4(a,b,c,d):
#     res1 = max2(a,b)
#     res2 = max2(res1,c)
#     res3 = max2(res2,d)
#     return res3
# print(max4(23,-7,31,11))