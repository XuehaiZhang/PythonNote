#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

# print
print('this is', 'new', end='\n')
print('this is''new')

# name = input('a')
# print(name)

print("I\'m \"OK\"")

# 为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\sd///')

# 换行print
print('''this
is
test.o''')

print(3 > 2)

# 缩进表示代码块
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

print(None)

# 浮点数除法和整除
print(10 / 3)
print(9 / 3)
print(10 // 3)
print(9 // 3)

# unicode编码
strU = chr(20236)
print(strU)

print('\u4e2d\u6587')

# encode和decode
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
# 格式化
print('hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Mike', 10000))

print('%2d, %.2f' % (3, 1))
print('%02d, %.2f' % (3, 1.12413))
print('%02d, %.2f' % (3, 1.12513))
print('%d' % True)
print('%s' % 123)
print('%s' % 1.23)
print('%s' % True, 'sf')
print('%d' % True + 'sf')
print('%d%%' % 7)

s1 = 72
s2 = 85
r = (85 - 72) / 75 * 100
print('%2.1f%%' % r)

# list
classmates = ['Mike', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
# 倒数，真是奇怪
print(classmates[-1])
print(classmates[-2])
classmates.append('Adam')
print(classmates)
# 增删改
classmates.insert(1, 'Jack')
print(classmates)
# 删除最后
print(classmates.pop())
# 删除指定,也可以用倒数 真酷炫
print(classmates.pop(1))
print(classmates)
classmates[1] = '张学海'
print(classmates)

L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])

# tuple,不可变的list
classmates = ('Mike', 'Bob', 'Tracy')
# 陷进
t = (1, 2)
print(t)
t = ()
print(t)
t = (1)
print(t)
t = (1,)
print(t)
# 可变的tuple?!!!
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
# 呵呵呵，练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])
# 一些小测试

a = 10
T1 = (a, 'b')
a = 11
print(T1)

a = 'a'
T1 = (a, 'b')
a = 'b'
print(T1)

L1 = ['A', 'B']
T1 = ('a', 'b', L1)
L1[0] = 'X'
print(T1)

# 条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is ', age)
    print('teenager')

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00before')
# else:
#     print('after00')


# 循环
names = ['Mick', 'Bob', 'Tracy']
for name in names:
    print(name)

for x in [1, 2, 3, 4]:
    print(x)

print(type(range(5)))

print(range(5))

print(list(range(5)))

su = 0
for x in range(101):
    su += x
print(su)

su1 = 0
while su1 != 55:
    su1 += 1
print(su1)

su2 = 0
for x in range(101):
    if x == 30:
        continue
    su2 += x
print(su2)

su3 = 0
x = 0
while x < 101:
    if x == 30:
        x += 1
        continue
    x += 1
    su3 += x
print(su3)

# dict key不可以为可变对象
d = {'Mike': 95, 'Bob': 75, 'Tracy': 85}
print(d['Mike'])
d['Adam'] = 67
print(d['Adam'])
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
print('Thomas' in d)
print('Jack' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))
d.pop('Bob')
print(d)

# set 放入的值不可以是可变对象
s = {1, 2, 3}
s = set([1, 2, 3])
print(s)
print(type(s))
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s1 = set([1, 2, 3, 3])
print(s1)
s2 = {2, 3, 4}
print(s2)
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
st = a.replace('a', 'A')
print(st)
print(a)

n1 = 255
print(hex(n1))
a = 0xff
print(str(a))

info = 'void handleRequest DragonRequest request receiveObj receiveObj'
if (info.find("handleRequest") != -1) & (info.find("DragonRequest") != -1) & (info.find("request") != -1):
    print(True)

ixxx = 2
ixxx += 2
ixxx = ixxx + 2


