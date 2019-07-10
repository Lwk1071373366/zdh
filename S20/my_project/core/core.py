import sys

from core.log import log
from core.auth import Authentic
from core.user import Student
from core.user import Manager

def entry_point():
    ret = Authentic.auth()
    if ret['result']:
        if hasattr(sys.modules[__name__], ret['identify']):
            cls = getattr(sys.modules[__name__], ret['identify'])
            obj = cls.init(ret['username'])
            while True:
                for index, opt in enumerate(cls.opt_lst, 1):
                    print(index, opt[0])
                try:
                    num = int(input('请选择您要操作的序号 :'))
                    if hasattr(obj, cls.opt_lst[num - 1][1]):
                        getattr(obj, cls.opt_lst[num - 1][1])()
                except ValueError:
                    log.logger.warning('选择序号输入的内容有误')