N=int(raw_input())
a=(raw_input()).split()
b=[]
for i in range(0,len(a)):
	if i%2==0:
		a[i]=int(a[i])
		if a[i]%2!=0:
			b.append(a[i])
	else:
		a[i]=int(a[i])
		if a[i]%2==0:
			b.append(a[i])
s=' '.join(map(str,b))
print(s)
