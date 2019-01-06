N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[]
for i in range(1,N):
    c=0
    for j in range(i):
        if(a[i]>a[j]):
            c=c+a[j]
    b.append(c)
print(sum(b))
