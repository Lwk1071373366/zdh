from django.shortcuts import render,HttpResponse,redirect
from zuoye01 import models
# Create your views here.


def look_books(request):

    return render(request,'look_books.html')
    # return redirect('/add_books/')


def add_books(request):
    # method = request.method
    # if method == 'POST':
    #     return render(request,'look_books.html')
    # else:
    #     return redirect('/add_books/')

    return render(request,'add_books.html')


# def compile(request):
#
#     return render(request,'compile.html')
#

obj_list = []
for i in range(1,10):
    obj = models.look_book(
        书籍名称='python',
        书籍价格='123',
        出版时间='2012-12-12',
        出版社='人民出版社'
    )
    obj_list.append(obj)
models.look_book.objects.bulk_create(obj_list)


# 提交 根据post 获取到值  拿到值添加到数据库
def query(request):
    all_obj = models.look_book.objects.all()
    print(all_obj)
    return HttpResponse('ok')