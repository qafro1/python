#!/usr/env python
# returns whether the path (dir or file) exists or not with Last modified or last access
import os
import os.path
import time


#Check if files in directory and Last modified
def files(path):
  if os.path.isfile(path):
    return False
  else:
    return "Files in directory. Last modified: %s" % time.ctime(os.path.getmtime(path))

# the time of last access of path.
def atime(path):
    if os.path.getatime(path):
        return "The time of last access of path: %s" % time.ctime(os.path.getatime(path)) + "\n" + path
# if the file does not exist by the numbers of files or is inaccessible
def sizeDir(path):
    if os.path.getsize(path):
         dirs = os.listdir(path)
         if len(dirs) != 0:
           return files(path)
    else:
        return IOError
#source directory of any files
path = "path"
print atime(path)
print sizeDir(path)
