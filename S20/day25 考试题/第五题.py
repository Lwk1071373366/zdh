'''
5、请用面向对象的知识完成购物车程序（20分）
现在有商品、用户等内容需要描述
请完成以下功能：
1）启动程序直接进入登录（5分）
2）登录成功之后可以看到用户对应的操作（5分）
	操作包括：查看商品列表，将商品添加到购物车，查看购物车，结算
3）将下面的商品列表使用pickle的方式写入goods_info文件（与大程序逻辑无关，可写在一个另一个py文件里）
商品列表如下：
商品名，商品数量，商品价格
苹果,50,5
香蕉,50,4
雨伞,100,30
咖啡,30,20

4)完成2）中“对应操作”中的具体代码，使你的程序更流畅（5分）
'''
# def login():
#     username = input('>>>')
#     password = input('>>>')
#     with open('userinfo',encoding='utf-8') as f :
#         for line in f :
#             user,pwd = line.strip().split('|')
#             if username == user and password == pwd :
#                 return {'flag':True,'name':username}
#         else:
#             return {'flag':False}
# login()
# lst = ['查看商品列表','将商品添加到购物车','查看购物车','结算']
# for index,opt in enumerate(lst,1):
#     print(index,opt)
#
# import pickle
# goods ='''苹果,50,5
#  香蕉,50,4
#  雨伞,100,30
#  咖啡,30,20'''
# ret = goods.split('\n')
# print(ret)
#
# class Goods(object):
#     def __init__(self,name,count,price):
#         self.name = name
#         self.count = count
#         self.price = price
# with open('goods_info','ab') as f :
#     for item in ret:
#         name,count,price = item.split(',')
#         g = Goods(name,count,price)  #实例化
#         pickle.dump(g,f)


class Goods(object):
    def __init__(self,name,count,price):
        self.name = name
        self.count = count
        self.price =price
class User(object):
    opt_lst = [('查看商品列表','show_goods'),('将商品添加到购物车','add_goods'),
              ('查看购物车','show_car'),('结算','pay')]
    def __init__(self,name):
        self.name = name
        self.car = []
    def show_goods(self):
        print('查看商品列表')
    def add_goods(self):
        print('将商品添加到购物车')
    def show_car(self):
        print('查看购物车')
    def pay(self):
        print('结算')
def login():
    username = input('>>>')
    password = input('>>>')
    with open('userinfo',encoding='utf-8') as f :
        for line in f:
            user,pwd =line.strip().split('|')
            if username == user and pwd == password:
                return {'flag':True,'name':username}
        else:
            return {'flag':False}
ret =login()
if ret['flag']:
    user = User(ret['name'])
    while True:
        for index,opt in enumerate(User.opt_lst,1):
            print(index,opt[0])
        num = int(input('请输入序号>>>'))
        if hasattr(user,User.opt_lst[num-1][1]):
            getattr(user,User.opt_lst[num-1][1])()