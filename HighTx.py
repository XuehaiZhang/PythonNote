#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
from collections import Iterator
import os

__author__ = 'bpmacmini01'

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 不包括索引3
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
# 不包括索引-1
print(L[-2: -1])

L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
# 前10个数，每2个取一个
print(L[:10:2])
print(L[::5])

print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。
# 因此，字符串也可以用切片操作，只是操作结果仍是字符串

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

print(type(d.items()))

for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(range(100), Iterable))
print(isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
l = []
for x in range(100):
    l.append((x, x))

for x, y in l:
    print(x, y)

for i, value in [(1, 1), (2, 4), (3, 9)]:
    print(i, value)

# 列表生成器
print(list(x * x for x in range(1, 11)))
print([x * x for x in range(1, 11)])
# 果然可以
print([[x, x] for x in range(1, 11)])
print(type([(x, x) for x in range(1, 11)][0]))
g = lambda x : x+2
info = [g(x) for x in range(10)]
print(info)

def g(x):
    return x+2

print([g(x) for x in range(10)])


# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层(多层)循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
print([m + n for m, n in [(1, 1), (2, 4), (3, 9)]])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': ' B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)

# 生成器
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) StopIteration

# next()之后要重新生成一个generator！！！
g = (x * x for x in range(10))
for n in g:
    print(n)


# generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # 要把fib函数变成generator，只需要把print(b)改为yield b就可以了
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

f = fib(6)
print(f)
for a in f:
    print(a)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
f = fib(6)
while True:
    try:
        x = next(f)
        print('f:', x)
    except StopIteration as e:
        print(e.value)
        break


# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L)-1)]
        L.insert(0, 1)
        L.append(1)
n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break

f = triangles()
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
print(isinstance((x for x in range(10)), Iterator))

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
g = iter([1, 2, 3])
print(next(g))
# 注意这里的试验
g = iter({'a': 'A', 'b': 'B'})
print(next(g))
print(type(next(g)))
g = iter({'a': 'A', 'b': 'B'}.items())
print(next(g))
print(type(next(g)))

