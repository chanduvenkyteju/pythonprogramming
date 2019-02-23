s=(raw_input())
a=[]
b=""
for i in s:
	if s.count(i)==1:
		a.append(i)
	else:
		a.append(i.upper())
for i in a:
	b=b+i
print(b)
