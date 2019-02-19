n=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=list(map(int,(raw_input()).split()))
c=1
for i in range(n-1):
    for j in range(i+1,n):
        if(a[j]>=b[i]):
            i=j
            c=c+1
            break
    if(i==n-1):
        break
print(c)
