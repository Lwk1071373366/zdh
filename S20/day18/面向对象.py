# class Dog:
#     def __init__(self,name,hp,ad,sex):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.sex = sex
#     def yao(self,Person):
#         Person.hp-=self.ad
#         print('%s咬了%s，%s掉了%s血'% (self.name,taibai.name,taibai.name,self.ad))
# class Person:
#     def __init__(self,name,hp,ad,sex):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.sex = sex
#     def gongji(self,Dog):
#         Dog.hp-=self.ad
#         print('%s打了%s，%s掉了%s血'% (self.name,Dog.name,Dog.name,self.ad))
# hei=Dog('小黑',50,10,'男')
# taibai=Person('太白',100,20,'男')
# taibai.gongji(hei)
# print(hei.hp)
# hei.yao(taibai)
# print(taibai.hp)


# alex=Dog('alex',20,10,'不详')
# print(alex.name)
# print(alex.sex)
# taibai=Dog('太白',30,20,'不详')
# print(taibai.name)

'''
圆形类
属性：半径
方法：计算周长和面积
'''
from math import pi
# class Circle:
#     def __init__(self,r):
#         self.r = r
#     def area(self):
#         return pi * self.r**2
#     def perimeter(self):
#         return 2*pi*self.r
# c1 = Circle(5)
# c2 = Circle(10)
# print(c1.area())
# print(c2.area())

# 计算长方形、正方形、圆形、平行四边形、三角形面积
# class chang:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
# c1 = chang(5,6)
# print(c1.area())
# c2 = chang(7,8)
# print(c2.area())

# class zheng:
#     def __init__(self,length):
#         self.length = length
#     def area(self):
#         return self.length**2
# c1 = zheng(6)
# print(c1.area())

# class ping:
#     def __init__(self,bottom,high):
#         self.bottom = bottom
#         self.high = high
#     def area(self):
#         return self.bottom * self.high
# c1 = ping(8,9)
# print(c1.area())
#
#
# class  triangle :
#     def __init__(self,length,high):
#         self.length = length
#         self.high = high
#     def area(self):
#         return self.length*self.high/2
# c1 = triangle(6,6,)
# print(c1.area())