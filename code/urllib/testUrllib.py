#*****************************************************************************
#    # #              Name   : testUrllib.py
#  #     #            Date   : Apr. 24, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# test for Urllib
#*****************************************************************************
#!/usr/bin/python
# coding=utf-8

import urllib.request
import urllib.parse

def testUrllib():
   # Get request
   response = urllib.request.urlopen("http://www.baidu.com")
   htmlData = response.read().decode('utf-8')
   #print(htmlData)
   htmlFile = open('./testUrllibGet.html', 'w')
   htmlFile.write(htmlData)
   htmlFile.close()

   # Post request - User login
   # Data is require
   data = bytes(urllib.parse.urlencode({'1':'2'}), encoding="utf-8")
   response = urllib.request.urlopen("http://httpbin.org/post", data=data)
   htmlData = response.read().decode('utf-8')
   #print(htmlData)
   htmlFile = open('./testUrllibPost.html', 'w')
   htmlFile.write(htmlData)
   htmlFile.close()

   # Ping douban(douban will know we are urllib)
   # User Agent should be set for douban
   url = "https://movie.douban.com/top250"
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
   }
   req = urllib.request.Request(url=url, data=data, headers=headers, method="GET")
   response = urllib.request.urlopen(req)
   htmlData = response.read().decode('utf-8')
   htmlFile = open('./testUrllibHeaders.html', 'w')
   htmlFile.write(htmlData)
   htmlFile.close()
