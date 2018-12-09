N=int(raw_input())
M=[]
for i in range(1,N+1):
    if(N%i==0 and i%2!=0):
        M.append(i)
s=" ".join(map(str,M))
print(s)
