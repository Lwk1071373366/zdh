# names = [‘alex’,’taibai’,’wusir’,‘yuan’,‘eva’] 
# ( for 循环遍历，与列表推导式 两种方法做)找出上述名字中长度大于4的名字,
# 组成列表打印出来. 
# names = ['alex','taibai','wusir','yuan','eva']
# print([name for name in names if len(name)>4])
# print(list(filter(lambda name:len(name)>4,names)))
'''
一，编程题（共60分（含20分加分题））

1、请用推到式或者循环实现以下需求，有字典d如下，请找出字典中key以’a’开头的项，
并判断年龄，如果年龄大于40，
那么对应的value修改成老年，小于40，对应的项修改成青年
d = {'alex': 84,'wusir': 73,'taibai':18,'amber':20}
结果示例：{'alex': '老年', 'amber': ‘青年’}（5分）

'''
d = {'alex': 84,'wusir': 73,'taibai':18,'amber':20}
# d.pop('wusir')
# d.pop('taibai')
# for i in d :
#     if i.startswith('a'):
#         if d[i] > 40:
#             d[i] ='老年'
#         else: d[i] ='青年'
# print(d)
# d = {k :'老年' if d[k]>40 else '青年' for k in d if k.startswith('a')}
# print(d)
# d1 = {}
# for k in d :
#     if k.startswith('a'):
#         if d[k] > 40:
#             d[k]='老年'
#         else:
#             d[k]='青年'
#         d1[k]=d[k]
# print(d1)

