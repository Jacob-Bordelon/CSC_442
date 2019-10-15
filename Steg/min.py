def findMinMax(L):
    c = 0
    minv = maxv = L[0]

    for n in range(0,len(L),2):
        c+= 3
        if L[n-1] < L[n]:
            minv = minv if minv <= L[n-1] else L[n-1]
            maxv = maxv if maxv >= L[n] else L[n]

        else:
            minv = minv if minv <= L[n] else L[n]
            maxv = maxv if maxv >= L[n-1] else L[n-1]
        print c, 3*len(L)/2-2
        return minv, maxv