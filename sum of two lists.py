N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=list(map(int,(raw_input()).split()))
c=[]
for i in range(0,N):
    c.append(a[i]+b[i])
print(" ".join(str(i) for i in c))
