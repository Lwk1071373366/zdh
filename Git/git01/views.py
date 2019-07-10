from django.shortcuts import render,redirect,HttpResponse
from git01 import form
from git01 import models
from django.http import JsonResponse
# Create your views here.




def register(request):
    if request.method == 'GET':
        form_obj = form.UserForm()
        return  render(request,'register.html',{'form_obj':form_obj})
    else:
        form_obj = form.UserForm(request.POST)
        if form_obj.is_valid():
            # print(form_obj.cleaned_data) #将没有用的字段删除
            data=form_obj.cleaned_data
            data.pop('r_password')
            models.UserInfo.objects.create_user(**data) #create_user密文创建
            return redirect('login')
        else:
            return render(request,'register.html',{'form_obj':form_obj})
#登录
def login(request):
    response_msg = {'code':None,'msg':None}
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        #首先验证验证码是否正确
        if valid_bode.upper() == request.session.get('valid_str').upper():
            user_obj = auth.authenticate(username=username,password=password)
            if user_obj:
                auth.login(request,user_obj)
                response_msg['code']=1000
                response_msg['msg'] = '登录成功'
                # return redirect('index')
            else:
                response_msg['code'] = 1002
                response_msg['msg'] ='用户名或者密码错误'
        else:
            response_msg['code'] = 1001
            response_msg['msg'] = '验证码输入错误'
        return JsonResponse(response_msg)
