N=int(raw_input())
a=list(map(int,(raw_input()).split()))
k=max(a)
for i in range(0,N-1):
    for j in range(i+1,N):
        if((a[i]+a[j]==0) or (a[i]+a[j]<k)):
            print(a[i],a[j])
            break
    break
