N,K=map(int,(raw_input()).split())
a=list(map(int,(raw_input()).split()))
c=0
for i in range(0,N):
    for j in range(i+1,N):
        if((a[i]-a[j])==K):
            c=c+1
        elif(a[j]-a[i]==K):
            c=c+1
        else:
            c=c
print(c) 
