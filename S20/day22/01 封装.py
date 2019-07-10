# class Goods:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# apple = Goods('苹果',50)
# print(apple.name)
# print(apple.price)


# class Goods:
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
#
# apple = Goods('苹果',50)
# print(apple.name)
# # print(apple.price)
# apple.get_price()

# class Goods:
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
# apple = Goods('苹果',50)
# print(apple.name)
# apple.get_price()
# class Goods:
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     def get_price(self):
#         print(self.__price)
# apple = Goods('苹果',60)
# print(apple.name)
# apple.get_price()

# class Goods:
#     discount = 0.8
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def pricr(self):
#         return self.__price * self.discount
#     @pricr.setter
#     def price(self,value):
#         if type(value) is int or type(value) is float:
#             self.pricr = value
# apple = Goods('苹果',40)
# banana = Goods('香蕉',65)
# print(apple.name)
# print(apple.pricr)
# Goods.discount  = 1
# print(apple.name)
# print(apple.pricr)

# class Goods:
#     discount = 0.5
#     def __init__(self,name,price):
#         self.name = name
#         self.__price = price
#     @property
#     def price(self):
#         return self.__price*self.discount
#     @price.setter
#     def price(self,value):
#         if type(value) is int or type(value) is float:
#             self.price = value
# apple = Goods('苹果',10)
# print(apple.name)
# print(apple.price)

# class Foo:
#     def __init__(self):
#         self.__func()
#     def __func(self):
#         print('in fon')
# class Son(Foo):
#     def __func(self):
#         print('in son')
# Son()

# class User:
#     def func(self):
#         self.__wahaha()
# class VipUser(User):
#     def __wahaha(self):
#         print('in vip user')
# VipUser().func()

# class Circle:
#     def __init__(self,r):
#         self.r = r
#     @property
#     def area(self):
#         return 3.14 * self.r**2
#     @property
#     def perimeter(self):
#         return 2*3.14*self.r
# c1 = Circle(5)
# # print(c1.area)
# # print(c1.perimeter)
# c1.r = 10
# print(c1.area)

# l1= [1,2,3,4,5]
# print(list(map(lambda x:x+10,l1)))
# def func(i):
#     return i*i
# print(list(map(func,l1)))
# def func(i):
#     return i*i
# print(list(map(func,l1)))