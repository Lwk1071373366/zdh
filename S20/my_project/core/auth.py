import hashlib
from core.log import log
from conf.settings import userinfo
class Authentic(object):
    def __init__(self, usr, pwd):
        self.usr = usr
        self.pwd = pwd

    def get_md5(self):
        md5 = hashlib.md5(self.usr.encode('utf-8'))
        md5.update(self.pwd.encode('utf-8'))
        return md5.hexdigest()

    def login(self):
        with open(userinfo, encoding='utf-8') as f:
            for line in f:
                username, password, ident = line.strip().split('|')
                if self.usr == username and self.get_md5() == password:
                    return {'result': True, 'identify': ident, 'username': self.usr}
            else:
                return {'result': False}

    @classmethod
    def auth(cls):
        opt_lst1 = ['登录', '退出']
        while True:
            for index, opt in enumerate(opt_lst1, 1):
                print(index, opt)
            num = int(input('请输入你要做的操作 :'))
            if num == 1:
                usr = input('username :')
                pwd = input('password :')
                obj = cls(usr, pwd)
                ret = obj.login()
                if ret['result']:
                    print('登录成功')
                    log.logger.info('%s用户%s登录成功' % (ret['identify'], ret['username']))
                    return ret
                else:
                    print('登录失败')
            elif num == 2:
                exit()