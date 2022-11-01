def minpluszero(arr):
    pcount=0
    ncount=0
    zcount=0
    n=len(arr)
    for i in arr:
        if(i>0):
            pcount+=1
        elif(i<0):
            ncount+=1
        else:
            zcount+=1
    return (pcount/n, ncount/n, zcount/n)

if __name__=='__main__':
    arr=list(map(int,input().rstrip().split()))
    print(minpluszero(arr))
