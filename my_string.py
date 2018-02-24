#-*-coding:utf-8-*-
import sys
if __name__=="__main__":
    #使用字符串截取子串
    word="world Hello"
    print word[0]
    #string[start:end:step]
    #从 0 开始截取三个
    print word[0:3]
    #从0开始
    print word[0::2]
    #使用 split()获取子串
    sentence="Bob Said:1,2,3,4"
    print "使用空格取子串:",sentence.split()
    print "使用逗号取子串:",sentence.split(",")
    print "使用两个逗号取子串:",sentence.split(",",2)
