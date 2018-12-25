N,K=(raw_input().split())
N=int(N)
K=int(K)
a=(raw_input()).split()
b=[]
c=N-K
for i in range(0,c):
    b.append(a[i])
print(" ".join(b))  
