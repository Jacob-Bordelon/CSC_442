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
    def __init__(self,args):
        self.bitMethod = '-b' if args.bit == True else '-B'
        self.dataMethod = '-s' if args.store == True else "-r"
        self.interval = args.interval
        self.offset = int(args.offset)
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
    W = File.wrapper

    while o < len(W):
        b = W[o]
        if b in S:
            pass
        else:
            H+=b
        o+=I
    stdout.write(H)


def byteStorage(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden
    W = File.wrapper

    


# Bit Method
def bitExtraction(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = bytearray()
    W = File.wrapper
    

  
   



def bitStorage(File):
    o = File.offset
    I = File.interval
    S = File.sentinal
    H = File.hidden
    W = File.wrapper
       


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
    
    
      




