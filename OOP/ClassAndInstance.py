#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


class Student(object):
    pass


bart = Student()
print(Student)
print(bart)

bart.name = 'Bart Simpson'
print(bart.name)


class Student(object):
    # 和普通的函数相比，在类中定义的函数只有一点不同，
    # 就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.get_grade())


class Student(object):
    def __init__(self, name, score):
        # 实例的变量名如果以__开头，就变成了一个私有变量（private）
        # 只有内部可以访问，外部不能访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

bart = Student('Bart Simpson', 98)
bart.print_score()
# print(bart.__name) 报错！

# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
# 这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当
# 你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，
# 仍然可以通过_Student__name来访问__name变量：
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
