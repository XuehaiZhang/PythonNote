#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


# 所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，
# 它不但捕获该类型的错误，还把其子类也“一网打尽”。
# 常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
try:
    # foo()
    pass
except ValueError as e:
    print('ValueError:', e)
except UnicodeError as e:
    print('UnicodeError:', e)


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，
# 这时，只要main()捕获到了就可以处理：
def foo(s):
    return bar(s) * 2


def bar(s):
    return 10 / int(s)


def main():
    try:
        foo('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

if __name__ == '__main__':
    main()

