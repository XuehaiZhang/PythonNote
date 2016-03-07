#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'


def fact(n):

    '''

    >>> fact(1)
    1
    >>> fact(5)
    120
    >>> fact(0)
    Traceback (most recent call last):
      File "E:\pyclass\7.py", line 22, in <module>
        print( fact(0) )
      File "E:\pyclass\7.py", line 12, in fact
        raise ValueError()
    ValueError

    '''

    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
