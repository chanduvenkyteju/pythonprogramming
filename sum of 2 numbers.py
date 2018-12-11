N,X=map(int,(raw_input()).split())
l=input().split()
z=0
for i in range(0,len(l)):
    c=0
    if(i==len(l)-1):
        c=int(l[0])+int(l[i])
    else:
        c=int(l[i])+int(l[i+1])
    if(c==X):
        z=z+1
if(z>0):
    print("yes")
else:
    print("no")
