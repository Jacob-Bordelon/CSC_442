from sys import stdin, stdout
import argparse
from math import floor

# Grab terminal parameters as flags
parser = argparse.ArgumentParser(prog='steg.py',conflict_handler="resolve")
parser.add_argument("-b","--bit", help="Use bit method",action='store_true')
parser.add_argument("-B","--byte", help="Use byte method", action="store_true")
parser.add_argument("-s","--store", help="Store (and hide) data", action="store_true")
parser.add_argument("-r","--retrieve", help="Retrieve hidden data", action="store_true")
parser.add_argument("-o","--offset",help="Set offset to <val>",type=int)
parser.add_argument("-i","--interval",default=1,help=" Set interval to <val>",type=int)
parser.add_argument("-w","--wrapper_file",help="Set wrapper file to <val>")
parser.add_argument("-h","--hidden_file",help="Set hidden file to <val>")
args = parser.parse_args()


# check and organize parameters 
class params:
    def __init__(self,args,sentinal):
        self.bitMethod = '-b' if args.bit == True else '-B'
        self.dataMethod = '-s' if args.store == True else "-r"
        self.interval = args.interval
        self.offset = int(args.offset)
        self.wrapper = bytearray(open(args.wrapper_file,'rb').read()) if args.wrapper_file != None else bytearray()
        self.hidden = bytearray(open(args.hidden_file,'rb').read()) if args.hidden_file != None else bytearray()
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



# Byte Method

#Extract
def byteExtraction(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden
    W = File.wrapper
    
    while o < len(W):
        b = W[o]
        if b not in S:
            H+=bytes([b])
        o+=I
    stdout.buffer.write(H)
    

#Store
def byteStorage(File):
    o = File.offset
    I = File.interval
    S = [int(i,16) for i in File.sentinal]
    H = File.hidden
    W = File.wrapper

    # input in the Hidden bytes
    i=0
    while i < len(H):
        W[o] = H[i]
        o += I
        i+=1

    i=0
    # input in the sentinal
    while i < len(S):
        W[o] = S[i]
        o += I
        i +=1
        
    stdout.buffer.write(W)

    


# Bit Method

#Extract
def bitExtraction(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden
    W = File.wrapper


    
    while o < len(W):
        b = 0
        for j in range(8):  
            # this break check is needed incase the offset variable is greater than the list of bytes
            if o >= len(W):
                break
            b |= (W[o] & 1)
            if j < 7:
                b = (b<<1) & (2**8-1)
                o+=I
        if b not in S:
            H += bytes([b])
        o+=I
    stdout.buffer.write(H)
    

    
# Store
def bitStorage(File):
    o = File.offset
    I = File.interval
    S = [int(i,16) for i in File.sentinal]
    H = File.hidden
    W = File.wrapper

    # input in the hidden bits
    i = 0
    while i < len(H):
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
    stdout.buffer.write(W)
    

# ////////////////////[   MAIN   }///////////////////////////////////////
sentinal = "0x0 0xff 0x0 0x0 0xff 0x0" # change this value if the sentinal changes 


if __name__ == "__main__":
    
    a = params(args,sentinal) # first, create a params instance to organize data given from the flags

    # then using the bitMethod and Datamethod, determine which one youre using and call that particular function
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
    
    
    
      




