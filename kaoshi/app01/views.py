from django.shortcuts import render,redirect,HttpResponse,reverse
from app01 import models
# Create your views here.


def show_books(request):

    if request.method == 'GET':
        all_books_objs = models.Book.objects.all()
        print(all_books_objs)
        return render(request, 'show_books.html', {'all_books_objs': all_books_objs})


def add_books(request):
    if request.method == 'GET':

        return render(request,'add_books.html')
    else:
        book_info_dict = request.POST.dict()
        del book_info_dict['csrfmiddlewaretoken']
        models.Book.objects.create(**book_info_dict)

        return redirect(reverse('show_books'))

def del_books(request,n):
    models.Book.objects.filter(pk=n).delete()
    return redirect('show_books')

def edit_books(request,n):
    old_obj = models.Book.objects.get(pk=n)
    return render(request,'edit_books.html',{'old_obj':old_obj})