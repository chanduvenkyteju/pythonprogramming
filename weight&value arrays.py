n,w=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
b=list(map(int,(raw_input()).split()))
d=[]
c=0
for i in range(n):
    x=b[i]/a[i]
    d.append(x)
while w>=0 and len(d)>0:
    mindex=d.index(max(d))
    if w>=a[mindex]:
        c=c+b[mindex]
        w=w-a[mindex]
    a.pop(mindex)
    b.pop(mindex)
    d.pop(mindex)
print(c)
