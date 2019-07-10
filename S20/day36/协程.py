from greenlet import greenlet
# def eat():
#     print('start eating')
#     g2.switch()
#     print('eating')
#     print('end eating')
#     g2.switch()
# def sleep():
#     print('start sleeping')
#     g1.switch()
#     print('sleeping')
#     print('end sleeping')
# g1 = greenlet(eat)
# g2 = greenlet(sleep)
# g1.switch()
#
# import gevent
# def eat():
#     print('start eating')
#     gevent.sleep(1)
#     print('end eating')
# def sleep():
#     print('start sleeping')
#     gevent.sleep(1)
#     print('end sleeping')
# gevent.spawn(eat)
# gevent.spawn(sleep)
# gevent.sleep(3)



# import time
# from urllib.request import urlopen
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def get_html(name,addr):
#     ret = urlopen(addr)
#     return {'name':name,'content':ret.read()}
# def parser_page(ret_obj):
#     # start = time.time()
#     dic = ret_obj.result()
#     with open(dic['name']+'.html','wb') as f :
#         f.write(dic['content'])
#     # end_time = time.time()-start
#     # print(end_time)
# url_lst = {
#     '协程':'http://www.cnblogs.com/Eva-J/articles/8324673.html',
#     '线程':'http://www.cnblogs.com/Eva-J/articles/8306047.html',
#     '目录':'https://www.cnblogs.com/Eva-J/p/7277026.html',
#     '百度':'http://www.baidu.com',
#     'sogou':'http://www.sogou.com'
# }
# t = ThreadPoolExecutor(20)
# for url in url_lst:
#     task = t.submit(get_html,url,url_lst[url])
#     task.add_done_callback(parser_page)

# url_dic = {
#     '协程':'http://www.cnblogs.com/Eva-J/articles/8324673.html',
#     '线程':'http://www.cnblogs.com/Eva-J/articles/8306047.html',
#     '目录':'https://www.cnblogs.com/Eva-J/p/7277026.html',
#     '百度':'http://www.baidu.com',
#     'sogou':'http://www.sogou.com',
#     '4399':'http://www.4399.com',
#     '豆瓣':'http://www.douban.com',
#     'sina':'http://www.sina.com.cn',
#     '淘宝':'http://www.taobao.com',
#     'JD':'http://www.JD.com'
# }
# import time
# from gevent import monkey;monkey.patch_all()
# from urllib.request import urlopen
# import gevent
# def get_html(name,url):
#     ret = urlopen(url)
#     count = ret.read()
#     with open(name,'wb') as f :
#         f.write(count)
# start = time.time()
# for name in url_dic:
#     get_html(name+'_sync.html',url_dic[name])
# ret = time.time() - start
# # print('同步时间',ret)
#
# start = time.time()
# g_l = []
# for name in url_dic:
#     g = gevent.spawn(get_html,name+'async.html',url_dic[name])
#     g_l.append(g)
# gevent.joinall(g_l)
# ret = time.time()-start
# # print('异步时间',ret)










