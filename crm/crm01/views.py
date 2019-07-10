import os
import random
from crm import settings
from django.shortcuts import render,HttpResponse,redirect
from crm01 import form
from crm01 import models
from django.views import View
from PIL import Image, ImageDraw, ImageFont
from django.http import JsonResponse
from  django.urls import reverse
from django.contrib import auth
from crm01 import page
from django.contrib.auth.decorators import login_required
from django.db.models import Q
@login_required   #认证装饰器
def index(request):
    return render(request,'index.html')

#注册
def register(request):
    if request.method == 'GET':
        form_obj = form.UserForm()
        return  render(request,'register.html',{'form_obj':form_obj})
    else:
        form_obj = form.UserForm(request.POST)
        if form_obj.is_valid():
            # print(form_obj.cleaned_data) #将没有用的字段删除
            data=form_obj.cleaned_data
            data.pop('r_password')
            models.UserInfo.objects.create_user(**data) #create_user密文创建
            return redirect('login')
        else:
            return render(request,'register.html',{'form_obj':form_obj})
#登录
def login(request):
    response_msg = {'code':None,'msg':None}
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_bode = request.POST.get('valid_code')
        #首先验证验证码是否正确
        if valid_bode.upper() == request.session.get('valid_str').upper():
            user_obj = auth.authenticate(username=username,password=password)
            if user_obj:
                auth.login(request,user_obj)
                response_msg['code']=1000
                response_msg['msg'] = '登录成功'
                # return redirect('index')
            else:
                response_msg['code'] = 1002
                response_msg['msg'] ='用户名或者密码错误'
        else:
            response_msg['code'] = 1001
            response_msg['msg'] = '验证码输入错误'
        return JsonResponse(response_msg)
#注销
def logout(request):
    auth.logout(request)
    return redirect('login')

# def starter(request):
#     pass
#验证码
def get_valid_img(request):

    def get_random_color():
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    img_obj = Image.new('RGB', (200, 34), get_random_color()) #图片对象
    draw_obj = ImageDraw.Draw(img_obj)  #通过图片对象生成一个画笔对象
    font_path = os.path.join(settings.BASE_DIR,'statics/font/NAUERT__.TTF') #获取字体,注意有些字体文件不能识别数字，所以如果数字显示不出来，就换个字体
    font_obj = ImageFont.truetype(font_path,16) #创建字体对象
    sum_str = ''  #这个数据就是用户需要输入的验证码的内容
    for i in range(6):
        a = random.choice([str(random.randint(0,9)), chr(random.randint(97,122)), chr(random.randint(65,90))])  #4  a  5  D  6  S
        sum_str += a
    print(sum_str)
    draw_obj.text((64,10),sum_str,fill=get_random_color(),font=font_obj) #通过画笔对象，添加文字

    width=200
    height=34
    # 添加噪线
    for i in range(5): #添加了5条线
        #一个坐标表示一个点，两个点就可以连成一条线
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw_obj.line((x1,y1,x2,y2),fill=get_random_color())
    # # 添加噪点
    for i in range(10):
        #这是添加点，50个点
        draw_obj.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        #下面是添加很小的弧线，看上去类似于一个点，50个小弧线
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw_obj.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color()) #x, y是弧线的起始点位置，x + 4, y + 4是弧线的结束点位置

    from io import BytesIO
    f = BytesIO()  #操作内存的把手
    img_obj.save(f,'png')  #
    data = f.getvalue()

    # 存这个验证码的方式1：赋值给全局变量的简单测试
    # global valid_str
    # valid_str = sum_str
    # 方式2：将验证码存在各用户自己的session中,session的应用其实还有很多
    request.session['valid_str'] = sum_str
    return HttpResponse(data)

#查看所有的公户信息信息
# def customers(request):
#     all_customers = models.Customer.objects.all()
#     return render(request,'customers.html',{'all_customers':all_customers})

