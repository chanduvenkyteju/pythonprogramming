N=int(raw_input())
M=str(raw_input())
O=str(raw_input())
a=[]
for i in range(0,len(M)):
    if(M[i]==O[i]):
        a.append(M[i])
c=''.join(a)
print(c)
