#-*-coding:utf-8-*-
import sys
class A:
    # static variable
    y=2
    def __init__(self):
        # public variable
        self.x=1
        # private variable
        self.__z=1
if __name__=="__main__":
    a=A()
    # print public variable
    print a.x
    # print static variable
    print A.y
    # print private variable occur error
    print a.__z
