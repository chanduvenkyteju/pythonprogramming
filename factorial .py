z=int(raw_input())
f=1
if(z==0):
	print("1")
else:
	for i in range(1,z+1):
		f=f*i
	print(f)
