#/usr/bin/env pyhton
#search for a string in text files?
import mmap
import re
#source directory of the file
src = open('path')
#target directory of the result file
dst = open('path','w')
#search string
search = ('csv.ready')
s = mmap.mmap(src.fileno(),0,access=mmap.ACCESS_READ)
if s.find(search) != -1:
  print(True)
  dst.write('The search string is found in the file')
else:
  print(False)
  dst.write('The search string is not found in the file')
dst.close()
