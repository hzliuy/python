# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 16:34:14 2016

@author: liuy
"""

import urllib
import urllib2
import cookielib
import re
 
 #模拟登陆bitcenter
class bidcenter:
 
    def __init__(self):
        self.loginUrl = 'http://sso.bidcenter.com.cn/validate/'
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'stuid':'13777804195',
            'pwd':'813428@hz'
         })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
 
    def getPage(self):
        request  = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        #打印登录内容
        print result.read().decode('utf8')
 
 
sdu = bidcenter()
sdu.getPage()