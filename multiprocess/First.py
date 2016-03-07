#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import os

# 多进程


# # UNIX下
# # 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# # 然后，分别在父进程和子进程内返回。
#
# # 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
# # 所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#     # 用来结束进程！！！
#     os._exit(os.getpid())
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
#
# # multiprocessing 跨平台多进程
# from multiprocessing import Process
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
#     p.join()
#     print('Child process end')
#
# # Pool批量创建子进程
# from multiprocessing import Pool
# import time, random
#
#
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s run %0.2f seconds' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Wait for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# # 子进程
# import subprocess
#
# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)


# # 进程间通信
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', "C"]:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__ == '__main__':
#     q= Queue()
#     pw = Process(target=write, args=(q, ))
#     pr = Process(target=read, args=(q, ))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()

