# # 练习：写一个类，能自动统计这个类有多少个对象！
# class A:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         A.count += 1
# c1 = A('taibai')
# c2 = A('taihei')
# print(A.count)
# class B:
#     count = 0
#     def __init__(self,name):
#         self.name = name
#         B.count +=1
# c1 =B('tt')
# c2 =B('TT')
# print(B.count)
# class Student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     a = 1
#     b = 2
#     def func(self):
#         pass
# yang = Student('杨',20,'男')
# class Student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
# liu = Student('liu',20,'nan')
# class Syudent:
#     country = 'China'
#     def __init__(self,name,country):
#         self.name = name
#         self.country = country
#
# zhang = Syudent('zhang','riben')
# # zhang = Syudent('zhang')
# print(zhang.country)
# print(Syudent.country)
# class Student:
#     country = 'china'
#     def __init__(self,name):
#         self.name = name
# zou = Student('zou')
# print(zou.country)
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def date(self):
#         return '%s-%s-%s'%(self.year,self.month,self.day)
# class Student:
#     def __init__(self,name,num,birth,in_shcool,start_day):
#         self.name = name
#         self.num = num
#         self.birth = birth
#         self.in_school = in_shcool
#         self.start_day = start_day
# d1 = Date(2000,1,1)
# d2 = Date(2010,1,1)
# d3 = Date(2010,9,1)
# li = Student('李',1,d1,d2,d3)
# print(li.birth.year)
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def date(self):
        return '%s-%s-%s' % (self.year,self.month,self.day)
class Student:
    def __init__(self,name,num,birth,in_shcool,start_day):
        self.name = name
        self.num = num
        self.birth = birth
        self.in_shcool = in_shcool
        self.strat_day = start_day
d1 = Date(2000,1,1)
d2 = Date(2010,1,1)
d3 = Date(2010,9,1)
li = Student('li',1,d1,d2,d3)
print(li.in_shcool.date())
class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
class Student:
    def __init__(self,name,num,course):
        self.name = name
        self.num = num
        self.course = course
python = Course('python',20000,'6个月')
s1 = Student('li',1,python)
s2 = Student('li',2,python)
print(s1.__dict__)
# class Date:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def date(self):
#         return '%s-%s-%s' % (self.year,self.month,self.day)
# class Student:
#     def __init__(self,name,num,birth,in_shcool,start_day):
#         self.name = name
#         self.num = num
#         self.birth = birth
#         self.in_shcool = in_shcool
#         self.start_day = start_day
# d1 = Date(2000,1,1)
# d2 = Date(2010,1,1)
# d3 = Date(2010,9,1)
# li = Student('li',1,d1,d2,d3)
# print(li.start_day())
# class Student:
#     def __init__(self,name,num,course):
#         self.name = name
#         self.num = num
#         self.course = course
# class Course:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
# python = Course('python',20000,'6个月')
# s1 = Student('li',1,python)
# python.price = 30000
# print(s1.course.price)
# print(s1.__dict__)
# class Student:
#     def __init__(self,name,num,coures):
#         self.name = name
#         self.num = num
#         self.coures = coures
# class Coures:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
# python = Coures('python',20000,'6个月')
# python.price = 30000
# s1 = Student('li',1,python)
# print(s1.coures.price)

#人狗大战进阶版
# def get_line():
#     with open('userinfo',encoding='utf-8') as f:
#         for line in f :
#             user,pwd = line.strip().split()
#             yield user,pwd
# def register():
#     flag = True
#     while flag:
#         username =input('输入用户名user:>>>')
#         password =input('输入密码pwd:>>>')
#         for user,pwd in get_line():
#             if username == user:
#                 print('用户名已存在')
#                 break
#         else:
#             flag=False
#     with open('userinfo','a',encoding='utf-8') as f:
#         f.write('%s,%s\n'%(username,password))
# register()
# def login():
#     username = input('user:')
#     password = input('pwd:')
#     for user,pwd in get_line():
#         if username == user and pwd == md5(username,password):
#             return  True
# ret = login()
# if ret:
#     print('登录成功')
# register()
# ---------------------------------------------------------------
# class Person:
#     def __init__(self,name,hp,ad,race):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.race = race
#         self.money = 50000
#         self.bao = []
#     def Gj(self,Dog):
#         Dog.hp -= self.ad
#         print('%s攻击了%s，%s掉了%s滴血。'% (self.name,Dog.name,Dog.name,self.ad))
#     def buy_weapon(self,weapon):
#         if weapon.price<=self.money:
#             self.money-=weapon.price
#             self.money = round(self.money,2)
#             self.bao.append(weapon)
#             print('购买%s成功，当前余额%s'%(weapon.name,self.money))
#         else:
#             print('余额不足，请充值。')
#     def use_weapon(self):
#         for weap in self.bao:
#             if weap.t == 'weapon':
#                 self.weapon = weap
#                 self.hp += weap.hp
#                 self.ad += weap.ad
#                 break
# class Dog:
#     def __init__(self,name,hp,ad,kind):
#         self.name = name
#         self.hp = hp
#         self.ad = ad
#         self.kind = kind
#     def Yao(self,Person):
#         Person.hp -= self.ad
#         print('%s咬了%s一口，%s掉了%s血。'% (self.name,Person.name,Person.name,self.ad))
# R = Person('鲁班',500,10,'矮人')
# G = Dog('老黑',650,15,'藏獒')
# s1 = G.Yao(R)
# print(R.hp)

# class Weapon:
#     t = 'weapon'
#     def __init__(self,name,price,ad,hp):
#         self.name = name
#         self.price = price
#         self.ad = ad
#         self.hp = hp
#     def throw(self,Dog):
#         Dog.hp = self.ad
#         print('%s被砖头砸中，掉了%s血' % (Dog.name,self.ad))
# class Dog_GG:
#     def __init__(self,name,ad,hp,kind):
#         self.name = name
#         self.ad = ad
#         self.hp = hp
#         self.kind = kind
#     def fire(self,Person):
#         Person.hp -= self.ad
#         print('%s被火烧了，掉了%s血' % (Person.name,self.ad))
#
# R = Person('鲁班',500,10,'矮人')
# G = Dog('老黑',650,15,'藏獒')
# s1 = G.Yao(R)
# print(R.hp)
#
# WQ = Weapon('砖头',50,30,0)
# DG =Dog_GG('小火龙',100,1000,'龙')
# s2 = WQ.throw(G)
# print(G.hp)
# R.buy_weapon(WQ)
# print(R.bao)
# R.use_weapon()
# print(R.weapon.name)
# print(R.__dict__)
# R.weapon.throw(DG)

# print('\033[0;36m爆竹声中一岁除，')
# print('春风送暖入屠苏。')
# print('千门万户曈曈日，')
# print('总把新桃换旧符。\033[0m')