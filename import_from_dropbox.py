# Script Name	: import_from_dropbox.py
# Author			: Craig Richards
# Created			: 1st July 2016
# Last Modified	: 
# Version			: 1.0

# Modifications	:

# Description		: This will download all the files from Dropbox into Pythonista

import dropbox
from dropboxlogin import get_client
import os

dropbox_client = get_client()
path='My_Backups/Pythonista'
downloads=dropbox_client.metadata(path)
files=[]
for item in downloads['contents']:
   files=(item['path'])
   print files
   download=dropbox_client.get_file_and_metadata(files)
   pyfile=os.path.basename(files)
   print pyfile
   out=open(pyfile,'w')
   download,metadata=dropbox_client.get_file_and_metadata(files)
   out.write(download.read())
   out.close()
   print files
