#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import asyncio
from aiohttp import web


def index(request):
    # 我以为是我的问题 结果不是  教程代码执行结果就这样 这里页面直接显示了全部字符
    # 如果不加上 content_type="text/html" 这个参数默认为None
    # 某些浏览器 如Safari 会直接显示出<h1>Awesome</h1>
    return web.Response(body=b'<h1>Index</h1>', content_type="text/html")


def hello(request):
    yield from asyncio.sleep(0.5)
    text = '<h1>hello, %s</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type="text/html")


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()