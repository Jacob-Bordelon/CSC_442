# File:     Binary.py
# Team:     Johnmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  09.23.19
# Usage:    Use python 2.7
#           Example: python Binary.py < test1.txt
# Github:   https://github.com/Jacob-Bordelon/CSC_442.git
# Descr:    This program reads from a text file containing a sequence
#           of binary digits, in either 7- or 8-bit. It then decodes
#           the file into readable ouptut for the user.

import sys


# This function converts the list of 7 or 8 binary strings
# first, it iterates through the string, checking for 1's
# if it finds a 1, it adds a 2 to the power of the bitType(7 or 8) - 1 - index 
# this way, its able to raise it to the appropriate power based on its current index
# it then checks for a value of 8 (the back space), if found it will input [bs]
# the function chr(), takes in a decimal value and converts it to ascii
def convert(num):
    value = 0
    for i in range(len(num)):
        if int(num[i]) == 1:
            value += 2**(len(num)-1-i)
    return chr(value)


    
# this is the standard input
# sometimes, the file has a EOF or \n character at the end, it will remove it if so
contents = sys.stdin.read().replace('\n','')



# This try/execpt test tests if the file has a character that isnt in the ascii 
# table. If a character doesnt exist, it makes the assumption that its the wrong bit type
# using a for loop, it concatinates the characters together into a single string.
# if the result.decode() returns an error, that means a character that appeared shoundt be there 
# so, it swaps its bit types and starts over
try: 
    bitType = 8
    result = ""
    for i in range(0,len(contents),bitType):
        result += convert(contents[i:i+bitType])
        result.decode('ascii') 
except UnicodeDecodeError:
    bitType = 7
    result = ""
    for i in range(0,len(contents),bitType):
        result += convert(contents[i:i+bitType])
   

# return the result
print result

    


