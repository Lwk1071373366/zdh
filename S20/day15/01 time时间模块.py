# '2019-03-20 10:40:00'
# 这个时间向后退一个月
# 获取当前时间求前一月的现在时间
# import time
# s1=time.strptime('2019-03-20 10:40:00','%Y-%m-%d %X')
# # print(s1)
# s2=time.mktime(s1)
# # print(s2+86400*31)
# s3=s2+86400*31
#
# s4=time.localtime(s3)
# # print(s4)
# s5=time.strftime('%Y-%m-%d %X',s4)
# print(s5)
#
# s6=time.time()-30*86400
# s7=time.localtime(s6)
# print(time.strftime('%Y-%m-%d %X',s7))
# from datetime import datetime,timedelta
# print(datetime.now()-timedelta(hours=13))