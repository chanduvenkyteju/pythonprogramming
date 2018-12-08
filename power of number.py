N,K=map(int,(raw_input()).split())
c=0
for i in range(1,N+1):
    if(N==(K**i)):
        c=c+1
        break
if(c==1):
    print("yes")
else:
    print("no")
