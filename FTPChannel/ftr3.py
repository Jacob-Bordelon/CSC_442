#python2, universal
import os
from sys import platform
#variable to determine whether to do 7 or 10
METHOD = 7
# fetch all the files in the directory
if "win" in platform:
    cmd = "dir > files.txt"
elif "linux" in platform:
    cmd = "ls -lh > files.txt"
else:
    cmd = "ls -l > files.txt"
os.system(cmd)
# fetch the file listing with permission from FTP server
with open('files.txt','r') as f:
    data = f.read()
    print data
#isolate and decode permissions
# if 7 bit, filter out any of first three bits set
# utilize all 10
# generate and output covert message


#========================
# with open('files.txt','r') as f: data = f.read()
# with open('files.txt','w') as f: data = ''; f.write(data);
# use os.scandir('') or pathlib.Path()