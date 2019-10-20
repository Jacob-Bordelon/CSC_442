#python2, linux OS
import os
#variable to determine whether to do 7 or 10
METHOD = 7 
# fetch all the files in the directory
os.system("ls -alh >> files.txt")
# fetch the file listing with permission from FTP server
with open('files.txt','r') as f:
    data = f.read()
    print data
#isolate and decode permissions
# if 7 bit, filter out any of first three bits set
# utilize all 10
# generate and output covert message
