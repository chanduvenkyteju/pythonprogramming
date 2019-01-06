N=int(raw_input())
a=list(map(int,(raw_input()).split()))
m=max(a)
for i in range(0,N):
    for j in range(i,N):
        if(a[i]<a[j]):
            a[i],a[j]=a[j],a[i]
for k in a:
    print(k)
