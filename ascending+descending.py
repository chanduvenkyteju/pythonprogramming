n,k=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
b=[]
c=[]
for i in range(0,k):
    b.append(a[i])
b.sort()    
for i in range(k,n):
    c.append(a[i])
c=c[::-1]
for j in range(0,len(c)):
    b.append(c[j])
print(" ".join(str(i) for i in b))
