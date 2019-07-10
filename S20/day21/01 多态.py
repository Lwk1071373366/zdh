# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):
#         pass
#     @abstractmethod
#     def back(self):
#         pass
# class Wechatpay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信充值了%s元' % (self.name,self.money))
# class Alipay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝充值了%s元' % (self.name,self.money))
# class Applepay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过苹果充值了%s元' % (self.name,self.money))
#     def back(self):
#         print('退款')
# def pay(person):
#     person.pay()
# app=Applepay('alex',200)
# pay(app)
# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):
#         pass
#     @abstractmethod
#     def back(self):
#         pass
# class Wechatpay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信支付了%s元'%(self.name,self.money))
# class Alipay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝支付了%s元'%(self.name,self.money))
# class Applepay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过苹果支付了%s元'%(self.name,self.money))
#     def back(self):
#         print('退出')
# def pay(Person):
#     Person.pay()
# app = Applepay('alex',20000)
# pay(app)
# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):    # 抽象类
#
#     @abstractmethod   # 如果我必须要实现pay方法,那么我需要给pay加一个装饰器
#     def pay(self):
#         pass   # 创建的这个pay并没有内容,
#                # 之所以写一个pay是为了提醒所有子类你一定要实现一个pay方法
#
#     @abstractmethod
#     def back(self):
#         pass
#
# class Wechatpay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信支付了%s元'%(self.name,self.money))
#
# class Alipay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝支付了%s元'%(self.name,self.money))
#
# class ApplePay(Payment):
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过apple pay支付了%s元' % (self.name, self.money))
#     def back(self):
#         print('退款')
#
# # 归一化设计
# def pay(person):
#     person.pay()
#
# ApplePay('alex',20000)


#
# class Wechatpay:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信支付了%s元'%(self.name,self.money))
#
# class Alipay:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝支付了%s元'%(self.name,self.money))
#
# class ApplePay:
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def fuqian(self):
#         print('%s通过apple pay支付了%s元' % (self.name, self.money))
#
#
# # 归一化设计
# def pay(person):
#     person.pay()
#
#
# wcp = Wechatpay('alex',2000000)
# pay(wcp)
# ali = Alipay('alex',2000000)

# app = ApplePay('alex',2000000)
# pay(app)
# l1 = [7,-8,5,4,0,-2,-5]
# s1=sorted(l1,key=lambda x : (str(x).startswith('-'),abs(x)))
# print(s1)

# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):pass
#     @abstractmethod
#     def back(self):pass
# class Wechatpay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信支付%s元'%(self.name,self.money))
# class Alipay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝支付%s元'%(self.name,self.money))
# class Applepay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过苹果支付了%s元'%(self.name,self.money))
#     def back(self):
#         print('退出')
# def pay(person):
#     person.pay()
# app = Applepay('alex',200000)
# pay(app)


# from abc import ABCMeta,abstractmethod
# class Payment(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):pass
#     @abstractmethod
#     def back(self):pass
# class Wechatpay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过微信支付了%s'%(self.name,self.money))
# class Alipay(Payment):
#     def __init__(self,name,money):
#         self.name= name
#         self.money = money
#     def pay(self):
#         print('%s通过支付宝支付了%s'%(self.name,self.money))
# class Applepay(Payment):
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#     def pay(self):
#         print('%s通过苹果支付了%s'%(self.name,self.money))
#     def back(self):
#         print('退款')
# def pay(person):
#     person.pay()
# app = Applepay('alex',20000)
# pay(app)



# class User:
#     def __init__(self,username,password,email):
#         self.username = username
#         self.password = password
#         self.email = email
#
# user_list = []
# for i in range(3):
#         user = input('请输入用户名:')
#         pwd = input('请输入密码:')
#         email = input('请输入邮箱:')
#         u = User(user,pwd,email)
#         user_list.append(u)
#         # print(u)
# else:
#     for u in user_list:
#         print('我叫%s，邮箱是%s'%(u.username,u.email))

# class User:
#     def __init__(self,name,pwd):
#         self.name =name
#         self.pwd = pwd
# class Account():
#     def __init__(self):
#         self.user_list = []
#
#     def login(self):
#         print('欢迎来到登录环节：')
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         for u in self.user_list:
#             if u.name == username and u.pwd == password:
#                 print('登录成功')
#                 return
#         else:
#             print('登录失败')
#     def register(self):
#         print('欢迎注册环节')
#         uname = input('请输入用户名')
#         pwd = input('请输入密码')
#
#         u = User(uname,pwd)
#         self.user_list.append(u)
#     def run(self):
#         while 1:
#             print('1. 注册')
#             print('2.登录')
#             num = input('请输入你要执行的操作：Q退出')
#             if num == '1':
#                 self.register()
#             elif num == '2':
#                 self.login()
#                 break
#             else:
#                 print('是不是傻')
#
# obj = Account()
# obj.run()
#
#
#
# class User:
#     def __init__(self,username,password,email):
#         self.username = username
#         self.password = password
#         self.email = email
# user_list = []
# for i in range(3):
#     user = input('请输入用户名')
#     pwd = input('请输入密码')
#     email = input('输入邮箱')
#     u = User(user,pwd,email)
#     user_list.append(u)
# else:
#     for u in user_list:
#         print('我叫%s，邮箱是%s'%(u.username,u.email))


# class User:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.pwd = pwd
# class Account:
#     def __init__(self):
#         self.user_list =[]
#     def register(self):
#         print('欢迎来到注册环节')
#         uname = input('输入用户名')
#         pwd = input('输入密码')
#         u = User(uname,pwd)
#         self.user_list.append(u)
#     def login(self):
#         print('欢迎来到登录环节')
#         username = input('请输入用户名')
#         password = input('请输入密码')
#         for u in self.user_list:
#             if u.name == username and u.pwd == password:
#                 print('登录成功')
#                 return
#         else:
#             print('登录失败')
#
#     def run(self):
#             while 1:
#                 print('1，注册')
#                 print('2，登录')
#                 num = input('请输入序号：')
#                 if num == '1':
#                     self.register()
#                 elif num == '2':
#                     self.login()
#                 else:
#                     print('是不是傻')
# obj = Account()
# obj.run()


# class User:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.pwd = pwd
# class Account():
#     def __init__(self):
#         self.user_list = []
#     def login(self):
#         print('欢迎来到登录')
#         username = input('输入用户名')
#         password = input('输入密码')
#         for u in self.user_list:
#             if username ==u.name and password == u.pwd:
#                 print('登录成功')
#                 return
#         else:
#             print('登录失败')
#     def register(self):
#         print('欢迎注册')
#         name = input('>>>')
#         pwd = input('>>>')
#         u = User(name,pwd)
#         self.user_list.append(u)
#     def run(self):
#         while 1:
#             print('1,zhuce')
#             print('2,denglu')
#             num = input('>>>')
#             if num == '1':
#                 self.register()
#             elif num =='2':
#                 self.login()
#                 break
#             else:
#                 print('是不傻')
# obj = Account()
# obj.run()

import pickle
class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
# python = Course('python',20000,'6 months')
# with open('python','ab') as f :
#     pickle.dump(python,f)

import pickle
with open('python','rb') as f :
#     obj1 = pickle.load(f)
# print(obj1.__dict__)
    while 1:
        try:
            obj2 = pickle.load(f)
            print(obj2.__dict__)
        except EOFError:
            break
