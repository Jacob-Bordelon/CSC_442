import os
#ls -l covert | awk '{print$1}'

# Convet the binary into decimal/ characters
def convert(num,bitType):
    value = 0
    for index in range(len(num)):
        if(int(num[index])==1):
            value+= (2**((bitType-1)-index))
    return value

# change the file permissions format into binary
def change(x):
    arr = ""
    for i in x:
        if i == "-":
            arr+="0"
        else:
            arr+="1"
    return convert(arr,7)


# this line will export all the file permissions of every file (not filtering for traffic) and house it in the variable permissions
# os.popen executes whatever command is inputted, the read() funtion returns it as a string, 
# the [6:-1] removes the 'total' and '\n' that appears at the beggining and end of the command line
# and the replace() call takes all the instances of a break line and replaces them with a space
# giving you one solid line to work with
permissions = os.popen("ls -l | awk '{print$1}'").read()[6:-1].replace('\n',' ')

#brokenList parses through the permissions string and separates each one by the space between them
# returns a list
brokenList = list(permissions.split(" "))

# if the method is 7, then the safeList is needed. because you can only look at the 7 right most bits
# this returns another list of 7 bit file permission strings
safeList = [i[3:] for i in brokenList]

print change(safeList[0])




