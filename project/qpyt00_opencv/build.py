#*****************************************************************************
#    # #              Name   : build.py
#  #     #            Date   : Mar. 20, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# build.py for qpyt00_opencv project
#*****************************************************************************
#!/usr/bin/python

import os
import sys

#*****************************************************************************
# Add persional python function
#*****************************************************************************
sys.path.append('../../code/utils')
sys.path.append('../../code/opencv')

import printTools
import testPattern

#*****************************************************************************
# Add persional python function
#*****************************************************************************
def printStart():
   print( "Building starting......" )

def testPatternGen():
   testPattern.gen()

if __name__ == "__main__":
   printStart()
   testPatternGen()
   