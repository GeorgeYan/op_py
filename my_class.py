#-*-coding:utf-8-*-
import sys

class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def getName(self):
        format="my name is %s my age is %d"%(self.__name,self.__age)
        print format
    def __del__(self):
        print "del"
if __name__=="__main__":
    student=Student("chu",35)
    student.getName()
