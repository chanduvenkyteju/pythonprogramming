N=int(raw_input())
a=list(map(int,(raw_input()).split()))
for i in range(0,N-1):
    for j in range(i+1,N):
        if(a[i]+a[j]==0):
            print(a[i],a[j])
            break
