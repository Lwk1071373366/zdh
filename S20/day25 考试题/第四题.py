'''
4、写装饰器，补全log中的内容，使用time模块实现下列结果：
blablabla
2019-04-02 20:28:32 func被调用了
提示：
func.__name__可以获得函数名

import time
def log(func):
    pass


@log
def func():
    print('blablabla')

func()

'''
import time
def log(func):
   def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        print('%s %s被调用了'%(time.strftime('%Y-%m-%d %X'),func.__name__))
        return ret
   return inner

@log
def func():
    print('blablabla')
    print('666啊')
func()