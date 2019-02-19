N=int(raw_input())
s=0
for i in range(2,N+1):
    if(i%2!=0 and i%10==3):
        s=s+i
print(s)
