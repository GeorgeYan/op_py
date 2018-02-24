#-*-coding:utf-8-*-
import sys
import re
if __name__=="__main__":
    #使用^与$的使用方法
    s="HELLO WORLD"
    #匹配 hello 开始的字符串,由于变量 s 中的 HELLO 是大写的所以匹配失败
    print re.findall(r"^hello",s)
    #re.I 表示时忽略大小写
    print re.findall(r"^hello",s,re.I)
    #$的意思是匹配尾部
    print re.findall(r"WORLD$",s)
    #匹配每个英文单词\b 用于分割单词
    print re.findall(r"\b\w+\b",s)
