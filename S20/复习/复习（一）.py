# day01作业及默写
# Day1作业及默写
# 1.简述变量命名规范
# 1、必须是以字母 数字 下划线组成 2、不能以数字开头3、具有可描述性4、不宜过长5、不能是中文6、不能是Python中的关键字
# 2.name = input(“>>>”) name变量是什么数据类型？
str
# 3.if条件语句的基本结构？
# if 、 if elif、 if elif elif、 if elif else  、if嵌套
# 4.⽤print打印出下⾯内容：
# ⽂能提笔安天下,
# 武能上⻢定乾坤.
# ⼼存谋略何⼈胜,
# 古今英雄唯是君.
msg = '''
# 文能提笔安天下，
# 武能上马定乾坤，
# 心存谋略何人胜，
# 古今英雄唯世君。
# '''
# print(msg)
# 5.利⽤if语句写出猜⼤⼩的游戏：
# 设定⼀个理想数字⽐如：66，让⽤户输⼊数字，如果⽐66⼤，则显示猜测的结果⼤
# 了；如果⽐66⼩，则显示猜测的结果⼩了;只有等于66，显示猜测结果正确。
# i=int(input('输入数字：'))          注意： 输入数字 要考虑 int！
# if i > 66:
#     print('dale')
# elif i < 66:
#     print('xiaole')
# else:
#     print('duile')

# 6.提⽰⽤户输⼊他的年龄, 程序进⾏判断.
# 如果⼩于10, 提⽰⼩屁孩, 如果⼤于10, ⼩于 20, 提⽰⻘春期叛逆的⼩屁孩. 如果
# ⼤于20, ⼩于30. 提⽰开始定性, 开始混社会的⼩ 屁孩⼉, 如果⼤于30, ⼩于40. 提⽰
# 看⽼⼤不⼩了, 赶紧结婚⼩屁孩⼉. 如果⼤于40, ⼩ 于50. 提⽰家⾥有个不听话的⼩
# 屁孩⼉. 如果⼤于50, ⼩于60. 提⽰⾃⼰⻢上变成不听 话的⽼屁孩⼉.如果⼤于60, ⼩
# 于70. 提⽰活着还不错的⽼屁孩⼉. 如果⼤于70, ⼩于 90. 提⽰⼈⽣就快结束了的⼀
# 个⽼屁孩⼉. 如果⼤于90以上. 提⽰. 再⻅了这个世界.
# age = int(input('请输入年龄：'))                  注意： 输入数字 要考虑 int！
# if age < 10:
#     print('xiao pi hai')
# elif age < 20:
#     print('叛逆的小屁孩')
# elif age < 30:
#     print('hun shehuide xiaopihai')
# elif age < 40:
#     print('ganjinjiehun')
# elif age < 50:
#     print('jialii youge butinghuade ')
# elif age <60:
#     print('lao pi hai')
# elif age < 70:
#     print('huozhe haibucuo de ')
# elif age < 90:
#     print('kuai jieshu de ')
# else:print('zaijian')
# 7.单⾏注释以及多⾏注释？
# # 单行   ''' '''   """"""  多行注释
# 8.简述你所知道的Python3x和Python2x的区别？
# Python2 源码混乱  Python3 源码清晰简洁
# 9.提⽰⽤户输入⿇花藤. 判断⽤户输入的对不对. 如果对, 提⽰真聪明, 如果不对, 提
# ⽰输入有误
# name=input('请输入:')
# if name == '麻花藤':
#     print('zhen cong ming ')
# else:
#     print('shuru youwu')
# 10. ⽤户输⼊⼀个⽉份. 然后判断⽉份是多少⽉. 根据不同的⽉份, 打印出不同的饮⻝
# (根据个⼈习惯和⽼家习惯随意编写)11. ⽤户输⼊⼀个分数.
#
#  根据分数来判断⽤户考试成绩的档次
# >=90 A
# >=80 B
# >=70 C
# >=60 D
# < 60 不及格

# fenshu=int(input('输入分数：'))
# if fenshu >= 90:
#     print('A')
# elif fenshu >= 80:
#     print('B')
# elif fenshu >=70:
#     print('c')
# elif fenshu >=60:
#     print('D')
# else:print('bujige')


