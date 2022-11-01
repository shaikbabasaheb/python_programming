def applesorangesOnHome(s,t,a,b,m,n,apples,oranges):
    acount=ocount=0
    for i in apples:
        if s<= a+i <=t:
            acount+=1
    for j in oranges:
        if s<= b+j <=t:
            ocount+=1
    return [acount,ocount]
    
if __name__=='__main__':
    s=int(input())
    t=int(input())
    a=int(input())
    b=int(input())
    m=int(input())
    n=int(input())
    apples=[]
    oranges=[]
    for _ in range(m):
        val=int(input())
        apples.append(val)
    for _ in range(n):
        val=int(input())
        oranges.append(val)
    print(applesorangesOnHome(s,t,a,b,m,n,apples,oranges))
        
