# File:     client.py
# Team:     THE ROMANS->
#           Jonmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  10.09.19
# Usage:    Use python 2.7
#           Example: python client.py
# Github:   https://github.com/Jacob-Bordelon/CSC_442/blob/master/FTP/ftp.py
# Descr:    This program connects to a chat server, receives an overt message,
#           and displays it as it is being received to standard output. As the
#           message is received, the delays between characters is calculated
#           and used to generate a binary code that contains a covert message.
#           After the overt message ends, the program disconnects from the
#           chat server and the covert message is converted to ASCII and
#           displayed on standard output. 
#====================== IMPORT STATEMENTS ==================================#
from time import time
from binascii import unhexlify
import socket
import sys
#============================== VARIABLES ==================================#
# chat server to be connected to
ip = 'jeangourd.com'
# the port on the server to connect to
port = 31337
# the first time delay in characters
ZERO = 0.025
# the second time delay in characters
ONE = 0.1
# the covert binary message
covert_bin = ""
#============================== FUNCTIONS ==================================#
# This function converts an 8-bit binary number into an ASCII character one
# byte at a time. First, it grabs a byteiterates through the string, checking for 1's. If it finds
# a 1, it adds 2 to the power of (bitType=7-1) minus the index to the value
# of the decimal form of the number. Then, this decimal value is convertet
# to an ASCII character using chr(). 
def toASCII(num):
    msg = ""
    i = 0
    while (i < len(num)):
        # process one byte at a time
        b = num[i:i+8]
        # convert to ASCII
        n = int("0b{}".format(b),2)
        try:
            msg += unhexlify("{0:x}".format(n))
        except TypeError:
            msg += "?"
        # stop at "EOF"
        i += 8
    return msg
#============================== MAIN PROGRAM ===============================#
try:
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the chat server at the provided ip address and port
    s.connect((ip,port))
    # receive data at 
    data = s.recv(4096)
    # receive an overt message and display as transmitted
    # as long as "EOF" is not seen
    while (data.rstrip("\n") != "EOF"):
        # write to standared output
        sys.stdout.write(data)
        # remove any buffers.
        sys.stdout.flush()
        # figure out time delays between characters
        t0 = time()
        data = s.recv(4096)
        t1 = time()
        delta = round(t1-t0, 3)
        # if the time delay matches ONE, add "1" to binary message
        # otherwise, add "0"
        if (delta >= ONE):
            covert_bin += "1"
        else:
            covert_bin += "0"
    # close the connection to the server
    s.close()
except Exception as e:
    print e

# convert the received binary message to ASCII and output the decoded message
message = toASCII(covert_bin)
print "Covert message = " + message
