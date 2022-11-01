def stairs(n):
    for i in range(1,n+1):
        s=' '*(n-i)
        t='#'*i
        print(s+t)
        
if __name__=='__main__':
    n=int(input())
    stairs(n)
