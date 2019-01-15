N=int(raw_input())
a=list(map(int,(raw_input()).split()))
K=N//2
b=sorted(a[:K])
c=sorted(a[K:])
d=c[::-1]
M=b+d
print(" ".join(str(i) for i in (M)))
