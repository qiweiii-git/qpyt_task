#*****************************************************************************
#    # #              Name   : UrlibCtrl.py
#  #     #            Date   : Apr. 25, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# Urllib control
#*****************************************************************************
#!/usr/bin/python
# coding=utf-8

import urllib.request
import urllib.parse
import os
import shutil

def UrllibGet(url):
   # Ping URL
   # User Agent should be set for douban
   data = bytes(urllib.parse.urlencode({'1':'2'}), encoding="utf-8")
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
   }
   try:
      req = urllib.request.Request(url=url, data=data, headers=headers, method="GET")
      response = urllib.request.urlopen(req, timeout=3)
   except urllib.error.URLError as error:
      print("time out when accessing %s!" %(url))
   htmlData = response.read().decode('utf-8')
   return htmlData

def UrllibGetDataFromDouban():
   urlBase = "https://movie.douban.com/top250"
   for i in range(0, 10):
      url = urlBase + '?start=' + '%d' % (i * 25)
      htmlData = UrllibGet(url)
      fileName = './douban250Page' + '%d' % (i) + '.html'
      htmlFile = open(fileName, 'w')
      htmlFile.write(htmlData)
      htmlFile.close()
