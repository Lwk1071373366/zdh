"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from crm01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #首页
    url(r'^index/',views.index,name='index'),
    #注册
    url(r'^register/',views.register,name='register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #验证码
    url(r'^get_valid_img/',views.get_valid_img,name='get_valid_img'),
    #注销
    url(r'^logout/',views.logout,name='logout'),
    #展示公户信息
    url(r'^customers/list/', views.CustomerView.as_view(), name='customers'),
    #展示私户信息
    url(r'^mycustomers/', views.MyCustomerView.as_view(), name='mycustomers'),
    #展示客户跟进记录
    url(r'^Follow_Up_Records/$', views.Follow_Up_Records.as_view(), name='Follow_Up_Records'),
    #公户页面显示跟进记录
    url(r'^Follow_Up_Records/(\d+)$', views.Follow_Up_Records.as_view(), name='DanGe_Follow_Up_Records'),
    #展示客户跟进 添加记录
    url(r'^Follow_Up_Records/add/', views.AddFollow_Up_Records.as_view(), name='addFollow_Up_Records'),
    #编辑跟进记录
    url(r'^Follow_Up_Records/edit/(\d+)', views.EditFollow_Up_Records.as_view(), name='editFollow'),

    #测试分页
    # url(r'^test/', views.test, name='test'),
    #添加信息
    url(r'^customers/add/',views.AddCustomer.as_view(),name='addcustomer'),
    #编辑信息
    url(r'^customers/edit/(\d+)/',views.Editcustomer.as_view(),name='editcustomer'),
    #删除信息
    url(r'^customers/del/(\d+)/',views.Delcustomer.as_view(),name='delcustomer'),

]
