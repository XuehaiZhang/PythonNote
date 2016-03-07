#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


# # 调用堆栈
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     bar('0')
#
# main()

# Traceback (most recent call last):
#   File "/Users/bpmacmini01/PyWork/LearnPy/FixError/err.py", line 19, in <module>
#     main()
#   File "/Users/bpmacmini01/PyWork/LearnPy/FixError/err.py", line 17, in main
#     bar('0')
#   File "/Users/bpmacmini01/PyWork/LearnPy/FixError/err.py", line 13, in bar
#     return foo(s) * 2
#   File "/Users/bpmacmini01/PyWork/LearnPy/FixError/err.py", line 9, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero

# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常容易地记录错误信息：
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。
# import logging
#
#
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
#
# main()
# print('END')


# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。
# 因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，
# 然后，用raise语句抛出一个错误的实例：
# class FooError(ValueError):
#     pass
#
#
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')
# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。


# raise语句如果不带参数，就会把当前错误原样抛出。
# 此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，
# 又把错误通过raise语句抛出去了，这不有病么？
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# 好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

