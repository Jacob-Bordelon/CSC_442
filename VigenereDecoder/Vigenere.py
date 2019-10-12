import sys

# Jacob, Bruno, Eboni, JonMichael, Logan, Tyler
# Github: https://github.com/Jacob-Bordelon/CSC_442.git

# Use python2.7

# Terminal: python Vigenere.py [-e,-d] [key] (<>) [name_of_text_file]
# Ex: python Vigenere.py -e mykey
# enter the message

# encryption method:
# you're given a key and a message
# Ex: message = "This is the Message", key = "Lemon"
# the case of the key does not matter, but the case of the message does
# Steps:
#   1) Line up the message and the key (ignoring spaces and separating letters)
#       Ex: [T,h,i,s,i,s,t,h,e,M,e,s,s,a,g,e]
#           [L,e,m,o,n,L,e,m,o,n,L,e,m,o,n,L]
#               The key should be repeated until it reaches the length of the message, ignoring spaces
#               This can be done with math
#                   the letter lining up is the index of the message mod length of key (i.e key[i%len(key)])
#   2) Compare the values to the viginare table 
#       This can be simplified with math
#       take the value of the message letter (i.e A = 0, B = 1), add it to the value of the aligning key letter (A+B = 0+1 = 1)
#       Then take the mod of 26 to that value (A+B%26 = 1) the value returned is the index of the alphabet so (A+B%26=B)
#   3) Now do that for each letter in the message, keeping track of uppercase and lower case in the message          

# Decryption:
# its the exact same as encryption only instead of adding the two value of the message and key
# we're subtracting: (ie. A-B%26 = new letter ) 

# get the table value of the combined letters
def getAlphabet(message,key,mode):
    # checks if the character is a letter
    if message.isalpha() == False:
        return message
    
    # encrypt the message
    if(mode == "-e"):
        value = (ord(message.upper()) + ord(key.upper()))%26
        if message.isupper() :
            return chr(value+65).upper()
        else:
            return chr(value+65).lower()
    else:
        # decrypt the message
        value = (ord(message.upper()) - ord(key.upper()))%26
        if message.isupper() :
            return chr(value+65).upper()
        else:
            return chr(value+65).lower()

#encypt/decrypt the message
def crypt(message, key, mode):
    a = 0
    result = ""
    for i in range(len(message)):
        # check for spaces
        if(not message[i].isalpha()):
            result+=str(message[i])
        else:
            # will either encrypt or decrypt the message based on the mode
            result += getAlphabet(message[i],key[a%len(key)],mode)
            a+=1
    return result


# Main

# check for user input errors 
if len(sys.argv) < 3:
    if len(sys.argv) == 1:
        print "mode not present"
    if len(sys.argv) == 2:
        print "key not present"
    quit(0)


mode = sys.argv[1]
key = sys.argv[2].replace(' ','')



if mode not in ['-e','-d']:
    final = "Mode not recognized \nPlease use either -e (encryption) or -d (decryption)\n"
    sys.stdout.write(final)
    quit(0)



# uses stdin and stdout to read and write from the program
# use ^D (EOF) to break out of the terminal
while(True):
    message = sys.stdin.readline()
    if message == '':
        break
    final = crypt(message, key, mode)
    sys.stdout.write(final)




