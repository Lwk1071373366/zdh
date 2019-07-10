# import time
# import random
# from multiprocessing import Process,Queue
#
# def producer(q,name):
#     for i in range(10):
#         time.sleep(random.random())
#         food = '饭%s'%i
#         print('%s做了%s'%(name,food))
#         q.put(food)
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if not food : break
#         time.sleep(random.uniform(1,2))
#         print('%s吃了%s'%(name,food))
# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer,args=(q,'A'))
#     p1.start()
#     p2 = Process(target=producer,args=(q,'B'))
#     p2.start()
#     c1 = Process(target=consumer,args=(q,'C'))
#     c1.start()
#     c2 = Process(target=consumer,args=(q,'D'))
#     c2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
























