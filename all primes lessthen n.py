n=int(raw_input())
a=[]
for i in range(2,n):
    c=0
    for j in range(2,i):
	    if i%j==0:
                c=1
    if c==0:
	    a.append(i)
if a==[]:
    print("0")
else:
    print(" ".join(str(i) for i in a))
