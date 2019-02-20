a=(raw_input())
b=[]
c=[]
a=a.lower()
for i in range(0,len(a)):
	for j in range(0,len(a)):
		z=a[i:j+1]
		y=z[::-1]
		if z==y:
			b.append(z)
for i in b:
	if len(i)>1:
		c.append(i)
c.sort(key=len)
for i in c:
	print(i)
