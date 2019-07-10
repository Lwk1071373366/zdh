# money=input('')
# if money.isdigit():
#     money=int(money)
#     print(' ')
# l1=[]
# with open('userinfo','r',encoding='utf-8') as f :
#     f.readline().split()
#     for i in f:
#         k,j=i.split()
#         dic={'name':k,'price':int(j)}
#         l1.append(dic)
#     print(l1)
# shopping_car={}
# shopping_money=0
# while 1:
#     for i in range(len(l1)):
#         print(i+1,l1[i]['name'],l1[i]['price'])
#     chose=input('购买序号：')
#     if chose.isdigit() and 0< int(chose)<=len(l1):
#         chose=int(chose)-1
#         shop_name=l1[chose]['name']
#         shop_price=l1[chose]['price']
#         if shop_name not in shopping_car:
#             shopping_car[shop_name]={'price':shop_price,'num':1}
#         else:
#             shopping_car['shop_name']['num']+=1
#             print(shopping_car)
#     elif chose.upper()=='Q':
#         print('tuichu')
#         shopping_car.clear()
#         break
#     elif chose.upper()== 'N':
#         for i in shopping_car:
#             print(i,shopping_car[i]['peice']*shopping_car[i]['num'])
#             shopping_money=shopping_car[i]['price']*shopping_car[i]['num']
#         while money < shopping_money:
#             print('余额不足')
#             for i in shopping_car:
#                 print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             del_shop=input('shu ru yao shanchu de ')
#             if shopping_car.get(del_shop):
#                 shopping_car[del_shop]['num']-=1
#                 shopping_money=shopping_car[del_shop]['price']*shopping_car[del_shop]['num']
#                 if shopping_car[del_shop]['num']==0:
#                     shopping_car.pop(del_shop)
#             elif del_shop.upper()=='Q':
#                 exit()
#             else:
#                 print('shanchu you wu')
#         else:
#             money-=shopping_money
#             print('youqianren')
#     else:
#         print('shuru you wu ')
# if shopping_car:
#     with open('wenjian','a',encoding='utf-8') as f:
#         for i in shopping_car:
#             print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             f.write('商品%s价格%s数量%s'.format(i,shopping_car[i]['price'],shopping_car[i]['num']))
#     print('消费了%s余额%s'.format(shopping_money,money))


# money = input('请充值：')
# if money.isdigit():
#     money =int(money)
#     print('充值成功')
# l1= []
# with open('userinfo','r',encoding='utf-8')as f:
#     f.readline().split()
#     for i in f :
#         k,j =i.split()
#         dic = {'name':k,'price':int(j)}
#         l1.append(dic)
# shopping_car = {}
# shopping_money = 0
# while 1 :
#     for i in range(len(l1)):
#         print(i+1,l1[i]['name'],l1[i]['price'])
#     chose = input('请输入序号：（Q退出/N结算）')
#     if chose.isdigit() and 0< int(chose) <=len(l1):
#         chose = int(chose)-1
#         shop_name = l1[chose]['name']
#         shop_price = l1[chose]['price']
#         if shop_name not in shopping_car:
#             shopping_car[shop_name] = {'peice':shop_price,'num':1}
#         else:
#             shopping_car[shop_name]['num'] +=1
#             print(shopping_car)
#     elif chose.upper() == 'Q':
#         print('退出')
#         shopping_car.clear()
#         break
#     elif chose.upper() =='N':
#         for i in shopping_car:
#             print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             shopping_money += shopping_car[i]['price']*shopping_car[i]['num']
#         while money < shopping_money:
#             print('余额不足')
#             for i in shopping_car:
#                 print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             del_shop = input('请输入要删除的商品')
#             if shopping_car.get(del_shop):
#                 shopping_car[del_shop]['num'] -= 1
#                 shopping_money = shopping_car[del_shop]['price']*shopping_car[del_shop]['num']
#                 if shopping_car[del_shop]['num'] == 0:
#                     shopping_car.pop(del_shop)
#             elif    del_shop.upper() =='Q':
#                     exit()
#         else:
#             money -= shopping_money
#             print('有钱')
#     else:
#         print('输入有误')
# if shopping_car:
#     with open('buy_goods','a',encoding='utf-8') as f:
#         for i in shopping_car:
#             print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             f.write('购买了%s，单价%s，数量%s'% (i,shopping_car[i]['price'],shopping_car[i]['num']))
#     print('消费了%s余额%s'%(shopping_money,money))



