import time
from wsgiref.simple_server import make_server

def app(environ,start_response):
    start_response('200 OK', [('Content-Type', 'text/html'), ('k1', 'v1')])
    path = environ['PATH_INFO']
    for urlpattern in urlpatterns:
        if urlpattern[0] == path:
            ret = urlpattern[1]()
            return ret

def html():
    with open('01进阶版.html', 'rb') as f:
        date = f.read()
    return [date]

def home():
    current_time = str(time.time())                #动态效果，用时间模拟
    with open('home.html', 'r',encoding='utf-8') as f:
        data = f.read()
        data = data.replace('双击666',current_time).encode('utf-8')
    return [data]
urlpatterns=[
    ('/',html),
    ('/home.html',home)
]
httpd = make_server('127.0.0.1',9001,app)
httpd.serve_forever()
