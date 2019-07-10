# shop 买东西类
    # 1.浏览商品   scan_goods
    # 2.选择商品 ,添加到购物车  choose_goods
    # 3.删除商品   delete_goods

# class Shop:
#     def __init__(self,name):
#         self.name = name
#     def Scan_goods(self):
#         print('%s正在浏览商品'%self.name)
#     def Choose_goods(self):
#         print('%s正在选择商品' % self.name)
#     def Delete_goods(self):
#         print('%s正在删除商品' % self.name)
# s = Shop('alex')
# # s.Choose_goods()
# getattr(s,'Choose_goods')()
# getattr(s,'Choose_goods')()
# getattr(s,'Delete_goods')()

# class Shop:
#     def __init__(self,name):
#         self.name = name
#     def scan_goods(self):
#         print('%s正在浏览商品' % self.name)
#     def choose_goods(self):
#         print('%s正在选择商品' % self.name)
#     def delete_goods(self):
#         print('%s正在删除商品' % self.name)
# s = Shop('taibai')
# getattr(s,'delete_goods')()
# class Shop:
#     def __init__(self,name):
#         self.name = name
#     def scan_goods(self):
#         print('%s正在浏览商品'%self.name)
#
#     def choose_goods(self):
#         print('%s正在选择商品'%self.name)
#
#     def delete_goods(self):
#         print('%s正在删除商品'%self.name)
#
# s = Shop('self哥')
# s.choose_goods()
# s.scan_goods()
# s.delete_goods()

# from sys
# a = 1
# b = 2
# while True:
#     name = input('>>')
#     getattr()