N,P,Q,R=map(int,(raw_input()).split())
l=list(map(int,(raw_input()).split()))
g=[]
for i in range(0,len(l)):
	for j in range(0,len(l)):
		for k in range(0,len(l)):
			if i<=j<=k:
				f=P*l[i]+Q*l[j]+R*l[k]
				g.append(f)
print(max(g))
