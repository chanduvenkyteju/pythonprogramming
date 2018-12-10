N,K=((raw_input()).split())
c=0
for i in N:
    for j in K:
        if(i==j):
            c=c+1
        else:
            c=c
if(c>0):
    print("yes")
else:
    print("no")
