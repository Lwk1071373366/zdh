from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac import models
from rbac.server.init_permission import init_permission
import copy
from rbac.service.permission_input import initial_session

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        
        user = models.User.objects.filter(name=username, password=pwd).first()
        
        if not user:
            err_msg = '用户名或密码错误'
            return render(request, 'login.html', {'err_msg': err_msg})

        # 将用户信息注入到session中
        request.session['user'] = user.name
        # 登录成功
        # 将权限信息写入到session
        # init_permission(request,user)
        initial_session(request,user)

        return redirect(reverse('customer'))

    return render(request, 'login.html')
