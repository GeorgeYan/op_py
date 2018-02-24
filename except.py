#-*-coding:utf-8-*-
import sys
def Main():
    try:
        f=open('firstpython.py')
        s=f.readline()
        print s
    except IOError,(errno,strerror):
        print "I/O error(%s):%s" %(errno,strerror)
    except ValueError:
        print "Could not convert data to an integer"
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise
    finally:
        f.close()
if __name__=="__main__":
    Main()
