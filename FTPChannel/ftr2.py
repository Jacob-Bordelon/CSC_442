#python3
from pathlib import Path
#variable to determine whether to do 7 or 10
METHOD = 7 
# file to contain the list of files and their permissions
files = open('files.txt', 'w')
# fetch all the files in the directory
# fetch the file listing with permission from FTP server
filesList = open('files.txt','w');
#isolate and decode permissions
# if 7 bit, filter out any of first three bits set
# utilize all 10
# generate and output covert message


#========================
# with open('files.txt','r') as f: data = f.read()
# with open('files.txt','w') as f: data = ''; f.write(data);
# use os.scandir('') or pathlib.Path()

# permissions
# OWNER READ, WRITE, EXECUTE
# GROUP
# USERS