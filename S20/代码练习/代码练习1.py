# import os
# from multiprocessing import Process
#
# class MyProcess(Process):
#     def __init__(self,a,b):
#         super().__init__()
#         self.a = a
#         self.b = b
#     def run(self):
#         print(os.getpid(),self.a,self.b)
# if __name__== '__main__':
#     for i in range(10):
#         MyProcess(1,2).start()


from threading import enumerate,Thread

def func():
    print('in son thread')
Thread(target=func).start()
print(enumerate())
