from django.shortcuts import render,HttpResponse,redirect
from zuoye02 import models  #引入数据库数据  标准库的放上面，第三方库的放下面，引入自己项目系统中的文件放最下面
from django.urls import reverse
# Create your views here.
# 1、反向解析
# 2、for循环
# 3、静态文件
# 4、urls 问什么加name = show_books / add_books   避免路径写死
# 5、过滤器
# 6、{% csrf_token %} 用法
# 7、from Django.urls import reverse
# 8、提交数据 用from表单    action 指定路径
def show_books(request):
    if request.method == 'GET':
        #在前端显示内容
        all_books_objs = models.Book.objects.all()  #all_books_objs 所有的model对象
        return render(request,'show_books.html',{'all_books_objs':all_books_objs})  #render 字符串替换，展示所有


def add_books(request):
    if request.method == 'GET':

        return render(request,'add_books.html')
    else:
        # name = request.POST.get('name')
        # price = request.POST.get('price')
        # date = request.POST.get('date')
        # publisher = request.POST.get('publisher')



        # 向后端传入保存数据，是一种方法，还有另一种，关键字传参可以打散
        # models.Book.objects.create(
        #     name=name,
        #     price=price,
        #     date=date,
        #     publisher=publisher
        # )

        #打散传数据
        book_info_dict = request.POST.dict()
        # print(book_info_dict)
        del book_info_dict['csrfmiddlewaretoken']
        models.Book.objects.create(**book_info_dict)

        #创建完数据返回show_books
        return redirect(reverse('show_books'))

def del_books(request,n):
    models.Book.objects.filter(pk=n).delete()
    return redirect('show_books')

def edit_books(request,n):
    old_obj = models.Book.objects.get(pk=n)
    return render(request,'edit_books.html',{'old_obj':old_obj})


def register(request):
    if request.method == 'GET':
        return  redirect('register')
    #注册成功返回登录界面
    else:
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        models.User.objects.create(
            username=username,
            password=password
        )
        return redirect('login')

def login(request):
    if request.method =='GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        # 问题一：如何匹配数据库里的用户名密码
        # if username == models.User.objects.get(username) and password == models.User.objects.get(password):
        # if username == 'li' and password =='666':
        #     ret = models.User.objects.filter(username='li').values()
        # for i in ret:
        #     if username == i['username'] and password == i['password']:
        #         return redirect('show_books')

        ret = models.User.objects.values()
        print(ret)
        for i in ret:
            if username == i['username'] and password == i['password']:
                return redirect('show_books')
            else:
                return HttpResponse('用户或用户名错误')