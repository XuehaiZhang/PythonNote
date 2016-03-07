#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

__author__ = 'bpmacmini01'


def my_abs(x):
    # 参数类型检测
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-10))


# pass占位符，各种地方都可以用~
def nop():
    pass


print(nop())


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x1, y1 = move(100, 100, 60, math.pi / 6)
print(x1, y1)
r = move(100, 100, 60, math.pi / 6)
print(r)


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) & isinstance(b, (int, float)) & isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    tmp = b * b - 4 * a * c
    if tmp < 0:
        return 'NoResult'
    elif tmp == 0:
        return -b / (a * 2)
    else:
        tp = math.sqrt(tmp)
        x = (-b + tp) / (a * 2)
        y = (-b - tp) / (a * 2)
        return x, y


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))
s = 'a' + 'b'
print(s)
s = 'a' 'b'
print(s)


# 默认参数相关！！！
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
# 因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
# 如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=[]):
#     L.append('END')
#     return L
# # ['END']
# print(add_end())
# # ['END', 'END']
# print(add_end())
# # ['END', 'END', 'END']
# print(add_end())


def add_end(li=None):
    if li is None:
        li = []
    li.append('End')
    return li


# 当参数为可变参数时候 改变了 原来的也会改变 我觉得这些类型实际上类似于指针
l = [1, 2, 3]
add_end(l)
print(l)

print(add_end())
print(add_end())
print(add_end())


# 可变参数
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple！！！
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum1 = 0
    print(type(numbers))
    for n in numbers:
        sum1 += n * n
    return sum1


print(calc(1, 2))
print(calc())


# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
# 因为传进去之后都变成tuple了 不可变
nums = [1, 2, 3]
calc(*nums)
print(nums)
print(calc(*nums))


# 疯狂地测试
# 为什么我能想出这么酷炫的测试用例
# 这里说明形参和实参实际上指向同一个地方 不是拷贝！！！
def crazy(*t):
    print('是否为list', type(t[3]))
    t[3].append('End')
    print(t)


ts = [1, 2, 3, [4, 5, 6]]
crazy(*ts)
print(ts)


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)


person('Mike', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
person2('Jack', 24, city='Beijing', job='Engineer')
# 这正是一个奇怪的方式
dd = {'city': 'Beijing', 'job': 'Worker'}
person2('Jack', 24, **dd)


def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person3('Jack', 24, job='Engineer')


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw = ', kw)


def f2(a, b, c=0, *, d='a', **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw = ', kw)


def f3(a, b, c=0, d=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd = ', d, 'args =', args, 'kw = ', kw)

f1(1, 2)
f1(1, 2, 3)
# 最后关键字参数的key值不能为啊a,b,c
f1(1, 2, 3, 'd', e='e')
f1(1, 2, args='d', e='e')  # a = 1 b = 2 c = 0 args = () kw =  {'e': 'e', 'args': 'd'}
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
# f3(1, 2, d=99, 'a', 'b', x=99) 报错 当默认参数后面还有参数时 不能通过key值 跳过某一个
# 以下注释部分均会报错
# TypeError: f2() got multiple values for argument
# 最后关键字参数的key值不能为a,b,c,d
# d = {'d': 12}
# f2(1, 2, 3, d='a', **d)
# d = {'b': 12}
# f2(1, 2, 3, d='a', **d)
# d = {'c': 12}
# f2(1, 2, 3, d='a', **d)
# d = {'a': 12}
# f2(1, 2, 3, d='a', **d)


# 最神奇的是通过一个tuple和dict，你也可以调用上述函数：
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def f4(a, b, c=0, *args, **kw):
    a += 1
    args[0][1] = 10
    kw['d'] = 88
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw = ', kw)


def f5(a, b, c=0, *, d='a', **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw = ', kw)

#这个测试 可以方便的看出哪些是指向 哪些是拷贝
args = (1, 2, 3, [4, 5])
kw = {'d': 99, 'x': "#"}
f4(*args, **kw)
print(args)
print(kw)

args = (1, 2, 3)
kw = {'d': 99, 'x': "#"}
f5(*args, **kw)


# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))


# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
# 所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
# 都只占用一个栈帧，不会出现栈溢出的情况。
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact_iter(5, 1))


# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')


