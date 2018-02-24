#-*-coding:utf-8-*-
import sys
import os
def Main():
    sys.stdout.write("Hello world! george\n")
    i=10
    j="啦啦"
    print str(i)+j
    print os.listdir(".")
    print "Hello world from %s" % __name__
if __name__=="__main__":
    Main()
