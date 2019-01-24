N,l,r=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
b=[]
for i in range(l-1,r):
    b.append(a[i])
print(min(b))
