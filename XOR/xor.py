import sys
from binascii import unhexlify

# you need to convert the non characters into binary values
# this is done by taking the decimal value of the each indivual character, converting that to binary (line 10)
# since we want the string to maintain its length, we extend the length of each bit so it matches 8 bits (line 11)
# after the character has been converted, combine the binary string into one massive integer array to save 
# from having to convert later on
def convertToBits(string):
    result = []
    for c in string:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

# The xor operation works very simply, when comparing just two bits. since youre only comparing two bits
# theres only 4 possiblities the conversion can be. either they match or they dont
# a dictionary of the 4 values saves spaces and looks cleaner than a line of if statements
# the function takes two bytes (a,b) and searches for it in the dictionary. if the bits match, the dictionary returns
# a zero. if they dont match, it returns a 1
def xor(a,b):
    dictionary={(0,0):0,(1,1):0,(0,1):1,(1,0):1}
    return dictionary[(a,b)]

# convert the binary bits to ascii characters
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




# the key wont be passed as an argument, it will exist in the same directory as the function
# so, we need to open up the file and read its contents. passing them as the file variable 'key'
key = open('key', 'r').read()

# the plain/cipher text is to be taken as a paramenter, so we need to read it from standard input
text = sys.stdin.read()



# Once we have our documents, we need to convert the documents to binary strings, making sure they have
# they same length even after theyve been converted.
# we lable these as binaryKey and binaryText, or bKey and bText for short
bText = convertToBits(text)
bKey = convertToBits(key)




# now iterate through the bKey and bText, xor'ing each binary bit, and adding the output to the result
# variable

result = ""
for i in range(len(bKey)):
    result+=str(xor(bKey[i],bText[i]))



# lastly, print out the result

# NOTE this will return the binary string, we need to pass it through the binary.py converter

print toASCII(result)




