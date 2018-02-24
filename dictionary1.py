#-*-coding:utf-8-*-
import sys
def Main():
    D={'food':'spam','quantity':4,'color':'pink'}
    print D['food']
    D['quantity']+=1
    print D
    #另外一种定义字典的方法
    D={}
    D['name']='Bob'
    D['job']='dev'
    D['age']=40
    print D
    #使用键值,进行排序
    D={'a':1,'b':2,'c':3}
    print D
    Ks=D.keys()
    print Ks
    Ks.sort()
    print Ks
    for key in Ks:
        print key,'=>',D[key]
    for key in sorted(D):
        print key,'=>',D[key] #迭代与优化
    squares=[x ** 2 for x in [1,2,3,4,5]]
    print squares
    #与以下代码是等效的
    squares=[]
    for x in [1,2,3,4,5]:
        squares.append(x**2)
if __name__=="__main__":
    Main()
