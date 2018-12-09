N=int(raw_input())
c=0
for i in range(1,N+1):
    if(N%i==0):
        c=c+1
if(c!=0):
    print("yes")
else:
    print("no")
