# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:16:27 2016
爬取糗事百科的段子
@author: liuy
"""

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' + \
             'AppleWebKit/537.36 (KHTML, like Gecko)'   + \
             'Chrome/53.0.2785.101'                     + \
             'Safari/537.36'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    #print response.read()
    content = response.read().decode('utf-8')
    #pattern = re.compile('.*?(.*?).*?.*?(.*?).*?.*?class=”number”>(.*?)',re.S)  
    pattern =re.compile(r' class=')    
    #pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+ \
    #                     'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[3],item[4]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

