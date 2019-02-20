n,m=map(int,(raw_input()).split())
c=0
while(n<2):
    n=n+1
for i in range(n,m):
    s=0
    while(i!=0):
        a=int(i%10)
        s=s+a
        i=int(i/10)
    if(s>=2):
        for j in range(2,s):
            if(s%j==0):
                break
        else:
            c=c+1
print(c)