# 明⽇默写内容：
# 1. 变量的命名规范。
# 2. 单⾏注释，多⾏注释。
# --------------------------------------------------------------------- day 01
# day02作业及默写
# Day2作业及默写
# 1.判断下列逻辑语句的True,False.
# 1）1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# 2）not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# 2.求出下列逻辑语句的值。
# 1),8 or 3 and 4 or 2 and 0 or 9 and 7
# 2),0 or 2 and 3 and 4 or 6 and 0 or 3
# 3.下列结果是什么？
# print(6 or 2 > 1)   6
# 2)、3 or 2 > 1
# 3)、0 or 5 < 4
# 4)、5 < 4 or 3
# 5)、2 > 1 or 6
# print(3 and 2 > 1)
# 7)、0 and 3 > 1
# 8)、2 > 1 and 3
# 9)、3 > 1 and 0
# 10)、3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# 4.while循环语句基本结构？
# 5.利⽤while语句写出猜⼤⼩的游戏：
# 设定⼀个理想数字⽐如：66，让⽤户输⼊数字，如果⽐66⼤，则显示猜测的结果⼤
# 了；如果⽐66⼩，则显示猜测的结果⼩了;只有等于66，显示猜测结果正确，然后退出
# 循环。
# while True:
#     num = int(input('请输入一个数字：'))
#     if num > 66:
#         print('dale')
#     elif num < 66:
#         print('xiaole')
#     else:
#         print('duile')
#         break               注意：break的位置  要放到 最后一个print下面 才能循环起来


# 6.在5题的基础上进⾏升级：
# 给⽤户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果
# 三次之内没有猜测正确，则⾃动退出循环，并显示‘太笨了你....’。
# count = 0
# while count <3:
#     num = int(input('请输入一个数字：'))
#     if num !=66:
#         count+=1                       #计数器 思想  count
#     elif num == 66:
#         print('duile')
#         break
#     if count == 3:
#         print('ben')
#         break


# 7.使⽤while循环输出 1 2 3 4 5 6 8 9 10
# count = 0
# while count < 10:
#     count += 1
#     print(count)
#


# 8.求1-100的所有数的和
# count=0
# sum =0
# while count < 100:
#     count += 1
#     sum += count
# print(sum)
# 9.输出 1-100 内的所有奇数
# count=0
# while count < 100:
#     count+=1
#     if count % 2 ==1:
#      print(count)
# 10.输出 1-100 内的所有偶数
# count= 0
# while count < 101:
#     count += 1
#     if count % 2 == 0:
#         print(count)
# 11.求1-2+3-4+5 ... 99的所有数的和
# count = 1
# sum = 0
# while count < 100:
#     if count % 2 == 1:
#             sum = sum + count         注意：格式  格式
#     else:
#             sum = sum - count
#     count += 1
# print(sum)
# 12.⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格
# 式化）
# count =0
# while count < 3:
#     name=input('用户名：')
#     if name  == '李':                                    注意：count 次数的 使用及计算
#         print('成功')
#         break
#     else:
#         print('错误,还有{}次'.format(3-int(count+1)))
#     count+=1
#

