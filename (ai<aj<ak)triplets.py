N=int(raw_input())
c=0
a=list(map(int,input().split()))
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if(a[i]<a[j]<a[k]):
                c=c+1
print(c)
