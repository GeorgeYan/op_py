#-*-coding:utf-8-*-
import sys
def Main():
    #使用 if 替代
    x='4'
    print "OK"
    if x=='1':
        print 'one'
    elif x=='2':
        print 'two'
    else:
        print 'nothing!'
        #使用 dict
    numtrans={
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four'}
    try:
        print numtrans[x]
    except KeyError:
        print 'nothing!'
if __name__=="__main__": Main()
