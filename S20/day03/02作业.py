# 有变量name = "aleX leNb" 完成如下操作：
# 1. 移除 name 变量对应的值两边的空格,并输出处理结果

#
# name ='aleX leNB'
# print(name.strip())
# 2. 移除name变量左边的"al"并输出处理结果

# name ='aleX leNB'
# print(name[2:])
# 移除name变量右⾯的"Nb",并输出处理结果
# name='aleX leNB'
# print(name[0:7])
# 移除name变量开头的a"与最后的"b",并输出处理结果
# name='aleX leNB'
# # print(name[1:8])
# 判断 name 变量是否以 "al" 开头,并输出结果
# name = 'aleX leNB'
# # print(name.startswith('al'))
# 判断name变量是否以"Nb"结尾,并输出结果
# name = 'aleX leNB'
# print(name.endswith('NB'))
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
# name = 'aleX leNB'
# print(name.replace('l','p'))
# 将name变量对应的值中的第⼀个"l"替换成"p",并输出结果

# print(name.replace('l','p'))

# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# print(name.split('l'))
# 将name变量对应的值根据第⼀个"l"分割,并输出结果。
# print(name.split('l',1))
# 将 name 变量对应的值变⼤写,并输出结果
# print(name.upper())
# 将 name 变量对应的值变⼩写,并输出结果
# print(name.lower())
# 将name变量对应的值⾸字⺟"a"⼤写,并输出结果
# print(name.capitalize())

# 判断name变量对应的值字⺟"l"出现⼏次，并输出结果
# . 从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
# print(name.find('N'))
# print(name.index('N'))
# 从name变量对应的值中找到"X le"对应的索引,并输出结果
# print(name.find('X le'))
# 请输出 name 变量对应的值的第 2 个字符?
# name = 'aleX leNB'
# 请输出 name 变量对应的值中 "e" 所在索引位置（两个e都找）?
# print(name.find('e'))


# 有字符串s = "123a4b5c"
# a.通过对s切⽚形成新的字符串s1,s1 = "123"
# b. 通过对s切⽚形成新的字符串s2,s2 = "a4b"
# c. 通过对s切⽚形成新的字符串s3,s3 = "1345"
# d. 通过对s切⽚形成字符串s4,s4 = "2ab"
# e. 通过对s切⽚形成字符串s5,s5 = "c"
# # f. 通过对s切⽚形成字符串s6,s6 = "ba2"
# s='123a4b5c'
# s1=print(s[0:3])
# s2=print(s[3:6])
# s3=print(s[0:7:2])
# s4=print(s[1:6:2])
# s5=print(s[-1])
# s6=print(s[-3:-8:-2])
#


# 使⽤while和for循环分别打印字符串s="asdfer"中每个元素
# s='asdfer'
#
# for i in s:
#     print(i)
#
#
#
# count = 0
# while count < len(s):
#     print(s[count])
#     count += 1
#
# count =0
# while count<len(s):
#     print(s[count])
#     count += 1
# 使⽤for循环对s="asdfer"进⾏循环，但是每次打印的内容都是"asdfer"
# s ='asdfer'
# for i  in s :
#     print(s)
# 使⽤for循环对s="abcdefg"进⾏循环，每次打印的内容是每个字符加上sb， 例如：
# asb, bsb，csb,...gsb
# s ='abcdefg'
# for i in s:
#     i = i+"sb"
#     print(i)
# 使⽤for循环对s="321"进⾏循环，打印的内容依次是："倒计时3秒"，"倒计时2
# 秒"，"倒计时1秒"，"出发

# s= '321'
# for i in s:
#     if i == '3':
#       print('倒计时3S')
#     if i == '2':
#       print('倒计时2S')
#     if i == '1':
#       print('倒计时1S')
# else:print('出发')
#


# 计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和

x= 1
result = 0
while x <= 99:
    if x % 2 == 1:
        result += x
    else :
        if x != 88:
            result -= x
    x += 1

print(result)

x=1
s=0
while x <=99:
    if x % 2 ==1 :
        s = s + x
    else:
        if x != 88:
            s = s - x
    x= x+1
print(s)




# 判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海 ⾃来⽔来⾃海上
# a ="上海自来水来自海上"




# content = input("请输⼊内容:") ⽤户输⼊：5+9或5+ 9或5 + 9，然后进⾏分
# 割再进⾏计算
#
# sum = 0
# content = input('请输入内容：').strip()
# print(content)
# s = content.split('+')
# print(s)
# for i in  s:
#   sum += int(i)
# print(sum)


# 计算⽤户输⼊的内容中有⼏个整数（以个位数为单位）。
# 如：content = input("请输⼊内容：") # 如fhdal234slfh98769fjdla
#
# content = input('请输入内容：')
# count = 0
# for i in  content:
#   if i.isdigit():
#     count += 1
#   else:continue
# print(count)


# 如：content = input("请输⼊内容:") ⽤户输⼊：5+9+6 +12+ 13，然后进⾏分割
# 再进⾏计算。
# sum = 0
# content = input('请输入：')
# count = content.rsplit('+')
# print(count)
# for i in count:
#   sum = sum +int(i)
# print(sum)

#
# content =input('输入数字')
# count = 0
# for i in content:
#   if i.isdigit():
#     count +=1
#   else:continue
# print(count)
#

# 写代码，完成下列需求：(升级题)
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
# A，B,C选项

















# 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，⼩写字⺟，数字， 其它字符
# 共出现了多少次，并输出出来
# s =input('请输入：')
# count = 0
# for i in  s :
#  if i.islower():
#     count += 1
# print(count)
# if i.isdigit():
#        count += 1
# print(count)
# if i.isupper():
#     count += 1
# print(count)
# if i.isalnum():
#     count += 1
# print(count)
# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进
# ⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
# f ='敬爱可亲的{}，最喜欢在{}的{}'
# name = input('姓名')
# hobby = input('爱好')               formatde 应用
# addr =input('地点')
#
# print(f.format(name,hobby,addr))
# a = '敬爱的{}，喜欢{}干{}'
# name = input('姓名')
# hobby=input('爱好')
# addr=input('地点')
#
# print(a.format(name,hobby,addr))

# 输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，⼩写字⺟，数字， 其它字符
# 共出现了多少次，并输出出来
# upp=0
# low=0
# dig=0
# oth=0
# s = input('内容')
# for i in s :
#     if i.upper() :
#         upp+=1
#     if i.lower():
#         low+=1
#     if i.isdigit() :
#         dig+=1
#     else:
#         oth+=1
# print('大写{}，小写{}，数字{}，其他{}'.format(upp,low,dig,oth))
#
# counter_upper = 0
# counter_lower = 0
# counter_digit = 0
# counter_other = 0
#
#
#
# s = input("input a string:")
# for x in s:
#     if x.isdigit():
#         counter_digit += 1
#     elif x.isupper():
#         counter_upper += 1
#     elif x.islower():
#         counter_lower += 1
#     else:
#         counter_other += 1
#
# print("大写：{}，小写：{}，数字：{}，其他{}".format(counter_other,counter_upper,counter_digit,counter_lower))
#
# counter_upper = 0
# counter_lower = 0
# counter_digit = 0
# counter_other = 0
#
# s = input('内容:')
# for i  in s:
#     if i.upper():
#         counter_upper += 1
#     elif i.lower():
#         counter_lower += 1
#     elif i.isdigit():
#         counter_digit += 1
#     else:
#         counter_other += 1
#     print('大写{}，小写{}, 数字{},其他{}'.format(counter_upper,counter_lower,counter_digit,counter_other))

