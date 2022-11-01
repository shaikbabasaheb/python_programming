def kangaroo(x1,v1,x2,v2):
    if(x1<x2 and v1<v2):
        return 'NO'
    for i in range(1,10000):
        if ((i*v1)+x1)%((i*v2)+x2)==0:
            return 'YES'
    else:
        return 'NO'

    ''' if v1!=v2 and (x2-x1)%(v2-v1)==0:
        return 'YES'
    else:
        return 'NO'
    '''
    
if __name__=='__main__':
    x1=int(input())
    v1=int(input())
    x2=int(input())
    v2=int(input())
    print(kangaroo(x1,v1,x2,v2))
