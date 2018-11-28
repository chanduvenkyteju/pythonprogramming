N=int(raw_input())
i=1
while(i<=N):
    K=0
    if(N%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                K=K+1
            j=j+1
        if(K==2):
            print(i,end=(' '))
    i=i+1
