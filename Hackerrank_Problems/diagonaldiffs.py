def diagonaldiffs(arr):
    lsum=0
    rsum=0
    for i in range(len(arr)):
        lsum+=arr[i][i]
        rsum+=arr[i][len(arr)-i-1]

    print(lsum,rsum)
    return abs(lsum-rsum)

    
if __name__=='__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().rstrip().split())))
    print(diagonaldiffs(arr))
