from django.shortcuts import render,HttpResponse,redirect
from Ajax import settings
# Create your views here.

def login(request):

    return render(request,'login.html')

def index(request):

    return HttpResponse('ok')

def upload(request):
    if request.method =='POST':
        file_obj = request.FILES.get('picture')   #文件对象
        # print(file_obj)
        # print(file_obj.name)
    # return HttpResponse('ok')
        file_name = file_obj.name
        import os
        file_path = os.path.join(settings.BASE_DIR,'statics',file_obj.name)
        with open(file_path,'wb') as f :
            # for date in file_obj:
            #     f.write(date)
            for chunk in file_obj.chunks():
                f.write(chunk)

        return HttpResponse('ok')

    else:
        return render(request,'upload.html')