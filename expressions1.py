#-*-coding:utf-8-*-
import sys
def arithmetic(x=1,y=1,operator="+"):
    result={
            "+":x+y,
            "-":x-y,
            "*":x*y,
            "/":x/y
            }
    return result.get(operator)
if __name__=="__main__":
    print arithmetic(1,2)
    print arithmetic(1,2,"-")
    print arithmetic(2,25,"*")
