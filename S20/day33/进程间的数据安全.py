
# 进程间数据安全
from multiprocessing import Process,Manager,Lock

def func(dic,lock):
    with lock:
        dic['count'] -= 1

if __name__ == '__main__':
    lock = Lock()
    m = Manager()
    dic = m.dict({'count':100})
    p_l = []
    for i in range(100):
        p = Process(target=func,args=(dic,lock))
        p.start()
        p_l.append(p)
    for p in p_l:p.join()
    print(dic)
