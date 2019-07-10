# s1='双击'
# a=s1.encode('utf-8')
# print(a,type(a))    #字符串到utf-8   bytes 的转化

# b=s1.encode('gbk')
# print(b)              #字符串到gbk   bytes 的转化

# 终极转换
# utf-8   bytes   ----》gbk   bytes

# c=a.decode('utf-8')
# print(c)                先将utf-8编码的bytes （decode）解码成 Unicode ；再将Unicode编码的bytes （encode）编码成gbk。
# d=c.encode('gbk')
# print(d)