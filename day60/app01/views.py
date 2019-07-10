from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Max
# Create your views here.


from app01 import models

def query(request):
    # book_obj=models.Book.objects.get(id=4)  #书籍id为4的 对应的出版社所在的城市
    # print(book_obj.publish.city)

    # author_obj = models.Author.objects.get(name='唐家三少') #找到唐家三少的地址
    # print(author_obj.ad.addr)
    # addr_obj = models.AuthorDetail.objects.get(addr='澳门')  #看谁在澳门
    # print(addr_obj.author.name)
    # author_obj = models.Author.objects.get(name='我吃西红柿')
    # print(author_obj.book_set.all())

    # ****************基于双下划线的查询****************************
    # 1、书籍id为4的 对应的出版社所在的城市
    # city_obj=models.Book.objects.filter(id=4).values('publishs__city')
    # print(city_obj)
    # city_obj = models.Publish.objects.filter(book__id=4).values('city')
    # print(city_obj)
    # 2、辰东是哪个城市的
    #正向
    # ret = models.Author.objects.filter(name='辰东').values('ad__addr')
    # print(ret)<QuerySet [{'ad__addr': '台湾'}]>
    #反向
    # ret = models.AuthorDetail.objects.filter(author__name='辰东').values('addr')
    # print(ret)<QuerySet [{'addr': '台湾'}]>
    # 3、斗罗大陆的作者是谁
    # ret = models.Book.objects.filter(title='斗罗大陆').values('authors__name')
    # print(ret)  #<QuerySet [{'authors__name': '唐家三少'}]>
    # ret = models.Author.objects.filter(book__title='斗破苍穹').values('name')
    # print(ret)  #<QuerySet [{'name': '辰东'}]>

    # 4、上海出版社出版的所有书籍的名称和对应的作者的名称
    # ret = models.Publish.objects.filter(name='上海出版社').values('book__title','book__authors__name')
    # print(ret) #<QuerySet [{'book__title': '斗破苍穹', 'book__authors__name': '辰东'},
                #  {'book__title': '星辰变', 'book__authors__name': '我吃西红柿'}]>
    # ret = models.Book.objects.filter(publishs__name='上海出版社').values('title','authors__name')
    # print(ret) #<QuerySet [{'title': '斗破苍穹', 'authors__name': '辰东'},
    #             # {'title': '星辰变', 'authors__name': '我吃西红柿'}]>
    # ret = models.Author.objects.filter(book__publishs__name='上海出版社').values('book__title','name')
    # print(ret) #<QuerySet [{'book__title': '斗破苍穹', 'name': '辰东'},
                # {'book__title': '星辰变', 'name': '我吃西红柿'}]>
    # 5、电话号码大于110的作者出版过的所有书籍名称及出版社名称
    # ret = models.AuthorDetail.objects.filter(telephone__gt=110).values('author__book__title','author__book__publishs__name')
    # print(ret)  #<QuerySet [{'author__book__title': '神印王座', 'author__book__publishs__name': '南京出版社'},
                #  {'author__book__title': '神墓', 'author__book__publishs__name': '南京出版社'},
                # {'author__book__title': '星辰变', 'author__book__publishs__name': '上海出版社'},
                #  {'author__book__title': '斗破苍穹', 'author__book__publishs__name': '上海出版社'}]>

    # 6、每个作者出版的所有书的最高价格的那本书的名称
    ret = models.Author.objects.values('book__title').annotate(m=max('book__price'))

    return HttpResponse('OK啦~~~')


