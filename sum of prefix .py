N=int(raw_input())
a=list(map(int,(raw_input()).split()))
b=[a[0]]
for i in range(2,N+1) :
    b.append(sum(a[:i]))
print(" ".join([str(i) for i in b]))
