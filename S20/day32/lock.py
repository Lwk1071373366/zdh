import time
import random
from multiprocessing import Process,Queue

def producer(q):
    for i in range(10):
        time.sleep(random.random())
        food = '饭%s'%i
        print('%s做好了%s'%('taibai',food))
        q.put(food)
def consumer(q,name):
    while True:
        food = q.get()
        if not food : break
        time.sleep(random.uniform(1,2))
        print('%s吃了%s'%(name,food))
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,))
    p1.start()
    c1 = Process(target=consumer,args=(q,'alex'))
    c1.start()
    c2 = Process(target=consumer,args=(q,'wusir'))
    c2.start()
    p1.join()
    q.put(None)
    q.put(None)