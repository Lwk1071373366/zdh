from django.shortcuts import render,HttpResponse,redirect
from book import models
from django.urls import reverse
# Create your views here.



def show_book(request):
    if request.method == 'GET':
        all_books = models.book.objects.all()

    return render(request,'show_book.html',{'all_books':all_books})

def add_book(request):
    if request.method == 'GET':
        return render(request,'add_book.html')
    else:
        name = request.POST.get('name')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publisher = request.POST.get('publisher')

        models.book.objects.create(
            name=name,price=price,
            date=date,publisher=publisher
        )

        return redirect('show_book')

def edit_book(request,n):
    old_book =models.book.objects.get(pk=n)
    return render(request,'edit_book.html',{'old_book':old_book})

def del_book(request,n):
    models.book.objects.filter(pk=n).delete()
    return redirect('show_book')