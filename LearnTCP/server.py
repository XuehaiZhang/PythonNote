#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))
s.listen(5)
print('waiting for connection...')


def tcplink(sock, addr):
    print('ss')
    print('Accept new connection from %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    print('ssss')
    # accept()会等待并返回一个客户端的连接:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
