#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


# # 多线程
import time, threading
#
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print(('thread %s >>> %s' % (threading.current_thread().name, n)))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread % s ended.' % threading.current_thread().name)


# 多线程和多进程最大的不同在于，多进程中，同一个变量，
# 各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# import threading, multiprocessing
# # 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
# # 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
# # 让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# # 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

print(-101 % 4)
s = 'sss'
print(s[0])

import itertools

ns = itertools.repeat('ABC', 3)
for n in ns:
    print(n)

from urllib import request

url = 'http://weather.yahooapis.com/forecastrss?u=c&w=2151330'
data = request.urlopen(url)
# 只能read一次 第二次就没了！！！
s = data.read().decode('utf-8')
# print(data.read().decode('utf-8'))

from xml.parsers.expat import ParserCreate


class WeatherSaxHandler(object):
    def __init__(self):
        self.location = dict()
        self.weather = list()

    def start_element(self, name, attrs):
        if name == 'yweather:location':
            self.location['city'] = attrs['city']
            self.location['country'] = attrs['country']
            print(self.location)

        if name == 'yweather:forecast' and len(self.weather) < 2:
            aweather = dict()
            aweather['text'] = attrs['text']
            aweather['high'] = attrs['high']
            aweather['low'] = attrs['low']
            self.weather.append(aweather)

    def end_element(self, name):
        pass

    def char_data(self, text):
        pass


def parse_weather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return {
        'city': handler.location['city'],
        'country': handler.location['country'],
        'today': {
            'text': handler.weather[0]['text'],
            'low': handler.weather[0]['low'],
            'high': handler.weather[0]['high']
        },
        'tomorrow': {
            'text': handler.weather[1]['text'],
            'low': handler.weather[1]['low'],
            'high': handler.weather[1]['high']
        }
    }
print(parse_weather(s))


from urllib import request, parse

print('Login to weibo')
username = '18627947930'
passwd = 'zxh3221952'
login_data = parse.urlencode([
    ('username', username),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
