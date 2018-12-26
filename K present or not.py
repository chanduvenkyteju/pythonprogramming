N,K=(raw_input().split())
N=int(N)
K=int(K)
a=(raw_input()).split()
for i in range(0,N):
    if(int(a[i])==K):
        print("yes")
        break
    else:
        print("no")
