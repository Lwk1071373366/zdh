# 1，完成一个商城购物车的程序。
# 商品信息在文件存储的，存储形式：
# name  price
# 电脑  1999
# 鼠标  10
# 游艇  20
# 美女  998
# 要求:
# 1，用户先给自己的账户充钱：比如先充3000元。
# 2，读取商品信息文件将文件中的数据转化成下面的格式：
# goods = [{"name": "电脑", "price": 1999},
#          {"name": "鼠标", "price": 10},
#          {"name": "游艇", "price": 20},
#          {"name": "美女", "price": 998}]
# print(goods)
# 3，页面显示
# 序号 + 商品名称 + 商品价格，如：
# 1   电脑   1999
# 2   鼠标   10
# 3   游艇   20
# 4   美女   998
# n购物车结算
# q或者Q退出程序。
# 4，用户输入选择的商品序号，然后打印商品名称及商品价格, 并将此商品，添加到购物车，用户还可继续添加商品。
# 5，如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 6，用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
# 7，用户输入Q或者q退出程序。
# 8，退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少，并将购买信息写入文件。

money=input('请输入您要充值的金额：')
if money.isdigit():
    money=int(money)
    print('充值成功！')
l1=[]
#将文件中的内容转换成想要的结构 --开始
with open('userinfo','r',encoding='utf-8') as f:
    f.readline().split()
    for i in f:
        k,j=i.split()
        dic={'name':k,'price':int(j)}
        l1.append(dic)
# 将文件中的内容转换成想要的结构 --结束
shopping_car={}   #定义一个购物车
shop_money=0    #消费的金额
while 1:
    #循环展示商品信息--开始
    for i in range(len(l1)):
        print(i+1,l1[i]['name'],l1[i]['price'])
    #循环展示商品信息--结束
    #让用户选择购买的商品序号--开始
    chose=input('请输入商品序号：（Q退出/N结算）')
    # 让用户选择购买的商品序号--结束
    #判断用户输入的序号是否在范围内，并且将商品加入到购物车
    if chose.isdigit() and 0<int(chose)<=len(l1):
        chose=int(chose)-1
        shop_name=l1[chose]['name'] #找到商品名称
        shop_price=l1[chose]['price']#找到商品价格
        #将用户选择的商品加到购物车  ---开始
        if shop_name not in shopping_car:
            shopping_car[shop_name]={'price':shop_price,'num':1}
        else:
            shopping_car[shop_name]['num']+=1
        # 将用户选择的商品加到购物车  ---结束
        print(shopping_car)
        #退出程序--开始
    elif chose.upper()=='Q':
        print('退出')
        shopping_car.clear()
        break
        # 退出程序--结束
        #结算购物车中的商品--开始
    elif chose.upper()=='N':
        #显示购买的商品信息
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            #计算商品价格
            shop_money+=shopping_car[i]['price']*shopping_car[i]['num']
        #循环判断账户余额
        while money < shop_money:
            #账户余额不足时 删除商品
            print('余额不足')
            for i in shopping_car:
                print(i,shopping_car[i]['price'],shopping_car[i]['num'])
                #展示要删除的商品
            del_shop=input('请输入您要删除的商品：（Q退出）')
                #让用户选择要删除的商品
            #删除商品的数量
            if shopping_car.get(del_shop):
                shopping_car[del_shop]['num']-=1
                #每个用户选择的商品数量减一
                shop_money=shopping_car[del_shop]['price']*shopping_car[del_shop]['num']
                #计算最新消费
                if shopping_car[del_shop]['num']==0:
                    #如果商品的数量为零时 清空这个购物车
                    shopping_car.pop(del_shop)
            elif    del_shop.upper()=='Q':
                    exit()
            else:
                #删除商品错误的时候 提示语句
                print('输入有误 请重新输入')
        else:
            #结算购物车中的商品
            money-=shop_money
            #计算最新价格
            print('这个超市我包了')
    else:
        print('输入有误重新输入')
if shopping_car:
    #显示购物车中的商品
    with open('buy_goods','a',encoding='utf-8') as f:
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            #将购买的商品写入文件中
            f.write('购买了：%s,单价：%s,数量：%s' % (i,shopping_car[i]['price'],shopping_car[i]['name']))
    print('消费了：%s，账户余额：%s'% (shop_money,money))
        #提示用户消费了多少钱
# ----------------------------------------------------------------------------
money = input('请输入你要充值的金额：')
if money.isdigit():
    money=int(money)
    print('充值成功：')
l1=[]
with open('userinfo','r',encoding='utf-8') as f:
    f.readline().strip()
    for i in f:
        k,j=i.split()
        dic={'name':k,'price':int(j)}
        l1.append(dic)
shopping_car={}

shop_money=0
while 1:
    for i in range(len(l1)):
        print(i+1,l1[i]['name'],l1[i]['price'])
    chose=input('请输入商品序号：  （Q退出/N结算）')
    if chose.isdigit() and 0<int(chose)<len(l1):
        chose=int(chose)-1
        shop_name=l1[chose]['name']
        shop_price=l1[chose]['price']
        if shop_name not in shopping_car:
            shopping_car[shop_name]={'price':shop_price,'num':1}
        else:
            shopping_car[shop_name]['num']+=1
            print(shopping_car)
    elif chose.upper()=='Q':
        print('退出程序')
        shopping_car.clear()
        break
    elif chose.upper()=='N':
        print('结算')
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            shop_money+=shopping_car[i]['price']*shopping_car[i]['num']
        while money < shop_money:
            print('余额不足')
            for i in shopping_car:
                print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            del_shop=input('请输入要删除的商品')
            if shopping_car.get(del_shop):
                shopping_car[del_shop]['num']-=1
                shop_money=shopping_car[del_shop]['peice']*shopping_car[del_shop]['num']
                if del_shop['num']==0:
                    shopping_car.pop(del_shop)
            elif del_shop=='Q':
                exit()
            else:
                print('删除有误，请重新选择')
        else:
            money-=shop_money
            print('还有钱')
    else:
        print('输入有误，重新输入')
if shopping_car:
    with open('buy_goods','a',encoding='utf-8') as f:
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
        f.write('购买了{},价格{},数量{}'.format(i,shopping_car[i]['price'],shopping_car[i]['num']))
    print('消费了{},余额{}'.format(shop_money,money))
# 完成1 - 3
# 要求为C。
# 完成1 - 4
# 要求为
# C +。
# 完成1 - 6
# 要求为B。
# 完成全部要求并且没有BUG为A
# 或者A +。
#
