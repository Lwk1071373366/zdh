import re
from django.shortcuts import HttpResponse,render,redirect
from django.utils.deprecation import MiddlewareMixin

class PermissonMiddleWare(MiddlewareMixin):

    def process_request(self,request):
        #白名单放行
        for i in ['/login/','/admin/.*']:
            ret = re.search(i,request.path)
            if ret:
                return None

        #登录认证
        user = request.session.get('user')
        if not user:
            return redirect('login')

        #权限认证
        for item in request.session['permisson_list']:
            reg = '^%s$'%item
            ret = re.search(reg,request.path)
            if ret:
                return None
        else:
            return HttpResponse('不好意思,权限不够!!无权访问!')







