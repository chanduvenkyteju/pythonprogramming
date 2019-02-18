N=int(raw_input())
c=0
a=list(map(int,(raw_input()).split()))
for i in range(0,N-1):
    for j in range(i+1,N):
        if(a[i]<a[j]):
            c=c+1
print(c)
