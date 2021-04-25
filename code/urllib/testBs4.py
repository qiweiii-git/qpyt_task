#*****************************************************************************
#    # #              Name   : testBs4.py
#  #     #            Date   : Apr. 25, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# test for BS4
#*****************************************************************************
#!/usr/bin/python
# coding=utf-8

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re

def testBs4():
   # Get baidu.html
   response = urllib.request.urlopen("http://www.baidu.com")
   htmlData = response.read().decode('utf-8')
   htmlFile = open('./baidu.html', 'w')
   htmlFile.write(htmlData)
   htmlFile.close()
   # Decode
   file = open('./baidu.html', 'rb')
   htmlData = file.read()
   bs = BeautifulSoup(htmlData, 'html.parser')
   #print(bs.title)
   #print(bs.title.string)
   #print(bs.a.attrs)
   list = bs.find_all('a')
   #print(list)
   list = bs.find_all(re.compile('a'))
   #print(list)
