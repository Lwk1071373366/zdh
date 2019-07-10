# <h1>hahaha<\h1>
import re
# re.findall()
# <h2>wahaha<\h2>
# <title>qqxing<\title>
# ret= re.findall('\d+','alex123yuan234')
# print(ret)
#
# import re
# 正则表达式练习
# 1、匹配一篇英文文章的标题 类似 The Voice Of China
ret1=re.findall(r'(?:[A-Z][a-z]*)(?: [A-Z][a-z]*)*','The Voice Of China')
print(ret1)
# 2、匹配一个网址
# ret3=re.findall(r'(?:https|http|ftp):\/\/[^\s]+','https://www.baidu.com')
# print(ret3)
    # 类似 https://www.baidu.com http://www.cnblogs.com
# ret=re.findall(r'https?://www.\w+.com','http://www.cnblogs.com')
# print(ret)
# 3、匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# ret=re.findall(r'\d{1,4}.\d{1,2}.\d{1,2}','2018/12/06')
# print(ret)
# 4、匹配15位或者18位身份证号
# ret=re.findall('[1-9]\d{14}(?:\d{2}[\dX])?','123456789123456')
# print(ret)
# 5、从lianjia.html中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
# import re
# with open('lianjia.html',encoding='utf-8') as f:
#     content = f.read()
# par = '<div class="userinfo clear">.*?<a.*?data-sl="">(?P<loc>.*?)</a>.*?<span class="divide">/</span>(?P<type>.*?)<span class="divide">/</span>(?P<area>.*?)<span class="divide">'
# ret = re.findall(par,content,re.S)
# print(ret)
# 6、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
# ret=re.findall(r'(?:-\d{2}/\d)','1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))')
# print(ret)
# for i in ret:
#     print(i.group())
# 7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法
# ret=re.findall('\W+','9-2*5/3+7/3*99/4*2998+10*568/14')
# l1=[]
# # print(ret)
# for i in ret:
#     if i =='*' or i =='/':
#         l1.append(i)
# print(l1)
# 8、完成三级菜单
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
# menu
# def threeLM(dic):
#     while True:
#         for k in dic:print(k)
        # key = input('input>>').strip()
        # if key == 'b' or key == 'q':return key
        # elif key in dic.keys() and dic[key]:
        #     ret = threeLM(dic[key])
        #     if ret == 'q': return 'q'

# threeLM(menu)
# print('北京\n上海\n山东')
# while True:
#     location=input('请输入位置：>>>').strip()
#     if location=='北京':
#         print('海淀\n昌平\n朝阳\n东城')
#         location = input('请输入位置：>>>').strip()
#         if location == '海淀':
#             print('五道口\n中关村\n上地')
#             location = input('请输入位置：>>>').strip()
#             if location == '五道口':
#                 print('soho\n网易\ngoogle')
#             elif location == '中关村':
#                 print('爱奇艺\n汽车之家\n优酷')
#             elif location == '上地':
#                 print('百度')
#         elif location == '昌平':
#             print('沙河')
#             location = input('请输入位置：>>>').strip()
#             if location == '沙河':
#                 print('老男孩')
#                 print('北航')
#             print('天通苑')
#             print('回龙观')
#     if location == '上海':
#         print('闵行\n闸北\n浦东')
#         location = input('请输入位置：>>>').strip()
#         if location == '闵行':
#             print('人民广场')
#             location = input('请输入位置：>>>').strip()
#             if location == '人民广场':
#                 print('炸鸡店')
#         elif location == '闸北':
#             print('火车站')
#             location = input('请输入位置：>>>').strip()
#             if location == '火车站':
#                 print('携程')
#         elif location == '浦东':
#             print(' ')
#     elif location == '山东':
#         print(' ')
#     else:
#         break

