from django.conf.urls import url
from web.views import customer
from web.views import payment
from web.views import account

urlpatterns = [

    #客户信息管理
    url(r'^customer/list/$', customer.customer_list,name='customer'),
    url(r'^customer/add/$', customer.customer_add),
    url(r'^customer/edit/(?P<cid>\d+)/$', customer.customer_edit),
    url(r'^customer/del/(?P<cid>\d+)/$', customer.customer_del),

    #缴费管理
    url(r'^payment/list/$', payment.payment_list),
    url(r'^payment/add/$', payment.payment_add),
    url(r'^payment/edit/(?P<pid>\d+)/$', payment.payment_edit),
    url(r'^payment/del/(?P<pid>\d+)/$', payment.payment_del),

    url(r'^login/$',account.login,name='login')
]
