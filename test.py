# -*- coding: utf-8 -*-
# @File    : test.py
# @Software: PyCharm

def test1(a):
    if a==1:
        test2()
    else:
        pass

def test2(a):
    return Test('1')


class Test():
    def __init__(self,a):
        self.a = a

    def __enter__(self):
        print('enter----')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

    def ttt(self):
        def for_():

for i in range(1,3):
    test1(i)

