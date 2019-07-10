import re
def mul_div(exp):
    '''
    计算最简单的两个数之间的乘除法
    :param exp: str数据类型的 两个数的乘除法表达式,例如'2.34*3.21'
    :return: str数据类型的计算结果
    '''
    if '*' in exp:
        a,b = exp.split('*')
        return str(float(a)*float(b))
    else:
        a, b = exp.split('/')
        return str(float(a) / float(b))

def format_exp(exp):
    '''
    完成表达式格式整理,将一些叠在一起的符号整理成一个符号
    :param exp: str数据类型的表达式 '1.23++3+-4--5'
    :return: 整理之后的str数据类型的字符串,'1.23+3-4+5'
    '''
    exp = exp.replace('++','+')
    exp = exp.replace('-+','-')
    exp = exp.replace('+-','-')
    exp = exp.replace('--','+')
    return exp

def cal_no_bracket(no_bracket_exp):  #
    '''
    计算内部不再有其他小括号的表达式
    :param no_bracket_exp:字符串数据类型的,内部不再含有其他小括号的表达式,例如:(9-2*5/3+7/3*99/4*2998+10*568/14)
    :return: float数据类型的结果
    '''
    # 再计算乘除法
    while True:
        mul_dic_exp = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', no_bracket_exp)
        if mul_dic_exp:
            md_exp = mul_dic_exp.group()
            res = mul_div(md_exp)
            no_bracket_exp = no_bracket_exp.replace(md_exp, res)
        else:break
    # 表达式中的符号管理,把++ 编程+ ,--变成+
    no_bracket_exp = format_exp(no_bracket_exp)
    # 再计算加减法
    res_lst = re.findall('[-+]?\d+(?:\.\d+)?',no_bracket_exp)
    sum_n = 0
    for i in res_lst:
        sum_n += float(i)
    return sum_n

def remove_bracket(exp):
    '''
    将表达式中所有的括号都计算出结果,替换原有的表达式,直到这个表达式内不再含有括号
    :param exp:str类型带着括号的表达式'1-2*((60-30+(9-2*5/3+7/3*99/4*2998+10*568/14)*(-40/5))-(-4*3)/(16-3*2))'
    :return:str类型的不带括号的表达式'1-2*-1388335.8476190479'
    '''
    # 先计算括号内的
    while True:
        ret = re.search('\([^()]+\)', exp)  #1-2*5
        if ret:
            no_bracket_exp = ret.group()  # (9-2*5/3+7/3*99/4*2998+10*568/14)
            res = cal_no_bracket(no_bracket_exp)  # (9-2*5/3+7/3*99/4*2998+10*568/14)
            exp = exp.replace(no_bracket_exp,str(res))
        else:break
    return exp

def calculator(exp):
    '''
    处理原始表达式格式,去掉括号并且进行最后一步计算
    :param exp:原始的字符串格式的表达式
    :return:float类型的结果
    '''
    exp = exp.replace(' ','')
    ret = remove_bracket(exp)
    return cal_no_bracket(ret)

exp = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )*(-40/5)) - (-4*3)/ (16-3*2) )'
res = calculator(exp)
print(res,type(res))
#


# import  re
# def mul_div(exp):
#     if '*' in exp:
#         a,b =exp.split('*')
#         return str(float(a)/float(b))
# def format_exp(exp):
#     exp = exp.replace('++','+')
#     exp = exp.replace('+-','-')
#     exp = exp.replace('--','+')
#     exp = exp.replace('-+','-')
#     return exp
# def cal_no_bracket(no_bracket_exp):
#     while True:
#         mul_dic_exp = re.search('\d+(\.\d)?[*/]-?\d+(\.\d)?',no_bracket_exp)
#         if mul_dic_exp:
#             md_exp = mul_dic_exp.group()
#             res = mul_div(md_exp)
#             no_bracket_exp = no_bracket_exp.replace(md_exp,res)
#         else:break
#     no_bracket_exp = format_exp(no_bracket_exp)
#     res_lst = re.findall('[-+]?\d+(?:\.\d+)?',no_bracket_exp)
#     sum_n = 0
#     for i in res_lst:
#         sum_n += float(i)
#     return sum_n
# def remove_bracket(exp):
#     while True:
#         ret = re.search('\([^()]+\)',exp)
#         if ret:
#             no_bracket_exp = ret.group()
#             res = cal_no_bracket(no_bracket_exp)
#             exp = exp.replace(no_bracket_exp,str(res))
#         else:break
#     return exp
# def calculator(exp):
#     exp = exp.replace(' ','')
#     ret = remove_bracket(exp)
#     return cal_no_bracket(ret)
# exp = '1 - 2 * ( (60-30 + (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )*(-40/5)) - (-4*3)/ (16-3*2) )'
# res = calculator(exp)
# print(res,type(res))


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

















