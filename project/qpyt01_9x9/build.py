#*****************************************************************************
#    # #              Name   : build.py
#  #     #            Date   : Apr. 24, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# build.py for qpyt01_9x9 project
#*****************************************************************************
#!/usr/bin/python

import os
import sys

#*****************************************************************************
# Add persional python function
#*****************************************************************************
def printStart():
   print( "Building starting......" )

def print9x9():
   for i in range(1, 10):
      for j in range(1, i + 1):
         print( "%d*%d=%d" % ( i, j, i*j ), end='\t')
      print("\n")

if __name__ == "__main__":
   printStart()
   print9x9()
