#-*-coding:utf-8-*-
import sys
import web
db = web.database(dbn='mysql', db='big-back', user='root', pw='')
tb = 'users'

def get_by_id(id):
    s = db.select(tb, where="id=$id", vars=locals())
    if not s:
        return False
    return s[0]
if __name__=="__main__":
    resultValue=get_by_id(2)
    print resultValue
