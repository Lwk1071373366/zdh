# lst = [1,2,3,4,5,6,7,8,9,10]
# 按照顺序把列表中的每一个元素都计算一个平方
# 使用多线程的方式
# 并将结果按顺序返回


# import time
# import random
# from threading import Thread,currentThread
# dic = {}
# def func(i):
#     t = currentThread()
#     print(t)
#     time.sleep(random.random())
#     dic[t.ident] = i**2
# t_lst = []
# for i in range(1,11):
#     t = Thread(target=func,args=(i,))
#     t.start()
#     t_lst.append(t)
# for t in t_lst:
#     t.join()
#     print(dic[t.ident])


# import time
# import random
# from threading import Thread,currentThread
# dic = {}
# def func(i):
#     t = currentThread()
#     time.sleep(random.random())
#     dic[t.ident] = i**2
# t_lst = []
# for i in range(1,11):
#     t = Thread(target=func,args=(i,))
#     t.start()
#     t_lst.append(t)
# for t in t_lst:
#     t.join()
#     print(dic[t.ident])
#

# import time
# from multiprocessing import Process
# from threading import Thread
#
# def func(a):
#     a += 1
# if __name__ == '__main__':
#     start = time.time()
#     t_l = []
#     for i in range(100):
#         t = Thread(target=func,args=(i,))
#         t.start()
#         t_l.append(t)
#     for t in t_l:
#         t.join()
#     print('t:',time.time()-start)
#
#     start = time.time()
#     p_l = []
#     for i in range(100):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('p:',time.time()-start)

# from dis import dis
# def func():
#     a = []
#     a.append(1)
# dis(func)



#多个线程间共享全局变量

# from threading import Thread
#
# tn = 0
# def func():
#     global tn
#     tn += 1
# t_l = []
# for i in range(100):
#     t = Thread(target=func)
#     t.start()
#     t_l.append(t)
# for t in t_l:t.join()
# print(tn)

# import os
# import time
# from threading import Thread
#
# def func():
#     time.sleep(1)
#     print('in func',os.getpid())
# print('in main',os.getpid())
# for i in range(20):
#     Thread(target=func,).start()
#
#
# import os
# import time
# from threading import Thread
#
# def func(i):
#     time.sleep(1)
#     print('in func',i,os.getpid())
# print('in main',os.getpid())
#
# for i in range(50):
#     Thread(target=func,args=(i,)).start()




# import time
# import random
# from threading import Thread
#
# def func():
#     time.sleep(random.random())
#     t1 = Thread(target=func)
#     t1.start()
#     t2 = Thread(target=func)
#     t2.start()
#     t1.join()
#     t2.join()
#     t3 = Thread(target=func)
#     t3.start()
#     t4 = Thread(target=func)
#     t4.start()
#     t5 = Thread(target=func)
#     t5.start()
#     t3.join()
#     t4.join()
#     t5.join()
#     print('结束')




import time
from threading import Thread

def func(name):
    print('t%s'%name)
    time.sleep(1)

if __name__ == '__main__':
    l1=[]
    l2=[]
    for i in range(1,3):
        t = Thread(target=func,args=(i,))
        t.start()
        l1.append(t)
    for i in l1:
        i.join()
    for i in range(3,6):
        t = Thread(target=func,args=(i,))
        t.start()
        l2.append(t)
    for i in l2:
        i.join()
    print('结束')





