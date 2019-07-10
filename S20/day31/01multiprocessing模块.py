# from   multiprocessing  import Process
# import time
# def func():
#     time.sleep(1)
#     print(0)
#
# if __name__ == '__main__':
#     Process(target=func).start()
#     Process(target=func).start()
#     Process(target=func).start()

# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,5))
#     print('已经给%s发送邮件了'%name)
# if __name__ =='__main__':
#     lst = ['alex','宝元','太白']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('所有的信息发送完毕')

# 使用multiprocess起一个最简单的子进程,执行查看子进程的进程id
# import os
# from multiprocessing import Process
# def func(a):
#     print(a,os.getpid())
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))
#     p.start()

# import os
# from multiprocessing import Process
#
# def func(a):
#     print(a,os.getpid())
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))
#     p.start()

# import os
# from multiprocessing import Process
#
# def func(a):
#     print(a,os.getpid())
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))
#     p.start()

# import os
# from multiprocessing import Process
#
# def func(a):
#     print(a,os.getpid())
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))
#     p.start()



