# File:     timelock.py
# Team:     Johnmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  10.13.19
# Usage:    Use python 2.7
#           Example: python timelock.py < epoch.txt
# Github:   https://github.com/Jacob-Bordelon/CSC_442.git
# Descr:    This program
#           Reads the epoch from stdin in the format YYYY MM DD HH mm SS
#           Use the systems current time to calculate the elloted time of epoch and current
#           and sends the calculated 4-character code to stdout.
#
# NOTE: you may need to install pytz 

from datetime import datetime, timedelta
from hashlib import md5
import pytz
import sys


# This class creates an element dubbed utcTime
# upon instance, it will take a string as input, given the format 'year month day hour minute second'
# it will then create a datetime instance to convert the current time - epoch time in seconds
# if utcTime is printed, it will return the seconds elapsed since january 1 1970
# the dst function adjusts the time for day light savings time so when the time is caluculated, its accurate
class utcTime:
    def __init__(self,sInput):
        self.input = [int(i) for i in sInput.split(' ')] # convert the string to an array by spaces
        self.utc = datetime(self.input[0],self.input[1],self.input[2],self.input[3],self.input[4],self.input[5]) # create the date time instance with the input
        if self.dst() == True: # test for daylight savings time
            self.utc = self.utc - timedelta(hours=1) # change if so
        self.seconds = int((self.utc-datetime(1970, 1, 1)).total_seconds()) # give the seconds elapsed since the begining
        # NOTE: this time thats elapsed is not the user inputed epoch time, but rather january 1 1970
        
    # test for daylight savings time 
    def dst(self):
        localtime = pytz.timezone('US/Central')
        a = localtime.localize(self.utc)
        return bool(a.dst())

    # return the integer of seconds so it can be calculated
    def __int__(self):
        return self.seconds

    # print out the elapsed seconds
    def __str__(self):
        return str(self.seconds)

# convert the hashed value to a 4 bit string
# of first 2 letters and last 3 digits
# NOTE: This checks for if there are no letters or numbers and will return the appropriate output
def fourBit(hashed):
    # separate the values of hashed into two groups, letters(l) or digits(d)
    # separate the values but maintain order
    # reverse the order of the digits
    d = [i for i in hashed if i.isdigit()][::-1] 
    l = [i for i in hashed if i.isalpha()]

    
    # if it reads both lists are over 2 values each, then add the first two objects to the string
    # this works since the d list is already reversed, so, it will be in proper order
    # lastly, join all the elements together into one string
    if len(d) >= 2 and len(l) >= 2: 
        return ''.join(l[:2]+d[:2])
    elif len(d) < 2: # if only 1 or no digits exist, append what is there to the end of 3 to 4 characters of l
        return ''.join(l[:4-len(d)]+d)
    elif len(l) < 2:# # if only 1 or no letters exist, append what is there to the begging of 3 to 4 characters of d
        return ''.join(l+d[:4-len(l)])
    
if __name__ == "__main__":
    # Get the epoch time from stdin
    epochInput = sys.stdin.read()

    # get the current system time
    # NOTE Change c to change the current time
    #/////////////////////////////////////////////////////////
    currentTime = datetime.now().strftime("%Y %m %d %H %M %S") # use for normal timelock.py
    # c = open('current.txt','r').read() #use for test.py
    # c = "2017 04 23 18 02 30" # use for testing
    #/////////////////////////////////////////////////////////


    # Create a utcTime element of both epoch and current 
    # this creates a datetime instance that is then converted to seconds since january 1 1970
    # it will also adjust for day light savings time, since it will need to subtrace an hour to adjust for the time difference
    epoch = utcTime(epochInput)
    current = utcTime(currentTime)

    # the elapsed time takes the current seconds in utc and 
    elapsed = current.seconds - epoch.seconds  

    # this line is md5 of an md5 of the starting time. 
    # NOTE: elapsed - elapsed%60 is giving the exact time at the begging of the minute rather than the end
    # cause it will affect the output
    hashed = md5(md5(str(elapsed-(elapsed%60)).encode()).hexdigest()).hexdigest()

    # give output through stdout
    sys.stdout.write(fourBit(hashed))
