import time
# def func(s):
#     print(s)
#     print('这是主功能')
#     time.sleep(2)
# def warpper(f):
#     def inner(*args,**kwargs):
#         start_time=time.time()
#         f(*args,**kwargs)
#         end_time=time.time()
#         print('%s函数的运行时间是:%s'% (f.__name__,end_time-start_time))
#     return inner
# func=warpper(func)
# func(5)

def func(s):
    print(s)
    print('这是一个主功能')
    time.sleep(5)
def warpper(f):
    def inner(*args,**kwargs):
        start_time=time.time()
        f(*args,**kwargs)
        end_time=time.time()
        print('%s函数的运行时间是：%s' % (f.__name__,end_time-start_time))
    return inner
func=warpper(func)
func(6)
# def func(s):
#     print(s)
#     print('这是一个新功能')
#     time.sleep(5)
# def warpper(f):
#     def inner(*args):
#      start_time=time.time()
#      f(*args)
#      end_time=time.time()
#      print('%s函数的运行时间是：%s' % (f.__name__,end_time-start_time))
#     return inner
# func=warpper(func)
# func(66)
