N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[]
for i in range(0,N) :
    b.append(sum(a[i:]))
print(" ".join(b))