# 13.简述ASCII、Unicode、utf-8编码
# 14.简述位和字节的关系？
# 明⽇默写内容：
# 1. 求1~100所有数的和。
# 2. break continue的含义区别
# 3，Unicode，utf-8，GBK，每个编码英⽂，中⽂，分别⽤⼏个字节表示。
# ------------------------------------------------------------------------------------day02
# day03作业及默写
# Day03作业及默写
# 1.有变量
# name = "aleX leNb" #完成如下操作：
# 1. 移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# 2. 移除name变量左边的"al"并输出处理结果
# print(name.lstrip('al'))
# 3. 移除name变量右⾯的"Nb",并输出处理结果
# print(name.rstrip('Nb'))
# 4. 移除name变量开头的a"与最后的"b",并输出处理结果
# print(name.strip('ab'))      #strip  去两头的
# 5. 判断 name 变量是否以 "al" 开头,并输出结果
# print(name.startswith('al'))
# 6. 判断name变量是否以"Nb"结尾,并输出结果
# print(name.endswith('Nb'))
# 7. 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# print(name.replace('l','p'))
# 8. 将name变量对应的值中的第⼀个"l"替换成"p",并输出结果
# print(name.replace('l','p',1))
# 9. 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# print(name.split('l'))
# 10. 将name变量对应的值根据第⼀个"l"分割,并输出结果。
# print(name.split('l',1))
# 11. 将 name 变量对应的值变⼤写,并输出结果
# print(name.upper())
# 12. 将 name 变量对应的值变⼩写,并输出结果
# print(name.lower())
# 13. 将name变量对应的值⾸字⺟"a"⼤写,并输出结果
# print(name.capitalize())    首字母大写
# 14. 判断name变量对应的值字⺟"l"出现⼏次，并输出结果
# print(name.count('l'))
# 15. 如果判断name变量对应的值前四位"l"出现⼏次,并输出结果
# print(name.count('l',0,4))     加对应的索引
# 16. 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
# print(name.index('N'))
# 17. 从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
# print(name.find('N'))
name = "aleX leNb"
# 18. 从name变量对应的值中找到"X le"对应的索引,并输出结果
# print(name.find('X le'))
# 19. 请输出 name 变量对应的值的第 2 个字符?
# print(name[1])   加索引
# 20. 请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# 21. 请输出 name 变量对应的值的后 2 个字符?
# print(name[-1:-3:-1])
# 22. 请输出 name 变量对应的值中 "e" 所在索引位置（两个e都找）?
# print(name.find('e'))
# one=name.find('e')
# two=name.find('e',one+1)   第二个e 在第一个e+1 后面找
# print(two)
# 2.有字符串s = "123a4b5c"
# s = "123a4b5c"
# a. 通过对s切⽚形成新的字符串s1,s1 = "123"
# print(s[0:3])
# b. 通过对s切⽚形成新的字符串s2,s2 = "a4b"
# print(s[3:6])
# c. 通过对s切⽚形成新的字符串s3,s3 = "1345"
# print(s[0:7:2])
# d. 通过对s切⽚形成字符串s4,s4 = "2ab"
# print(s[1:6:2])
# e. 通过对s切⽚形成字符串s5,s5 = "c"
# print(s[-1])
# f. 通过对s切⽚形成字符串s6,s6 = "ba2"
# print(s[-3:0:-2])
# 3.使⽤while和for循环分别打印字符串s="asdfer"中每个元素。
# s="asdfer"
# for i in s:
#     print(i)
# count=0                  依次打印索引 s的每一个索引即元素
# while count<=len(s):
#     print(s[count])
#     count+=1
# 4.使⽤for循环对s="asdfer"进⾏循环，但是每次打印的内容都是"asdfer"。
# for i in s:
#     print(i)
# 5.使⽤for循环对s="abcdefg"进⾏循环，每次打印的内容是每个字符加上sb， 例如：
# asb, bsb，csb,...gsb。
# for i in s:
    # print(i+'sb')
# 6.使⽤for循环对s="321"进⾏循环，打印的内容依次是："倒计时3秒"，"倒计时2
# 秒"，"倒计时1秒"，"出发！"。
# s="321"
# for i in s:
#     print('倒计时%s秒'%i)   #格式化输出 占位符
# print('出发')
# s='654321'
# for i in s:
#     print('倒计时%s秒'%i)
# print('出发')
# s='987654321'
# for i in s:
#     print('倒计时%s'%i)
# print('出发')
# 7.实现⼀个整数加法计算器(两个数相加)：
# 如：content = input("请输⼊内容:") ⽤户输⼊：5+9或5+ 9或5 + 9，然后进⾏分
# 割再进⾏计算。
# count=input('请输入内容：').strip()
# s=count.split('+')    #输入的是字符串格式  先分割   得到一个列表
# # print(s)
# one=s[0].strip()     #第一个数 : 第一步分割后形成一个列表 所以第一个数是 列表s[] 加第一个数的索引0 第二数 同理
# two=s[1].strip()
# sum=int(one)+int(two) #一定得加int 数字类型
# print(sum)
# s=count.split('+')
# one=s[0]
# two=s[1]
# sum=int(one)+int(two)
# print(sum)

