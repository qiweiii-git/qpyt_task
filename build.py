#*****************************************************************************
#    # #              Name   : build.py
#  #     #            Date   : Mar. 19, 2020
# #    #  #  #     #  Author : Qiwei Wu
#  #     #  # #  # #  Version: 1.0
#    # #  #    #   #
# build.py
#*****************************************************************************
#!/usr/bin/python

import os
import sys
import time
import shutil
from optparse import OptionParser

#*****************************************************************************
# Add persional python function
#*****************************************************************************
sys.path.append('./code/utils')

import printTools

#*****************************************************************************
# Build setting
#*****************************************************************************
parser = OptionParser()
parser.add_option( "-p", "--project", dest="projectName", help="Build project's name" )
( options, args ) = parser.parse_args()

workPath = os.path.abspath( os.getcwd() ) + "/"
buildPath = workPath + ".build/"
resPath = workPath + ".res/"
logPath = resPath + "build.log"
projectPath = workPath + "project/"
codePath =workPath + "code/"

#*****************************************************************************
# PrintLog
#*****************************************************************************
def printLog( string, color ):
   printTools.printColor( time.asctime( time.localtime( time.time() ) ) + ": " + string, color)
   logFile = open( logPath, 'a' )
   logFile.write( "%s: %s" % ( time.asctime( time.localtime( time.time() ) ), string ) + '\n' )
   logFile.close()

#*****************************************************************************
# Make folder
#*****************************************************************************
def MkdirRes():
   if os.path.exists( resPath ):
      shutil.rmtree( resPath )
      printTools.printColor( "%s is removed" % ( resPath ), 'none' )
   os.makedirs( resPath )
   logFile = open( logPath, 'w' )
   logFile.close()
   printLog( "%s is created" % ( resPath ), 'none' )
   printLog( "Starting......", 'green' )

def MkdirBuild():
   if os.path.exists( buildPath ):
      shutil.rmtree( buildPath )
      printLog( "%s is removed" % ( buildPath ), 'none' )
   os.makedirs( buildPath )
   printLog( "%s is created" % ( buildPath ), 'none' )

#*****************************************************************************
# Build Start
#*****************************************************************************
if __name__ == "__main__":
   MkdirRes()

   if options.projectName is None:
      printLog( "Missing project name, please type '%s -h' for more details" % ( __file__ ), 'red' )
      sys.exit( -1 )
   printLog( "Build Project %s" % ( options.projectName ), 'green' )
   printLog( "Project from %s and building in %s" % ( projectPath, buildPath ), 'green' )

   # build start
   if options.projectName == 'all':
      projectItems = os.listdir( projectPath )
      projectNum = len( projectItems )
   else:
      projectItems[0] = options.projectName
      projectNum = 1

   printLog( "%d projects need to be built" % ( projectNum ), 'none' )

   # build needed project
   for i in range( 0, projectNum ):
      printLog( "No.%d project %s is building now" % ( i, projectItems[i] ), 'yellow' )

      if not os.path.exists( projectPath + projectItems[i] + '/build.py' ):
         printLog( "No build script found", 'red' )
         sys.exit( -1 )
      else:
         os.makedirs( resPath + projectItems[i] )
         os.chdir( projectPath + projectItems[i] )
         os.system( 'python build.py' )
         os.chdir( workPath )
         for path, dirs, files in os.walk( projectPath + projectItems[i], topdown = False ):
            for name in files:
               if not ".py" in name:
                  fileSrcPath = os.path.join( path, name )
                  fileDestPath = os.path.join( resPath + projectItems[i], name )
                  shutil.copy( fileSrcPath, fileDestPath )
                  printLog( "Copping %s into %s" % ( name, resPath + projectItems[i] ), 'yellow' )

   # finish
   printLog( "Finish building Project %s" % ( options.projectName ), 'green' )
