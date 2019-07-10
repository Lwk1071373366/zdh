# day05作业及默写
# 1.有如下变量（tu是个元祖），请实现要求的功能
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a. 讲述元祖的特性
#  不能修改 只能查询
# b. 请问tu变量中的第⼀个元素 "alex" 是否可被修改？
#   不能被修改
# c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在
# 其中添加⼀个元素 "Seven"
# print(tu[1],type(tu[1]))
# print(tu[1].append("Seven")) 返回None
# d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其
# 中添加⼀个元素 "Seven"
# set=tu[1]
# set1=set[2]
# set1['k3']
# print(set1['k3'],type(set1['k3'])) #对应的值是元祖 不能修改
# set2=set1['k3'].append('Seven')
# print(set2)
# 2.字典dic,\
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 1. 请循环输出所有的key                                用for循环
# print(dic.keys())
# 2. 请循环输出所有的value
# print(dic.values())
# c. 请循环输出所有的key和value
# print(dic.items())
# d. 请在字典中添加⼀个键值对，"k4": "v4"，输出添加后的字典
# dic['k4']='v4'
# print(dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1']='alex'
# print(dic)
# f. 请在k3对应的值中追加⼀个元素 44，输出修改后的字典
# dic['k3'].append('44')
# print(dic)
# g. 请在k3对应的值的第 1 个位置插⼊个元素 18，输出修改后的字典
# dic['k3'][0]='18'
# print(dic)
# av_catalog = {
# "欧美":{
# "www.太⽩.com": ["很多免费的，世界最多的",'质量一般'],
# "www.alex.com": ["很多免费的,也很⼤","质量⽐yourporn⾼点"],
# "oldboy.com": ["多是⾃拍,⾼质量图⽚很多","资源不多,更新慢"],
# "hao222.com":["质量很⾼,真的很⾼","全部收费,屌丝请绕过"]
# },
# "⽇韩":{
# "tokyo-hot":["质量怎样不清楚,个⼈已经不喜欢⽇韩范了","verygood"]
# },
# "⼤陆":{
# "1024":["全部免费,真好,好⼈⼀⽣平安","服务器在国外,慢"]
# }}
#
# # a,给此 ["很多免费的,世界最⼤的","质量⼀般"]列表第⼆个位置插⼊⼀个 元素：'量很
# av_catalog[0][1]='量很大'
# print(av_catalog)
# b,将此 ["质量很⾼,真的很⾼","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过"
# 删除。
# c,将此["质量怎样不清楚,个⼈已经不喜欢⽇韩范了","verygood"]列表的
# "verygood"全部 变成⼤写。
# d,给 '⼤陆' 对应的字典添加⼀个键值对 '1048' :['⼀天就封了']
# e,"oldboy.com": ["多是⾃拍,⾼质量图⽚很多","资源不多,更新慢"]
# f,给此["全部免费,真好,好⼈⼀⽣平安","服务器在国外,慢"]列表的第⼀个元素，加上
# ⼀句话：'可以爬下来'
# 4.有字符串"
# #  k: 1|k1 :2|k2:3 |k3 :4  #" 处理成字典 {'k':1,'k1':2....} (升级题)
s1='k: 1|k1 :2|k2:3 |k3 :4'
# dic = {}
# l1 = s1.split('|')  # ['k: 1', 'k1 :2', 'k2:3 ', 'k3 :4']
# for i in l1:
#     # print(i)  # 'k: 1'
#     small_list = i.split(':')
#     # print(small_list)
#     key,value = small_list
#     # print(key,value)
#     dic[key.strip()] = int(value)
# print(dic)
dic={}
l1 = s1.split('|')
for i in l1 :
    small_list=i.split(':')
    key,value=small_list
    dic[key.strip()]=int(value)
print(dic)








# l={}
# s=s.replace(' ',' ').split('|')
# for i in range(0,len(s)):
#     s[i]=s[i].split(':')
#     l.setdefault(s[i][0],s[i][1])
# print(l)

# dict={}
# s1=s.split('|') #得到:['k: 1', 'k1 :2', 'k2:3 ', 'k3 :4']
# for i in range(len(s1)) :
#     print(i)    #得到: k: 1  k1 :2 k2:3  k3 :4
#     a =i.split(':')
#     # print(a)   #得到:['k', ' 1'] ['k1 ', '2']['k2', '3 ']['k3 ', '4']
#     b=':'.join(a)
#     # print(b)       #得到: k: 1  k1 :2 k2:3  k3 :4
#
#     dict.setdefault(b)
#     # print(i)
#     dict.setdefault(i)
# print(dict)











# 5.元素分类
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有⼤于 66 的值保存⾄字典的
# 第⼀个key中，将⼩于 66 的值保存⾄第⼆个key的值中。
# 即： {'k1': ⼤于66的所有值列表, 'k2': ⼩于66的所有值列表}
# li= [11,22,33,44,55,66,77,88,99,90]
# dict={'k1':[],'k2':[]}
# for index in li:
#     if index > 66:
#         dict['k1'].append(index)
#     elif index < 66:
#         dict['k2'].append(index)
# print(dict)











# # k1_dic={}
# # k2_dic={}
# k_dic={}
# list1=[]
# list2=[]
# for i in li :
#     if i < 66:
#         list1.append(i)
#     else:list2.append(i)
# # k1_dic={'k1':list1}
# # k2_dic={'k2':list2}
# k_dic={'k1':list1,'k2':list2}
# print(k_dic)

# print(k1_dic)
# print(k2_dic)





# 6.输出商品列表，⽤户输⼊序号，显示⽤户选中的商品
# # 商品列表：
goods = [{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}, ]

while 1:
    for index in range(len(goods)):
        print('{} {} {}'.format(index+1,goods[index]['name'],goods[index]['price']))
    goods_num=input('请输入选项：输入Q或q退出程序').strip()

    if goods_num.isdigit():
        goods_num=int(goods_num)
        if 0 < goods_num <len(goods):
            print(goods[goods_num-1]['name'],goods[goods_num-1]['price'])
        else:
            print('输入的超出范围，请重新输入')
    elif    goods_num.upper()=='Q':
        break
    else:
        print('你输入的有非数字元素，请重新输入')
# # 要求:
# # 1：⻚⾯显示 序号 + 商品名称 + 商品价格，如：
# # 1 电脑 1999
# # 2 ⿏标 10
# for i in range(len(goods)):
#     print(i)




# …
# 2：⽤户输⼊选择的商品序号，然后打印商品名称及商品价格
# 3：如果⽤户输⼊的商品序号有误，则提示输⼊有误，并重新输⼊。
# 4：⽤户输⼊Q或者q，退出程序。
#
#
#
#
#
#
# 明⽇默写内容。
# 1)字典的增删改查。
# 2)过滤敏感字符代码的默写。
# li = ["苍⽼师","东京热","武藤兰","波多野结⾐"]
# l1 = []
# comment = input('请输⼊评论>>>')
# for i in li:
#     if i in li:
#      comment = comment.replace(i,'*'*len(i))
#     l1.append(comment)
# print(l1)
