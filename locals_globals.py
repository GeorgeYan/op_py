#-*-coding:utf-8-*-
from __future__ import unicode_literals
from sys import *
def test(arg):
    z=1
    print locals()

test(5)
test('啦啦啦')
print globals()
