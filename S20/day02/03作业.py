# print(bool('1>1or3<4or4>5and2>1and9>8or7<6'))
# print(bool('not2>1and3<4or4>5and2>1and9>8or7<6'))
# TRUE


# 利⽤while语句写出猜⼤⼩的游戏：
# 设定⼀个理想数字⽐如：66，让⽤户输⼊数字，如果⽐66⼤，则显示猜测的结果⼤
# 了；如果⽐66⼩，则显示猜测的结果⼩了;只有等于66，显示猜测结果正确，然后退出
# 循环

# num = 66
# while True:
#     num = int(input('请输入一个数字：'))
#     if num > 66:
#         print('大了')
#
#     elif num < 66:
#         print('小了')
#
#     elif num == 66:
#         print('结果正确')

# 在5题的基础上进⾏升级：
# 给⽤户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果
# 三次之内没有猜测正确，则⾃动退出循环，并显示‘太笨了你....’。

# num = 66
# count = 1
# while count <=3:
#     num = int(input('请输入一个数字：'))
#     count += 1
#     if num > 66:
#         if count == 4 :
#             print('太笨了')
#             break
#     if num < 66:
#         if count == 4:
#             print('太笨了')
#             break
#     if num == 66:
#       if count <=3:
#         print('聪明')
#         break

# 使⽤while循环输出 1 2 3 4 5 6 8 9 10
#
# count = 1
#
# while count<11:
#     if count == 7:
#         pass
#     else:print(count)
#     count=count+1


# 求1-100的所有数的和

# count = 1
# s  = 0
# while True :
#     s = s + count
#     count =count + 1
#     if count > 100 :
#      break
# print(s)
#
#
# count = 1
# s = 0
#
# while count <101:
#     s = s +count
#     count =count + 1
# print(s)


# 输出 1-100 内的所有奇数
# count = 1
#
# while count < 100:
#     print(count)
#     count % 2 == 1
#     count = count + 2
#     if count == 101:
#          break

# 输出 1-100 内的所有偶数
# count = 2
# while True:
#     print(count)
#     count = count+2
#     if count ==102:
#         break

# 求1-2+3-4+5 ... 99的所有数的和
# 思路！！！ ？？？
# a = 1
# b = 0
# while a<100:
#     c= a % 2
#     if c == 1 :
#         b= b +a
#     else:b = b -a
#     a += 1
# print(b)


# ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格
# 式化）
username = 'kai'
password = '666'
count = 1
while count < 4:
    username = input('请输入姓名：')
    password = input('请输入密码：')
    if username =='kai'and password == '666':
      print('登录成功了')
      break

    else:
      print('登录失败，剩余%s次，请重新登录' % (3-count))


    count = count +1



# name = input('请输入你的姓名：')
# age = input('请输入你的年龄：')
# job = input('请输入你的工作：')
# hobby = input('请输入你的爱好：')
# msg = '''-----userinfo of %s----
# name = %s
# age = %d
# job = %s
# hobby = %s
# -----end-----'''% (name,name,int(age),job,hobby)
# print(msg)

# count = 1
#
# while count<11:
#     if count== 9:
#         pass
#     else:
#         print(count)
#     count = count +1
#
#
#
# count = 1
#
# while count < 100:
#     if count % 10 == 0:
#         pass
#     else:print(count)
#     count=count +1

# age_of_0ldboy = 66
# count = 0
# while count < 3:
#     guess=int(input('>>>'))
#     if guess == age_of_0ldboy:
#         print("ni zhen bang")
#         break
#     count=count+1

username = 'kai'
password = '111'
count =1
while count < 4:
    username =input('请输入你的名字')
    password = input('请输入你的密码：')
    if username == 'kai'and password=='111':

        print('正确')
        break
    else:print('请重新输入，还剩%s次' % (3-count))

    count=count+1


