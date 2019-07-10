# 原版
# from django import template
#
# register = template.Library()
#
# from django.conf import settings
# import re
#
#
# @register.inclusion_tag('rbac/menu.html')
# def menu(request):
#     menu_list = request.session.get('permission_menu_list')
#     for item in menu_list:
#         url = item['url']
#         if re.match('^{}$'.format(url), request.path_info):
#             item['class'] = 'active'
#             break
#
#     return {"menu_list": menu_list}

import re
from django import template
from django.urls import reverse
register = template.Library()

from django.conf import settings

@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_dict = request.session.get('permission_menu_dict')
    for key,item in menu_dict.items():
        item['class'] = 'hide'
        for child in item['children']:
            if request.show_id == child['pk']:
                item['class'] = ''
                child['class'] = 'active'
                break
    return {'menu_dict':menu_dict}
@register.filter
def haspermission(base_url,request):
    for item in request.session['permission_list']:
        reg = '^%s$'%item['url']
        ret = re.search(reg,base_url)
        if ret :
            return True
    return False