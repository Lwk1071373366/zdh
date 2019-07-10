# 1:
# *
# **
# ***
# ****
# *****

# i = 1
# while i <6:
#     j =1
#     while j<=i :
#         print('*',end='')
#         j += 1
#     print('')
#     i += 1
# 2:
# *****
# ****
# ***
# **
# *
# i = 1
# while i <6:
#     j =1
#     while j<=i :
#         print('*',end='')
#         j += 1
#     print('')
#     i += 1





# 3:
# *
# ***
# *****
# *******
# *********
# i = 1
# while i <6:
#     j =1
#     while j<=2*i-1:
#         print('*',end='')
#         j += 1
#     print('')
#     i += 1
for line in range(1,6):
    for col in range(1,2*line):
        print('*',end='')
    print()








# 2.
# 输入⼀个⼴告标语.判断这个广告是否合法.根据最新的⼴告法来判断. ⼴告法内容过
# 多.我们就判断是否包含
# '最', '第⼀', '稀缺', '国家级'
# 等字样.如果包含.提⽰, ⼴告不
# 合法
# 例如,
# (1)
# 老男孩python世界第⼀.不合法
# (2)
# 今年过年不收礼啊.收礼只收脑⽩⾦.合法
# comment_list=input('请输入一个广告语：').strip()
# index=0
# comment_list1=['最','第一','稀缺','国家级']
# for index in comment_list1:
#     if index in comment_list:
#         print('不合法')
#
#



# 3.
# 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.
# 给出⼀个任意的数字n.从1开始数.数到n结束.把每个数字都放在列表中, 在数的过程中出现7或
# 者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个
# '咣'
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# lst=[]
# num = input("一个数：")
# for i in range(len(num)):
#     if i % 7 == 0:
#         lst.append('i')
# print(lst)
# 念数字给出一个字典.在字典中标识出每个数字的发音.包括相关符号.然后由用户输入一个数字.让程序读出相对应的发音(不需要语音输出.单纯的打印即可)
#
# 5.
# 电影投票.程序先给出⼀个⽬前正在上映的电影列表.由⽤户给每⼀个电影投票.最终将该⽤户投票信息公布出来 。
# 要求：
# 1，用户输入序号，进行投票。比如输入序号
# 1，给金瓶梅投票1。
# 2，每次投票成功，显示给哪部电影投票成功。
# 3，退出投票程序后，要显示最终每个电影的投票数。
#
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# 结果: {'⾦瓶梅': 99, '解救吴先⽣': 80, '美国往事': 6, '⻄⻄⾥的美丽传说': 23}
# #
# lst =['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
#
# # lst =['金瓶梅','解救吾先生','美国往事','西西里的美丽传说']
#
# num=input('请输入电影序号：').strip()
# dic={'金瓶梅': 99,'解救吾先生':80,'美国往事':6,'西西里的美丽传说':23}

lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']

# print(lst[0])  lst[] 中括号内加索引 打印出 元素
dic={}
# while 1 :
#     print('请投票：')
#     for index in range(len(lst)):
#         print('电影序号{}，电影名称{}'.format(index+1,lst[index]))
#     num=input('请输入电影序号：').strip()
#     if num.upper()=='Q':
#         print('感谢参与！')
#         break
#     elif num.isdigit():
#         num=int(num)
#         if 0<num<=len(lst):
#             dic[lst[num-1]]=dic.get(lst[num-1],0)+1
#             print('给{},投票成功'.format(lst[num-1]))
#         else:
#             print('超出范围')
#     else:
#         print('输入有误')
# for dianyingming , dianyingpiaoshu in dic.items():
#     print('电影{},票数{}'.format(dianyingming,dianyingpiaoshu))

while 1:
    print("请投票")
    for index in range(len(lst)):
        print('电影序号{}，电影名称{}'.format(index + 1, lst[index]))
    num = input('请输入序号：按q或者Q退出').strip()
    if num.upper() == 'Q':
        print('退出')
        break
    elif num.isdigit():
        num = int(num)
        if 0 < num <= len(lst):
            dic[lst[num - 1]] = dic.get(lst[num - 1], 0) + 1
            print('给{}投票成功'.format(lst[num - 1]))
        else:
            print('超出范围')
for mingzi, piaoshu in dic.items():
    print('电影{}，票数{}'.format(mingzi, piaoshu))








# 明日默写内容：
# l1 = [11, 22, 33, 44, 55]
# for i in range(len(l1)-1,-1,-1):
#     if i % 2 == 0:
#         l1.pop(i)
# print(l1)
# 用代码将列表的索引的偶数位对应的元素删除。
# （不能使用del
# l1[::2]
# 这种方法）
#dic = {“k1”: “v1”,“k2”: “v2”, “k3”: “v3”, “name”: “太白”} #将字典中含有k元素的所有key全部删除。
dic={'k1':'v1','k2':'v2','k3':'v3','name':'taibai'}
l1=[]
for i in dic :
    if 'k'in i :
        l1.append(i)
for i in l1:
        dic.pop(i)
print(dic)
