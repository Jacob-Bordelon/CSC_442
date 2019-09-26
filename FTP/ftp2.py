#python2, linux OS

# if ran normally, it will run it as METHOD = 7
# the arguments in brackets are optional
# Usage: python ftp2.py [METHOD] [Server] [User] [Password]
import os
from ftplib import FTP
import sys

#variable to determine whether to do 7 or 10
METHOD = 7

# this function converts a binary number
# into a 7-bit ASCII character
def getASCII(num):
    value = 0
    for index in range(len(num)):
        if(int(num[index])==1):
            value+=(2**(6-index))
    return chr(value)
    
# this function converts the permissions string
# into a binary number
def getBinary(x):
    permissions = ""
    for i in x:
        permissions += ("0" if (i=="-") else "1")
    return permissions
######################################################################

def getFTP(method,server,user,password):
    # fetch the file listing with permission from FTP server
    source = []
    ftp = FTP(server)
    ftp.login(user,password)
    ftp.cwd("/"+str(method))
    ftp.retrlines('LIST',source.append)
    ftp.close()
    

    # start decoding message hidden in permissions by grabbing
    # the list of files, isolating the permissions for each file,
    # and then decoding the permissions
    bin_msg = ""
    for a_file in source:
        bin_msg += str(getBinary(a_file[0:10]))
    print "Length = ",len(bin_msg)

    # With the binary message, generate the covert message
    # and output to the terminal
    secret = ""
    # check if 7bit or 10bit so can shift accordingly
    shift = 3 if (method == 7) else 0
    for i in range(0,len(bin_msg),shift+7):
        if((method==7) and ("1" in bin_msg[i:i+3])):
            continue
        secret += getASCII(bin_msg[i+shift:i+shift+7])
    return secret

# Base configuraton
args = {1:METHOD,2:'jeangourd.com',3:'anonymous',4:''}

# if system arguments exists, append them to the dictionary
for i in range(1,len(sys.argv)):
    args[i] = sys.argv[i]

# Stdout 
print getFTP(int(args[1]),args[2],args[3],args[4])
