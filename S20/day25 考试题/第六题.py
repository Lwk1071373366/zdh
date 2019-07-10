'''
加分题：
有一个数据结构如下所示，请编写一个函数从该结构数据中返回由指定的字段和对应的值组成的字典。如果指定字段不存在，则跳过该字段。（10分）
data:{"time":"2016-08-05T13:13:05",
	  "some_id":"ID1234",
	  "grp1":{	"fld1":1,
	  			"fld2":2},
	  "xxx2":{	"fld3":0,
	  			"fld5":0.4},
	  "fld6":11,
	  "fld7":7,
	  "fld46":8}
fields:由”|”连接的以"fld"开头的字符串,如:fld2|fld3|fld7|fld19
提示：请考虑字典的嵌套层数不是固定的

def select(data,fields):
	# TODO:implementation
	return result

'''
data = {'time': '2016-08-05T13:13:05', 'some_id': 'ID1234',
'grp1':{'fld1': 1, 'fld2': 2},
'xxx2': {'fld3': 0, 'test': {'fld5': 0.4}}, 'fld6': 11, 'fld7': 7,
'fld46': 8}
def select(data,fields):
    l1=[]
    for k,v in data.items():
        if isinstance(v,dict):
            l1+=select(v,fields)
        elif k in fields:
            l1.append({k:v})
    return l1
def core():
    while True:
        fields=input('field>>>:').strip().split('|')
        if fields[0].upper()=='Q':
            break
        print(select(data,fields))
core()