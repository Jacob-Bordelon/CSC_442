#python2, linux OS
import os
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
# fetch the file listing with permission from FTP server
os.system("ls -lh >> files.txt")

# start decoding message hidden in permissions by grabbing
# the list of files, isolating the permissions for each file,
# and then decoding the permissions
bin_msg = ""
source = open('files.txt','r').readlines() 
for line in source:
    attributes = line.split(' ')
    if "total" not in attributes[0]:
        bin_msg += str(getBinary(attributes[0]))

# With the binary message, generate the covert message
# and output to the terminal
secret = ""
# check if 7bit or 10bit so can shift accordingly
shift = 3 if (METHOD == 7) else 0
for i in range(0, len(bin_msg)-10,10):
    # skip if any of first 3 bits is set
    if((METHOD == 7) and ("1" in bin_msg[i:i+3])):
        continue;
    secret += getASCII(bin_msg[i+shift:i+10])
print secret

# file cleanup
os.system("rm files.txt")

