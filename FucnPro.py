#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

__author__ = 'bpmacmini01'


def add(x, y, f):
    return f(x) + f(y)


print(add(12, -22, abs))


# map/reduce

# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4])))
print(tuple(map(f, (1, 2, 3, 4))))
print(list(map(f, {1: 'a', 2: 'a'})))


def f1(x):
    return [x[0], 'b']


print(dict(map(f1, {1: 'a', 2: 'a'}.items())))

print(list(map(str, [1, 2, 3, 4, 5])))


# reduce的用法。
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('12345'))


# 仅仅为了试验map里面也可以用lambda表达式
def str2int(s):
    return reduce(lambda x, y: x * 10 + y,
                  map(lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s], s))


print(str2int('12345'))
print(int('12345'))

L = ['adam', 'LISA', 'barT']
r = map(lambda s: s[0].upper() + s[1:].lower(), L)
print(list(r))


def prod(L):
    return reduce(lambda x, y: x * y, L)


L = [3, 5, 7, 9]
print(prod(L))


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    L = s.split('.')
    print(L)
    print(type(L))
    print(''.join(L))
    f = reduce(lambda x, y: x * 10 + y, map(char2num, ''.join(L)))
    if len(L) > 1:
        return f / pow(10, len(L[1]))
    else:
        return f / 1


print(str2float('12.23'))


# filter
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))


def _odd_iter():
    n = 1
    while True:
        n += 2
        # print('zhi')
        yield n
        # print('zhixing')


def _not_divisible(n):
    print('n:', n)

    # def f(x):
    #     print('x:', x)
    #     print('n', n)
    #     return x % n > 0
    #
    # return f
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        # print('n1', n)
        yield n
        # 底层的实现应该是每次要获得新值是，用之前的所有过滤过滤一遍
        # 为什么不能it = filter(lambda x: x % n > 0, it)
        # 你不能直接引用变量n，因为它在后面的循环中随时在变化，必须用函数参数捕获当前的n，复制一份。
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 100:
        print(n)
    else:
        break


def is_palindrome(n):
    s = str(n)
    s1 = s[::-1]
    return s == s1


output = filter(is_palindrome, range(1, 1000))
print(list(output))

# sorted
print(sorted([36, 5, -12, 9, -12]))
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([36, 5, -12, 9, -12], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0].lower()


print(sorted(L, key=by_name))
print(L)


def by_score(t):
    return t[1]


print(sorted(L, key=by_score, reverse=True))


# 函数作为返回值
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())


# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# 为了用循环变量
# 套一层函数该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    fs = []

    def g(i):
        def f():
            return i * i

        return f

    for i in range(1, 4):
        fs.append(g(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
print(list(map(lambda x: x * x, [1, 2, 3, 4])))

f = lambda x: [x, x + 1]
print(f(5))


# 装饰器
def now():
    print('2015-8-27')


f = now
f()

print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 把@log放到now()函数的定义处，相当于执行了语句：
# now = log(now)
@log
def now():
    print('2015-8-27')

now()


# 三层
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper
    return decorator


# @log('execute')相当于now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')

now()
# 函数的__name__属性被改变了
print(now.__name__)

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-8-27')

now()
print(now.__name__)


#练习
def log(f):
    print('Begin call')
    if (not hasattr(f, '__call__')):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print("%s %s():" % (f, func.__name__))
                ret = func(*args, **kw)
                print('End call')
                return ret
            return wrapper
        return decorator
    else:
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print("call %s():" % f.__name__)
            ret = f(*args, **kw)
            print('End call')
            return ret
        return wrapper

@log
def now():
    print('2015-8-27')
now()

@log('execute')
def now():
    print('2015-8-27')
now()


# 偏函数
print(int('12345'))
print(int('1001', base=2))
print(int('12345', 16))
print(int('12345', 8))


def int2(x, base=2):
    return int(x, base)

print(int2('100000'))

int2 = functools.partial(int, base=2)
print(int2('10010'))
# 相当于
kw = {'base': 2}
print(int('10010', **kw))

# 实际上会把10作为*args的一部分自动加到左边
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))


