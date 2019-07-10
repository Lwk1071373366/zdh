# f=open('D:\文件操作.txt',encoding='utf-8',mode='r')
# print(f.read())
# f.close()
# f=open('r模式',encoding='utf-8',mode='r+')
# f.read()
# f.write('999')
# f.close()
# f=open('r模式',encoding='utf-8',mode='r')
# for line in f:
#     print(line)
# line.close()
# f=open('w模式',encoding='utf-8',mode='w')
# f.write('laonanhai')
# f.close()
# f=open('图片.jpg',mode='rb')
# print(f.read())
# f.close()
# f1=open('图片2.jpg',mode='wb')
# f1.write('图片')
# f1.close()
# with open('r模式',encoding='utf-8',mode='r')as f1:
#     print(f1.read())
#     # f1.close()
#     with open('r模式',encoding='utf-8',mode='w') as f2:
#         print(f2.write())
# import os
# with open('alxe自述',encoding='utf-8') as f1,\
#     open('alxe自述.bak',encoding='utf-8',mode='w') as f2:
#         old_neirong=f1.read()
#         new_neirong=old_neirong.replace('alex','sb')
#         f2.write(new_neirong)
# os.remove('alxe自述')
# os.rename('alxe自述.bak','alxe自述')
#


# import os
# with open('alxe自述',encoding='utf-8') as f1,\
#     open('alxe自述.bak',encoding='utf-8',mode='w') as f2:
#        for old_line in f1:
#         new_line =old_line.replace('sb','taibai')
#         f2.write(new_line)
# os.remove('alxe自述')
# os.rename('alxe自述.bak','alxe自述')
# import os
# with open('alxe自述',encoding='utf-8',) as f1,\
#     open('alxe自述.bak',encoding='utf-8',mode='w') as  f2:
#     for old_line in f1:
#         new_line=old_line.replace('taibai','sabi')
#         f2.write(new_line)
# os.remove('alxe自述')
# os.rename('alxe自述.bak','alxe自述')
#
# import os
# with open('alxe自述',encoding='utf-8') as f1,\
#     open('alxe自述.bak',encoding='utf-8',mode='w')as f2:
#     for old_line in f1:
#         nem_line=old_line.replace('taibai','sb')
#         f2.write(nem_line)
# os.remove('alxe自述')
# os.rename('alxe自述.bak','alxe自述')





















