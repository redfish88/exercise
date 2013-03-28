#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:urllib2-header.py
 
import urllib2
import urllib
import sys
 
#抓取网页内容-发送报头-1
url= "http://www.phpno.com"
send_headers = {
    'Host':'www.phpno.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection':'keep-alive'
}
 
req = urllib2.Request(url,headers=send_headers)
r  = urllib2.urlopen(req)
 
html = r.read()                             #返回网页内容
receive_header = r.info()                   #返回的报头信息
 
# sys.getfilesystemencoding() 
html = html.decode('utf-8','replace').encode(sys.getfilesystemencoding())   #转码:避免输出出现乱码 
 
print receive_header
# print '####################################'
print html

doubleball = 'http://www.baidu.com/s?wd=%E5%8F%8C%E8%89%B2%E7%90%83'
html = urllib.urlopen(doubleball).read()
print html
