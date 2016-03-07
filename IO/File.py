#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)  # 操作系统类型

# 要获取详细的系统信息，可以调用uname()函数：
# 注意uname()函数在Windows上不提供
print(os.uname())
# 操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('s'))
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join(os.path.abspath('.'), 'testdir'))
# 然后创建一个目录:
os.mkdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 删掉一个目录:
os.rmdir(os.path.join(os.path.abspath('.'), 'testdir'))
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt'))
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# # 对文件重命名:
# os.rename('test.txt', 'test.py')
# # 删掉文件:
# os.remove('test.py')

# 复制文件需要引入新的模块
import shutil

shutil.copyfile('test.txt', 'test.py')

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
l = [x for x in os.listdir('.') if os.path.isdir(x)]
print(l)
# 要列出所有的.py文件，也只需一行代码：
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(l)


# 序列化
import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('test.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('test.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，
# 不能成功地反序列化也没关系。


# JSON
import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))

f = open('te.json', 'w')
json.dump(d, f)
f.close()

f = open('te.json', 'r')
d = json.load(f)
f.close()
print(d)


# JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# print(json.dumps(s))  # error


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dict
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，
# 用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s, default=lambda obj: obj.__dict__))


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"score": 88, "name": "Bob", "age": 20}'
print(json.loads(json_str, object_hook=dict2student))



