from rbac import models

def initial_session(request,user_obj):
    permissions = models.Permission.objects.filter(role__user__name=user_obj).values('title','url','pk','menu_id','menu_title','menu_icon','menu_pk','pid').distinct()
    #权限注入
    permission_list = []
    permission_menu_dict = {}
    for item in permissions:
        permission_list.append({
            'pk':item['pk'],
            'url':item['url'],
            'pid':item['pid']
        })
        if item['menu_id']:
            if item['menu_id'] in permission_menu_dict:
                permission_menu_dict[item['menu_pk']]['children'].append(
                    {'pk':item['pk'],'title':item['title'],'url':item['url']}
                )
            else:
                permission_menu_dict[item['menu_pk']]={
                    'title':item['title'],
                    'icon':item['icon'],
                    'children':[{
                        'pk':item['pk'],'title':item['title'],'url':item['url']
                    }]
                }
    request.session['permission_list'] = permission_list
    # print(permission_list)
    #['/customer/list/', '/customer/add/', '/customer/edit/(?P<cid>\\d+)/', '/customer/del/(?P<cid>\\d+)/',
    # '/payment/list/', '/payment/add/', '/payment/edit/(?P<pid>\\d+)/', '/payment/del/(?P<pid>\\d+)/']

    request.session['permission_menu_dict'] = permission_menu_dict
    # print(permission_menu_list)
    #[{'title': '客户列表', 'url': '/customer/list/', 'icon': 'fa-connectdevelop'},
    # {'title': '缴费列表', 'url': '/payment/list/', 'icon': 'fa-code-fork'}]

    # request.session['user'] = user_obj.name
    # permission_list = [i.url for i in permissions]
    # request.session['permission_list'] = permission_list