# 8.升级题：实现⼀个整数加法计算器（多个数相加）：
# 如：content = input("请输⼊内容:") ⽤户输⼊：5+9+6 +12+ 13，然后进⾏分割
# 再进⾏计算。
# count= input('请输入内容：').strip()
# l1=count.split('+')
# sum=int(l1[0])+int(l1[1])+int(l1[2])+int(l1[3])+int(l1[4])
# print(sum)
# count=input('请输入：').strip()
# l1=count.split('+')                       先分割  得到一个列表
# sum=0                                     定义一个求和变量
# for i in l1:                               for 循环 列表内的数据
#     i=int(i.strip())                        得到数字类型
#     sum=sum+i                                 最后求和
# print(sum)
# # 9.计算⽤户输⼊的内容中有⼏个整数（以个位数为单位）。
# 如：content = input("请输⼊内容：") # 如fhdal234slfh98769fjdla
# msg= input('请输入内容：').strip()
# count=0
# for i in msg:
#     if i.isdigit():
#         count+=1
# print(count)
# count=0
# for i in msg:
#     if i.isdigit():
#         count+=1
# print(count)
# 10.写代码，完成下列需求：(升级题)
# ⽤户可持续输⼊（⽤while循环），⽤户使⽤的情况：
# 输⼊A，则显示⾛⼤路回家，然后在让⽤户进⼀步选择：
# 是选择公交⻋，还是步⾏？
# 选择公交⻋，显示10分钟到家，并退出整个程序。
# 选择步⾏，显示20分钟到家，并退出整个程序。
# 输⼊B，则显示⾛⼩路回家，并退出整个程序。
# 输⼊C，则显示绕道回家，然后在让⽤户进⼀步选择：
# 是选择游戏厅玩会，还是⽹吧？
# 选择游戏厅，则显示 ‘⼀个半⼩时到家，爸爸在家，拿棍等你。’并让其重新输⼊
# A，B,C选项。
# 选择⽹吧，则显示‘两个⼩时到家，妈妈已做好了战⽃准备。’并让其重新输⼊
# A，B,C选项。
# while 1:
#     xx = input('请输入：')            #选项在循环内
#     if xx=='A':
#         print('大路回家')
#         xx= input('公交？步行？')      #进一步选择
#         if xx=='公交':
#             print('10分钟到家')
#         elif xx=='步行':
#             print('20分钟到家')
#         break
#     elif xx=='B':
#         print('小路回家')
#         break
#     elif xx=='C':
#         print('绕道回家')
#         xx = input('游戏厅？网吧')      #进一步选择
#         if xx=='游戏厅':
#             print('一个半小时到家，爸爸在家，拿棍等你')
#             continue
#         elif xx=='网吧':
#             print('两个小时到家，妈妈已经做好战斗准备')
#             continue
# 11.写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
# count = 0
# sum=0
# while count <100:
#     count !=88
#     if count % 2==1:
#         sum+=count
#     elif count %2==0:
#         sum-=count
#     count+=1
# print(sum)
# while count < 100:
#     count !=88
#     if count % 2 == 1:
#         sum += count
#     elif count % 2==0:
#         sum -= count
#     count+=1
# print(sum)

# 12.判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海 ⾃来⽔来⾃海上
# (升级题)
# str=input('输入：')
# str2=str[::-1]
# if str==str2:
#     print('y')
# else:
#     print('n')   正序=逆序！
# 13. 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，⼩写字⺟，数字， 其它字符
# 共出现了多少次，并输出出来
# l1=input('请输入：')
# shuzi=0                         统计四种 定义四个变量
# daxie=0
# xiaoxie=0
# qita=0
# for index in l1:
#     if index.isdigit() :
#         shuzi=shuzi+1          #is..判断是不是 如果是 自加一 最后用 格式化输出
#     elif index.isupper():
#         daxie=daxie+1
#     elif index.islower():
#         xiaoxie=xiaoxie+1
#     else:
#         qita=qita+1
# print('数字{}，大写{},小写{}.其他{}'.format(shuzi,daxie,xiaoxie,qita))




# 14.制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进
# ⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# name=input('用户输入姓名：')
# where=input('输入地点：')
# hobby=input('输入爱好：')
# f='敬爱的{}，最喜欢在{}，干{}'
# print(f.format(name,where,hobby))

