#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


import asyncio


# @asyncio.coroutine
# def hello():
#     print('HELLO WORLD!')
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(0.5)
#     print("HELLO AGAIN!")
#
# loop = asyncio.get_event_loop()
#
# loop.run_until_complete(hello())
# loop.close()


# import threading
#
#
# @asyncio.coroutine
# def hello():
#     print('HELLO WORLD! (%s)' % threading.current_thread())
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(2)
#     print("HELLO AGAIN! (%s)" % threading.current_thread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    conect = asyncio.open_connection(host, 80)
    # 这里也会停  魂淡！！！
    reader, writer = yield from conect
    print(host)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

