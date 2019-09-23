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
result = ""

# This function converts the list of 7 or 8 binary strings
# first, it iterates through the string, checking for 1's
# if it finds a 1, it adds a 2 to the power of the bitType(7 or 8) - 1 - index 
# this way, its able to raise it to the appropriate power based on its current index
# it then checks for a value of 8 (the back space), if found it will input [bs]
# the function chr(), takes in a decimal value and converts it to ascii
def convert(num,bitType):
    value = 0
    for index in range(len(num)):
        if(int(num[index])==1):
            value+=(2**((bitType-1)-index))
    # required to handle backspace at end of line
    if value == 8: 
        return "[bs]"
    return chr(value)

    
#this is the standard input
# the [:-1] is to eliminate the '/n' at the end of the string
contents = sys.stdin.read()[:-1]

# checks for the bitType by checking if the remainder contents devided by 7 is 0
# if it is, we have a 7 bit binary sequence
# if not, its gotta be an 8 bit
# Note: This can be adjusted if needed 
if(len(contents)%7==0):
    #finally, iterate through the entire file until the resulted output is complete
    # just a simple for-loop, breaking up the string into the bitType size and iterateing 
    # through it by that value
    # the output is collected in result 
    for i in range(0,len(contents),7):
        result+= convert(contents[i:i+7],7)
if(len(contents)%8==0):
    # if result isn't empty make a new line
    # check if this is okay
    result += ("\n" + "="*25 + "\n") if (result != "") else ""
    for i in range(0,len(contents),8):
        result+= convert(contents[i:i+8],8)


# if the backspace key exists in the final result remove it
# user a while loop to get every instance of backspace
while "[bs]" in result:
    erase = result.index("[bs]")
    result = result[0:erase-1:] + result[erase+4::]

print result


    
    


