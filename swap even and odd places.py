n=str(raw_input())
a=[]
l=len(n)
i=0
while(i<l-1):
    a.append(n[i+1])
    a.append(n[i])
    i=i+2
if(l%2==0):
    print("".join(a))
else:
    a.append(n[l-1])
    print("".join(a))
    
