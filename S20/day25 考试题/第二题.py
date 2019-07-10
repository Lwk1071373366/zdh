'''
2、写函数，完成清空一个文件夹的功能，假设这个文件夹中可能存在其他文件，但不存在文件夹（5分）
加分题 ：如果一个文件夹中还有其他文件和非空文件夹（10分）

'''
# import os
# def clear_dir(path):
#     if os.path.isdir(path):
#         name_lst = os.listdir(path)
#         for name in name_lst:
#             son_path = os.path.join(path,name)
#             os.remove(son_path)
# clear_dir('path')


# import os
# def clear_dir(path):
#     if os.path.isdir(path):
#         name_lst = os.listdir(path)
#         for name in name_lst:
#             son_path = os.path.join(path,name)
#             os.remove(son_path)
# clear_dir('path')


import os
def clear_dir(path):
    if os.path.isdir(path):
        name_lst = os.listdir(path)
        for name in name_lst:
            son_path = os.path.join(path,name)
            os.remove(son_path)
clear_dir('path')