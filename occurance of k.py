N,K=map(int,input().split())
c=0
while(N!=0):
    p=N%10
    if(p==K):
        c=c+1
    N=int(N/10)
print(c)
