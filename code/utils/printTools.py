#*****************************************************************************
#    # #              Name   : printTools.py
#  #     #            Date   : Mar. 19, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# printTools.py
#*****************************************************************************
#!/usr/bin/python

def printColor ( string, color ):
   if 'red' in color:
      print( "\033[40;31m{}\033[0m".format( string ) )
   elif 'cyan' in color:
      print( "\033[40;36m{}\033[0m".format( string ) )
   elif 'green' in color:
      print( "\033[40;32m{}\033[0m".format( string ) )
   elif 'blue' in color:
      print( "\033[40;34m{}\033[0m".format( string ) )
   elif 'yellow' in color:
      print( "\033[40;33m{}\033[0m".format( string ) )
   elif 'lavender' in color:
      print( "\033[40;35m{}\033[0m".format( string ) )
   elif 'gray' in color:
      print( "\033[40;30m{}\033[0m".format( string ) )
   else:
      print( string )
