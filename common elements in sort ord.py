N,M=(raw_input()).split()
N,M=int(N),int(M)
a=list(map(int,(raw_input()).split()))
k=[]
b=[]
c=a[:N]
d=a[N:]
for i in c:
    if(i in d):
        b.append(i)
for i in b:        
    if (i not in k):
        k.append(i)
k=sorted(k)        
print(" ".join([str(i) for i in k]))