# 明⽇默写内容：
# 分别⽤while，for循环输出字符串s = input（"你想输⼊的内容"）的每⼀个字符。
# --------------------------------------------------------------------------------day03
# day04作业及默写
# Day04作业及默写
# 1.写代码，有如下列表，按照要求实现每⼀个功能
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))
# a. 计算列表的⻓度并输出
# b. 列表中追加元素"seven",并输出添加后的列表
# li.append('seven')
# print(li)
# c. 请在列表的第1个位置插⼊元素"Tony",并输出添加后的列表
# li.insert(0,'Tony')
# print(li)
# d. 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
# li[1]='kelly'
# print(li)
# e. 请将列表
# l2=[1,"a",3,4,"heart"]#的每⼀个元素添加到列表li中，⼀⾏代码实现，不
# 允许循环添加。
# li.extend(l2)
# print(li)
# f. 请将字符串s = "qwert"的每⼀个元素添加到列表li中，⼀⾏代码实现，不允许循
# 环添加。
# s = "qwert"
# li.extend(s)
# print(li)
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# g. 请删除列表中的元素"ritian",并输出添加后的列表
# li.pop(2)
# print(li)
# h. 请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# li.pop(1)
# print(li)
# i. 请删除列表中的第2⾄4个元素，并输出删除元素后的列表
# del li[1:4]
# print(li)
# j. 请将列表所有得元素反转，并输出反转后的列表
# li.reverse()
# print(li)
# k. 请计算出"alex"元素在列表li中出现的次数，并输出该次数。
# s=li.count('alex')
# print(s)
# 2.写代码，有如下列表，利⽤切⽚实现每⼀个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# a. 通过对li列表的切⽚形成新的列表l1,l1 = [1,3,2]
# s=li[0:3]
# print(s)
# b. 通过对li列表的切⽚形成新的列表l2,l2 = ["a",4,"b"]
# print(li[3:6])
# c. 通过对li列表的切⽚形成新的列表l3,l3 = ["1,2,4,5]
# print(li[0:7:2])
# d. 通过对li列表的切⽚形成新的列表l4,l4 = [3,"a","b"]
# print(li[1:6:2])
# e. 通过对li列表的切⽚形成新的列表l5,l5 = ["c"]
# print(li[-1:-2:-1])
# f. 通过对li列表的切⽚形成新的列表l6,l6 = ["b","a",3]
# print(li[-3::-2])
# 3.写代码，有如下列表，按照要求实现每⼀个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# a. 将列表lis中的"tt"变成⼤写（⽤两种⽅式）。
# lis[3][2][1][0]='TT'
# print(lis)
# b. 将列表中的数字3变成字符串"100"（⽤两种⽅式）。
# lis[1]=100
# lis[3][2][1][1]=100
# print(lis)
# c. 将列表中的字符串"1"变成数字101（⽤两种⽅式）。
# lis[3][2][1][2]=101
# print(lis)
#4.请⽤代码实现：
# li = ["alex", "wusir", "taibai"]
# 利⽤下划线将列表的每⼀个元素拼接成字符串"alex_wusir_taibai"
# print('_'.join(li))     列表转字符串用 join 可更改连接符
# 5.利⽤for循环和range打印出下⾯列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)
# 6.利⽤for循环和range找出100以内所有的偶数并将这些偶数插⼊到⼀个新列表中。
# l1=[]
# for i in range(101):
#     if i % 2 == 0:
#         l1.append(i)
# print(l1)
# 7.利⽤for循环和range 找出50以内能被3整除的数，并将这些数插⼊到⼀个新列表中。
# l1=[]
# for i in range(50):
#     if i % 3==0:
#         l1.append(i)
# print(l1)
# # 8.利⽤for循环和range从100~1，倒序打印。
# for i in range(100,0,-1):
#     print(i)
# 9.利⽤for循环和range从100~10，倒序将所有的偶数添加到⼀个新列表中，然后对列
# 表的元素进⾏筛选，将能被4整除的数留下来。
# list=[]
# for i in range(100,9,-1):
#     if i % 4 ==0:
#         list.append(i)
# print(list)
# 10.利⽤for循环和range，将1-30的数字⼀次添加到⼀个列表中，并循环这个列表，将
# 能被3整除的数改成*。
# list=[]
# for i in range(1, 31):
#     list.append(i)
#     # # print(list)
# for i in list:
#     if i % 3 == 0:
#         list[i-1] = '*'
# print(list)
# list=[]
# for i in range(1,31):
#     list.append(i)
# # print(list)
# for i in list:
#     if i % 3== 0:
#         list[i-1]='*'
# print(list)
# 11.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾
# 的所有元素，并添加到⼀个新列表中,最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
# list=[]
# for i in li:
#     i=i.strip()
#     if (i.startswith('A') or i.startswith('a'))and i.endswith('c'):    以 ...开始  以...结束 注意题意
#         list.append(i)
# for i in list:
#     print(i)                                                            最后并循环这个列表
# # lst = []
# for x in li:
#     x = x.strip()
#     if (x.startswith('A') or x.startswith('a')) and x.endswith('c'):
#         lst.append(x)
# for x in lst:
#     print(x,end=' ')
# 12.开发敏感词语过滤程序，提示⽤户输⼊评论内容，如果⽤户输⼊的内容中包含特殊的
# 字符：
# 敏感词列表 li = ["苍⽼师", "东京热", "武藤兰", "波多野结⾐"]
# 则将⽤户输⼊的内容中的敏感词汇替换成等⻓度的*（苍⽼师就替换***），并添加到⼀
# 个列表中；如果⽤户输⼊的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结⾐"]
# comment=input('请输入评论：').strip()
# list=[]
# for name in li:
#     if name in comment:
#         comment=comment.replace(name,len(name)*'*')
# list.append(comment)
# print(list)
# 13.有如下列表
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它⾥⾯的元素。
# for x in li:
#     if type(x) == list:
#         for y in x:
#             if type(y) == str:
#              print(y.lower())
#             else:
#              print(y)
#     else:
#          if type(x) == str:
#              print(x.lower())
#          else:
#             print(x)
# for i in li:                                  先for循环遍历
#     if type(i)==list:                               如果 字符串类型
#         for j in i:                                       在遍历
#             if type(j)==str:                                 如果是字符串
#                 print(j.lower())                                    输出小写
#             else:print(j)                                                否则直接输出
#     else:
#         if type(i)==str:                                  如果是字符串
#             print(i.lower())                                  输出小写
#         else:print(i)                                         否则直接输出
# #我想要的结果是：
# 1 3 4 "a
# lex"
# 3 7
# ,
# 8"taibai"
# 5 ri
# tian
# 明⽇默写内容
# 将列表的增删改查不同的⽅法全部写出来，
# 例如：增：有三种，append：在后⾯添加。Insert按照索引添加，
# expend：迭代着添加。
# ----------------------------------------------------------------day04
# day05作业及默写
# Day05作业及默写
# 1.有如下变量（tu是个元祖），请实现要求的功能
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a. 讲述元祖的特性
# b. 请问tu变量中的第⼀个元素 "alex" 是否可被修改？
# c. 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在
# 其中添加⼀个元素 "Seven"
# d. 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其
# 中添加⼀个元素 "Seven"
# 2.字典dic,dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 1. 请循环输出所有的key
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# s=dic.keys()
# for i in s:
#     print(i)
# for  i in dic.keys():
#     print(i)
# 2. 请循环输出所有的value
# s=dic.values()
# for i in s:
#     print(i)
# c. 请循环输出所有的key和value
# for k,v in dic.items():
#     # print(k,v)
#     print(k,v,sep=':')
# d. 请在字典中添加⼀个键值对，"k4": "v4"，输出添加后的字典
# dic['k4']='v4'
# print(dic)
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
# dic['k1']='alex'
# print(dic)
# f. 请在k3对应的值中追加⼀个元素 44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
# g. 请在k3对应的值的第 1 个位置插⼊个元素 18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)
# 3.av_catalog = {
# "欧美":{
# "www.太⽩.com": ["很多免费的,世界最⼤的","质量⼀般"],
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
# a,给此 ["很多免费的,世界最⼤的","质量⼀般"]列表第⼆个位置插⼊⼀个 元素：'量很
# ⼤'。
# b,将此 ["质量很⾼,真的很⾼","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过"
# 删除。
# c,将此["质量怎样不清楚,个⼈已经不喜欢⽇韩范了","verygood"]列表的
# "verygood"全部 变成⼤写。
# d,给 '⼤陆' 对应的字典添加⼀个键值对 '1048' :['⼀天就封了']
# e,"oldboy.com": ["多是⾃拍,⾼质量图⽚很多","资源不多,更新慢"]
# f,给此["全部免费,真好,好⼈⼀⽣平安","服务器在国外,慢"]列表的第⼀个元素，加上
# ⼀句话：'可以爬下来'
# 4.有字符串"k: 1|k1 :2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....} (升级题)
# s="k: 1|k1 :2|k2:3 |k3 :4"
# dic={}
# s1=s.split('|')
# print(s1)
# for i in s1:
#     # print(i,type(i))  #'k: 1,k1 :2,k2:3,k3 :4'得到一个字符串
#     s2=i.split(':')
#     # print(s2)          #['k', ' 1']，['k1 ', '2']，['k2', '3 ']，['k3 ', '4']得到四个小列表
#     k,v=s2
#     # print(k,v)
#     dic[k.strip()]=int(v)
# print(dic)
# s1=s.split('|')
# for i in s1:
#     s2=i.split(':')
#     k,v=s2
#     dic[k.strip()]=int(v)
# print(dic)
# 5.元素分类
# 有如下值li= [11,22,33,44,55,66,77,88,99,90]，将所有⼤于 66 的值保存⾄字典的
# 第⼀个key中，将⼩于 66 的值保存⾄第⼆个key的值中。
# 即： {'k1': ⼤于66的所有值列表, 'k2': ⼩于66的所有值列表}
# li= [11,22,33,44,55,66,77,88,99,90]
# dic={}
# l1=[]
# l2=[]
# for i in li:
#     if i > 66:
#         l1.append(i)
# # print(l1)
#     if i < 66:
#         l2.append(i)
# # print(l2)
# dic['k1']=l1
# # print(dic)
# dic['k2']=l2
# print(dic)
# 6.输出商品列表，⽤户输⼊序号，显示⽤户选中的商品
# 商品列表：
# goods = [{"name": "电脑", "price": 1999},
# {"name": "⿏标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "美⼥", "price": 998}, ]
# 要求:
# 1：⻚⾯显示 序号 + 商品名称 + 商品价格，如：
# 1 电脑 1999
# 2 ⿏标 10
# …
# 2：⽤户输⼊选择的商品序号，然后打印商品名称及商品价格
# 3：如果⽤户输⼊的商品序号有误，则提示输⼊有误，并重新输⼊。
# for i in goods:
#     print(i['name'],i['price'])
# while 1:
#         for index in range(len(goods)):
#             print('{}\t{}\t{}\t'.format(index+1,goods[index]['name'],goods[index]['price']))
#         num=input('请输入序号：').strip()
#         if num.isdigit():
#             num=int(num)
#             if 0<num<=len(goods):
#                 print(goods[num-1]['name'],goods[num-1]['price'])
#             else:print('超出范围')
#         elif num.upper()=='Q':
#             print('退出程序')
#             break
#         else:
#             print('非数字，请重新输入')

