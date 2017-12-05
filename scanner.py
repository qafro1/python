#!/usr/env python
# returns whether the path (dir or file) exists or not with Last modified or last access
import os
import os.path
import time
import glob

#Check if files in directory and Last modified or is inaccessible
def files(path):
  if  glob.glob(filename):
    return " Files in directory.\n" + "Last modified: %s" % time.ctime(os.path.getmtime(path))
  else:
    return "\n" + "NO files"

# the time of last access of path.
def atime(path):
    if os.path.getatime(path):
        return "The time of last access of path: %s" % time.ctime(os.path.getatime(path)) + " \n" + path

#Open log file
file = open('path','w')
#source directory of any files
path = 'path'
filename = 'path/*.gz'
file.write(atime(path))
file.write(files(path))
file.close()
