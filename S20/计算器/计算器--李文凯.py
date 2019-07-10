# import re
# exp = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )*(-40/5)) - (-4*3)/ (16-3*2) )'
# def mul_div(exp):
#     if '*'in exp:                         #遍历exp ，以* / 分割，先用浮点型算出结果，再转为str，以便后面带入。
#         a,b = exp.split('*')
#         return str(float(a)*float(b))
#
#     else:
#         a,b = exp.split('/')
#         return str(float(a)/float(b))
# def format_exp(exp):                      #将exp中有可能出现的运算符的情况提前转换一下
#     exp = exp.replace('++','+')
#     exp = exp.replace('+-','-')
#     exp = exp.replace('-+','-')
#     exp = exp.replace('--','+')
#
#     return exp
# def cal_no_bracket(no_bracket_exp):
#     while True:
#         mul_dic_exp = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?',no_bracket_exp)
#         if mul_dic_exp:
#             md_exp = mul_dic_exp.group()
#             res = mul_div(md_exp)
#             no_bracket_exp = no_bracket_exp.replace(md_exp,res)
#         else:break
#     no_bracket_exp = format_exp(no_bracket_exp)
#     res_lst = re.findall('[-+]?\d+(?:\.\d+)?',no_bracket_exp)
#     sum_n = 0
#     for i in res_lst:
#         sum_n +=float(i)
#     return sum_n
# def remove_bracket(exp):
#     while True:
#         ret = re.search('\([^()]+\)',exp)
#         if ret:
#             no_brack_exp = ret.group()
#             res = cal_no_bracket(no_brack_exp)
#             exp = exp.replace(no_brack_exp,str(res))
#         else:
#             break
#     return exp
# def calculator(exp):
#     exp = exp.replace(' ','')
#     ret = remove_bracket(exp)
#     return cal_no_bracket(ret)
# res = calculator(exp)
# print(res)


# exp = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )*(-40/5)) - (-4*3)/ (16-3*2) )'
# import re
# def mul_div(exp):
#     if '*' in exp:
#         a,b =exp.split('*')
#         return str(float(a)*float(b))
#     else:
#         a,b = exp.split('/')
#         return str(float(a)/float(b))
# def format_exp(exp):
#     exp = exp.replace('++','+')
#     exp = exp.replace('--','+')
#     exp = exp.replace('+-','-')
#     exp = exp.replace('-+','-')
#     return exp
# def cal_no_bracket(no_bracket_exp):
#     while True :
#         mul_dic_exp = re.search('\d+(\.\d+)?[*/]\d+(\.\d+)?',no_bracket_exp)
#         if mul_dic_exp:
#             md_exp = mul_dic_exp.group()
#             res = mul_div(md_exp)
#             no_bracket_exp = no_bracket_exp.replace(md_exp,res)
#         else:break
#     no_bracket_exp = format_exp(no_bracket_exp)
#     res_lst = re.findall('[-+]?\d+(?:\.\d+)?',no_bracket_exp)
#     sun = 0
#     for i in res_lst:
#         sun += float(i)
#     return sun
# def remove_bracket(exp):
#     while True:
#         ret = re.search('\([^()]+\)',exp)
#         if ret:
#             no_bracket_exp =ret.group()
#             res = cal_no_bracket(no_bracket_exp)
#             exp = exp.replace(no_bracket_exp,str(res))
#         else:break
#     return exp
# def calculator(exp):
#     exp = exp.replace(' ','')
#     ret =remove_bracket(exp)
#     return cal_no_bracket(ret)
# res = calculator(exp)
# print(res,type(res))