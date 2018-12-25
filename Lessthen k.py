N,K=(raw_input()).split()
N=int(N)
K=int(K)
a=(raw_input()).split()
b=[]
for i in range(0,N):
    if(int(a[i])<K):
        b.append(a[i])
b=sorted(b)
print(" ".join(b)) 
