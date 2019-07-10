import time
import random
import gevent
from gevent import time

while True:
    def producer():
        print('太白做好了饭')
        gevent.sleep(1)
        print('太黑做好了饭')
    def consumer():
        print('小黑吃了')
        gevent.sleep(1)
        print('小白吃了')

    gevent.spawn(producer)
    gevent.spawn(consumer)
    gevent.sleep(2)