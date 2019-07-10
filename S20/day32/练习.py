# import time
# import random
# from multiprocessing import Process,Queue
#
# def producer(q):
#     for i in range(10):
#         time.sleep(random.random())
#         food = '饭%s'%i
#         print('%s做好了%s'%('taibai',food))
#         q.put(food)
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if not food:break
#         time.sleep(random.uniform(1,2))
#         print('%s吃了%s'%(name,food))
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer,args=(q,))
#     p1.start()
#     c1 = Process(target=consumer,args=(q,'alex'))
#     c1.start()
#     c2 = Process(target=consumer,args=(q,'wusir'))
#     c2.start()
#     p1.join()
#     q.put(None)
#     q.put(None)

# import time
# import random
# from multiprocessing import Process,Queue
#
# def producer(q):
#     for i in range(10):
#         time.sleep(random.random())
#         food = '饭%s'%i
#         print('%s做好了%s'%('taibai',food))
#         q.put(food)
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if not food:break
#         time.sleep(random.uniform(1,2))
#         print('%s吃了%s'%(name,food))
# if __name__ =='__main__':
#     q = Queue()
#     p1 = Process(target=producer,args=(q,))
#     p1.start()
#     c1 = Process(target=consumer,args=(q,'alex'))
#     c1.start()
#     c2 = Process(target=consumer,args=(q,'wusir'))
#     c2.start()
#     p1.join()
#     q.put(None)
#     q.put(None)

import time
import random
from multiprocessing import Process,Queue

def producer(q,name):
    for i in range(10):
        time.sleep(random.random())
        food = '饭%s'%i
        print('%s做好了%s'%(name,food))
        q.put(food)
def consumer(q,name):
    while True:
        food =q.get()
        if not food:break
        time.sleep(random.uniform(1,2))
        print('%s吃了%s'%(name,food))
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,'太白'))
    p1.start()
    p2 = Process(target=producer,args=(q,'宝元'))
    p2.start()
    c1 = Process(target=consumer,args=(q,'alex'))
    c1.start()
    c2 = Process(target=consumer,args=(q,'wusir'))
    c2.start()
    c3 = Process(target=consumer,args=(q,'小黑'))
    c3.start()
    c4 = Process(target=consumer,args=(q,'小白'))
    c4.start()
    p1.join()
    q.put(None)
    q.put(None)
    q.put(None)
    q.put(None)
#

# import json
# import time
# from multiprocessing import Process,Lock
#
# def search_ticket(name):
#     with open('ticket',encoding='utf-8')as f :
#         dic = json.load(f)
#         print('%s查询余票%s'%(name,dic['count']))
# def buy_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#     time.sleep(2)
#     if dic['count'] >= 1:
#         print('%s买到票了'%name)
#         dic['count'] -= 1
#         time.sleep(2)
#         with open('ticket',mode='w',encoding='utf-8') as f :
#             json.dump(dic,f)
#     else:
#         print('余票为0,%s没买到票'%name)
# def use(name,lock):
#     search_ticket(name)
#     print('%s在等待'%name)
#     with lock:
#         print('%s开始执行了'%name)
#         buy_ticket(name)
# if __name__ == '__main__':
#     lock = Lock()
#     l = ['alex','wusir','taibai']
#     for name in l :
#         Process(target=use,args=(name,lock)).start()


# import json
# import time
# from multiprocessing import Process,Lock
#
# def search_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#         print('%s查询余票%s'%(name,dic['count']))
# def buy_ticket(name):
#     with open('ticket',encoding='uff-8') as f :
#         dic = json.load(f)
#     time.sleep(2)
#     if dic['count'] >= 1:
#         print('%s买到票了'%name)
#         dic['count'] -= 1
#         time.sleep(2)
#         with open('ticlet',mode='w',encoding='utf-8') as f :
#             json.dump(dic,f)
#     else:
#         print('余票为0,%s没买到票'%name)
# def use(name,lock):
#     search_ticket(name)
#     print('%s在等待'%name)
#     with lock:
#         print('%s在等待'%name)
#         with lock:
#             print('%s开始执行了'%name)
#             buy_ticket(name)
# if __name__ == '__main__':
#     lock = Lock()
#     l = ['alex','wusir','taibai']
#     for name in l :
#         Process(target=use,args=(name,lock)).start()

# import json
# import time
# from multiprocessing import Process,Lock
# def search_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#         print('%s查询余票%s'%(name,dic['count']))
# def buy_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#     time.sleep(2)
#     if dic['count'] >= 1:
#         print('%s买到票了'%name)
#         dic['count'] -= 1
#         time.sleep(2)
#         with open('ticket',mode='w',encoding='utf-8') as f :
#             json.dump(dic,f)
#     else:
#         print('余票为0，%s没买到票'%name)
# def use(name,lock):
#     search_ticket(name)
#     print('%s在等待'%name)
#     with lock:
#         print('%s开始执行了'%name)
#         buy_ticket(name)
# if __name__ =='__main__':
#     lock = Lock()
#     l = ['alex','wusir']
#     for name in l :
#         Process(target=use,args=(name,lock)).start()

# import json
# import time
# from multiprocessing import Process,Lock
#
# def search_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#         print('%s查询余票%s'%(name,dic['count']))
# def buy_ticket(name):
#     with open('ticket',encoding='utf-8') as f :
#         dic = json.load(f)
#     time.sleep(2)
#     if dic['count'] >= 1:
#         print('%s买到票了'%name)
#         dic['count'] -= 1
#         time.sleep(2)
#         with open('ticket',mode='w',encoding='utf-8') as f :
#             json.dump(dic,f)
#     else:
#         print('余票为0，%s没有买到票'%name)
# def use(name,lock):
#     search_ticket(name)
#     print('%s在等待'%name)
#     with lock:
#         print('%s开始执行了'%name)
#         buy_ticket(name)
# if __name__ =='__main__':
#     lock = Lock()
#     l = ['alex','taibai']
#     for name in l :
#         Process(target=use,args=(name,lock)).start()









