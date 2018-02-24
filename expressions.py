#-*-coding:utf-8-*-
import sys
def func():
    # 9*9 expressions
    #s=[(x,y,x*y) for x in range(1,10) for y in range(1,10) if x>=y]

    x=1
    y=2
    m=3
    n=4
    sum=lambda x,y:x+y
    print sum
    sub=lambda m,n:m-n
    print sub
    return sum(x,y)*sub(m,n)
if __name__ == "__main__":
    print func()


