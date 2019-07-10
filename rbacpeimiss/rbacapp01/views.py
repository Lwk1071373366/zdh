from django.shortcuts import render,HttpResponse,redirect
from rbacapp01 import models
# Create your views here.

from rbac.service.permission_input import initial_session
def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user_obj = models.User.objects.filter(name=user,pwd=pwd).first()
        if user_obj:
            initial_session(request,user_obj)
            return HttpResponse('登录成功')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')
def order(request):

    return HttpResponse('order进来了')
def addorder(request):

    return HttpResponse('addorder进来了')
def editorder(request,pk):

    return HttpResponse('editorder进来了')
def delorder(request,pk):

    return HttpResponse('delorder进来了')
def customer(request):

    return HttpResponse('customer进来了')
def addcustomer(request):

    return HttpResponse('addcustomer进来了')
def editcustomer(request,pk):

    return HttpResponse('editcustomer进来了')
def delcustomer(request,pk):

    return HttpResponse('delcustomer进来了')
