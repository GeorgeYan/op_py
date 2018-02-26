#-*-coding:utf-8-*-
import memcache
mc = memcache.Client(['127.0.0.1:11211'],debug=True)
mc.set('name','lala',20)
print mc.get('name')
