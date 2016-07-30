# Script Name	: backup_to_dropbox.py
# Author			: Craig Richards
# Created			: 1st July 2016
# Last Modified	: 
# Version			: 1.0

# Modifications	:

# Description		: This backups all my Pythonista scripts into Dropbox

import os
import dropbox
from dropboxlogin import get_client

dropbox_client = get_client()

for file in os.listdir('.'):
	if file.endswith(".py"):
		print file
		f=open(file,'r')
		dropbox_client.put_file('My_Backups/Pythonista/'+file,f,overwrite=True)
		f.close()
		