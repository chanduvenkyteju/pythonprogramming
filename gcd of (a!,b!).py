def fact(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
n,m=map(int,(raw_input()).split())
p=min(m,n)
k=fact(p)
print(k)
