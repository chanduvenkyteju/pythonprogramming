N,K=(raw_input()).split()
N=int(N)
K=int(K)
O=list(str(N))
while K>0:
    K=K-1
    del(O[K])
print(''.join(O))
