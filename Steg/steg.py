# File:     steg.py
# Team:     THE ROMANS->
#           Jonmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  10.22.19
# Usage:    Use python 2.7
#           Example: python steg.py [--help] [-b] [-B] [-s] [-r] [-o OFFSET] [-i INTERVAL]
#               [-w WRAPPER_FILE] [-h HIDDEN_FILE]
#           Note: -b and -B should not be used at the same time and both INTERVAL
#                 and HIDDEN_FILE are optional paramets
#           Help: python steg.py --help
# Github:   https://github.com/Jacob-Bordelon/CSC_442/blob/master/Steg/steg.py
# Descr:    This program can use either bit method or byte method of steganography
#           to either store or read hidden files or messages inside of a bitmap file.
#=================================== IMPORT STATEMENTS ===================================#
from sys import stdin, stdout
import argparse
from math import floor
#======================================= VARIABLES =======================================#
# Sentinal is used to indicate the end of the message/hidden file
sentinal = "0x0 0xff 0x0 0x0 0xff 0x0" # change this value if the sentinal changes 
# Grab terminal parameters as flags
parser = argparse.ArgumentParser(prog='steg.py',conflict_handler="resolve")
parser.add_argument("-b","--bit", help="Use bit method",action='store_true')
parser.add_argument("-B","--byte", help="Use byte method", action="store_true")
parser.add_argument("-s","--store", help="Store (and hide) data", action="store_true")
parser.add_argument("-r","--retrieve", help="Retrieve hidden data", action="store_true")
parser.add_argument("-o","--offset",default=0,help="Set offset to <val>",type=int)
parser.add_argument("-i","--interval",default=1,help=" Set interval to <val>",type=int)
parser.add_argument("-w","--wrapper_file",help="Set wrapper file to <val>")
parser.add_argument("-h","--hidden_file",help="Set hidden file to <val>")
args = parser.parse_args()
#======================================== CLASSES ========================================#
# check and organize parameters 
class params:
    # Constructor for params
    # Given a set of arguments and a sentinal, extract the relevant data and assign to
    # the correct fields in the class. If one of the files can't be found, the program
    # will exit.
    def __init__(self,args,sentinal):
        self.bitMethod = '-b' if args.bit == True else '-B'
        self.dataMethod = '-s' if args.store == True else "-r"
        self.interval = args.interval
        self.offset = int(args.offset)
        try:
            self.wrapper = bytearray(open(args.wrapper_file,'rb').read()) if args.wrapper_file != None else bytearray()
        except IOError:
            print "Wrapper file: \""+args.wrapper_file+"\" not found."
            exit()
        try:
            self.hidden = bytearray(open(args.hidden_file,'rb').read()) if args.hidden_file != None else bytearray()
        except IOError:
            print "Hidden file: \""+args.hidden_file+"\" not found."
            exit()
        self.sentinal = sentinal.split(' ')
    
    # Calculate the best interval given a wrapper and hidden file
    def calculateInterval(self):
        return floor((len(self.wrapper)-self.offset)/(len(self.hidden)+len(self.sentinal)))

    # return the minimum size a wrapper would need to be to house the given hidden input file
    def minWrapperSize(self):
        return len(self.hidden)*self.interval + self.offset

    # return the maximum size hidden file a wrapper could hold
    def maxHiddenSize(self):
        return floor((len(self.wrapper) - self.offset - len(self.sentinal))/self.interval)
#======================================== METHODS ========================================#
#  This method extracts a hidden message or file from a file using the Byte Method
def byteExtraction(File):
    o = File.offset # how far down to start looking
    I = File.interval # iterations to look at
    S = File.sentinal
    H = File.hidden
    W = File.wrapper

    # only continue if the offset is less than the length
    # of the wrapper file
    while o < len(W):
        # get the byte at the offset
        b = W[o]
        # if the byte is not in the the sentinal, added it
        # to the hidden file
        if b not in S:
            H+=chr(b)
        else:
        	sample = bytearray(len(S))
        	start = o
        	for k in range(0, len(S)):
        		sample[k] = W[start]
        		start+=I        	
        	if(sample == S): # if the two bytearrays equal, it's done
        		break
        	else:
        		H+=chr(b)
        # increase the offset
        o+=I
    # output the hidden file
    stdout.write(H)
    
#  This method stores a hidden message or file into a file using the Byte Method
def byteStorage(File):
    o = File.offset
    I = File.interval
    S = [int(i,16) for i in File.sentinal]
    H = File.hidden
    W = File.wrapper

    # input in the Hidden bytes at the offset
    i=0
    while i < len(H):
        W[o] = H[i]
        o += I # increase the offset
        i+=1

    i=0
    # input in the sentinal
    while i < len(S):
        W[o] = S[i]
        o += I #increase the offset
        i +=1
    # output the wrapper file
    stdout.write(W)

#  This method extracts a hidden message or file from a file using the Bit Method
def bitExtraction(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden
    W = File.wrapper

    # only continue if the offset is less than the length of the wrapper file
    while o < len(W):
        b = 0
        # extract the data bit-by-bit, grabbing the least significant bit
        for j in range(8):  
            # this break check is needed incase the offset variable 
            # is greater than the list of bytes
            if o >= len(W):
                break
            b |= (W[o] & 1)
            if j < 7:
                b = (b<<1) & (2**8-1)
                o+=I
        # if we haven't encountered the sentinal, add it to the hidden file
        if b not in S:
            H += bytearray(chr(b))
        # increase the offset
        o+=I
    # output the hidden file
    stdout.write(H)
    
#  This method stores a hidden message or file into a file using the Bit Method
def bitStorage(File):
    o = File.offset
    I = File.interval
    S = [int(i,16) for i in File.sentinal]
    H = File.hidden
    W = File.wrapper

    # input in the hidden bits, bit-by-bit
    i = 0
    while i < len(H):
        # grab the most significant bits
        for j in range(8):
            W[o] &= 11111110
            W[o] |= ((H[i] & 10000000) >> 7)
            H[i] = (H[i] << 1) & (2**8-1)
            o+=I
        i+=1
    
    # input in the sentinal bits
    i = 0
    while i < len(S):
        for j in range(8):
            W[o] &= 11111110
            W[o] |= ((S[i] & 10000000) >> 7)
            S[i] = (S[i] << 1) & (2**8-1)
            o+=I
        i+=1
    # output the wrapper file
    stdout.write(W)

#======================================== MAIN PROGRAM ========================================#
if __name__ == "__main__":
    # first, create a params instance to organize data given from the flags
    a = params(args,sentinal) 
    # then using the bitMethod and Datamethod, determine which one you're using
    # and call that particular function
    if a.bitMethod == "-b": # Bit method
        if a.dataMethod == "-s":
            bitStorage(a)   # Store
        elif a.dataMethod == "-r":
            bitExtraction(a)    #Extract
    elif a.bitMethod == "-B":   # Byte method
        if a.dataMethod == "-s":
            byteStorage(a) # Store
        elif a.dataMethod == "-r":
            byteExtraction(a)#Extract
    
    
    
      




