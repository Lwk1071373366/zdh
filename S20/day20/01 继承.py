# class Dog:
#     def __init__(self,name,kind):
#         self.name = name
#         self.kind = kind
#     def chi(self):
#         pass
# class Cat:
#     def __init__(self,name,kind):
#         self.name = name
#         self.kind = kind
# -----------------------------------------------------------------------人狗大战
# class Role(object):
#     def __init__(self,name,hp,ad):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
# class Dog(Role):
#     def __init__(self,name,hp,ad,kind):
#         super().__init__(name,hp,ad)
#         self.kind = kind
#
#     def bite(self,person):
#         person.hp -= self.ad
#         print('%s攻击了%s，%s掉了%s点血' % (self.name, person.name, person.name, self.ad))
# class Person(Role):
#     def __init__(self,name,hp,ad,sex):
#         super().__init__(name,hp,ad)
#         self.sex = sex
#     def fight(self,dog):
#         dog.hp -= self.ad
#         print('%s攻击了%s，%s掉了%s点血'%(self.name,dog.name,dog.name,self.ad))
# hei = Dog('小黑',300,20,'哈士奇')
# alex = Person('alex',20,1,'不详')
# alex.fight(hei)
# print(hei.hp)
# hei.bite(alex)
# print(alex.hp)
# -------------------------------------------------------------------------------
#     def __init__(self,name,blood,ad,kind):
#         self.name = name  # 向对象的内存空间中添加属性
#         self.hp = blood   # 可以通过self在类的内部完成
#         self.ad = ad
#         self.kind = kind
#
#     def bite(self,person):
#         person.hp -= self.ad
#         print('%s攻击了%s，%s掉了%s点血' % (self.name, person.name, person.name, self.ad))
#
# class Person:
#     def __init__(self,name,hp,ad,sex):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.sex = sex
#
#     def fight(self,dog):
#         dog.hp -= self.ad
#         print('%s攻击了%s，%s掉了%s点血'%(self.name,dog.name,dog.name,self.ad))
#
# hei = Dog('小黑',300,20,'哈士奇')
# alex = Person('alex',20,1,'不详')
# alex.fight(hei)
# print(hei.hp)
# hei.bite(alex)
# print(alex.hp)

# class O(object):
# #     pass
# #     def func(self):
# #         print('o')
# # class D(O):
# #     pass
# #     def func(self):
# #         print('d')
# # class E(O):
# #     pass
# #     def func(self):
# #         print('e')
# # class B(D, E):
# #     pass
# #     def func(self):
# #         print('b')
# # class F(O):
# #     pass
# #     def func(self):
# #         print('f')
# # class C(E,F):
# #     pass
# #     def func(self):
# #         print('c')
# # class A(B,C):
# #     pass
# #     def func(self):
# #         print('a')
# # g=A.mro()
# # print(g)


# -------------------------------------------------------作业
# 1.请使用C3算法计算出链接图中的继承顺序
# https://www.processon.com/view/link/5bf6690be4b08c22eea64888
# 2.请自己找一张类的继承图，按照C3算法说出它的继承顺序
# 3.运行代码，请说出结果，并说出为什么结果是这样？
# class Foo:
#       def __init__(self):
#              self.func()
#       def func(self):
#              print(‘in foo’)
# class Son(Foo):
#       def func(self):
#              print(‘in son’)
# 4.继续完成计算器作业
# 5.默写 使用继承完成的人狗大战程序
# class Foo:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print('in foo')
#
# class Son(Foo):
#     def func(self):
#         print('in son')
# Son()
# Foo()

# class G(object):
#     def func(self):
#         print('g')
# class F(object):
#     def func(self):
#         print('f')
# class D(object):
#     def func(self):
#         print('d')
# class E(G):
#     def func(self):
#         print('e')
# class C(D,F):
#     def func(self):
#         print('c')
# class B(D,E):
#     def func(self):
#         print('b')
# class A(B,C):
#     def func(self):
#         print('a')
# h = A.mro()
# print(h)
# ----------------------------------------------------------爬虫
from urllib.request import urlopen
# import re
# def urls(url):
#     str_path = urlopen(url).read().decode('utf-8')
#     return str_path
# def file_write(file):
#     with open('三寸人间.txt', 'a', encoding='utf-8') as f:
#         f.write(file + '\n')
# def comp(path):
#     com = re.compile(
#         '<h1>(?P<title>.*?)</h1>.*?<div id="content">(?P<cont>.*?)<br /><br /><p><a href="http://koubei.baidu.com/s/xbiquge.la"',
#         re.S)
#     str_con = com.findall(path)
#     for i in str_con:
#         str_con = i[1].replace('&nbsp;', '')
#         str_con = str_con.replace('\r<br />\r<br />', '\n')
#         return str_con
# url = 'http://www.xbiquge.la/10/10489/'
# str_path = urls(url)
# str_cont = re.findall("<dd><a href='(?P<url>.*?)' >(?P<title>.*?)</a></dd>", str_path)
# for i in str_cont:
#     path = 'http://www.xbiquge.la'+i[0]
#     path = urls(path)
#     file_con = comp(path)
#     file_write(file_con)
# print('下载完成')
