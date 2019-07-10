from django import template

register = template.Library()

from django.conf import settings
import re


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    # menu_list = request.session.get('permisson_menu_list')
    menu_dict= request.session.get('permisson_menu_dict')
    for key,item in menu_dict.items():
        # url =
        item['class'] = 'hide'

        for child in item['children']:
            # {
            #     'title': '客户列表1',
            #     'url': '/customer/list/'
            #
            #     'class':'active'
            # }
            # {
            #     'title': '客户列表2',
            #     'url': '/customer/list/'
            # }
            if re.match('^{}$'.format(child['url']), request.path):
                item['class'] = ''
                child['class'] = 'active'
                break


    return {"menu_dict": menu_dict}
