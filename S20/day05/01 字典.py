# dic={'name':'taibai','age':18,}
# dic['name']='jinxing'
# print(dic)
# dic['hobby']='car'
# print(dic)
# dic.setdefault('sex','nan')
# print(dic)
# res=dic.pop('name2',None)
# print(res)
# dic.clear()
# print(dic)
# del dic['name']
# print(dic)
# del dic['sex']
# print(dic)
# del dic
# print(dic)

# dic['name']='jin'
# print(dic)
# set=dic.update()   XXXX
# print(set)

# print(dic['name'])
# ret=dic.get('name')
# print(ret)

# ret=dic.keys()
# print(ret)
# print(dic.values())
# print(dic.items())
# a=100
# b=1000
# a,b=b,a
# print(a,b)
# --------------------------------------以上练习
dic = {
    'name_list': ['博哥', '菊哥', 'b哥', 'alex'],
    'barry': {
        'name': '太白金星',
        'age': 18,
        'hobby': 'wife',
    }
}

# 1，给这个列表['博哥', '菊哥', 'b哥', 'alex'] 追加一个元素 '老男孩'。
# 2，将这个列表['博哥', '菊哥', 'b哥', 'alex']中的alex变成首字母大写。
# 3，将这个键值对 'name': '太白金星' 的 '太白金星' 改成男神。
# 4，给barry对应的小字典增加一个键值对： weight: 160
dic['name_list'].append('老男孩')
print(dic)
# dic['name_list'][3]=dic['name_list'][3].capitalize()
# print(dic)
# dic['barry']['name']='男神'
# print(dic)
# dic['barry']['weight']=160
# print(dic)
