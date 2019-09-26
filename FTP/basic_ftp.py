# File:     ftp.py
# Team:     THE ROMANS->
#           Jonmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  09.25.19
# Usage:    Use python 2.7
#           Example: python ftp.py
# Github:   https://github.com/Jacob-Bordelon/CSC_442/blob/master/FTP/basic_ftp.py
# Descr:    This program connects to an ftp server and grabs information
#           about the files listed in a specified directory. It then
#           isolate the files' permissions and decodes any messages that
#           may be hidden in them, using either a 7-bit or a 10-bit
#           analysismethod.
#====================== IMPORT STATEMENTS ==================================#
import ftplib
#============================== VARIABLES ==================================#
# integer representing bit method to use
METHOD = 10
# ftp server to connect to
HOST = "jeangourd.com"
# port to connect to on server
# leave empty to use default port
PORT = "21"
# username and password needed for login
USER = "anonymous"
PASS = ""
# directory to travel to
DIR = "/" + str(METHOD)
#============================== FUNCTIONS ==================================#
# This function converts a 7-bit binary number into an ASCII character.
# First, it iterates through the string, checking for 1's. If it finds
# a 1, it adds 2 to the power of (bitType=7-1) minus the index to the value
# of the decimal form of the number. Then, this decimal value is convertet
# to an ASCII character using chr(). 
def getASCII(num):
    value = 0
    for index in range(len(num)):
        if(int(num[index])==1):
            value+=(2**(6-index))
    return chr(value)
    
# This functions takes in a permissions string (which contains either d, r,
# w, x, or -) and converts it into a binary number. It does this by
# replacing every instance of - with a 0 and everything else with a 1.
def getBinary(access):
    permissions = ""
    for char in access:
        permissions += ("0" if (char=="-") else "1")
    return permissions
#============================== MAIN PROGRAM ===============================#
# fetch the file listing at the provided directory (DIR), using the given 
# credentials (USER, PASS) from FTP server, HOST at port PORT and store 
# it in the source variable before closing the connection.
source = []
ftp = ftplib.FTP()
# if PORT is not supplied, connect to default
if PORT.isspace or PORT == "":
    ftp.connect(HOST)
else:
    ftp.connect(HOST,PORT)
ftp.login(USER,PASS)
ftp.cwd(DIR)
ftp.retrlines('LIST',source.append)
ftp.close()

# start decoding message hidden in permissions by grabbing the list of
# files, isolating the permissions for each file, and then decoding the
# permissions using getBinary() into a binary string (bin_msg)
bin_msg = ""
for a_file in source:
    bin_msg += str(getBinary(a_file[0:10]))
# With the decoded binary message, generate the covert message and output
# to the terminal. Make sure to shift 3 bits if the 7-bit method is being
# used as we are ignoring the first 3 bits in terms of decoding.
secret = ""
shift = 3 if (METHOD == 7) else 0
for i in range(0,len(bin_msg),shift+7):
    #ignore anything that has any of first 3 bits set
    if((METHOD==7) and ("1" in bin_msg[i:i+3])):
        continue
    secret += getASCII(bin_msg[i+shift:i+shift+7])
print secret
