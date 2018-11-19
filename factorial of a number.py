p=int(input())
fact=1
if(p==0):
	print("1")
else:
	for i in range(1,p+1):
		fact=fact*i
	print(fact) 
