#*****************************************************************************
#    # #              Name   : build.py
#  #     #            Date   : Apr. 24, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# build.py for qpyt02_douban250 project
#*****************************************************************************
#!/usr/bin/python
# coding=utf-8

import os
import sys
from bs4 import BeautifulSoup
import re
import urllib
import xlwt
import sqlite3

#*****************************************************************************
# Add persional python path
#*****************************************************************************
sys.path.append('../../code/urllib')

import testBs4
import testUrllib
import UrllibCtrl

#*****************************************************************************
# Add persional python function
#*****************************************************************************
def printStart():
   print( "Building starting......" )

if __name__ == "__main__":
   printStart()
   testUrllib.testUrllib()
   testBs4.testBs4()
   UrllibCtrl.UrllibGetDataFromDouban()
