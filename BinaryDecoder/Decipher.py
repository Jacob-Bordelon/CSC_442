import sys


def convert(num,bitType):
    value = 0
    for i in range(len(num)):
        if(int(num[i])==1):
            value+=(2**((bitType-1)-i))
    
    if(bitType == 7):
        if value == 8:
            return ""
    return chr(value)

if(len(sys.argv)==1):
    print "ERROR: File Needed"
else:       
    #open file to get contents
    f = open("{}".format(sys.argv[1]),"r")
    contents = f.read()[:-1]
    f.close() 

    

    if(len(contents)%7==0):
        bitType=7
    else:
        bitType=8

    for i in range(0,len(contents),bitType):
        print convert(contents[i:i+bitType],bitType),

        
    


