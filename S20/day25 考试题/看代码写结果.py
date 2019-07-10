# a = 1
# def func(a):
#     a=2
#     print(a)
# func(3)
# print(a)

# v = [lambda :x for x  in range(10)]
# print(v)           #[<function <listcomp>.<lambda> at 0x00000000027DCC80>, <function <listcomp>.<lambda> at 0x00000000027DCD90>, <function <listcomp>.<lambda> at 0x00000000027DCE18>,
                    #  <function <listcomp>.<lambda> at 0x00000000027DCEA0>, <function <listcomp>.<lambda> at 0x00000000027DCF28>, <function <listcomp>.<lambda> at 0x00000000027E2048>, <function <listcomp>.<lambda> at 0x00000000027E20D0>, <function <listcomp>.<lambda> at 0x00000000027E2158>, <function <listcomp>.<lambda> at 0x00000000027E21E0>, <function <listcomp>.<lambda> at 0x00000000027E2268>]

# print(v[0])   #<function <listcomp>.<lambda> at 0x00000000027BCC80>
# print(v[0]())   #9
# v = (lambda :x for x in range(10))
# print(v)         #[<function <listcomp>.<lambda> at 0x000000000216CC80>, <function <listcomp>.<lambda> at 0x000000000216CD90>, <function <listcomp>.<lambda> at 0x000000000216CE18>, <function <listcomp>.<lambda> at 0x000000000216CEA0>, <function <listcomp>.<lambda> at 0x000000000216CF28>, <function <listcomp>.<lambda> at 0x0000000002172048>, <function <listcomp>.<lambda> at 0x00000000021720D0>,
                # <function <listcomp>.<lambda> at 0x0000000002172158>, <function <listcomp>.<lambda> at 0x00000000021721E0>, <function <listcomp>.<lambda> at 0x0000000002172268>]
# print(v[0])      #<function <listcomp>.<lambda> at 0x00000000025FCC80>

# def func(a,b,c,*args,d=1,**kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
#     print(kwargs)
# func(1,2,3,4,5,6,7,key = 'value',name = 'alex')

# def func(a = 1,b = 2, l = []):
#     l.append(a+b)
#     print(l)
# func(1,2)    [3]
# func(3,4,[]) [7]
# func(5,6)    [3,11]

# class A:
#     Country = 'English'
#     def __init__(self):
#         self.Country = 'China'
#
#     print(Country)           #English

# class A:
#     def __init__(self):
#         self.Country = 'China'
#     def show_country(self):
#         return self.Country
#
#     Country = 'English'
# print(A.Country)           #English
# print(A().Country)          #china
# print(A().show_country())   #china

# flag = True
#
# def wrapper(func):
#     def inner(*args,**kwargs):
#         if flag:
#             ret = func(*args,**kwargs)
#             return ret
#
#     return inner
# @wrapper
# def wahaha():
#     print('wahaha')
#     return True
# flag = False
# ret = wahaha()
# print(ret)         #None?

# lst = filter(lambda n :n % 3 ==1,range(10))
# print(len(list(lst)))  #3
# print(len(list(lst)))  #0

# class B(object):
#     def func(self):
#         print('in B')
# class A(B):pass
# A().func()    in B

# class B(object):
#     def func(self):
#         print('in B')
# class A(B):
#     def func(self):
#         print('in A')
# A().func()

# class B(object):
#     def __init__(self):
#         self.func()
#     def func(self):
#         print('in B')
# class A(B):
#     def func(self):
#         print('in A')
# A()                    # in A

# class B(object):
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print('in B')
# class A(B):
#     def __func(self):
#         print('in A')
# A()                       # in B

# class A(object):
#     def func(self):
#         print('in A')
# class B(A):
#     def func(self):
#         print('in B')
# class C(A):
#     def func(self):
#         super().func()
#         print('in C')
# class D(A):
#     def func(self):
#         super().func()
#         print('in D')
# class E(B,C,D):
#     def func(self):
#         super().func()
#         print('in E')
# E().func()                  # in B  in E