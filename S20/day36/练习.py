#线程池开启任务 如何开启线程池 如何提交任务 获取返回值
#方法一
# from concurrent.futures import ThreadPoolExecutor
# def func(arg):
#     return arg * 20
#
# tp = ThreadPoolExecutor(5)
# ret_l = []
# for i in range(100):
#     ret = tp.submit(func,i)
#     ret_l.append(ret)
# for i in ret_l:
#     print(i.result())
#方法二

# from concurrent.futures import ThreadPoolExecutor
# def func(arg):
#     return arg * 20
# tp = ThreadPoolExecutor(5)
# ret_l = tp.map(func,range(100))
# for i in ret_l:
#     print(i)



# def checknum():
#     import random
#     l_check=[]
#     for i in range(0,4):
#         upper = chr(random.randint(65, 90))
#         lower = chr(random.randint(97, 122))
#         num = random.randint(0, 9)
#         loc = random.randint(1, 3)
#         if loc==1:
#             l_check.append(upper)
#         elif loc==2:
#             l_check.append(lower)
#         else :
#             l_check.append(str(num))
#     s_check = ''.join(l_check)
#     print(s_check)
# checknum()
