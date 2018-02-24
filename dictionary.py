#-*-coding:utf-8-*-
import sys
if __name__=="__main__":
    #字典的添加、删除、修改操作
    dict={"a":"apple","b":"banana","g":"grape","o":"orange"}
    dict["w"]="watermelon"
    print dict
    del(dict["a"])
    print dict
    print dict.pop("b")
    #dict.clear()
    #print dict #字典的遍历
    for k in dict:
        print "dict[%s]="%k,dict[k]
