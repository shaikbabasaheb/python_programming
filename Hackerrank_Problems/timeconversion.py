def conversionTime(t):
    mer=t[-2:]
    
    if(mer=='PM' and int(t[:2])!=12):
        t=str(int(t[:2])+12)+t[2:]
        
    if(mer=='AM' and int(t[:2])==12 ):
        t='00'+t[2:]

    return t[:-2]
    
if __name__=='__main__':
    t=input() #hh:mm:ssZZ
    print(conversionTime(t))
    
