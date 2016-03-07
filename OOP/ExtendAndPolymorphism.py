#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()
cat = Cat()
cat.run()


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat')


class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('Eating meat')


dog = Dog()
dog.run()
cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

b = Animal()
print(isinstance(b, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

print(type(123))
print(type('str'))
print(type(None))

print(type(abs))
print(type(b), type(b) == Animal)

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？
# 可以使用types模块中定义的常量：
import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
# 能用type()判断的基本类型也可以用isinstance()判断：

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 并且还可以判断一个变量是否是某些类型中的一种
# 比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
obj1 = MyObject()
print(getattr(obj, 'y'))
print(obj.y)

# 获取属性'z'，如果不存在，返回默认值404
print(getattr(obj, 'z', 404))

# 获取对象的方法，方法和属性不要重名，会被替换掉的！
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(hasattr(obj, '__init__'))
print(fn())


# 不行
# def xxx(self):
#     return self.x * self.x
# setattr(obj, 'power2', xxx)
# obj.power2()


class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


class Student(object):
    name = 'Student'


s = Student()
print(s.name)


class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90


class Student(object):
    name = 'Student'


s = Student()
print(s.name)
print(Student.name)
s.name = 'Mike'
print(s.name)
print(Student.name)

del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


# 从上面的例子可以看出，在编写程序的时候
# 千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，
# 再使用相同的名称，访问到的将是类属性。

class Student(object):
    def __init__(self, name):
        self.name = name


# 自己找了资料 类实例方法  类方法 静态方法
# 区别：
# 类方法和静态方法都可以被类和类实例调用，类实例方法仅可以被类实例调用
# 类方法的隐含调用参数是类，而类实例方法的隐含调用参数是类的实例，静态方法没有隐含调用参数
class A(object):
    def foo(self, x):
        # 类实例方法
        print('executing foo(%s, %s)' % (self, x))

    @classmethod
    def class_foo(cls, x):
        # 类方法
        print('executing class_foo(%s, %s)' % (cls, x))

    @staticmethod
    def static_foo(x):
        # 静态方法
        print('executing static_foo(%s)' % x)

a = A()
a.foo(1)

a.class_foo(1)
A.class_foo(1)

a.static_foo(1)
A.static_foo(1)