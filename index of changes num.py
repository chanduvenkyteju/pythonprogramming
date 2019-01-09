N=int(raw_input())
a=list(map(int,(raw_input()).split()))
K=sorted(a)
for i in range(0,N):
    if(a[i]!=K[i]):
        print(a.index(a[i]))
        break
