N,K=(raw_input()).split()
N=int(N)
K=int(K)
a=[]
b=[]
for i in range(0,N):
    a.append(int(raw_input()))
for i in range(0,N):
    if(a[i]%2!=0):
        b.append(a[i])
c=(' '.join(map(str,b)))
print(c[K])
