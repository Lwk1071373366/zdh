"""day58 URL Configuration

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
from zuoye02 import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^show_books',views.show_books,name='show_books'),
    url(r'^add_books',views.add_books,name='add_books'),
    url(r'^del_books/(\d+)',views.del_books,name='del_books'),
    url(r'^edit_books/(\d+)',views.edit_books,name='edit_books'),
    url(r'^login/',views.login,name='login'),
    url(r'^register',views.register,name='register')
]
