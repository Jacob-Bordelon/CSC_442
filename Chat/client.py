from time import time
from binascii import unhexlify
import socket
import sys

ip = 'jeangourd.com'
port = 31337
ONE = 0.1
ZERO = 0.025
threshold = 0.015
# not usually more than 2*threshold
# most filled: zero, exact, zero+2->one-2, zero+-1, less, add/minus1

def toASCII(num):
    msg = ""
    i = 0
    while (i < len(num)):
        # process one byte at a time
        b = covert_bin[i:i+8]
        # convert to ASCII
        n = int("0b{}".format(b),2)
        try:
            msg += unhexlify("{0:x}".format(n))
        except TypeError:
            msg += "?"
        # stop at "EOF"
        i += 8
    return msg

covert_bin = ""
try:
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the chat server
    s.connect((ip,port))
    print "[connected to server]\n..."
    # time delays between characters received;
    data = s.recv(4096)
    while (data.rstrip("\n") != "EOF"):
        sys.stdout.write(data)
        sys.stdout.flush()
        t0 = time()
        data = s.recv(4096)
        t1 = time()
        delta = round(t1-t0, 3)
        if ((delta >= (ZERO+2*threshold)) and (delta <= (ONE + 2*threshold))):
            covert_bin += "1"
        else:
            covert_bin += "0"
    s.close()
    print "...\n[disconnect from server]\n"
except Exception as e:
    print e
message = toASCII(covert_bin[:len(covert_bin)-32])
print "Covert message = " + message

####################################################3
# connect to server
# receive an overt message, and display as transmitted
# time delays between characters received
# determine end of covert message to disconnect
# output cover message (to stdout, which ends in EOF)
