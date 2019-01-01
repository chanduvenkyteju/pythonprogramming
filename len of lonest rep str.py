N=int(raw_input())
a=list(map(int,(raw_input()).split()))
c=0
b=[]
for i in range(0,len(a)-1):
	if int(a[i+1])>=int(a[i]):
		c=c+1
	else:
		b.append(c)
		c=0
print(max(b)+1)
