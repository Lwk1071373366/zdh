from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def login(request):
    if request.method =='GET':
        data = time.time()
        data = time.localtime(data)
        data = time.strftime('%Y-%m-%d %X',data)
        return render(request,'login.html',{'time':data})
    else:
        username =  request.POST.get('username')
        password = request.POST.get('pwd')
        if username =='chao' and password =='666':
            return render(request,'shouye.html')
        else:
            return HttpResponse('穷B一个')
