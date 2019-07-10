import re
from django.shortcuts import HttpResponse,render,redirect
from django.utils.deprecation import MiddlewareMixin

class PermissionMiddleware(MiddlewareMixin):
    def process_request(self,request):
        for i in ['/login/','/admin/']:
            ret = re.search(i,request.path)
            if ret:
                return None
        user = request.session.get('user')
        if not user:
            return redirect('login')

        for item in request.session['permisson_list']:
            reg = '^%s$'%item
            ret = re.search(reg,request.path)
            if ret:
                return None
        else:
            return HttpResponse('不好意思没有权限')