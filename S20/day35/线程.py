# from threading import Thread,enumerate
#
# def func():
#     print('in son thread')
# Thread(target=func).start()
# print(enumerate())



# import time
# from threading import Thread
#
# def daemon_func():
#     while True:
#         time.sleep(1)
#         print('守护线程')
# def son_func():
#     print('start son')
#     time.sleep(5)
#     print('end son')
# t = Thread(target=daemon_func)
# t.daemon = True
# t.start()
# Thread(target=son_func).start()
# time.sleep(3)
# print('主线程结束')




# import time
# from threading import Thread
#
# def daemon_func():
#     while True:
#         time.sleep(0.5)
#         print('守护线程')
#
# def son_func():
#     print('start son')
#     time.sleep(5)
#     print('end son')
#
# t = Thread(target=daemon_func)
# t.daemon = True
# t.start()
# Thread(target=son_func).start()
# time.sleep(3)
# print('主线程结束')
#
#
# import time
# from threading import Thread
# def daemon_func():
#     while True:
#         time.sleep(1)
#         print('守护线程')
# def son_func():
#     print('start son')
#     time.sleep(5)
#     print('end son')
# t = Thread(target=daemon_func)
# t.daemon = True
# t.start()
# Thread(target=son_func).start()
# time.sleep(3)
# print('主线程结束')



from threading import Thread
from queue import Queue
import time,random

def producer(q,name):
    for i in range(10):
        time.sleep(random.random())
        food = '饭%s'%i
        print('%s做好了%s'%(name,food))
        q.put(food)
def consumer(q,name):
    while True:
        global food
        food = q.get()
        if not food:break
        time.sleep(random.uniform(1,2))
        print('%s吃了%s'%(name,food))


















