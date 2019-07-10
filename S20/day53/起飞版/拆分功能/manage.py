from wsgiref.simple_server import make_server
from urls import urlpatterns


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    for urlpattern in urlpatterns:
        if path == urlpattern[0]:
            data =urlpattern[1](environ)
            break
    else:
        data = b'sorry 404!,not found the page'
    return [data]

httpd = make_server('127.0.0.1', 9001, application)
httpd.serve_forever()