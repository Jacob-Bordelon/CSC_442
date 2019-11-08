
# File:     xor.py
# Team:     Johnmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  10.12.19
# Usage:    Use python 2.7
#           Example: python xor.py < ciphertext 
#                    python xor.py < plaintext > ciphertext
# Github:   https://github.com/Jacob-Bordelon/CSC_442.git
# Descr:    This program reads a text file from stdin and a key in the current directory
#           it will compare the binary value of the text and key, xor'ing each binary bit
#           them return the xor'd data to stdout


import sys
from binascii import unhexlify, hexlify
import argparse

parser = argparse.ArgumentParser(prog='xor.py',conflict_handler="resolve")
parser.add_argument("text",metavar="text",nargs="+",help="Add name of text file")
parser.add_argument("key",metavar="key",nargs="+",help="Add name of key file")
args = parser.parse_args()


# this function takes one character as input and returns the binary equivalent as a string
def binary(byte):
    return "{0:08b}".format(int(hex(ord(byte)),16))

# the toAscii function takes a string of binary bytes and converts it to character strings
# it then returns the string as a bytearray
def toAscii(byte):
    b = ""
    i=0
    while i < len(byte):
        b+=chr(int(byte[i:i+8],2))
        i+=8
    return bytearray(b)

# the xor program takes two binary strings as the parameters and returns the xor'd value 
# the strings can be any length
def xor(t,k):
    h = ""
    for i in range(len(t)):
        h+=str(int(t[i])^int(k[i]))
    return h

# text takes either the ciphertext or plaintext as the parameter from stdin
# key must be a file in the current directory
# NOTE: use 'cp [name of key] key' to change the key you want to use
text = open(args.text[0],'rb').read() if args.text != None else sys.stdin.read()
key = open(args.key[0],'rb').read() if args.key != None else open('key','rb').read()

# convert both files from character files to binary files
# the ''.join() combines all the values of the list
# NOTE: if either the key or text file is already a binary file, just comment that like out and write k=key or t = text
t = ''.join([binary(i) for i in text])
k = ''.join([binary(i) for i in key])

#xor the two converted and joined binary strings
x = xor(t,k)

# convert the xor'd binary string to an array
a = toAscii(x)

# send the converted ascii key to standard output
sys.stdout.write(a)





   

