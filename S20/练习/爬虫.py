from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def get_html(name,addr):
    ret = urlopen(addr)
    return {'name':name,'content':ret.read()}
def parser_page(ret_obj):
    dic = ret_obj.result()
    with open(dic['name']+'.html','wb') as f:
        f.write(dic['content'])
url_lst = {
    'yc':'https://www.cnblogs.com/pyyu/p/9276851.html?tdsourcetag=s_pcqq_aiomsg'
}
t = ThreadPoolExecutor(20)
for url in url_lst:
    task = t.submit(get_html,url,url_lst[url])
    task.add_done_callback(parser_page)