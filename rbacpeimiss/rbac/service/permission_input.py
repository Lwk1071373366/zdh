from rbacapp01 import models

def initial_session(request,user_obj):
    #权限注入
    request.session['user'] = user_obj.name
    permissions = models.Permisson.objects.filter(role__user__name=user_obj.name).distinct()
    permission_list = [i.url for i in permissions]
    request.session['permisson_list'] = permission_list