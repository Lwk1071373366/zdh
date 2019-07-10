from urllib.parse import parse_qs
import webauth
def login(environ):
    with open('login.html', 'rb') as f:
        data = f.read()
    return data
def auth(environ):
    # if environ.get("REQUEST_METHOD") == "POST":
    #     try:
    #         request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    #     except (ValueError):
    #         request_body_size = 0
    #     request_data = environ['wsgi.input'].read(request_body_size)
    #     print('>>>>>', request_data)
    #     print('?????', environ['QUERY_STRING'])
    #     re_data = parse_qs(request_data)
    #     print('拆解后的数据', re_data)
    #     pass
    if environ.get("REQUEST_METHOD") == "GET":
        print('?????', environ['QUERY_STRING'])
        request_data = environ['QUERY_STRING']

        re_data = parse_qs(request_data)
        print('拆解后的数据', re_data)
        username = re_data['username'][0]
        password = re_data['password'][0]
        print(username, password)
        status = webauth.auth(username, password)
        if status:
            with open('websuccess.html', 'rb') as f:
                data = f.read()
        else:
            data = b'auth error'
        return data