# money = input('请输入金额：')
# if money.isdigit():
#     money = int(money)
#     print('ok')
# l1 = []
# with open('userinfo',encoding='utf-8') as f :
#     f.readline().split()
#     for i in f :
#         k,j = i.strip().split()
#         dic = {'name':k,'price':j}
#         l1.append(dic)
# shopping_car = {}
# shopping_money = 0
# while True:
#     for i in range(len(l1)):
#         print(i+1,l1[i]['name'],l1[i]['price'])
#     chose = input('输入商品序号：')
#     if chose.isdigit() and 0 < chose.isdigit() <=len(l1):
#         chose = int(chose)-1
#         shopping_name = l1[chose]['name']
#         shopping_price = l1[chose]['price']
#         if shopping_name not in shopping_car:
#             shopping_car[shopping_name] = {'price':shopping_price,'num':1}
#         else:
#             shopping_car[shopping_name]['num'] += 1
#             print(shopping_car)
#     elif chose.upper() == 'Q':
#         print('退出')
#         shopping_car.clear()
#         break
#     elif chose.upper() == 'N':
#         for i in shopping_car:
#             print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#         while money < shopping_money:
#             print('余额不足')
#             for i in shopping_car:
#                 print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             del_shop = input('请输入要删除的商品')
#             if shopping_car.get(del_shop):
#                 shopping_car[del_shop]['num'] -= 1
#                 shopping_money = shopping_car[del_shop]['pricr']*shopping_car[del_shop]['num']
#                 if shopping_car[del_shop]['num'] == 0:
#                     shopping_car.pop(del_shop)
#                 elif del_shop =='Q':
#                     exit()
#                 else:
#                     print('输入有误')
#         else:
#             money -= shopping_money
#             print('有钱')
#     else:
#         print('输入有误')
# if shopping_car:
#     with open('buy_goods','a',encoding='utf-8') as f:
#         for i in shopping_car:
#             print(i,shopping_car[i]['price'],shopping_car[i]['num'])
#             f.write('购买了%s，单价%s，数量%s' % (i,shopping_car[i]['pricr'],shopping_car[i]['num']))
#     print('消费了%s，余额%s'%(shopping_money,money))
#



money = input('请输入充值金额：')
if money.isdigit():
    money = int(money)
    print('充值成功')
l1 = []

with open('userinfo',encoding='utf-8') as f :
    f.readline().split()
    for i in f :
        k,v = i.split()
        dic ={'name':k,'price':v}
        l1.append(dic)
shopping_car = {}
shonping_money = 0
while 1:
    for i in range(len(l1)):
        print(i+1,l1[i]['name'],l1[i]['price'])
    chose = input('请输入商品序号：Q退出N结算 ')
    if chose.isdigit() and 0<int(chose) <=len(l1):
        chose = int(chose) - 1
        shop_name = l1[chose]['name']
        shop_price = l1[chose]['price']
        if shop_name not in shopping_car:
            shopping_car[shop_name] ={'price':shop_price,'num':1}
        else:
            shopping_car[shop_name]['num'] +=1

    elif chose.upper() =='Q':
        print('退出')
        shopping_car.clear()
        break
    elif chose.upper() == 'N':
        print('结算')
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            shonping_money = shopping_car[i]['price']*shopping_car[i]['price']
        while shonping_money > money:
            print('余额不足')
            for i in shopping_car:
                print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            del_shop = input('q请输入要删除的商品序号：')
            if shopping_car.get(del_shop):
                shopping_car[del_shop]['num'] -=1
                shonping_money = shopping_car[del_shop]['price']*shopping_car[del_shop]['num']
                if shopping_car[del_shop]['num'] == 0:
                    shopping_car.pop(del_shop)
            elif del_shop.upper() == 'Q':
                exit()
            else:print('输入有误')
        else:
            money -= shonping_money
            print('有钱')
    else:
        print('输入有误请重新输入')
if shopping_car:
    with open('buy_goods','a',encoding='utf-8') as f :
        for i in shopping_car:
            print(i,shopping_car[i]['price'],shopping_car[i]['num'])
            f.write('购买了%s，单价是%s，数量是%s'%(i,shopping_car[i]['price'],shopping_car[i]['num']))
    print('消费了%s，余额%s'%(shonping_money,money))





























