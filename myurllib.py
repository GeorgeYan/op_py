#-*-coding:utf-8-*-
import urllib2
keyword = urllib2.quote('python')
page = urllib2.urlopen("http://www.baidu.com/s?wd="+keyword+"&rsv_spt=1&rsv_iqid=0x932b5bc7000237df&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&inputT=974&rsv_sug4=973&rsv_sug=1")
print page.read()
