#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。
def application(environ, start_response):
    # 发送了HTTP响应的Header，注意Header只能发送一次，
    # 也就是只能调用一次start_response()函数。
    # start_response()函数接收两个参数，一个是HTTP响应码，
    # 一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:])
    print(environ)
    return [body.encode('utf-8')]
