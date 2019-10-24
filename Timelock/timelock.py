# File:     timelock.py
# Team:     THE ROMANS ->
#           Johnmichael Book, Jacob Bordelon, Tyler Nelson,
#           Logan Simmons, Eboni Williams, Breno Yamada Riquieri
# Version:  10.13.19
# Usage:    Use python 2.7
#           Example: python timelock.py < epoch.txt
# Github:   https://github.com/Jacob-Bordelon/CSC_442/blob/master/Timelock/timelock.py
# Descr:    This program reads the epoch from stdin in the format YYYY MM DD HH mm SS.
#           Then, it calculates the time elapsed (in second) between the current system
#           time and the epoch time. From this, a 4-character code is calculated,
#           generated, and sent to stdout.
#
# NOTE: you may need to install pytz 
#======================================= IMPORT STATEMENTS =======================================#
from datetime import datetime, timedelta
from hashlib import md5
import pytz
import sys
#============================================ CLASSES ============================================#
# This class creates an object in Coordinated Universal Time (UTC) 
# based on the epoch time (January 1, 1970). 
class utcTime:
    # Constructs a new 'utcTime' object.
    # Given an inputted time in the format 'YY MM DD HH MM SS', this time 
    # is converted to a datetime instance with adjustments being made for
    # daylight savings time. The seconds elapsed since
    # January 1, 1970 are also calculated.
    def __init__(self,sInput):
        # convert to array for parsing
        self.input = [int(i) for i in sInput.split(' ')]
        # create the date time instance with the input
        self.utc = datetime(self.input[0],self.input[1],self.input[2],self.input[3],self.input[4],self.input[5]) 
        # make corrections for daylight savings time
        if self.dst() == True:
            self.utc = self.utc - timedelta(hours=1)
        # # give the seconds elapsed since January 1, 1970
        self.seconds = int((self.utc-datetime(1970, 1, 1)).total_seconds()) 
        # NOTE: this time thats elapsed is not the user inputed epoch time,
        #       but rather january 1 1970
        
    # This method tests the current time to determine whether
    # it is daylight savings time or not.
    def dst(self):
        localtime = pytz.timezone('US/Central')
        a = localtime.localize(self.utc)
        return bool(a.dst())

    # This method returns the amount of seconds elapsed since as an integer.
    def __int__(self):
        return self.seconds

    # This method returns the amount of seconds elapsed as a string. 
    def __str__(self):
        return str(self.seconds)
#============================================ METHODS ============================================#
# This method generates a 4-character code based on a given hash string.
# Given the hashed value, the first 2 letters as read from left to right
# and last 2 single digits as read from right to left to generate the
# code. In the case where there aren't at least 2 numbers, extra digits
# are grabbed to fill in the code. In teh case where there aren't at least
# 2 digits, extra letters are grabbed to fill the code. 
def fourBit(hashed):
    # separate the values of hashed into two groups, letters(l) or digits(d)
    # maintain the order of the letters but reverse the order of the digits
    d = [i for i in hashed if i.isdigit()][::-1] 
    l = [i for i in hashed if i.isalpha()]
        
    # If we have more than 2 digits AND more than 2 letters,
    # add the first two objects to the string and join the
    # the elements together into one string
    if len(d) >= 2 and len(l) >= 2: 
        return ''.join(l[:2]+d[:2])
    # if less than 2 digits exist, fill the missing digit(s)
    # with a character
    elif len(d) < 2:
        return ''.join(l[:4-len(d)]+d)
    # if less than 2 letters exist, fill the missing letter(s)
    # with a digit
    elif len(l) < 2:
        return ''.join(l+d[:4-len(l)])

#========================================= MAIN PROGRAM ==========================================#
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
    # this creates a datetime instance that is then converted to seconds 
    # since january 1 1970; it will also adjust for day light savings 
    # time, since it will need to subtrace an hour to adjust for the time difference
    epoch = utcTime(epochInput)
    current = utcTime(currentTime)

    # the elapsed time takes the difference in seconds between the
    # current time and epoch time
    elapsed = current.seconds - epoch.seconds  

    # After rounding the elapsed time to the minute (so a hash is generated each minute
    # not second), convert that time to a UTF-8 string. Then, get the hashed value of 
    # the elapsed time string. Once done, convert the characters in the string from
    # ASCII to UTF-8. Repeat this last step again. 
    hashed = md5(md5(str(elapsed-(elapsed%60)).encode()).hexdigest()).hexdigest()

    # give output through stdout
    sys.stdout.write(fourBit(hashed))
