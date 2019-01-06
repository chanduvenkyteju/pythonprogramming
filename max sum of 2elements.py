N=int(raw_input())
a=list(map(int,(raw_input()).split()))
s=0
c=[]
for i in a:
    for j in range(i+1,N):
        s=a[i]+a[j]
        c.append(s)
print(max(c))
