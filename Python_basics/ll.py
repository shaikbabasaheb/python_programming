l=[10,20,30,40,100]
s=[str(ele) for ele in range(10) if ele%2!=0]
r=[]
for i in l:
    flag=0
    for j in s:
        if j in str(i):
            flag=1
            break
    if(flag==0):
        r.append(i)
print(r)
        

    
    
