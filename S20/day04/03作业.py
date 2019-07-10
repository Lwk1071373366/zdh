# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"].
# a.计算列表的⻓度并输出
# b. 列表中追加元素"seven",并输出添加后的列表
# c. 请在列表的第1个位置插⼊元素"Tony",并输出添加后的列表
# d. 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# e. 请将列表l2=[1,"a",3,4,"heart"]的每⼀个元素添加到列表li中，⼀⾏代码实现，不
# 允许循环添加。
# f. 请将字符串s = "qwert"的每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循
# 环添加。
# g. 请删除列表中的元素"ritian",并输出添加后的列表
# h. 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# i. 请删除列表中的第2⾄4个元素，并输出删除元素后的列表
# j. 请将列表所有得元素反转，并输出反转后的列表
# k. 请计算出"alex"元素在列表li中出现的次数，并输出该次数
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))
# li.append('seven')
# print(li)
# li.insert(0,'Tony')
# print(li)
# li.insert(1,'Kelly')
# print(li)
# l2=[1,"a",3,4,"heart"]
# li.extend(l2)
# print(li)
# s = "qwert"
# li.extend(s)
# print(li)
# del li[2]
# print(li)
# li.pop(1)
# print(li.pop(1))
# print(li)
# del li[1:4]
# print(li)
# li.reverse()
# print(li)
# print(li.count('alex'))
# 写代码，有如下列表，利⽤切⽚实现每⼀个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# a. 通过对li列表的切⽚形成新的列表l1,l1 = [1,3,2]
# b. 通过对li列表的切⽚形成新的列表l2,l2 = ["a",4,"b"]
# c. 通过对li列表的切⽚形成新的列表l3,l3 = ["1,2,4,5]
# d. 通过对li列表的切⽚形成新的列表l4,l4 = [3,"a","b"]
# e. 通过对li列表的切⽚形成新的列表l5,l5 = ["c"]
# f. 通过对li列表的切⽚形成新的列表l6,l6 = ["b","a",3]
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# # del li[3::1]
# # print(li)
# # del li[1::2]
# # print(li)
# # del li[:6:2]
# # print(li)
# # del li[:7:1]
# # print(li)
# print(li[-3::-2])

# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# a. 将列表lis中的"tt"变成⼤写（⽤两种⽅式）。
# b. 将列表中的数字3变成字符串"100"（⽤两种⽅式）。
# c. 将列表中的字符串"1"变成数字101（⽤两种⽅式）。


# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0]=lis[3][2][1][0].upper()
# print(lis)
# lis[1]=100
# lis[3][2][1][1]=100   还有一种
# print(lis)
# lis[3][2][1][2]=101
# print(lis)
# li = ["alex", "wusir", "taibai"]
# 利⽤下划线将列表的每⼀个元素拼接成字符串"alex_wusir_taibai"
# li = ["alex", "wusir", "taibai"]
# l1='_'.join(li)
# print(l1)
#

# 利⽤for循环和range打印出下⾯列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)
# for i in range(len(li)):
#     print(i)
# for i in range(len(li)):
#     print(i)

# 利⽤for循环和range找出100以内所有的偶数并将这些偶数插⼊到⼀个新列表中
# list=[]
# for i in range(100):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# for i in range (2,100,2):
#     list.append(i)
# print(list)

# 利⽤for循环和range从100~1，倒序打印
# for i in range(100,1,-1):
#     print(i)


