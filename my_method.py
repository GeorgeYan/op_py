#-*-coding:utf-8-*-
import sys
class A:
    def prt(self):
        print "my name is A"
    def reprt(self):
        A.prt(self)
    @staticmethod
    def prt2():
        print "I'm static method"
if __name__=="__main__":
    a=A()
    a.prt()
    a.reprt()
    A.prt2()
