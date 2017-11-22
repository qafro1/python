#!usr/bin/python
#This python script archive files gz in a source directory to a target directory as backup

import tarfile
import glob
import os

#input the source directory
src = "path"
#archive name of the target path directory
archive_name = "path"
# write to latest_files.tar.gz
with tarfile.open(archive_name, "w:gz") as tar:
  for name in glob.glob(os.path.join(src,"*")):
      tar.add(name,arcname=os.path.basename(name),exclude=os.path.isdir)
