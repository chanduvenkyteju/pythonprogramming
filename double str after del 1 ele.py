a=(raw_input())
if len(a)%2==1:
	i=len(a)//2
	x=a[:i]
	y=a[i+1:]
	if x==y:
		print("YES")
	else:
		print("NO")
else:
	print("NO")
