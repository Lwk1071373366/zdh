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
#     l = ['alex','wusir','baoyuan','taibai']
#     for name in l:
#         Process(target=use,args=(name,lock)).start()