#查看所有公户信息  ‘销售为空’
# def customers(request):
class CustomerView(View):#用CBV的方式做 公共客户信息展示及批量操作
    def get(self,request):
        wd = request.GET.get('wd','')
        condition = request.GET.get('condition','')

        all_customers = models.Customer.objects.filter(consultant__isnull=True)
        if wd:
            q = Q()
            q.children.append((condition,wd))
            all_customers = all_customers.filter(q)
        current_page_num = request.GET.get('page',1)
        per_page_counts = 10  # 每页显示10条
        page_number = 5  # 总共显示5个页码
        total_count = all_customers.count()
        page_obj = page.PageNation(request.path,current_page_num,request,total_count,per_page_counts,page_number)
        all_customers = all_customers.order_by('-pk')[page_obj.start_num:page_obj.end_num]
        ret_html = page_obj.page_html()
        return render(request,'customers.html',{'all_customers':all_customers,'ret_html':ret_html})
    def post(self,request):
        self.data = request.POST.getlist('selected_id')
        action = request.POST.get('action')
        if hasattr(self,action):
            func = getattr(self,action)
            if callable(func):
                ret = func(request)
                if ret:
                    return ret
                return redirect('customers')
            else:
                return HttpResponse('NO')
        else:
            return HttpResponse('NO')
    #批量删除
    def batch_del(self,request):
        models.Customer.objects.filter(pk__in=self.data).delete()
    #批量更新
    def batch_update(self,request):
        models.Customer.objects.filter(pk__in=self.data).update(name='大白')
    #批量公户转私户
    def batch_g_s(self,request):
        batch_customer = models.Customer.objects.filter(pk__in=self.data)
        res = []
        for i in batch_customer:
            if i.consultant:
                res.append(i)
            else:
                i.consultant =request.user
                i.save()
        if res:
            res_str = ','.join([(i.qq + ':'+i.name) for i in res])
            return HttpResponse(res_str+'信息被其他人选走')
        models.Customer.objects.filter(pk__in=self.data).update(consultant=request.user)

#查看当前登录的用户 负责的客户信息
# def mycustomers(request):
#     mycustomers = models.Customer.objects.filter(consultant=request.user)
#     return render(request,'mycustomers.html',{'mycustomers':mycustomers})
class MyCustomerView(View):#用CBV的方式做 我的客户信息展示及批量操作
    def get(self,request):
        wd = request.GET.get('wd','')
        condition = request.GET.get('condition','')

        all_my_customers = models.Customer.objects.filter(consultant=request.user)
        if wd:
            q = Q()
            q.children.append((condition,wd))
            all_my_customers = all_my_customers.filter(q)
        current_page_num = request.GET.get('page',1)
        per_page_counts = 10  # 每页显示10条
        page_number = 5  # 总共显示5个页码
        total_count = all_my_customers.count()
        page_obj = page.PageNation(request.path,current_page_num,request,total_count,per_page_counts,page_number)
        all_my_customers = all_my_customers.order_by('-pk')[page_obj.start_num:page_obj.end_num]
        ret_html = page_obj.page_html()
        return render(request,'mycustomers.html',{'all_my_customers':all_my_customers,'ret_html':ret_html})
    def post(self,request):
        self.data = request.POST.getlist('selected_id')
        action = request.POST.get('action')
        if hasattr(self,action):
            func = getattr(self,action)
            if callable(func):
                func(request)
                return redirect('mycustomers')
            else:
                return HttpResponse('NO')
        else:
            return HttpResponse('NO')

    # 批量删除
    def batch_del(self, request):
        models.Customer.objects.filter(pk__in=self.data).delete()

    # 批量更新
    def batch_update(self, request):
        models.Customer.objects.filter(pk__in=self.data).update(name='小白')

    # 批量私户转公户
    def batch_s_g(self, request):
        models.Customer.objects.filter(pk__in=self.data).update(consultant=None)

#客户跟进记录
class Follow_Up_Records(View):
    def get(self,request,pk=None):
        wd = request.GET.get('wd','')
        condition = request.GET.get('condition','')
        if pk:
            all_records = models.ConsultRecord.objects.filter(customer_id=pk)
        else:
            all_records = models.ConsultRecord.objects.filter(consultant=request.user)
        if wd:
            q = Q()
            q.children.append((condition,wd))
            all_records = all_records(q)
        current_page_num = request.GET.get('page',1)
        per_page_counts = 10
        page_number = 5
        total_count = all_records.count()
        page_obj = page.PageNation(request.path,current_page_num,request,per_page_counts,page_number,total_count)
        all_records = all_records.order_by('-pk')[page_obj.start_num:page_obj.end_num]
        ret_html = page_obj.page_html()
        return render(request, 'Follow_Up_Records.html', {'all_records':all_records, 'ret_html':ret_html})

    def post(self, request):
        self.data = request.POST.getlist('selected_id')
        action = request.POST.get('action')
        if hasattr(self, action):
            func = getattr(self, action)
            if callable(func):
                func(request)
                return redirect('Follow_Up_Records')
            else:
                return HttpResponse('NO')
        else:
            return HttpResponse('NO')

        # 批量删除

    def batch_del(self, request):
        models.Customer.objects.filter(pk__in=self.data).delete()

        # 批量更新跟进信息

    def batch_update(self, request):
        models.Customer.objects.filter(pk__in=self.data).update(name='小白')

