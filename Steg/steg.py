from sys import stdin, stdout
import argparse
from math import floor

# CONSTANTS
# SENTINEL = bytearray([0x0,0xff,0x0,0x0,0xff,0x0])

######PROBABLY NEED PARAMERTER FOR BIT DATA STORAGE DIRECTION
### FOR ASSIGNMENT, LEFT TO RIGHT
### FOR CYBERSTORM, RIGHT TO LEFT
#########MAKE SURE TO CHECK FOR OUTPUT REDIRECTION
##### IF EITHER HIDDEN OR WRAPPER FILE IS NOT FOUND, PROVIDE ERROR MESSAGE
#### OUTPUT TO STDOUT AS BINARY DATE: SYS.STDOUT.BUFFER.WRITE IN PYTHON 3
# SPECIFY SENTINEL AT TOP OF ARRAY AS CONSTANT (FOR CHANGING LATER): STORE AS BINARY DATE USING BYTEARRAY

# Grab terminal parameters as flags
parser = argparse.ArgumentParser(prog='steg.py',conflict_handler="resolve")
parser.add_argument("-b","--bit", help="Use bit method",action='store_true')
parser.add_argument("-B","--byte", help="Use byte method", action="store_true")
parser.add_argument("-s","--store", help="Store (and hide) data", action="store_true")
parser.add_argument("-r","--retrieve", help="Retrieve hidden data", action="store_true")
parser.add_argument("-o","--offset",default=0,help="Set offset to <val>",type=int)
parser.add_argument("-i","--interval",default=1,help=" Set interval to <val>",type=int) ####optional
parser.add_argument("-w","--wrapper_file",help="Set wrapper file to <val>")
parser.add_argument("-h","--hidden_file",help="Set hidden file to <val>") ### optional
args = parser.parse_args()


# check and organize parameters 
class params:
    def __init__(self,args):
        self.bitMethod = '-b' if args.bit == True else '-B' #### what happens if enter wrong thing, needs to be handled
        self.dataMethod = '-s' if args.store == True else "-r"
        self.interval = args.interval
        self.offset = int(args.offset)
        # note:these are strings
        self.wrapper = open(args.wrapper_file,'rb').read() if args.wrapper_file != None else None
        self.hidden = open(args.hidden_file,'rb').read() if args.hidden_file != None else None
        self.sentinal = "0x0 0xff 0x0 0x0 0xff 0x0".split(' ')
    
    def calculateInterval(self):
        return floor((len(self.wrapper)-self.offset)/(len(self.hidden)+len(self.sentinal)))

    def minWrapperSize(self):
        return len(self.hidden)*self.interval + self.offset

    def maxHiddenSize(self):
        return floor((len(self.wrapper) - self.offset - len(self.sentinal))/self.interval)

# Byte Method
def byteExtraction(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = bytearray()
    W = File.wrapper # in bytes

    while o < len(W):
        b = W[o]
        if b in S:
            pass
        else: #may need to add matched partial sentinel bytes first
            H+=b
        o+=I
    stdout.write(H)

def byteStorage(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden # in bytes
    W = File.wrapper # in bytes
    #i <- 0
    # while i < length(H)
        #W[offset] <- H{i}
        #offset += interval
        # i += 1
    #i=0
    #while i<length(S)
        #W[offset] <- S[i]
        #offset += interval
        # i+=1

# Bit Method
def bitExtraction(File):
    o = File.offset
    I = File.interval
    # convert from bytes to bits
    H = [format(i,'b') for i in bytearray()]
    W = [format(i, 'b') for i in File.wrapper]

    while( o < len(W)):
        b = 0
        for j in range(7):
            b = bitOr(b,bitAnd(W[o],"00000001"))
            if j < 7:
                b = leftShift(b,1)
                o += I
        H += b
        o += I

def bitStorage(File):
    offset = File.offset
    interval = File.interval
    # convert from bytes to bits
    sentinel = [format(i,'b') for i in File.sentinal]
    hidden = [format(i,'b') for i in File.hidden]
    wrapper = [format(i,'b') for i in File.wrapper]

    byte = 0
    while(byte < len(hidden)):
        for bit in range(7):
            wrapper[offset] = bitAnd(wrapper[offset],"11111110")
            wrapper[offset] = bitOr(wrapper[offset],rightShift(bitAnd(hidden[byte],"10000000"),7))
            hidden[interval] = leftShift(hidden[byte],1)
            offset += interval
        byte += 1
    biny = 0
    while(biny < len(sentinel)):
        for ind in range(7):
            wrapper[offset] = bitAnd(wrapper[offset],"11111110")
            wrapper[offset] = bitOr(wrapper[offset],rightShift(bitAnd(sentinel[biny],"10000000"),7))
            sentinel[biny] = leftShift(sentinel[biny],1)
            offset += interval
        biny += 1

# for shifts make sure to handle if not 8 bits;
# takes in a string and a number
# returns a string
def rightShift(binary, shift):
    result = binary
    s = 0
    while (s < shift):
        for bit in range(len(result)-1,0):
            result[bit] = result[bit-1]
        result[0] = "0"
        shift += 1
    return result

def leftShift(binary, shift, length=8):
    result = binary
    s = 0
    while (s < shift):
        for bit in range(len(result)-1):
            result[bit] = result[bit+1]
        result[len(result)-1] = "0" 
        shift += 1
    return bitAnd(result,bin(2*length-1)) #prevent larger than 1 byte

# takes in 2 strings
def bitAnd(op1, op2):
    # Make sure same length, otherwise add 0's to beginning
    diff = len(op1) - len(op2)
    if(diff < 0):# op2 is bigger
        op1 = ""*abs(diff) + op1
    elif(diff > 0): #op1 is bigger
        op2 = ""*diff + op2

    result = ["" for x in range(len(op1))]
    for bit in range(len(result)):
        if((op1[bit] == "0") or (op2[bit] == "0")):
            result[bit] = "0"
        else:
            result[bit] = "1"
    return result

# takes in 2 strings
def bitOr(op1, op2):
    # Make sure same length, otherwise add 0's to beginning
    diff = len(op1) - len(op2)
    if(diff < 0):# op2 is bigger
        op1 = ""*abs(diff) + op1
    elif(diff > 0): #op1 is bigger
        op2 = ""*diff + op2
    
    result = ["" for x in range(len(op1))]
    for bit in range(len(result)):
        if((op1[bit] == "1") or (op2[bit] == "1")):
            result[bit]  = "1"
        else:
            result[bit] = "0"
    return result

if __name__ == "__main__":
    a = params(args)
    if a.bitMethod == "-b":
        if a.dataMethod == "-s":
            pass
        else:
            bitExtraction(a)
    else:
        if a.dataMethod == "-s":
            pass
        else:
            byteExtraction(a)
    
    
      




