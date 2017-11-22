#!usr/bin/python
#This python script will archive timestamp files gz in a source directory to a target directory as backup

import tarfile
import glob
import os
from datetime import datetime
import time

#input the source directory
src = "path"
#archive name of the target path directory
archive_name = "path"
#timestamp archive_name
archive_name_time = datetime.now().strftime(archive_name + '_%H_%M_%d_%m_%Y.gz')
# write to latest_files.tar.gz
with tarfile.open(archive_name_time, "w:gz") as tar:
  for name in glob.glob(os.path.join(src,"*")):
      tar.add(name,arcname=os.path.basename(name),exclude=os.path.isdir)
