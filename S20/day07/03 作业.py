# day08作业及默写
# Day08作业及默写
# 1.有如下⽂件，a1.txt，⾥⾯的内容为：
# ⽼男孩是最好的学校，
# 全⼼全意为学⽣服务，
# 只为学⽣未来，不为牟利。
# 我说的都是真的。哈哈
# 分别完成以下的功能：
# a,将原⽂件全部读出来并打印。
# f=open('老男孩',encoding='utf-8',)
# print(f.read())
# b,在原⽂件后⾯追加⼀⾏内容：信不信由你，反正我信了。
# f=open('老男孩',encoding='utf-8',mode='a')
# print(f.write('信不信由你，反正我信了'))
# f.close()
# c,将原⽂件全部读出来，并在后⾯添加⼀⾏内容：信不信由你，反正我信了。
# f=open('老男孩',encoding='utf-8',mode='r')
# print(f.read())
# f.close()
# f=open('老男孩',encoding='utf-8',mode='a')
# print(f.write('信不信由你，反正我信了'))
# f.close()
# d,将原⽂件全部清空，换成下⾯的内容：
# f=open('老男孩',encoding='utf-8',mode='w')
# msg='''
# 每天坚持⼀点，
# 每天努⼒⼀点，
# 每天多思考⼀点，
# 慢慢你会发现，
# 你的进步越来越⼤。
# '''
# print(f.write(msg))
# f.close()
 # 每天坚持⼀点，
# 每天努⼒⼀点，
# 每天多思考⼀点，
# 慢慢你会发现，
# 你的进步越来越⼤。
# 2.有如下⽂件，t1.txt,⾥⾯的内容为：
# 葫芦娃，葫芦娃，
# ⼀根藤上七个⽠
# ⻛吹⾬打，都不怕，
# 啦啦啦啦。
# 我可以算命，⽽且算的特别准:
# 上⾯的内容你肯定是⼼⾥默唱出来的，对不对？哈哈
# 分别完成下⾯的功能：
# a,以r+的模式打开原⽂件，判断原⽂件是否可读，是否可写。
# f=open('t1.txt',encoding='utf-8',mode='r+')
# print(f.read())
# print(f.readable())   true
# print(f.writable())   true
# f.close()

# b,以r的模式打开原⽂件，利⽤for循环遍历⽂件句柄。
# f=open('t1.txt',encoding='utf-8',mode='r')
# for i in f:
#     print(i)
#
# c,以r的模式打开原⽂件，以readlines()⽅法读取出来，并循环遍历 readlines(),
# 并分析b,与c 有什么区别？深⼊理解⽂件句柄与 readlines()结果的区别。
# f=open('t1.txt',encoding='utf-8',mode='r')
# for i in f.readlines():
#     print(i)

# d,以r模式读取‘葫芦娃，’前四个字符。
# f=open('t1.txt',encoding='utf-8',mode='r')
# print(f.read(4))
# f.close()
# e,以r模式读取第⼀⾏内容，并去除此⾏前后的空格，制表符，换⾏符。
# f=open('t1.txt',encoding='utf-8',mode='r')
# print(f.readline().strip())
# f.close()
# f,以r模式打开⽂件，从‘⻛吹⾬打.....’开始读取，⼀直读到最后。
# f=open('t1.txt',encoding='utf-8',mode='r')
# f.seek(24)
# # print(f.read())
# f.seek(21)
# print(f.read())
# f.close()
# g,以a+模式打开⽂件，先追加⼀⾏：‘⽼男孩教育’然后在从最开始将 原内容全
# 部读取出来。
# f=open('t1.txt',encoding='utf-8',mode='a+')
# f.write('lao')
# print(f.read())
# f.close()

# h,截取原⽂件，截取内容：‘葫芦娃，葫芦娃，’
# f=open('t1.txt',encoding='utf-8',mode='r')
# def truncate(t1,size:int(24)):
#     print(f.read())
# f.close()
# 3.⽂件a.txt内容：每⼀⾏内容分别为商品名字，价钱，个数。
# apple 10 3
# tesla 100000 1
# mac 3000 2
# lenovo 30000 3
# chicken 10 3
# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},
# {'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
# li = []
# num_sum = 0
# with open('a.txt','r',encoding='utf-8')as f:
#     for i in f:
#         name,price,num = i.split()
#         dic={'name':name,'price':int(price),'num':int(num)}
#         li.append(dic)
#         sum = int(price) * int(num)
#         num_sum += sum
# print(li)
# print(num_sum)
l1=[]
num_sum = 0
with open('a.txt',encoding='utf-8',mode='r') as f:
    for i in f :
        name,price,num =i.split()
        dic = {'name':name,'price':int(price),'num':int(num)}
        l1.append(dic)
        # sum=int(price)*int(num)
        # num_sum += sum
print(l1)
# print(num_sum)
# 4.有如下⽂件：
# alex是⽼男孩python发起⼈，创建⼈。
# alex其实是⼈妖。
# 谁说alex是sb？
# 你们真逗，alex再⽜逼，也掩饰不住资深屌丝的⽓质。
# 将⽂件中所有的alex都替换成⼤写的SB（⽂件的改的操作）。




# 5.⽂件a1.txt内容(升级题)
# name:apple price:10 amount:3 year:2012
# name:tesla price:100000 amount:1 year:2013
# .......通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3,year:2012},
# {'name':'tesla','price':1000000,'amount':1}......]
# 并计算出总价钱。



# 6.⽂件a1.txt内容(升级题)
# 序号 部⻔ ⼈数 平均年龄 备注
# 1 python 30 26 单身狗
# 2 Linux 26 30 没对象
# 3 运营部 20 24 ⼥⽣多
# .......
# 通过代码，将其构建成这种数据类型：
# [{'序号':'1','部⻔':Python,'⼈数':30,'平均年龄':26,'备注':'单身狗'},
# ......]
# 明⽇默写内容：
# 就是第4题的代码（课上讲过）。