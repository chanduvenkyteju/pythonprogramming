N,K=map(int,(raw_input()).split())
b=[]
c=[]
a=(raw_input()).split()
for i in range(0,N):
    if(a.count(a[i])<K):
        b.append(a[i])    
        while i in a:
            a.remove(i)
for i in b:            
    if(i not in c):
        c.append(i)
c=sorted(c)        
print(" ".join(c))