# 递归函数实现三级菜单
# 9、大作业：计算器
import re
# s='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
'''
计算流程:
1.将括号表达式(内部不包含括号)匹配出来
2.计算括号表达式的值,用计算值替换原括号表达式
    计算处理流程:
    1)从左至右匹配,匹配出乘法或除法表达式,计算出值,塞回去替换匹配的内容
    2)乘除法运算都已处理完,对剩下表达式从左至右匹配
    3)匹配一个加法或减法运算式,计算出值,塞回去,替换匹配的表达式
    4)直到没有匹配运算式,停止,本轮括号表达式计算替换值流程完成
3.再次进行括号表达式(内部不包含括号)匹配
4.重复2
5.直到匹配不出括号表达式,直接对剩余运算式进行乘除加减处理
'''
s='1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

def func():
    ret=re.search(r'\([^()]+\)',s)
    ret1=ret.group()


func()



# l1=[]
# def count(s):
#     ret=re.finditer(r'\([^()]+\)',s)
#     for i in ret:
#         ret1=i.group()
#         # print(ret1.split('/'))
#         print(ret1.split())
#
#     for i in ret:
#         ret1=re.search(r'(?:-\d{2}/\d)',ret[0])
#     print(ret1.group())
#     s1=ret1.group()
#     s2=s1.split('/')
    # print(s2,type(s2))
    # for j in s2:
    #     yi=int(s2[0])/int(s2[1])   # 一括号等于8
    # print(yi)
    # ret2 = re.search(r'', s)
    # print(ret2.group())


# count(s)
#10、继续完成day16的五个功能题


# 1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
#\([^()]+\)

# 从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法
# \d+(\.\d+)?[*/]\d+(\.\d+)?

# _*_ coding:utf-8 _*_
# import re
# s = '1 - 2 * ( (-60*-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# def count(s):  #计算没有括号的算数
#     s = ''.join(s.split())   #去除空格
#     for i in s:
#         if i == '*':
#             cheng = re.search('-?\d+\.?\d*\*-?\d+\.?\d*',s)
#             print(cheng)
#             c = cheng.group().split('*')
#             # print(c)
#             sum = str(float(c[0])*float(c[1]))
#             print(sum)
#             s = s.replace(cheng.group(),'+%s'%sum)
#             if re.search('\+\++',s):
#                 s = s.replace(re.search('\+\++',s).group(),'+')
#             if s[0] == '+':s = s.strip('+')
#         if i == '/':
#             chu = re.search('-?\d+\.?\d*\/-?\d+\.?\d*',s)
#             c = chu.group().split('/')
#             sum = str(float(c[0])/float(c[1]))
#             s = s.replace(chu.group(),sum)
#     while '-'in s or '+' in s:
#         jia=re.search('-?\d+\.?\d*\+-?\d+\.?\d*',s)
#         if not jia:
#             if s[0] != '-':
#                 jian = re.split('-',s)
#                 print(jian)
#                 s = str(float(jian[0])-float(jian[1]))
#             if s.count('-') == 2:
#                 jian = re.split('-',s)
#                 jian.remove('')
#                 s = str(float(jian[0])+float(jian[1]))
#                 s = '-%s'%s
#             break
#         c = jia.group().split('+')
#         sum = str(float(c[0])+float(c[1]))
#         s = s.replace(jia.group(), '+%s' %sum)
#         if s[0] == '+':s = s.strip('+')
#     return s
# def brackets(strs):  #去括号
#     strs = ''.join(strs.split())  #去除空格
#     res = re.findall('\([^()]+\)', strs)
#     for i in range(len(res)):
#         res[i] = res[i][1:-1]
#     return strs, res
# while '('in s: #有括号时 取括号内的式子计算
#     strs, res = brackets(s)
#     rep = []  #存放括号内计算的结果准备替换
#     for i in res:
#         rep.append(count(i))
#     for i in range(len(rep)):
#         strs = strs.replace('(%s)' % res[i], rep[i])
#     if '--' in strs:
#         strs = strs.replace('--', '+')
#     s = strs
# print(count(s))  #没有括号，进行最后一步计算


