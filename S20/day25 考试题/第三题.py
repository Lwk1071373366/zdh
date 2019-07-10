'''
3、写函数，计算一个大文件的md5值（5分）
'''
# import os
# import hashlib
# def file_md5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while filesize >= 4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def file(path):
#     return file_md5(path)
# path = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\作业题讲解.mp4'
# ret = file(path)
# print(ret)

# import os
# import hashlib
# def file_md5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while filesize >= 4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def file(path):
#     return file_md5(path)
# path = r'lujing'
# ret = file(path)
# print(ret)

# import os
# import hashlib
# def file_md5(path):
#     file_size = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while file_size >= 4096:
#             content = f.read(4096)
#             md5.update(content)
#             file_size -= 4096
#         else:
#             content = f.read(file_size)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def file(path):
#     return file_md5(path)
# path = r'lujing'
# ret = file(path)
# print(ret)


# import os
# import hashlib
#
# def file_md5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while filesize >=4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def file(path):
#     return file_md5(path)
# path = r'D:\飞秋资料（讲师每天的视频及大纲）\day18\视频\作业题讲解.mp4'
# ret = file(path)
# print(ret)

# import os
# import hashlib
# def file_mad5(path):
#     filesize = os.path.getsize(path)
#     md5 = hashlib.md5()
#     with open(path,'rb') as f :
#         while filesize >4096:
#             content = f.read(4096)
#             md5.update(content)
#             filesize -= 4096
#         else:
#             content = f.read(filesize)
#             if content:
#                 md5.update(content)
#     return md5.hexdigest()
# def file(path):
#     return file_mad5(path)
# path = r'path'
# ret = file(path)
# print(ret)