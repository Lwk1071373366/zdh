# import time
# import random
# from multiprocessing import Process
# def send_mail(name):
#     time.sleep(random.uniform(1,5))
#     print('已经给%s发了邮件'%name)
# if __name__ == '__main__':
#     lst = ['alex','baoyuan','eva_j','taibai']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('所有信息已发送')

# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,5))
#     print('已经给%s发送邮件了'%name)
# if __name__=='__main__':
#     lst = ['alex','baoyuan','taibai','eva_j']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('都发完了')


# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,3))
#     print('已经给%s发完邮件了'%name)
# if __name__ == '__main__':
#     lst  = ['taibai','baoyuan','alex']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('都发完了')


# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,2))
#     print('已经给%s发了邮件'%name)
# if __name__ == '__main__':
#     lst = ['taibai','alex']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('都发完了')


# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,3))
#     print('已经给%s发邮件了'%name)
# if __name__ == '__main__':
#     lst = ['taibai','alex']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('都已经发完了')

# import time
# import random
# from multiprocessing import Process
#
# def send_mail(name):
#     time.sleep(random.uniform(1,3))
#     print('已经给%s发邮件了'%name)
# if __name__ == '__main__':
#     lst = ['taibai','alex']
#     p_l = []
#     for name in lst:
#         p = Process(target=send_mail,args=(name,))
#         p.start()
#         p_l.append(p)
#     for p in p_l:
#         p.join()
#     print('都发了')

