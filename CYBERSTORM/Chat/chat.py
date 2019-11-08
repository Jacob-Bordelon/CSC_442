import socket
import sys
from time import time
from binascii import unhexlify
import argparse
import os


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

def collect(L):
    collection = list(set(L))
    new = []
    for i in collection:
        new.append((i,L.count(i)))
    return sorted(new,key=lambda new: new[1])


ip = "192.168.1.19"
port = 31337
ONE = 0.1
ZERO = 0.025


parser = argparse.ArgumentParser(prog='chat.py',conflict_handler="resolve")
parser.add_argument('-ip','--addr',default = ip, help="IP Address")
parser.add_argument('-p','--port',type=int,default = port,help="Port Number")
parser.add_argument('-o','--one',default = ONE, help="Value for One")
parser.add_argument('-z','--zero',default = ZERO,help="Value for Zero")
parser.add_argument('-t','--times',help="Show all unique times", action='store_true')
args = parser.parse_args()





times = []
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.addr,args.port))

    data = s.recv(4096)
    while data.rstrip('\n') != "EOF":
        sys.stdout.write(data)
        sys.stdout.flush()

        t0 = time()
        data = s.recv(4096)
        t1 = time()

        times.append(round(t1-t0, 3))
    s.close()
except Exception as e:
    print e

if args.times == True:
    print "Time(sec)\t\tInstances"
    for i in collect(times)[::-1]:
        print "\t{}\t{}".format(i[0],i[1])
    quit()

covert_bin = ""
for i in times:
    if i >= ONE:
        covert_bin+="1"
    else:
        covert_bin+="0"


message = toASCII(covert_bin)
print "Covert message = " + message











