import os
#ls -l covert | awk '{print$1}'

def convert(num,bitType):
    value = 0
    for index in range(len(num)):
        if(int(num[index])==1):
            value+= (2**((bitType-1)-index))
    return value

def change(x):
    arr = ""
    for i in x:
        if i == "-":
            arr+="0"
        else:
            arr+="1"
    return convert(arr,7)



n = os.popen("ls -l covert | awk '{print$1}'").read()[6:-1].replace('\n',' ')
p = list(n.split(" "))
safeList = [i[3:] for i in p]

print change(safeList[0])




