def maxcandles(arr):
    return arr.count(max(arr))

if __name__=='__main__':
    n=int(input().strip())
    arr=list(map(int,input().rstrip().split()))
    print(maxcandles(arr))
