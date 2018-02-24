#-*-coding:utf-8-*-
import sys
def Main():
    M=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    col2=[row[1] for row in M]
    print col2
    col3=[row[1]+1 for row in M]
    print col3
    colfilter=[row[1] for row in M if row[1]%2==0]
    print colfilter
if __name__=="__main__":
    Main()
