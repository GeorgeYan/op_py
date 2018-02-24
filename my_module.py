#-*-coding:utf-8-*-

import sys
import define

def Main():
    print define.myvar
    print dir(define)
    print define.__file__
if __name__=="__main__":
    Main()
    print __name__
    print __doc__
    print __file__
    print __package__
