N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in range(0,N):
    if(int(a[i])<N):
        b.append(a[i])
b=sorted(b)
print(" ".join(b))