# while True:
#         for index in range(len(goods)):
#             print('{}\t{}\t{}\t'.format(index+1,goods[index]['name'],goods[index]['price']))
#         num=input('请输入序号：  按q或Q退出程序').strip()
#         if num.isdigit():
#             num = int(num)
#             if 0<num<=len(goods):
#                 print(goods[num-1]['name'],goods[num-1]['price'])
#             else:
#                 print('超出范围')
#         elif num.upper()=='Q':
#                 print('退出')
#                 break
#         else:
#              print('非数字 请重新输入')


# 4：⽤户输⼊Q或者q，退出程序。明⽇默写内容。
# 1)字典的增删改查。
# 2)过滤敏感字符代码的默写。
# ---------------------------------------------------------------------------------------day05
# Day6作业及默写
# 1.
# 使⽤循环打印以下效果:
# 1:
# *
# **
# ** *
# ** **
# ** ** *
# i=0
# j=0
# for i in range(1,7):
#     for j in range(1,i):
#         print('*',end='')
#     print()  换行
# 2:
# ** ** *
# ** **
# ** *
# **
# *
# i=0
# j=0
# for i in range(6,1,-1):
#     for j in range(1,i):
#         print('*',end='')
#     print()

# 3:
# *
# ** *
# ** ** *
# ** ** ** *
# ** ** ** ** *
# i=0  #行
# j=0  #每一行的个数
# for i in range(1,6):
#     for j in range(0,2*i-1):
#         print('*',end='')
#     print()
#
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
# l1=['最','第一','稀缺','国家级']
# l2=[]
# comment=input('请输入你的评论：').strip()
# for name in l1:
#     # print(name)
#     # for name in comment:
#     if name in comment:
#         print('不合法')
#     else:
#         print('合法')
# while True :
#     s = input("请输入一个广告:")
#     if "最"in s or "第一"in s or "稀缺"in s or "国家级"in s:
#         print("你输入的广告不合法,请重新输入")
#     else:
#         print("你输入的广告合法.")
# while 1 :
#     s = input('请输入你的评论：')
#     if '最' in s or '第一' in s or '稀缺' in s or '国家级' in s :
#         print('你输入的不合法')
#     else:
#         print('合法')
# 3.
# 敲七游戏.从1开始数数.遇到7或者7的倍数（不包含17, 27, 这种数）要在桌上敲⼀下.编程来完成敲七.
# 给出⼀个任意的数字n.从1开始数.数到n结束.把每个数字都放在列表中, 在数的过程中出现7或
# 者7的倍数（不包含17, 27, 这种数）.则向列表中添加⼀个
# '咣'
# 例如, 输⼊10.
# lst = [1, 2, 3, 4, 5, 6, '咣', 8, 9, 10]
# l1=[]
# num=input('请输入一个数字：').strip()
# for i in range(1,int(num)):
#     if i % 7 ==0:
#         i='咣'
#     l1.append(i)
# print(l1)
# l1=[]
# num = input('请数入一个数字：').strip()
# for i in range(1,int(num)):
#     if i % 7 ==0:
#         i='咣'
#     l1.append(i)
# print(l1)
# 4.
# 念数字给出一个字典.在字典中标识出每个数字的发音.包括相关符号.然后由用户输入一个数字.让程序读出相对应的发音(不需要语音输出.单纯的打印即可)
dic = {
    "-": "fu",
    "0": "ling",
    "1": "yi",
    "2": "er",
    "3": "san",
    "4": "si",
    "5": "wu",
    "6": "liu",
    "7": "qi",
    "8": "ba",
    "9": "jiu",
    ".": "dian",
}
# msg=input('请输入：')
# for i in msg:
#     if i in dic:
#         print(dic[i],end=' ')
# msg=input('请输入：')
# for i in msg:
#     if i in dic:
#         print(dic[i],end=' ')
msg=input('请输入：')
for i in msg:
    print(i)
    if i in dic:
        print(dic[i],end=' ')


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
# lst = ['⾦瓶梅', '解救吾先⽣', '美国往事', '⻄⻄⾥的美丽传说']
# dic={}
# while 1 :
#     print('请投票：')
#     for i in range(len(lst)):
#         print('电影序号{}电影名称{}'.format(i+1,lst[i]))
#     num=input('请输入序号：').strip()
#     if num.upper()=='Q':
#         print('退出')
#         break
#     elif 0 < num <=len(lst):
#         dic[lst[num-1]]=dic.get(lst[num-1],0)+1
#         print('给{}投票成功'.format(lst[num-1]))
#     else:print('超出范围')
# for mingzi,piaoshu in dic.items():
#     print('电影{}票数{}'.format(mingzi,piaoshu))
#
# while 1:
#     print('请投票：')
#     for index in range(len(lst)):
#         print('电影序号{}电影名称{}'.format(index+1,lst[index]))
#     num=input('请输入序号：').strip()
#     if num.upper()=='Q':
#         print('退出')
#         break
#     elif num.isdigit():
#         num=int(num)
#         if  0<num<=len(lst):
#             dic[lst[num-1]]=dic.get(lst[num-1],0)+1
#             print('给{}投票成功'.format(lst[num-1]))
#     else:
#         print('超出范围')
# for mingcheng,piaoshu in dic.items():
#         print('电影{},票数{}'.format(mingcheng,piaoshu))



#
# 明日默写内容：
# l1 = [11, 22, 33, 44, 55]
# s=l1[-2:0:-2]
# print(s)
# 用代码将列表的索引的偶数位对应的元素删除。
# （不能使用del
# l1[::2]
# 这种方法）
# 2，dic = {“k1”: “v1”, “k2”: “v2”, “k3”: “v3”, “name”: “太白”} 将字典中含有k元素的所有key全部删除。
# dic = {'k1':'v1','k2':'v2','k3':'v3','name':'太白'}
# l1=[]
# for i in dic:
#     if 'k' in i:
#         l1.append(i)
# for  i in l1:
#     dic.pop(i)
# print(dic)
# num = int (input("请输入一个数:"))
# w = 0
# while num >= 1:
#     num = num // 10
#     w =w+1
# print('这个数是%s位数' % (w))
