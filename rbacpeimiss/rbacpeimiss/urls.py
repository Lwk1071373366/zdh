"""rbacpeimiss URL Configuration

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
from rbacapp01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login,name='login'),
    url(r'^order/$', views.order),
    url(r'^order/add/', views.addorder),
    url(r'^order/edit/(\d+)/', views.editorder),
    url(r'^order/del/(\d+)/', views.delorder),
    url(r'^customer/$', views.customer),
    url(r'^customer/add/', views.addcustomer),
    url(r'^customer/edit/(\d+)', views.editcustomer),
    url(r'^customer/del/(\d+)', views.delcustomer),

]
