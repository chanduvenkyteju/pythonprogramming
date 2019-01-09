N,M=map(int,(raw_input()).split())
if(M>N):
    s=M
else:
    s=N
for i in range(1,s+1):
    if(M%i==0 and N%i==0):
        gcd=i
print(gcd) 
