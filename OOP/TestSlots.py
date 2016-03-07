#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


class Student(object):
    pass


# 给实例绑定一个属性
s = Student()
s.name = 'Mike'
print(s.name)


# 给实例绑定一个方法
def set_age(self, age):
    self.age = age


from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


# 给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score

# 这个地方实际上是添加了类属性而已 根据下面的输出可以得出结论
Student.set_score = MethodType(set_score, Student)
s.set_score(100)
print(s.score)
print(Student.score)
s2 = Student()
s2.set_score(99)
print(s2.score)
print(s.score)
print(Student.score)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')

print(Student.__slots__)
s = Student()
s.name = 'name'
s.age = 'age'
# s.n = 'n' # Error
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__!!!
# someone君的理解
# slots限制类实例添加属性，类可以动态添加属性，类中添加以后，类实例中可以引用。
