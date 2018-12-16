N=int(raw_input())
a=(raw_input()).split()
k=[]
for i in range(0,len(a)):
	if i%2==0:
		a[i]=int(a[i])
		if a[i]%2!=0:
			k.append(a[i])
	else:
		a[i]=int(a[i])
		if a[i]%2==0:
			k.append(a[i])
s=' '.join(map(str,k))
print(s)
