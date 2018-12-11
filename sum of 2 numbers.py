N,X=map(int,(raw_input()).split())
a=input().split()
z=0
for i in range(0,len(a)):
    c=0
    if(i==len(a)-1):
        c=int(a[0])+int(a[i])
    else:
        c=int(a[i])+int(a[i+1])
    if(c==X):
        z=z+1
if(z>0):
    print("yes")
else:
    print("no")