class AddFollow_Up_Records(View):
    def get(self,request):
        form_obj = form.ConsultRecordModelForm(request)
        return render(request, 'addFollow_Up_Records.html', {'form_obj':form_obj})
    def post(self,request):
        form_obj = form.ConsultRecordModelForm(request,request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('Follow_Up_Records')
        else:
            return render(request, 'Follow_Up_Records.html', {'form_obj':form_obj})

class EditFollow_Up_Records(View):
    def get(self,request,pk):
        followobj = models.ConsultRecord.objects.filter(pk=pk).first() #.first() 拿对象
        form_obj = form.ConsultRecordModelForm(request,instance=followobj)
        return render(request, 'editFollow.html', {'form_obj':form_obj})
    def post(self,request,pk):
        followobj = models.ConsultRecord.objects.filter(pk=pk).first()
        form_obj = form.ConsultRecordModelForm(request,request.POST,instance=followobj)#QueryDict
        if form_obj.is_valid():
            form_obj.save()
            return redirect('Follow_Up_Records')
        else:
            return render(request, 'Follow_Up_Records.html', {'form_obj':form_obj})



# def test(request):
#     wd = request.GET.get('wd','')
#     condition = request.GET.get('condition','')
#     condition = condition + '__condition'
#     current_page_num = request.GET.get('page',1)
#     if wd:
#         # all_data = models.Customer.objects.filter(Q(qq__contains=wd) | Q(name__contains=wd))
#         q = Q()
#         q .connector='or'
#         q.children.append((condition,wd))
#         q.children.append(('qq_name_contains','王'))
#         all_data = models.Customer.objects.filter(q)
#     else:
#         all_data = models.Customer.objects.all()
#     per_page_counts = 10 #每页显示10条
#     page_number = 5  #总共显示5个页码
#     all_data = models.Customer.objects.all()
#     total_count = all_data.count()
#     # ret_html,start_num,end_num = page.pagenation(request.path, current_page_num,total_count,per_page_counts,page_number)
#     p_obj = page.PageNation(request.path, current_page_num,total_count,per_page_counts,page_number)
#     ret_html = p_obj.page_html()
#     all_data = models.Customer.objects.all()[p_obj.start_num:p_obj.end_num]
#     return render(request,'test.html',{'all_data':all_data,'ret_html':ret_html})

#增加
#通过modelform创建
class AddCustomer(View):
    def get(self,request):
        form_obj = form.CustomerModelForm()
        return render(request,'addcustomer.html',{'form_obj':form_obj})
    def post(self,request):
        form_obj = form.CustomerModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()  # 添加数据的时候，modelform实例化一个对象， 只有is_valid()通过验证，再调用save()就自动保存了
            return redirect('customers')
        else:
            return render(request,'addcustomer.html',{'form_obj':form_obj})

#  老师版
# class AddCustomer(View):
#     #获取添加页面
#     def get(self,request):
#         form_obj = form.CustomerModelForm()
#         return render(request,'addcustomer.html',{'form_obj':form_obj})
#     def post(self,request):
#         form_obj = form.CustomerModelForm(request.POST)
#         #{'qq':'11111','name':'xiaohei'}
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect('customers')
#         else:
#             return render(request,'addcustomer.html',{'form_obj':form_obj})

#编辑
class Editcustomer(View):
    def get(self,request,pk):
        custome_obj  = models.Customer.objects.filter(pk=pk).first()
        form_obj = form.CustomerModelForm(instance=custome_obj)
        return render(request,'editcustomer.html',{'form_obj':form_obj})
    def post(self,request,pk):
        custome_obj = models.Customer.objects.filter(pk=pk).first()
        form_obj = form.CustomerModelForm(request.POST,instance=custome_obj)
        if form_obj.is_valid():
            form_obj.save()  # 添加数据的时候，modelform实例化一个对象， 只有is_valid()通过验证，再调用save()就自动保存了
            return redirect('mycustomers')
        else:
            return render(request,'editcustomer.html',{'form_obj':form_obj})
#删除
class Delcustomer(View):
    def get(self,request,pk):
        models.Customer.objects.filter(pk=pk).delete()
        return redirect('customers')

