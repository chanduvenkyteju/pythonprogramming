S=(raw_input())
e=[]
o=[]
for i in range(1,len(S)+1):
	if(i%2==0):
		e.append(S[i-1])
	else:
		o.append(S[i-1])
print("".join(str(i) for i in o) +" "+"".join(str(i) for i in e))