#-----------------------------------------------------------------------
# 利⽤for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然后对列
# # 表的元素进⾏筛选，将能被4整除的数留下来。
# list = []                       #先定义一个空列表 用for循环 遍历 100~10的偶数
#                                 # 既然是偶数 可以用加步长的方式解决这个问题
#                                 #再用i 取4的倍数 将满足条件的 增加到列表中
# # list1=[]
# for i in range(100,10,-2):
#     if i % 4 == 0:
#         list.append(i)
# print(list)
# # --------------------------------------------------------------
# 利⽤for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个列表，将
# 能被3整除的数改成*
# list = []
# list1 = []
# for i in range(1,31,1):
#     list.append(i)
#     if i % 3 != 0:
#         list1.append(i)
#     else:i = '*'
#     list1.append(i)
# print(list1)
#------------------------------------------------------------
# li=[]
# index=0                      先定义一个空列表  先定义一个空列表，及index
#                              在30以内遍历，遍历到的数据
#                              添加到空列表中， 若 遍历到
#                                的数字取3等于0.则视为3的倍
#                                数，将index替换为星号，并
#                                    每次自加一。
# for i in range(1,31,1):
#     li.append(i)
# for i in li:
#     if i % 3==0:
#         li[index]='*'
#     index=index+1
# print(li)
# ----------------------------------------------------------
# lst = []
# for x in range(1,31):
#     lst.append(x)
#
# index = 0
# while index < len(lst):         # while循环做法
#     if lst[index] % 3 == 0:
#         lst[index] = '*'
#     index += 1
#
# print(lst)
# -----------------------------------------------------------

# 查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾
# 的所有元素，并添加到⼀个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]  先用 for...in 取出元素
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc",]
# # lst = []
# # for x in li:
# #     x = x.strip()
# #     if (x.startswith('A') or x.startswith('a')) and x.endswith('c'):
# #         lst.append(x)
# # for x in lst:
# #     print(x,end=' ')
# #
# # lst=[]
# # for i in li:
# #     i=i.strip()
# #     if (i.startswith('A')or i.startswith('a')) and i.endswith('c'):
# #         lst.append(i)
# # for i in lst:
# #     print(i)
#
# lst = []
# for i in li:
#     i=i.strip()
#     if (i.startswith('A') or i.startswith('a') ) and i.endswith('c'):
#         lst.append(i)
#     if i in lst:
#         print(i)
#先定义个空列表 给变量 lst ； 用for循环，若 i 在 列表li里：题中要求元素去空格，所以 将去掉空格的i 重新赋值给 i
#此时 得到的 i 是去掉空格的；用if 判断 若 以A或a 并以c开头的元素 添加的一个新列表中 ；若 遍历到的 i 在这个列表中，输出即可。



# list = []                                                               创建一个新列表
# for i in li :                                                            取出的元素赋值一个变量‘J’并去空格
#      j = i.strip()                                                       判断条件：因为是以C为结尾的所有元素 所有是True
#      if j.endswith('c')and j.startswith('A')or j.startswith('a') :       所以‘c’ 在前 ....
#         # print(j)
#         list.append(j)
# print(list)

# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# list=[]
# for i in li:
#     j = i.strip()
#     if j.endswith('c')and j.startswith('A')or j.startswith('a'):
#         list.append(j)
# print(list)
# list=[]
# for i in li:
#     j = i.strip()
#     if j.endswith('c')and j.startswith('A')or j.startswith('a'):
#         list.append(j)
# print(j)
# 开发敏感词语过滤程序，提示⽤户输⼊评论内容，如果⽤户输⼊的内容中包含特殊的
# 字符：
# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结⾐"]
# 则将⽤户输⼊的内容中的敏感词汇替换成等⻓度的*（苍⽼师就替换***），并添加到⼀
# 个列表中；如果⽤户输⼊的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结⾐"]
# comment_list=[]
# comment=input('请输入你的评论：')
# for name in li:
#     if name in comment:
#         comment=comment.replace(name,len(name)*'*')
# comment_list.append(comment)
# print(comment_list)
# li = ["苍老师", "东京热", "武藤兰", "波多野结⾐"]
# comment_list=[]
# comment=input('请输入你的评论：')
# for name in li:
#     if name in comment:
#         comment=comment.replace(name,len(name)*'*')
# comment_list.append(comment)
# print(comment_list)
#
#
# li= ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# l1=[]
# comment = input('请输入评论：')
# for i in li:
#     if i in comment:
#         comment=comment.replace(i,len(i))
# l1.append(comment)
# print(li)



# 利⽤下划线将列表的每⼀个元素拼接成字符串"alex_wusir_taibai"
# li = ["alex", "wusir", "taibai"]
# l1='_'.join(li)
# print(l1)
#
