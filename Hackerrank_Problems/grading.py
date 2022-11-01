def grading(arr):
    res=[]
    for i in arr:
        if(i>=38):
            mod=i%5
            if(mod>=3):
                i+=5-mod
        res.append(i)
    print(res)
        
if __name__=='__main__':
    n=int(input().rstrip())
    arr=list(map(int,input().rstrip().split()))
    print(grading(arr))
