#-*-coding:utf-8-*-
import sys
def Main():
    test=[0]
    print type(test)
    test=[0,]
    print type(test)
    test=(0,)
    print type(test)
    test=(0)
    print type(test)
    test=0,
    print type(test)
    a=1
    b=2
    a,b=b,a
    print a,b
if __name__=="__main__":
    Main()
